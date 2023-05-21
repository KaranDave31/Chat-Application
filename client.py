# import tkinter
# from tkinter import *
# import socket
# from threading import Thread
#
# def receive():
#
#     while True:
#         try:
#             message = sock.recv(1024).decode("utf8")
#             msg_list.insert(tkinter.END,message)
#         except:
#             print("There is some error ")
#
# def send ():
#     try:
#         msg = my_msg.get()
#         my_msg.set("")
#         sock.send(bytes(msg,"utf8"))
#         if msg=="#quit":
#             sock.close()
#             window.close()
#
#     except:
#         print("There is some error ")
#
# def on_closing():
#     my_msg.set("#quit")
#     send()
#
# window = Tk()
# window.title("Chat Application")
# window.configure(bg="green")
#
# message_frame = Frame(window, height=100,width=100,bg="red")
# message_frame.pack()
#
# my_msg = StringVar()
# my_msg.set("")
#
# scroll_bar = Scrollbar(message_frame)
# msg_list = Listbox(message_frame, height=15,width=15,bg = "red", yscrollcommand = scroll_bar.set)
# scroll_bar.pack(side=RIGHT, fill= Y)
# msg_list.pack(side=LEFT,fill=BOTH)
# msg_list.pack()
#
# label = Label(window, text="Enter the message ",fg="blue",font="Aeria", bg = "red")
# label.pack()
#
# entry_field = Entry(window, textvariable = my_msg,fg="red", width=50)
# entry_field.pack()
#
# send_Button = Button(window, text= "Send", font="Aerial", fg = "white", command = send)
# send_Button.pack()
#
# quit_Button = Button(window, text= "Quit", font="Aerial", fg = "white", command = on_closing)
# quit_Button.pack()
#
#
# host = "localhost"
# port = 8080
#
# try:
#     sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
#     sock.connect((host, port))
#
#     receive_Thread = Thread(target = receive)
#     receive_Thread.start()
#
#     sock.close()
#     print("Connection closed")
# except Exception as e:
#     print("Error:", e)
#
#
# mainloop()
#import tkinter
from tkinter import *
import socket
from threading import Thread

def receive(msg_list):
    while True:
        try:
            message = sock.recv(1024).decode("utf8")
            if message:
                msg_list.insert(END, message)
        except ConnectionAbortedError:
            break
        except:
            print("Error receiving message")
            break

def send(event=None):
    try:
        msg = my_msg.get()
        my_msg.set("")
        sock.send(bytes(msg, "utf8"))
        if msg == "#quit":
            sock.close()
            window.destroy()

    except:
        print("Error sending message")

def on_closing(event=None):
    my_msg.set("#quit")
    send()

window = Tk()
window.title("Chat App")
window.resizable(0, 0)
#
# header_frame = Frame(window, bg="blue", height=70)
# header_frame.pack(fill=X)
#
# logo_label = Label(header_frame, text="My Chat App", font=("Arial", 20), fg="white", bg="blue")
# logo_label.pack(side=LEFT, padx=10)
#
# search_entry = Entry(header_frame, font=("Arial", 14), fg="black", width=30)
# search_entry.pack(side=LEFT, padx=10)
#
# settings_button = Button(header_frame, text="Settings", font=("Arial", 14), fg="white", bg="blue")
# settings_button.pack(side=RIGHT, padx=10)
#
# header_frame = Frame(window, height=70, bg="#075e54")
# header_frame.pack(side=TOP, fill=X)
#
# logo_image = PhotoImage(file="logo.png")
# logo_label = Label(header_frame, image=logo_image, bg="#075e54")
# logo_label.image = logo_image  # To prevent garbage collection of the image
# logo_label.pack(side=LEFT, padx=10)
#
# search_entry = Entry(header_frame, font=("Helvetica", 12), bg="#128c7e", fg="white", borderwidth=0, highlightthickness=0)
# search_entry.insert(0, "Search")
# search_entry.bind("<FocusIn>", lambda event: search_entry.delete(0, END))
# search_entry.bind("<FocusOut>", lambda event: search_entry.insert(0, "Search"))
# search_entry.pack(side=LEFT, padx=10)
#
# options_image = PhotoImage(file="options.png")
# options_button = Button(header_frame, image=options_image, bg="#075e54", bd=0, highlightthickness=0, command=options_menu)
# options_button.image = options_image  # To prevent garbage collection of the image
# options_button.pack(side=RIGHT, padx=10)
#
header_frame = Frame(window, height=100, bg="#075e54")

logo_label = Label(header_frame, text="", font=("Helvetica", 28), fg="#fff", bg="#075e54")
logo_label.pack(side=LEFT, padx=20)

search_entry = Entry(header_frame, font=("Helvetica", 16), fg="#075e54", bg="#fff", width=30)
search_entry.insert(0, "Search")
search_entry.pack(side=LEFT, padx=20)

options_button = Button(header_frame, text="Settings", font=("Helvetica", 16), fg="#fff", bg="#075e54", relief=FLAT)
options_button.pack(side=RIGHT, padx=20)

header_frame.pack(fill=X)


# Chat frame
chat_frame = Frame(window)
chat_frame.pack(pady=10)




# Message frame
message_frame = Frame(window)
message_frame.pack(pady=10)

# Chat listbox
chat_list = Listbox(chat_frame, height=25, width=50, bg="white", fg="black", font=("Arial", 12))
chat_list.pack(side=LEFT, fill=BOTH)

# Chat scrollbar
chat_scrollbar = Scrollbar(chat_frame)
chat_scrollbar.pack(side=RIGHT, fill=Y)
chat_list.config(yscrollcommand=chat_scrollbar.set)
chat_scrollbar.config(command=chat_list.yview)

# Message listbox
msg_list = Listbox(message_frame, height=3, width=50, bg="white", fg="black", font=("Arial", 12))
msg_list.pack(side=LEFT, fill=BOTH)

# Message scrollbar
msg_scrollbar = Scrollbar(message_frame)
msg_scrollbar.pack(side=RIGHT, fill=Y)
msg_list.config(yscrollcommand=msg_scrollbar.set)
msg_scrollbar.config(command=msg_list.yview)

# Message entry
my_msg = StringVar()
my_msg.set("")
msg_entry = Entry(window, textvariable=my_msg, font=("Arial", 12), width=37)
msg_entry.pack(pady=10)

# Send button
send_btn = Button(window, text="Send", font=("Arial", 12), bg="#075e54", fg="white", command=send)
send_btn.pack(pady=5)

# Bindings
window.bind("<Return>", send)
window.protocol("WM_DELETE_WINDOW", on_closing)

# Socket
host = "localhost"
port = 8080
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
sock.connect((host, port))

# Receive thread
receive_thread = Thread(target=receive, args=(chat_list,))
receive_thread.start()

# Main loop
window.mainloop()
