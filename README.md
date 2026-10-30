# SysDev - Sistema de cadastro de empresas

Aplicação desktop em Python + PySide6 (Qt) para cadastro e gerência de empresas a partir do CNPJ. O CNPJ é consultado na API da Receita Federal (ReceitaWS) para auto-preencher os campos, e os registros são persistidos em um banco MySQL local. O CRUD completo é feito direto na interface, com exportação dos registros para Excel.

![Tela principal](imgs/menu.png)

## Público-alvo

Ferramenta de uso voltada a **recrutadores e usuários técnico-operacionais**. Pressupõe que a pessoa saiba executar a aplicação pelo código-fonte e tenha um MySQL disponível. Por isso, mensagens de erro do banco e da API aparecem de forma direta na interface — não são "traduzidas".

## Requisitos

- Python 3.12+
- MySQL **8.0.16 ou superior** (as constraints `CHECK` usam `REGEXP`)
- Token gratuito da [ReceitaWS](https://receitaws.com.br/) para o auto-complete via CNPJ
- No Linux, as bibliotecas do Qt listadas em [Dependências do sistema](#dependências-do-sistema-linux)

## Dependências do sistema (Linux)

No Windows e no macOS o pacote do PySide6 já inclui as bibliotecas do Qt. No Linux não: a partir do **Qt 6.5** o plugin de plataforma `xcb` passou a exigir a `libxcb-cursor`, e sem ela a aplicação aborta na inicialização com:

```
qt.qpa.plugin: From 6.5.0, xcb-cursor0 or libxcb-cursor0 is needed to load the Qt xcb platform plugin.
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
```

**Ubuntu / Debian / Linux Mint:**

```bash
sudo apt update
sudo apt install libxcb-cursor0 libxkbcommon-x11-0 libxcb-icccm4 libxcb-image0 \
                 libxcb-keysyms1 libxcb-render-util0 libxcb-xinerama0 libxcb-shape0 \
                 libgl1 libglib2.0-0
```

**Fedora:**

```bash
sudo dnf install xcb-util-cursor libxkbcommon-x11 xcb-util-wm xcb-util-image \
                 xcb-util-keysyms xcb-util-renderutil mesa-libGL glib2
```

> Só a `libxcb-cursor0` é obrigatória para o erro acima; as demais entram na lista porque são dependências comuns do plugin `xcb` e evitam um segundo round de erro em instalações mínimas.

## Instalação

**Windows (PowerShell):**

```powershell
git clone https://github.com/cristianjuniorpena/ProjectPySide6.git
cd ProjectPySide6
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Linux / macOS:**

```bash
git clone https://github.com/cristianjuniorpena/ProjectPySide6.git
cd ProjectPySide6
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Dependências linux

Para linux pode ser necessário a instalação de alguns módulos:

- sudo apt update && sudo apt install python3-venv 
- sudo apt update && sudo apt install -y libxcb-cursor0 libxkbcommon-x11-0 libegl1

## Configuração (.env)

Copie o `.env.example` para `.env` e preencha os valores:

```powershell
Copy-Item .env.example .env
```

| Variável | Descrição | Exemplo |
|---|---|---|
| `DB_HOST` | Host do MySQL | `localhost` |
| `DB_PORT` | Porta do MySQL | `3306` |
| `DB_USER` | Usuário do banco | `root` |
| `DB_PASSWORD` | Senha do banco (vazio se não houver) | `` |
| `DB_NAME` | Nome do banco de dados | `empresas` |
| `RECEITAWS_TOKEN` | Token da ReceitaWS | `XXXXXXXX-XXXX-...` |

> O arquivo `.env` está no `.gitignore` e **nunca deve ser versionado**.

## Banco de dados

O nome da **tabela é fixo em `empresa`**. O nome do **banco** é definido por `DB_NAME` no `.env`.

Para criar o banco e a tabela automaticamente:

```powershell
.\venv\Scripts\python.exe init_db.py
```

Alternativamente, crie o banco manualmente e execute o `schema.sql` dentro dele. O schema cria a tabela `empresa`:

```sql
CREATE TABLE IF NOT EXISTS `empresa` (
  `cnpj` varchar(80) NOT NULL,
  `nome_empresa` varchar(80) DEFAULT NULL,
  `logradouro` varchar(80) DEFAULT NULL,
  `numero` varchar(80) DEFAULT NULL,
  `complemento` varchar(80) DEFAULT NULL,
  `bairro` varchar(80) DEFAULT NULL,
  `municipio` varchar(80) DEFAULT NULL,
  `uf` varchar(80) DEFAULT NULL,
  `cep` varchar(80) DEFAULT NULL,
  `telefone` varchar(80) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`cnpj`),
  CONSTRAINT `chk_cep` CHECK (cep REGEXP '^[0-9]{8}$'),
  CONSTRAINT `chk_cnpj` CHECK (cnpj REGEXP '^[0-9]{14}$'),
  CONSTRAINT `chk_uf` CHECK (uf REGEXP '^[A-Z]{2}$')
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

> Por segurança, prefira criar um usuário MySQL dedicado ao app (com permissões apenas no banco `empresas`) em vez de usar `root`.

## Como usar

1. Abra a aba **Cadastro**.
2. Digite o CNPJ — ao atingir 14 dígitos válidos, os demais campos são preenchidos automaticamente.
3. Clique em **Adicionar** para salvar no banco.
4. Na aba da tabela, edite uma célula e clique em **Alterar** para persistir; selecione uma linha e clique em **Excluir** para remover.
5. Clique em **Exportar Excel** para gerar o arquivo em `arquivosExcel/`.

## Estrutura do projeto

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Janela principal, eventos da UI e orquestração |
| `database.py` | Camada de acesso ao MySQL (CRUD) |
| `requisicoes.py` | Consulta de CNPJ na API da ReceitaWS |
| `excel.py` | Exportação para Excel (openpyxl) |
| `config.py` | Leitura e validação das variáveis do `.env` |
| `init_db.py` / `schema.sql` | Criação do banco e da tabela |
| `main_window.ui` / `ui_main.py` / `myrecursos_rc.py` | Interface gerada pelo Qt Designer |
| `imgs/` | Imagens usadas na interface |

## Limitações conhecidas

- A ReceitaWS limita o auto-complete a **3 requisições por minuto**.
- Requer um MySQL local configurado; se a conexão falhar, a interface avisa e mantém a tabela vazia.
- As constraints do banco exigem CNPJ (`14` dígitos), CEP (`8` dígitos) e UF (`2` letras maiúsculas).

## Licença

Projeto de uso didático e de portfólio.
