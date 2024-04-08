from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import webbrowser
import mysql.connector
from datetime import datetime
from decimal import Decimal
import pyttsx3
def telegram():
  telegram_link = "place your telegram link"
  webbrowser.open(telegram_link)
def mail():
  email = "miyasajid19@gmail.com"
  webbrowser.open("mailto:" + email)
def whatsapp():
  link='https://whatsapp.com/channel/0029Va4K0PZ5a245NkngBA2M'
  webbrowser.open(link)
def connection1():
  try:
    connection=mysql.connector.connect(host="localhost",user="root",password="",database="restaurantmanagementsystem")
    if connection.is_connected():
      return connection
  except Exception as e:
    messagebox.showerror("error",e)

def book(data):
   if data[-1]=='TRUE':
      global name,contact,uid
      name=name.get()
      contact=contact.get()
      uid=uid.get()
      print(name,contact,uid)
      conn=connection1()
      mycursor=conn.cursor()
      sql1=f"INSERT INTO `guests`(`GuestID`, `Name`, `Contact`, `RoomID`, `RoomName`) VALUES ('{uid}','{name}','{contact}','{data[0]}','{data[1]}')"
      sql2=f"UPDATE `rooms` SET `Availability`='FALSE' WHERE  `RoomID`='{data[0]}'"
      try:
         mycursor.execute(sql1)
         mycursor.execute(sql2)
         messagebox.showinfo("info",f"booked successfully")
      except Exception as e:
         messagebox.showinfo("error",f"failed to book the book \n due to {e}")
      conn.commit()
      conn.close()
      global frame1
      frame1.destroy()
      frame1 = Frame(root, bg=b)
      frame1.pack()
      main()

def proceed_booking():
   global frame1
   frame1.destroy()
   frame1 = Frame(root, bg=b)
   frame1.pack()
   conn=connection1()
   mycursor=conn.cursor()
   sql=f"SELECT `RoomID`, `RoomNumber`, `RoomType`, `Capacity`, `Rate`, `AC`, `Availability` FROM `rooms` where `RoomID`= {room.get()}"
   mycursor.execute(sql)
   data=mycursor.fetchone()
   print(data)
   conn.commit()
   conn.close()
   global name,contact,uid
   try:
    img1=Image.open(r"images\Benefits-to-booking-a-room-directly-with-a-hotel-over-a-third-party-travel-site.webp").resize((500,300))
    img1=ImageTk.PhotoImage(img1)
    label=Label(frame1,image=img1,bg=b)
    label.image=img1
    label.grid(row=0,column=0,columnspan=2)
   except Exception as e:
      print(e)
   Label(frame1,text="RoomId",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=1,column=0)
   Label(frame1,text=data[0],font="helvetica 15 italic",bg=b,fg="#FFBE98").grid(row=1,column=1)
   Label(frame1,text="RoomNumber",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=2,column=0)
   Label(frame1,text=data[1],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=2,column=1)
   Label(frame1,text="RoomType",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=3,column=0)
   Label(frame1,text=data[2],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=3,column=1)
   Label(frame1,text="Capacity",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=4,column=0)
   Label(frame1,text=data[3],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=4,column=1)
   Label(frame1,text="Rate",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=5,column=0)
   Label(frame1,text=data[4],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=5,column=1)
   Label(frame1,text="AC",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=6,column=0)
   Label(frame1,text=data[5],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=6,column=1)
   Label(frame1,text="Availability",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=7,column=0)
   Label(frame1,text=data[6],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=7,column=1)
   Label(frame1,text="Name : ",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=12,column=0)
   name=Entry(frame1,font="helvetica 15 italic",width=30,fg="#FFBE98")
   name.grid(row=12,column=1)
   Label(frame1,text="identification number : ",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=13,column=0)
   uid=Entry(frame1,font="helvetica 15 italic",width=30,fg="#FFBE98")
   uid.grid(row=13,column=1)
   Label(frame1,text="contact : ",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=14,column=0)
   contact=Entry(frame1,font="helvetica 15 italic",width=30,fg="#FFBE98")
   contact.grid(row=14,column=1)
   img=Image.open(r"images\\360_F_289646929_mvmudLRuRSTKw38sbfANSoZcQwByTlV6.jpg").resize((150,75))
   img=ImageTk.PhotoImage(img)
   def go():
      book(data)
   btn=Button(frame1,image=img,command=go,bg=b,border=0,bd=0)
   btn.image=img
   btn.grid(row=15,column=0,columnspan=2,sticky=N)
  
def checkin():
   global frame1
   frame1.destroy()
   frame1=Frame(root,bg=b)
   frame1.pack()
   Label(frame1,text="check in",font="stencil 20 bold",bg=b,fg="white").grid(row=0,column=0,columnspan=5)
   img=Image.open(r"images\Benefits-to-booking-a-room-directly-with-a-hotel-over-a-third-party-travel-site.webp").resize((500,400))
   img=ImageTk.PhotoImage(img)
   label=Label(frame1,image=img,bg=b)
   label.image=img
   label.grid(row=1,column=0,columnspan=5)
  
   conn = connection1()
   if conn:
       mycursor = conn.cursor()
       sql = "SELECT `RoomID`, `RoomNumber`,  `RoomType`, `Capacity`, `Rate`,  `AC`,`Availability` FROM `rooms` "
       mycursor.execute(sql)
       data = mycursor.fetchall() 
       if data:
         # Creating a treeview to display menu items
         tree = ttk.Treeview(frame1, columns=("RoomID", "RoomNumber", "RoomType", "Capacity", "Rate", "AC","Availability"))
         tree.heading("RoomID", text="RoomID")
         tree.heading("RoomNumber", text="RoomNumber")
         tree.heading("RoomType", text="RoomType")
         tree.heading("Capacity", text="Capacity")
         tree.heading("Rate", text="Rate")
         tree.heading("AC", text="AC")
         tree.heading("Availability", text="Availability")
         # Adjusting column widths
         tree.column("RoomID", width=100)
         tree.column("RoomNumber", width=150)
         tree.column("RoomType", width=100)
         tree.column("Capacity", width=60)
         tree.column("Rate", width=120)
         tree.column("AC", width=110)
         tree.column("Availability", width=110)
         # Adding a scrollbar
         scrollbar = ttk.Scrollbar(frame1, orient="vertical", command=tree.yview)
         scrollbar.grid(row=2, column=2, sticky="ns", padx=10, pady=10)
         tree.configure(yscrollcommand=scrollbar.set)
         # Inserting data into the treeview
         for record in data:
             tree.insert("", "end", values=record)
         # Placing the treeview
         tree.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
         # Styling the treeview
         style = ttk.Style()
         style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), foreground="#E59BE9")
         style.configure("Treeview", font=("helvetica", 12, "italic"), background=b, foreground="#E59BE9")
         # Closing the database connection
         conn.close()
   frame2=Frame(frame1,bg=b)
   frame2.grid(row=3,column=0,columnspan=3)
   Label(frame2,text="RoomID : ",bg=b,fg="white",font="stencil 20 bold",anchor=CENTER).grid(row=0,column=0,sticky=N,padx=10,pady=10)
   global room
   room=StringVar()
   Entry(frame2,textvariable=room,width=30,fg=b,font="ariel 10 italic").grid(row=0,column=1,sticky=N,padx=10,pady=20)
   img1=Image.open(r"images\Next_logo.png").resize((100,50))
   img1=ImageTk.PhotoImage(img1)
   btn=Button(frame2,image=img1,command=proceed_booking,border=0,bd=0,bg=b)
   btn.image=img1
   btn.grid(row=1,column=0,sticky=N,columnspan=3)
def give():
    global key,bankid,rest,fid,tot
    sid = bankid.get()
    rid = rest.get()
    rs=tot
    spassword = key.get()

    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="", database="bankingsystem")
        cursor = connection.cursor()

        # Check if sender and receiver exist
        cursor.execute("SELECT * FROM `users`")
        users = cursor.fetchall()
        user_ids = {user[0] for user in users}

        if sid in user_ids and rid in user_ids:
            # Check sender's balance and perform transaction
            cursor.execute(f"SELECT amount FROM account WHERE casid = {sid} AND passs = '{spassword}'")
            print("SELECT amount FROM account WHERE casid = %s AND passs = %s", (sid, spassword))
            sender_balance = cursor.fetchone()
            
            if sender_balance:
                sender_balance = int(sender_balance[0])
                print(sender_balance)
                if sender_balance >= rs:
                    sender_balance -= rs
                    cursor.execute("UPDATE account SET amount = %s WHERE casid = %s", (sender_balance, sid))

                    # Update receiver's balance
                    cursor.execute("SELECT amount FROM account WHERE casid = %s", (rid,))
                    receiver_balance = int(cursor.fetchone()[0])
                    receiver_balance += rs
                    cursor.execute("UPDATE account SET amount = %s WHERE casid = %s", (receiver_balance, rid))
                    
                    connection.commit()
                    speak(f" Rs. {rs} has been successfully credited to SMPK bank account")
                    messagebox.showinfo("Success", f"{rs} has been paid")
                    connection.close()
                    conn=connection1()
                    mycursor=conn.cursor()
                    if funid=="food":
                       
                      sql1=f"DELETE FROM `pending_orders` WHERE contact={contact.get()}"
                      mycursor.execute(sql1)
                      conn.commit()
                      conn.close()
                      conn=connection1()
                      mycursor=conn.cursor()
                      for i in fid:

                        sql3=f"SELECT `Availability` FROM `menu` WHERE MenuItemID={i}"
                        mycursor.execute(sql3)
                        data=mycursor.fetchone()
                        print(data[0])
                        conn.commit()
                        conn.close()
                        print(sql3)
                        conn=connection1()
                        mycursor=conn.cursor()
                        sql2=f"UPDATE `menu` SET `Availability`='{int(data[0])+1}' WHERE `MenuItemID`={i}"
                        print(sql2)
                        mycursor.execute(sql2)
                    else:
                      global id
                      sql1=f"DELETE FROM `guests` WHERE  `GuestID`={id.get()}"
                      mycursor.execute(sql1)
                      conn.commit()
                      conn.close()
                      conn=connection1()
                      mycursor=conn.cursor()
                      global datax
                      sql3=f"SELECT `Availability` FROM `rooms` WHERE `RoomID`={datax[-2]}"
                      mycursor.execute(sql3)
                      data=mycursor.fetchone()
                      print(data[0])
                      conn.commit()
                      conn.close()
                      print(sql3)
                      conn=connection1()
                      mycursor=conn.cursor()
                      sql2=f"UPDATE `rooms` SET `Availability`='TRUE' WHERE  `RoomID`='{datax[-2]}'"
                      print(sql2)
                      mycursor.execute(sql2)
                      
                      
                      
                    conn.commit()
                    conn.close()
                    global frame1
                    frame1.destroy()
                    # Declare frame1 as global
                    frame1.pack_forget()  # Use pack_forget() instead of frame1.forget()
                    frame1 = Frame(root)
                    frame1.configure(bg=b)
                    frame1.grid(row=0, column=0, sticky="nsew")
                    main()
                else:
                    speak("Insufficient balance to proceed with the transaction")
                    messagebox.showerror("Error", "Insufficient balance to proceed with the transaction")
            else:
                speak("Invalid pasword")
                messagebox.showerror("Error", "Invalid password")
        else:
            speak("Either sender or receiver does not have a bank account")
            messagebox.showerror("Error", "Either sender or receiver does not have a bank account")
    except mysql.connector.Error as e:
        speak("Database error")
        messagebox.showerror("Error", f"Database error: {e}")
    finally:
        if 'connection' in locals():
            connection.close()
        

def payforfood():
    
    global frame1,b,contact
    frame1.destroy()  # Destroy the existing frame
    frame1 = Frame(root)  # Recreate the frame
    frame1.configure(bg=b)
    frame1.pack()
    def show():
      contact.config(state="disabled")
      btn1.destroy()
      frame12=Frame(frame1,bg=b)
      frame12.pack()
      conn=connection1()
      mycursor=conn.cursor()
      sql=f"SELECT id FROM `pending_orders` WHERE contact='{contact.get()}'"
      mycursor.execute(sql)
      data=mycursor.fetchall()
      print(data)
      global fid
      fid=list()
      for i in data:
         print(i[0])
         fid.append(i[0])
      print("sadf:",fid)
      conn.commit()
      conn.close()
      foods=list()
      costs=list()
      conn=connection1()
      mycursor=conn.cursor()
      global total
      total=0
      for i in fid:
        sql=f"SELECT `MenuItemName`,`Price`, `PreparationTime` FROM `menu` WHERE MenuItemID={i}"
        mycursor.execute(sql)
        data=mycursor.fetchall()
        
        for j in data:
          foods.append(j[0])
          costs.append(j[1])
          print(j[1]+4444)
          total = total + Decimal(j[1]) + Decimal('0.13') * Decimal(j[1])
       
      print(foods,costs,total)
      conn.commit()
      conn.close()
      Label(frame12,text="orders : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=0,column=0)
      Label(frame12,text=foods,font="helvetica 15 italic",bg=b,fg="light pink").grid(row=0,column=1)
      Label(frame12,text="prices : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=1,column=0)
      Label(frame12,text=costs,font="helvetica 15 italic",bg=b,fg="light pink").grid(row=1,column=1)
      Label(frame12,text="tax  : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=2,column=0)
      Label(frame12,text="13%",font="helvetica 15 italic",bg=b,fg="light pink").grid(row=2,column=1)
      Label(frame12,text="total : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=3,column=0)
      Label(frame12,text=total,font="helvetica 15 italic",bg=b,fg="light pink").grid(row=3,column=1)
      global bankid,key,rest
      Label(frame12,text="SMPK Resturant Account no. : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=5,column=0)
      rest=Entry(frame12,width=30,fg=b,font="helvetica 15 italic")
      rest.grid(row=5,column=1)
      rest.insert(0,"2591761497")
      rest.config(state="disabled")
      Label(frame12,text="SMPK Bank Account no. : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=6,column=0)
      bankid=Entry(frame12,width=30,fg=b,font="helvetica 15 italic")
      bankid.grid(row=6,column=1)
      Label(frame12,text="SMPK Bank Password : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=7,column=0)
      key=Entry(frame12,width=30,fg=b,font="helvetica 15 italic")
      key.grid(row=7,column=1)
      global tot
      tot=total
      #pay now
      img1=Image.open(r"images\images (1).png").resize((200,100))
      img1=ImageTk.PhotoImage(img1)
      global funid
      funid="food"
      btn3=Button(frame12,image=img1,border=0,bg=b,command=give)
      btn3.image=img1
      btn3.grid(row=8,column=0,columnspan=2,padx=20,pady=20)
      
    frame11=Frame(frame1,bg=b)
    frame11.pack()
    global contact
    Label(frame11,text="find my food",font="stencil 30 bold",bg=b,fg="white").grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    Label(frame11,text="customer name :",justify= "left",bg=b,font="stencil 15 bold",fg="light pink").grid(row=1,column=0,padx=10,pady=10)
    contact=Entry(frame11,fg=b,font="helvetica 15 italic",width=30)
    contact.grid(row=1,column=1,padx=10,pady=10)
    img1=Image.open(r"images\Find-magnifying-glass-search-icon-Graphics-13344255-1-1-580x376.jpg").resize((100,75))
    img1=ImageTk.PhotoImage(img1)
    btn1=Button(frame11,image=img1,border=0,bg=b,command=show)
    btn1.image=img1
    btn1.grid(row=2,column=0,columnspan=2,padx=20,pady=20)



def payforroom():
   
    global frame1,b,contact
    frame1.destroy()  # Destroy the existing frame
    frame1 = Frame(root)  # Recreate the frame
    frame1.configure(bg=b)
    frame1.pack()
    def show():
      id.config(state="disabled")
      btn1.destroy()
      frame12=Frame(frame1,bg=b)
      frame12.pack()
      conn=connection1()
      mycursor=conn.cursor()
      
      sql=f"SELECT `GuestID`, `Name`, `Contact`, `RoomID`, `RoomName` FROM `guests` WHERE `GuestID`='{id.get()}'"
      mycursor.execute(sql)
      global datax
      datax=mycursor.fetchone()
      print(datax)
      conn.commit()
      conn.close()
      
      conn = connection1()
      mycursor = conn.cursor()    
      sql = f"SELECT `Rate` FROM `rooms` WHERE `RoomID` = {datax[-2]}"
      mycursor.execute(sql)
      data1 = mycursor.fetchone()  # Fetch the result
      rate = data1[0]  # Convert fetched rate to Decimal
      tax_rate = float(0.13)
      rate=float(rate)
      print(tax_rate) # Convert tax rate to Decimal
      global tot
      tot = rate + rate * tax_rate  # Calculate total rate with taxrate = data1[0]
        # Extracting rate from the fetched result
      print("Rate:", tot)  # Printing the rate
      conn.close()  # Closing the connection

      Label(frame12,text="Sub Total : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=0,column=0)
      Label(frame12,text=rate,font="helvetica 15 italic",bg=b,fg="light pink").grid(row=0,column=1)
      Label(frame12,text="tax amount : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=2,column=0)
      Label(frame12,text=rate*0.13,font="helvetica 15 italic",bg=b,fg="light pink").grid(row=2,column=1)
      Label(frame12,text="tax  : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=1,column=0)
      Label(frame12,text="13%",font="helvetica 15 italic",bg=b,fg="light pink").grid(row=1,column=1)
      Label(frame12,text="total : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=3,column=0)
      Label(frame12,text=(rate+rate*0.13),font="helvetica 15 italic",bg=b,fg="light pink").grid(row=3,column=1)
      global bankid,key,rest
      Label(frame12,text="SMPK Resturant Account no. : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=5,column=0)
      rest=Entry(frame12,width=30,fg=b,font="helvetica 15 italic")
      rest.grid(row=5,column=1)
      rest.insert(0,"2591761497")
      rest.config(state="disabled")
      Label(frame12,text="SMPK Bank Account no. : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=6,column=0)
      bankid=Entry(frame12,width=30,fg=b,font="helvetica 15 italic")
      bankid.grid(row=6,column=1)
      Label(frame12,text="SMPK Bank Password : ",font="helvetica 15 italic",bg=b,fg="light blue").grid(row=7,column=0)
      key=Entry(frame12,width=30,fg=b,font="helvetica 15 italic")
      key.grid(row=7,column=1)

      #pay now
      img1=Image.open(r"images\images (1).png").resize((200,100))
      img1=ImageTk.PhotoImage(img1)
      global funid
      funid="hotel"
      btn3=Button(frame12,image=img1,border=0,bg=b,command=give)
      btn3.image=img1
      btn3.grid(row=8,column=0,columnspan=2,padx=20,pady=20)
      
    frame11=Frame(frame1,bg=b)
    frame11.pack()
    global id
    Label(frame11,text="find my room",font="stencil 30 bold",bg=b,fg="white").grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    Label(frame11,text="guest identification number :",justify= "left",bg=b,font="stencil 15 bold",fg="light pink").grid(row=1,column=0,padx=10,pady=10)
    id=Entry(frame11,fg=b,font="helvetica 15 italic",width=30)
    id.grid(row=1,column=1,padx=10,pady=10)
    img1=Image.open(r"images\Find-magnifying-glass-search-icon-Graphics-13344255-1-1-580x376.jpg").resize((100,75))
    img1=ImageTk.PhotoImage(img1)
    btn1=Button(frame11,image=img1,border=0,bg=b,command=show)
    btn1.image=img1
    btn1.grid(row=2,column=0,columnspan=2,padx=20,pady=20)

def pay():
   global frame1
   frame1.destroy()
   frame1=Frame(root,bg=b)
   frame1.pack()
   #food
   img1=Image.open(r"images\food-delivery-line-icon-meal-order-location-sign-vector-35351859.jpg").resize((300,300))
   img1=ImageTk.PhotoImage(img1)
   btn1=Button(frame1,image=img1,border=0,bg=b,command=payforfood)
   btn1.image=img1
   btn1.grid(row=0,column=0,padx=20,pady=20)

   #room
   img2=Image.open(r"images\hotel-check-in-registration-of-a-room-vector-23694094.jpg").resize((300,300))
   img2=ImageTk.PhotoImage(img2)
   btn2=Button(frame1,image=img2,border=0,bg=b,command=payforroom)
   btn2.image=img2
   btn2.grid(row=0,column=1,padx=20,pady=20)
def orderred(data):
   if (data[6]>0):
    global name,contact,email
    conn=connection1()
    mycursor=conn.cursor()
    currenttime=datetime.today().time().replace(microsecond=0)
    sql=f"INSERT INTO `pending_orders`(`id`, `customer`, `contact`, `email`,`start`) VALUES ({data[0]},'{name.get()}','{contact.get()}','{email.get()}','{currenttime}')"
    mycursor.execute(sql)
    conn.commit()
    conn.close()
    x=(int(data[6])-1)
    conn=connection1()
    mycursor=conn.cursor()
    sql=f"UPDATE `menu` SET `Availability`={x} WHERE `MenuItemID`={data[0]}"
    mycursor.execute(sql)
    conn.commit()
    conn.close()
    speak("order placed x=successfully")
    messagebox.showinfo("info","order placed successfully")
   else:
      speak("sorry this food is not availble right now")
      messagebox.showerror("error","sorry this food is not availble right now")
   global frame1
   frame1.destroy()
   frame1=Frame(root,bg=b)
   frame1.pack()
   main()
   
   



def place_order():
   global frame1
   frame1.destroy()
   frame1 = Frame(root, bg=b)
   frame1.pack()
   conn=connection1()
   mycursor=conn.cursor()
   sql=f"SELECT `MenuItemID`, `MenuItemName`, `Description`, `Category`, `Price`, `Ingredients`, `Availability`, `PreparationTime`, `Calories`, `SpecialInformation`, `MenuItemImage`, `MenuItemRating` FROM `menu` WHERE `MenuItemID`={food.get()}"
   mycursor.execute(sql)
   data=mycursor.fetchone()
   conn.commit()
   conn.close()
   global name,contact,email
   try:
    img1=Image.open(data[-2]).resize((300,300))
    img1=ImageTk.PhotoImage(img1)
    label=Label(frame1,image=img1,bg=b)
    label.image=img1
    label.grid(row=0,column=0,columnspan=2)
   except Exception as e:
      print(e)
   Label(frame1,text="MenuItemID",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=1,column=0)
   Label(frame1,text=data[0],font="helvetica 15 italic",bg=b,fg="#FFBE98").grid(row=1,column=1)
   Label(frame1,text="MenuItemName",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=2,column=0)
   Label(frame1,text=data[1],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=2,column=1)
   Label(frame1,text="Description",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=3,column=0)
   Label(frame1,text=data[2],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=3,column=1)
   Label(frame1,text="Category",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=4,column=0)
   Label(frame1,text=data[3],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=4,column=1)
   Label(frame1,text="Price",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=5,column=0)
   Label(frame1,text=data[4],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=5,column=1)
   Label(frame1,text="Ingredients",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=6,column=0)
   Label(frame1,text=data[5],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=6,column=1)
   Label(frame1,text="Availability",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=7,column=0)
   Label(frame1,text=data[6],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=7,column=1)
   Label(frame1,text="PreparationTime",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=8,column=0)
   Label(frame1,text=f"{data[7]} minutes",font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=8,column=1)
   Label(frame1,text="Calories",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=9,column=0)
   Label(frame1,text=data[8],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=9,column=1)
   Label(frame1,text="SpecialInformation",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=10,column=0)
   Label(frame1,text=data[9],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=10,column=1)
   Label(frame1,text="MenuItemRating",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=11,column=0)
   Label(frame1,text=data[11],font="helvetical 15 italic",bg=b,fg="#FFBE98").grid(row=11,column=1)
   Label(frame1,text="Name : ",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=12,column=0)
   name=Entry(frame1,font="helvetica 15 italic",width=30,fg="#FFBE98")
   name.grid(row=12,column=1)
   Label(frame1,text="contact : ",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=13,column=0)
   contact=Entry(frame1,font="helvetica 15 italic",width=30,fg="#FFBE98")
   contact.grid(row=13,column=1)
   Label(frame1,text="email : ",font="stencil 15 bold",bg=b,fg="#E3FEF7").grid(row=14,column=0)
   email=Entry(frame1,font="helvetica 15 italic",width=30,fg="#FFBE98")
   email.grid(row=14,column=1)
   img=Image.open(r"images\\360_F_289646929_mvmudLRuRSTKw38sbfANSoZcQwByTlV6.jpg").resize((150,75))
   img=ImageTk.PhotoImage(img)
   def go():
      orderred(data)
   btn=Button(frame1,image=img,command=go,bg=b,border=0,bd=0)
   btn.image=img
   btn.grid(row=15,column=0,columnspan=2,sticky=N)
   
def order_food():
    global frame1
    # Destroying the previous frame if exists
    if frame1:
        frame1.destroy()

    # Creating a new frame
    frame1 = Frame(root, bg=b)
    frame1.pack()

    # Loading and displaying the menu image
    imgfood = Image.open(r"images/Food-Menu-Card-Template-1.jpg").resize((500, 400))
    imgfood = ImageTk.PhotoImage(imgfood)
    label = Label(frame1, image=imgfood, bg=b)
    label.image = imgfood
    label.grid(row=0, column=0, columnspan=5)

    # Fetching menu data from the database
    conn = connection1()
    if conn:
        mycursor = conn.cursor()
        sql = "SELECT `MenuItemID`, `MenuItemName`,  `Category`, `Price`, `Availability`,  `MenuItemRating` FROM `menu` "
        mycursor.execute(sql)
        data = mycursor.fetchall()

        if data:
          # Creating a treeview to display menu items
          tree = ttk.Treeview(frame1, columns=("MenuItemID", "MenuItemName", "Category", "Price", "Availability", "MenuItemRating"))
          tree.heading("MenuItemID", text="MenuItemID")
          tree.heading("MenuItemName", text="MenuItemName")
          tree.heading("Category", text="Category")
          tree.heading("Price", text="Price")
          tree.heading("Availability", text="Availability")
          tree.heading("MenuItemRating", text="MenuItemRating")
          # Adjusting column widths
          tree.column("MenuItemID", width=100)
          tree.column("MenuItemName", width=150)
          tree.column("Category", width=100)
          tree.column("Price", width=60)
          tree.column("Availability", width=120)
          tree.column("MenuItemRating", width=110)
          # Adding a scrollbar
          scrollbar = ttk.Scrollbar(frame1, orient="vertical", command=tree.yview)
          scrollbar.grid(row=1, column=2, sticky="ns", padx=10, pady=10)
          tree.configure(yscrollcommand=scrollbar.set)
          # Inserting data into the treeview
          for record in data:
              tree.insert("", "end", values=record)
          # Placing the treeview
          tree.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
          # Styling the treeview
          style = ttk.Style()
          style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), foreground="#E59BE9")
          style.configure("Treeview", font=("helvetica", 12, "italic"), background=b, foreground="#E59BE9")
          # Closing the database connection
          conn.close()
    frame2=Frame(frame1,bg=b)
    frame2.grid(row=3,column=0,columnspan=3)
    Label(frame2,text="food id : ",bg=b,fg="white",font="stencil 20 bold",anchor=CENTER).grid(row=0,column=0,sticky=N,padx=10,pady=10)
    global food
    food=StringVar()
    Entry(frame2,textvariable=food,width=30,fg=b,font="ariel 10 italic").grid(row=0,column=1,sticky=N,padx=10,pady=20)
    img1=Image.open(r"images\360_F_676465704_6ZcQMlbQdisl3oGcS22UUC04dMSuM0hn.jpg").resize((100,50))
    img1=ImageTk.PhotoImage(img1)
    btn=Button(frame2,image=img1,command=place_order,border=0,bd=0,bg=b)
    btn.image=img1
    btn.grid(row=1,column=0,sticky=N,columnspan=3)
root=Tk()
root.title("resturant management system")
root.iconbitmap(r"images/1496677256-3_84637.ico")
b="#865DFF"
root.configure(bg=b)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)

global frame1
frame1=Frame(root,bg=b)
frame1.pack()
def  main():
  Label(frame1,text="smpk resturant and lodge",font="stencil 30 bold",fg="white",bg=b).grid(row=0,column=0,columnspan=10)
  img=Image.open(r"images/img-20160718-194703-largejpg.jpg").resize((500,300))
  img=ImageTk.PhotoImage(img)
  label=Label(frame1,image=img)
  label.image=img
  label.grid(row=1,column=0,columnspan=10)
  Label(frame1, text="""
      Welcome to SMPK Restaurant and Lodge! We understand that finding a comfortable and enjoyable dining and accommodation
      experience is essential. That's why we're dedicated to providing you with a delightful and relaxing stay at our   
      establishment. Our restaurant offers a diverse menu of mouthwatering dishes prepared by skilled chefs, ensuring
      a memorable culinary experience.Whether you're here for a quick bite or a leisurely dining experience, we have options
      to suit every palate. Our lodge provides cozy and well-appointed rooms designed to make you feel at home during your 
      stay. With amenities such as complimentary Wi-Fi and room service, we strive to make your visit as comfortable as 
      possible. Our attentive staff is always on hand to cater to your needs and ensure your satisfaction.We also offer 
      flexible booking options and special packages to accommodate your preferences and budget. Whether you're traveling for 
      business or leisure, SMPK Restaurant and Lodge is your ideal destination. Thank you for choosing us. We look forward to
      providing you with a memorable dining and lodging  experience.""",
        font="helvetica 15 italic", bg=b,fg="#FBFFB1").grid(row=2, column=0, columnspan=10)

  #see avaibility
  img1=Image.open(r"images/images.png").resize((100,50))
  img1=ImageTk.PhotoImage(img1)
  btn=Button(frame1,image=img1,bg=b,command=checkin,border=0,bd=0)
  btn.image=img1
  btn.grid(row=5,column=0)

  #check out
  img2=Image.open(r"images/360_F_494920621_A8MW4s5rZ9hU0hwPVFXFFXNrw1oK1TkQ.jpg").resize((100,50))
  img2=ImageTk.PhotoImage(img2)
  btn2=Button(frame1,image=img2,bg=b,command=payforroom,border=0,bd=0)
  btn2.image=img2
  btn2.grid(row=5,column=1)

  #pay
  img3=Image.open(r"images/E36JpOcX0AIMpGd.png").resize((100,50))
  img3=ImageTk.PhotoImage(img3)
  btn3=Button(frame1,image=img3,bg=b,command=pay,border=0,bd=0)
  btn3.image=img3
  btn3.grid(row=5,column=2)

  #food
  img4=Image.open(r"images/online-ordering_900x600.jpg").resize((100,50))
  img4=ImageTk.PhotoImage(img4)
  btn4=Button(frame1,image=img4,bg=b,command=order_food,border=0,bd=0)
  btn4.image=img4
  btn4.grid(row=5,column=3)

  #whatsapp
  img5=Image.open(r"images/733641.png").resize((100,50))
  img5=ImageTk.PhotoImage(img5)
  btn5=Button(frame1,image=img5,background=b,command=whatsapp,border=0,bd=0)
  btn5.image=img5
  btn5.grid(row=5,column=4)

  #mail
  img6=Image.open(r"images/free-mail-icon-142-thumb.png").resize((100,50))
  img6=ImageTk.PhotoImage(img6)
  btn6=Button(frame1,image=img6,bg=b,command=mail,border=0,bd=0)
  btn6.image=img6
  btn6.grid(row=5,column=5)

  #telegram
  img7=Image.open(r"images/3488463.png").resize((100,50))
  img7=ImageTk.PhotoImage(img7)
  btn7=Button(frame1,image=img7,bg=b,command=telegram,border=0,bd=0)
  btn7.image=img7
  btn7.grid(row=5,column=6)

main()
root.mainloop()