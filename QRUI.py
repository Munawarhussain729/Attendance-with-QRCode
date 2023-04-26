import tkinter as tk
import qrcode
input1 = ""
input2 = ""


def GenerateQR():
    global input1
    global input2
    data = input1.get() + " # " + input2.get()
    img = qrcode.make(data)
    img.save(input2.get()+'.png')
    input1.delete(0, 'end')
    input2.delete(0, 'end')


def Clear():
    global input1
    global input2
    input1.delete(0, 'end')
    input2.delete(0, 'end')



# Create the main window
window = tk.Tk()
window.title("QR Code Generator")
window.configure(background="#FFFFFF")

# Create a frame for the widgets
frame = tk.Frame(window, bg="#FFFFFF")
frame.grid(row=0, column=0, padx=20, pady=20)

# Create the labels and input fields
label1 = tk.Label(frame, text="Name :", font=(
    "Helvetica", 14), fg="#333333", bg="#FFFFFF")
input1 = tk.Entry(frame, font=("Helvetica", 14),
                  highlightthickness=0)
label2 = tk.Label(frame, text="Roll Number :", font=(
    "Helvetica", 14), fg="#333333", bg="#FFFFFF")
input2 = tk.Entry(frame, font=("Helvetica", 14),
                  highlightthickness=0)

# Create the buttons
Generate = tk.Button(frame, text="Generate", font=(
    "Helvetica", 14), bg="#4285F4",  bd=0, padx=10, pady=5, command=GenerateQR)
clear = tk.Button(frame, text="Clear", font=(
    "Helvetica", 14), bg="#4285F4",  bd=0, padx=10, pady=5, command=Clear)

# Place the widgets in the frame
label1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
input1.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
label2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
input2.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

Generate.grid(row=2, column=1, padx=10, pady=10, sticky="w")
clear.grid(row=2, column=0, padx=10, pady=10, sticky="e")


# Run the main loop
window.mainloop()
