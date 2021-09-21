from tkclass import GUI
from tkinter import *
import sys

default_padding = 10
buttons_padding = 5
standard_font_size = 12
text_color = "#0b9608"
labels_text_color = "#98d9ed"
key_separator = "--"

window_width = 1200
window_height = 1000

# ------------------------------------------------------ Functions ------------------------------------------------------- #
def generate_ascii_values():
    ascii_values = []
    for i in range(1,256):
        ascii_values.append(chr(i))
    return ascii_values


def key_handler(key:list):
    new_key = []
    if key == ['']:
        window.error_box(title="Error",message="Key cannot be empty!")
        return "return"

    for element in key:
        if not str(element).isalnum():
            window.error_box(title="Error",message="You can only Enter Alphanumeric characters in key\n(A-Z),(a-z),(0-9)")
            return "return"

        try:
            if int(element) >= 0:
                new_key.append(int(element) % 255)
            else:
                new_key.append(int(element) % -255)
        except ValueError:
            new_key.append(ord(element[0]))
    return new_key


def ciph(text:str,key:list):
    ciphered_text = ''
    i = 0
    for charx in text:
        ascii_index = ord(charx)+key[i]
        if ascii_index >= len(ascii_values):
            ascii_index = ascii_index % len(ascii_values)
        elif ascii_index < 0:
            ascii_index = len(ascii_values) - (ascii_index*-1)
        ciphered_text += ascii_values[ascii_index-1]
        i += 1
        if i == len(key):
            i = 0
    return ciphered_text


def deciph(text:str,key:list):
    deciphered_text = ''
    i = 0
    for charx in text:
        ascii_index = ord(charx)-key[i]
        if ascii_index >= len(ascii_values):
            ascii_index = ascii_index % len(ascii_values)
        elif ascii_index < 0:
            ascii_index = len(ascii_values) - (ascii_index * -1)
        deciphered_text += ascii_values[ascii_index-1]
        i += 1
        if i == len(key):
            i = 0
    return deciphered_text


def encrypt():
    two_layers = True
    text = inp_text_area.get(1.0,END)
    text = text[:-1] if text[-1] == "\n" else text
    if len(text) == 0:
        return window.error_box(title="Error",message="Enter some text in Text box to proceed!")

    full_key_str = key_value.get()
    if full_key_str == '':
        window.error_box("Error", "Please Enter the Key to continue.")
        return
    out_text_area.delete(1.0, END)

    temp_key1 = full_key_str.split('--')[0].split(',')
    try:
        temp_key2 = full_key_str.split(key_separator)[1].split(',')
        key2 = key_handler(temp_key2)
        if key2 == "return":
            return
    except IndexError:
        two_layers = False

    key1 = key_handler(temp_key1)
    if key1 == "return":
        return
    l1_text = ciph(text,key1)
    final_text = l1_text

    if two_layers:
        l2_text = ciph(l1_text,key2)
        final_text = l2_text
    return out_text_area.insert(1.0,final_text)


def decrypt():
    two_layers = True
    text = inp_text_area.get(1.0,END)
    text = text[:-1] if text[-1] == "\n" else text
    if len(text) == 0:
        return window.error_box(title="Error",message="Enter some text in Text box to proceed!")

    full_key_str = key_value.get()
    if full_key_str == '':
        window.error_box("Error", "Please Enter the Key to continue.")
        return
    out_text_area.delete(1.0, END)

    temp_key1 = full_key_str.split('--')[0].split(',')
    try:
        temp_key2 = full_key_str.split(key_separator)[1].split(',')
        key2 = key_handler(temp_key2)
        if key2 == "return":
            return
    except IndexError:
        two_layers = False

    key1 = key_handler(temp_key1)
    if key1 == "return":
        return

    if two_layers:
        l1_text = deciph(text,key2)
        l2_text = deciph(l1_text,key1)
        final_text = l2_text
    else:
        l1_text = deciph(text,key1)
        final_text = l1_text
    return out_text_area.insert(1.0,final_text)


def clear_fields():
    """
    Clears the fields after getting confirmation from the user.
    if fields are already cleared, then does nothing
    """
    inp_value = inp_text_area.get(1.0,END)
    out_value = out_text_area.get(1.0,END)
    inp_value = inp_value[:-1] if inp_value[-1] == "\n" else inp_value
    out_value = out_value[:-1] if out_value[-1] == "\n" else out_value
    fields_clear = (len(inp_value) == 0 and len(out_value) == 0 and len(key_value.get()) == 0)

    if fields_clear:
        return window.info_box(title="Info",message="Fields are already empty!")
    else:
        confirm_clear = window.askyesno(title="Confirm Clearing Fields?",message="Before clearing the fields, Make sure you don't have anything to copy from the text boxes\n"
                                                                                "Do you want to continue with clearing the fields?")
        if confirm_clear:
            inp_text_area.delete(1.0,END)
            key_value.set('')
            out_text_area.delete(1.0,END)
            return
        else:
            return
# ------------------------------------------------------------------------------------------------------------------------- #
window = GUI(title="Encryptor - Application By Usama", geometry=f"{window_width}x{window_height}", icon="encrypted.ico",fixed_geometry=False)

ascii_values = generate_ascii_values()

# TK Variables
inp_text = StringVar()
key_value = StringVar()
out_text = StringVar()
# ------------------------------------------------------------------------------------------------------------------------- #

# ----------------------------------------------------- Header Frame ----------------------------------------------------=- #
header_frame = Frame(window,bg=window.background_color)
header_frame.pack(side=TOP,fill=BOTH)

header_title = Label(header_frame, text="Encryption - Decryption Application".title(), font=('comicsansms',16,'bold'),
                     bg=window.background_color, fg=labels_text_color, borderwidth=7, relief=SUNKEN,
                     padx=default_padding, pady=default_padding)
header_title.pack(padx=default_padding,pady=default_padding)
# ------------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------------ Input Frame ------------------------------------------------------ #
input_frame = Frame(window,bg=window.background_color,borderwidth=1,relief=RIDGE)
input_frame.pack(padx=default_padding,pady=default_padding,fill=BOTH)

text_label = Label(input_frame, text="Enter Your Text Here :", font=('comicsansms',standard_font_size,'bold'),
                   bg=window.background_color, fg=labels_text_color,
                   padx=default_padding, pady=default_padding)
text_label.grid(row=0,column=0,padx=default_padding,pady=default_padding)

inp_text_area = Text(input_frame,height=15,width=100,bg=window.background_color,fg=text_color,font=('consolas',standard_font_size))
inp_text_area.grid(row=0,column=1,padx=default_padding,pady=default_padding)

key_label = Label(input_frame, text="Enter Your Key Here :", font=('comicsansms',standard_font_size,'bold'),
                  bg=window.background_color, fg=labels_text_color,
                  padx=default_padding, pady=default_padding)
key_label.grid(row=1,column=0)

key_entry = Entry(input_frame,textvariable=key_value,width=100,font=('consolas',standard_font_size),bg=window.background_color,fg=text_color)
key_entry.grid(row=1,column=1)

key_note = Label(input_frame, text=(f"NOTE : Enter each element of key separated with a comma ','\n\t   "
                                   f"If using 2 keys, separate the keys using two hyphens '{key_separator}'\n\t            "
                                   f"Make sure that you do not have any spaces before or after '{key_separator}'"),
                 font=('comicsansms',standard_font_size,'bold'), bg=window.background_color, fg=labels_text_color,
                 padx=default_padding, pady=default_padding)
key_note.grid(row=2,column=1)
# ---------------------------------------------------------------------------------------------------------------=---------- #

# ----------------------------------------------------- Buttons Frame ------------------------------------------------------ #
buttons_frame = Frame(window,bg=window.background_color)
buttons_frame.pack(padx=default_padding,pady=default_padding,fill=BOTH)

decrypt_button = Button(buttons_frame, text="Decrypt", font=('comicsansms', standard_font_size, 'bold'), borderwidth=3, relief=RAISED,
                        bg=window.background_color, fg=labels_text_color, command=decrypt,
                        padx=buttons_padding, pady=buttons_padding)
decrypt_button.pack(side=RIGHT, anchor='ne', padx=buttons_padding, pady=buttons_padding)

encrypt_button = Button(buttons_frame, text="Encrypt", font=('comicsansms', standard_font_size, 'bold'), borderwidth=3, relief=RAISED,
                        bg=window.background_color, fg=labels_text_color, command=encrypt,
                        padx=buttons_padding, pady=buttons_padding)
encrypt_button.pack(side=RIGHT, anchor='ne', padx=buttons_padding, pady=buttons_padding)

clearfields_button = Button(buttons_frame,text="Clear Fields",font=('comicsansms',standard_font_size,'bold'),borderwidth=3,relief=RAISED,
                            bg=window.background_color,fg=labels_text_color,command=clear_fields,
                            padx=buttons_padding,pady=buttons_padding)
clearfields_button.pack(side=LEFT,anchor='nw',padx=buttons_padding,pady=buttons_padding)
# -------------------------------------------------------------------------------------------------------------------------- #

# ------------------------------------------------------ Output Frame ------------------------------------------------------ #
output_frame = Frame(window,bg=window.background_color,borderwidth=1,relief=RIDGE)
output_frame.pack(padx=default_padding,pady=default_padding,fill=BOTH)

out_text_label = Label(output_frame, text="          Result :          ", font=('comicsansms',standard_font_size,'bold'),
                       bg=window.background_color, fg=labels_text_color,
                       padx=default_padding, pady=default_padding)
out_text_label.grid(row=0,column=0,padx=default_padding,pady=default_padding)

out_text_area = Text(output_frame,height=15,width=100,bg=window.background_color,fg=text_color,font=('consolas',standard_font_size))
out_text_area.grid(row=0,column=1,padx=default_padding,pady=default_padding)

exit_button = Button(output_frame,text="Exit",font=('comicsansms',standard_font_size,'bold'),borderwidth=3,relief=RAISED,
                     bg=window.background_color,fg=labels_text_color,command=window.exit_window,
                     padx=buttons_padding,pady=buttons_padding)
exit_button.grid(row=1,column=2,padx=buttons_padding,pady=buttons_padding)
# -------------------------------------------------------------------------------------------------------------------------- #
#TODO: Make help menu to show how this program works (works on principle of cipher, but is not cipher, because of using ascii)
window.run()