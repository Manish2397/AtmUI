from tkinter import *

root = Tk()
pin = 0

l1 = Label(root, text="Bank Of India", width="20", height="3",bd=1,anchor=CENTER)
screen=Label(root, text=0, width="18", height="6")
prompt=Label(root, text="Enter your 4 digit pin", width="18", height="6")
flag=0
# l2= tk.Label(root, text="Red Sun", bg="red", width="20", height="3")
# l3= tk.Label(root, text="Red Sun", bg="red", width="20", height="3")

keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '9', '#'],
]
def collectMoney():
    prompt["text"]="Collect Your Money"
    screen.destroy()
def amountScreen():
    prompt["text"]="Enter amount"
    pin=0
    screen["text"]=0
    btns = Button(root, text="Next", height="6", width="12", command=collectMoney)
    btns.grid(row=5, column=0)



def pinChange1():
    pin=screen["text"]
    pin=pin*10+1
    print(pin)
    screen["text"]=pin


def pinChange2():
    pin = screen["text"]
    pin = pin * 10 + 2
    print(pin)
    screen["text"] = pin

def pinChange3():
    pin = screen["text"]
    pin = pin * 10 + 3
    print(pin)
    screen["text"] = pin
def pinChange4():
    pin = screen["text"]
    pin = pin * 10 + 4
    print(pin)
    screen["text"] = pin
def pinChange5():
    pin = screen["text"]
    pin = pin * 10 + 5
    print(pin)
    screen["text"] = pin

def pinChange6():
    pin = screen["text"]
    pin = pin * 10 + 6
    print(pin)
    screen["text"] = pin
def pinChange7():
    pin = screen["text"]
    pin = pin * 10 + 7
    print(pin)
    screen["text"] = pin
def pinChange8():
    pin = screen["text"]
    pin = pin * 10 + 8
    print(pin)
    screen["text"] = pin
def pinChange9():
    pin = screen["text"]
    pin = pin * 10 + 9
    print(pin)
    screen["text"] = pin
def pinChanges():
    pass
def pinChange0():
    pin = screen["text"]
    pin = pin * 10
    print(pin)
    screen["text"] = pin
def pinChangeh():
    pin = screen["text"]
    pin = pin//10
    print(pin)
    screen["text"] = pin


def clickMe():
    cashWithdrawBtn.destroy()
    transferBtn.destroy()
    changeCardSettingBtn.destroy()
    balanceInquiryBtn.destroy()
    billPaymentBtn.destroy()
    offersBtn.destroy()
    l1.destroy()


    # create global variable for pin
      # empty string

    screen.grid(row=1,column=0,columnspan=3)
    prompt.grid(row=0,column=0,columnspan=3)
    btn1 = Button(root, text=1, height="6", width="12", command=pinChange1)
    btn2 = Button(root, text=2, height="6", width="12", command=pinChange2)
    btn3 = Button(root, text=3, height="6", width="12", command=pinChange3)
    btn4 = Button(root, text=4, height="6", width="12", command=pinChange4)
    btn5 = Button(root, text=5, height="6", width="12", command=pinChange5)
    btn6 = Button(root, text=6, height="6", width="12", command=pinChange6)
    btn7 = Button(root, text=7, height="6", width="12", command=pinChange7)
    btn8 = Button(root, text=8, height="6", width="12", command=pinChange8)
    btn9 = Button(root, text=9, height="6", width="12", command=pinChange9)
    btns = Button(root, text="Next", height="6", width="12", command=amountScreen)
    btn0 = Button(root, text=0, height="6", width="12", command=pinChange0)
    btnh = Button(root, text="<--", height="6", width="12", command=pinChangeh)
    btnh = Button(root, text="<--", height="6", width="12", command=pinChangeh)
    btn1.grid(row=2, column=0)
    btn2.grid(row=2, column=1)
    btn3.grid(row=2, column=2)
    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)
    btn7.grid(row=4, column=0)
    btn8.grid(row=4, column=1)
    btn9.grid(row=4, column=2)
    btns.grid(row=5, column=0)
    btn0.grid(row=5, column=1)
    btnh.grid(row=5, column=2)



cashWithdrawBtn = Button(root,text="Cash Withdrawal",height="6",width="20",command= clickMe)
transferBtn = Button(root,text="Transfer",height="6",width="20")
changeCardSettingBtn = Button(root,text="Change Card Setting",height="6",width="20")
balanceInquiryBtn = Button(root,text="Balance Inquiry",height="6",width="20")
billPaymentBtn = Button(root,text="Bill Payment",height="6",width="20")
offersBtn = Button(root,text="Donation/Offers",height="6",width="20")

l1.grid(row=0,column=0,ipadx=20,ipady=20,columnspan=3)
cashWithdrawBtn.grid(row=1,column=0,padx=(0,100))
transferBtn.grid(row=1,column=1,padx=(100,0))
changeCardSettingBtn.grid(row=2,column=0,padx=(0,100))
balanceInquiryBtn.grid(row=2,column=1,padx=(100,0))
billPaymentBtn.grid(row=3,column=0,padx=(0,100))
offersBtn.grid(row=3,column=1,padx=(100,0))


root.mainloop()