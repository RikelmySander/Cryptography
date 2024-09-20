#Flet use for apps, web, and apis
import flet as ft

from CryptoSanderV_1_2 import Cryptography,crypt_dict,Crypto
#create function main
def main(page):
    #Create
    title = ft.Text("Live Chat")
    title_popup = ft.Text("Welcome to the chat")
    username_field = ft.TextField(label="Write your name in the chat")
    
    def send_menssage_tunnel(menssage):
        chat.controls.append(ft.Text(menssage))
        page.update()

    #create a communication tunnel
    page.pubsub.subscribe(send_menssage_tunnel)

    def send_menssage(event):
        crypt_dict = Cryptography(text_msg.value)
        print(crypt_dict.values)
        msg = f"{username_field.value}: {crypt_dict.values}"
        page.pubsub.send_all(msg)
        text_msg.value = ""
        page.update()
        return msg
    
    text_msg = ft.TextField(label="Write your menssage", on_submit=send_menssage)
    btn_send = ft.ElevatedButton("Send", on_click=send_menssage)
    #colluns and rows
    chat = ft.Column()
    row_menssage = ft.Row([text_msg, btn_send])

    def enter_chat(event):
        page.remove(title,btn_init)
        popup.open = False
        page.add(chat)
        page.add(row_menssage)
        page.pubsub.send_all(f"{username_field.value} entered the chat")
        page.update()

    btn_join = ft.ElevatedButton("Enter the chat", on_click=enter_chat)

    def open_popup(event):
        page.overlay.append(popup)
        popup.open = True
        page.update()
        
    popup = ft.AlertDialog(title=title_popup, content=username_field, actions=[btn_join])

    btn_init = ft.ElevatedButton("Start chat", on_click=open_popup)
    
    #Add
    page.add(title)
    page.add(btn_init)

#run the system as an app
ft.app(target=main,port=8000)
#To run in the web browser, execute this code in the terminal: 
#flet run --web --port:8000 code.py (or another port of your choice)