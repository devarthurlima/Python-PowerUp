# Automação de Cadastro (Python PowerUp)

Este é um projeto prático de Automação de Processos Robóticos (RPA) desenvolvido em Python. O script automatiza o login em um sistema web, lê uma base de dados local em formato `.csv` e realiza o preenchimento automático de todos os campos de formulário para cadastrar produtos em lote.

O projeto é ideal para demonstrar fundamentos de manipulação de dados com **Pandas** e automação de interface gráfica (GUI) com **PyAutoGUI**.

---

## 🚀 Funcionalidades

- **Abertura Automatizada:** Executa e acessa o navegador de internet (configurado para o Brave) de forma autônoma.
- **Autenticação Automática:** Preenche as credenciais de login e navega até a tela de cadastro do sistema.
- **Leitura de Base de Dados:** Extrai informações estruturadas de um arquivo CSV de forma rápida usando Pandas.
- **Preenchimento Inteligente (Looping):** Percorre linha por linha da planilha, inserindo dinamicamente dados como código, marca, tipo, categoria, preços e observações, lidando inclusive com valores nulos (`NaN`).
- **Controle de Tela:** Realiza rolagem automática de página (scroll) para garantir o alinhamento correto dos cliques a cada novo item cadastrado.

## 🛠️ Tecnologias e Bibliotecas Utilizadas

- **[Python](https://www.python.org/):** Linguagem base do projeto.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/):** Responsável pelo controle programático do mouse e teclado.
- **[Pandas](https://pandas.pydata.org/):** Utilizado para leitura, análise e estruturação de dados tabulares.

## 📋 Pré-requisitos

Antes de rodar o script, certifique-se de ter o Python instalado na sua máquina e instale as dependências necessárias executando o comando abaixo no terminal:

```bash
pip install pyautogui pandas

git clone https://github.com/devarthurlima/Python-PowerUp.git
```

💡 Créditos e Agradecimentos

Este projeto foi desenvolvido acompanhando as aulas práticas da Hashtag Treinamentos. O código foi reproduzido, estudado e adaptado por mim como parte do meu processo de aprendizado inicial em Python e automação.
