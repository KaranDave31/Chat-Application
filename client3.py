import tkinter
from tkinter import *
import socket
from threading import Thread

def receive():

    while True:
        try:
            message = sock.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END,message)
        except:
            print("There is some error ")

def send ():
    try:
        msg = my_msg.get()
        my_msg.set("")
        sock.send(bytes(msg,"utf8"))
        if msg=="#quit":
            sock.close()
            window.close()

    except:
        print("There is some error ")

def on_closing():
    my_msg.set("#quit")
    send()

window = Tk()
window.title("Chat Application")
window.configure(bg="green")

message_frame = Frame(window, height=100,width=100,bg="red")
message_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=15,width=15,bg = "red", yscrollcommand = scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill= Y)
msg_list.pack(side=LEFT,fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter the message ",fg="blue",font="Aeria", bg = "red")
label.pack()

entry_field = Entry(window, textvariable = my_msg,fg="red", width=50)
entry_field.pack()

send_Button = Button(window, text= "Send", font="Aerial", fg = "white", command = send)
send_Button.pack()

quit_Button = Button(window, text= "Quit", font="Aerial", fg = "white", command = on_closing)
quit_Button.pack()


host = "localhost"
port = 8080

try:
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    sock.connect((host, port))

    receive_Thread = Thread(target = receive)
    receive_Thread.start()

    sock.close()
    print("Connection closed")
except Exception as e:
    print("Error:", e)


mainloop()

