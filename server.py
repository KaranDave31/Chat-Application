#used for TCP server that listens for incoming messages on certain port 
import socket #imported socket which provides low level networking functionality 
from threading import Thread

host = "localhost"  # specifices host name or IP address
port = 8080  # TCP port number that server listens on
client = {}  # making dictionary for all client
addresses = {}  # making dictionary for all addresses

try:

    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM) #creates a socket object using ipv6 family and TCP protocl, used for listening 

    sock.bind((host, port))

    def handle_clients(con,address):
        name = con.recv(1024).decode()
        welcome = "Welcome " + name + "You can type #quit to leave "
        con.send(bytes(welcome ,"utf8"))
        msg = name + " Has joined chat room "
        broadcast(bytes(msg,"utf8"))
        client[con] = name

        while True:
            msg = con.recv(1024)
            if msg != bytes("#quit","utf8"):
                broadcast(msg,name)
            else:
                con.send(bytes("#quit","utf8"))
                con.close()
                del client[con]
                broadcast(bytes(name + "has left the chat room ","utf8"))

    def accept_client_connections():
        while True:
            client_con, client_address = sock.accept()
            print(client_address, "has connected")
            client_con.send("Welcome to ChatApp, Enter your name to proceed ".encode('utf8'))
            addresses[client_con] = client_address

            Thread(target=handle_clients,args=(client_con,client_address)).start()


    def broadcast(msg,prefix=""):
        for x in client:
            x.send(bytes(prefix,"utf8")+msg)


    if __name__ == "__main__":
        sock.listen(5) #can listen to 5 requests at same time
        print("Server is running and listening")

    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join() #will stop function of another thread until one is complete




    # sock.listen(1) #sets socket to listen for incoming connections with maximum limit 1
    # print("Server is running and listening")
    # con, address = sock.accept()
    # message = "Message incoming"
    # con.send(message.encode()) #sends the message to client after encoding
    # con.close() #close the connection

except Exception as e:
    print("Error: ", e)
