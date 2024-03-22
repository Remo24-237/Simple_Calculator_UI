
# importing required library
import tkinter

# string to hold results of various calculations
operation =""

def add_to_result (symbol):
    global operation
    operation += str(symbol)
    text_area.delete(1.0, "end")
    text_area.insert(1.0, operation)

def evaluate_operation():
    global operation
    try:
        operation = str(eval(operation))
        text_area.delete(1.0, "end")
        text_area.insert(1.0, operation)
    except:
        clear_field()
        text_area.insert(1.0,"Error")

def clear_field():
    global operation
    operation =""
    text_area.delete(1.0, "end")

# defining the user interface
root=tkinter.Tk()
root.geometry("300x280")

text_area = tkinter.Text(root, height=2, width=14, font=("Arial", 24))
text_area.grid(columnspan=8)

# staging the numbers as a keypad in a grid
btn_1 = tkinter.Button(root, text="1", command=lambda: add_to_result(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tkinter.Button(root, text="2", command=lambda: add_to_result(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tkinter.Button(root, text="3", command=lambda: add_to_result(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tkinter.Button(root, text="4", command=lambda: add_to_result(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tkinter.Button(root, text="5", command=lambda: add_to_result(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tkinter.Button(root, text="6", command=lambda: add_to_result(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tkinter.Button(root, text="7", command=lambda: add_to_result(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tkinter.Button(root, text="8", command=lambda: add_to_result(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tkinter.Button(root, text="9", command=lambda: add_to_result(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_0 = tkinter.Button(root, text="0", command=lambda: add_to_result(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

# inserting symbols
btn_plus = tkinter.Button(root, text="+", command=lambda: add_to_result("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=5)
btn_minus = tkinter.Button(root, text="-", command=lambda: add_to_result("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=5)
btn_div = tkinter.Button(root, text="/", command=lambda: add_to_result("/"), width=5, font=("Arial", 14))
btn_div.grid(row=4, column=5)
btn_mult = tkinter.Button(root, text="*", command=lambda: add_to_result("*"), width=5, font=("Arial", 14))
btn_mult.grid(row=5, column=5)

btn_left_bracket = tkinter.Button(root, text="(", command=lambda: add_to_result("("), width=5, font=("Arial", 14))
btn_left_bracket.grid(row=5, column=1)
btn_right_bracket = tkinter.Button(root, text=")", command=lambda: add_to_result(")"), width=5, font=("Arial", 14))
btn_right_bracket.grid(row=5, column=3)

btn_clear = tkinter.Button(root, text="Clear", command=clear_field, width=5, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_equal = tkinter.Button(root, text="=", command=lambda: evaluate_operation(), width=5, font=("Arial", 14))
btn_equal.grid(row=6, column=3, columnspan=2)

root.mainloop()