from PyPDF2 import PdfFileWriter, PdfFileReader
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox

# Global Var
filename = ''
password = ''
password_entry = ''


win = tk.Tk()
win.geometry('300x200')
win.title('PDF Encryptor')


def encrypt():
    global filename
    global password
    out = PdfFileWriter()

    file = PdfFileReader(filename)
    num = file.numPages
    for i in range(num):
        page = file.getPage(i)
        out.addPage(page)

    password = password_entry.get()

    print(password)
    out.encrypt(password)

    with open('D:/Project-Python/PDF-Encryptor/encrypted.pdf', 'wb') as f:
        out.write(f)

    messagebox.showinfo('Success', 'File Saved!')


def select_PDF():
    global filename
    global password_entry

    filename = filedialog.askopenfilename()
    file_label = tk.Label(win, text=f'Select File: {filename}', bg='red')
    file_label.grid(row=2, column=0, columnspan=8, padx=5)

    psd_label = tk.Label(win, text='Password for PDF : ')
    psd_label.grid(row=3, column=0, pady=10)

    password_entry = tk.Entry(win, width=25)
    password_entry.grid(row=3, column=1, columnspan=2, pady=10)

    enc_button = ttk.Button(win, text='Encrypt File',
                            command=encrypt, width=30)
    enc_button.grid(row=4, column=0, columnspan=8, pady=10)

    return filename


title = tk.Label(win, text='PDF Encryptor',
                 font=('arial', 25), justify='center')
title.grid(row=0, column=0, columnspan=8)

label1 = ttk.Label(win, text='Select File : ')
label1.grid(row=1, column=0, pady=10)

select_file = ttk.Button(win, text='Choose File', command=select_PDF)
select_file.grid(row=1, column=1, pady=10)

win.mainloop()
