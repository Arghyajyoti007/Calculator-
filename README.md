# 🧮 Python Command-Line Calculator

A user-friendly command-line calculator built in Python that allows basic arithmetic operations like addition, subtraction, multiplication, and division. This calculator supports **continuous operations**, allowing you to perform chained calculations with previous results.

---

## 📌 Features

- Supports basic arithmetic: `+`, `-`, `*`, `/`
- Allows continuous calculations with previous results
- Prevents division by zero
- Modular function-based architecture
- CLI-based interaction with input prompts
- ASCII art banner using external module

---

## 🛠️ Technologies Used

- Python 3
- Standard Input/Output
- External ASCII Art module:
  - `Day10_CalculatorArt.py` for the calculator logo

---

## 📷 Sample Output  
```
 _____________________
|  _________________  |
| | Python Calc     | |
| |_________________| |
|_____________________|

Enter the First Number: 5
+
-
*
/

Pick an Operation: +
Enter the Next Number: 3
5.0 + 3.0 = 8.0
Type 'y' to continue calculation with 8.0. Or type 'n' to start a new Calculator: y

+
-
*
/
Pick an Operation: *
Enter the Next Number: 2
8.0 * 2.0 = 16.0
Type 'y' to continue calculation with 16.0. Or type 'n' to start a new Calculator: n

```

## 🧠 Function Breakdown
add(n1, n2)  
Returns the sum.  

subtract(n1, n2)  
Returns the difference.  

multiply(n1, n2)  
Returns the product.  

divide(n1, n2)  
Performs division. If the second number is 0, it safely returns 0.  

calculator(first_num, second_num, operator)  
Uses a dictionary to map operator symbols to their respective functions.  

main_menu()  
Controls the program flow and allows chained or new calculations based on user choice.  

## 💡 Enhancements You Can Add
- Add modulus (%) and exponentiation (**) support

- Add input validation for invalid operations or non-numeric input

- Display calculation history

- Create a GUI using Tkinter

- Save calculation logs to a file

## 👨‍💻 Author  
Arghyajyoti Samui  
GitHub: @Arghyajyoti007  
