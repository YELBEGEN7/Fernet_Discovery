import customtkinter as ctg
from cryptography.fernet import Fernet
from PIL import Image
from CTkMessagebox import CTkMessagebox
import base64



#Global Değişkenler v
global update_keys

#Uygulama Başlık,Boyut,Logo
app=ctg.CTk()
app.geometry("1100x400")
app.title("Fernet")

#Frame Alanları
frame_logo=ctg.CTkFrame(master=app,width=300,height=400,corner_radius=0)
frame_logo.grid(row=1,column=0)
frame_center=ctg.CTkFrame(master=app,width=400,height=400,corner_radius=0)
frame_center.grid(row=1,column=1)
frame_save_data=ctg.CTkFrame(master=app,width=400,height=400,corner_radius=0)
frame_save_data.grid(row=1,column=2)

def generate_key():
    keys=Fernet.generate_key()
    return keys

#Key oluşturma Butonu Eventi ve girdi alanı
def event_button_key():
    keys=generate_key()
    entry_key.delete(0,'end')
    entry_key.insert(0,f"{keys.decode('ascii')}")
    textbox_data.insert("end",f"\nkey={keys.decode('ascii')}\n\n")
button_key=ctg.CTkButton(master=frame_center,text="Key Generate",width=75,command=event_button_key)
button_key.grid(row=3,column=1,padx=10,pady=10)

entry_key=ctg.CTkEntry(master=frame_center,placeholder_text="key",width=200)
entry_key.grid(row=3,column=0,padx=10,pady=10)

#Şifre girme alanı
entry_password=ctg.CTkEntry(master=frame_center,placeholder_text="Password",width=200)
entry_password.grid(row=2,column=0,padx=10,pady=10)

#Password Şifreleme ve Değişmemesi gereken değerleri kitliyor
def event_button_password():
    key=bytes(entry_key.get(),'utf-8')
    msg=bytes(entry_password.get(),'utf-8')
    fernet=Fernet(key)
    encrypt_password=fernet.encrypt(msg)
    entry_enpassword.delete(0,'end')
    entry_enpassword.insert(0,encrypt_password)
    textbox_data.insert("end",f"password={msg.decode('utf-8')}\n\n")
    textbox_data.insert("end",f"encrypt={encrypt_password.decode('utf-8')}\n\n")
    entry_password.configure(state="normal")

button_password=ctg.CTkButton(master=frame_center,text="Password Encrypt",command=event_button_password)
button_password.grid(row=4,column=1,padx=10,pady=10)

entry_enpassword=ctg.CTkEntry(master=frame_center,placeholder_text="Password Encrease",width=200)
entry_enpassword.grid(row=4,column=0,padx=10)

#Şifrelenmiş Password çözümleme
def event_button_depassword():
    key=bytes(entry_key.get(),'utf-8')
    msg=bytes(entry_enpassword.get(),'utf-8')
    fernet=Fernet(key)     
    descrypted_password=fernet.decrypt(msg)
    entry_depassword.delete(0,'end')
    entry_depassword.insert(0,str(descrypted_password,'utf-8'))
    textbox_data.insert("end",f"decrypt={descrypted_password.decode()}\n")
button_depassword=ctg.CTkButton(master=frame_center,text="Password Decrypt",command=event_button_depassword)
button_depassword.grid(row=5,column=1,padx=10,pady=10)

entry_depassword=ctg.CTkEntry(master=frame_center,placeholder_text="Password Decrease",width=200)
entry_depassword.grid(row=5,column=0,padx=10,pady=10)

#Alanların kilidini ve değerlerini sıfırlar
def event_button_reset():
    button_password.configure(state="normal")
    button_key.configure(state="normal")
    entry_key.configure(state="normal")
    entry_password.configure(state="normal")
    entry_enpassword.configure(state="normal")
    entry_depassword.delete(0,'end')
    entry_enpassword.delete(0,'end')
    entry_key.delete(0,'end')
    entry_password.delete(0,'end')


button_reset=ctg.CTkButton(master=frame_center,text="Reset",command=event_button_reset,fg_color="#008170")
button_reset.grid(row=6,column=0,padx=10,pady=10)

textbox_data=ctg.CTkTextbox(master=frame_save_data,width=375,height=350)
textbox_data.grid(row=0, column=0, sticky="nsew",padx=10,pady=10)

def event_button_clear():
    textbox_data.delete("0.0",'end')

button_clear=ctg.CTkButton(master=frame_center,text="Clear",command=event_button_clear,fg_color="#008170")
button_clear.grid(row=6,column=1,padx=10,pady=10)



app.mainloop()