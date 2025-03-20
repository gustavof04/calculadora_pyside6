# Calculator with PySide6

Graphical interface of a functional calculator made in Python with the PySide6 library.

The calculator has the basic operations of addition, subtraction, multiplication, and division. However, by importing the <code>math</code> module, I included exponentiation using a conditional structure and the <code>.pow()</code> function. Finally, I implemented a "C" (clear) button to clear the calculation, a "◀" (backspace) button to clear the last number in the calculation, and an "N" (negative) button to convert the numbers in the calculation from positive to negative.

> Project Status: ✔️ (completed)

## 🔧 Technologies Used
Python V.: 3.11.1 || PySide V.: 6.5.1.1

## ⚙️ Setting Up the Virtual Environment
* In your terminal, navigate to the project's root folder and run the following command to create a virtual environment:

  ```bash
  python -m venv name_of_virtualenv
  ```

* Run the command according to your system to activate your virtual environment:

  **Windows**
  ```bash
  .\name_of_virtualenv\Scripts\activate
  ```
  
  **Linux or macOS**
  ```bash
  source name_of_virtualenv/bin/activate
  ```

## 🧑‍🔬 Installing Dependencies
* With the virtual environment **activated**, install the project dependencies with the following command:
  
  ```bash
  pip install -r requirements.txt
  ```

## 📂 Opening the Project
* Run the main file from the list as follows:

  ```bash
  python main.py
  ```
