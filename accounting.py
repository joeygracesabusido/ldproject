from distutils import command
from importlib.resources import contents
from tkinter import *
import csv
# from types import NoneType
from PIL import Image, ImageTk
import PIL.Image
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import datetime as dt
from numpy import True_, true_divide
from tkcalendar import DateEntry
from tkcalendar import DateEntry as TkcDateEntry
import tkinter as tk
from tkinter import scrolledtext
import time
import datetime
import tkinter.messagebox as tkMessageBox
from tkinter import messagebox
from reportlab.pdfgen.canvas import Canvas
from PollyReports import *
from os import startfile
import xlsxwriter

from datetime import date, timedelta
from datetime import datetime

#from PIL import ImageTk, Image as PILImage
#from payroll import selectTransaction
import babel.numbers

from tkinter.scrolledtext import ScrolledText

from pymongo import MongoClient
import pandas as pd
import re
# from datetime import timedelta 

from bson.objectid import ObjectId
import dateutil.parser
import pymongo

import certifi
ca = certifi.where()


client = pymongo.MongoClient(f"mongodb+srv://joeysabusido:genesis11@cluster0.bmdqy.mongodb.net/ldglobal?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.ldglobal





root = Tk()
root.title("JRS SYSTEM")

width = 750
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="skyblue")

#load = Image.open("image\login.png").convert("RGB")
load = PIL.Image.open("image\login.png")
load =load.resize((130, 130), PIL.Image.ANTIALIAS)
logo_icon = ImageTk.PhotoImage(load)

def clearpayrollFrame():
    # destroy all widgets from frame
    for widget in payroll_frame.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    payroll_frame.pack_forget()

def cleartrialbalanceFrame():
    # destroy all widgets from frame
    for widget in accounting_frame.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    accounting_frame.pack_forget()

def clearFrame():
    # destroy all widgets from frame
    for widget in MidViewForm9.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    MidViewForm9.pack_forget()
#======================================Account Payable Frame===================================================
def testing_dictionary2():
    """
    """
    for i in data:
        
        print(i,data[i]['date_entry'])
    

def testing_dictionary():
    """
    this function is for
    testing dictionaries
    """
    global data
    collection = db['journal_entry']


    answer = 'yes'
    date_time_obj = ""

    journal = ""
    ref = ""
    journalMemo =""
    acountNumber = ""
    accountTitle = ""
    bsClass = ""
    debit_amount = 0
    credit_amount = 0
    user = ''
    data ={}
    cnt =0 
    # while answer == 'yes':

    # collection = db['journal_entry'] # this is to create collection and save as table
    # dateEntry =  journalEntryInsert_datefrom.get()
    # date_time_obj = datetime.strptime(dateEntry, '%m/%d/%Y')

    # journal = journal_manual.get(),
    # ref = reference_manual_entry.get(),
    # journalMemo = journal_memo_entry.get('1.0', 'end-1c'),
    # acountNumber = account_number_entry.get(),
    # accountTitle = chart_of_account_manual.get(),
    # bsClass = bs_class_entry.get(),
    # debit_amount = float(debit_manual_entry.get())
    # credit_amount = float(credit_manual_entry.get())
    # user = USERNAME.get(),
    # answer = tkMessageBox.askquestion('JRS','Are you sure you want to add?',icon="warning")

    # while answer =='yes':
    dateEntry =  journalEntryInsert_datefrom.get()
    date_time_obj = datetime.strptime(dateEntry, '%m/%d/%Y')

    journal = journal_manual.get(),
    ref = reference_manual_entry.get(),
    journalMemo = journal_memo_entry.get('1.0', 'end-1c'),
    acountNumber = account_number_entry.get(),
    accountTitle = chart_of_account_manual.get(),
    bsClass = bs_class_entry.get(),
    debit_amount = float(debit_manual_entry.get())
    credit_amount = float(credit_manual_entry.get())
    user = USERNAME.get(),

    answer = tkMessageBox.askquestion('JRS','Are you sure you want to add?',icon="warning")
    
    if answer =='yes':
        add_entryFields1()
        # dateEntry =  journalEntryInsert_datefrom.get()
        # date_time_obj = datetime.strptime(dateEntry, '%m/%d/%Y')

        # journal = journal_manual.get(),
        # ref = reference_manual_entry.get(),
        # journalMemo = journal_memo_entry.get('1.0', 'end-1c'),
        # acountNumber = account_number_entry.get(),
        # accountTitle = chart_of_account_manual.get(),
        # bsClass = bs_class_entry.get(),
        # debit_amount = float(debit_manual_entry.get())
        # credit_amount = float(credit_manual_entry.get())
        # user = USERNAME.get(),
    
    else:
        data.update({len(data)+1:{
            'date_entry': date_time_obj,
            'journal': journal,
            'ref': ref,
            'descriptions': journalMemo,
            'acoount_number': acountNumber,
            'account_disc': accountTitle,
            'bsClass':bsClass,
            'debit_amount': debit_amount,
            'credit_amount': credit_amount,
            'user': user,
            'created':datetime.now()
        }})


    for i in data:
    
        print(i,data[i]['account_disc'])

        # dataInsert = {
        # 'date_entry': data[i]['date_entry'],
        # 'journal': data[i]['journal'],
        # 'ref': data[i]['ref'],
        # 'descriptions': data[i]['descriptions'],
        # 'acoount_number':data[i]['acoount_number'],
        # 'account_disc': data[i]['account_disc'],``````````````````````````````````````````
        # 'bsClass':data[i]['bsClass'],
        # 'debit_amount': data[i]['debit_amount'],
        # 'credit_amount': data[i]['credit_amount'],
        # 'user': data[i]['user'],
        # 'created':data[i]['created']
        # }

        # try:
        #     collection.insert_one(dataInsert)

            
        
        # except Exception as ex:
        #     print("Error", f"Error due to :{str(ex)}") 

def delete_journalEntry_apv():
    """
    this function is for
    deleting journal entry
    """
    dataSearch = db['journal_entry']
    query = {'_id': ObjectId(Selected_ID_entry.get())}
    result = tkMessageBox.askquestion('JRS','Are you sure you want to Update?',icon="warning")
    if result == 'yes':
        x = dataSearch.delete_one(query)
        messagebox.showinfo('JRS', 'Selected Record has been deleted')
        journalEntryManual_list_treeview_apv()

# this is for supplier_entry APv data base entry
def auto_dueDate_computation(e):
    """
    this function
    is for auto complete
    for account number
    """

    NumDays = int(dueDate_apv_entry.get())
    dateEntry_From =  journalEntryInsert_datefrom.get()
    date_time_obj = datetime.strptime(dateEntry_From, '%m/%d/%Y')

    DueDate =  (date_time_obj + timedelta(days=NumDays))

    
    journalEntryInsert_Duedate.delete(0, END)
    journalEntryInsert_Duedate.insert(0, (DueDate))
    

def suppier_entry_apv():
    """
    This function is for saving
    supplier info of payables
    """

    debit_entry = float(debit_manual_entry.get())
    
    
    credit_entry = float(credit_manual_entry.get())
    

    dateEntry =  journalEntryInsert_datefrom.get()
    date_time_obj = datetime.strptime(dateEntry, '%m/%d/%Y')
    
    
    collection = db['journal_entry'] # this is to create collection and save as table
    dataInsert = {
    # 'date_entry': journalEntryInsert_datefrom.get(),
    'date_entry': date_time_obj,
    'journal': journal_manual.get(),
    'ref': reference_manual_entry_apv.get(),
    'descriptions': journal_memo_entry.get('1.0', 'end-1c'),
    'acoount_number': account_number_entry.get(),
    'account_disc': chart_of_account_manual.get(),
    'bsClass': bs_class_entry.get(),
    'debit_amount': debit_entry,
    'credit_amount': credit_entry,
    'due_date_apv': journalEntryInsert_Duedate.get(),
    'terms_days': dueDate_apv_entry.get(),
    'supplier/Client': supplier_apv_entry.get(),
    'user': USERNAME.get(),
    'created':datetime.now()
    
    }

    
    
    try:
        collection.insert_one(dataInsert)

       
        
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")    
                   
   




def updated_journalEntry_apv():
    """
    This function is for 
    updating journal entry
    """
    dataSearch = db['journal_entry']
    query = {'_id': ObjectId(Selected_ID_entry.get())}

    result = tkMessageBox.askquestion('JRS','Are you sure you want to Update?',icon="warning")
    if result == 'yes':
        dateEntry =  journalEntryInsert_datefrom.get()
        date_time_obj = datetime.strptime(dateEntry, '%m/%d/%Y')
        try:
            newValue = { "$set": { "date_entry": date_time_obj,
                                 "journal": journal_manual.get(), 
                                 "ref": reference_manual_entry_apv.get(),
                                 "descriptions": journal_memo_entry.get('1.0', 'end-1c'),
                                 "acoount_number": account_number_entry.get(),
                                     "account_disc": chart_of_account_manual.get(),
                                     "debit_amount": float(debit_manual_entry.get()), 
                                     "credit_amount": float(credit_manual_entry.get()),}           
                                    }
            dataSearch.update_many(query, newValue)
            messagebox.showinfo('JRS', 'Data has been updated')
            journalEntryManual_list_treeview_apv()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}")


def select_record_treeview_apv():
    """
    this function is for
    selecting record from
    treeview
    """
    journalEntryInsert_datefrom.delete(0, END)
    journal_manual.delete(0, END)
    reference_manual_entry_apv.delete(0, END)
    journal_memo_entry.delete('1.0', END)
    account_number_entry.delete(0, END)
    chart_of_account_manual.delete(0, END)
    debit_manual_entry.delete(0, END)
    credit_manual_entry.delete(0, END)
    Selected_ID_entry.delete(0, END)
    bs_class_entry.delete(0, END)
    journalEntryInsert_Duedate.delete(0, END),
    dueDate_apv_entry.delete(0, END),
    supplier_apv_entry.delete(0, END),


    selected = journalEntryManual_apv_treeview.focus()
    values = journalEntryManual_apv_treeview.item(selected)
    selectedItems = values['values']
    


    dataSearch = db['journal_entry']
    query = {'_id': ObjectId(selectedItems[0])}
    try:
       
        
        for x in dataSearch.find(query):
            
            id_num = x['_id']
            date_entry = x['date_entry']
            journal = x['journal']
            ref = x['ref']
            descriptions = x['descriptions']
            account_number = x['acoount_number']
            account_disc = x['account_disc']
            debit_amount = x['debit_amount']
            debit_amount2 = '{:,.2f}'.format(debit_amount)
            credit_amount = x['credit_amount']
            credit_amount2 = '{:,.2f}'.format(credit_amount)
            bs_class = x['bsClass']
            due_date = x['due_date_apv']
            terms = x['terms_days']
            supplier_client = x['supplier/Client']
            
            journalEntryInsert_datefrom.insert(0, date_entry)
            journal_manual.insert(0, journal)
            reference_manual_entry_apv.insert(0, ref)
            journal_memo_entry.insert('1.0', descriptions)
            account_number_entry.insert(0, account_number)
            chart_of_account_manual.insert(0, account_disc)
            debit_manual_entry.insert(0, debit_amount)
            credit_manual_entry.insert(0, credit_amount)
            Selected_ID_entry.insert(0, id_num)
            bs_class_entry.insert(0, bs_class)
            journalEntryInsert_Duedate.insert(0, due_date),
            dueDate_apv_entry.insert(0, terms),
            supplier_apv_entry.insert(0, supplier_client),
            

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")

    


def journalEntryManual_list_treeview_apv():
    
    """
    this function is for
    button to display the list
    of income Statement as per query
    """
    
    journalEntryManual_apv_treeview.delete(*journalEntryManual_apv_treeview.get_children())
    return journalEntry_manual_list_apv()
def journalEntry_manual_list_apv():
    """
    This function is for manual
    entry list
    """
    dataSearch = db['journal_entry']
    query = {'ref':reference_manual_entry_apv.get() }

    # query ==""
    # if query == "":
    #     messagebox.showinfo("Error","No Record found" )
    # else:
    try:
        cnt = 0
        debit_amount_total = 0
        credit_amount_total= 0
        
        for x in dataSearch.find(query):
            cnt+=1
            id_num = x['_id']
            date_entry = x['date_entry']
            journal = x['journal']
            ref = x['ref']
            descriptions = x['descriptions']
            account_number = x['acoount_number']
            account_disc = x['account_disc']
            debit_amount = x['debit_amount']
            debit_amount2 = '{:,.2f}'.format(debit_amount)
            credit_amount = x['credit_amount']
            credit_amount2 = '{:,.2f}'.format(credit_amount)
            
            debit_amount_total+=debit_amount
            debit_amount_total2 = '{:,.2f}'.format(debit_amount_total)

            credit_amount_total+=credit_amount
            credit_amount_total2 = '{:,.2f}'.format(credit_amount_total)
            
            journalEntryManual_apv_treeview.insert('', 'end', values=(id_num,date_entry,journal,
                                ref,descriptions, account_number,account_disc,debit_amount2,
                                credit_amount2 ))

            totalDebit_manual_entry.delete(0, END)
            totalDebit_manual_entry.insert(0, (debit_amount_total2))


            totalCredit_manual_entry.delete(0, END)
            totalCredit_manual_entry.insert(0, (credit_amount_total2))

        # for x in dataSearch.find({"ref": {"$exists": True}}):
        #     print(x)
            # a = x['ref']
            # if a =='':
            #     messagebox.showinfo("Error","No Record found" )
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")


def add_entryFields1():
    """
    This function is to
    add Entryfields and delete/edit/
    """
   
    global account_number_entry
    account_number_entry = Entry(accountPayable_frame, width=12, font=('Arial', 10), justify='right')
    account_number_entry.place(x=10, y=260)


    global chart_of_account_manual
    chart_of_account_manual = ttk.Combobox(accountPayable_frame, width=39)
    chart_of_account_manual['values'] = chart_of_account_list()
    chart_of_account_manual.place(x=110, y=260)
    chart_of_account_manual.bind("<<ComboboxSelected>>", auto_account_num)


    global debit_manual_entry
    debit_manual_entry = Entry(accountPayable_frame, width=16, font=('Arial', 10), justify='right')
    debit_manual_entry.place(x=390, y=260)

   

    global credit_manual_entry
    credit_manual_entry = Entry(accountPayable_frame, width=16, font=('Arial', 10), justify='right')
    credit_manual_entry.place(x=520, y=260)

    global bs_class_entry
    bs_class_entry = Entry(accountPayable_frame, width=16, font=('Arial', 10), justify='right')
    bs_class_entry.place(x=650, y=260)

    btn_add_entry = Button(accountPayable_frame, text='Add', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=14, height=1
                              )
    btn_add_entry.place(x=815, y=260)

def insert_journalEntry_manual_apv():
    """
    this function is for inserting
    record to journal_entry
    """

    debit_entry = float(debit_manual_entry.get())
    
    
    credit_entry = float(credit_manual_entry.get())
    

    dateEntry =  journalEntryInsert_datefrom.get()
    date_time_obj = datetime.strptime(dateEntry, '%m/%d/%Y')
    
    
    collection = db['journal_entry'] # this is to create collection and save as table
    dataInsert = {
    # 'date_entry': journalEntryInsert_datefrom.get(),
    'date_entry': date_time_obj,
    'journal': journal_manual.get(),
    'ref': reference_manual_entry_apv.get(),
    'descriptions': journal_memo_entry.get('1.0', 'end-1c'),
    'acoount_number': account_number_entry.get(),
    'account_disc': chart_of_account_manual.get(),
    'bsClass': bs_class_entry.get(),
    'debit_amount': debit_entry,
    'credit_amount': credit_entry,
    'due_date_apv': journalEntryInsert_Duedate.get(),
    'terms_days': dueDate_apv_entry.get(),
    'supplier/Client': supplier_apv_entry.get(),
    'user': USERNAME.get(),
    'created':datetime.now()
    
    
    }

    
    
    try:
        collection.insert_one(dataInsert)

        account_number_entry.delete(0, END)
        chart_of_account_manual.delete(0, END)
        debit_manual_entry.delete(0, END)
        credit_manual_entry.delete(0, END)
        
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")    
                   
    messagebox.showinfo('JRS', 'Data has been exported and save')
    journalEntryManual_list_treeview_apv()




    
def supplier_list():
    """
    this function is for 
    the displaying chart of 
    account to dropdown menu
    or combo box
    """  
    dataSearch = db['supplier_db'] 
    # agg_result = dataSearch.find()
    agg_result = dataSearch.find().sort('supplierName', pymongo.ASCENDING)

    data = []
    for x in agg_result:
        data.append(x['supplierName'])
    return data


def autoIncrement_accountsPayable_ref():
    """
    This function is for
    autoincrement Number
    for reference in
    Account Payable
    """


    dataSearch = db['journal_entry']
    agg_result = dataSearch.find({'ref': {"$regex": "^APV"}}).sort('ref',-1).limit(1)

    a = ""
    for x in agg_result :
        a = x['ref']


        # current_year =  datetime.today().year
    if a =="":
        test_str = 'APV-000'
        res = test_str

        reference_manual_entry_apv.delete(0, END)
        reference_manual_entry_apv.insert(0, (res))
        
        
    
    else:
        

        reference_manual = a 
        res = re.sub(r'[0-9]+$',
                lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}", 
                reference_manual)

        reference_manual_entry_apv.delete(0, END)
        reference_manual_entry_apv.insert(0, (res))

def accountPayble_insert_frame():
    """
    This function is
    for Account Payable Voucher
    """
    clearFrame()

    global accountPayable_frame
    accountPayable_frame = Frame(MidViewForm9, width=1120, height=575, bd=2, bg='gray', relief=SOLID)
    accountPayable_frame.place(x=160, y=8)
   
    entry_date_label = Label(accountPayable_frame, text='Date:', width=14, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    entry_date_label.place(x=10, y=35)

    global journalEntryInsert_datefrom
    journalEntryInsert_datefrom = DateEntry(accountPayable_frame, width=15, background='darkblue',
                                  date_pattern='MM/dd/yyyy',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    journalEntryInsert_datefrom.place(x=170, y=35)
    journalEntryInsert_datefrom.configure(justify='center')
    journalEntryInsert_datefrom.bind("<<DateEntrySelected>>", auto_dueDate_computation)


    entry_date_label = Label(accountPayable_frame, text='Due Date:', width=14, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    entry_date_label.place(x=290, y=35)

    global journalEntryInsert_Duedate
    journalEntryInsert_Duedate = DateEntry(accountPayable_frame, width=15, background='darkblue',
                                  date_pattern='MM/dd/yyyy',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    journalEntryInsert_Duedate.place(x=430, y=35)
    journalEntryInsert_Duedate.configure(justify='center')


    account_number_lbl = Label(accountPayable_frame, text='Terms in days:', width=14, height=1, bg='yellow', 
                          fg='black',
                          font=('Arial', 10), anchor='e')
    account_number_lbl.place(x=10, y=5)

    global dueDate_apv_entry
    dueDate_apv_entry = Entry(accountPayable_frame, width=12, font=('Arial', 10), justify='right')
    dueDate_apv_entry.place(x=170, y=5)
    


    journal_label = Label(accountPayable_frame, text='Journal:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    journal_label.place(x=10, y=70)

    global journal_manual
    
    journal_manual = ttk.Combobox(accountPayable_frame, width=14)
    journal_manual['values'] = ("Payments", "Receipts", "Sales", "Purchases",'General')
    journal_manual.place(x=170, y=70)

    supplier_label = Label(accountPayable_frame, text='Supplier:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    supplier_label.place(x=290, y=70)

    # global supplier_apv_entry
    # supplier_apv_entry = Entry(accountPayable_frame, width=25, font=('Arial', 10), justify='right')
    # supplier_apv_entry.place(x=430, y=70)
    global supplier_apv_entry
    supplier_apv_entry = ttk.Combobox(accountPayable_frame, width=35)
    supplier_apv_entry['values'] = supplier_list()
    supplier_apv_entry.place(x=430, y=70)
    # supplier_apv_entry.bind("<<ComboboxSelected>>", auto_account_num)

    reference_label = Label(accountPayable_frame, text='reference:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    reference_label.place(x=10, y=105)

    global reference_manual_entry_apv
    reference_manual_entry_apv = Entry(accountPayable_frame, width=12, font=('Arial', 10), justify='right')
    reference_manual_entry_apv.place(x=170, y=105)

    
    journal_memo_lbl = Label(accountPayable_frame, text='Journal Memo:', width=14, height=1, bg='yellow', 
                          fg='black',
                          font=('Arial', 10), anchor='e')
    journal_memo_lbl.place(x=10, y=140)

    global journal_memo_entry
    journal_memo_entry = scrolledtext.ScrolledText(accountPayable_frame,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
    journal_memo_entry.place(x=170, y=140)


    account_number_lbl = Label(accountPayable_frame, text='Acct Number:', width=10, height=1, bg='yellow', 
                          fg='black',
                          font=('Arial', 10), anchor='e')
    account_number_lbl.place(x=10, y=200)

    global account_number_entry
    account_number_entry = Entry(accountPayable_frame, width=12, font=('Arial', 10), justify='right')
    account_number_entry.place(x=10, y=235)

    account_title_lbl = Label(accountPayable_frame, text='Acct Title:', width=32, height=1, bg='yellow', 
                          fg='black',
                          font=('Arial', 10), anchor='c')
    account_title_lbl.place(x=110, y=200)

    global chart_of_account_manual
    chart_of_account_manual = ttk.Combobox(accountPayable_frame, width=39)
    chart_of_account_manual['values'] = chart_of_account_list()
    chart_of_account_manual.place(x=110, y=235)
    chart_of_account_manual.bind("<<ComboboxSelected>>", auto_account_num)



    debitManual_label = Label(accountPayable_frame, text='Debit:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='c')
    debitManual_label.place(x=390, y=200)

    global debit_manual_entry
    debit_manual_entry = Entry(accountPayable_frame, width=16, font=('Arial', 10), justify='right')
    debit_manual_entry.place(x=390, y=235)

    creditManual_label = Label(accountPayable_frame, text='Credit:', 
                                            width=14, height=1, bg='yellowgreen', fg='black',
                                             font=('Arial', 10), anchor='c')
    creditManual_label.place(x=520, y=200)

    global credit_manual_entry
    credit_manual_entry = Entry(accountPayable_frame, width=16, font=('Arial', 10), justify='right')
    credit_manual_entry.place(x=520, y=235)

    bs_class_label = Label(accountPayable_frame, text='BS Class:', 
                                            width=14, height=1, bg='yellowgreen', fg='black',
                                             font=('Arial', 10), anchor='c')
    bs_class_label.place(x=650, y=200)

    global bs_class_entry
    bs_class_entry = Entry(accountPayable_frame, width=16, font=('Arial', 10), justify='right')
    bs_class_entry.place(x=650, y=235)

    # btn_add_entry = Button(accountPayable_frame, text='Add', bd=2, bg='blue', fg='white',
    #                           font=('arial', 10), width=14, height=1,
    #                            command=testing_dictionary)
    # btn_add_entry.place(x=815, y=235)



    selected_label = Label(accountPayable_frame, text='Transaction ID:', 
                                            width=14, height=1, bg='yellowgreen', fg='black',
                                             font=('Arial', 10), anchor='c')
    selected_label.place(x=900, y=235)

    global Selected_ID_entry
    Selected_ID_entry = Entry(accountPayable_frame, width=16, font=('Arial', 10), justify='right')
    Selected_ID_entry.place(x=1020, y=235)


    grand_total_label = Label(accountPayable_frame, text='TOTAL', 
                                            width=14, height=1, bg='yellowgreen', fg='black',
                                             font=('Arial', 10), anchor='c')
    grand_total_label.place(x=650, y=490)

   
    
    global totalDebit_manual_entry
    totalDebit_manual_entry = Entry(accountPayable_frame, width=16, font=('Arial', 10), justify='right')
    totalDebit_manual_entry.place(x=880, y=490)


   
    
    global totalCredit_manual_entry
    totalCredit_manual_entry = Entry(accountPayable_frame, width=16, font=('Arial', 10), justify='right')
    totalCredit_manual_entry.place(x=1000, y=490)
    
    
    
    btn_batch_entry_apv = Button(accountPayable_frame, text='Add Batch Entry', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=autoIncrement_accountsPayable_ref)
    btn_batch_entry_apv.place(x=670, y=35)

    btn_JournalManual_entry_apv = Button(accountPayable_frame, text='Insert Entry', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=insert_journalEntry_manual_apv)
    btn_JournalManual_entry_apv.place(x=670, y=70)

    btn_selected_apv = Button(accountPayable_frame, text='Selected', bd=2, bg='khaki', fg='black',
                              font=('arial', 10), width=14, height=1,
                               command=select_record_treeview_apv)
    btn_selected_apv.place(x=670, y=105)

    btn_update_entry_apv = Button(accountPayable_frame, text='Update', bd=2, bg='gray', fg='black',
                              font=('arial', 10), width=14, height=1,
                               command=updated_journalEntry_apv)
    btn_update_entry_apv.place(x=670, y=140)

    btn_selected_delete_apv = Button(accountPayable_frame, text='Delete', bd=2, bg='red', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=delete_journalEntry_apv)
    btn_selected_delete_apv.place(x=670, y=175)


    btn_search_ref_apv = Button(accountPayable_frame, text='Search Ref', bd=2, bg='white', fg='black',
                              font=('arial', 10), width=14, height=1,
                               command=journalEntryManual_list_treeview_apv)
    btn_search_ref_apv.place(x=815, y=35)

    btn_save_entry = Button(accountPayable_frame, text='Save', bd=2, bg='white', fg='black',
                              font=('arial', 10), width=14, height=1,
                               command=testing_dictionary)
    btn_save_entry.place(x=815, y=70)


    # this is for treeview for payroll computation
    journaEntrymanual_view_apv_Form = Frame(accountPayable_frame, width=500, height=10)
    journaEntrymanual_view_apv_Form.place(x=10, y=280)

    style = ttk.Style(accountPayable_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    rowheight=15,
                    fieldbackground="yellow")
   
    
    
    global journalEntryManual_apv_treeview
    scrollbarx = Scrollbar(journaEntrymanual_view_apv_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(journaEntrymanual_view_apv_Form, orient=VERTICAL)
    
    journalEntryManual_apv_treeview = ttk.Treeview(journaEntrymanual_view_apv_Form,
                                             columns=('ID','DATE', "JOURNAL","REF",
                                               "DESCRIPTION",
                                              "ACCOUNT",'ACCOUNTTITLE','DEBIT', 'CREDIT'),
                                             selectmode="extended", height=8, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=journalEntryManual_apv_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=journalEntryManual_apv_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    journalEntryManual_apv_treeview.heading('ID', text="ID", anchor=CENTER)
    journalEntryManual_apv_treeview.heading('DATE', text="Date", anchor=CENTER)
    journalEntryManual_apv_treeview.heading('JOURNAL', text="Journal", anchor=CENTER)
    journalEntryManual_apv_treeview.heading('REF', text="Ref", anchor=CENTER)
    journalEntryManual_apv_treeview.heading('DESCRIPTION', text="Description", anchor=CENTER)
    journalEntryManual_apv_treeview.heading('ACCOUNT', text="Account #", anchor=CENTER)
    journalEntryManual_apv_treeview.heading('ACCOUNTTITLE', text="Acct Title", anchor=CENTER)
    journalEntryManual_apv_treeview.heading('DEBIT', text="Debit", anchor=CENTER)
    journalEntryManual_apv_treeview.heading('CREDIT', text="Credit", anchor=CENTER)


    journalEntryManual_apv_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    journalEntryManual_apv_treeview.column('#1', stretch=NO, minwidth=0, width=50, anchor='e')
    journalEntryManual_apv_treeview.column('#2', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_apv_treeview.column('#3', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_apv_treeview.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_apv_treeview.column('#5', stretch=NO, minwidth=0, width=220, anchor='e')
    journalEntryManual_apv_treeview.column('#6', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_apv_treeview.column('#7', stretch=NO, minwidth=0, width=220, anchor='e')
    journalEntryManual_apv_treeview.column('#8', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_apv_treeview.column('#9', stretch=NO, minwidth=0, width=100, anchor='e')
   
   

    journalEntryManual_apv_treeview.pack()
    


#======================================Supplier Frame==========================================================
def updated_supplier():
    """
    This function is for 
    updating journal entry
    """
    dataSearch = db['supplier_db']
    query = {'_id': ObjectId(supplier_transID_entry.get())}

    result = tkMessageBox.askquestion('JRS','Are you sure you want to Update?',icon="warning")
    if result == 'yes':
      
        try:

            newValue = { "$set": { "supplierID": supplierID_entry.get(),
                                 "supplierName": supplierName_entry.get(), 
                                 "supplier_address": supplier_address_entry.get('1.0', 'end-1c'),
                                 "supplier_tin": supplier_vat_registrationNum_entry.get(),
                                 "supplier_email": supplier_email_entry.get(),
                                 "supplier_vat_class": supplier_tax_class_entry.get(),
                                  "contactNumber": supplier_contactNum_entry.get(), }           
                                    }
            dataSearch.update_many(query, newValue)
            messagebox.showinfo('JRS', 'Data has been updated')
            supplier_list_treeview()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}")
            print(ex)


def delete_supplier():
    """
    this function is for
    deleting journal entry
    """
    dataSearch = db['supplier_db']
    query = {'_id': ObjectId(supplier_transID_entry.get())}
    result = tkMessageBox.askquestion('JRS','Are you sure you want to Delete?',icon="warning")
    if result == 'yes':
        x = dataSearch.delete_one(query)
        messagebox.showinfo('JRS', 'Selected Record has been deleted')
        supplier_list_treeview()

def autoIncrement_supplierID():
    """
    This function is for
    autoincrement Customer ID
    for reference in
    journala Entry
    """
    dataSearch = db['supplier_db']
    agg_result = dataSearch.find().sort('supplierID',-1).limit(1)

    a = ""
    for x in agg_result :
        a = x['supplierID']


        # current_year =  datetime.today().year
    if a =="":
        test_str = 'ID-000'
        res = test_str

        supplierID_entry.delete(0, END)
        supplierID_entry.insert(0, (res))
        
    else:
    
        reference_manual = a 
        res = re.sub(r'[0-9]+$',
                lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}", 
                reference_manual)

        supplierID_entry.delete(0, END)
        supplierID_entry.insert(0, (res))


def select_record_supplierTreeview():
    """
    This function is for
    selection of  treeview
    """

    

    supplierID_entry.delete(0, END)
    supplier_address_entry.delete('1.0', END)
    supplierName_entry.delete(0, END)
    supplier_email_entry.delete(0, END)
    supplier_contactNum_entry.delete(0, END)
    supplier_vat_registrationNum_entry.delete(0, END)
    supplier_tax_class_entry.delete(0, END)
    supplier_transID_entry.delete(0, END)
    

    selected = supplier_tree_view.focus()
    values = supplier_tree_view.item(selected)
    selectedItems = values['values']
    


    dataSearch = db['supplier_db']
    query = {'_id': ObjectId(selectedItems[0])}
    try:
       
        
        for x in dataSearch.find(query):
            
            id_num = x['_id']
            supplierName = x['supplierName']
            supplierID = x['supplierID']
            supplier_address = x['supplier_address']
            supplier_email = x['supplier_email']
            supplier_vat_registrationNum = x['supplier_tin']
            tax_class = x['supplier_vat_class']
            customer_contactNum = x['contactNumber']

            
            
            supplierID_entry.insert(0, supplierID)
            supplierName_entry.insert(0, supplierName)
            supplier_address_entry.insert('1.0', supplier_address)
            supplier_email_entry.insert(0, supplier_email)
            supplier_tax_class_entry.insert(0, tax_class)
            supplier_vat_registrationNum_entry.insert(0, supplier_vat_registrationNum)
            supplier_transID_entry.insert(0, id_num)
            supplier_contactNum_entry.insert(0, customer_contactNum)
           

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")
def supplier_list_treeview():
    
    """
    this function is for
    button to display the list
    of supplier
    """
    
    supplier_tree_view.delete(*supplier_tree_view.get_children())
    return supplierList_Treeview()

def supplierList_Treeview():
    """
    this function is for 
    displaying customer List
    """
    dataSearch = db['supplier_db']
    # query = {'customerID':customerID_entry.get() }
    try:
        
        for x in dataSearch.find():
            transID = x['_id']
            supplierID = x['supplierID']
            supplierName = x['supplierName']
            supplier_address = x['supplier_address']
            supplier_email = x['supplier_email']
            vat_registrationNum = x['supplier_tin']
            supplier_tax_class = x['supplier_vat_class']
           
            
           
            
            supplier_tree_view.insert('', 'end', values=(transID,supplierID,supplierName,supplier_address,
                                supplier_email,vat_registrationNum, supplier_tax_class ))

            
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")

def insert_supplierFrame():
    """
    This function is for
    inserting customer
    """
    collection = db['supplier_db'] # this is to create collection and save as table
    dataInsert = {
    
    'supplierID': supplierID_entry.get(),
    'supplierName': supplierName_entry.get(),
    'supplier_address': supplier_address_entry.get('1.0', 'end-1c'),
    'supplier_email': supplier_email_entry.get(),
    'contactNumber': supplier_contactNum_entry.get(),
    'supplier_tin': supplier_vat_registrationNum_entry.get(),
    'supplier_vat_class': supplier_tax_class_entry.get(),
    
    'user': USERNAME.get(),
    'created':datetime.now()
    
    }

    
    
    try:
        collection.insert_one(dataInsert)

        supplierID_entry.delete(0, END)
        supplierName_entry.delete(0, END)
        supplier_address_entry.delete('1.0', END)
        supplier_email_entry.delete(0, END)
        supplier_contactNum_entry.delete(0, END)
        supplier_vat_registrationNum_entry.delete(0, END)
        supplier_tax_class_entry.delete(0, END)
        supplier_transID_entry.delete(0, END)
        messagebox.showinfo('JRS', 'Data has been exported and save')
        
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")    
                   
    
    supplier_list_treeview()



def insert_supplier_frame():
    """
    This function si for
    customer frame
    """

    clearFrame()

    global insert_supplier_frame
    insert_supplier_frame = Frame(MidViewForm9, width=1120, height=575, bd=2, bg='gray', relief=SOLID)
    insert_supplier_frame.place(x=160, y=8)

    supplierID_label = Label(insert_supplier_frame, text='Supplier ID:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    supplierID_label.place(x=10, y=10)

    global supplierID_entry
    supplierID_entry = Entry(insert_supplier_frame, width=20, font=('Arial', 10), justify='right')
    supplierID_entry.place(x=170, y=10)


    supplierName_label = Label(insert_supplier_frame, text='Supplier Name:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    supplierName_label.place(x=10, y=35)

    global supplierName_entry
    supplierName_entry = Entry(insert_supplier_frame, width=20, font=('Arial', 10), justify='right')
    supplierName_entry.place(x=170, y=35)


    supplier_adress_lbl = Label(insert_supplier_frame, text='Supplier Address:', width=14, height=1, bg='yellow', 
                          fg='black',
                          font=('Arial', 10), anchor='e')
    supplier_adress_lbl.place(x=10, y=65)

    global supplier_address_entry
    supplier_address_entry = scrolledtext.ScrolledText(insert_supplier_frame,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
    supplier_address_entry.place(x=170, y=65)


    supplier_email_label = Label(insert_supplier_frame, text='Supplier Email:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    supplier_email_label.place(x=10, y=140)

    global supplier_email_entry
    supplier_email_entry = Entry(insert_supplier_frame, width=20, font=('Arial', 10), justify='right')
    supplier_email_entry.place(x=170, y=140)

    supplier_vat_registrationNum_label = Label(insert_supplier_frame, text='Supplier TIN:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    supplier_vat_registrationNum_label.place(x=10, y=170)

    global supplier_vat_registrationNum_entry
    supplier_vat_registrationNum_entry = Entry(insert_supplier_frame, width=20, font=('Arial', 10), justify='right')
    supplier_vat_registrationNum_entry.place(x=170, y=170)

    supplier_contactNum_label = Label(insert_supplier_frame, text='Supplier Number:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    supplier_contactNum_label.place(x=10, y=200)

    global supplier_contactNum_entry
    supplier_contactNum_entry = Entry(insert_supplier_frame, width=20, font=('Arial', 10), justify='right')
    supplier_contactNum_entry.place(x=170, y=200)


    tax_class_label = Label(insert_supplier_frame, text='Tax Class:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    tax_class_label.place(x=10, y=230)

    global supplier_tax_class_entry
    
    supplier_tax_class_entry = ttk.Combobox(insert_supplier_frame, width=14)
    supplier_tax_class_entry['values'] = ("Vat", "Non-Vat")
    supplier_tax_class_entry.place(x=170, y=230)

    transID_label = Label(insert_supplier_frame, text='Trans ID:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    transID_label.place(x=10, y=257)

    global supplier_transID_entry
    
    supplier_transID_entry = Entry(insert_supplier_frame, width=20, font=('Arial', 10), justify='right')
    supplier_transID_entry.place(x=170, y=257)


    btn_addsuppID_entry = Button(insert_supplier_frame, text='Supplier ID', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=autoIncrement_supplierID)
    btn_addsuppID_entry.place(x=670, y=35)

    btn_insert_supplier_entry = Button(insert_supplier_frame, text='Insert Supplier', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=insert_supplierFrame)
    btn_insert_supplier_entry.place(x=670, y=70)

    btn_selected = Button(insert_supplier_frame, text='Selected', bd=2, bg='khaki', fg='black',
                              font=('arial', 10), width=14, height=1, command=select_record_supplierTreeview
                               )
    btn_selected.place(x=670, y=105)

    btn_update_entry = Button(insert_supplier_frame, text='Update', bd=2, bg='gray', fg='yellow',
                              font=('arial', 10), width=14, height=1,
                               command=updated_supplier)
    btn_update_entry.place(x=670, y=140)

    btn_selected_delete = Button(insert_supplier_frame, text='Delete', bd=2, bg='red', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=delete_supplier)
    btn_selected_delete.place(x=670, y=175)


    btn_search_ref = Button(insert_supplier_frame, text='All Supplier', bd=2, bg='white', fg='black',
                              font=('arial', 10), width=14, height=1,
                               command=supplier_list_treeview)
    btn_search_ref.place(x=815, y=35)

    
    # this is for treeview for supplier frame
    supplier_tree_view_Form = Frame(insert_supplier_frame, width=500, height=10)
    supplier_tree_view_Form.place(x=10, y=280)

    style = ttk.Style(insert_supplier_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    rowheight=15,
                    fieldbackground="yellow")
   
    

    
    
    global supplier_tree_view
    scrollbarx = Scrollbar(supplier_tree_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(supplier_tree_view_Form, orient=VERTICAL)
    
    supplier_tree_view = ttk.Treeview(supplier_tree_view_Form,
                                             columns=('TRANS-ID','ID','CUSTOMER', "CUST-ADD","CUS-EMAIL",
                                               "TIN",
                                              "TAX-CLASS"),
                                             selectmode="extended", height=12, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=supplier_tree_view.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=supplier_tree_view.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    supplier_tree_view.heading('TRANS-ID', text="Trans-ID", anchor=CENTER)
    supplier_tree_view.heading('ID', text="ID", anchor=CENTER)
    supplier_tree_view.heading('CUSTOMER', text="NAME", anchor=CENTER)
    supplier_tree_view.heading('CUST-ADD', text="Supp-Address", anchor=CENTER)
    supplier_tree_view.heading('CUS-EMAIL', text="Email", anchor=CENTER)
    supplier_tree_view.heading('TIN', text="Tin", anchor=CENTER)
    supplier_tree_view.heading('TAX-CLASS', text="Tax Class", anchor=CENTER)
    


    supplier_tree_view.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    supplier_tree_view.column('#1', stretch=NO, minwidth=0, width=150, anchor='e')
    supplier_tree_view.column('#2', stretch=NO, minwidth=0, width=150, anchor='e')
    supplier_tree_view.column('#3', stretch=NO, minwidth=0, width=150, anchor='e')
    supplier_tree_view.column('#4', stretch=NO, minwidth=0, width=150, anchor='e')
    supplier_tree_view.column('#5', stretch=NO, minwidth=0, width=150, anchor='e')
    supplier_tree_view.column('#6', stretch=NO, minwidth=0, width=150, anchor='e')
   
   

    supplier_tree_view.pack()



#======================================Customer Frame==========================================================
def updated_customer():
    """
    This function is for 
    updating journal entry
    """
    dataSearch = db['customer_db']
    query = {'_id': ObjectId(transID_entry.get())}

    result = tkMessageBox.askquestion('JRS','Are you sure you want to Update?',icon="warning")
    if result == 'yes':
      
        try:
            newValue = { "$set": { "customerID": customerID_entry.get(),
                                 "customerName": customerName_entry.get(), 
                                 "customer_address": customer_address_entry.get('1.0', 'end-1c'),
                                 "customer_tin": vat_registrationNum_entry.get(),
                                 "vat_class": tax_class_entry.get(),
                                 "customer_email": customer_email_entry.get(),
                                  "contactNumber": customer_contactNum_entry.get(), }           
                                    }
            dataSearch.update_many(query, newValue)
            messagebox.showinfo('JRS', 'Data has been updated')
            customer_list_treeview()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}")
            print(ex)


def delete_customer():
    """
    this function is for
    deleting journal entry
    """
    dataSearch = db['customer_db']
    query = {'_id': ObjectId(transID_entry.get())}
    result = tkMessageBox.askquestion('JRS','Are you sure you want to Delete?',icon="warning")
    if result == 'yes':
        x = dataSearch.delete_one(query)
        messagebox.showinfo('JRS', 'Selected Record has been deleted')
        customer_list_treeview()

def autoIncrement_CustomerID():
    """
    This function is for
    autoincrement Customer ID
    for reference in
    journala Entry
    """
    dataSearch = db['customer_db']
    agg_result = dataSearch.find().sort('customerID',-1).limit(1)

    a = ""
    for x in agg_result :
        a = x['customerID']


        # current_year =  datetime.today().year
    if a =="":
        test_str = 'ID-000'
        res = test_str

        customerID_entry.delete(0, END)
        customerID_entry.insert(0, (res))
        
    else:
    
        reference_manual = a 
        res = re.sub(r'[0-9]+$',
                lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}", 
                reference_manual)

        customerID_entry.delete(0, END)
        customerID_entry.insert(0, (res))


def select_record_customerTreeview():
    """
    This function is for
    selection of  treeview
    """
    customerName_entry.delete(0, END)
    customer_address_entry.delete('1.0', END)
    customer_email_entry.delete(0, END)
    vat_registrationNum_entry.delete(0, END)
    tax_class_entry.delete(0, END)
    transID_entry.delete(0, END)
    customerID_entry.delete(0, END)
    customer_contactNum_entry.delete(0, END)
    

    selected = customer_tree_view.focus()
    values = customer_tree_view.item(selected)
    selectedItems = values['values']
    


    dataSearch = db['customer_db']
    query = {'_id': ObjectId(selectedItems[0])}
    try:
       
        
        for x in dataSearch.find(query):
            
            id_num = x['_id']
            customerName = x['customerName']
            customerID = x['customerID']
            customer_address = x['customer_address']
            customer_email = x['customer_email']
            vat_registrationNum = x['customer_tin']
            tax_class = x['vat_class']
            customer_contactNum = x['contactNumber']
            
            
            customerID_entry.insert(0, customerID)
            customerName_entry.insert(0, customerName)
            customer_address_entry.insert('1.0', customer_address)
            customer_email_entry.insert(0, customer_email)
            vat_registrationNum_entry.insert(0, vat_registrationNum)
            tax_class_entry.insert(0, tax_class)
            transID_entry.insert(0, id_num)
            customer_contactNum_entry.insert(0, customer_contactNum)
           

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")
def customer_list_treeview():
    
    """
    this function is for
    button to display the list
    of income Statement as per query
    """
    
    customer_tree_view.delete(*customer_tree_view.get_children())
    return customerList_Treeview()

def customerList_Treeview():
    """
    this function is for 
    displaying customer List
    """
    dataSearch = db['customer_db']
    # query = {'customerID':customerID_entry.get() }
    try:
        
        for x in dataSearch.find():
            transID = x['_id']
            customerID = x['customerID']
            customerName = x['customerName']
            customer_address = x['customer_address']
            customer_email = x['customer_email']
            vat_registrationNum = x['customer_tin']
            tax_class = x['vat_class']
           
            
           
            
            customer_tree_view.insert('', 'end', values=(transID,customerID,customerName,customer_address,
                                customer_email,vat_registrationNum, tax_class ))

            
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")

def insert_customerFrame():
    """
    This function is for
    inserting customer
    """
    collection = db['customer_db'] # this is to create collection and save as table
    dataInsert = {
    
    'customerID': customerID_entry.get(),
    'customerName': customerName_entry.get(),
    'customer_address': customer_address_entry.get('1.0', 'end-1c'),
    'customer_email': customer_email_entry.get(),
    'contactNumber': customer_contactNum_entry.get(),
    'customer_tin': vat_registrationNum_entry.get(),
    'vat_class': tax_class_entry.get(),
    
    'user': USERNAME.get(),
    'created':datetime.now()
    
    }

    
    
    try:
        collection.insert_one(dataInsert)

        customerID_entry.delete(0, END)
        customerName_entry.delete(0, END)
        customer_address_entry.delete('1.0', END)
        customer_email_entry.delete(0, END)
        vat_registrationNum_entry.delete(0, END)
        tax_class_entry.delete(0, END)
        customer_contactNum_entry.delete(0, END)
        transID_entry.delete(0, END)

        messagebox.showinfo('JRS', 'Data has been exported and save')
        
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")    
                   
    
    customer_list_treeview()



def insert_customer_frame():
    """
    This function si for
    customer frame
    """

    clearFrame()

    global insert_customer_frame
    insert_customer_frame = Frame(MidViewForm9, width=1120, height=575, bd=2, bg='gray', relief=SOLID)
    insert_customer_frame.place(x=160, y=8)

    customerID_label = Label(insert_customer_frame, text='Customer ID:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    customerID_label.place(x=10, y=10)

    global customerID_entry
    customerID_entry = Entry(insert_customer_frame, width=20, font=('Arial', 10), justify='right')
    customerID_entry.place(x=170, y=10)


    customerName_label = Label(insert_customer_frame, text='Customer Name:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    customerName_label.place(x=10, y=35)

    global customerName_entry
    customerName_entry = Entry(insert_customer_frame, width=20, font=('Arial', 10), justify='right')
    customerName_entry.place(x=170, y=35)


    customer_adress_lbl = Label(insert_customer_frame, text='Customer Address:', width=14, height=1, bg='yellow', 
                          fg='black',
                          font=('Arial', 10), anchor='e')
    customer_adress_lbl.place(x=10, y=65)

    global customer_address_entry
    customer_address_entry = scrolledtext.ScrolledText(insert_customer_frame,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
    customer_address_entry.place(x=170, y=65)


    customer_email_label = Label(insert_customer_frame, text='Customer Email:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    customer_email_label.place(x=10, y=140)

    global customer_email_entry
    customer_email_entry = Entry(insert_customer_frame, width=20, font=('Arial', 10), justify='right')
    customer_email_entry.place(x=170, y=140)

    vat_registrationNum_label = Label(insert_customer_frame, text='Customer TIN:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    vat_registrationNum_label.place(x=10, y=170)

    global vat_registrationNum_entry
    vat_registrationNum_entry = Entry(insert_customer_frame, width=20, font=('Arial', 10), justify='right')
    vat_registrationNum_entry.place(x=170, y=170)

    customer_contactNum_label = Label(insert_customer_frame, text='Customer Number:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    customer_contactNum_label.place(x=10, y=200)

    global customer_contactNum_entry
    customer_contactNum_entry = Entry(insert_customer_frame, width=20, font=('Arial', 10), justify='right')
    customer_contactNum_entry.place(x=170, y=200)


    tax_class_label = Label(insert_customer_frame, text='Tax Class:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    tax_class_label.place(x=10, y=230)

    global tax_class_entry
    
    tax_class_entry = ttk.Combobox(insert_customer_frame, width=14)
    tax_class_entry['values'] = ("Vat", "Non-Vat")
    tax_class_entry.place(x=170, y=230)

    transID_label = Label(insert_customer_frame, text='Trans ID:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    transID_label.place(x=10, y=257)

    global transID_entry
    
    transID_entry = Entry(insert_customer_frame, width=20, font=('Arial', 10), justify='right')
    transID_entry.place(x=170, y=257)


    btn_addcustID_entry = Button(insert_customer_frame, text='Customer ID', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=autoIncrement_CustomerID)
    btn_addcustID_entry.place(x=670, y=35)

    btn_insert_customer_entry = Button(insert_customer_frame, text='Insert Customer', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=insert_customerFrame)
    btn_insert_customer_entry.place(x=670, y=70)

    btn_selected = Button(insert_customer_frame, text='Selected', bd=2, bg='khaki', fg='black',
                              font=('arial', 10), width=14, height=1, command=select_record_customerTreeview
                               )
    btn_selected.place(x=670, y=105)

    btn_update_entry = Button(insert_customer_frame, text='Update', bd=2, bg='gray', fg='yellow',
                              font=('arial', 10), width=14, height=1,
                               command=updated_customer)
    btn_update_entry.place(x=670, y=140)

    btn_selected_delete = Button(insert_customer_frame, text='Delete', bd=2, bg='red', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=delete_customer)
    btn_selected_delete.place(x=670, y=175)


    btn_search_ref = Button(insert_customer_frame, text='All Customer', bd=2, bg='white', fg='black',
                              font=('arial', 10), width=14, height=1,
                               command=customer_list_treeview)
    btn_search_ref.place(x=815, y=35)

    
    # this is for treeview for customer frame
    customer_tree_view_Form = Frame(insert_customer_frame, width=500, height=10)
    customer_tree_view_Form.place(x=10, y=280)

    style = ttk.Style(insert_customer_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    rowheight=15,
                    fieldbackground="yellow")
   
    

    
    
    global customer_tree_view
    scrollbarx = Scrollbar(customer_tree_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(customer_tree_view_Form, orient=VERTICAL)
    
    customer_tree_view = ttk.Treeview(customer_tree_view_Form,
                                             columns=('TRANS-ID','ID','CUSTOMER', "CUST-ADD","CUS-EMAIL",
                                               "TIN",
                                              "TAX-CLASS"),
                                             selectmode="extended", height=12, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=customer_tree_view.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=customer_tree_view.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    customer_tree_view.heading('TRANS-ID', text="Trans-ID", anchor=CENTER)
    customer_tree_view.heading('ID', text="ID", anchor=CENTER)
    customer_tree_view.heading('CUSTOMER', text="NAME", anchor=CENTER)
    customer_tree_view.heading('CUST-ADD', text="Cus-Address", anchor=CENTER)
    customer_tree_view.heading('CUS-EMAIL', text="Email", anchor=CENTER)
    customer_tree_view.heading('TIN', text="Tin", anchor=CENTER)
    customer_tree_view.heading('TAX-CLASS', text="Tax Class", anchor=CENTER)
    


    customer_tree_view.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    customer_tree_view.column('#1', stretch=NO, minwidth=0, width=150, anchor='e')
    customer_tree_view.column('#2', stretch=NO, minwidth=0, width=150, anchor='e')
    customer_tree_view.column('#3', stretch=NO, minwidth=0, width=150, anchor='e')
    customer_tree_view.column('#4', stretch=NO, minwidth=0, width=150, anchor='e')
    customer_tree_view.column('#5', stretch=NO, minwidth=0, width=150, anchor='e')
    customer_tree_view.column('#6', stretch=NO, minwidth=0, width=150, anchor='e')
   
   

    customer_tree_view.pack()


    
    
#=====================================Accounting Frame==============================================================

def delete_journalEntry():
    """
    this function is for
    deleting journal entry
    """
    dataSearch = db['journal_entry']
    query = {'_id': ObjectId(Selected_ID_entry.get())}
    result = tkMessageBox.askquestion('JRS','Are you sure you want to Update?',icon="warning")
    if result == 'yes':
        x = dataSearch.delete_one(query)
        messagebox.showinfo('JRS', 'Selected Record has been deleted')
        journalEntryManual_list_treeview()


def updated_journalEntry():
    """
    This function is for 
    updating journal entry
    """
    dataSearch = db['journal_entry']
    query = {'_id': ObjectId(Selected_ID_entry.get())}

    result = tkMessageBox.askquestion('JRS','Are you sure you want to Update?',icon="warning")
    if result == 'yes':
        dateEntry =  journalEntryInsert_datefrom.get()
        date_time_obj = datetime.strptime(dateEntry, '%m/%d/%Y')
        try:
            newValue = { "$set": { "date_entry": date_time_obj,
                                 "journal": journal_manual.get(), 
                                 "ref": reference_manual_entry.get(),
                                 "descriptions": journal_memo_entry.get('1.0', 'end-1c'),
                                 "acoount_number": account_number_entry.get(),
                                     "account_disc": chart_of_account_manual.get(),
                                     "bsClass": bs_class_entry.get(),
                                     "debit_amount": float(debit_manual_entry.get()), 
                                     "credit_amount": float(credit_manual_entry.get()),}           
                                    }
            dataSearch.update_many(query, newValue)
            messagebox.showinfo('JRS', 'Data has been updated')
            journalEntryManual_list_treeview()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}")


def select_record_treeview():
    """
    this function is for
    selecting record from
    treeview
    """
    journalEntryInsert_datefrom.delete(0, END)
    journal_manual.delete(0, END)
    reference_manual_entry.delete(0, END)
    journal_memo_entry.delete('1.0', END)
    account_number_entry.delete(0, END)
    chart_of_account_manual.delete(0, END)
    debit_manual_entry.delete(0, END)
    credit_manual_entry.delete(0, END)
    Selected_ID_entry.delete(0, END)
    bs_class_entry.delete(0, END)

    selected = journalEntryManual_treeview.focus()
    values = journalEntryManual_treeview.item(selected)
    selectedItems = values['values']
    


    dataSearch = db['journal_entry']
    query = {'_id': ObjectId(selectedItems[0])}
    try:
       
        
        for x in dataSearch.find(query):
            
            id_num = x['_id']
            date_entry = x['date_entry']
            journal = x['journal']
            ref = x['ref']
            descriptions = x['descriptions']
            account_number = x['acoount_number']
            account_disc = x['account_disc']
            debit_amount = x['debit_amount']
            debit_amount2 = '{:,.2f}'.format(debit_amount)
            credit_amount = x['credit_amount']
            credit_amount2 = '{:,.2f}'.format(credit_amount)
            bs_class = x['bsClass']
            
            journalEntryInsert_datefrom.insert(0, date_entry)
            journal_manual.insert(0, journal)
            reference_manual_entry.insert(0, ref)
            journal_memo_entry.insert('1.0', descriptions)
            account_number_entry.insert(0, account_number)
            chart_of_account_manual.insert(0, account_disc)
            debit_manual_entry.insert(0, debit_amount)
            credit_manual_entry.insert(0, credit_amount)
            Selected_ID_entry.insert(0, id_num)
            bs_class_entry.insert(0, bs_class)

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")

    


def journalEntryManual_list_treeview():
    
    """
    this function is for
    button to display the list
    of income Statement as per query
    """
    
    journalEntryManual_treeview.delete(*journalEntryManual_treeview.get_children())
    return journalEntry_manual_list()
def journalEntry_manual_list():
    """
    This function is for manual
    entry list
    """
    dataSearch = db['journal_entry']
    query = {'ref':reference_manual_entry.get() }

    # query ==""
    # if query == "":
    #     messagebox.showinfo("Error","No Record found" )
    # else:
    try:
        cnt = 0
        debit_amount_total = 0
        credit_amount_total= 0
        a = ""
        for x in dataSearch.find(query):
            a = x['ref']
            
            if a == "":
                    messagebox.showinfo("Error","No Record found" )
            else:
                cnt+=1
                id_num = x['_id']
                date_entry = x['date_entry']
                journal = x['journal']
                ref = x['ref']
                descriptions = x['descriptions']
                account_number = x['acoount_number']
                account_disc = x['account_disc']
                debit_amount = x['debit_amount']
                debit_amount2 = '{:,.2f}'.format(debit_amount)
                credit_amount = x['credit_amount']
                credit_amount2 = '{:,.2f}'.format(credit_amount)
                
                debit_amount_total+=debit_amount
                debit_amount_total2 = '{:,.2f}'.format(debit_amount_total)

                credit_amount_total+=credit_amount
                credit_amount_total2 = '{:,.2f}'.format(credit_amount_total)
                
                journalEntryManual_treeview.insert('', 'end', values=(id_num,date_entry,journal,
                                    ref,descriptions, account_number,account_disc,debit_amount2,
                                    credit_amount2 ))

                totalDebit_manual_entry.delete(0, END)
                totalDebit_manual_entry.insert(0, (debit_amount_total2))


                totalCredit_manual_entry.delete(0, END)
                totalCredit_manual_entry.insert(0, (credit_amount_total2))

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")
def insert_journalEntry_manual():
    """
    this function is for inserting
    record to journal_entry
    """

    debit_entry = float(debit_manual_entry.get())
    
    
    credit_entry = float(credit_manual_entry.get())
    

    dateEntry =  journalEntryInsert_datefrom.get()
    date_time_obj = datetime.strptime(dateEntry, '%m/%d/%Y')
    
    
    collection = db['journal_entry'] # this is to create collection and save as table
    dataInsert = {
    # 'date_entry': journalEntryInsert_datefrom.get(),
    'date_entry': date_time_obj,
    'journal': journal_manual.get(),
    'ref': reference_manual_entry.get(),
    'descriptions': journal_memo_entry.get('1.0', 'end-1c'),
    'acoount_number': account_number_entry.get(),
    'account_disc': chart_of_account_manual.get(),
    'bsClass': bs_class_entry.get(),
    'debit_amount': debit_entry,
    'credit_amount': credit_entry,
    'due_date_apv': '',
    'terms_days': '',
    'supplier/Client': '',
    'user': USERNAME.get(),
    'created':datetime.now()
    
    
    }

    
    
    try:
        collection.insert_one(dataInsert)

        account_number_entry.delete(0, END)
        chart_of_account_manual.delete(0, END)
        debit_manual_entry.delete(0, END)
        credit_manual_entry.delete(0, END)
        
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")    
                   
    messagebox.showinfo('JRS', 'Data has been exported and save')
    journalEntryManual_list_treeview()


def autoIncrement_journal_manual_ref():
    """
    This function is for
    autoincrement Number
    for reference in
    journala Entry
    """
    dataSearch = db['journal_entry']
    agg_result = dataSearch.find().sort('ref',-1).limit(1)

    a = ""
    for x in agg_result :
        a = x['ref']

        # current_year =  datetime.today().year
    if a =="":
        test_str = 'GJ000'
        res = test_str

        reference_manual_entry.delete(0, END)
        reference_manual_entry.insert(0, (res))
        
    else:
        

        reference_manual = a 
        res = re.sub(r'[0-9]+$',
                lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}", 
                reference_manual)

        reference_manual_entry.delete(0, END)
        reference_manual_entry.insert(0, (res))
def auto_account_num(e):
    """
    this function
    is for auto complete
    for account number
    """

    dataSearch = db['chart_of_account'] 
    agg_result = dataSearch.find({'accountTitle':chart_of_account_manual.get()})

    for x in agg_result:
        a = x['accountNum']
        b = x['bsClass']
        account_number_entry.delete(0, END)
        account_number_entry.insert(0, (a))

        bs_class_entry.delete(0, END)
        bs_class_entry.insert(0, (b))




def chart_of_account_list():
    """
    this function is for 
    the displaying chart of 
    account to dropdown menu
    or combo box
    """  
    dataSearch = db['chart_of_account'] 
    # agg_result = dataSearch.find()
    agg_result = dataSearch.find().sort('accountNum', pymongo.ASCENDING)

    data = []
    for x in agg_result:
        data.append(x['accountTitle'])
    return data
        

def journal_entry_insert_frame():
    """
    This function is for
    inserting journal entry 
    """
    cleartrialbalanceFrame()
   
    entry_date_label = Label(accounting_frame, text='Date from:', width=14, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    entry_date_label.place(x=10, y=35)

    global journalEntryInsert_datefrom
    journalEntryInsert_datefrom = DateEntry(accounting_frame, width=15, background='darkblue',
                                  date_pattern='MM/dd/yyyy',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    journalEntryInsert_datefrom.place(x=170, y=35)
    journalEntryInsert_datefrom.configure(justify='center')
    
   

    journal_label = Label(accounting_frame, text='Journal:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    journal_label.place(x=10, y=70)

    global journal_manual
    
    journal_manual = ttk.Combobox(accounting_frame, width=14)
    journal_manual['values'] = ("Payments", "Receipts", "Sales", "Purchases",'General')
    journal_manual.place(x=170, y=70)

    reference_label = Label(accounting_frame, text='reference:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    reference_label.place(x=10, y=105)

    global reference_manual_entry
    reference_manual_entry = Entry(accounting_frame, width=12, font=('Arial', 10), justify='right')
    reference_manual_entry.place(x=170, y=105)

    
    journal_memo_lbl = Label(accounting_frame, text='Journal Memo:', width=14, height=1, bg='yellow', 
                          fg='black',
                          font=('Arial', 10), anchor='e')
    journal_memo_lbl.place(x=10, y=140)

    global journal_memo_entry
    journal_memo_entry = scrolledtext.ScrolledText(accounting_frame,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
    journal_memo_entry.place(x=170, y=140)


    account_number_lbl = Label(accounting_frame, text='Acct Number:', width=10, height=1, bg='yellow', 
                          fg='black',
                          font=('Arial', 10), anchor='e')
    account_number_lbl.place(x=10, y=200)

    global account_number_entry
    account_number_entry = Entry(accounting_frame, width=12, font=('Arial', 10), justify='right')
    account_number_entry.place(x=10, y=235)

    account_title_lbl = Label(accounting_frame, text='Acct Title:', width=32, height=1, bg='yellow', 
                          fg='black',
                          font=('Arial', 10), anchor='c')
    account_title_lbl.place(x=110, y=200)

    global chart_of_account_manual
    chart_of_account_manual = ttk.Combobox(accounting_frame, width=39)
    chart_of_account_manual['values'] = chart_of_account_list()
    chart_of_account_manual.place(x=110, y=235)
    chart_of_account_manual.bind("<<ComboboxSelected>>", auto_account_num)



    debitManual_label = Label(accounting_frame, text='Debit:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='c')
    debitManual_label.place(x=390, y=200)

    global debit_manual_entry
    debit_manual_entry = Entry(accounting_frame, width=16, font=('Arial', 10), justify='right')
    debit_manual_entry.place(x=390, y=235)

    creditManual_label = Label(accounting_frame, text='Credit:', 
                                            width=14, height=1, bg='yellowgreen', fg='black',
                                             font=('Arial', 10), anchor='c')
    creditManual_label.place(x=520, y=200)

    global credit_manual_entry
    credit_manual_entry = Entry(accounting_frame, width=16, font=('Arial', 10), justify='right')
    credit_manual_entry.place(x=520, y=235)

    bs_class_label = Label(accounting_frame, text='BS Class:', 
                                            width=14, height=1, bg='yellowgreen', fg='black',
                                             font=('Arial', 10), anchor='c')
    bs_class_label.place(x=650, y=200)

    global bs_class_entry
    bs_class_entry = Entry(accounting_frame, width=16, font=('Arial', 10), justify='right')
    bs_class_entry.place(x=650, y=235)


    selected_label = Label(accounting_frame, text='Transaction ID:', 
                                            width=14, height=1, bg='yellowgreen', fg='black',
                                             font=('Arial', 10), anchor='c')
    selected_label.place(x=800, y=235)

    global Selected_ID_entry
    Selected_ID_entry = Entry(accounting_frame, width=16, font=('Arial', 10), justify='right')
    Selected_ID_entry.place(x=920, y=235)


    grand_total_label = Label(accounting_frame, text='TOTAL', 
                                            width=14, height=1, bg='yellowgreen', fg='black',
                                             font=('Arial', 10), anchor='c')
    grand_total_label.place(x=650, y=490)

   
    
    global totalDebit_manual_entry
    totalDebit_manual_entry = Entry(accounting_frame, width=16, font=('Arial', 10), justify='right')
    totalDebit_manual_entry.place(x=880, y=490)


   
    
    global totalCredit_manual_entry
    totalCredit_manual_entry = Entry(accounting_frame, width=16, font=('Arial', 10), justify='right')
    totalCredit_manual_entry.place(x=1000, y=490)
    
    
    
    btn_batch_entry = Button(accounting_frame, text='Add Batch Entry', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=autoIncrement_journal_manual_ref)
    btn_batch_entry.place(x=670, y=35)

    btn_JournalManual_entry = Button(accounting_frame, text='Insert Entry', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=insert_journalEntry_manual)
    btn_JournalManual_entry.place(x=670, y=70)

    btn_selected = Button(accounting_frame, text='Selected', bd=2, bg='khaki', fg='black',
                              font=('arial', 10), width=14, height=1,
                               command=select_record_treeview)
    btn_selected.place(x=670, y=105)

    btn_update_entry = Button(accounting_frame, text='Update', bd=2, bg='gray', fg='black',
                              font=('arial', 10), width=14, height=1,
                               command=updated_journalEntry)
    btn_update_entry.place(x=670, y=140)

    btn_selected_delete = Button(accounting_frame, text='Delete', bd=2, bg='red', fg='white',
                              font=('arial', 10), width=14, height=1,
                               command=delete_journalEntry)
    btn_selected_delete.place(x=670, y=175)


    btn_search_ref = Button(accounting_frame, text='Search Ref', bd=2, bg='white', fg='black',
                              font=('arial', 10), width=14, height=1,
                               command=journalEntryManual_list_treeview)
    btn_search_ref.place(x=815, y=35)


    # this is for treeview for payroll computation
    journaEntrymanual_view_Form = Frame(accounting_frame, width=500, height=10)
    journaEntrymanual_view_Form.place(x=10, y=280)

    style = ttk.Style(accounting_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    rowheight=15,
                    fieldbackground="yellow")
   
    
    
    global journalEntryManual_treeview
    scrollbarx = Scrollbar(journaEntrymanual_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(journaEntrymanual_view_Form, orient=VERTICAL)
    
    journalEntryManual_treeview = ttk.Treeview(journaEntrymanual_view_Form,
                                             columns=('ID','DATE', "JOURNAL","REF",
                                               "DESCRIPTION",
                                              "ACCOUNT",'ACCOUNTTITLE','DEBIT', 'CREDIT'),
                                             selectmode="extended", height=8, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=journalEntryManual_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=journalEntryManual_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    journalEntryManual_treeview.heading('ID', text="ID", anchor=CENTER)
    journalEntryManual_treeview.heading('DATE', text="Date", anchor=CENTER)
    journalEntryManual_treeview.heading('JOURNAL', text="Journal", anchor=CENTER)
    journalEntryManual_treeview.heading('REF', text="Ref", anchor=CENTER)
    journalEntryManual_treeview.heading('DESCRIPTION', text="Description", anchor=CENTER)
    journalEntryManual_treeview.heading('ACCOUNT', text="Account #", anchor=CENTER)
    journalEntryManual_treeview.heading('ACCOUNTTITLE', text="Acct Title", anchor=CENTER)
    journalEntryManual_treeview.heading('DEBIT', text="Debit", anchor=CENTER)
    journalEntryManual_treeview.heading('CREDIT', text="Credit", anchor=CENTER)


    journalEntryManual_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    journalEntryManual_treeview.column('#1', stretch=NO, minwidth=0, width=50, anchor='e')
    journalEntryManual_treeview.column('#2', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_treeview.column('#3', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_treeview.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_treeview.column('#5', stretch=NO, minwidth=0, width=220, anchor='e')
    journalEntryManual_treeview.column('#6', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_treeview.column('#7', stretch=NO, minwidth=0, width=220, anchor='e')
    journalEntryManual_treeview.column('#8', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntryManual_treeview.column('#9', stretch=NO, minwidth=0, width=100, anchor='e')
   
   

    journalEntryManual_treeview.pack()
    
    





def incomeStatement_list_treeview():
    
    """
    this function is for
    button to display the list
    of income Statement as per query
    """
    
    incomeStatement_treeview.delete(*incomeStatement_treeview.get_children())
    return incomeStatement_calculation()

def incomeStatement_calculation():
    """
    This function is for calculation
    of Income Statement
    """
    dataSearch = db['journal_entry']
    # datefrom = incomeStament_datefrom.get()
    # dateto = incomeStament_dateto.get()


    datefrom = incomeStament_datefrom.get()
    date_time_obj_from = datetime.strptime(datefrom, '%Y-%m-%d')

    dateto = incomeStament_dateto.get()
    date_time_obj_to = datetime.strptime(dateto, '%Y-%m-%d')

    agg_result= dataSearch.aggregate(
        [
        {"$match":{'date_entry': {'$gte':date_time_obj_from, '$lte':date_time_obj_to},
            '$or': [
            {'acoount_number': {"$regex": "^5"}},
            {'acoount_number': {"$regex": "^4"}}
        ] }},
        # {"$match": { "cut_off_period": date } },
        # {'$sort' : { '$meta': "textScore" }, '$account_disc': -1 },
        {"$group" : 
            {"_id" :  '$acoount_number',
            "accountName": {'$first':'$account_disc'},
            "totalDebit" : {"$sum" : '$debit_amount'},
            "totalCredit" : {"$sum" : '$credit_amount'},
            
            }},
        {'$sort':{'_id': 1}}
            
        ])

    total_debit_amount = 0
    total_credit_amount = 0
    for x in agg_result: 
        
        # # print(x)
        # account_number = x['_id']
        # print(account_number)
        # # TotalDebit = x['totalDebit']
        
                
        account_number = x['accountName']
        debit_amount = x['totalDebit']
        debit_amount2 = '{:,.2f}'.format(debit_amount)
        credit_amount = x['totalCredit']
        credit_amount2 = '{:,.2f}'.format(credit_amount)

        total_debit_amount+=debit_amount
        total_debit_amount2 ='{:,.2f}'.format(total_debit_amount)


        total_credit_amount+=credit_amount
        total_credit_amount2 ='{:,.2f}'.format(total_credit_amount)

        
        netIncome = float(total_credit_amount - total_debit_amount)
        netIncome2 ='{:,.2f}'.format(netIncome)
        
        incomeStatement_treeview.insert('', 'end', values=(account_number,
                                                        debit_amount2,
                                                        credit_amount2 ))

        totalIncome_entry.delete(0, END)
        totalIncome_entry.insert(0, (total_credit_amount2))

        totalExpenses_entry.delete(0, END)
        totalExpenses_entry.insert(0, (total_debit_amount2))

        netIncome_entry.delete(0, END)
        netIncome_entry.insert(0, (netIncome2))



def incomeStatement_frame():
    """
    This function is for
    income statement frame
    """
    cleartrialbalanceFrame()
    global entry_datefrom
    entry_date_label = Label(accounting_frame, text='Date from:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    entry_date_label.place(x=10, y=35)

    global incomeStament_datefrom
    incomeStament_datefrom = DateEntry(accounting_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    incomeStament_datefrom.place(x=120, y=35)
    incomeStament_datefrom.configure(justify='center')
    
    entry_date_label = Label(accounting_frame, text='Date to:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    entry_date_label.place(x=250, y=35)

    global incomeStament_dateto
    incomeStament_dateto = DateEntry(accounting_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    incomeStament_dateto.place(x=350, y=35)
    incomeStament_dateto.configure(justify='center')

    totalIncome_label = Label(accounting_frame, text='Total Income:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    totalIncome_label.place(x=850, y=110)

    global totalIncome_entry
    totalIncome_entry = Entry(accounting_frame, width=12, font=('Arial', 12), justify='right')
    totalIncome_entry.place(x=970, y=110)

    totalExpenses_label = Label(accounting_frame, text='Total Expenses:', 
                                            width=14, height=1, bg='green', fg='white',
                                             font=('Arial', 10), anchor='e')
    totalExpenses_label.place(x=850, y=140)

    global totalExpenses_entry
    totalExpenses_entry = Entry(accounting_frame, width=12, font=('Arial', 12), justify='right')
    totalExpenses_entry.place(x=970, y=140)


    netIncome_label = Label(accounting_frame, text='Net Income:', 
                                            width=14, height=1, bg='Red', fg='black',
                                             font=('Arial', 10), anchor='e')
    netIncome_label.place(x=850, y=170)

    global netIncome_entry
    netIncome_entry = Entry(accounting_frame, width=12, font=('Arial', 12), justify='right')
    netIncome_entry.place(x=970, y=170)
    
    
    
    
    btn_search_incomeStatment = Button(accounting_frame, text='Search', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=10, height=1, command=incomeStatement_list_treeview)
    btn_search_incomeStatment.place(x=720, y=35)
    
    
    # this is for treeview for trial Balance
    incomeStatment_view_Form = Frame(accounting_frame, width=500, height=25)
    incomeStatment_view_Form.place(x=15, y=110)

    style = ttk.Style(accounting_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="white",
                    foreground="black",
                    fieldbackground="yellow")
    # change selected color

    style.map('Treeview',
                [('selected','green')])
    
    
    global incomeStatement_treeview
    scrollbarx = Scrollbar(incomeStatment_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(incomeStatment_view_Form, orient=VERTICAL)
    
    incomeStatement_treeview = ttk.Treeview(incomeStatment_view_Form,
                                             columns=("ACCOUNTTITLE",'DEBIT', 'CREDIT'),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=incomeStatement_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=incomeStatement_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    # trialBalance_treeview.heading('ACCOUNT#', text="Account #", anchor=CENTER)
    incomeStatement_treeview.heading('ACCOUNTTITLE', text="Account Title", anchor=CENTER)
    incomeStatement_treeview.heading('DEBIT', text="Debit", anchor=CENTER)
    incomeStatement_treeview.heading('CREDIT', text="Credit", anchor=CENTER)


    incomeStatement_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    incomeStatement_treeview.column('#1', stretch=NO, minwidth=0, width=400, anchor='sw')
    incomeStatement_treeview.column('#2', stretch=NO, minwidth=0, width=200, anchor='e')
    incomeStatement_treeview.column('#3', stretch=NO, minwidth=0, width=200, anchor='e')
    
   
   
   

    incomeStatement_treeview.pack()


def trialBalance_list_treeview():
    
    """
    this function is for
    button to display the list
    of journal entry as per query
    """
    
    trialBalance_treeview.delete(*trialBalance_treeview.get_children())
    return trialBalance_search()


def trialBalance_search():
    """
    this function is for searching
    for per account for
    trial balance purposes 
    """
    dataSearch = db['journal_entry']
    
    datefrom = trialBalance_datefrom.get()
    date_time_obj_from = datetime.strptime(datefrom, '%Y-%m-%d')

    dateto = trialBalance_dateto.get()
    date_time_obj_to = datetime.strptime(dateto, '%Y-%m-%d')

    agg_result= dataSearch.aggregate(
        [
        {"$match": {'date_entry': {'$gte':date_time_obj_from, '$lte':date_time_obj_to}} },
        # {"$match": { "cut_off_period": date } },
        # {'$sort' : { '$meta': "textScore" }, '$account_disc': -1 },
        {"$group" : 
             {"_id" :  '$acoount_number',
            "accountName": {'$first':'$account_disc'},
            "totalDebit" : {"$sum" : '$debit_amount'},
            "totalCredit" : {"$sum" : '$credit_amount'},
            # "accountNum":'$acoount_number'
            
            }},
        {'$sort':{'_id': 1}}
            
        ])
    
    totalDebit = 0
    totalCredit = 0
    for x in agg_result: 
        
                
        account_number = x['accountName']
        debit_amount = x['totalDebit']
        debit_amount2 = '{:,.2f}'.format(debit_amount)
        credit_amount = x['totalCredit']
        credit_amount2 = '{:,.2f}'.format(credit_amount)

        balance_amount = float(debit_amount - credit_amount)
        balance_amount2 = '{:,.2f}'.format(balance_amount)

        totalDebit+=debit_amount
        totalDebit2 = '{:,.2f}'.format(totalDebit)

        totalCredit+=credit_amount
        totalCredit2 = '{:,.2f}'.format(totalCredit)
        
        trialBalance_treeview.insert('', 'end', values=(account_number,
                                                        debit_amount2,
                                                        credit_amount2,
                                                        balance_amount2 ))
                
        totalDebit_trialbalanceTreeview_entry.delete(0, END)
        totalDebit_trialbalanceTreeview_entry.insert(0, (totalDebit2))

        totalCredit_trialbalanceTreeview_entry.delete(0, END)
        totalCredit_trialbalanceTreeview_entry.insert(0, (totalCredit2))



def trialBalance_frame():
    """
    This function
    is for trialbalance frame or button
    """
    cleartrialbalanceFrame()
    global entry_datefrom
    entry_date_label = Label(accounting_frame, text='Date from:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    entry_date_label.place(x=10, y=35)

    global trialBalance_datefrom
    trialBalance_datefrom = DateEntry(accounting_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    trialBalance_datefrom.place(x=120, y=35)
    trialBalance_datefrom.configure(justify='center')
    
    entry_date_label = Label(accounting_frame, text='Date to:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    entry_date_label.place(x=250, y=35)

    global trialBalance_dateto
    trialBalance_dateto = DateEntry(accounting_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    trialBalance_dateto.place(x=350, y=35)
    trialBalance_dateto.configure(justify='center')
    
    
    
    
    btn_searchTrialBalance = Button(accounting_frame, text='Search Entry', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=10, height=1, command=trialBalance_list_treeview)
    btn_searchTrialBalance.place(x=720, y=35)
    
    
    # this is for treeview for trial Balance
    trialBalance_view_Form = Frame(accounting_frame, width=500, height=25)
    trialBalance_view_Form.place(x=15, y=110)

    style = ttk.Style(accounting_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="yellow")
    # change selected color

    style.map('Treeview',
                [('selected','green')])
    
    
    global trialBalance_treeview
    scrollbarx = Scrollbar(trialBalance_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(trialBalance_view_Form, orient=VERTICAL)
    
    trialBalance_treeview = ttk.Treeview(trialBalance_view_Form,
                                             columns=("ACCOUNTTITLE",'DEBIT', 'CREDIT','BALANCE'),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=trialBalance_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=trialBalance_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    # trialBalance_treeview.heading('ACCOUNT#', text="Account #", anchor=CENTER)
    trialBalance_treeview.heading('ACCOUNTTITLE', text="Account Title", anchor=CENTER)
    trialBalance_treeview.heading('DEBIT', text="Debit", anchor=CENTER)
    trialBalance_treeview.heading('CREDIT', text="Credit", anchor=CENTER)
    trialBalance_treeview.heading('BALANCE', text="Balance", anchor=CENTER)


    trialBalance_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    trialBalance_treeview.column('#1', stretch=NO, minwidth=0, width=400, anchor='sw')
    trialBalance_treeview.column('#2', stretch=NO, minwidth=0, width=200, anchor='e')
    trialBalance_treeview.column('#3', stretch=NO, minwidth=0, width=200, anchor='e')
    trialBalance_treeview.column('#4', stretch=NO, minwidth=0, width=200, anchor='e')
    
   
   
   

    trialBalance_treeview.pack()


    netIncome_label = Label(accounting_frame, text='Grand Total', 
                                            width=14, height=1, bg='Red', fg='black',
                                             font=('Arial', 10), anchor='e')
    netIncome_label.place(x=250, y=75)

    global totalDebit_trialbalanceTreeview_entry
    totalDebit_trialbalanceTreeview_entry = Entry(accounting_frame, width=21,
                                             font=('Arial', 12), justify='right')
    totalDebit_trialbalanceTreeview_entry.place(x=415, y=75)

    global totalCredit_trialbalanceTreeview_entry
    totalCredit_trialbalanceTreeview_entry = Entry(accounting_frame, width=21,
                                             font=('Arial', 12), justify='right')
    totalCredit_trialbalanceTreeview_entry.place(x=615, y=75)
    
    
    




def journalEntry_list_treeview():
    
    """
    this function is for
    button to display the list
    of journal entry as per query
    """
    
    journalEntry_treeview.delete(*journalEntry_treeview.get_children())
    return searchJournalEntry_treeview()

def searchJournalEntry_treeview():
    """
    This function is for
    journal Entry List
    """
    dataSearch = db['journal_entry']
    
    # datefrom = journal_entry_datefrom.get()
    # dateto = journal_entry_dateto.get()

    datefrom =  journal_entry_datefrom.get()
    date_time_obj_from = datetime.strptime(datefrom, '%Y-%m-%d')

    dateto = journal_entry_dateto.get()
    date_time_obj_to = datetime.strptime(dateto, '%Y-%m-%d')

    account_search = accountNumber_entry.get()
    ref_search2 = str(account_search)
    
    if  accountNumber_entry.get() == "" and reference_entry.get() =="": 
        
        try:
            cnt = 0
            agg_result= dataSearch.find({'date_entry': {'$gte':date_time_obj_from, '$lte':date_time_obj_to}})
           
            for x in agg_result:
                cnt+=1
                date_entry = x['date_entry']
                journal = x['journal']
                ref = x['ref']
                descriptions = x['descriptions']
                account_number = x['acoount_number']
                account_disc = x['account_disc']
                debit_amount = x['debit_amount']
                debit_amount2 = '{:,.2f}'.format(debit_amount)
                credit_amount = x['credit_amount']
                credit_amount2 = '{:,.2f}'.format(credit_amount)
                
                
                journalEntry_treeview.insert('', 'end', values=(date_entry,journal,
                                    ref,descriptions, account_number,account_disc,debit_amount2,
                                    credit_amount2 ))
                
                
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}")    
    elif reference_entry.get() =="": # this is for date and accountNumber search
        # query = {'date_entry': {'$gte':datefrom, '$lte':dateto}},{'ref':accountNumber_entry.get()}
        try:
            cnt = 0
            # for x in dataSearch.find({'$and' :[{'date_entry': {'$gte':datefrom, '$lte':dateto}},
            #                                    {'acoount_number':accountNumber_entry.get()}]}):

            for x in dataSearch.find({'acoount_number':accountNumber_entry.get()}):
                cnt+=1
                date_entry = x['date_entry']
                journal = x['journal']
                ref = x['ref']
                descriptions = x['descriptions']
                account_number = x['acoount_number']
                account_disc = x['account_disc']
                debit_amount = x['debit_amount']
                debit_amount2 = '{:,.2f}'.format(debit_amount)
                credit_amount = x['credit_amount']
                credit_amount2 = '{:,.2f}'.format(credit_amount)
                
                
                journalEntry_treeview.insert('', 'end', values=(date_entry,journal,
                                    ref,descriptions, account_number,account_disc,debit_amount2,
                                    credit_amount2 ))
              
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}")  
        
    elif accountNumber_entry.get() =="": # this is for date and reference Number search
        # query = {'date_entry': {'$gt':datefrom, '$lt':dateto}},{'ref':accountNumber_entry.get()}
        try:
            cnt = 0
            for x in dataSearch.find({'ref':reference_entry.get()}):
                cnt+=1
                date_entry = x['date_entry']
                journal = x['journal']
                ref = x['ref']
                descriptions = x['descriptions']
                account_number = x['acoount_number']
                account_disc = x['account_disc']
                debit_amount = x['debit_amount']
                debit_amount2 = '{:,.2f}'.format(debit_amount)
                credit_amount = x['credit_amount']
                credit_amount2 = '{:,.2f}'.format(credit_amount)
                
                
                journalEntry_treeview.insert('', 'end', values=(date_entry,journal,
                                    ref,descriptions, account_number,account_disc,debit_amount2,
                                    credit_amount2 ))
              
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}") 


def importChartofAccount():
    """
    This function is for 
    importing chart of account
    """    
    dataSearch = db['chart_of_account']
    agg_result= dataSearch.find()

    a = ""
    for x in agg_result:
        a = x['accountNum']

    with open("chartofaccount.csv",) as stocks:
            r_csv = csv.reader(stocks,delimiter=',')
            accountNum = ""
            for row in r_csv:

                accountNum = row[0]
                accountTitle = row[1]
                bsClass = row[2]
                
            

                if a == accountNum:
                    messagebox.showinfo('JRS',f'Account Number {accountNum} already taken')

                
                else:
                
                    collection = db['chart_of_account'] # this is to create collection and save as table
                    dataInsert = {
                    'accountNum': accountNum,
                    'accountTitle': accountTitle,
                    'bsClass': bsClass,
                    'user': USERNAME.get(),
                    'created':datetime.now()
                    
                    }
                    
                    try:
                        result = tkMessageBox.askquestion('JRS System', 'you want to save data', icon="warning")
                        if result == 'yes':
                            collection.insert_one(dataInsert)
                            messagebox.showinfo('JRS', 'Data has been exported and save')
                        
                    except Exception as ex:
                        messagebox.showerror("Error", f"Error due to :{str(ex)}")    
            

def import_journal_entry():
    """
    This function is for exporting
    entry from nch entry
    """
    # clearFrame()
    with open("journal_entry.csv",) as stocks:
            r_csv = csv.reader(stocks,delimiter=',')
            for row in r_csv:
                    date_entry = row[0]
                    journal = row[1]
                    ref = row[2]
                    descriptions = row[3]
                    acoount_number = row[4]
                    account_disc = row[5]
                    
                    debit_amount = float(row[6])
                    credit_amount = float(row[7])
                    
                    date_time_obj_to = datetime.strptime(date_entry, '%m-%d-%Y')

                    collection = db['journal_entry'] # this is to create collection and save as table
                    dataInsert = {
                    'date_entry': date_time_obj_to,
                    'journal': journal,
                    'ref': ref,
                    'descriptions': descriptions,
                    'acoount_number': acoount_number,
                    'account_disc': account_disc,
                    'debit_amount': debit_amount,
                    'credit_amount': credit_amount,
                    'due_date_apv': '',
                    'terms_days': '',
                    'supplier/Client': '',
                    'user': USERNAME.get(),
                    'created':datetime.now()
                    
                    }

                    
                    try:
                        collection.insert_one(dataInsert)
                        
                    except Exception as ex:
                        messagebox.showerror("Error", f"Error due to :{str(ex)}")    
                    
    messagebox.showinfo('JRS', 'Data has been exported and save')


def importEntry_frame():
    """
    This function
    is for exporting journal
    entry from csv
    """
    cleartrialbalanceFrame()
    global entry_datefrom
    entry_date_label = Label(accounting_frame, text='Date from:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    entry_date_label.place(x=10, y=35)

    global journal_entry_datefrom
    journal_entry_datefrom = DateEntry(accounting_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    journal_entry_datefrom.place(x=120, y=35)
    journal_entry_datefrom.configure(justify='center')
    
    entry_date_label = Label(accounting_frame, text='Date to:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    entry_date_label.place(x=250, y=35)

    global journal_entry_dateto
    journal_entry_dateto = DateEntry(accounting_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    journal_entry_dateto.place(x=350, y=35)
    journal_entry_dateto.configure(justify='center')
    
    
    
    accountNumber_label = Label(accounting_frame, text='Account #:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    accountNumber_label.place(x=470, y=35)
    
    global accountNumber_entry
    accountNumber_entry = Entry(accounting_frame, width=15, font=('Arial', 10), justify='right')
    accountNumber_entry.place(x=570, y=35)

    reference_label = Label(accounting_frame, text='Reference #:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    reference_label.place(x=690, y=35)
    
    global reference_entry
    reference_entry = Entry(accounting_frame, width=15, font=('Arial', 10), justify='right')
    reference_entry.place(x=790, y=35)
    
    btn_searchEntry = Button(accounting_frame, text='Search Entry', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=10, height=1, command=journalEntry_list_treeview)
    btn_searchEntry.place(x=910, y=35)
    
    btn_importEntry = Button(accounting_frame, text='Import Entry', bd=2, bg='yellow', fg='black',
                              font=('arial', 10), width=10, height=1, command=import_journal_entry)
    btn_importEntry.place(x=10, y=70)
    
    
    # this is for treeview for payroll computation
    journaEntry_view_Form = Frame(accounting_frame, width=500, height=25)
    journaEntry_view_Form.place(x=15, y=110)

    style = ttk.Style(accounting_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="yellow")
   
    
    
    global journalEntry_treeview
    scrollbarx = Scrollbar(journaEntry_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(journaEntry_view_Form, orient=VERTICAL)
    
    journalEntry_treeview = ttk.Treeview(journaEntry_view_Form,
                                             columns=('DATE', "JOURNAL","REF",
                                               "DESCRIPTION",
                                              "ACCOUNT",'ACCOUNTTITLE','DEBIT', 'CREDIT'),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=journalEntry_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=journalEntry_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    journalEntry_treeview.heading('DATE', text="Date", anchor=CENTER)
    journalEntry_treeview.heading('JOURNAL', text="Journal", anchor=CENTER)
    journalEntry_treeview.heading('REF', text="Ref", anchor=CENTER)
    journalEntry_treeview.heading('DESCRIPTION', text="Description", anchor=CENTER)
    journalEntry_treeview.heading('ACCOUNT', text="Account #", anchor=CENTER)
    journalEntry_treeview.heading('ACCOUNTTITLE', text="Acct Title", anchor=CENTER)
    journalEntry_treeview.heading('DEBIT', text="Debit", anchor=CENTER)
    journalEntry_treeview.heading('CREDIT', text="Credit", anchor=CENTER)


    journalEntry_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    journalEntry_treeview.column('#1', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntry_treeview.column('#2', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntry_treeview.column('#3', stretch=NO, minwidth=0, width=80, anchor='e')
    journalEntry_treeview.column('#4', stretch=NO, minwidth=0, width=250, anchor='e')
    journalEntry_treeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntry_treeview.column('#6', stretch=NO, minwidth=0, width=250, anchor='e')
    journalEntry_treeview.column('#7', stretch=NO, minwidth=0, width=100, anchor='e')
    journalEntry_treeview.column('#8', stretch=NO, minwidth=0, width=100, anchor='e')
   
   

    journalEntry_treeview.pack()
    
    
    


def accounting_frame():
    """
    This function is for accounting
    frame
    """
    
    clearFrame()
    global accounting_frame

   
        

    accounting_frame = Frame(MidViewForm9, width=1120, height=575, bd=2, bg='gray', relief=SOLID)
    accounting_frame.place(x=160, y=8)

    
    btn_importEntry = Button(MidViewForm9, text='Journal Entry', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command=importEntry_frame)
    btn_importEntry.place(x=2, y=100)
    
    
    btn_trialBalance = Button(MidViewForm9, text='Trial Balance', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command=trialBalance_frame)
    btn_trialBalance.place(x=2, y=160)

    btn_incomeStatement = Button(MidViewForm9, text='Income Statment', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command=incomeStatement_frame)
    btn_incomeStatement.place(x=2, y=220)

    btn_manualJournalEntry = Button(MidViewForm9, text='Manual Entry', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command=journal_entry_insert_frame)
    btn_manualJournalEntry.place(x=2, y=280)

    btn_importChartofAccount = Button(MidViewForm9, text='Import CoA', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command=importChartofAccount)
    btn_importChartofAccount.place(x=2, y=340)
    
# this button is for Employee Details
    # btn_employeeDetails = Button(MidViewForm9, text='Employee Details', bd=2, bg='blue', fg='white',
    #                         font=('arial', 12), width=15, height=2)
    # btn_employeeDetails.place(x=2, y=160)
    

    # btn_1601C = Button(MidViewForm9, text='1601 C Report', bd=2, bg='blue', fg='white',
    #                              font=('arial', 12), width=15, height=2,command=frame_1601)
    # btn_1601C.place(x=2, y=220)
    

    # btn_payroll_export = Button(MidViewForm9, text='Export Excel', bd=2, bg='blue', fg='white',
    #                              font=('arial', 12), width=15, height=2)
    # btn_payroll_export.place(x=2, y=280)
    


#==========================================This is for Payroll Computation ================================================
def computation_1601():
    """
    This function is for 
    computation of 1601C
    """

    collection = db['payroll_computation']

def frame_1601():
    """
    This function
    is for GUI of
    1601C computation
    """
    
    clearpayrollFrame()
    global frame1601c_date
    frame1601c_date_label = Label(payroll_frame, text='Date:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    frame1601c_date_label.place(x=10, y=35)

    frame1601c_date = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    frame1601c_date.place(x=120, y=35)
    frame1601c_date.configure(justify='center')
    
    
    btn_import = Button(payroll_frame, text='Search', bd=2, bg='yellow', fg='black',
                              font=('arial', 10), width=10, height=1, command=computation_1601)
    btn_import.place(x=10, y=70)

    




def searchFor_treeview():
    """"
    This function is for
    searching for payroll computation treeview
    """
    
    payroll_computation_treeview.delete(*payroll_computation_treeview.get_children())
    return payroll_comp_treeview()


def payroll_comp_treeview():
    """
    This is for treeview
    """
    
    dataSearch = db['payroll_computation']
    
    Date_search = payCal_date.get()
    
    query = {'cut_off_period':Date_search }
    try:
        cnt = 0
        for x in dataSearch.find(query):
            cnt+=1
            date_search = x['cut_off_period']
            empID = x['employee_id']
            basicSal = x['basicSal']
            grossPay = x['grossPay']
            totalMan = x['totalMandatory']
            totalDem = x['totalDeminimis']
            totalTaxwidth = x['taxWidthel']
            netPay = x['netpay']
            taxCode = x['taxCode']
            
            
            payroll_computation_treeview.insert('', 'end', values=(cnt,date_search,
                                empID,basicSal, grossPay,totalTaxwidth,netPay ))
            
            
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")    



def payroll_import():
    """
    This function is
    for importing csv file
    for payroll computation
    """
   
    
    
    
    with open("chinessFG.csv",) as stocks:
            r_csv = csv.reader(stocks,delimiter=',')
            for row in r_csv:
                    idNum = row[0]
                    lastName = row[1]
                    basicSalry = float(row[2])
                    mwe = float(row[3])
                    uniform = float(row[4])
                    rice = float(row[5])
                    laundry = float(row[6])
                    medical = float(row[7])
                    medical2 = float(row[8])
                    otherNontax = float(row[9])
                    sss = float(row[10])
                    phic = float(row[11])
                    hdmf =float(row[12])
                    
                    posistion = 0
                    taxCode = str(row[13])
                    allowance = 0
                    fname2 = '0'

    
                    transID = 0
                    overtime = float(0.00)
                    late = float(0.00)
                    holiday = float(0.00)
                    Nightdiff = float(0.00)
                    incentives = float(0.00)
                    adjustment = float(0.00)
                    cashadvance = float(0.00)
                    otherdedcution = float(0.00)
                    totaldeduction = cashadvance + otherdedcution
                    adjustment2 = float(0.00)
                    grosspayMWE = float(0.00)
                    OTmwe = float(0.00)
                    holidayMWE = float(0.00)
                    mandatoryMWE = float(0.00)
                    taxableNotsubject = float(0.00) 
                    lateTaxable = float(0.00)             

                    grosspay = float(basicSalry + allowance + overtime\
                            + late + holiday + Nightdiff + incentives + adjustment)
                    totalMandatory = sss + phic + hdmf
                    taxableBasic = grosspay-mwe
                    totalDeminimis = (  uniform + rice + laundry + medical + medical2 )
                    afterDeminimis = taxableBasic - totalDeminimis
                    taxableAmount = grosspay -totalMandatory-otherNontax - totalDeminimis
                    netpay1 = grosspay - totalMandatory -  totaldeduction
                    mandatoryTaxable = totalMandatory
                    
                    taxable = 0
                    netpay = 0
                    if grosspay >= 50000:
                        taxable = float(grosspay * .25)
                        netpay = netpay1 - taxable
                    else:
                        taxable = float(12500)
                        netpay = netpay1 - taxable
                    # firsttable = float(20833)
                    # secondTable =float(33332.99)
                    
            
                    # taxable = 0
                    # netpay = 0
                    # if taxableAmount <= firsttable:
                    #         taxable = 0
                            
                    # elif taxableAmount <= secondTable and taxableAmount > firsttable:
                    #         comparable = taxableAmount - 20833 
                    #         if comparable <=0 :
                    #                 taxable = 0
                                    
                    #         else:
                    #                 taxable = comparable * .20
                    #                 netpay = netpay1 - taxable
                    
                   
                    collection = db['payroll_computation']
                    dataInsert = {
                    'cut_off_period': payCal_date.get(),
                    'employee_id': idNum,
                    'lastName': lastName,
                    'basicSal': basicSalry,
                    'grossPay': float(grosspay),
                    'totalMandatory': float(totalMandatory),
                    'totalDeminimis': float(totalDeminimis),
                    'taxWidthel': float(taxable),
                    'netpay': float(netpay),
                    'taxCode': str(taxCode),
                    'user': USERNAME.get(),
                    'created':datetime.now()
                    
                    }
                    
                    try:
                        collection.insert_one(dataInsert)
                        
                    except:
                        print('error occured')
    messagebox.showinfo('JRS', 'Data has been exported and save')
    
    
    dataSearch = db['payroll_computation']
    
    Date_search = payCal_date.get()
    
    query = {'cut_off_period':Date_search }
    try:
        cnt = 0
        for x in dataSearch.find(query):
            cnt+=1
            date_search = x['cut_off_period']
            empID = x['employee_id']
            basicSal = x['basicSal']
            grossPay = x['grossPay']
            totalMan = x['totalMandatory']
            totalDem = x['totalDeminimis']
            totalTaxwidth = x['taxWidthel']
            netPay = x['netpay']
            taxCode = x['taxCode']
            
            
            payroll_computation_treeview.insert('', 'end', values=(cnt,date_search,
                                empID,basicSal, grossPay,totalTaxwidth,netPay ))
            
            
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")    
#==============================================Frame for Payroll Transaction=========================================
def payroll_importation():
    """
    This function is
    for importing 
    data from csv file for
    calculation
    """
    global payCal_date
    payCal_date_label = Label(payroll_frame, text='Date:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    payCal_date_label.place(x=10, y=35)

    payCal_date = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    payCal_date.place(x=120, y=35)
    payCal_date.configure(justify='center')
    
    
    btn_import = Button(payroll_frame, text='Import Data', bd=2, bg='yellow', fg='black',
                              font=('arial', 10), width=10, height=1, command=payroll_import)
    btn_import.place(x=10, y=70)
    
    
    
    btn_search = Button(payroll_frame, text='SEARCH', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1, command=searchFor_treeview)
    btn_search.place(x=300, y=35)
    
    # this is for treeview for payroll computation
    payroll_view_Form = Frame(payroll_frame, width=500, height=25)
    payroll_view_Form.place(x=15, y=110)

    style = ttk.Style(payroll_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="yellow")
    # change selected color

    # style.map('Treeview',
    #             background[('selected','green')])
    
    
     

    scrollbarx = Scrollbar(payroll_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(payroll_view_Form, orient=VERTICAL)
    global payroll_computation_treeview
    payroll_computation_treeview = ttk.Treeview(payroll_view_Form,
                                             columns=("COUNT",'DATE', "EMPLOYEEID","BASICSALARY",
                                               "GROSS PAY",
                                              "TOTAL W-TAX",'NETPAY'),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=payroll_computation_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=payroll_computation_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    payroll_computation_treeview.heading('COUNT', text="COUNT", anchor=CENTER)
    payroll_computation_treeview.heading('DATE', text="DATE ", anchor=CENTER)
    payroll_computation_treeview.heading('EMPLOYEEID', text="EMPLOYEE ID", anchor=CENTER)
    payroll_computation_treeview.heading('BASICSALARY', text="BASIC SALARY", anchor=CENTER)
    
    payroll_computation_treeview.heading('GROSS PAY', text="GROSS PAY", anchor=CENTER)
    payroll_computation_treeview.heading('TOTAL W-TAX', text="W-TAX", anchor=CENTER)
    payroll_computation_treeview.heading('NETPAY', text="NET PAY", anchor=CENTER)


    payroll_computation_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    payroll_computation_treeview.column('#1', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#2', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#3', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#4', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#5', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#6', stretch=NO, minwidth=0, width=150, anchor='e')
   
   

    payroll_computation_treeview.pack()

def payroll_transactions():
    #("Head Office", "Admin-Site", "Pampanga", "Rizal-R&F")

    clearFrame()
    global payroll_frame

   
        

    payroll_frame = Frame(MidViewForm9, width=1120, height=575, bd=2, bg='gray', relief=SOLID)
    payroll_frame.place(x=160, y=8)

    
    btn_payrollCal = Button(MidViewForm9, text='Payroll Computation', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command=payroll_importation)
    btn_payrollCal.place(x=2, y=100)
    
# this button is for Employee Details
    btn_employeeDetails = Button(MidViewForm9, text='Employee Details', bd=2, bg='blue', fg='white',
                            font=('arial', 12), width=15, height=2)
    btn_employeeDetails.place(x=2, y=160)
    

    btn_1601C = Button(MidViewForm9, text='1601 C Report', bd=2, bg='blue', fg='white',
                                 font=('arial', 12), width=15, height=2,command=frame_1601)
    btn_1601C.place(x=2, y=220)
    

    btn_payroll_export = Button(MidViewForm9, text='Export Excel', bd=2, bg='blue', fg='white',
                                 font=('arial', 12), width=15, height=2)
    btn_payroll_export.place(x=2, y=280)
    
    
    
    
    

    


def Logout():
    result = tkMessageBox.askquestion('JRS System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':

        root.deiconify()
        reportFrame.destroy()


def dashboard():
    global MidViewForm9
    global logo_icon2
    global reportFrame

    reportFrame = Toplevel()
    reportFrame.title("DashBoard")
    width = 1300
    height = 650
    screen_width = reportFrame.winfo_screenwidth()
    screen_height = reportFrame.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    reportFrame.geometry("%dx%d+%d+%d" % (width, height, x, y))
    reportFrame.resizable = True

#=============================================Frame for time & others in DashBoard======================================
    TopdashboardForm = Frame(reportFrame, width=1295, height=50, bd=2, relief=SOLID)
    TopdashboardForm.place(x=1,y=8)
#============================================================= menu Bar=================================================
    menubar = Menu(reportFrame)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)
    filemenu5 = Menu(menubar, tearoff=0)
    filemenu6 = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Logout", command = Logout)
    # filemenu.add_command(label="Exit")
    filemenu2.add_command(label="Product Registration")
    filemenu2.add_command(label="Add new")
    filemenu2.add_command(label="View")
    filemenu3.add_command(label="Payroll",command=payroll_transactions)
   
    filemenu4.add_command(label="Accounting Module", command=accounting_frame)
    filemenu4.add_command(label="Insert Customer", command=insert_customer_frame)
    filemenu4.add_command(label="Insert Supplier", command=insert_supplier_frame)
    filemenu4.add_command(label="Account Payable", command=accountPayble_insert_frame)
    filemenu6.add_command(label="Equipment Module")
    filemenu5.add_command(label="Reports Module")
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    menubar.add_cascade(label="Payroll Transactions", menu=filemenu3)
    menubar.add_cascade(label="Accounting Transaction", menu=filemenu4)
    
    menubar.add_cascade(label="Equipment", menu=filemenu6)
    menubar.add_cascade(label="Reports", menu=filemenu5)

    reportFrame.config(menu=menubar)


    MidViewForm9 = Frame(reportFrame, width=1295, height=600,bd=2,relief=SOLID)
    MidViewForm9.place(x=1, y=58)
    MidViewForm9.config(bg="skyblue")


    load2 = PIL.Image.open("image\search2.jpg")
    load2 = load2.resize((125, 50), PIL.Image.ANTIALIAS)
    logo_icon2 = ImageTk.PhotoImage(load2)

    UserName = userName_entry.get()
    user_label = Label(TopdashboardForm, text='Sign in as', width=17, height=1, bg='yellow', fg='gray',
                      font=('Arial', 11), anchor='c')
    user_label.place(x=5, y=15)


    user_Name_label = Label(TopdashboardForm, text='', width=17, height=1, bg='yellow', fg='gray',
                       font=('Arial', 11), anchor='c')
    user_Name_label.place(x=175, y=15)
    user_Name_label.config(text=UserName, fg="red")

    # :%a, %b %d %Y
    DateTime_label = Label(TopdashboardForm, text=f"{dt.datetime.now():%a, %b %d %Y %I:%M %p}",
                           fg="white", bg="black", font=("helvetica", 10))
    DateTime_label.place(x=1100, y=15)



USERNAME =StringVar()
PASSWORD = StringVar()



# ======================================LOGIN ============================================
def Login(event=None):
    if user_description.get() =="Admin":
        if USERNAME.get == "" or PASSWORD.get() == "":
                lbl_result.config(text="Please complete the required field!", fg="red")
        else:
            dataSearch = db['login']

            # query = dataSearch.find_one({'name': USERNAME.get(), 'password':PASSWORD.get()})
            # query = {'username': USERNAME.get(), 'password':PASSWORD.get(),'status':'approved'}
            # search_variable = dataSearch.find_one(query)
            # search_variable = dataSearch.find_one({'$and' :[{'username': USERNAME.get()} ,
            #                                    {'password':PASSWORD.get()},
            #                                    {'status':'approved'}
            #                                    ]})

            agg_result= dataSearch.aggregate( [
                    {"$match": {'status':'approved',
                        '$and': [
                        {'username': USERNAME.get()},
                        {'password': PASSWORD.get()}           
                        ]}},
                    
                                                        
                    {"$group" : 
                        {"_id" : '$username',
                        "count" : {"$sum" : 1},
                        
                        }},
                    
                    ])


            # listCusor = list(agg_result)

            # df = pd.DataFrame(listCusor)
            # # test = df.head()
            # print(df)

            for x in agg_result :
                
                a = x['count']
                try:

                # if a is None:
                    
                #     lbl_result.config(text="Invalid username or password", fg="red")
                #     USERNAME.set("")
                #     PASSWORD.set("")
                    

                # elif a >= 0:

                    PASSWORD.set("")
                    lbl_result.config(text="")
                    root.withdraw()
                    dashboard()
                except Exception as ex:
                    messagebox.showerror("Error", f"Error due to :{str(ex)}")
    





# ================================================= label and entryfields ===========================================


global userName_entry
global password_entry
logolbl = Label(root,image= logo_icon)
logolbl.place(x=200,y=40)

loginlabe = Label(root,text='Sign in as',width=17,height=1,bg='yellow',fg='gray',
                            font=('Arial',14),anchor='c')
loginlabe.place(x=350,y=70)

user_description = ttk.Combobox(root, width=19,font=('Arial',13))
user_description['values'] = ("Admin", "Employee")
user_description.place(x=350, y=105)

username_lbl = Label(root,text='Username',width=14,height=1,bg='yellow',fg='gray',
                            font=('Arial',11),anchor='c')
username_lbl.place(x=200,y=260)

userName_entry = Entry(root, width=22,textvariable = USERNAME, font=('Arial', 12))
#userName_entry.insert(0, u'enter username')
userName_entry.place(x=350, y=260)


password_lbl = Label(root,text='Password',width=14,height=1,bg='yellow',fg='gray',
                            font=('Arial',11),anchor='c')
password_lbl.place(x=200,y=290)

password_entry = Entry(root, width=22,textvariable = PASSWORD, font=('Arial', 12),show="*")
#password_entry.insert(0,u'enter password')
password_entry.place(x=350, y=290)

lbl_result = Label(root, text="", bg='skyblue', font=('arial', 13),anchor='c')
lbl_result.place(x=200, y=320)


btn_login = Button(root, text="Login", font=('arial', 12), width=39,command=Login)
btn_login.place(x=200, y=340)
# btn_login.bind('<Return>', Login),



# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()


