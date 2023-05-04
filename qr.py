import segno
import tkinter
from tkinter import *
from segno import helpers
def qr_generator_vcard(name,dispname,phone,email,org,title):
    qrcode = helpers.make_vcard(name= name,displayname=dispname, phone=phone, email= email, org= org, title= title)
    qrcode.show()
def qr_generator_url(url):
    qrcode = segno.make(url)
    qrcode.show()
def qr_generator_wifi(ssid,password,security):
    qrcode= helpers.make_wifi(ssid=ssid, password=password, security=security)
    qrcode.show()
def qr_generator_txt(text):
    qrcode= segno.make(text)
    qrcode.show()
def create_vcard(name,phone,mail,org,title):
    d = name.get()
    n = organize_name_for_vcard_input(d)
    p = phone.get()
    e = mail.get()
    o = org.get()
    t = title.get()
    qr_generator_vcard(n,d,p,e,o,t)
def create_url(url):
    u = url.get()
    qr_generator_url(u)
def create_wifi(ssid,password,security):
    ss = ssid.get()
    p = password.get()
    s = security.get()
    qr_generator_wifi(ss,p,s)
def create_text(text):
    t = text.get(1.0, "end-1c")
    qr_generator_txt(t)
def organize_name_for_vcard_input(s):
    l = s.split(" ")
    result = l[-1]
    l = l[:-1]
    for i in l:
        result+= ";"+i
    return result
def tkinker_of_vcard():
    master = Tk()
    master.geometry("400x160")
    l_name = Label(master, text="Name and Surname").grid(row=0, column=0)
    name = Entry(master, width=40)
    name.grid(row=0, column=1)
    l_phone = (Label(master, text="Phone Number")).grid(row=1, column=0)
    phone = Entry(master, width=40)
    phone.grid(row=1, column=1)
    l_mail = (Label(master, text="Email")).grid(row=2, column=0)
    mail = Entry(master, width=40)
    mail.grid(row=2, column=1)
    l_org = (Label(master, text="Organisation")).grid(row=3, column=0)
    org = Entry(master, width=40)
    org.grid(row=3, column=1)
    l_t = (Label(master, text="Title")).grid(row=4, column=0)
    title = Entry(master, width=40)
    title.grid(row=4, column=1)
    b = (Button(master, text="CREATE", command=lambda: create_vcard(name, phone, mail, org, title))).grid(row=5, column=1)
    b1 = (Button(master, text="CLOSE", command=master.destroy)).grid(row=6, column=1)
    master.mainloop()
def tkinker_of_url():
    master = Tk()
    master.geometry("550x80")
    u_name = (Label(master,text="URL")).grid(row=0,column=0)
    url = Entry(master,width=80)
    url.grid(row=0,column=1)
    b = (Button(master,text="CREATE",command=lambda: create_url(url))).grid(row=1,column=1)
    b1 = (Button(master, text="CLOSE", command=master.destroy)).grid(row=2, column=1)
    master.mainloop()
def tkinker_of_wifi():
    master = Tk()
    master.geometry("550x150")
    ss_name = (Label(master, text="Wifi Name")).grid(row=0, column=0)
    ssid = Entry(master, width=70)
    ssid.grid(row=0, column=1)
    p = Label(master,text="Password").grid(row=1,column=0)
    password = Entry(master,width=70)
    password.grid(row=1,column=1)
    radio = tkinter.StringVar(master,value=None)
    s = Label(master,text="Security Type:").grid(row=2,column=0)
    r1 = Radiobutton(master,text="WEP",variable= radio,value= "WEP",tristatevalue=0).grid(row=3, column=0)
    r2 = Radiobutton(master,text="WPA/WPA2",variable= radio,value= "WPA",tristatevalue=0).grid(row=4, column=0)
    b1 = Button(master,text="CREATE",command=lambda : create_wifi(ssid,password,radio)).grid(row=3,column=1)
    b2 = Button(master,text="CLOSE",command=master.destroy).grid(row=4,column=1)
    master.mainloop()
def tkinker_of_text():
    master=Tk()
    master.geometry("750x450")
    s_name = Label(master,text="Write your text: ").grid(row=0,column=0)
    text = Text(master)
    text.grid(row=0,column=1)
    b1 = Button(master,text="CREATE",command=lambda :create_text(text)).grid(row=1,column=0)
    b2 = Button(master,text="CLOSE",command= master.destroy).grid(row=2,column=0)
    master.mainloop()
def main():
    master=Tk()
    master.title("QRCODE CREATOR")
    b1 = Button(master,text="URL",height=8,width=16,command=lambda: [master.destroy(),tkinker_of_url()]).grid(row=0,column=0)
    b2 = Button(master, text="TEXT",height=8,width=16, command=lambda: [master.destroy(), tkinker_of_text()]).grid(row=0, column=1)
    b3 = Button(master, text="WI-FI",height=8,width=16, command=lambda: [master.destroy(), tkinker_of_wifi()]).grid(row=1, column=0)
    b4 = Button(master, text="VCARD",height=8,width=16, command=lambda: [master.destroy(), tkinker_of_vcard()]).grid(row=1, column=1)
    master.mainloop()
main()