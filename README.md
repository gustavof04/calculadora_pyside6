# Calculadora com <img src="https://www.pythonguis.com/images/libraries/pyside6.png" alt="pyside-img" width="100">

Interface gráfica de uma calculadora funcional feita em Python com a lib PySide6. Sendo meu segundo projeto utilizando libs de interface gráfica do Qt, percebi que em comparação com o PyQt5, não há tantas diferenças além das **políticas de licença distintas** entre as duas bibliotecas.

A calculadora possui as operações básicas de adição, substração, multiplicação e divisão. Entretanto, importando o módulo <code>math</code>, incluí a potenciação utilizando uma estrutura condicional e a função <code>.pow()</code>. Por fim, implementei um botão "C" (clear) para limpar a conta, um botão "◀" (backspace) para limpar o último número da conta e um botão N (negative) para converter os números da conta de positivos para negativos.

## 🔧 Tecnologias utilizadas
Python V.: 3.11.1 || PyQt5 V.: 6.5.1.1

OBS.: É obrigatória a instalação manual do Python na versão citada acima para ser possível a criação do ambiente virtual e instalação das dependências do projeto.

- Windows 8+

https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe

- macOS 10.9+

https://www.python.org/ftp/python/3.11.1/python-3.11.1-macos11.pkg

## ⚙️ Configurando o ambiente virtual
* No seu terminal, navegue até a pasta raiz do projeto e execute o seguinte comando para criar um ambiente virtual:

  <code>python -m venv nome_da_virtualenv</code> (exemplo: venv)

* Rode o comando de acordo com seu sistema para ativar seu ambiente virtual:

  <code>.\nome_da_virtualenv\Scripts\activate</code> (Windows)

  <code>source nome_da_virtualenv/bin/activate</code> (Linux ou macOS)

## 🧑‍🔬 Instalando as dependências
* Com o ambiente virtual **ativado**, instale as dependências do projeto com o seguinte comando:

  <code>pip install -r requirements.txt</code>

## 📂 Abrindo o projeto
* Execute o arquivo principal da lista conforme abaixo:

  <code>python main.py</code>
