import mysql.connector
from tkinter import *
from PIL import Image, ImageTk
import PIL.Image
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import datetime as dt
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

#from PIL import ImageTk, Image as PILImage
#from payroll import selectTransaction
import babel.numbers

from tkinter.scrolledtext import ScrolledText

#from payroll import payroll_transactions

import csv

from pymongo import MongoClient
import pandas as pd
import re

from bson.objectid import ObjectId
import dateutil.parser
import pymongo

import certifi
ca = certifi.where()


cluster = "mongodb+srv://joeysabusido:genesis11@cluster0.bmdqy.mongodb.net/ldglobal?retryWrites=true&w=majority"
client = MongoClient(cluster)

db = client.ldglobal

mydb = mysql.connector.connect(
            host="192.46.225.247",
            user="joeysabusido",
            password="Genesis@11",
            database="ldglobal",
            auth_plugin='mysql_native_password')
cursor = mydb.cursor()
# this is to create table for admin login
cursor.execute(
        "CREATE TABLE IF NOT EXISTS admin (id INT AUTO_INCREMENT PRIMARY KEY,\
             username VARCHAR(250), password VARCHAR(250))")
# this is to create table for employee Log In
cursor.execute(
        "CREATE TABLE IF NOT EXISTS user_employee (id INT AUTO_INCREMENT PRIMARY KEY,\
             username VARCHAR(250), password VARCHAR(250))")
# this is to creaete table for cut-off period!!!!
cursor.execute(
        "CREATE TABLE IF NOT EXISTS cut_off (id INT AUTO_INCREMENT PRIMARY KEY,\
             datefrom DATE,\
              dateto DATE,\
              payrollDate Date)")
# THIS IS TO CREATE SSS LOAN TABLE DEDUCTION
cursor.execute(
        "CREATE TABLE IF NOT EXISTS sss_loanDeduction (employee_id VARCHAR(250),\
             lastname VARCHAR(250) ,\
              firstname VARCHAR(250),\
                loan_deduction DECIMAL (18,2),\
                id INT AUTO_INCREMENT PRIMARY KEY)")
# THIS IS TO CREATE TABLE FOR HMDF LOAN
cursor.execute(
        "CREATE TABLE IF NOT EXISTS HDMF_loanDeduction (employee_id VARCHAR(250),\
             lastname VARCHAR(250) ,\
              firstname VARCHAR(250),\
                loan_deduction DECIMAL (18,2),\
                id INT AUTO_INCREMENT PRIMARY KEY)")

# THIS IS TO CREATE TABLE FOR CASH ADVANCE
cursor.execute(
        "CREATE TABLE IF NOT EXISTS cash_advance (employee_id VARCHAR(250),\
             lastname VARCHAR(250) ,\
              firstname VARCHAR(250),\
                ca_deduction DECIMAL (18,2),\
                id INT AUTO_INCREMENT PRIMARY KEY)")
# THIS IS TO CREATE PAYROLL COMPUTATION TABLE!!!!
cursor.execute(
        "CREATE TABLE IF NOT EXISTS payroll_computation (id INT AUTO_INCREMENT PRIMARY KEY,\
             department VARCHAR (250),\
             cut_off_date DATE,\
             employee_id VARCHAR (250),\
             last_name VARCHAR (250),\
             first_name VARCHAR (250),\
             position_name VARCHAR (250),\
             salary_rate DECIMAL (18,2),\
             provicaial_rate DECIMAL (18,2),\
             regular_day DECIMAL (18,2),\
            regularday_cal DECIMAL (18,2),\
            regularday_ot DECIMAL (18,2),\
            regularday_ot_cal DECIMAL (18,2),\
            regularsunday DECIMAL (18,2),\
            regularsunday_cal DECIMAL (18,2),\
            regularsunday_ot DECIMAL (18,2),\
            regularsunday_ot_cal DECIMAL (18,2),\
            spl DECIMAL (18,2),\
            spl_cal DECIMAL (18,2),\
            spl_ot DECIMAL (18,2),\
            spl_ot_cal DECIMAL (18,2),\
            legal_day DECIMAL (18,2),\
            legal_day_cal DECIMAL (18,2),\
            legal_day_ot DECIMAL (18,2),\
            legal_day_ot_cal DECIMAL (18,2),\
            shoprate_day DECIMAL (18,2),\
            shoprate_day_cal DECIMAL (18,2),\
            proviRate_day DECIMAL (18,2),\
            proviRate_day_cal DECIMAL (18,2),\
            proviRate_day_ot DECIMAL (18,2),\
            proviRate_day_ot_cal DECIMAL (18,2),\
            provisun_day DECIMAL (18,2),\
            provisun_day_cal DECIMAL (18,2),\
            provisun_day_ot DECIMAL (18,2),\
            provisun_day_ot_cal DECIMAL (18,2),\
            nightdiff_day DECIMAL (18,2),\
            nightdiff_day_cal DECIMAL (18,2),\
            adjustment DECIMAL (18,2),\
            adjustment_cal DECIMAL (18,2),\
            grosspay_save DECIMAL (18,2),\
            salaryDetails_save VARCHAR (250),\
            sss_save DECIMAL (18,2),\
            phic_save DECIMAL (18,2),\
            hmdf_save DECIMAL (18,2),\
            sss_provi_save DECIMAL (18,2),\
            total_mandatory DECIMAL(18,2),\
            uniform_save DECIMAL (18,2),\
            rice_save DECIMAL (18,2),\
            laundry_save DECIMAL (18,2),\
            medical1_save DECIMAL (18,2),\
            medical2_save DECIMAL (18,2),\
            totalDem_save DECIMAL (18,2),\
            otherforms_save DECIMAL (18,2),\
            taxable_amount DECIMAL(18,2), \
            taxwitheld_save DECIMAL (18,2),\
            cashadvance_save DECIMAL (18,2),\
            sssloan_save DECIMAL (18,2),\
            hdmfloan_save DECIMAL (18,2),\
            netpay_save DECIMAL (18,2),\
            userlog VARCHAR (250),\
            time_update TIMESTAMP)")

cursor.execute(
        """CREATE TABLE IF NOT EXISTS `diesel_consumption` (
          id INT AUTO_INCREMENT PRIMARY KEY,
          `transaction_date` date DEFAULT NULL,
          `equipment_id` varchar(250) DEFAULT NULL,
          `withdrawal_slip` varchar(250) DEFAULT NULL,
          `use_liter` decimal(18,2) DEFAULT NULL,
          `price` decimal(18,2) DEFAULT NULL,
          `amount` decimal(18,2) DEFAULT NULL,
          `transaction_id` varchar(250) DEFAULT NULL)"""
            )

cursor.execute(
    """CREATE TABLE IF NOT EXISTS `equipment_rental` (
  id INT AUTO_INCREMENT PRIMARY KEY,
  `transaction_id` varchar(250) DEFAULT NULL,
  `transaction_date` date DEFAULT NULL,
  `equipment_id` varchar(250) DEFAULT NULL,
  `total_rental_hour` decimal(18,2) DEFAULT NULL,
  `rental_rate` decimal(18,2) DEFAULT NULL,
  `rental_amount` decimal(18,2) DEFAULT NULL,
  `username` VARCHAR(250) DEFAULT NULL,
  `date_update` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"""
    )



# create table for cost entry expense
cursor.execute(
    "CREATE TABLE IF NOT EXISTS cost_entry (\
        id INT NOT NULL AUTO_INCREMENT,\
        trans_date DATE,\
        equipment_id VARCHAR(150),\
        clasification VARCHAR(250),\
        cost_amount DECIMAL(18,2),\
        username VARCHAR(250),\
        update_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\
        PRIMARY KEY(id)); ")
# cursor.execute("ALTER TABLE diesel_consumption ADD  date_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP \
#                              after username; ")

# cursor.execute("ALTER TABLE equipment_rental ADD  date_update TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP \
#                              after username; ")

# this is to create table for part Registration

# cursor.execute("ALTER TABLE payroll_computation  \
#                             DROP COLUMN salaryDetails_save; ")

# cursor.execute("ALTER TABLE employee_details ADD update_date TIMESTAMP \
#                              after user; ")

# cursor.execute("ALTER TABLE employee_details ADD off_on_details VARCHAR(250) \
#                              after Salary_Detail; ")

# cursor.execute("ALTER TABLE payroll_computation ADD taxable_mwe_detail VARCHAR(250) \
#                              after netpay_save; ")

#cursor.execute("INSERT INTO  user_employee (username, password) VALUES('royrin', 'simon')")
mydb.commit()

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

global mwe_monthly
mwe_monthly = 10920/2 # monthly Minimum Wage Earner
total_deminimis = 3883.64/2


class DateEntry(TkcDateEntry):
    def _setup_style(self, event=None):
        # override problematic method to implement fix
        self.style.layout('DateEntry', self.style.layout('TCombobox'))
        self.update_idletasks()
        conf = self.style.configure('TCombobox')
        if conf:
            self.style.configure('DateEntry', **conf)
        # The issue comes from the line below:
        maps = self.style.map('TCombobox')
        if maps:
            try:
                self.style.map('DateEntry', **maps)
            except tk.TclError:
                # temporary fix to issue #61: manually insert correct map
                maps = {'focusfill': [('readonly', 'focus', 'SystemHighlight')],
                        'foreground': [('disabled', 'SystemGrayText'),
                                       ('readonly', 'focus', 'SystemHighlightText')],
                        'selectforeground': [('!focus', 'SystemWindowText')],
                        'selectbackground': [('!focus', 'SystemWindow')]}
                self.style.map('DateEntry', **maps)
        try:
            self.after_cancel(self._determine_downarrow_name_after_id)
        except ValueError:
            # nothing to cancel
            pass
        self._determine_downarrow_name_after_id = self.after(10, self._determine_downarrow_name)
#===============================================Clear frame  in Equipment Rental==============================================
def clear_rentalModule():
    # destroy all widgets from frame
    for widget in equipmentModule_frame.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    equipmentModule_frame.pack_forget()
#===============================================Clear all widgets in Frame==============================================
def clearFrame():
    # destroy all widgets from frame
    for widget in MidViewForm9.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    MidViewForm9.pack_forget()

#=========================================Clear Frame from Inventory Frame=============================================
def clearInventory_frame():
    # destroy all widgets from frame
    for widget in inventory_frame.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    inventory_frame.pack_forget()

#=============================================Clear Frame from Payroll Frame============================================
def clearpayrollFrame():
    # destroy all widgets from frame
    for widget in payroll_frame.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    payroll_frame.pack_forget()




#=====================================Accounting Frame==============================================================
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
            
            
            journalEntryInsert_datefrom.insert(0, date_entry)
            journal_manual.insert(0, journal)
            reference_manual_entry.insert(0, ref)
            journal_memo_entry.insert('1.0', descriptions)
            account_number_entry.insert(0, account_number)
            chart_of_account_manual.insert(0, account_disc)
            debit_manual_entry.insert(0, debit_amount)
            credit_manual_entry.insert(0, credit_amount)
            Selected_ID_entry.insert(0, id_num)
            

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
    'debit_amount': debit_entry,
    'credit_amount': credit_entry,
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

    for x in agg_result :
        a = x['ref']
        current_year =  datetime.today().year
        if a is not None:
            reference_manual = a 
            res = re.sub(r'[0-9]+$',
                    lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}", 
                    reference_manual)

            reference_manual_entry.delete(0, END)
            reference_manual_entry.insert(0, (res))
            
        
        else:
            test_str = 'ENTRY-000'
            res = test_str

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
        account_number_entry.delete(0, END)
        account_number_entry.insert(0, (a))




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


    selected_label = Label(accounting_frame, text='Transaction ID:', 
                                            width=14, height=1, bg='yellowgreen', fg='black',
                                             font=('Arial', 10), anchor='c')
    selected_label.place(x=700, y=235)

    global Selected_ID_entry
    Selected_ID_entry = Entry(accounting_frame, width=16, font=('Arial', 10), justify='right')
    Selected_ID_entry.place(x=820, y=235)


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
    with open("chartofaccount.csv",) as stocks:
            r_csv = csv.reader(stocks,delimiter=',')
            for row in r_csv:
                    accountNum = row[0]
                    accountTitle = row[1]
                   
                    
                    
                    
                    collection = db['chart_of_account'] # this is to create collection and save as table
                    dataInsert = {
                    'accountNum': accountNum,
                    'accountTitle': accountTitle,
                    'user': USERNAME.get(),
                    'created':datetime.now()
                    
                    }
                    
                    try:
                        collection.insert_one(dataInsert)
                        
                    except Exception as ex:
                        messagebox.showerror("Error", f"Error due to :{str(ex)}")    
                    
    messagebox.showinfo('JRS', 'Data has been exported and save')
   
        

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

    
#=============================================Equipment Module==========================================================
def cost_per_equipment_list():
    """This function is for displaying list of cost per Equipment"""
    mydb._open_connection()
    cursor = mydb.cursor()
    date1 = costEquip_sateSearchFrom.get()
    date2 = costEquip_sateSearchTo.get()

    try:
    
        

        # query = "Select * \
        #         from equipment_rental\
        #         where transaction_date\
        #         BETWEEN '" + date1 + "' and\
        #         '" + date2 + "' \
        #         "
        # cursor.execute(query)
        # row = cursor.fetchone()

        # if row == None:

        #     messagebox.showerror("Error", "No record from Rental data with the date Selected")

        # else:
            
        query = "Select\
                    equipment_id,\
                    sum(total_rental_hour) as TotalRental,\
                    sum(rental_amount) as TotalRental \
                    from equipment_rental\
                    where transaction_date\
                    BETWEEN '" + date1 + "' and\
                    '" + date2 + "' \
                    GROUP BY equipment_id \
                    "
        cursor.execute(query)
        myresult = cursor.fetchall()

        for row  in myresult:
            equipID_rental = row[0]
           
            total_rental_hour = row[1]
            total_rental_amount = row[2]

            query2 = "Select\
                            equipment_id,\
                            sum(use_liter) as diesel,\
                            sum(amount) as totalAmount \
                            from diesel_consumption\
                            where transaction_date\
                            BETWEEN '" + date1 + "' and\
                            '" + date2 + "' and equipment_id = '" + equipID_rental + "' \
                            GROUP BY equipment_id \
                        "
            cursor.execute(query2)
            myresult = cursor.fetchall()
            for row in myresult:
                equipID_diesel = row[0]
                totalAmount_diesel = row[2]


                query2 = "Select\
                                equipment_id,\
                                sum(cost_amount) as TotalCost\
                                from cost_entry\
                                where trans_date\
                                BETWEEN '" + date1 + "' and\
                                '" + date2 + "' and equipment_id = '" + equipID_diesel + "' \
                                GROUP BY equipment_id \
                            "
                cursor.execute(query2)
                myresult = cursor.fetchall()

                for row in myresult:
                    equipID_cost = row[0]
                    amount_cost = row[1]


                    totalhours = total_rental_hour
                    totalhours2 = '{:,.2f}'.format(totalhours)

                    total_dieselAmount = totalAmount_diesel
                    total_dieselAmount2 = '{:,.2f}'.format(total_dieselAmount)


                    costing = amount_cost
                    costing2 = '{:,.2f}'.format(costing)

                    totalCost = total_dieselAmount + costing
                    totalCost2 = '{:,.2f}'.format(totalCost)

                    cost_per_equipment = totalCost / totalhours
                    cost_per_equipment2 = '{:,.2f}'.format(cost_per_equipment)

                    cost_per_equipment_treeview.insert('', 'end', values=(
                                equipID_cost, totalhours2, total_dieselAmount2, costing2,
                                totalCost2, cost_per_equipment2 ))

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")
    # query = "Select\
    #             equipment_id,\
    #             sum(total_rental_hour) as TotalRental,\
    #             sum(rental_amount) as TotalRental \
    #             from equipment_rental\
    #             where transaction_date\
    #             BETWEEN '" + date1 + "' and\
    #             '" + date2 + "' \
    #             GROUP BY equipment_id \
    #             "
    # cursor.execute(query)
    # myresult = cursor.fetchall()

    # transDate = ''
    # equipID = ''
    # rental_hour = 0
    # totalrow = 0

    # rental_report = {}
    # for i in myresult:
    #     data = {i[0]:
    #                 {'totalHours': i[1],
    #                 'total_rental_amount': i[2]
    #                  }
    #             }

    #     rental_report.update(data)

    # for j in rental_report:
    #     equipmID = j
    #     total1 = rental_report[j]['totalHours']

    #     query2 = "Select\
    #                 equipment_id,\
    #                 sum(use_liter) as diesel,\
    #                 sum(amount) as totalAmount \
    #                 from diesel_consumption\
    #                 where transaction_date\
    #                 BETWEEN '" + date1 + "' and\
    #                 '" + date2 + "'  \
    #                 GROUP BY equipment_id \
    #             "
    #     cursor.execute(query2)
    #     myresult = cursor.fetchall()

    #     diesel_report = {}
    #     for h in myresult:
    #         data2 = {h[0]:
    #                      {'totalliters': h[1],
    #                         'totalAmount': h[2]
    #                       }
    #                  }
    #         diesel_report.update(data2)
    #     liters_per_hour = 0
    #     for k in diesel_report:
    #         total2 = diesel_report[k]['totalliters']

    #         query2 = "Select\
    #                 equipment_id,\
    #                 sum(cost_amount) as TotalCost\
    #                 from cost_entry\
    #                 where trans_date\
    #                 BETWEEN '" + date1 + "' and\
    #                 '" + date2 + "'  \
    #                 GROUP BY equipment_id\
    #             "
    #         cursor.execute(query2)
    #         myresult = cursor.fetchall()

    #         cost_report = {}
    #         for c in myresult:
    #             data2 = {c[0]:
    #                         {
    #                          'totalCost': c[1]
    #                         }
    #                     }
    #             cost_report.update(data2)
    #         total_cost = 0
    #         totalhours= 0
    #         total_dieselAmount = 0
    #         costing = 0
    #         cost_per_equipment = 0
    #         totalCost = 0
    #         for cost in cost_report:
                
    #             if k == cost and cost == j :
                    
    #                 totalhours= rental_report[j]['totalHours']
    #                 totalhours2 = '{:,.2f}'.format(totalhours)

    #                 total_dieselAmount =diesel_report[k]['totalAmount']
    #                 total_dieselAmount2 = '{:,.2f}'.format(total_dieselAmount)


    #                 costing =cost_report[cost]['totalCost']
    #                 costing2 = '{:,.2f}'.format(costing)

    #                 totalCost = total_dieselAmount + costing
    #                 totalCost2 = '{:,.2f}'.format(totalCost)

    #                 cost_per_equipment = totalCost / totalhours
    #                 cost_per_equipment2 = '{:,.2f}'.format(cost_per_equipment)

    #                 cost_per_equipment_treeview.insert('', 'end', values=(
    #                         k, totalhours2, total_dieselAmount2, costing2,
    #                         totalCost2, cost_per_equipment2 ))



def cost_per_equipment_frame():
    """This is for cost per Equipment Frame"""
    clear_rentalModule()
    ltrHrs_sateSearchFrom_label = Label(equipmentModule_frame, text='Date From', width=10, height=1, bg='yellow',
                                        fg='gray',
                                        font=('Arial', 10), anchor='e')
    ltrHrs_sateSearchFrom_label .place(x=300, y=15)
    global costEquip_sateSearchFrom
    costEquip_sateSearchFrom = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                      foreground='white', borderwidth=2, padx=10, pady=10)
    costEquip_sateSearchFrom.place(x=400, y=15)
    costEquip_sateSearchFrom.configure(justify='center')

    ltrHrs_sateSearchTO_label = Label(equipmentModule_frame, text='Date To', width=10, height=1, bg='yellow',
                                        fg='gray',
                                        font=('Arial', 10), anchor='e')
    ltrHrs_sateSearchTO_label.place(x=550, y=15)
    global costEquip_sateSearchTo
    costEquip_sateSearchTo = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
    costEquip_sateSearchTo.place(x=650, y=15)
    costEquip_sateSearchTo.configure(justify='center')

    btn_costEquip_search = Button(equipmentModule_frame, text='Search', bd=2, bg='green', fg='white',
                               font=('arial', 10), width=10, height=1, command=cost_per_equipment_list)
    btn_costEquip_search.place(x=750, y=15)
    btn_costEquip_search.bind('<Return>', cost_per_equipment_list)

    # this is for Tree View for Rental Equipment
    cost_view_Form = Frame(equipmentModule_frame, width=500, height=450)
    cost_view_Form.place(x=120, y=50)

    style = ttk.Style(equipmentModule_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="yellow")
    # change selected color

    # style.map('Treeview',
    #             background[('selected','green')])

    scrollbarx = Scrollbar(cost_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(cost_view_Form, orient=VERTICAL)
    global cost_per_equipment_treeview
    cost_per_equipment_treeview = ttk.Treeview(cost_view_Form,
                                             columns=("EQUIPMENTID", "TOTALRENTALS",
                                              "TOTALDIESEL", "EXPENSES",
                                              "TOTALEXPENSES",'COSTPEREQUIP'),
                                             selectmode="extended", height=21, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=cost_per_equipment_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=cost_per_equipment_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    cost_per_equipment_treeview.heading('EQUIPMENTID', text="EQUIPMENT ID", anchor=CENTER)
    cost_per_equipment_treeview.heading('TOTALRENTALS', text="TOTAL RENTAL HOURS", anchor=CENTER)
    cost_per_equipment_treeview.heading('TOTALDIESEL', text="TOTAL DIESEL AMOUNT", anchor=CENTER)
    cost_per_equipment_treeview.heading('EXPENSES', text="EXPENSES", anchor=CENTER)
    cost_per_equipment_treeview.heading('TOTALEXPENSES', text="TOTAL EXPENSE", anchor=CENTER)
    cost_per_equipment_treeview.heading('COSTPEREQUIP', text="COST PER EQUIPMENT", anchor=CENTER)


    cost_per_equipment_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    cost_per_equipment_treeview.column('#1', stretch=NO, minwidth=0, width=150, anchor='e')
    cost_per_equipment_treeview.column('#2', stretch=NO, minwidth=0, width=150, anchor='e')
    cost_per_equipment_treeview.column('#3', stretch=NO, minwidth=0, width=150, anchor='e')
    cost_per_equipment_treeview.column('#4', stretch=NO, minwidth=0, width=150, anchor='e')
    cost_per_equipment_treeview.column('#5', stretch=NO, minwidth=0, width=150, anchor='e')
    cost_per_equipment_treeview.column('#6', stretch=NO, minwidth=0, width=150, anchor='e')


    
    cost_per_equipment_treeview.pack()

def cost_entry_save():
    """This function is to save cost entry"""
    mydb._open_connection()
    cursor = mydb.cursor()
    username = userName_entry.get()

    try:
        if cost_equipmentID_entry.get() == "" or cost_clasfn_entry.get() == ''\
                or cost_amount_entry.get() == "":
            messagebox.showerror("Error", "Entry field is  required")

        else:
            cursor.execute("INSERT INTO cost_entry (trans_date,equipment_id,clasification,"
                           "cost_amount,username)"
                           
                           " VALUES(%s, %s, %s, %s, %s)",

                           (cost_date.get(),cost_equipmentID_entry.get(),
                            cost_clasfn_entry.get(),
                            cost_amount_entry.get(), username ))

            messagebox.showinfo('JRS', 'Data has been Save')

   

            mydb.commit()
            mydb.close()
            cursor.close()
            # diesel_registry_list()

            cost_amount_entry.delete(0, END)
            cost_equipmentID_entry.delete(0, END)
            



    except Exception as ex:
        messagebox.showerror("Erro", f"Error due to :{str(ex)}")



def cost_entry():
    """This function is for supplier frame """
    clear_rentalModule()
    diesel_date_label1 = Label(equipmentModule_frame, text='Date:', width=20, height=1, bg='gray', fg='yellow',
                               font=('Arial', 11), anchor='e')
    diesel_date_label1.place(x=10, y=15)

    global cost_date
    cost_date = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                foreground='white', borderwidth=2, padx=10, pady=10)
    cost_date.place(x=225, y=15)
    cost_date.configure(justify='center')

    cost_euipID_lbl = Label(equipmentModule_frame, text='Equpment ID:', width=20, height=1, bg='gray', fg='yellow',
                       font=('Arial', 11), anchor='e')
    cost_euipID_lbl.place(x=10, y=42)

    global cost_equipmentID_entry
    cost_equipmentID_entry = ttk.Combobox(equipmentModule_frame, width=20)
    cost_equipmentID_entry['values'] = equipmentFields()
    cost_equipmentID_entry.place(x=225, y=42)

    pr_clasfn = Label(equipmentModule_frame, text='Classification:', width=20, height=1, bg='gray', fg='yellow',
                     font=('Arial', 11), anchor='e')
    pr_clasfn.place(x=10, y=69)

    # pr_clasfn_entry = Entry(inventory_frame,  width=22, font=('Arial', 11), justify='right')
    # pr_clasfn_entry.place(x=140, y=185)

    global cost_clasfn_entry
    cost_clasfn_entry = ttk.Combobox(equipmentModule_frame, width=20)
    cost_clasfn_entry['values'] = ("Salaries", "Oil-lubes", "Repair-Maintenance", "Meals",
                                 "Tranpo", "Tires", "Depreciation","Others")
    cost_clasfn_entry.place(x=225, y=69)


    cost_amount_lbl = Label(equipmentModule_frame, text='Search:', width=20, height=1, bg='gray',
                                   fg='yellow',
                                   font=('Arial', 11), anchor='e')
    cost_amount_lbl.place(x=10, y=97)

    global cost_amount_entry

    cost_amount_entry = Entry(equipmentModule_frame, width=18, font=('Arial', 11), justify='left')
    cost_amount_entry.place(x=225, y=97)
    

    global cost_btn_save_account
    cost_btn_save_account = Button(equipmentModule_frame, text='Save', bd=2, bg='black', fg='white',
                                 font=('arial', 10), width=12, height=1, command = cost_entry_save)
    cost_btn_save_account.place(x=80, y=127)
    

    cost_btn_update = Button(equipmentModule_frame, text='Update', bd=2, bg='green', fg='white',
                                       font=('arial', 10), width=12, height=1)
    cost_btn_update.place(x=190, y=127)
    # supplier_btn_update.bind('<Return>', supplier_update)

    supplier_search_lbl = Label(equipmentModule_frame, text='Search', width=10, height=1, bg='gray',
                                   fg='yellow',
                                   font=('Arial', 11), anchor='e')
    supplier_search_lbl.place(x=350, y=15)

    global cost_search_entry

    cost_search_entry = Entry(equipmentModule_frame, width=10, font=('Arial', 11), justify='left')
    cost_search_entry.place(x=450, y=15)

    cost_search_btn = Button(equipmentModule_frame, text='Search', bd=2, bg='Blue', fg='white',
                                       font=('arial', 10), width=12, height=1)
    cost_search_btn.place(x=550, y=15)
    # supplier_btn_search.bind('<Return>', supplier_search)


  

    if user_description.get() == "Employee":
        cost_btn_update['state'] = DISABLED

def diesel_registry_search_with_equipID():
    """This function is for searching Diesel Registry tru Date Query"""
    mydb._open_connection()
    cursor = mydb.cursor()
    equipment_diesel_treeview.delete(*equipment_diesel_treeview.get_children())
    Date1 = diesel_sateSearchFrom.get()
    Date2 = diesel_sateSearchTo.get()
    equipmentID = diesel_equipmentID_entry_list_search.get()
    cursor.execute("Select \
            `transaction_date`,\
            `equipment_id` ,\
            `withdrawal_slip`, \
            `use_liter`, \
            `price`,\
            `amount`,\
            `username` ,\
            `date_update`,\
            `id`\
            FROM  diesel_consumption\
            WHERE transaction_date BETWEEN '" + Date1 +"' AND '"+ Date2 + "' \
            AND equipment_id = '"+ equipmentID + "' \
            ORDER by id DESC\
                ")

    fetch = cursor.fetchall()
    cnt = 0
    balance = 0
    for data in fetch:
        cnt += 1
        date1 = data[0]
        equip_id = data[1]

        useLiter = data[3]
        price = data[4]
        amount = data[5]
        balance = amount + balance
        userName_rental = data[6]
        dateUpdate = data[7]
        trans_id = data[8]
        amount2 = '{:,.2f}'.format(data[5])
        balance2 = '{:,.2f}'.format(balance)

        equipment_diesel_treeview.insert('', 'end', values=(
            cnt, trans_id, date1, equip_id, useLiter, price, amount2, balance2,
            userName_rental, dateUpdate))
def update_diesel_registry():
    """
    This function is for 
    updating diesel registry
    """
    mydb._open_connection()
    cursor = mydb.cursor()
    
    
    diesel_date_update = diesel_dateFrom.get()
    equipmentID = diesel_equipmentID_entry_list.get()
    withdrawalSlip = withdrawalslip_diesel_entry.get()
    totalliter = total_diesel_entry.get()
    dieselRate = diesel_rate_entry.get()
    totalAmount = diesel_amount_entry.get()
    
    
    try:
        if diesel_search_entry.get() == '':
            messagebox.showerror("Error", "Search ID  Must be required")
        else:
            cursor.execute('Select * from diesel_consumption where id = %s',
                    (diesel_search_entry.get(),))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "This trans id is not exist")

            else:
               
                cursor.execute(
                                "UPDATE diesel_consumption SET  \
                            equipment_id = '" + equipmentID + "', \
                            withdrawal_slip = '" + withdrawalSlip + "', \
                            use_liter = '" + totalliter + "',\
                            price = '" + dieselRate + "',\
                            amount = '" + totalAmount + "', \
                            transaction_date = '" + diesel_date_update + "'\
                    WHERE id = %s",(diesel_search_entry.get(),))

                messagebox.showinfo('JRS','Data has been Updated')
                mydb.commit()
                mydb.close()
                cursor.close()
                diesel_registry_list()


    except Exception as ex:
        messagebox.showerror("Erro", f"Error due to :{str(ex)}")

    
    
    

def diesel_registry_search():
    """This function is for searching Diesel Registry tru Date Query"""
    mydb._open_connection()
    cursor = mydb.cursor()
    equipment_diesel_treeview.delete(*equipment_diesel_treeview.get_children())
    Date1 = diesel_sateSearchFrom.get()
    Date2 = diesel_sateSearchTo.get()

    cursor.execute("Select \
            `transaction_date`,\
            `equipment_id` ,\
            `withdrawal_slip`, \
            `use_liter`, \
            `price`,\
            `amount`,\
            `username` ,\
            `date_update`,\
            `id`\
            FROM  diesel_consumption\
            WHERE transaction_date BETWEEN '" + Date1 +"' AND '"+ Date2 + "' \
            ORDER by id DESC\
                ")

    fetch = cursor.fetchall()
    cnt = 0
    balance = 0
    for data in fetch:
        cnt += 1
        date1 = data[0]
        equip_id = data[1]

        useLiter = data[3]
        price = data[4]
        amount = data[5]
        balance = amount + balance
        userName_rental = data[6]
        dateUpdate = data[7]
        trans_id = data[8]
        amount2 = '{:,.2f}'.format(data[5])
        balance2 = '{:,.2f}'.format(balance)

        equipment_diesel_treeview.insert('', 'end', values=(
            cnt, trans_id, date1, equip_id, useLiter, price, amount2, balance2,
            userName_rental, dateUpdate))





def delete_diesel_registry():
    """This function is for searching data tru trans ID to each fields"""
    mydb._open_connection()
    cursor = mydb.cursor()


    try:
        if diesel_search_entry.get() == '':
            messagebox.showerror("Error", "Search ID  Must be required")
        else:
            cursor.execute('Select * from diesel_consumption where id = %s',
                    (diesel_search_entry.get(),))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "This trans_id is not exist")

            else:
                cursor.execute("""DELETE
                    FROM  diesel_consumption
                    WHERE id = %s""",(diesel_search_entry.get(),))

                messagebox.showinfo('JRS','Data has been deleted')
                mydb.commit()
                mydb.close()
                cursor.close()
                diesel_registry_list()


    except Exception as ex:
        messagebox.showerror("Erro", f"Error due to :{str(ex)}")

def calculate_diesel_comp(e):
    """This function is to calculate rental amount Fields """
    global amount_diesel
    total_liters = total_diesel_entry.get()

    if total_diesel_entry.get() == '':
        total_liters = 0
        amount_diesel = float(diesel_rate_entry.get()) * float(total_liters)
        amount = '{:,.2f}'.format(amount_diesel)

        diesel_amount_entry.delete(0, END)
        diesel_amount_entry.insert(0, (amount))
    else:
        total_liters = total_diesel_entry.get()
        amount_diesel = float(diesel_rate_entry.get()) * float(total_liters)
        amount = '{:,.2f}'.format(amount_diesel)

        diesel_amount_entry.delete(0, END)
        diesel_amount_entry.insert(0, (amount))
def diesel_registry_list():
    """This function is for Diesel registry Treeview List"""
    mydb._open_connection()
    cursor = mydb.cursor()
    equipment_diesel_treeview.delete(*equipment_diesel_treeview.get_children())
    cursor.execute("""
            Select 
            `transaction_date`, 
            `equipment_id` ,
            `withdrawal_slip`, 
            `use_liter`, 
            `price`,
            `amount`,
            `username` ,
            `date_update`,
            `id`
            FROM  diesel_consumption
            ORDER by id DESC
                """)

    fetch = cursor.fetchall()
    cnt = 0
    balance = 0
    for data in fetch:
        cnt += 1
        date1 = data[0]
        equip_id = data[1]

        useLiter = data[3]
        price = data[4]
        amount = data[5]
        balance = amount + balance
        userName_rental = data[6]
        dateUpdate = data[7]
        trans_id = data[8]
        amount2 = '{:,.2f}'.format(data[5])
        balance2 = '{:,.2f}'.format(balance)

        equipment_diesel_treeview.insert('', 'end', values=(
            cnt, trans_id, date1, equip_id, useLiter, price, amount2, balance2,
            userName_rental, dateUpdate))


def save_diesel_registry():
    """This function is for Saving Rental Transaction"""
    mydb._open_connection()
    cursor = mydb.cursor()
    user_name = userName_entry.get()

    try:
        if withdrawalslip_diesel_entry.get() == "" or diesel_equipmentID_entry_list.get() == ''\
                or total_diesel_entry.get() == "":
            messagebox.showerror("Error", "Entry field is  required")

        else:
            cursor.execute("INSERT INTO diesel_consumption (transaction_date,equipment_id,"
                           "withdrawal_slip,use_liter,price,"
                           "amount,username)"
                           
                           " VALUES(%s, %s, %s, %s, %s, %s, %s)",

                           (diesel_dateFrom.get(),diesel_equipmentID_entry_list.get(),
                            withdrawalslip_diesel_entry.get(),
                            total_diesel_entry.get(), diesel_rate_entry.get(),
                            amount_diesel, userName_entry.get()))

            messagebox.showinfo('JRS', 'Data has been Save')

            mydb.commit()
            mydb.close()
            cursor.close()
            diesel_registry_list()

            withdrawalslip_diesel_entry.delete(0, END)
            total_diesel_entry.delete(0, END)
            diesel_rate_entry.delete(0, END)
            diesel_amount_entry.delete(0, END)
            userName_entry.delete(0, END)



    except Exception as ex:
        messagebox.showerror("Erro", f"Error due to :{str(ex)}")


def diesel_registry():
    """This is for Diesel Registry Module"""
    clear_rentalModule()

    diesel_date_label1 = Label(equipmentModule_frame, text='Date', width=15, height=1, bg='yellow', fg='gray',
                               font=('Arial', 11), anchor='e')
    diesel_date_label1.place(x=10, y=15)

    global diesel_dateFrom
    diesel_dateFrom = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                foreground='white', borderwidth=2, padx=10, pady=10)
    diesel_dateFrom.place(x=160, y=15)
    diesel_dateFrom.configure(justify='center')

    diesel_equipment_lbl = Label(equipmentModule_frame, text='Equipment', width=15, height=1, bg='yellow', fg='gray',
                                 font=('Arial', 11), anchor='e')
    diesel_equipment_lbl.place(x=10, y=45)

    global diesel_equipmentID_entry_list
    diesel_equipmentID_entry_list = ttk.Combobox(equipmentModule_frame, width=17)
    diesel_equipmentID_entry_list['values'] = equipmentFields()
    diesel_equipmentID_entry_list.place(x=160, y=45)
    diesel_equipmentID_entry_list.bind("<<ComboboxSelected>>", calculate_diesel_comp)

    withdrawalslip_diesel_lbl = Label(equipmentModule_frame, text='Withdrawal Slip', width=15, height=1, bg='yellow',
                             fg='gray',
                             font=('Arial', 11), anchor='e')
    withdrawalslip_diesel_lbl.place(x=10, y=75)

    global withdrawalslip_diesel_entry
    withdrawalslip_diesel_entry = Entry(equipmentModule_frame, width=15, font=('Arial', 11), justify='right')
    withdrawalslip_diesel_entry.place(x=160, y=75)

    total_diesel_lbl = Label(equipmentModule_frame, text='liters Use', width=15, height=1, bg='yellow',
                             fg='gray',
                             font=('Arial', 11), anchor='e')
    total_diesel_lbl.place(x=10, y=105)

    global total_diesel_entry
    total_diesel_entry = Entry(equipmentModule_frame, width=15, font=('Arial', 11), justify='right')
    total_diesel_entry.place(x=160, y=105)

    diesel_rate_lbl = Label(equipmentModule_frame, text='Price', width=15, height=1, bg='yellow',
                            fg='gray',
                            font=('Arial', 11), anchor='e')
    diesel_rate_lbl.place(x=10, y=135)

    global diesel_rate_entry
    diesel_rate_entry = Entry(equipmentModule_frame, width=15, font=('Arial', 11), justify='right')
    diesel_rate_entry.place(x=160, y=135)

    diesel_amount_lbl = Label(equipmentModule_frame, text='Total Amount', width=15, height=1, bg='yellow',
                              fg='gray',
                              font=('Arial', 11), anchor='e')
    diesel_amount_lbl.place(x=10, y=165)

    global diesel_amount_entry
    diesel_amount_entry = Entry(equipmentModule_frame, width=15, font=('Arial', 11), justify='right')
    diesel_amount_entry.place(x=160, y=165)

    diesel_search_lbl = Label(equipmentModule_frame, text='Search', width=10, height=1, bg='yellow',
                              fg='gray',
                              font=('Arial', 10), anchor='e')
    diesel_search_lbl.place(x=10, y=245)

    global diesel_search_entry
    diesel_search_entry = Entry(equipmentModule_frame, width=10, font=('Arial', 11), justify='right')
    diesel_search_entry.place(x=100, y=245)

    diesel_sateSearchFrom_label = Label(equipmentModule_frame, text='Date From', width=10, height=1, bg='yellow',
                                        fg='gray',
                                        font=('Arial', 10), anchor='e')
    diesel_sateSearchFrom_label.place(x=300, y=15)
    global diesel_sateSearchFrom
    diesel_sateSearchFrom = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                      foreground='white', borderwidth=2, padx=10, pady=10)
    diesel_sateSearchFrom.place(x=400, y=15)
    diesel_sateSearchFrom.configure(justify='center')

    diesel_sateSearchto_label = Label(equipmentModule_frame, text='Date To', width=10, height=1, bg='yellow',
                                        fg='gray',
                                        font=('Arial', 10), anchor='e')
    diesel_sateSearchto_label.place(x=500, y=15)
    global diesel_sateSearchTo
    diesel_sateSearchTo = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
    diesel_sateSearchTo.place(x=600, y=15)
    diesel_sateSearchTo.configure(justify='center')

    global diesel_equipmentID_entry_list_search
    diesel_equipmentID_entry_list_search = ttk.Combobox(equipmentModule_frame, width=17)
    diesel_equipmentID_entry_list_search['values'] = equipmentFields()
    diesel_equipmentID_entry_list_search.place(x=735, y=15)


# this is for Button for diesel registry
    btn_diesel_save = Button(equipmentModule_frame, text='Save', bd=2, bg='gray', fg='yellow',
                             font=('arial', 10), width=10, height=1, command=save_diesel_registry)
    btn_diesel_save.place(x=10, y=195)
    btn_diesel_save.bind('<Return>', save_diesel_registry)

    btn_diesel_delete = Button(equipmentModule_frame, text='Delete', bd=2, bg='red', fg='white',
                               font=('arial', 10), width=10, height=1, command=delete_diesel_registry)
    btn_diesel_delete.place(x=200, y=245)
    btn_diesel_delete.bind('<Return>', delete_diesel_registry)
    
    btn_diesel_update = Button(equipmentModule_frame, text='Update', bd=2, bg='red', fg='white',
                               font=('arial', 10), width=10, height=1, command=update_diesel_registry)
    btn_diesel_update.place(x=200, y=295)
    btn_diesel_update.bind('<Return>', update_diesel_registry)

    btn_diesel_search = Button(equipmentModule_frame, text='Search', bd=2, bg='green', fg='white',
                               font=('arial', 10), width=10, height=1, command=diesel_registry_search)
    btn_diesel_search.place(x=870, y=15)
    btn_diesel_search.bind('<Return>', diesel_registry_search)

    btn_diesel_search_with_eqID = Button(equipmentModule_frame, text='Search with ID', bd=2, bg='green', fg='white',
                               font=('arial', 10), width=15, height=1, command=diesel_registry_search_with_equipID)
    btn_diesel_search_with_eqID.place(x=970, y=15)
    btn_diesel_search_with_eqID.bind('<Return>', diesel_registry_search_with_equipID)

    # this is for Tree View for Rental Equipment
    MidViewForm23 = Frame(equipmentModule_frame, width=500, height=450)
    MidViewForm23.place(x=300, y=50)

    style = ttk.Style(equipmentModule_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="yellow")
    # change selected color

    # style.map('Treeview',
    #             background[('selected','green')])

    scrollbarx = Scrollbar(MidViewForm23, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm23, orient=VERTICAL)
    global equipment_diesel_treeview
    equipment_diesel_treeview = ttk.Treeview(MidViewForm23,
                                             columns=("CNT", "Trans ID", "DATE", "Equipment ID",
                                                      "RENTAL HOUR", "Rental Rate", "Amount",
                                                      "Balance", "UserName", "DateUpdate"),
                                             selectmode="extended", height=21, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=equipment_diesel_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=equipment_diesel_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    equipment_diesel_treeview.heading('CNT', text="No.", anchor=CENTER)
    equipment_diesel_treeview.heading('Trans ID', text="Trans ID", anchor=CENTER)
    equipment_diesel_treeview.heading('DATE', text="Date", anchor=CENTER)

    equipment_diesel_treeview.heading('Equipment ID', text="Equipment ID", anchor=CENTER)
    equipment_diesel_treeview.heading('RENTAL HOUR', text="Liters", anchor=CENTER)
    equipment_diesel_treeview.heading('Rental Rate', text="Price", anchor=CENTER)
    equipment_diesel_treeview.heading('Amount', text="Amount", anchor=CENTER)
    equipment_diesel_treeview.heading('Balance', text="Balance", anchor=CENTER)
    equipment_diesel_treeview.heading('UserName', text="User", anchor=CENTER)
    equipment_diesel_treeview.heading('DateUpdate', text="Update", anchor=CENTER)

    equipment_diesel_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    equipment_diesel_treeview.column('#1', stretch=NO, minwidth=0, width=30, anchor='e')
    equipment_diesel_treeview.column('#2', stretch=NO, minwidth=0, width=50, anchor='e')
    equipment_diesel_treeview.column('#3', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_diesel_treeview.column('#4', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_diesel_treeview.column('#5', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_diesel_treeview.column('#6', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_diesel_treeview.column('#7', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_diesel_treeview.column('#8', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_diesel_treeview.column('#9', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_diesel_treeview.column('#10', stretch=NO, minwidth=0, width=90, anchor='e')

    equipment_diesel_treeview.pack()


#===========================================Liters Per Hour=============================================================
def total_liters_per_equipment():
    """
    This function is for
    selecting total diesel
    per equipment
    """
    mydb._open_connection()
    cursor = mydb.cursor()
    liter_per_hour_treeview.delete(*liter_per_hour_treeview.get_children())
    date1 = ltrHrs_sateSearchFrom.get()
    date2 = ltrHrs_sateSearchTo.get()


    query2 = "Select\
                equipment_id,\
                sum(use_liter) as diesel\
                from diesel_consumption\
                where transaction_date\
                BETWEEN '" + date1 + "' and\
                '" + date2 + "'  \
                GROUP BY equipment_id \
            "
    cursor.execute(query2)
    myresult = cursor.fetchall()

    for i in myresult:
        eqp_id = i[0]
        totalDiesel = i[1]

        totalliters2 = '{:,.2f}'.format(totalDiesel)
        totalhours2 = 0
        liters_per_hour2 = 0

        liter_per_hour_treeview.insert('', 'end', values=(
                    eqp_id, totalliters2, totalhours2,
                    liters_per_hour2))

    # query = "Select\
    #             equipment_id,\
    #             sum(total_rental_hour) as TotalRental\
    #             from equipment_rental\
    #             where transaction_date\
    #             BETWEEN '" + date1 + "' and\
    #             '" + date2 + "' \
    #             GROUP BY equipment_id \
    #             "
    # cursor.execute(query)
    # myresult = cursor.fetchall()

    # for j in myresult:



def liter_per_hour_listview():
    """This function is to appear data for ltrs/hour in treeview """
    mydb._open_connection()
    cursor = mydb.cursor()
    liter_per_hour_treeview.delete(*liter_per_hour_treeview.get_children())
    date1 = ltrHrs_sateSearchFrom.get()
    date2 = ltrHrs_sateSearchTo.get()


    query = "Select\
                equipment_id,\
                sum(total_rental_hour) as TotalRental\
                from equipment_rental\
                where transaction_date\
                BETWEEN '" + date1 + "' and\
                '" + date2 + "' \
                GROUP BY equipment_id \
                "
    cursor.execute(query)
    myresult = cursor.fetchall()

    transDate = ''
    equipID = ''
    rental_hour = 0
    totalrow = 0

    rental_report = {}
    for i in myresult:
        data = {i[0]:
                    {'totalHours': i[1]
                     }
                }

        rental_report.update(data)

    for j in rental_report:
        equipmID = j
        total = rental_report[j]['totalHours']

        query2 = "Select\
                    equipment_id,\
                    sum(use_liter) as diesel\
                    from diesel_consumption\
                    where transaction_date\
                    BETWEEN '" + date1 + "' and\
                    '" + date2 + "'  \
                    GROUP BY equipment_id \
                "
        cursor.execute(query2)
        myresult = cursor.fetchall()

        diesel_report = {}
        for h in myresult:
            data2 = {h[0]:
                         {'totalliters': h[1]
                          }
                     }
            diesel_report.update(data2)

        totalliters = 0
        totalliters2 = 0
        totalhours2 = 0
        for k in diesel_report:

            if k == j:
                liters_per_hour = diesel_report[k]['totalliters'] / rental_report[j]['totalHours']
                liters_per_hour2 = '{:,.2f}'.format(liters_per_hour)
                # print(f'Liters/Hour: {liters_per_hour2}')
                totalliters =diesel_report[k]['totalliters']
                totalliters2 = '{:,.2f}'.format(totalliters)

                totalhours= rental_report[j]['totalHours']
                totalhours2 = '{:,.2f}'.format(totalhours)

                liter_per_hour_treeview.insert('', 'end', values=(
                    k, totalliters2, totalhours2,
                    liters_per_hour2))

                

           

def liter_per_hour_module():
    """This function is for computation of liter per Hour"""
    clear_rentalModule()
    ltrHrs_sateSearchFrom_label = Label(equipmentModule_frame, text='Date From', width=10, height=1, bg='yellow',
                                        fg='gray',
                                        font=('Arial', 10), anchor='e')
    ltrHrs_sateSearchFrom_label .place(x=300, y=15)
    global ltrHrs_sateSearchFrom
    ltrHrs_sateSearchFrom = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                      foreground='white', borderwidth=2, padx=10, pady=10)
    ltrHrs_sateSearchFrom.place(x=400, y=15)
    ltrHrs_sateSearchFrom.configure(justify='center')

    ltrHrs_sateSearchTO_label = Label(equipmentModule_frame, text='Date To', width=10, height=1, bg='yellow',
                                        fg='gray',
                                        font=('Arial', 10), anchor='e')
    ltrHrs_sateSearchTO_label.place(x=550, y=15)
    global ltrHrs_sateSearchTo
    ltrHrs_sateSearchTo = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
    ltrHrs_sateSearchTo.place(x=650, y=15)
    ltrHrs_sateSearchTo.configure(justify='center')

    btn_perHour_search = Button(equipmentModule_frame, text='Search', bd=2, bg='green', fg='white',
                               font=('arial', 10), width=10, height=1, command=liter_per_hour_listview)
    btn_perHour_search.place(x=750, y=15)
    btn_perHour_search.bind('<Return>', liter_per_hour_listview)

    btn_totalDiesel = Button(equipmentModule_frame, text='Total Diesel', bd=2, bg='gray', fg='yellow',
                            font=('arial', 10), width=14, height=1, command=total_liters_per_equipment)
    btn_totalDiesel.place(x=870, y=15)

    # this is for Tree View for Rental Equipment
    MidViewForm21 = Frame(equipmentModule_frame, width=500, height=450)
    MidViewForm21.place(x=250, y=50)

    style = ttk.Style(equipmentModule_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="yellow")
    # change selected color

    # style.map('Treeview',
    #             background[('selected','green')])

    scrollbarx = Scrollbar(MidViewForm21, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm21, orient=VERTICAL)
    global liter_per_hour_treeview
    liter_per_hour_treeview = ttk.Treeview(MidViewForm21,
                                             columns=("EQUIPMENTID", "TOTALLTRS", "TOTALHRS", "LTRS/HRS"),
                                             selectmode="extended", height=21, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=liter_per_hour_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=liter_per_hour_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    liter_per_hour_treeview.heading('EQUIPMENTID', text="EQUIPMENT ID", anchor=CENTER)
    liter_per_hour_treeview.heading('TOTALLTRS', text="TOTAL LITERS", anchor=CENTER)
    liter_per_hour_treeview.heading('TOTALHRS', text="TOTAL HOURS", anchor=CENTER)
    liter_per_hour_treeview.heading('LTRS/HRS', text="LITERS/HOURS", anchor=CENTER)


    liter_per_hour_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    liter_per_hour_treeview.column('#1', stretch=NO, minwidth=0, width=150, anchor='e')
    liter_per_hour_treeview.column('#2', stretch=NO, minwidth=0, width=150, anchor='e')
    liter_per_hour_treeview.column('#3', stretch=NO, minwidth=0, width=150, anchor='e')
    liter_per_hour_treeview.column('#4', stretch=NO, minwidth=0, width=150, anchor='e')


    liter_per_hour_treeview.pack()

    #show_rental_list()


#===========================================Rental Registry MOdule======================================================
def rental_list_dateSearch_with_equipID():
    """This function is to search with date and equipment ID parameter"""

    mydb._open_connection()
    cursor = mydb.cursor()
    equipment_rental_treeview.delete(*equipment_rental_treeview.get_children())
    Date1 = rental_sateSearchFrom.get()
    Date2 =rental_sateSearchTo.get()
    equipID = rental_with_equipmentID_search.get()
    cursor.execute("Select \
                `transaction_date`, \
                `equipment_id` , \
                `total_rental_hour`, \
                `rental_rate`, \
                `rental_amount` ,\
                `username` ,\
                `date_update`,\
                `id`\
                FROM  equipment_rental\
                WHERE transaction_date BETWEEN '" + Date1 +"' AND '"+ Date2 + "'\
                AND equipment_id = '"+ equipID + "' \
                ORDER by id ASC \
                    ")

    fetch = cursor.fetchall()
    cnt = 0
    balance = 0
    for data in fetch:
        cnt += 1
        date1 = data[0]
        equip_id = data[1]
        rentalHour = data[2]
        rentalRate = data[3]
        amount = data[4]
        balance = amount + balance
        userName_rental = data[5]
        dateUpdate = data[6]
        trans_id = data[7]
        amount2 = '{:,.2f}'.format(data[4])
        balance2 = '{:,.2f}'.format(balance)

        equipment_rental_treeview.insert('', 'end', values=(
            cnt, trans_id, date1, equip_id, rentalHour, rentalRate, amount2, balance2,
            userName_rental, dateUpdate))


def rental_list_dateSearch():
    """This function is to search with date parameter"""

    mydb._open_connection()
    cursor = mydb.cursor()
    equipment_rental_treeview.delete(*equipment_rental_treeview.get_children())
    Date1 = rental_sateSearchFrom.get()
    Date2 =rental_sateSearchTo.get()
    cursor.execute("Select \
                `transaction_date`, \
                `equipment_id` , \
                `total_rental_hour`, \
                `rental_rate`, \
                `rental_amount` ,\
                `username` ,\
                `date_update`,\
                `id`\
                FROM  equipment_rental\
                WHERE transaction_date BETWEEN '" + Date1 +"' AND '"+ Date2 + "'\
                ORDER by id ASC \
                    ")

    fetch = cursor.fetchall()
    cnt = 0
    balance = 0
    for data in fetch:
        cnt += 1
        date1 = data[0]
        equip_id = data[1]
        rentalHour = data[2]
        rentalRate = data[3]
        amount = data[4]
        balance = amount + balance
        userName_rental = data[5]
        dateUpdate = data[6]
        trans_id = data[7]
        amount2 = '{:,.2f}'.format(data[4])
        balance2 = '{:,.2f}'.format(balance)

        equipment_rental_treeview.insert('', 'end', values=(
            cnt, trans_id, date1, equip_id, rentalHour, rentalRate, amount2, balance2,
            userName_rental, dateUpdate))


def delete_rental():
    """This function is for searching data tru trans ID to each fields"""
    mydb._open_connection()
    cursor = mydb.cursor()


    try:
        if rental_search_entry.get() == '' :
            messagebox.showerror("Error", "Search ID  Must be required")
        else:
            cursor.execute('Select * from equipment_rental WHERE id = %s',
                           (rental_search_entry.get(),))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "This trans_id is not exist")

            else:
                cursor.execute("""DELETE
                    FROM  equipment_rental
                    WHERE id = %s""",(rental_search_entry.get(),))

                messagebox.showinfo('JRS','Data has been deleted')
                mydb.commit()
                mydb.close()
                cursor.close()
                show_rental_list()


    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")

def show_rental_list():
    equipment_rental_treeview.delete(*equipment_rental_treeview.get_children())
    rental_list()
def rental_list():
    """This function is for Rental Treeview List"""
    mydb._open_connection()
    cursor = mydb.cursor()
    cursor.execute("""
            Select 
            `transaction_date`, 
            `equipment_id` ,
            `total_rental_hour`, 
            `rental_rate`, 
            `rental_amount` ,
            `username` ,
            `date_update`,
            `id`
            FROM  equipment_rental
            ORDER by id DESC
                """)

    fetch = cursor.fetchall()
    cnt = 0
    balance = 0
    for data in fetch:
        cnt += 1
        date1 = data[0]
        equip_id = data[1]
        rentalHour = data[2]
        rentalRate = data[3]
        amount = data[4]
        balance = amount + balance
        userName_rental = data[5]
        dateUpdate = data[6]
        trans_id = data[7]
        amount2 = '{:,.2f}'.format(data[4])
        balance2 = '{:,.2f}'.format(balance)

        equipment_rental_treeview.insert('', 'end', values=(
            cnt, trans_id, date1, equip_id, rentalHour, rentalRate, amount2, balance2,
            userName_rental, dateUpdate))

def save_rental():
    """This function is for Saving Rental Transaction"""
    mydb._open_connection()
    cursor = mydb.cursor()
    user_name = userName_entry.get()



    try:
        if rental_equipmentID_entry_search.get() == "" or total_rental_entry.get() == '':
            messagebox.showerror("Error", "Equipment ID and Total Rental Hours Must be required")

        else:
            cursor.execute("INSERT INTO equipment_rental (transaction_date,equipment_id,"
                           "total_rental_hour,rental_rate,"
                           "rental_amount,username)"

                           " VALUES(%s, %s, %s, %s, %s, %s)",

                           (rental_dateFrom.get(),rental_equipmentID_entry_search.get(),
                            total_rental_entry.get(), rental_rate_entry.get(),
                            amount_rental, userName_entry.get()))

            messagebox.showinfo('JRS', 'Data has been Save')

            mydb.commit()
            mydb.close()
            cursor.close()
            show_rental_list()


    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")


def calculate_rental():
    """This function is to calculate rental amount Fields """
    global amount_rental
    total_rentalhours = total_rental_entry.get()

    if total_rental_entry.get() == '':
        total_rentalhours = 0
        amount_rental = float(rental_rate_entry.get()) * float(total_rentalhours)
        amount = '{:,.2f}'.format(amount_rental)

        rental_amount_entry.delete(0, END)
        rental_amount_entry.insert(0, (amount))
    else:
        total_rentalhours = total_rental_entry.get()
        amount_rental = float(rental_rate_entry.get()) * float(total_rentalhours)
        amount = '{:,.2f}'.format(amount_rental)

        rental_amount_entry.delete(0, END)
        rental_amount_entry.insert(0, (amount))


def automatic_rental_rate(event):
    """This function is for automatic rental rate """
    mydb._open_connection()
    cursor = mydb.cursor()


    cursor.execute("SELECT equipment_id, rental_rate\
                             FROM `equipment_details`\
                             WHERE  equipment_id = %s",
                   (rental_equipmentID_entry_search.get(),))

    myresult2 = cursor.fetchall()

    for row in myresult2:
        equipmentID = row[0]
        rental_rate = row[1]

        try:
            if rental_equipmentID_entry_search.get() == equipmentID:
                rental_rate_entry.delete(0, END)
                rental_rate_entry.insert(0, (rental_rate))
                calculate_rental()
            else:

                messagebox.showerror("Error", "No Record found ")

        except Exception as ex:

            messagebox.showerror("Error", f"Error due to :{str(ex)}")




def rental_registry():
    """This is for Rental Registry"""
    clear_rentalModule()

    rental_date_label1 = Label(equipmentModule_frame, text='Date', width=15, height=1, bg='yellow', fg='gray',
                           font=('Arial', 11), anchor='e')
    rental_date_label1.place(x=10, y=15)

    global rental_dateFrom
    rental_dateFrom = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                            foreground='white', borderwidth=2, padx=10, pady=10)
    rental_dateFrom.place(x=160, y=15)
    rental_dateFrom.configure(justify='center')

    rental_equipment_lbl = Label(equipmentModule_frame, text='Equipment', width=15, height=1, bg='yellow', fg='gray',
                               font=('Arial', 11), anchor='e')
    rental_equipment_lbl.place(x=10, y=45)

    global rental_equipmentID_entry_search
    rental_equipmentID_entry_search = ttk.Combobox(equipmentModule_frame, width=17)
    rental_equipmentID_entry_search['values'] = equipmentFields()
    rental_equipmentID_entry_search.place(x=160, y=45)
    rental_equipmentID_entry_search.bind("<<ComboboxSelected>>", automatic_rental_rate)

    total_rental_lbl = Label(equipmentModule_frame, text='Total Rental Hours', width=15, height=1, bg='yellow', fg='gray',
                                 font=('Arial', 11), anchor='e')
    total_rental_lbl.place(x=10, y=75)

    global total_rental_entry
    total_rental_entry = Entry(equipmentModule_frame, width=15, font=('Arial', 11), justify='right')
    total_rental_entry.place(x=160, y=75)

    rental_rate_lbl = Label(equipmentModule_frame, text='Rental Rate', width=15, height=1, bg='yellow',
                             fg='gray',
                             font=('Arial', 11), anchor='e')
    rental_rate_lbl.place(x=10, y=105)

    global rental_rate_entry
    rental_rate_entry = Entry(equipmentModule_frame, width=15, font=('Arial', 11), justify='right')
    rental_rate_entry.place(x=160, y=105)

    rental_amount_lbl = Label(equipmentModule_frame, text='Rental Amount', width=15, height=1, bg='yellow',
                            fg='gray',
                            font=('Arial', 11), anchor='e')
    rental_amount_lbl.place(x=10, y=135)

    global rental_amount_entry
    rental_amount_entry = Entry(equipmentModule_frame, width=15, font=('Arial', 11), justify='right')
    rental_amount_entry.place(x=160, y=135)

    rental_search_lbl = Label(equipmentModule_frame, text='Search', width=10, height=1, bg='yellow',
                              fg='gray',
                              font=('Arial', 10), anchor='e')
    rental_search_lbl.place(x=10, y=215)

    global rental_search_entry
    rental_search_entry = Entry(equipmentModule_frame, width=10, font=('Arial', 11), justify='right')
    rental_search_entry.place(x=100, y=215)

    rental_sateSearchFrom_label = Label(equipmentModule_frame, text='Date From', width=10, height=1, bg='yellow', fg='gray',
                               font=('Arial', 10), anchor='e')
    rental_sateSearchFrom_label.place(x=300, y=15)
    global rental_sateSearchFrom
    rental_sateSearchFrom = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                foreground='white', borderwidth=2, padx=10, pady=10)
    rental_sateSearchFrom.place(x=400, y=15)
    rental_sateSearchFrom.configure(justify='center')

    rental_sateSearchFrom_label = Label(equipmentModule_frame, text='Date To', width=10, height=1, bg='yellow',
                                        fg='gray',
                                        font=('Arial', 10), anchor='e')
    rental_sateSearchFrom_label.place(x=500, y=15)

    global rental_with_equipmentID_search
    rental_with_equipmentID_search = ttk.Combobox(equipmentModule_frame, width=17)
    rental_with_equipmentID_search['values'] = equipmentFields()
    rental_with_equipmentID_search.place(x=710, y=15)


    global rental_sateSearchTo
    rental_sateSearchTo = DateEntry(equipmentModule_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                      foreground='white', borderwidth=2, padx=10, pady=10)
    rental_sateSearchTo.place(x=600, y=15)
    rental_sateSearchTo.configure(justify='center')

    rental_equipment_lbl = Label(equipmentModule_frame, text='Equipment', width=15, height=1, bg='yellow', fg='gray',
                                 font=('Arial', 11), anchor='e')
    rental_equipment_lbl.place(x=10, y=45)

    btn_rental_save = Button(equipmentModule_frame, text='Save', bd=2, bg='gray', fg='yellow',
                              font=('arial', 10), width=10, height=1, command=save_rental)
    btn_rental_save.place(x=10, y=175)
    btn_rental_save.bind('<Return>', save_rental)

    btn_rental_delete = Button(equipmentModule_frame, text='Delete', bd=2, bg='red', fg='white',
                             font=('arial', 10), width=10, height=1, command=delete_rental)
    btn_rental_delete.place(x=200, y=215)
    btn_rental_delete.bind('<Return>', delete_rental)

    btn_rental_search = Button(equipmentModule_frame, text='Search', bd=2, bg='green', fg='white',
                               font=('arial', 10), width=10, height=1,command = rental_list_dateSearch)
    btn_rental_search.place(x=850, y=15)
    btn_rental_search.bind('<Return>',rental_list_dateSearch)

    btn_rental_search_with_equipID = Button(equipmentModule_frame, text='Search with Equip', bd=2, bg='green', fg='white',
                               font=('arial', 10), width=15, height=1, command=rental_list_dateSearch_with_equipID)
    btn_rental_search_with_equipID.place(x=950, y=15)
    btn_rental_search_with_equipID.bind('<Return>', rental_list_dateSearch_with_equipID)

# this is for Tree View for Rental Equipment
    MidViewForm20 = Frame(equipmentModule_frame, width=500, height=450)
    MidViewForm20.place(x=300, y=50)

    style = ttk.Style(equipmentModule_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="yellow")
    # change selected color

    # style.map('Treeview',
    #             background[('selected','green')])

    scrollbarx = Scrollbar(MidViewForm20, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm20, orient=VERTICAL)
    global equipment_rental_treeview
    equipment_rental_treeview = ttk.Treeview(MidViewForm20,
                                          columns=("CNT", "Trans ID", "DATE", "Equipment ID",
                                                   "RENTAL HOUR", "Rental Rate", "Amount",
                                                   "Balance","UserName","DateUpdate"),
                                          selectmode="extended", height=21, yscrollcommand=scrollbary.set,
                                          xscrollcommand=scrollbarx.set)
    scrollbary.config(command=equipment_rental_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=equipment_rental_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    equipment_rental_treeview.heading('CNT', text="No.", anchor=CENTER)
    equipment_rental_treeview.heading('Trans ID', text="Trans ID", anchor=CENTER)
    equipment_rental_treeview.heading('DATE', text="Date", anchor=CENTER)

    equipment_rental_treeview.heading('Equipment ID', text="Equipment ID", anchor=CENTER)
    equipment_rental_treeview.heading('RENTAL HOUR', text="Rental Hour", anchor=CENTER)
    equipment_rental_treeview.heading('Rental Rate', text="Rental Rate", anchor=CENTER)
    equipment_rental_treeview.heading('Amount', text="Amount", anchor=CENTER)
    equipment_rental_treeview.heading('Balance', text="Balance", anchor=CENTER)
    equipment_rental_treeview.heading('UserName', text="User", anchor=CENTER)
    equipment_rental_treeview.heading('DateUpdate', text="Update", anchor=CENTER)

    equipment_rental_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    equipment_rental_treeview.column('#1', stretch=NO, minwidth=0, width=30, anchor='e')
    equipment_rental_treeview.column('#2', stretch=NO, minwidth=0, width=50, anchor='e')
    equipment_rental_treeview.column('#3', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_rental_treeview.column('#4', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_rental_treeview.column('#5', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_rental_treeview.column('#6', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_rental_treeview.column('#7', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_rental_treeview.column('#8', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_rental_treeview.column('#9', stretch=NO, minwidth=0, width=90, anchor='e')
    equipment_rental_treeview.column('#10', stretch=NO, minwidth=0, width=90, anchor='e')

    equipment_rental_treeview.pack()

    show_rental_list()



def equipment_module():
    """This function is for Equipment Module"""

    clearFrame()
    global equipmentModule_frame
    # global logo_icon3
    # load3 = Image.open("image\partsregistry.png")
    # load3 = load3.resize((130, 70), Image.ANTIALIAS)
    # logo_icon3 = ImageTk.PhotoImage(load3)

    equipmentModule_frame = Frame(MidViewForm9, width=1120, height=575, bd=2, bg='gray', relief=SOLID)
    equipmentModule_frame.place(x=160, y=8)

    btn_rental_Registry = Button(MidViewForm9, text='Rental Registry', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command= rental_registry)
    btn_rental_Registry.place(x=2, y=70)
    btn_rental_Registry.bind('<Return>',rental_registry )

    btn_diesel_registry = Button(MidViewForm9, text='Diesel Withdrawal', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command=diesel_registry)
    btn_diesel_registry.place(x=2, y=120)
    btn_diesel_registry.bind('<Return>', diesel_registry)

    btn_liters_per_hour = Button(MidViewForm9, text='Liters/Hour', bd=2, bg='blue', fg='white',
                                 font=('arial', 12), width=15, height=2, command=liter_per_hour_module)
    btn_liters_per_hour.place(x=2, y=170)
    btn_liters_per_hour.bind('<Return>', liter_per_hour_module)

    btn_expenses_per_equipment = Button(MidViewForm9, text='Expense Entry', bd=2, bg='blue', fg='white',
                                 font=('arial', 12), width=15, height=2, command=cost_entry)
    btn_expenses_per_equipment.place(x=2, y=220)
    btn_expenses_per_equipment.bind('<Return>', cost_entry)

    btn_cost_per_equipment = Button(MidViewForm9, text='Cost per Equipment', bd=2, bg='blue', fg='white',
                                 font=('arial', 12), width=15, height=2, command=cost_per_equipment_frame)
    btn_cost_per_equipment.place(x=2, y=270)
    btn_cost_per_equipment.bind('<Return>', cost_per_equipment_frame)

#==============================================Parts Withdrawal=========================================================
def search_with_per_equipment():
    """This function is for searching tru date"""

    mydb._open_connection()
    cursor = mydb.cursor()
    date1 = dr_dateFrom.get()
    date2 = dr_dateto.get()
    equipmet_ID = dr_equipmentID_entry_search.get()
    tree_aging_report_with.delete(*tree_aging_report_with.get_children())
    cursor.execute("SELECT date_transact,id,equipment_id,inventory_id,\
           quantity_with,amount_with\
           FROM `parts` WHERE date_transact BETWEEN '" + date1 + "' AND '" + date2 + "' \
           AND equipment_id ='" + equipmet_ID + "' AND amount_with >0\
           ORDER BY id")
    fetch = cursor.fetchall()
    cnt = 0
    for data in fetch:
        cnt += 1
        id_num = data[1]
        date1 = data[0]
        equip_id = data[2]
        inv_id = data[3]
        quantity = '{:,.2f}'.format(data[4])
        amount = '{:,.2f}'.format(data[5])

        tree_aging_report_with.insert('', 'end', values=(
            cnt, date1, id_num, equip_id, inv_id,
            quantity, amount))


def parts_widthrawal_treeView():
    """This function is to display data in Treeview"""
    mydb._open_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id,equipment_id,inventory_id,\
           quantity_with,amount_with,date_transact\
           FROM `parts` WHERE amount_with >0\
           ORDER BY id")
    fetch = cursor.fetchall()
    cnt = 0
    for data in fetch:
        cnt += 1
        id_num = data[0]
        equip_id = data[1]
        inv_id = data[2]
        quantity = '{:,.2f}'.format(data[3])
        amount = '{:,.2f}'.format(data[4])
        date1 = data[5]

        tree_aging_report_with.insert('', 'end', values=(
            cnt, date1, id_num, equip_id, inv_id,
            quantity, amount))


def print_withrawal():
    """This function is to print Parts widthrawal"""

    mydb._open_connection()
    cursor = mydb.cursor()
    user_reg = userName_entry.get()
    date1 = dr_dateFrom.get()
    date2 = dr_dateto.get()
    equipmet_ID = dr_equipmentID_entry_search.get()
    cursor.execute("SELECT equipment_id,\
           SUM(quantity_with) As TotalQuantity, SUM(amount_with) as TotalAmount\
           FROM `parts` WHERE date_transact BETWEEN '" + date1 + "' AND '" + date2 + "' \
           AND amount_with >0 \
           GROUP BY equipment_id ")

    myresult = cursor.fetchall()
    result = []

    cnt = 0
    for row in myresult:
        cnt+=1
        data = {'count': cnt,
                'equipmentID': row[0],
                'total_quantity': row[1],
                'total_amount': row[2],

                'total_quantity2': '{:,.2f}'.format(row[1]),
                'total_amount2': '{:,.2f}'.format(row[2])
                }

        result.append(data)

        #     gross_payT = '{:,.2f}'.format(row[0])
        #     net_payt = '{:,.2f}'.format(row[1])

        rpt = Report(result)
        rpt.detailband = Band([
            Element((30, 0), ("Helvetica", 8), key='count', align="right"),
            Element((65, 0), ("Helvetica", 8), key='equipmentID', align="right"),
            Element((130, 0), ("Helvetica", 8), key='total_quantity', align="right"),
            Element((210, 0), ("Helvetica", 8), key='total_amount', align="right"),


            # Rule((36, 0), 11.5 * 72, thickness=.2)

        ])

        rpt.pageheader = Band([
            Element((30, 0), ("Times-Bold", 13),
                    text="LD Widthrawal"),
            Element((170, 0), ("Times-Bold", 13),
                    text='Date From:'),
            Element((250, 0), ("Times-Bold", 13),
                    text=date1),
            Element((325, 0), ("Times-Bold", 13),
                    text=' to'),
            Element((350, 0), ("Times-Bold", 13),
                    text=date2),
            Element((30, 24), ("Helvetica", 10),
                    text="Equipment ID"),
            Element((150, 24), ("Helvetica", 10),
                    text="Total Quantity", align="right"),
            Element((210, 24), ("Helvetica", 10),
                    text="Total Amount", align="right"),


            Rule((36, 42), 11.5 * 40, thickness=2),
        ])
        rpt.reportfooter = Band([
            Rule((36, 4), 11.5 * 40),
            Element((36, 4), ("Helvetica-Bold", 12),
                    text="Grand Total"),

            SumElement((130, 4), ("Helvetica-Bold", 9),
                       key="total_quantity", align="right"),
            SumElement((210, 4), ("Helvetica-Bold", 9),
                       key="total_amount", align="right"),

            Element((40, 30), ("Helvetica", 10),
                    text="Prepared  BY:"),
            Element((80, 60), ("Helvetica", 10),
                    text=user_reg),
            Element((300, 30), ("Helvetica", 10),
                    text="Check  BY:"),
            Element((344, 60), ("Helvetica", 10),
                    text='JEROME R. SABUSIDO'),

        ])
        # canvas = Canvas("payroll.pdf") for short bond paper configuration
        canvas = Canvas("partswidthrawal.pdf")
        rpt.generate(canvas)
        canvas.save()

    startfile("partswidthrawal.pdf")


def search_product_widthrawal():
    """This function is to display data true search button """
    tree_aging_report_with.delete(*tree_aging_report_with.get_children())
    search_widthrawal_treeView()
def search_widthrawal_treeView():
    """This function is for searching tru date"""
    mydb._open_connection()
    cursor = mydb.cursor()
    date1 = dr_dateFrom.get()
    date2 = dr_dateto.get()
    equipmet_ID = dr_equipmentID_entry_search.get()
    cursor.execute("SELECT date_transact,id,equipment_id,inventory_id,\
       quantity_with,amount_with\
       FROM `parts` WHERE date_transact BETWEEN '" + date1 + "' AND '" + date2 + "' \
       AND amount_with >0\
       ORDER BY id")
    fetch = cursor.fetchall()
    cnt = 0
    for data in fetch:
        cnt += 1
        id_num = data[1]
        date1 = data[0]
        equip_id = data[2]
        inv_id = data[3]
        quantity = '{:,.2f}'.format(data[4])
        amount = '{:,.2f}'.format(data[5])


        tree_aging_report_with.insert('', 'end', values=(
                                    cnt, date1, id_num,  equip_id, inv_id,
                                    quantity, amount))
def parts_widthrawal_treeView():
    """This function is to display data in Treeview"""
    mydb._open_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id,equipment_id,inventory_id,\
       quantity_with,amount_with,date_transact\
       FROM `parts` WHERE amount_with >0\
       ORDER BY id")
    fetch = cursor.fetchall()
    cnt = 0
    for data in fetch:
        cnt += 1
        id_num = data[0]
        equip_id = data[1]
        inv_id = data[2]
        quantity = '{:,.2f}'.format(data[3])
        amount = '{:,.2f}'.format(data[4])
        date1 = data[5]

        tree_aging_report_with.insert('', 'end', values=(
                                    cnt, date1, id_num, equip_id, inv_id,
                                    quantity, amount))

def insert_widthrawal():
    """This function is for saving widthrawal"""
    ts = time.time()
    mydb._open_connection()

    amount_dr = float(dr_qty_entry_with.get()) * float(dr_unit_price_entry_with.get())

    date1 = partwidth_date_with.get()
    equipment_id_with = dr_equipmentID_entry.get()
    desc_reg = dr_description_entry_with.get('1.0', 'end-1c')
    brand_reg = dr_brand_entry_with.get()
    classfin = dr_clasfn_entry_with.get()
    location_reg = dr_location_entry_with.get()
    quantity_reg = dr_qty_entry_with.get()
    unit_rg = dr_unit_entry_with.get()
    unitPrice_reg = dr_unit_price_entry_with.get()
    amount_reg = amount_dr

    receiver_reg = dr_receiver_entry_with.get()
    remarks_reg = dr_remarks_with.get('1.0', 'end-1c')
    user_reg = userName_entry.get()
    date_time_update = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    inventoryID = dr_itemsID.get()

    if equipment_id_with == '' :
        messagebox.showinfo('JRS', 'Equipment ID Fields is Empty Please fill up!!!')

    else:
        cursor.execute(
            "INSERT INTO parts (equipment_id,inventory_id,"
            "date_transact,description,brand,classification,location,"
            "unit,unit_price,quantity_with,amount_with,receiver,remarks,users,date_update)"
            " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            ( equipment_id_with,inventoryID,
              date1, desc_reg, brand_reg, classfin, location_reg,
              unit_rg, unitPrice_reg, quantity_reg, amount_reg,
             receiver_reg, remarks_reg, user_reg, date_time_update))

        mydb.commit()
        mydb.close()
        cursor.close()

        messagebox.showinfo('JRS', 'Data has been Save')
        tree_aging_report_with.delete(*tree_aging_report_with.get_children())
        parts_widthrawal_treeView()

    # pr_si_entry.delete(0, END)
    # pr_description_entry.delete('1.0', END)
    # pr_brand_entry.delete(0, END)
    # pr_clasfn_entry.delete(0, END)
    # pr_location_entry.delete(0, END)
    # pr_qty_entry.delete(0, END)
    # pr_unit_entry.delete(0, END)
    # pr_unit_price_entry.delete(0, END)
    # pr_amount_entry.delete(0, END)
    # pr_mris_entry.delete(0, END)
    # pr_purchaser_entry.delete(0, END)
    # pr_receiver_entry.delete(0, END)
    # pr_remarks.delete('1.0', END)
    # userName_entry.delete(0, END)
    # pr_inventoryID_entry.delete(0, END)


# global partwidth_date_with
# global dr_itemsID
# global dr_equipmentID_entry
# global dr_description_entry_with
# global dr_brand_entry_with
# global dr_clasfn_entry_with
# global dr_location_entry_with
# global dr_qty_entry_with
# global dr_unit_entry_with
# global dr_unit_price_entry_with
# global dr_amount_entry_with
def calculate_withrawal():
    """This function is to calculate amount Fields """
    amount_dr = float(dr_qty_entry_with.get()) * float(dr_unit_price_entry_with.get())
    amount = '{:,.2f}'.format(amount_dr)

    dr_amount_entry_with.delete(0, END)
    dr_amount_entry_with.insert(0, (amount))


def search_items():
    """This function is to search Items"""
    mydb._open_connection()
    cursor = mydb.cursor()

    inventoryid_with = dr_itemsID.get()

    query2 = "SELECT inventory_id,description,brand,\
                classification,location,unit,unit_price\
                     FROM parts WHERE inventory_id = '"+ inventoryid_with +"' "

    cursor.execute(query2)

    myresult2 = cursor.fetchall()

    for row in myresult2:
        inventoryID = row[0]
        descrip_with = row[1]
        brand_width = row[2]
        classif_with = row[3]
        loc_with = row[4]
        unit_with = row[5]
        unitprice_with = row[6]


        # dr_itemsID.delete(0, END)
        # dr_itemsID.insert(0, (inventoryID))

        dr_description_entry_with.delete('1.0', END)
        dr_description_entry_with.insert('1.0', (descrip_with))

        dr_brand_entry_with.delete(0, END)
        dr_brand_entry_with.insert(0, (brand_width))

        dr_clasfn_entry_with.delete(0, END)
        dr_clasfn_entry_with.insert(0, (classif_with))

        dr_location_entry_with.delete(0, END)
        dr_location_entry_with.insert(0, (loc_with))

        dr_unit_entry_with.delete(0, END)
        dr_unit_entry_with.insert(0, (unit_with))

        dr_unit_price_entry_with.delete(0, END)
        dr_unit_price_entry_with.insert(0, (unitprice_with))

        # global partwidth_date_with
        # global dr_itemsID
        # global dr_equipmentID_entry
        # global dr_description_entry_with
        # global dr_brand_entry_with
        # global dr_clasfn_entry_with
        # global dr_location_entry_with
        # global dr_qty_entry_with
        # global dr_unit_entry_with
        # global dr_unit_price_entry_with
        #global dr_amount_entry_with

def equipmentFields():
    """this function is for equipment Fields to apper in Combobox"""
    mydb._open_connection()
    cursor = mydb.cursor()
    query2 = "SELECT equipment_id\
                 FROM equipment_details\
                 ORDER BY equipment_id"


    cursor.execute(query2)

    myresult2 = cursor.fetchall()
    data = []
    for row in myresult2:
        data.append(row[0])

    return data

def partswithdrawal_module():
    """This function is for partwidthdrawal Frame"""
    clearInventory_frame()
    # user_Name_label = Label(inventory_frame, text='Parts Withdrawal', width=17, height=1, bg='yellow', fg='gray',
    #                         font=('Arial', 15), anchor='c')
    # user_Name_label.place(x=460, y=15)
    dr_date_label1 = Label(inventory_frame, text='Date From:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 11), anchor='e')
    dr_date_label1.place(x=350, y=15)

    global dr_dateFrom
    dr_dateFrom = DateEntry(inventory_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                                    foreground='white', borderwidth=2, padx=10, pady=10)
    dr_dateFrom.place(x=450, y=15)
    dr_dateFrom.configure(justify='center')

    dr_date_label2 = Label(inventory_frame, text='Date To:', width=10, height=1, bg='yellow', fg='gray',
                           font=('Arial', 11), anchor='e')
    dr_date_label2.place(x=550, y=15)

    global dr_dateto
    dr_dateto = DateEntry(inventory_frame, width=13, background='darkblue', date_pattern='yyyy-MM-dd',
                            foreground='white', borderwidth=2, padx=10, pady=10)
    dr_dateto.place(x=650, y=15)
    dr_dateto.configure(justify='center')

    global dr_equipmentID_entry_search
    dr_equipmentID_entry_search = ttk.Combobox(inventory_frame, width=17)
    dr_equipmentID_entry_search['values'] = equipmentFields()
    dr_equipmentID_entry_search.place(x=760, y=15)

    dr_quantity_with = DoubleVar()
    dr_unitPrice_with = DoubleVar()

    dr_itemsID_label = Label(inventory_frame, text='Items ID', width=13, height=1, bg='yellow', fg='gray',
                     font=('Arial', 11), anchor='e')
    dr_itemsID_label.place(x=10, y=15)

    global dr_itemsID
    dr_itemsID = Entry(inventory_frame, width=15, font=('Arial', 11), justify='left')
    dr_itemsID.place(x=140, y=15)


    dr_date_label = Label(inventory_frame, text='Date:', width=13, height=1, bg='yellow', fg='gray',
                          font=('Arial', 11), anchor='e')
    dr_date_label.place(x=10, y=50)

    global partwidth_date_with
    partwidth_date_with = DateEntry(inventory_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    partwidth_date_with.place(x=140, y=50)
    partwidth_date_with.configure(justify='center')

    product_si = Label(inventory_frame, text='Equpment ID:', width=13, height=1, bg='yellow', fg='gray',
                       font=('Arial', 11), anchor='e')
    product_si.place(x=10, y=75)

    global dr_equipmentID_entry
    dr_equipmentID_entry = ttk.Combobox(inventory_frame, width=20)
    dr_equipmentID_entry['values'] = equipmentFields()
    dr_equipmentID_entry.place(x=140, y=75)

    # pr_si_entry_with = Entry(inventory_frame, width=22, font=('Arial', 11))
    # pr_si_entry_with.place(x=140, y=75)

    pr_desciption = Label(inventory_frame, text='Description:', width=13, height=1, bg='yellow', fg='gray',
                          font=('Arial', 11), anchor='e')
    pr_desciption.place(x=10, y=100)

    global dr_description_entry_with
    dr_description_entry_with = scrolledtext.ScrolledText(inventory_frame,
                                                     wrap=tk.WORD,
                                                     width=23,
                                                     height=3,
                                                     font=("Arial",
                                                           10))
    dr_description_entry_with.place(x=140, y=100)

    pr_brand = Label(inventory_frame, text='Brand:', width=13, height=1, bg='yellow', fg='gray',
                     font=('Arial', 11), anchor='e')
    pr_brand.place(x=10, y=160)

    global dr_brand_entry_with
    dr_brand_entry_with = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    dr_brand_entry_with.place(x=140, y=160)

    dr_clasfn = Label(inventory_frame, text='Classification:', width=13, height=1, bg='yellow', fg='gray',
                      font=('Arial', 11), anchor='e')
    dr_clasfn.place(x=10, y=185)

    global dr_clasfn_entry_with
    dr_clasfn_entry_with = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    dr_clasfn_entry_with.place(x=140, y=185)

    dr_location = Label(inventory_frame, text='Location:', width=13, height=1, bg='yellow', fg='gray',
                        font=('Arial', 11), anchor='e')
    dr_location.place(x=10, y=210)

    global dr_location_entry_with
    dr_location_entry_with = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    dr_location_entry_with.place(x=140, y=210)

    pr_qty = Label(inventory_frame, text='Quantity:', width=13, height=1, bg='yellow', fg='gray',
                   font=('Arial', 11), anchor='e')
    pr_qty.place(x=10, y=235)

    global dr_qty_entry_with
    dr_qty_entry_with = Entry(inventory_frame, textvariable=dr_quantity_with, width=22, font=('Arial', 11), justify='right')
    dr_qty_entry_with.place(x=140, y=235)

    pr_unit = Label(inventory_frame, text='Unit:', width=13, height=1, bg='yellow', fg='gray',
                    font=('Arial', 11), anchor='e')
    pr_unit.place(x=10, y=260)

    global dr_unit_entry_with
    dr_unit_entry_with = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    dr_unit_entry_with.place(x=140, y=260)

    pr_unit_price = Label(inventory_frame, text='Unit Price:', width=13, height=1, bg='yellow', fg='gray',
                          font=('Arial', 11), anchor='e')
    pr_unit_price.place(x=10, y=285)

    global dr_unit_price_entry_with
    dr_unit_price_entry_with = Entry(inventory_frame, textvariable=dr_unitPrice_with, width=22, font=('Arial', 11),
                                justify='right')
    dr_unit_price_entry_with.place(x=140, y=285)

    pr_amount = Label(inventory_frame, text='Amount:', width=13, height=1, bg='yellow', fg='gray',
                      font=('Arial', 11), anchor='e')
    pr_amount.place(x=10, y=310)

    global dr_amount_entry_with
    dr_amount_entry_with = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    dr_amount_entry_with.place(x=140, y=310)

    pr_mris = Label(inventory_frame, text='MRIS:', width=13, height=1, bg='yellow', fg='gray',
                    font=('Arial', 11), anchor='e')
    pr_mris.place(x=10, y=335)

    dr_mris_entry_with = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    dr_mris_entry_with.place(x=140, y=335)

    pr_purchaser = Label(inventory_frame, text='Purchaser:', width=13, height=1, bg='yellow', fg='gray',
                         font=('Arial', 11), anchor='e')
    pr_purchaser.place(x=10, y=360)

    dr_purchaser_entry_with = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    dr_purchaser_entry_with.place(x=140, y=360)

    global dr_receiver_entry_with
    pr_receiver = Label(inventory_frame, text='Receiver:', width=13, height=1, bg='yellow', fg='gray',
                        font=('Arial', 11), anchor='e')
    pr_receiver.place(x=10, y=385)

    dr_receiver_entry_with = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    dr_receiver_entry_with.place(x=140, y=385)

    pr_remarkslbl = Label(inventory_frame, text='Remarks:', width=13, height=1, bg='yellow', fg='gray',
                          font=('Arial', 11), anchor='e')
    pr_remarkslbl.place(x=10, y=410)

    global dr_remarks_with
    dr_remarks_with = scrolledtext.ScrolledText(inventory_frame,
                                           wrap=tk.WORD,
                                           width=23,
                                           height=3,
                                           font=("Arial",
                                                 10))
    dr_remarks_with.place(x=140, y=410)

    # this is for Button Fields
    btn_pr_search_treeview = Button(inventory_frame, text="Search", bg='black', fg='white', font=('arial', 10),
                                 width=8,
                                 command=search_product_widthrawal)
    btn_pr_search_treeview.place(x=880, y=15)
    btn_pr_search_treeview.bind('<Return>', search_product_widthrawal)

    btn_pr_search_treeview_equip = Button(inventory_frame, text="EquipID", bg='black', fg='white', font=('arial', 10),
                                    width=8,
                                    command=search_with_per_equipment)
    btn_pr_search_treeview_equip.place(x=960, y=15)
    btn_pr_search_treeview_equip.bind('<Return>', search_with_per_equipment)

    btn_pr_search_print = Button(inventory_frame, text="Print", bg='red', fg='white', font=('arial', 10),
                                    width=8,
                                    command=print_withrawal)
    btn_pr_search_print.place(x=1040, y=15)
    btn_pr_search_print.bind('<Return>', print_withrawal)

    btn_pr_calculate_with = Button(inventory_frame, text="Calculate", bg='green', fg='white', font=('arial', 10), width=10,
                              command=calculate_withrawal)
    btn_pr_calculate_with.place(x=10, y=470)
    btn_pr_calculate_with.bind('<Return>', calculate_withrawal)

    btn_dr_save = Button(inventory_frame, text="Save", bg='cyan', fg='black', font=('arial', 10),
                                 width=9,
                                 command=insert_widthrawal)
    btn_dr_save.place(x=150, y=470)
    btn_dr_save.bind('<Return>', insert_widthrawal)

    btn_pr_search_items = Button(inventory_frame, text="Search", bg='cyan', fg='black', font=('arial', 10),
                                   width=9,
                                   command=search_items)
    btn_pr_search_items.place(x=280, y=15)
    btn_pr_search_items.bind('<Return>', search_items)


    # ===========================================Parts withdrawal Tree view Function======================================
    MidViewForm15 = Frame(inventory_frame, width=500, height=450)
    MidViewForm15.place(x=350, y=50)

    style = ttk.Style(inventory_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="yellow")
    # change selected color

    # style.map('Treeview',
    #             background[('selected','green')])

    scrollbarx = Scrollbar(MidViewForm15, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm15, orient=VERTICAL)
    global tree_aging_report_with
    tree_aging_report_with = ttk.Treeview(MidViewForm15,
                                     columns=("CNT", "DATE", "Trans ID", "Equipment ID",
                                              "INV-ID", "QUANTITY", "Amount"),
                                     selectmode="extended", height=21, yscrollcommand=scrollbary.set,
                                     xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree_aging_report_with.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree_aging_report_with.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree_aging_report_with.heading('CNT', text="No.", anchor=CENTER)
    tree_aging_report_with.heading('DATE', text="Date", anchor=CENTER)
    tree_aging_report_with.heading('Trans ID', text="Trans ID", anchor=CENTER)
    tree_aging_report_with.heading('Equipment ID', text="Equipment ID", anchor=CENTER)
    tree_aging_report_with.heading('INV-ID', text="INV-ID", anchor=CENTER)
    tree_aging_report_with.heading('QUANTITY', text="QUANTITY", anchor=CENTER)
    tree_aging_report_with.heading('Amount', text="Total Amount", anchor=CENTER)

    tree_aging_report_with.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    tree_aging_report_with.column('#1', stretch=NO, minwidth=0, width=90, anchor='e')
    tree_aging_report_with.column('#2', stretch=NO, minwidth=0, width=90, anchor='e')
    tree_aging_report_with.column('#3', stretch=NO, minwidth=0, width=90, anchor='e')
    tree_aging_report_with.column('#4', stretch=NO, minwidth=0, width=90, anchor='e')
    tree_aging_report_with.column('#5', stretch=NO, minwidth=0, width=90, anchor='e')
    tree_aging_report_with.column('#6', stretch=NO, minwidth=0, width=90, anchor='e')
    tree_aging_report_with.column('#7', stretch=NO, minwidth=0, width=90, anchor='e')

    tree_aging_report_with.pack()


# user_Name_label = Label(inventory_frame, text='', width=17, height=1, bg='yellow', fg='gray',
    #                         font=('Arial', 11), anchor='c')
    # user_Name_label.place(x=10, y=40)
#==============================================Parts Registry Module====================================================
def search_productRegistry():
    tree_parts_register.delete(*tree_parts_register.get_children())
    searchTreview()
def edit_product_registry():
    ts = time.time()
    mydb._open_connection()
    cursor = mydb.cursor()

    searchID = sear_edit_entry.get()
    cursor.execute("SELECT date_transact, si_dr_no, description, brand, classification, location,\
               quantity,unit,unit_price,amount,mris,purchaser,receiver,remarks,inventory_id\
               FROM `parts`\
               WHERE id ='" + searchID + "'")

    #inventory_id, date_transact, si_dr_no, description, brand, classification, location, "
    #"quantity,unit,unit_price,amount,mris,purchaser,receiver,remarks,users,date_update)"

    myresult = cursor.fetchall()
    for data in myresult:
        date_edit = data[0]
        siDr = data[1]
        desc_edit = data[2]
        brand_edit = data[3]
        classfi_edit = data[4]
        location_edit = data[5]
        quantity_edit = data[6]
        unit_edit = data[7]
        unitPrice_edit = data[8]
        amount_edit = data[9]
        mris_edit = data[10]
        pruchaser_edit = data[11]
        recieve_edit = data[12]
        remarks = data[13]
        inv_id = data[14]


        partregistry_date.delete(0, END)
        partregistry_date.insert(0, (date_edit))

        pr_si_entry.delete(0, END)
        pr_si_entry.insert(0, (siDr))

        pr_description_entry.delete('1.0', END)
        pr_description_entry.insert('1.0',(desc_edit))

        pr_brand_entry.delete(0, END)
        pr_brand_entry.insert(0, (brand_edit))

        pr_clasfn_entry.delete(0, END)
        pr_clasfn_entry.insert(0, (classfi_edit))

        pr_location_entry.delete(0, END)
        pr_location_entry.insert(0, (location_edit))

        pr_qty_entry.delete(0, END)
        pr_qty_entry.insert(0, (quantity_edit))

        pr_unit_entry.delete(0, END)
        pr_unit_entry.insert(0, (unit_edit))

        pr_unit_price_entry.delete(0, END)
        pr_unit_price_entry.insert(0, (unitPrice_edit))

        pr_amount_entry.delete(0, END)
        pr_amount_entry.insert(0, (amount_edit))

        pr_mris_entry.delete(0, END)
        pr_mris_entry.insert(0, (mris_edit))

        pr_purchaser_entry.delete(0, END)
        pr_purchaser_entry.insert(0, (pruchaser_edit))

        pr_receiver_entry.delete(0, END)
        pr_receiver_entry.insert(0, (recieve_edit))

        pr_remarks.delete('1.0', END)
        pr_remarks.insert('1.0', (remarks))

        pr_inventoryID_entry.delete(0, END)
        pr_inventoryID_entry.insert(0, (inv_id))


        date1 = partregistry_date.get()
        si_reg = pr_si_entry.get()
        desc_reg = pr_description_entry.get('1.0', 'end-1c')
        brand_reg = pr_brand_entry.get()
        classfin = pr_clasfn_entry.get()
        location_reg = pr_location_entry.get()
        quantity_reg = pr_qty_entry.get()
        unit_rg = pr_unit_entry.get()
        unitPrice_reg = pr_unit_price_entry.get()

        # amount = ('{:.2f}'.format(amount_reg))
        mris_reg = pr_mris_entry.get()
        purchaer_reg = pr_purchaser_entry.get()
        receiver_reg = pr_receiver_entry.get()
        remarks_reg = pr_remarks.get('1.0', 'end-1c')
        user_reg = userName_entry.get()
        date_time_update = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        inventoryID = pr_inventoryID_entry.get()
def parts_treeView_list():
    """This function is for dipslay of Parts Registry Data"""

    tree_parts_register.delete(*tree_parts_register.get_children())
    parts_register_treeView()

def searchTreview():

    mydb._open_connection()
    cursor = mydb.cursor()

    transIDSearch = pr_search.get()
    cursor.execute("SELECT id,inventory_id,si_dr_no,description,brand,classification,\
           quantity,unit,unit_price,amount\
           FROM `parts`\
           WHERE classification LIKE %s", ('%' + transIDSearch + '%',))
    #ORDER BY classification)
    fetch = cursor.fetchall()
    cnt = 0
    for data in fetch:
        cnt += 1
        id_num = data[0]
        inv_id = data[1]
        siNum = data[2]
        desc = data[3]
        brand = data[4]
        clasisification = data[5]

        quantity = '{:,.2f}'.format(data[6])
        unit = data[7]
        unit_price = '{:,.2f}'.format(data[8])
        amount = '{:,.2f}'.format(data[9])

        tree_parts_register.insert('', 'end', values=(
                                    cnt, id_num, inv_id, siNum, desc,
                                    brand, clasisification,
                                    quantity, unit, unit_price, amount))



def testing():
    mydb._open_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id,inventory_id,users,date_update\
           FROM `parts`\
           ORDER BY classification")
    fetch = cursor.fetchall()
    cnt = 0
    for data in fetch:
        cnt += 1
        id_num = data[0]
        inventoryID = data[1]
        users = data[2]
        update_user = data[3]

        print(cnt, inventoryID,  id_num, users, update_user)

def parts_register_treeView():
    mydb._open_connection()
    cursor = mydb.cursor()
    cursor.execute("SELECT id,inventory_id,si_dr_no,description,brand,classification,\
       quantity,unit,unit_price,amount\
       FROM `parts`\
       ORDER BY classification")
    fetch = cursor.fetchall()
    cnt = 0
    for data in fetch:
        cnt += 1
        id_num = data[0]
        inv_id = data[1]
        siNum = data[2]
        desc = data[3]
        brand = data[4]
        clasisification = data[5]

        quantity = data[6]
        unit = data[7]
        unit_price = '{:,.2f}'.format(data[8])
        amount = data[9]

        tree_parts_register.insert('', 'end', values=(
                                    cnt, id_num, inv_id, siNum, desc,
                                    brand, clasisification,
                                    quantity, unit, unit_price, amount))


def product_regstry_save():
    ts = time.time()
    mydb._open_connection()
    cursor = mydb.cursor()
    amountpr = float(pr_qty_entry.get()) * float(pr_unit_price_entry.get())

    date1 = partregistry_date.get()
    si_reg = pr_si_entry.get()
    desc_reg = pr_description_entry.get('1.0', 'end-1c')
    brand_reg = pr_brand_entry.get()
    classfin = pr_clasfn_entry.get()
    location_reg = pr_location_entry.get()
    quantity_reg = pr_qty_entry.get()
    unit_rg = pr_unit_entry.get()
    unitPrice_reg = pr_unit_price_entry.get()
    amount_reg = amountpr
    #amount = ('{:.2f}'.format(amount_reg))
    mris_reg = pr_mris_entry.get()
    purchaer_reg = pr_purchaser_entry.get()
    receiver_reg = pr_receiver_entry.get()
    remarks_reg = pr_remarks.get('1.0', 'end-1c')
    user_reg =userName_entry.get()
    date_time_update = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    inventoryID = pr_inventoryID_entry.get()

    try:
        if pr_inventoryID_entry.get() == '':
            messagebox.showerror('Plese input Inventory ID fields!')
        else:
            cursor.execute(
                "INSERT INTO parts (inventory_id,date_transact,si_dr_no,description,brand,classification,location,"
                "quantity,unit,unit_price,amount,mris,purchaser,receiver,remarks,users,date_update)"
                " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (inventoryID,date1, si_reg, desc_reg, brand_reg, classfin, location_reg, quantity_reg,
                 unit_rg, unitPrice_reg, amount_reg,
                 mris_reg, purchaer_reg,
                 receiver_reg, remarks_reg, user_reg, date_time_update))

            mydb.commit()
            mydb.close()
            cursor.close()
            messagebox.showinfo('JRS','Data has been save')
            parts_treeView_list()

            pr_si_entry.delete(0, END)
            pr_description_entry.delete('1.0', END)
            pr_brand_entry.delete(0, END)
            pr_clasfn_entry.delete(0, END)
            pr_location_entry.delete(0, END)
            pr_qty_entry.delete(0, END)
            pr_unit_entry.delete(0, END)
            pr_unit_price_entry.delete(0, END)
            pr_amount_entry.delete(0, END)
            pr_mris_entry.delete(0, END)
            pr_purchaser_entry.delete(0, END)
            pr_receiver_entry.delete(0, END)
            pr_remarks.delete('1.0', END)
            userName_entry.delete(0, END)
            pr_inventoryID_entry.delete(0, END)

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")
def amount_productRegistry_cal():
    mydb._open_connection()
    cursor = mydb.cursor()
    amountpr = float(pr_qty_entry.get()) * float(pr_unit_price_entry.get())
    #print(amountpr)
    amountpr1 = (amountpr)
    amountpr2 = '{:,.2f}'.format(amountpr1)
    pr_amount_entry.delete(0, END)
    pr_amount_entry.insert(0, (amountpr2))


def partsRegistry_module():
    clearInventory_frame()
    mydb._open_connection()
    pr_quantity = DoubleVar()
    pr_unitPrice = DoubleVar()

    global partregistry_date
    global pr_si_entry
    global pr_description_entry
    global pr_brand_entry
    global pr_clasfn_entry
    global pr_location_entry
    global pr_qty_entry
    global pr_unit_entry
    global pr_unit_price_entry
    global pr_amount_entry
    global pr_mris_entry
    global pr_purchaser_entry
    global pr_receiver_entry
    global pr_remarks
    global pr_search
    global pr_inventoryID_entry
    global sear_edit_entry



    user_Name_label = Label(inventory_frame, text='Parts Registry', width=17, height=1, bg='yellow', fg='gray',
                            font=('Arial', 15), anchor='c')
    user_Name_label.place(x=460, y=15)

# this is for search function

    user_Name_label = Label(inventory_frame, text='Classification', width=15, height=1, bg='yellow', fg='gray',
                            font=('Arial', 12), anchor='c')
    user_Name_label.place(x=660, y=15)

    # pr_search = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    # pr_search.place(x=810, y=15)


# this is for fields frames for Parts Registry
    inventoryid_label = Label(inventory_frame, text='Inventory ID:', width=13, height=1, bg='yellow', fg='gray',
                       font=('Arial', 11), anchor='e')
    inventoryid_label.place(x=10, y=25)

    pr_inventoryID_entry = Entry(inventory_frame, width=22, font=('Arial', 11))
    pr_inventoryID_entry.place(x=140, y=25)

    pr_date_label = Label(inventory_frame, text='Date:', width=13, height=1, bg='yellow', fg='gray',
                          font=('Arial', 11), anchor='e')
    pr_date_label.place(x=10, y=50)

    partregistry_date = DateEntry(inventory_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    partregistry_date.place(x=140, y=50)
    partregistry_date.configure(justify='center')

    product_si = Label(inventory_frame, text='SI/DR no:', width=13, height=1, bg='yellow', fg='gray',
                       font=('Arial', 11), anchor='e')
    product_si.place(x=10, y=75)

    pr_si_entry = Entry(inventory_frame, width=22,  font=('Arial', 11))
    pr_si_entry.place(x=140, y=75)

    pr_desciption = Label(inventory_frame, text='Description:', width=13, height=1, bg='yellow', fg='gray',
                       font=('Arial', 11), anchor='e')
    pr_desciption.place(x=10, y=100)

    pr_description_entry = scrolledtext.ScrolledText(inventory_frame,
                                          wrap=tk.WORD,
                                          width=23,
                                          height=3,
                                          font=("Arial",
                                                10))
    pr_description_entry.place(x=140, y=100)

    pr_brand = Label(inventory_frame, text='Brand:', width=13, height=1, bg='yellow', fg='gray',
                   font=('Arial', 11), anchor='e')
    pr_brand.place(x=10, y=160)

    pr_brand_entry = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    pr_brand_entry.place(x=140, y=160)

    pr_clasfn = Label(inventory_frame, text='Classification:', width=13, height=1, bg='yellow', fg='gray',
                     font=('Arial', 11), anchor='e')
    pr_clasfn.place(x=10, y=185)

    # pr_clasfn_entry = Entry(inventory_frame,  width=22, font=('Arial', 11), justify='right')
    # pr_clasfn_entry.place(x=140, y=185)

    pr_clasfn_entry = ttk.Combobox(inventory_frame, width=20)
    pr_clasfn_entry['values'] = ("Salaries", "Oil-lubes", "Repair-Maintenance", "Meals",
                                 "Tranpo", "Tires", "Depreciation","Others")
    pr_clasfn_entry.place(x=140, y=185)

    pr_location = Label(inventory_frame, text='Location:', width=13, height=1, bg='yellow', fg='gray',
                      font=('Arial', 11), anchor='e')
    pr_location.place(x=10, y=210)

    pr_location_entry = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    pr_location_entry.place(x=140, y=210)

    pr_qty = Label(inventory_frame, text='Quantity:', width=13, height=1, bg='yellow', fg='gray',
                          font=('Arial', 11), anchor='e')
    pr_qty.place(x=10, y=235)

    pr_qty_entry = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    pr_qty_entry.place(x=140, y=235)

    pr_unit = Label(inventory_frame, text='Unit:', width=13, height=1, bg='yellow', fg='gray',
                   font=('Arial', 11), anchor='e')
    pr_unit.place(x=10, y=260)

    pr_unit_entry = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    pr_unit_entry.place(x=140, y=260)

    pr_unit_price = Label(inventory_frame, text='Unit Price:', width=13, height=1, bg='yellow', fg='gray',
                    font=('Arial', 11), anchor='e')
    pr_unit_price.place(x=10, y=285)

    pr_unit_price_entry = Entry(inventory_frame,width=22, font=('Arial', 11), justify='right')
    pr_unit_price_entry.place(x=140, y=285)

    pr_amount = Label(inventory_frame, text='Amount:', width=13, height=1, bg='yellow', fg='gray',
                          font=('Arial', 11), anchor='e')
    pr_amount.place(x=10, y=310)

    pr_amount_entry = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    pr_amount_entry.place(x=140, y=310)

    pr_mris = Label(inventory_frame, text='MRIS:', width=13, height=1, bg='yellow', fg='gray',
                      font=('Arial', 11), anchor='e')
    pr_mris.place(x=10, y=335)

    pr_mris_entry = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    pr_mris_entry.place(x=140, y=335)

    pr_purchaser = Label(inventory_frame, text='Purchaser:', width=13, height=1, bg='yellow', fg='gray',
                    font=('Arial', 11), anchor='e')
    pr_purchaser.place(x=10, y=360)

    pr_purchaser_entry = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    pr_purchaser_entry.place(x=140, y=360)

    pr_receiver = Label(inventory_frame, text='Receiver:', width=13, height=1, bg='yellow', fg='gray',
                         font=('Arial', 11), anchor='e')
    pr_receiver.place(x=10, y=385)

    pr_receiver_entry = Entry(inventory_frame, width=22, font=('Arial', 11), justify='right')
    pr_receiver_entry.place(x=140, y=385)

    pr_remarkslbl = Label(inventory_frame, text='Remarks:', width=13, height=1, bg='yellow', fg='gray',
                          font=('Arial', 11), anchor='e')
    pr_remarkslbl.place(x=10, y=410)

    pr_remarks = scrolledtext.ScrolledText(inventory_frame,
                                                     wrap=tk.WORD,
                                                     width=23,
                                                     height=3,
                                                     font=("Arial",
                                                           10))
    pr_remarks.place(x=140, y=410)

    pr_search = Entry(inventory_frame, width=10, font=('Arial', 11), justify='right')
    pr_search.place(x=810, y=15)

    searchLabel = Label(inventory_frame, text='Unit:', width=13, height=1, bg='yellow', fg='gray',
                    font=('Arial', 11), anchor='e')
    searchLabel.place(x=10, y=530)

    sear_edit_entry = Entry(inventory_frame, width=10, font=('Arial', 11), justify='right')
    sear_edit_entry.place(x=140, y=530)

    btn_pr_search = Button(inventory_frame, text="Search ID", bg='green', fg='white', font=('arial', 10), width=10,
                              command=edit_product_registry)
    btn_pr_search.place(x=230, y=530)
    btn_pr_search.bind('<Return>', edit_product_registry)

    btn_pr_calculate = Button(inventory_frame, text="Calculate", bg='green', fg='white', font=('arial', 10), width=10,
                        command=amount_productRegistry_cal)
    btn_pr_calculate.place(x=10, y=470)
    btn_pr_calculate.bind('<Return>', amount_productRegistry_cal)

    btn_pr_save = Button(inventory_frame, text="Save", bg='black', fg='white', font=('arial', 10), width=10,
                              command=product_regstry_save)
    btn_pr_save.place(x=110, y=470)
    btn_pr_save.bind('<Return>', product_regstry_save)

    btn_pr_test = Button(inventory_frame, text="Testing", bg='black', fg='white', font=('arial', 10), width=10,
                         command=testing)
    btn_pr_test.place(x=210, y=470)
    btn_pr_test.bind('<Return>', testing)

    btn_pr_search = Button(inventory_frame, text="Search", bg='black', fg='white', font=('arial', 10), width=10,
                           command=search_productRegistry)
    btn_pr_search.place(x=910, y=15)
    btn_pr_search.bind('<Return>', search_productRegistry)

# ===========================================Parts Registration Tree view Function======================================
    MidViewForm15 = Frame(inventory_frame, width=500, height=450)
    MidViewForm15.place(x=350, y=50)

    style = ttk.Style(inventory_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    fieldbackground="yellow")
    # change selected color

    # style.map('Treeview',
    #             background[('selected','green')])

    scrollbarx = Scrollbar(MidViewForm15, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm15, orient=VERTICAL)
    global tree_parts_register
    tree_parts_register = ttk.Treeview(MidViewForm15,
                                     columns=("CNT", "TRANS ID", "InventoryID",
                                              "SI NUM", "Description",
                                              "Brand", "Classification", "Quantity",
                                              "Unit", "Unit Price", "Amount"),
                                     selectmode="extended", height=21, yscrollcommand=scrollbary.set,
                                     xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree_parts_register.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree_parts_register.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree_parts_register.heading('CNT', text="No.", anchor=CENTER)

    tree_parts_register.heading('TRANS ID', text="Tran ID", anchor=CENTER)
    tree_parts_register.heading('InventoryID', text="INV-ID", anchor=CENTER)
    tree_parts_register.heading('SI NUM', text="SI number", anchor=CENTER)

    tree_parts_register.heading('Description', text="Description", anchor=CENTER)
    tree_parts_register.heading('Brand', text="Brand", anchor=CENTER)
    tree_parts_register.heading('Classification', text="Classification", anchor=CENTER)
    tree_parts_register.heading('Quantity', text="Quantity", anchor=CENTER)
    tree_parts_register.heading('Unit', text="unit", anchor=CENTER)
    tree_parts_register.heading('Unit Price', text="Unit Price", anchor=CENTER)
    tree_parts_register.heading('Amount', text="Amount", anchor=CENTER)

    tree_parts_register.column('#0', stretch=NO, minwidth=0, width=0)
    tree_parts_register.column('#1', stretch=NO, minwidth=0, width=50)
    tree_parts_register.column('#2', stretch=NO, minwidth=0, width=50)
    tree_parts_register.column('#3', stretch=NO, minwidth=0, width=50, anchor='e')
    tree_parts_register.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
    tree_parts_register.column('#5', stretch=NO, minwidth=0, width=150, anchor='e')
    tree_parts_register.column('#6', stretch=NO, minwidth=0, width=50, anchor='e')
    tree_parts_register.column('#7', stretch=NO, minwidth=0, width=50, anchor='e')
    tree_parts_register.column('#8', stretch=NO, minwidth=0, width=50, anchor='e')
    tree_parts_register.column('#9', stretch=NO, minwidth=0, width=50, anchor='e')
    tree_parts_register.column('#10', stretch=NO, minwidth=0, width=50, anchor='e')
    tree_parts_register.column('#11', stretch=NO, minwidth=0, width=100, anchor='e')



    tree_parts_register.pack()

    parts_treeView_list()




def inventory_module():
    clearFrame()
    global inventory_frame
    # global logo_icon3
    # load3 = Image.open("image\partsregistry.png")
    # load3 = load3.resize((130, 70), Image.ANTIALIAS)
    # logo_icon3 = ImageTk.PhotoImage(load3)

    inventory_frame = Frame(MidViewForm9, width=1120, height=575, bd=2,bg='gray', relief=SOLID)
    inventory_frame.place(x=160, y=8)

    btn_partRegistry = Button(MidViewForm9, text='Parts Registry', bd=2,bg='blue', fg='white',
                        font=('arial', 12), width=15,height=2,command=partsRegistry_module)
    btn_partRegistry.place(x=2, y=70)
    btn_partRegistry.bind('<Return>', partsRegistry_module)

    btn_partwithdral = Button(MidViewForm9, text='Parts Withdrawal', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command=partswithdrawal_module)
    btn_partwithdral.place(x=2, y=120)
    btn_partwithdral.bind('<Return>', partswithdrawal_module)
#===============================================Payroll Transactions===================================================
def print1601c_report():
    """This function is to print 1601C"""

    mydb._open_connection()
    cursor = mydb.cursor()
    date1 = cal7.get()
    date2 = cal8.get()
    user_reg = userName_entry.get()
    miminum_wage = str(420)

    cursor.execute("SELECT employee_id\
                            FROM payroll_computation where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' ")
    myresult = list(cursor.fetchall())
    result = []

    cnt = 0
    for row in myresult:
        cnt += 1

        data = {'count': cnt,
                'employeeid': row[0],

                }

        result.append(data)


    # this query is for total Gross
        cursor.execute("SELECT sum(grosspay_save) as GROSS\
                                    FROM payroll_computation\
                                    where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                                 ")
        myresult = list(cursor.fetchall())

        for row in myresult:
            gross_payT = '{:,.2f}'.format(row[0])

    # this query is for total MWE Gross
        cursor.execute("SELECT sum(grosspay_save) as GROSS, SUM(total_mandatory) AS TOTALMAN,\
                       sum(regularday_ot_cal) as REGOT,sum(regularsunday_ot_cal) as SUNOT,\
                       sum(spl_ot_cal) as SPLOT,sum(legal_day_ot_cal) as LGL2OT,\
                       sum(proviRate_day_ot_cal) as PROVIOT,sum(provisun_day_ot_cal) as PROVISUNOT,\
                       sum(nightdiff_day_cal) as NDIFF \
                       FROM payroll_computation \
                       where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                        AND  salary_rate <= '"+ miminum_wage +"' ")
                                            # FROM payroll_computation\
                                            # where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                            #  AND  salary_rate <= '"+ miminum_wage +"' ")

        # "sss_save,phic_save,hmdf_save,sss_provi_save,total_mandatory,uniform_save,rice_save,laundry_save,"
        # "medical1_save,"
        # "medical2_save,totalDem_save,otherforms_save,taxable_amount,taxwitheld_save,cashadvance_save,"
        # "sssloan_save,hdmfloan_save,netpay_save,"

        myresult = list(cursor.fetchall())

        for row in myresult:
            totalMan = row[1]
            mwe_gross1 = row[0]
            reg_ot = row[2]
            sun_ot = row[3]
            spl_ot = row[4]
            lgl2_ot = row[5]
            provi_ot = row[6]
            provisun_ot = row[7]
            nightdiff = row[8]
            mwe_gross3 = mwe_gross1-totalMan-reg_ot-sun_ot-spl_ot-lgl2_ot-provi_ot-provisun_ot-nightdiff
            mwe_gross = '{:,.2f}'.format(mwe_gross3)

    # this query is for total MWE OT & Others
        cursor.execute("SELECT \
                       sum(regularday_ot_cal) as REGOT,sum(regularsunday_ot_cal) as SUNOT,\
                       sum(spl_ot_cal) as SPLOT,sum(legal_day_ot_cal) as LGL2OT,\
                       sum(proviRate_day_ot_cal) as PROVIOT,sum(provisun_day_ot_cal) as PROVISUNOT,\
                       sum(nightdiff_day_cal) as NDIFF \
                       FROM payroll_computation \
                       where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                        AND  salary_rate <= '" + miminum_wage + "' ")


        myresult = list(cursor.fetchall())

        for row in myresult:

            reg_ot = row[0]
            sun_ot = row[1]
            spl_ot = row[2]
            lgl2_ot = row[3]
            provi_ot = row[4]
            provisun_ot = row[5]
            nightdiff = row[6]
            mwe_ot = reg_ot + sun_ot + spl_ot + lgl2_ot + provi_ot + provisun_ot + nightdiff
            mwe_ot1 = '{:,.2f}'.format(mwe_ot)

    # this is for Total Deminimis
        cursor.execute("SELECT sum(totalDem_save) as totaldem\
                                            FROM payroll_computation\
                                            where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                                         ")
        myresult = list(cursor.fetchall())

        for row in myresult:
            totaldem = row[0]
            totaldem1 = '{:,.2f}'.format(row[0])

    # this is for Total Taxable Not Subject
        cursor.execute("SELECT sum(taxable_amount) as totaltaxable_amount\
                                            FROM payroll_computation\
                                            where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                             AND  salary_rate >= '" + miminum_wage + "'\
                                              AND taxable_amount < 10417")
        myresult = list(cursor.fetchall())

        for row in myresult:
            taxable_notsubject = row[0]
            taxable_notsubject1 = '{:,.2f}'.format(row[0])

    # this is for Total Otherforms
        cursor.execute("SELECT sum(otherforms_save) as totalOtherForms\
                                               FROM payroll_computation\
                                               where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                                            ")
        myresult = list(cursor.fetchall())

        for row in myresult:
            other_forms = row[0]
            other_forms1 = '{:,.2f}'.format(row[0])

    # this is for Total Mandatory
        cursor.execute("SELECT sum(total_mandatory) as Totalmandatory\
                                                   FROM payroll_computation\
                                                   where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                                                ")
        myresult = list(cursor.fetchall())

        for row in myresult:
            total_manDatory = row[0]
            total_manDatory1 = '{:,.2f}'.format(row[0])

    # this is for Total taxWithheld
        cursor.execute("SELECT sum(taxwitheld_save) as totaltaxwithheld\
                                                   FROM payroll_computation\
                                                   where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                                                ")
        myresult = list(cursor.fetchall())

        for row in myresult:
            withheld = row[0]
            withheld1 = '{:,.2f}'.format(row[0])

    # this is for Total Taxable greater than 10417
        cursor.execute("SELECT sum(taxable_amount) as totaltaxable_amount\
                                               FROM payroll_computation\
                                               where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                                AND  salary_rate >= '" + miminum_wage + "'\
                                                 AND taxable_amount > 10417")
        myresult = list(cursor.fetchall())

        for row in myresult:
            taxable_subject = row[0]
            taxable_subject1 = '{:,.2f}'.format(row[0])
        a1 = date1
        a2 = date2
        rpt = Report(result)

        rpt.detailband = Band([

            #Element((65, 0), ("Helvetica", 8), key='employeeid', align="right"),
        ])
        rpt.pageheader = Band([
            Element((30, 0), ("Times-Bold", 13),
                    text="LD GLOBAL LEGACY    1601c"),
            Element((250, 0), ("Times-Bold", 13),
                    text='Date From'),
            Element((330, 0), ("Times-Bold", 13),
                    text=a1),
            Element((415, 0), ("Times-Bold", 13),
                    text=' to'),
            Element((440, 0), ("Times-Bold", 13),
                    text=a2),
            Rule((36, 42), 11.5 * 40, thickness=2),
        ])

        rpt.reportfooter = Band([

            Element((115, 40), ("Helvetica-Bold", 10),
                    text="Total Gross"),
            Element((280, 40), ("Helvetica-Bold", 10),
                    text=gross_payT, align="right"),
            Element((115, 70), ("Helvetica-Bold", 10),
                    text="Total Gross MWE"),
            Element((280, 70), ("Helvetica-Bold", 10),
                    text=mwe_gross, align="right"),
            Element((115, 100), ("Helvetica-Bold", 10),
                    text="Total MWE OT"),
            Element((280, 100), ("Helvetica-Bold", 10),
                    text=mwe_ot1, align="right"),
            Element((115, 130), ("Helvetica-Bold", 10),
                    text="Total Deminimis"),
            Element((280, 130), ("Helvetica-Bold", 10),
                    text=totaldem1, align="right"),
            Element((115, 160), ("Helvetica-Bold", 10),
                    text="Total Other Forms"),
            Element((280, 160), ("Helvetica-Bold", 10),
                    text=other_forms1, align="right"),
            Element((115, 190), ("Helvetica-Bold", 10),
                    text="Total Mandatory"),
            Element((280, 190), ("Helvetica-Bold", 10),
                    text=total_manDatory1, align="right"),
            Element((115, 220), ("Helvetica-Bold", 10),
                    text="Total Not Subject"),
            Element((280, 220), ("Helvetica-Bold", 10),
                    text=taxable_notsubject1, align="right"),
            Element((115, 250), ("Helvetica-Bold", 10),
                    text="Total Taxable"),
            Element((280, 250), ("Helvetica-Bold", 10),
                    text=taxable_subject1, align="right"),
            Element((115, 280), ("Helvetica-Bold", 10),
                    text="Total Tax With Held"),
            Element((280, 280), ("Helvetica-Bold", 10),
                    text=withheld1, align="right"),
            Element((70, 370), ("Helvetica", 10),
                    text="Prepared BY:"),
            Element((210, 370), ("Helvetica", 10),
                    text=user_reg),
        ])
        canvas = Canvas("1601c.pdf")
        rpt.generate(canvas)
        canvas.save()


    startfile("1601c.pdf")

def print_1601C():
    """This function is to search 1601C"""
    clearpayrollFrame()
    mydb._open_connection()
    cursor = mydb.cursor()

    global cal7
    global cal8
    global date_from_entry
    global date_to_entry

    date_from_label = Label(payroll_frame, text='Date From:', width=10, height=1, bg='yellow', fg='gray',
                              font=('Arial', 10), anchor='e')
    date_from_label.place(x=250, y=150)

    # date_from_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    # date_from_entry.place(x=350, y=150)

    cal7 = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                            foreground='white', borderwidth=2, padx=10, pady=10)
    cal7.place(x=350, y=150)
    cal7.configure(justify='center')

    date_to_label = Label(payroll_frame, text='Date To:', width=10, height=1, bg='yellow', fg='gray',
                            font=('Arial', 10), anchor='e')
    date_to_label.place(x=550, y=150)

    # date_to_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    # date_to_entry.place(x=650, y=150)

    cal8 = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                               foreground='white', borderwidth=2, padx=10, pady=10)
    cal8.place(x=650, y=150)
    cal8.configure(justify='center')

    btn_search = Button(payroll_frame, text="Print 1601c", bg='gray', fg='yellow', font=('arial', 9),
                                width=12, command=print1601c_report)
    btn_search.place(x=820, y=150)
    btn_search.bind('<Return>', print1601c_report)






def print_payroll():
    """This function is to print Payroll"""
    mydb._open_connection()
    cursor = mydb.cursor()
    department = department_list.get()
    user_reg = userName_entry.get()


    query = 'Select *\
                     from cut_off'
    cursor.execute(query)
    myresult = cursor.fetchall()


    for row in myresult:
        date1 = str(row[1])
        date2 = str(row[2])


        cursor.execute("SELECT employee_id,last_name,\
                        first_name,salary_rate,grosspay_save,sss_save,\
                        phic_save,hmdf_save,totalDem_save,taxwitheld_save,\
                       cashadvance_save,sssloan_save,hdmfloan_save,netpay_save\
                        FROM payroll_computation where cut_off_date BETWEEN '"+ date1 +"' and '"+ date2 +"' \
                      AND department = '" + department + "'")
        myresult = list(cursor.fetchall())
        result = []

        cnt = 0
        for row in myresult:
            cnt+=1

            data = {'count': cnt,
                    'employeeid': row[0],
                    'lastname': row[1],
                    'firstname': row[2],
                    'salaryrate': row[3],
                    'grosspay': row[4],
                    'sss': row[5],
                     'phic': row[6],
                    'hdmf': row[7],
                    'totaldem': row[8],
                     'taxwidtheld': row[9],
                    'cashadvance': row[10],
                    'sssloan': row[11],
                    'hdmfloan': row[12],
                    'netpay': row[13],
                    'netpay2': '{:,.2f}'.format(row[13])
                    }

            result.append(data)
            a1 = date1
            a2 = date2
            defp_fields = ''

            if department == 'Admin-Site':
                defp_fields  = 'ADMIN SITE PAYROLL'
            elif department == 'Pampanga':
                defp_fields  = 'PAMPANGA PAYROLL'
            elif department == 'Rizal-R&F':
                defp_fields  = 'RIZAL  PAYROLL'

            else:
                defp_fields = 'LD HO PAYROLL'

            cursor.execute("SELECT sum(grosspay_save) as GROSS,SUM(netpay_save) AS netpay\
                                           FROM payroll_computation where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                         AND department = '" + department + "'")
            myresult = list(cursor.fetchall())

            for row in myresult:
                gross_payT = '{:,.2f}'.format(row[0])
                net_payt =  '{:,.2f}'.format(row[1])

            rpt = Report(result)
            rpt.detailband = Band([

                Element((65, 0), ("Helvetica", 8), key='employeeid', align="right"),
                Element((130, 0), ("Helvetica", 8), key='lastname', align="right"),
                Element((210, 0), ("Helvetica", 8), key='firstname', align="right"),
                Element((270, 0), ("Helvetica", 8), key='salaryrate', align="right"),
                Element((325, 0), ("Helvetica", 8), key='grosspay', align="right"),
                Element((380, 0), ("Helvetica", 8), key='sss', align="right"),
                Element((420, 0), ("Helvetica", 8), key='phic', align="right"),
                Element((460, 0), ("Helvetica", 8), key='hdmf', align="right"),
                Element((520, 0), ("Helvetica", 8), key='totaldem', align="right"),
                Element((590, 0), ("Helvetica", 8), key='taxwidtheld', align="right"),
                Element((665, 0), ("Helvetica", 8), key='cashadvance', align="right"),
                Element((730, 0), ("Helvetica", 8), key='sssloan', align="right"),
                Element((800, 0), ("Helvetica", 8), key='hdmfloan', align="right"),
                Element((870, 0), ("Helvetica", 8), key='netpay2', align="right"),
                Element((30, 0), ("Helvetica", 8), key='count', align="right"),
                #Rule((36, 0), 11.5 * 72, thickness=.2)



            ])

            rpt.pageheader = Band([
                Element((30, 0), ("Times-Bold", 13),
                        text=defp_fields),
                Element((170, 0), ("Times-Bold", 13),
                        text='Date From'),
                Element((250, 0), ("Times-Bold", 13),
                        text=a1),
                Element((325, 0), ("Times-Bold", 13),
                        text=' to'),
                Element((350, 0), ("Times-Bold", 13),
                        text=a2),
                Element((30, 24), ("Helvetica", 9),
                        text="Employee ID"),
                Element((150, 24), ("Helvetica", 9),
                        text="Last Name", align="right"),
                Element((210, 24), ("Helvetica", 9),
                        text="First Name", align="right"),
                Element((270, 24), ("Helvetica", 9),
                        text="Salary Rate", align="right"),
                Element((325, 24), ("Helvetica", 9),
                        text="Gross Pay", align="right"),
                Element((380, 24), ("Helvetica", 9),
                        text="SSS", align="right"),
                Element((420, 24), ("Helvetica", 9),
                        text="PHIC", align="right"),
                Element((460, 24), ("Helvetica", 9),
                        text="HDMF", align="right"),
                Element((520, 24), ("Helvetica", 9),
                        text="Total DEM", align="right"),
                Element((590, 24), ("Helvetica", 9),
                        text="TAX WITHELD", align="right"),
                Element((665, 24), ("Helvetica", 9),
                        text="CASH ADVANCE", align="right"),
                Element((730, 24), ("Helvetica", 9),
                        text="SSS LOAN", align="right"),
                Element((800, 24), ("Helvetica", 9),
                        text="HDMF LOAN", align="right"),
                Element((870, 24), ("Helvetica", 9),
                        text="NET PAY", align="right"),
                Element((28, 24), ("Helvetica", 9),
                        text="No.", align="right"),

                Rule((36, 42), 11.5 * 72, thickness=2),
            ])
            rpt.reportfooter = Band([
                Rule((36, 4), 11.5 * 72),
                Element((36, 4), ("Helvetica-Bold", 12),
                        text="Grand Total"),
                Element((325, 4), ("Helvetica-Bold", 10),
                           text=gross_payT, align="right"),
                SumElement((380, 4), ("Helvetica-Bold", 9),
                           key="sss", align="right"),
                SumElement((420, 4), ("Helvetica-Bold", 9),
                           key="phic", align="right"),
                SumElement((460, 4), ("Helvetica-Bold", 9),
                           key="hdmf", align="right"),
                SumElement((520, 4), ("Helvetica-Bold", 9),
                           key="totaldem", align="right"),
                SumElement((590, 4), ("Helvetica-Bold", 9),
                           key="taxwidtheld", align="right"),
                SumElement((665, 4), ("Helvetica-Bold", 9),
                           key="cashadvance", align="right"),
                SumElement((730, 4), ("Helvetica-Bold", 9),
                           key="sssloan", align="right"),
                SumElement((800, 4), ("Helvetica-Bold", 9),
                           key="hdmfloan", align="right"),
                Element((870, 4), ("Helvetica-Bold", 10),
                           text=net_payt, align="right"),
                Element((36, 30), ("Helvetica", 10),
                        text="Prepared BY:"),
                Element((80, 60), ("Helvetica", 10),
                        text= user_reg),
                Element((300, 30), ("Helvetica", 10),
                        text="Check  BY:"),
                Element((344, 60), ("Helvetica", 10),
                        text='JEROME R. SABUSIDO'),

            ])
            #canvas = Canvas("payroll.pdf") for short bond paper configuration
            canvas = Canvas("payroll.pdf", (72 * 13, 72 * 8.5))
            rpt.generate(canvas)
            canvas.save()

        startfile("payroll.pdf")









def save_payroll():
    mydb._open_connection()
    cursor = mydb.cursor()

    ts = time.time()
    result = tkMessageBox.askquestion('JRS Software', 'Would you like to save Transaction?', icon="warning")
    if result == 'yes':

        department = department_list.get()
        date1 = payCal_date.get()
        empID = empID_entry.get()
        lastname = lastname_entry.get()
        firstname = firstname_entry.get()
        posittion = position_entry.get()
        salRate_entry = salaryRate
        provicialRate = mwe
        regday_save = regday_entry.get()
        regdaycal_save = regdaycal
        regdayot_save = regOT
        regdaycalOT_save = regdaycalOT
        regsun_save = regsun
        regsuncal_save = regsuncal
        regsunOT_save = regsunOT
        regsuncalOT_save = regsuncalOT
        spl_save =  spl
        splCal_save = splCal
        splOT_save = splOT
        splOTcal_save = splOTcal
        legal_save = legal
        legalCal_save = legalCal
        legalOT_save = legalOT
        legalOTcal_save = legalOTcal
        shoprate_save = shoprate
        shoprateCal_save = shoprateCal
        proviRate_save = proviRate
        proviRateCal_save = proviRateCal
        proviRateOT_save = proviRateOT
        proviRateOTcal_save = proviRateOTcal
        proviRateSun_save = proviRateSun
        proviRateSunCal_save = proviRateSunCal
        proviSunRateOT_save = proviSunRateOT
        proviSunRateOTcal_save = proviSunRateOTcal
        nightdiff_save = nightdiff
        nightdiffCal_save = nightdiffCal
        adjustments_save = adjustments
        adjustmentCal_save = adjustmentCal
        grosspay_save = grosspay
        salaryDetails_save = details

    # this is for govt mandatory variable
        sss_save = sss_entry.get()
        hdmf_save = hdmf_entry.get()
        phic_save = phic_entry.get()
        provshare_save = provshare

        # sss_save = sss
        # hdmf_save = hdmf
        # phic_save = phic
        # provshare_save = provshare
        #
        # sss3 = sss_entry.get()
        # hdmf3 = hdmf_entry.get()
        # phic3 = phic_entry.get()

        totalMadatory_save = totalMadatory

    # this is for deminimis and taxwithdeld
        uniform_save = uniform
        rice_save = rice
        laundry_save = laundry
        medical1_save = medical1
        medical2_save = medical2
        totalDem_save = totalDem
        afterDem_save = afterDem
        otherForms_save = otherForms
        taxable_amount_save = taxable_amount
        taxWithheld_save = taxWithheld


     # this is for loan deduction and CS
        hdmfdeduct_save = hdmfdeduct
        ca_deduct_save = ca_deduct
        sss_loandeduct_save = sss_loandeduct
        netPay_save = netPay





        user_reg = userName_entry.get()

        date_time_update = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        cursor.execute(
            "INSERT INTO payroll_computation (department,cut_off_date,employee_id,last_name," 
            "first_name,position_name,salary_rate,provicaial_rate,regular_day, regularday_cal," 
            "regularday_ot,regularday_ot_cal,regularsunday, regularsunday_cal,regularsunday_ot,regularsunday_ot_cal, " 
            "spl,spl_cal,spl_ot,spl_ot_cal, legal_day,legal_day_cal,legal_day_ot,legal_day_ot_cal,"
            "shoprate_day,shoprate_day_cal,proviRate_day,proviRate_day_cal,proviRate_day_ot," 
            "proviRate_day_ot_cal,provisun_day,provisun_day_cal,provisun_day_ot,provisun_day_ot_cal," 
            "nightdiff_day,nightdiff_day_cal,adjustment,adjustment_cal,grosspay_save,salaryDetails_save,"
            "sss_save,phic_save,hmdf_save,sss_provi_save,total_mandatory,uniform_save,rice_save,laundry_save,"
            "medical1_save," 
            "medical2_save,totalDem_save,otherforms_save,taxable_amount,taxwitheld_save,cashadvance_save," 
            "sssloan_save,hdmfloan_save,netpay_save,"
            "userlog,time_update)" 
            " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

            (department, date1, empID, lastname,
             firstname, posittion, salRate_entry,  provicialRate, regday_save, regdaycal_save,
             regdayot_save, regdaycalOT_save, regsun_save, regsuncal_save, regsunOT_save, regsuncalOT_save,
             spl_save, splCal_save, splOT_save, splOTcal_save, legal_save, legalCal_save, legalOT_save, legalOTcal_save,
             shoprate_save, shoprateCal_save, proviRate_save, proviRateCal_save, proviRateOT_save,
             proviRateOTcal_save, proviRateSun_save, proviRateSunCal_save,proviSunRateOT_save,proviSunRateOTcal_save,
             nightdiff_save,nightdiffCal_save, adjustments_save, adjustmentCal_save, grosspay_save, salaryDetails_save,
             sss_save, phic_save, hdmf_save, provshare_save, totalMadatory_save, uniform_save, rice_save, laundry_save,
             medical1_save,
             medical2_save, totalDem_save,otherForms_save, taxable_amount_save, taxWithheld_save, ca_deduct_save,
             sss_loandeduct_save, hdmfdeduct_save, netPay_save,
             user_reg,
             date_time_update))
        # 58
        messagebox.showinfo('JRS','Data has been Save')


        mydb.commit()
        mydb.close()
        cursor.close()

def net_pay():
    """This funtion is for computaion of Net Pay"""
    mydb._open_connection()
    cursor = mydb.cursor()
    empID = empID_entry.get()
    global uniform
    global rice
    global laundry
    global medical1
    global medical2
    global totalDem
    global afterDem
    global otherForms
    global CalotherForms
    global taxable_amount
    global taxWithheld
    global netPay
    netPay = 0
    global salaryRate
    cursor.execute("SELECT employee_id, lastName, firstName, position, salary_rate, Salary_Detail\
                                     FROM employee_details where employee_id  = '" + empID + "' ")

    fetch = cursor.fetchall()
    salRate = 0
    uniform = 0
    rice = 0
    laundry = 0
    medical1 = 0
    medical2 = 0
    afterDem = 0
    otherForms = 0
    CalotherForms = 0
    taxable_amount = 0
    taxWithheld = 0
    totalMandatory =  totl_mandatory_entry.get()
    global details
    for data in fetch:
        uniform_entry.set = ''
        rice_entry.set = ''
        laundry_entry.set = ''
        medical1_entry.set = ''
        medical2_entry.set = ''

        salaryRate = float(data[4])
        detail = data[5]

        # uniform = uniform_entry.get()
        # rice =rice_entry.get()
        # laundry = laundry_entry.get()
        # medical1 = medical1_entry.get()
        # medical2 = medical2_entry.get()
        grossPay = grosspay
        details = salaDetails_entry.get()

        if details == 'Monthly':
            salRate = salaryRate / 2
        elif details == 'Daily':
            salRate = salaryRate * 13


        #salRate = salaryRate * 13
        basic_taxable = grosspay - mwe_monthly
        totalDem = 0


        if basic_taxable <=0:
            basic_taxable = 0
        else:
            basic_taxable = basic_taxable


        if salRate <= mwe_monthly and grossPay >= mwe_monthly:
            uniform = 0
            rice = 0
            laundry = 0
            medical1 = 0
            medical2 = 0
            otherForms = 0
            uniform_entry.delete(0, END)
            uniform_entry.insert(0, (uniform))

            rice_entry.delete(0, END)
            rice_entry.insert(0, (rice))

            laundry_entry.delete(0, END)
            laundry_entry.insert(0, (laundry))

            medical1_entry.delete(0, END)
            medical1_entry.insert(0, (medical1))

            medical2_entry.delete(0, END)
            medical2_entry.insert(0, (medical2))
            totalDem = uniform + rice + laundry + medical1 + medical2

        elif salRate <= mwe_monthly and grossPay <= mwe_monthly:
            uniform = 0
            rice = 0
            laundry = 0
            medical1 = 0
            medical2 = 0
            otherForms = 0
            uniform_entry.delete(0, END)
            uniform_entry.insert(0, (uniform))

            rice_entry.delete(0, END)
            rice_entry.insert(0, (rice))

            laundry_entry.delete(0, END)
            laundry_entry.insert(0, (laundry))

            medical1_entry.delete(0, END)
            medical1_entry.insert(0, (medical1))

            medical2_entry.delete(0, END)
            medical2_entry.insert(0, (medical2))
            totalDem = uniform + rice + laundry + medical1 + medical2




# this function is for calculation of Taxable but gross is less than Deminimis!!!
        elif salRate > mwe_monthly and grossPay <= mwe_monthly and grossPay <= total_deminimis and basic_taxable <= 0:

            uniform = grossPay * 0.13
            rice = grossPay * 0.52
            laundry = grossPay * 0.08
            medical1 = grossPay * 0.21
            medical2 = grossPay * 0.06

            uniform_entry.delete(0, END)
            uniform_entry.insert(0, (uniform))

            rice_entry.delete(0, END)
            rice_entry.insert(0, (rice))

            laundry_entry.delete(0, END)
            laundry_entry.insert(0, (laundry))

            medical1_entry.delete(0, END)
            medical1_entry.insert(0, (medical1))

            medical2_entry.delete(0, END)
            medical2_entry.insert(0, (medical2))
            totalDem = uniform + rice + laundry + medical1 + medical2

# this function is for computation of Total Demin Taxable and grosspay is greater than deminimis
        elif salRate > mwe_monthly and grossPay <= mwe_monthly and grossPay > total_deminimis and basic_taxable <= 0:

            uniform = total_deminimis * 0.13
            rice = total_deminimis * 0.52
            laundry = total_deminimis * 0.08
            medical1 = total_deminimis * 0.21
            medical2 = total_deminimis * 0.06

            uniform_entry.delete(0, END)
            uniform_entry.insert(0, (uniform))

            rice_entry.delete(0, END)
            rice_entry.insert(0, (rice))

            laundry_entry.delete(0, END)
            laundry_entry.insert(0, (laundry))

            medical1_entry.delete(0, END)
            medical1_entry.insert(0, (medical1))

            medical2_entry.delete(0, END)
            medical2_entry.insert(0, (medical2))
            totalDem = uniform + rice + laundry + medical1 + medical2

# this function is for Taxable with Gross Pay is greater than MWE
        elif salRate > mwe_monthly and basic_taxable > 0 and basic_taxable > total_deminimis:

            uniform = total_deminimis * 0.13
            rice = total_deminimis * 0.52
            laundry = total_deminimis * 0.08
            medical1 = total_deminimis * 0.21
            medical2 = total_deminimis * 0.06

            uniform_entry.delete(0, END)
            uniform_entry.insert(0, (uniform))

            rice_entry.delete(0, END)
            rice_entry.insert(0, (rice))

            laundry_entry.delete(0, END)
            laundry_entry.insert(0, (laundry))

            medical1_entry.delete(0, END)
            medical1_entry.insert(0, (medical1))

            medical2_entry.delete(0, END)
            medical2_entry.insert(0, (medical2))
            totalDem = uniform + rice + laundry + medical1 + medical2
# this function is Taxable with gross Pay is greater than MWE and Basic Taxable is less Than total Deminimis
        elif salRate > mwe_monthly and basic_taxable > 0 and basic_taxable <= total_deminimis:

            uniform = basic_taxable * 0.13
            rice = basic_taxable * 0.52
            laundry = basic_taxable * 0.08
            medical1 = basic_taxable * 0.21
            medical2 = basic_taxable * 0.06

            uniform_entry.delete(0, END)
            uniform_entry.insert(0, (uniform))

            rice_entry.delete(0, END)
            rice_entry.insert(0, (rice))

            laundry_entry.delete(0, END)
            laundry_entry.insert(0, (laundry))

            medical1_entry.delete(0, END)
            medical1_entry.insert(0, (medical1))

            medical2_entry.delete(0, END)
            medical2_entry.insert(0, (medical2))
            totalDem = uniform + rice + laundry + medical1 + medical2



        if grossPay > 0 and  salRate > mwe_monthly and basic_taxable <=0:
            afterDem = grossPay - totalDem
            taxable_amount = grossPay - totalDem - float(totalMandatory)
            #taxable_amount = grossPay - totalDem - afterDem - float(totalMandatory)
            if afterDem <=0:
                afterDem =0
            else:
                afterDem = afterDem
        elif grossPay > 0 and  salRate > mwe_monthly and basic_taxable > 0:
            afterDem = basic_taxable - totalDem
            taxable_amount = grossPay - totalDem - float(totalMandatory)
            #taxable_amount = grossPay - totalDem - afterDem - float(totalMandatory)
            if afterDem <= 0:
                afterDem = 0
            else:
                afterDem = afterDem


# this function is for computating  other Forms!!!!!!

        # if afterDem <= 0 and salRate <= mwe_monthly:
        #     otherForms = 0

        if afterDem >= 0 and salRate >= mwe_monthly:
            if salRate <= 15000 and salRate >= mwe_monthly :
                CalotherForms = ((90000 - (salRate * 2)) / 24)

                if afterDem <= CalotherForms:
                    otherForms = afterDem
                else:
                    otherForms = CalotherForms
            elif salRate > 15000 and salRate >= mwe_monthly:
                CalotherForms = (90000 -30000) / 24

                if afterDem <= CalotherForms:
                    otherForms = afterDem
                else:
                    otherForms = CalotherForms
        taxable_amount = taxable_amount - otherForms

        if taxable_amount > 0:
            cursor.execute("SELECT * FROM tax_table")
            query_result = cursor.fetchall()
            for row in query_result:

                amountFrom_tax = float(row[1]) / 2

                amountTo_tax = float(row[2]) / 2
                baseAmount_tax = float(row[3]) / 2
                percentage_tax = float(row[4])
                if taxable_amount >= amountFrom_tax and taxable_amount <= amountTo_tax:

                    taxbase = baseAmount_tax
                    cal = taxable_amount - amountFrom_tax
                    if cal <= 0:
                        cal = 0
                        taxWithheld = baseAmount_tax + (cal * percentage_tax)


                    else:
                        cal = cal
                        taxWithheld = baseAmount_tax + (cal * percentage_tax)

        else:
            taxWithheld = 0

    taxWithheld2 = '{:,.2f}'.format(taxWithheld)
    taxWitheld_entry.delete(0, END)
    taxWitheld_entry.insert(0, (taxWithheld2))


    totalDem = uniform + rice + laundry + medical1 + medical2
    totalDem2 = '{:,.2f}'.format(totalDem)
    totalDem_entry.delete(0, END)
    totalDem_entry.insert(0, (totalDem2))

    otherForms2 = '{:,.2f}'.format(otherForms)
    otherForms_entry.delete(0, END)
    otherForms_entry.insert(0, (otherForms2))





    netPay = grossPay - taxWithheld - totalMadatory - float(sss_loandeduct) - float(hdmfdeduct) - float(ca_deduct)
    netPay2 = '{:,.2f}'.format(netPay)
    netpay_entry.delete(0, END)
    netpay_entry.insert(0, (netPay2))

    
    

def sum_total_mandatory():
    """This function is for computation of Total Mandatory"""
    global totalMadatory
    sss3 = sss_entry.get()
    hdmf3 = hdmf_entry.get()
    phic3 = phic_entry.get()
    sss_prov3 = sssPro_entry.get()
    totalMadatory = float(sss3) + float(hdmf3) + float(phic3) + float(sss_prov3)
    totalMadatory2 = '{:.2f}'.format(totalMadatory)
    totl_mandatory_entry.delete(0, END)
    totl_mandatory_entry.insert(0, (totalMadatory2))


def govt_mandatory_comp():
    """This function is for computation of Govt Mandatory"""

    mydb._open_connection()
    cursor = mydb.cursor()
    global sss
    global hdmf
    global phic
    global provshare
    global sss_prov
    global hdmfdeduct
    global ca_deduct
    global sss_loandeduct

    check = checkvar1.get()

    details = salaDetails_entry.get()
    salary_base = salaryRate_entry.get()
    if details == 'Monthly':
        salary_base = float(salaryRate_entry.get())
    elif details == 'Daily':
        salary_base = float(salaryRate_entry.get()) * 26

    sss = float(0)
    hdmf = float(0)
    phic = float(0)
    provshare = float(0)
    empID = empID_entry.get()
    hdmfdeduct = 0
    sss_loandeduct = 0
    
    if check >= 1:
        cursor.execute("SELECT *\
                       FROM sss_table  ")

        fetch = cursor.fetchall()
        for data in fetch:
            amountFrom = float(data[1])
            amountto  = float(data[2])
            empshare = float(data[3])
            provshare = float(data[4])

            if salary_base < amountto and salary_base > amountFrom:
                sss = empshare
                sss2 = '{:,.2f}'.format(sss)
                sss_entry.delete(0, END)
                sss_entry.insert(0, (sss2))

            # this is for provident share computation
                sss_prov = provshare
                sss_prov2 = '{:,.2f}'.format(sss_prov)
                sssPro_entry.delete(0, END)
                sssPro_entry.insert(0, (sss_prov2))

        # for hdmf computation!!!!
        if salary_base > 0:
            hdmf = float(100)
            hdmf2 = '{:,.2f}'.format(hdmf)
            hdmf_entry.delete(0, END)
            hdmf_entry.insert(0, (hdmf2))

        if salary_base <= 10000:
            phic = 300 / 2
            phic2 = '{:,.2f}'.format(phic)
            phic_entry.delete(0, END)
            phic_entry.insert(0, (phic2))
        elif  salary_base < 60000 and salary_base > 10000:
            phic = salary_base * .03 / 2
            phic2 = '{:,.2f}'.format(phic)
            phic_entry.delete(0, END)
            phic_entry.insert(0, (phic2))
        elif salary_base >= 60000:
            phic = 1800
            phic2 = '{:,.2f}'.format(phic)
            phic_entry.delete(0, END)
            phic_entry.insert(0, (phic2))
        
        # this function is for getting the hdmf loan deduction
        cursor.execute("SELECT employee_id,loan_deduction\
                              FROM HDMF_loanDeduction\
                               WHERE employee_id ='" + empID + "'  \
                       ")

        fetch = cursor.fetchall()
        hdmfloan ={}
        hdmfdeduct = 0
        row_count = cursor.rowcount

        if row_count == 0:
            hdmfdeduct = 0
            hdmfdeduct2 = '{:,.2f}'.format(hdmfdeduct)
            hdmfLoan_entry.delete(0, END)
            hdmfLoan_entry.insert(0, (hdmfdeduct2))

        else:
            cursor.execute("SELECT employee_id,loan_deduction\
                              FROM HDMF_loanDeduction\
                               WHERE employee_id ='" + empID + "'  \
                       ")

            fetch = cursor.fetchall()
            

            for row in fetch:
                deduct = row[1]

                hdmfdeduct = deduct
                hdmfdeduct2 = '{:,.2f}'.format(hdmfdeduct)
                hdmfLoan_entry.delete(0, END)
                hdmfLoan_entry.insert(0, (hdmfdeduct2))
                
        # this function is for getting the sss loan deduction
        cursor.execute("SELECT employee_id,loan_deduction\
                              FROM sss_loanDeduction\
                               WHERE employee_id ='" + empID + "'  \
                       ")

        fetch = cursor.fetchall()
        row_count = cursor.rowcount

        if row_count == 0:
            sss_loandeduct = 0
            sss_loandeduct2 = '{:,.2f}'.format(sss_loandeduct)
            sssLoan_entry.delete(0, END)
            sssLoan_entry.insert(0, (sss_loandeduct2))

        else:
            cursor.execute("SELECT employee_id,loan_deduction\
                              FROM sss_loanDeduction\
                               WHERE employee_id ='" + empID + "'  \
                       ")

            fetch = cursor.fetchall()
            

            for row in fetch:
                deduct = row[1]

                sss_loandeduct = deduct
                sss_loandeduct2 = '{:,.2f}'.format(sss_loandeduct)
                sssLoan_entry.delete(0, END)
                sssLoan_entry.insert(0, (sss_loandeduct2))

        # this function is for getting the cash advance  deduction
        cursor.execute("SELECT employee_id,ca_deduction\
                              FROM cash_advance\
                               WHERE employee_id ='" + empID + "'  \
                       ")

        fetch = cursor.fetchall()
        row_count = cursor.rowcount

        if row_count == 0:
            ca_deduct = 0
            ca_deduct2 = '{:,.2f}'.format(ca_deduct)
            cashAdvance_entry.delete(0, END)
            cashAdvance_entry.insert(0, (ca_deduct2))

        else:
            cursor.execute("SELECT employee_id,ca_deduction\
                              FROM cash_advance\
                               WHERE employee_id ='" + empID + "'  \
                       ")

            fetch = cursor.fetchall()

            for row in fetch:
                deduct = row[1]

                ca_deduct = deduct
                ca_deduct2 = '{:,.2f}'.format(ca_deduct)
                cashAdvance_entry.delete(0, END)
                cashAdvance_entry.insert(0, (ca_deduct2))



    else:
        sss = 0
        sss2 = '{:,.2f}'.format(sss)
        sss_entry.delete(0, END)
        sss_entry.insert(0, (sss2))

        phic = 0
        phic2 = '{:,.2f}'.format(phic)
        phic_entry.delete(0, END)
        phic_entry.insert(0, (phic2))

        hdmf = 0
        hdmf2 = '{:,.2f}'.format(hdmf)
        hdmf_entry.delete(0, END)
        hdmf_entry.insert(0, (hdmf2))

        sss_prov = 0
        sss_prov2 = '{:,.2f}'.format(sss_prov)
        sssPro_entry.delete(0, END)
        sssPro_entry.insert(0, (sss_prov2))


        hdmfdeduct = 0
        hdmfdeduct2 = '{:,.2f}'.format(hdmfdeduct)
        hdmfLoan_entry.delete(0, END)
        hdmfLoan_entry.insert(0, (hdmfdeduct2))


        ca_deduct = 0
        ca_deduct2 = '{:,.2f}'.format(ca_deduct)
        cashAdvance_entry.delete(0, END)
        cashAdvance_entry.insert(0, (ca_deduct2))


        sss_loandeduct = 0
        sss_loandeduct2 = '{:,.2f}'.format(sss_loandeduct)
        sssLoan_entry.delete(0, END)
        sssLoan_entry.insert(0, (sss_loandeduct2))


def gross_computation():

    """This function is for computation of Gross"""

    global regday
    global regdaycal
    global regday2
    global regOT
    global regdaycalOT
    global regOT
    global regdaycalOT

    global spl
    global splCal
    global splOT
    global splOTcal
    global legal
    global legalCal
    global legalOT
    global legalOTcal
    global shoprate
    global shoprateCal
    global proviRate
    global proviRateCal
    global proviRateOT
    global proviRateOTcal
    global proviRateSun
    global proviRateSunCal
    global nightdiff
    global nightdiffCal
    global adjustments
    global adjustmentCal

    # this is for calculation of regday!!!
    regday = 0
    regdaycal =0
    details = salaDetails_entry.get()
    salary_rate_grossComp = salaryRate_entry.get()
    rateProvi = 378.50

    if details == 'Monthly':
        salary_rate_grossComp = float(salaryRate_entry.get()) / 26
    elif details == 'Daily':
        salary_rate_grossComp = salaryRate_entry.get()

    if regday_entry.get() =='':
        regday = 0
        regdayCal_entry.delete(0, END)
        regdayCal_entry.insert(0, (regday))
    else:
        regday = regday_entry.get()
        regdaycal = float(salary_rate_grossComp) * float(regday)
        regdaycal2 = '{:,.2f}'.format(regdaycal)
        regdayCal_entry.delete(0, END)
        regdayCal_entry.insert(0, (regdaycal2))

        regday2 = regdaycal

    # this is for calculation of regday Over Time!!!

    regOT = 0
    regdaycalOT = 0

    if regdayOT_entry.get() =='':
        regOT = 0
        regdayCalOT_entry.delete(0, END)
        regdayCalOT_entry.insert(0, (regOT))
    else:
        regOT = regdayOT_entry.get()
        regdaycalOT = float(regOT) * (float(salary_rate_grossComp) / 8 * 1.25)
        regdaycalOT2 = '{:,.2f}'.format(regdaycalOT)
        regdayCalOT_entry.delete(0, END)
        regdayCalOT_entry.insert(0, (regdaycalOT2))

    # this is for computaion of regsunday!!!
    global regsun
    global regsuncal
    regsun = 0
    regsuncal = 0
    if regsun_entry.get() == '':
        regsun = 0
        regsunCal_entry.delete(0, END)
        regsunCal_entry.insert(0, (regsun))
    else:
        regsun = regsun_entry.get()
        regsuncal = float(regsun) * (float(salary_rate_grossComp) * 1.30)
        regsuncal2 = '{:,.2f}'.format(regsuncal)
        regsunCal_entry.delete(0, END)
        regsunCal_entry.insert(0, (regsuncal2))

    # this is for calculation of regsunday  Over Time!!!
    global regsunOT
    global regsuncalOT
    regsunOT = 0
    regsuncalOT = 0
    if sunOT_entry.get() == '':
        regsuncalOT = 0
        sunOTCal_entry.delete(0, END)
        sunOTCal_entry.insert(0, (regsuncalOT))
    else:
        regsunOT = sunOT_entry.get()
        regsuncalOT = float(regsunOT) * (float(salary_rate_grossComp) / 8 * 1.69)
        regdaycalOT2 = '{:,.2f}'.format(regsuncalOT)
        sunOTCal_entry.delete(0, END)
        sunOTCal_entry.insert(0, (regdaycalOT2))

    # this is for computaion of Special Holiday!!!

    spl = float(0)
    splCal = 0
    if spl_entry.get() == '':
        splCal = float(0)
        splCal_entry.delete(0, END)
        splCal_entry.insert(0, (splCal))
    else:
        spl = spl_entry.get()
        splCal = float(spl) * (float(salary_rate_grossComp) * 1.30)
        splcal2 = '{:,.2f}'.format(splCal)
        splCal_entry.delete(0, END)
        splCal_entry.insert(0, (splcal2))

    # this is for calculation of Special Holiday  Over Time!!!

    splOT = float(0)
    splOTcal = float(0)
    if splOT_entry.get() == '':
        splOTcal = float(0)
        splOTCal_entry.delete(0, END)
        splOTCal_entry.insert(0, (splOTcal))
    else:
        spltOT = splOT_entry.get()
        splOTcal = float(spltOT) * (float(salary_rate_grossComp) / 8 * 1.69)
        splOTcal2 = '{:,.2f}'.format(splOTcal)
        splOTCal_entry.delete(0, END)
        splOTCal_entry.insert(0, (splOTcal2))

    # this is for computaion of Legal Holiday!!!

    legal = float(0)
    legalCal = float(0)
    if legal_entry.get() == '':
        legalCal = float(0)
        legalCal_entry.delete(0, END)
        legalCal_entry.insert(0, (legalCal))
    else:
        legal = legal_entry.get()
        legalCal = float(legal) * (float(salary_rate_grossComp) * 2)
        legalCal2 = '{:,.2f}'.format(legalCal)
        legalCal_entry.delete(0, END)
        legalCal_entry.insert(0, (legalCal2))

    # this is for calculation of Legal Holiday  Over Time!!!

    legalOT = float(0)
    legalOTcal = float(0)
    if legalOT_entry.get() == '':
        legalOTcal = float(0)
        legalOTCal_entry.delete(0, END)
        legalOTCal_entry.insert(0, (legalOTcal))
    else:
        legalOT = legalOT_entry.get()
        legalOTcal = float(legalOT) * (float(salary_rate_grossComp) / 8) * 2 * (1.30)
        legalOTcal2 = '{:,.2f}'.format(legalOTcal)
        legalOTCal_entry.delete(0, END)
        legalOTCal_entry.insert(0, (legalOTcal2))

    # this is for computaion of Shop Rate!!!

    shoprate = float(0)
    shoprateCal = float(0)
    if shopRate_entry.get() == '':
        shoprateCal = float(0)
        shopRateCal_entry.delete(0, END)
        shopRateCal_entry.insert(0, (shoprateCal))
    else:
        shoprate = shopRate_entry.get()
        shoprateCal = float(shoprate) * (float(salary_rate_grossComp) / 2)
        shoprateCal2 = '{:,.2f}'.format(shoprateCal)
        shopRateCal_entry.delete(0, END)
        shopRateCal_entry.insert(0, (shoprateCal2))

    # this is for computaion of Provicial Rate!!!

    proviRate = float(0)
    proviRateCal = float(0)
    if proviRate_entry.get() == '':
        proviRateCal = float(0)
        proviRateCal_entry.delete(0, END)
        proviRateCal_entry.insert(0, (proviRateCal))
    else:
        proviRate = proviRate_entry.get()
        proviRateCal = float(proviRate) * (rateProvi)
        proviRateCal2 = '{:,.2f}'.format(proviRateCal)
        proviRateCal_entry.delete(0, END)
        proviRateCal_entry.insert(0, (proviRateCal2))

    # this is for calculation of ProviRate  Over Time!!!

    proviRateOT = float(0)
    proviRateOTcal = float(0)
    if  proviOT_entry.get() == '':
        proviRateOTcal = float(0)
        proviOTCal_entry.delete(0, END)
        proviOTCal_entry.insert(0, (proviRateOTcal))
    else:
        proviRateOT = proviOT_entry.get()
        proviRateOTcal = float(proviRateOT) * (rateProvi / 8 * 1.25)
        proviRateOTcal2 = '{:,.2f}'.format(proviRateOTcal)
        proviOTCal_entry.delete(0, END)
        proviOTCal_entry.insert(0, (proviRateOTcal2))

    # this is for computaion of ProvicialSunday Rate!!!

    proviRateSun = float(0)
    proviRateSunCal = float(0)
    if proviSun_entry.get() == '':
        proviRateSunCal = float(0)
        proviSunCal_entry.delete(0, END)
        proviSunCal_entry.insert(0, (proviRateSunCal))
    else:
        proviRateSun = proviSun_entry.get()
        proviRateSunCal = float(proviRateSun) * (rateProvi * 1.30)
        proviRateSunCal2 = '{:,.2f}'.format(proviRateSunCal)
        proviSunCal_entry.delete(0, END)
        proviSunCal_entry.insert(0, (proviRateSunCal2))

    # this is for calculation of ProviRateSunday Over Time!!!
    global proviSunRateOT
    global proviSunRateOTcal
    proviSunRateOT = float(0)
    proviSunRateOTcal = float(0)
    if  proviSunOT_entry.get() == '':
        proviSunRateOTcal = float(0)
        proviSunOTCal_entry.delete(0, END)
        proviSunOTCal_entry.insert(0, (proviSunRateOTcal))
    else:
        proviSunRateOT = proviSunOT_entry.get()
        proviSunRateOTcal = float(proviSunRateOT) * (rateProvi / 8 * 1.25)
        proviSunRateOTcal2 = '{:,.2f}'.format(proviSunRateOTcal)
        proviSunOTCal_entry.delete(0, END)
        proviSunOTCal_entry.insert(0, (proviSunRateOTcal2))

    # this is for computaion of Night Diff !!!

    nightdiff = float(0)
    nightdiffCal = float(0)
    if nightdiff_entry.get() == '':
        nightdiffCal = float(0)
        nightdiffCal_entry.delete(0, END)
        nightdiffCal_entry.insert(0, (proviRateSunCal))
    else:
        nightdiff = nightdiff_entry.get()
        nightdiffCal = float(nightdiff) * (float(salary_rate_grossComp) / 8 * 0.10)
        nightdiffCal2 = '{:,.2f}'.format(nightdiffCal)
        nightdiffCal_entry.delete(0, END)
        nightdiffCal_entry.insert(0, (nightdiffCal2))



    # # this is for computaion of adjustment !!!
    global adjustments
    global adjustmentCal
    adjustments = float(0)
    adjustmentCal = float(0)
    if adjustment_entry.get() == '':
        adjustmentCal = float(0)
        adjustmentCal_entry.delete(0, END)
        adjustmentCal_entry.insert(0, (adjustmentCal))
    else:
        v = 1
        adjustments = adjustment_entry.get()
        adjustmentCal = float(adjustments) * v
        adjustmentCal2 = '{:,.2f}'.format(adjustmentCal)
        adjustmentCal_entry.delete(0, END)
        adjustmentCal_entry.insert(0, (adjustmentCal2))




    global grosspay
    grosspay = (regdaycal + regdaycalOT + regsuncal + regsuncalOT + splCal +
                splOTcal + legalCal + legalOTcal + shoprateCal + proviRateCal +
                proviRateOTcal + proviRateSunCal + proviSunRateOTcal + nightdiffCal + adjustmentCal)
    grosspay2 ='{:,.2f}'.format(grosspay)
    gross_pay_entry.delete(0, END)
    gross_pay_entry.insert(0, (grosspay2))

    govt_mandatory_comp()






def searchEmployee_details():
    """This function is to search Employee Through employee ID"""
    mydb._open_connection()
    cursor = mydb.cursor()
    empID = empID_entry.get()
    global mwe
    cursor.execute("SELECT employee_id, lastName, firstName, position, salary_rate\
              FROM employee_details where employee_id  = '" + empID + "' ")

    fetch = cursor.fetchall()
    mwe = float(420)
    row_count = cursor.rowcount

    if empID=='':
        messagebox.showinfo('JRS', 'Empty fields')
    elif row_count == 0: # this is to query an empty field for mysql
        messagebox.showinfo('JRS', 'No records Found')
        lastname_entry.delete(0, END)
        firstname_entry.delete(0, END)
        position_entry.delete(0, END)
        salaryRate_entry.delete(0, END)
        provincialRate_entry.delete(0, END)
    else:
        cursor.execute("SELECT employee_id, lastName, firstName, position, salary_rate, Salary_Detail\
                                  FROM employee_details where employee_id  = '" + empID + "' ")

        fetch = cursor.fetchall()
        mwe = float(420)
        for data in fetch:

            id_num = data[0]
            lname = data[1]
            fname = data[2]
            post = data[3]
            salaryRate = float(data[4])
            details   = data[5]

            lastname_entry.delete(0, END)
            lastname_entry.insert(0, (lname))

            firstname_entry.delete(0, END)
            firstname_entry.insert(0, (fname))

            position_entry.delete(0, END)
            position_entry.insert(0, (post))

            salaryRate_entry.delete(0, END)
            salaryRate_entry.insert(0, (salaryRate))

            provincialRate_entry.delete(0, END)
            provincialRate_entry.insert(0, (mwe))

            salaDetails_entry.delete(0, END)
            salaDetails_entry.insert(0, (details))




def payrollComputation_module():
    clearpayrollFrame()
    global empID_entry
    global lastname_entry
    global firstname_entry
    global position_entry

    global provincialRate_entry
    global payCal_date
    global salaryRate_entry
    global regday_entry

    global regdayCal_entry
    global regdayOT_entry
    global regdayCalOT_entry
    global checkbutton1
    global checkvar1





    checkvar1 = IntVar()
    checkbutton1 = Checkbutton(payroll_frame, text ="With GovtMandatory", variable = checkvar1,\
                               onvalue = 1, offvalue = 0, height = 1, width = 15)
    checkbutton1.place(x =10,y=5)
    global department_list
    department_list_label = Label(payroll_frame, text='Department:', width=13, height=1, bg='yellow', fg='gray',
                              font=('Arial', 10), anchor='e')
    department_list_label.place(x=150, y=5)

    department_list = ttk.Combobox(payroll_frame, width=20)
    department_list['values'] = ("Head Office", "Admin-Site", "Pampanga", "Rizal-R&F")
    department_list.place(x=285, y=5)

    payCal_date_label = Label(payroll_frame, text='Date:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    payCal_date_label.place(x=10, y=35)

    payCal_date = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    payCal_date.place(x=120, y=35)
    payCal_date.configure(justify='center')

    employeeid_no = Label(payroll_frame, text='Employee ID:', width=10, height=1, bg='yellow', fg='gray',
                        font=('Arial', 10), anchor='e')
    employeeid_no.place(x=10, y=60)

    empID_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    empID_entry.place(x=120, y=60)


    lastname_label = Label(payroll_frame, text='Last Name:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    lastname_label.place(x=10, y=85)

    lastname_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    lastname_entry.place(x=120, y=85)

    firstname_label = Label(payroll_frame, text='First Name:', width=10, height=1, bg='yellow', fg='gray',
                           font=('Arial', 10), anchor='e')
    firstname_label.place(x=10, y=110)

    firstname_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    firstname_entry.place(x=120, y=110)

    position_label = Label(payroll_frame, text='Position:', width=10, height=1, bg='yellow', fg='gray',
                            font=('Arial', 10), anchor='e')
    position_label.place(x=10, y=135)

    position_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    position_entry.place(x=120, y=135)

    salaryRate_label = Label(payroll_frame, text='Salary Rate:', width=10, height=1, bg='yellow', fg='gray',
                           font=('Arial', 10), anchor='e')
    salaryRate_label.place(x=10, y=160)
    # var1 = DoubleVar()
    # var2 = DoubleVar()
    # var3 = DoubleVar

    salaryRate_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    salaryRate_entry.place(x=120, y=160)

    provicialRate_label = Label(payroll_frame, text='Provincial Rate:', width=10, height=1, bg='yellow', fg='gray',
                             font=('Arial', 10), anchor='e')
    provicialRate_label.place(x=10, y=185)

    provincialRate_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    provincialRate_entry.place(x=120, y=185)

    regday_label = Label(payroll_frame, text='Regular Dar:', width=10, height=1, bg='yellow', fg='gray',
                                font=('Arial', 10), anchor='e')
    regday_label.place(x=10, y=210)

    regday_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    regday_entry.place(x=120, y=210)



    regdayCal_entry = Entry(payroll_frame,width=10, font=('Arial', 10), justify='right')
    regdayCal_entry.place(x=200, y=210)

    regdayOT_label = Label(payroll_frame, text='Regular OT:', width=10, height=1, bg='yellow', fg='gray',
                         font=('Arial', 10), anchor='e')
    regdayOT_label.place(x=10, y=235)

    regdayOT_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    regdayOT_entry.place(x=120, y=235)

    regdayCalOT_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    regdayCalOT_entry.place(x=200, y=235)
    global regsun_entry
    regsun_label = Label(payroll_frame, text='Regular Sun:', width=10, height=1, bg='yellow', fg='gray',
                         font=('Arial', 10), anchor='e')
    regsun_label.place(x=10, y=260)

    regsun_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    regsun_entry.place(x=120, y=260)
    global  regsunCal_entry
    regsunCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    regsunCal_entry.place(x=200, y=260)

    sunOT_label = Label(payroll_frame, text='Sunday OT:', width=10, height=1, bg='yellow', fg='gray',
                         font=('Arial', 10), anchor='e')
    sunOT_label.place(x=10, y=285)
    global sunOT_entry
    sunOT_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    sunOT_entry.place(x=120, y=285)
    global sunOTCal_entry
    sunOTCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    sunOTCal_entry.place(x=200, y=285)

    spl_label = Label(payroll_frame, text='Special Holiday:', width=10, height=1, bg='yellow', fg='gray',
                         font=('Arial', 10), anchor='e')
    spl_label.place(x=10, y=310)

    global spl_entry
    spl_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    spl_entry.place(x=120, y=310)

    global splCal_entry
    splCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    splCal_entry.place(x=200, y=310)

    splOT_label = Label(payroll_frame, text='Special OT:', width=10, height=1, bg='yellow', fg='gray',
                      font=('Arial', 10), anchor='e')
    splOT_label.place(x=10, y=335)

    global splOT_entry
    splOT_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    splOT_entry.place(x=120, y=335)

    global splOTCal_entry
    splOTCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    splOTCal_entry.place(x=200, y=335)

    legal_label = Label(payroll_frame, text='Legal Holiday:', width=10, height=1, bg='yellow', fg='gray',
                      font=('Arial', 10), anchor='e')
    legal_label.place(x=340, y=60)

    global legal_entry
    legal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    legal_entry.place(x=430, y=60)

    global legalCal_entry
    legalCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    legalCal_entry.place(x=510, y=60)

    legalOT_label = Label(payroll_frame, text='Legal OT:', width=10, height=1, bg='yellow', fg='gray',
                        font=('Arial', 10), anchor='e')
    legalOT_label.place(x=340, y=85)

    global legalOT_entry
    legalOT_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    legalOT_entry.place(x=430, y=85)

    global legalOTCal_entry
    legalOTCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    legalOTCal_entry.place(x=510, y=85)

    shopRate_label = Label(payroll_frame, text='Shop Rate:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    shopRate_label.place(x=340, y=110)

    global shopRate_entry
    shopRate_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    shopRate_entry.place(x=430, y=110)

    global shopRateCal_entry
    shopRateCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    shopRateCal_entry.place(x=510, y=110)

    proviRate_label = Label(payroll_frame, text='Provi Rate:', width=10, height=1, bg='yellow', fg='gray',
                           font=('Arial', 10), anchor='e')
    proviRate_label.place(x=340, y=135)

    global proviRate_entry
    proviRate_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    proviRate_entry.place(x=430, y=135)

    global proviRateCal_entry
    proviRateCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    proviRateCal_entry.place(x=510, y=135)

    proviOT_label = Label(payroll_frame, text='Provi OT:', width=10, height=1, bg='yellow', fg='gray',
                            font=('Arial', 10), anchor='e')
    proviOT_label.place(x=340, y=160)

    global proviOT_entry
    proviOT_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    proviOT_entry.place(x=430, y=160)

    global proviOTCal_entry
    proviOTCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    proviOTCal_entry.place(x=510, y=160)

    proviSun_label = Label(payroll_frame, text='Provi Sunday:', width=10, height=1, bg='yellow', fg='gray',
                            font=('Arial', 10), anchor='e')
    proviSun_label.place(x=340, y=185)

    global proviSun_entry
    proviSun_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    proviSun_entry.place(x=430, y=185)

    global proviSunCal_entry
    proviSunCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    proviSunCal_entry.place(x=510, y=185)

    proviSunOT_label = Label(payroll_frame, text='ProviSun OT:', width=10, height=1, bg='yellow', fg='gray',
                           font=('Arial', 10), anchor='e')
    proviSunOT_label.place(x=340, y=210)

    global proviSunOT_entry
    proviSunOT_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    proviSunOT_entry.place(x=430, y=210)

    global proviSunOTCal_entry
    proviSunOTCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    proviSunOTCal_entry.place(x=510, y=210)

    nightdiff_label = Label(payroll_frame, text='Night Diff:', width=10, height=1, bg='yellow', fg='gray',
                             font=('Arial', 10), anchor='e')
    nightdiff_label.place(x=340, y=235)

    global nightdiff_entry
    nightdiff_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    nightdiff_entry.place(x=430, y=235)

    global nightdiffCal_entry
    nightdiffCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    nightdiffCal_entry.place(x=510, y=235)

    adjustment_label = Label(payroll_frame, text='Adjustment:', width=10, height=1, bg='yellow', fg='gray',
                            font=('Arial', 10), anchor='e')
    adjustment_label.place(x=340, y=260)

    global adjustment_entry
    adjustment_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    adjustment_entry.place(x=430, y=260)

    global adjustmentCal_entry
    adjustmentCal_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    adjustmentCal_entry.place(x=510, y=260)

    salaDetails_label = Label(payroll_frame, text='Salary Details:', width=11, height=1, bg='yellow', fg='gray',
                             font=('Arial', 10), anchor='e')
    salaDetails_label.place(x=340, y=313)

    global salaDetails_entry
    salaDetails_entry = Entry(payroll_frame, width=13, font=('Arial', 10), justify='right')
    salaDetails_entry.place(x=440, y=313)



#=========================================this is for Gross Pay Computaion=========================================

    gross_pay_label = Label(payroll_frame, text='Gross Pay:', width=10, height=1, bg='Red', fg='white',
                            font=('Arial', 10), anchor='e')
    gross_pay_label.place(x=290, y=285)

    global gross_pay_entry
    gross_pay_entry = Entry(payroll_frame, width=12,bg='white',fg='red', font=('Arial', 10), justify='right')
    gross_pay_entry.place(x=380, y=285)

#=========================================for Goverment Mandatory Fields===============================================
    sss_label = Label(payroll_frame, text='SSS:', width=10, height=1, bg='yellow', fg='gray',
                             font=('Arial', 10), anchor='e')
    sss_label.place(x=595, y=60)

    global sss_entry
    sss_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    sss_entry.place(x=685, y=60)

    phic_label = Label(payroll_frame, text='PHIC:', width=10, height=1, bg='yellow', fg='gray',
                      font=('Arial', 10), anchor='e')
    phic_label.place(x=595, y=85)

    global phic_entry
    phic_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    phic_entry.place(x=685, y=85)

    hdmf_label = Label(payroll_frame, text='HDMF:', width=10, height=1, bg='yellow', fg='gray',
                       font=('Arial', 10), anchor='e')
    hdmf_label.place(x=595, y=110)

    global hdmf_entry
    hdmf_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    hdmf_entry.place(x=685, y=110)

    sssPro_label = Label(payroll_frame, text='SSS Provi:', width=10, height=1, bg='yellow', fg='gray',
                       font=('Arial', 10), anchor='e')
    sssPro_label.place(x=595, y=135)

    global sssPro_entry
    sssPro_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    sssPro_entry.place(x=685, y=135)

    totl_mandatory_label = Label(payroll_frame, text='Total Mand:', width=10, height=1, bg='yellow', fg='gray',
                         font=('Arial', 10), anchor='e')
    totl_mandatory_label.place(x=595, y=160)

    global totl_mandatory_entry
    totl_mandatory_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right',fg='red')
    totl_mandatory_entry.place(x=685, y=160)

# ===================================This is for Deminimis Label & Fields========================================
    uniform_label = Label(payroll_frame, text='Uniform:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    uniform_label.place(x=770, y=8)

    global uniform_entry
    uniform_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    uniform_entry.place(x=860, y=8)

    rice_label = Label(payroll_frame, text='Rice:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    rice_label.place(x=770, y=33)

    global rice_entry
    rice_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    rice_entry.place(x=860, y=33)

    laundry_label = Label(payroll_frame, text='Laundry:', width=10, height=1, bg='yellow', fg='gray',
                       font=('Arial', 10), anchor='e')
    laundry_label.place(x=770, y=58)

    global laundry_entry
    laundry_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    laundry_entry.place(x=860, y=58)

    medical1_label = Label(payroll_frame, text='Medical 1:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    medical1_label.place(x=770, y=83)

    global medical1_entry
    medical1_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    medical1_entry.place(x=860, y=83)

    medical2_label = Label(payroll_frame, text='Medical 2:', width=10, height=1, bg='yellow', fg='gray',
                           font=('Arial', 10), anchor='e')
    medical2_label.place(x=770, y=108)

    global medical2_entry
    medical2_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    medical2_entry.place(x=860, y=108)

    totalDem_label = Label(payroll_frame, text='Total Dem:', width=10, height=1, bg='red', fg='white',
                           font=('Arial', 10), anchor='e')
    totalDem_label.place(x=770, y=133)

    global totalDem_entry
    totalDem_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right', fg='red')
    totalDem_entry.place(x=860, y=133)
#=======================================This Fields is for Other Forms and Taxwithdhel=============================+
    otherForms_label = Label(payroll_frame, text='Other Forms:', width=10, height=1, bg='yellow', fg='gray',
                           font=('Arial', 10), anchor='e')
    otherForms_label.place(x=770, y=158)

    global otherForms_entry
    otherForms_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right', fg='red')
    otherForms_entry.place(x=860, y=158)

    taxWitheld_label = Label(payroll_frame, text='Tax Witheld:', width=10, height=1, bg='yellow', fg='gray',
                             font=('Arial', 10), anchor='e')
    taxWitheld_label.place(x=770, y=183)

    global taxWitheld_entry
    taxWitheld_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right', fg='red')
    taxWitheld_entry.place(x=860, y=183)

#===========================================This fields is for Deduction===============================================
    cashAdvance_label = Label(payroll_frame, text='Cash Advance:', width=12, height=1, bg='yellow', fg='gray',
                             font=('Arial', 9), anchor='e')
    cashAdvance_label.place(x=768, y=208)

    global cashAdvance_entry
    cashAdvance_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right', fg='red')
    cashAdvance_entry.place(x=860, y=208)

    sssLoan_label = Label(payroll_frame, text='SSS loan:', width=10, height=1, bg='yellow', fg='gray',
                              font=('Arial', 10), anchor='e')
    sssLoan_label.place(x=770, y=233)

    global sssLoan_entry
    sssLoan_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right', fg='red')
    sssLoan_entry.place(x=860, y=233)

    hdmfLoan_label = Label(payroll_frame, text='HDMF loan:', width=10, height=1, bg='yellow', fg='gray',
                          font=('Arial', 10), anchor='e')
    hdmfLoan_label.place(x=770, y=258)

    global  hdmfLoan_entry
    hdmfLoan_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right', fg='red')
    hdmfLoan_entry.place(x=860, y=258)
    
#====================================================Net Pay =========================================================
    netpay_label = Label(payroll_frame, text='Net Pay:', width=10, height=1, bg='yellow', fg='gray',
                           font=('Arial', 10), anchor='e')
    netpay_label.place(x=770, y=283)

    global netpay_entry
    netpay_entry = Entry(payroll_frame, width=10, font=('Arial', 11), justify='right', fg='white',bg='red')
    netpay_entry.place(x=860, y=283)
#===========================================================Button for Net Pay=======================================
    btn_netpay = Button(payroll_frame, text="Net Pay Cal", bg='gray', fg='yellow', font=('arial', 9),
                                width=12, command= net_pay)
    btn_netpay.place(x=760, y=310)
    btn_netpay.bind('<Return>', net_pay)
# =======================================Button for Total Mandatory===================================================
    btn_totalMandatory = Button(payroll_frame, text="Total Mandatory", bg='gray', fg='yellow', font=('arial', 9),
                        width=12,command=sum_total_mandatory)
    btn_totalMandatory.place(x=595, y=185)
    btn_totalMandatory.bind('<Return>', sum_total_mandatory)


#"""This button is for autocomplete of fields from employee ID selections with function def searchEmployee_details()"""
    btn_Search = Button(payroll_frame, text="Go", bg='yellow', fg='gray', font=('arial', 9), width=6,
                                command=searchEmployee_details)
    btn_Search.place(x=279, y=60)
    btn_Search.bind('<Return>', searchEmployee_details)

#"""This button is for Salary Computation with function def!!!!"""

    btn_salaryComp = Button(payroll_frame, text="CalCulate Gross", bg='green', fg='white', font=('arial', 9), width=15,
                        command=gross_computation)
    btn_salaryComp.place(x=477, y=285)
    btn_salaryComp.bind('<Return>', gross_computation)

    btn_saveComp = Button(payroll_frame, text="Save", bg='yellowgreen', fg='black', font=('arial', 9), width=15,
                            command=save_payroll)
    btn_saveComp.place(x=990, y=40)
    btn_saveComp.bind('<Return>', save_payroll)

    btn_printPayroll = Button(payroll_frame, text="Print Payroll", bg='white', fg='red', font=('arial', 9), width=15,
                          command=print_payroll)
    btn_printPayroll.place(x=990, y=80)
    btn_printPayroll.bind('<Return>', print_payroll)




#============================================This Function is for Cut-of Period========================================
def cut_off_listbox():

    cut_off_listbox = tk.Listbox(payroll_frame,
                                  width=65, height=15, bg='darkblue', fg='white', font=('courier', 10))
    cut_off_listbox.place(x=300, y=250)
    cursor.execute("Select datefrom,dateto,\
                        payrollDate\
                      FROM cut_off ")

    myresult = cursor.fetchall()

    cut_offDate = {}

    for row in myresult:


        data = {
            'datefr': row[0],
            'dateTo': row[1],
            'paydate': row[2],

        }
        cut_offDate.update(data)

        datefr = str(cut_offDate['datefr'])
        dateto = str(cut_offDate['dateTo'])
        paydate = str(cut_offDate['paydate'])


        empstore = " "'Date From:' " " + datefr + " " "Date To: " + \
                   dateto + " " "'Pay Date:' "    + paydate


        cut_off_listbox.insert(END, (empstore))


def edit_cut_off():
    """This function is to edit Cut-off Date"""
    dateFrom = cut_offDate_from.get()
    dateTo = cut_offDate_to.get()
    payrlldate = payrollDate.get()
    idTrans = '1'
    cursor.execute(
        "UPDATE cut_off SET datefrom='" + dateFrom + "',dateto='" + dateTo + "',payrollDate='" + payrlldate + "'\
           WHERE id LIKE %s",
        ('%' + idTrans + '%',))
    mydb.commit()
    mydb.close()
    messagebox.showinfo('JMFS PRO System', 'Data has been Updated')

def save_cut_off_period():
    """This function is to save cut-off Period"""
    mydb._open_connection()
    cursor = mydb.cursor()
    dateFrom = cut_offDate_from.get()
    dateTo = cut_offDate_to.get()
    payrlldate = payrollDate.get()

    cursor.execute(
        "INSERT INTO cut_off (datefrom,dateto,payrollDate)"
        "VALUES(%s,%s,%s)",
        (dateFrom,dateTo,payrlldate))

    mydb.commit()
    mydb.close()
    cursor.close()
    messagebox.showinfo('Red Boulders System', 'Data has been saved')

def cut_off_period():

    clearpayrollFrame()
    cut_off_listbox()
    global cut_offDate_from
    global cut_offDate_to
    global payrollDate
    cut_offDate_from_label = Label(payroll_frame, text='Date From:', width=13, height=1, bg='yellow', fg='gray',
                              font=('Arial', 11), anchor='e')
    cut_offDate_from_label.place(x=400, y=100)

    cut_offDate_from = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                            foreground='white', borderwidth=2, padx=10, pady=10)
    cut_offDate_from.place(x=530, y=100)
    cut_offDate_from.configure(justify='center')

    cut_offDate_to_label = Label(payroll_frame, text='Date To:', width=13, height=1, bg='yellow', fg='gray',
                              font=('Arial', 11), anchor='e')
    cut_offDate_to_label.place(x=400, y=130)

    cut_offDate_to = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                            foreground='white', borderwidth=2, padx=10, pady=10)
    cut_offDate_to.place(x=530, y=130)
    cut_offDate_to.configure(justify='center')

    payrollDate_label = Label(payroll_frame, text='Payroll Date:', width=13, height=1, bg='yellow', fg='gray',
                                 font=('Arial', 11), anchor='e')
    payrollDate_label.place(x=400, y=160)

    payrollDate = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                               foreground='white', borderwidth=2, padx=10, pady=10)
    payrollDate.place(x=530, y=160)
    payrollDate.configure(justify='center')

    btn_cut_off_Save = Button(payroll_frame, text="Save", bg='green', fg='white', font=('arial', 10), width=10,
                              command=save_cut_off_period)
    btn_cut_off_Save.place(x=430, y=190)
    btn_cut_off_Save.bind('<Return>', save_cut_off_period)

    btn_cut_off_update = Button(payroll_frame, text="Update", bg='yellow', fg='gray', font=('arial', 10), width=10,
                              command= edit_cut_off)
    btn_cut_off_update.place(x=550, y=190)
    btn_cut_off_update.bind('<Return>', edit_cut_off)
#==============================================Frame for Payroll Details=============================================
def insert_listbox():
    mydb._open_connection()
    cursor = mydb.cursor()
    typed = searchlist_entry.get()
    employee_listbox = tk.Listbox(payroll_frame,
                                  width=57, height=29, bg='darkblue', fg='white', font=('courier', 10))
    employee_listbox.place(x=650, y=70)
    cursor.execute("Select employee_id,lastName,firstName,\
                    salary_rate, taxCode\
                  FROM employee_details where lastName LIKE %s", ('%' + typed + '%',))

    myresult = cursor.fetchall()
    cnt = 0
    employee = {}

    for row in myresult:
        cnt += 1
        # empID = row[0]
        # lname = row[1]
        # fname =  row[2]
        # salarate = str(row[3])
        # taxcode =  row[4]

        data = {
            'empid': row[0],
            'lastname': row[1],
            'firstname': row[2],
            'salaryrate': row[3],
            'taxcode': row[4],
            'count': cnt
        }
        employee.update(data)

        count1 = str(employee['count'])
        empsid = employee['empid']
        lname = employee['lastname']
        fname = employee['firstname']
        salarate = str(employee['salaryrate'])
        taxcode = employee['taxcode']

        empstore = (count1) + " " " " + empsid + " " " " + lname + " " " "  " " " " + fname + " " " " " " " " + salarate + " " " " + taxcode

        employee_listbox.insert(END, (empstore))

def employee_update():
    """This function is to Edit employee Registry"""
    ts = time.time()
    mydb._open_connection()
    cursor = mydb.cursor()
    user_name = userName_entry.get()
    update_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    empid_update = employee_id_entry.get()
    lname_update = lastName_reg_entry.get()
    fname_update = firstName_reg_entry.get()
    mname_update =  middleName_reg_entry.get()
    gender_update = gender_description.get()
    address_update = address_reg_entry.get('1.0', 'end-1c')
    contNum_update = contactNum_reg_entry.get()
    empStatus_update = emp_status_reg_entry.get()
    department_update = department_reg_entry.get()
    position_update = position_reg_entry.get()

    try:
        if employee_id_entry.get()== "":
            messagebox.showerror("Error", "Employee ID fields  Must be required")
        else:
            cursor.execute(
                "UPDATE employee_details SET employee_id ='"+empid_update+"', \
                lastName='"+lname_update+"',\
                firstName='"+fname_update+"',\
                middleName='"+mname_update+"',\
                gender='"+gender_update+"',\
                address_employee='"+address_update+"',\
                contactNumber='" + contNum_update + "',\
                employment_status='" + empStatus_update + "',\
                department='" + department_update + "',\
                position='" + position_update + "'\
                WHERE employee_id =%s", (employee_id_entry.get(),)
            )
            mydb.commit()
            mydb.close()
            cursor.close()
            messagebox.showinfo('JRS', 'Data has been updated')

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")


def search_employee_reg():
    """This Function is for searching employee by employee ID Number to register in fields"""
    mydb._open_connection()
    cursor = mydb.cursor()
    btn_save_employeeDetails["state"] = DISABLED
    try:
        if searchEmpID_reg_entry.get() == "":
            messagebox.showerror("Error", "search field  Must be required")
        else:
            cursor.execute('Select * from employee_details WHERE employee_id = %s',
                           (searchEmpID_reg_entry.get(),))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "No record found")
            else:
                cursor.execute('Select * from employee_details WHERE employee_id = %s',
                               (searchEmpID_reg_entry.get(),))
                myresult = cursor.fetchall()

                for row in myresult:
                    empid = row[1]
                    lastname = row[2]
                    fname_sch = row[3]
                    mname_sch = row[4]
                    gender_sch = row[5]
                    address_sch = row[6]
                    cont_num0sch = row[7]
                    cont_per_sch = row[8]
                    emr_per_sch = row[9]
                    posistion_sch = row[10]
                    date_hire_sch = row[11]
                    department_sch = row[12]
                    eoc_sch = row[13]
                    tin_sch =row[14]
                    sss_sch = row[15]
                    phic_sch = row[16]
                    hdmf_sch = row[17]
                    emp_status_sch = row[18]
                    update_cont_sch = row[19]
                    salaryRate_sch = row[20]
                    tax_code_sch = row[21]
                    salaryDetails_sch = row[22]



                    employee_id_entry.delete(0, END)
                    employee_id_entry.insert(0, (empid))

                    lastName_reg_entry.delete(0, END)
                    lastName_reg_entry.insert(0, (lastname))

                    firstName_reg_entry.delete(0, END)
                    firstName_reg_entry.insert(0, (fname_sch))

                    middleName_reg_entry.delete(0, END)
                    middleName_reg_entry.insert(0, (mname_sch))

                    gender_description.delete(0, END)
                    gender_description.insert(0, (gender_sch))

                    address_reg_entry.delete('1.0', END)
                    address_reg_entry.insert('1.0', (address_sch))

                    contactNum_reg_entry.delete(0, END)
                    contactNum_reg_entry.insert(0, (cont_num0sch))

                    contactPerson_reg_entry.delete(0, END)
                    contactPerson_reg_entry.insert(0, (cont_per_sch))

                    emergPerson_reg_entry.delete(0, END)
                    emergPerson_reg_entry.insert(0, (emr_per_sch))

                    position_reg_entry.delete(0, END)
                    position_reg_entry.insert(0, (posistion_sch))

                    dateHire_reg.delete(0, END)
                    dateHire_reg.insert(0, (date_hire_sch))

                    department_reg_entry.delete(0, END)
                    department_reg_entry.insert(0, (department_sch))

                    dateEOC_reg.delete(0, END)
                    dateEOC_reg.insert(0, (eoc_sch))

                    tin_reg_entry.delete(0, END)
                    tin_reg_entry.insert(0, (tin_sch))

                    sss_reg_entry.delete(0, END)
                    sss_reg_entry.insert(0, (sss_sch))

                    phic_reg_entry.delete(0, END)
                    phic_reg_entry.insert(0, (phic_sch))

                    hdmf_reg_entry.delete(0, END)
                    hdmf_reg_entry.insert(0, (hdmf_sch))

                    emp_status_reg_entry.delete(0, END)
                    emp_status_reg_entry.insert(0, (emp_status_sch))

                    update_con_reg_entry.delete(0, END)
                    update_con_reg_entry.insert(0, (update_cont_sch))

                    salaryRate__reg_entry.delete(0, END)
                    salaryRate__reg_entry.insert(0, (salaryRate_sch))

                    taxCode_reg_entry.delete(0, END)
                    taxCode_reg_entry.insert(0, (tax_code_sch))

                    salaryDetail_reg_entry.delete(0, END)
                    salaryDetail_reg_entry.insert(0, (salaryDetails_sch))





    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")

def employee_registry():
    """This function is to insert employee or Employee Registry"""
    ts = time.time()
    mydb._open_connection()
    cursor = mydb.cursor()
    user_name = userName_entry.get()
    update_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    try:
        if employee_id_entry.get() == "":
            messagebox.showerror("Error","Employee ID Must be required")
        else:
            cursor.execute('Select * from employee_details WHERE employee_id = %s',
                           (employee_id_entry.get(),))
            row = cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "This EmployeeID already assigned")
            else:
                cursor.execute("INSERT INTO employee_details (employee_id,lastName," 
                    "firstName, middleName, gender, address_employee, contactNumber , " 
                    "contact_person, emer_cont_person, position, date_hired, " 
                    "department, end_contract, tin, sssNumber, phicNumber, hdmfNumber ,"
                    "employment_status, update_contract, salary_rate, taxCode," 
                    "Salary_Detail, user, update_date)" 
                                       
                    " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                    "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                    "%s,%s,%s,%s)",

                    (employee_id_entry.get(), lastName_reg_entry.get(), firstName_reg_entry.get(),
                     middleName_reg_entry.get(), gender_description.get(),
                     address_reg_entry.get('1.0', 'end-1c'),
                     contactNum_reg_entry.get(), contactPerson_reg_entry.get(),
                     emergPerson_reg_entry.get(),position_reg_entry.get(),
                     dateHire_reg.get(), department_reg_entry.get(), dateEOC_reg.get(),
                     tin_reg_entry.get(), sss_reg_entry.get(), phic_reg_entry.get(),
                     hdmf_reg_entry.get(), emp_status_reg_entry.get(), update_con_reg_entry.get(),
                     salaryRate__reg_entry.get(), taxCode_reg_entry.get(), salaryDetail_reg_entry.get(),
                     user_name,
                     update_time))

                messagebox.showinfo('JRS', 'Data has been Save')


                mydb.commit()
                mydb.close()
                cursor.close()


    except Exception as ex:
        messagebox.showerror("Erro", f"Error due to :{str(ex)}")


def employee_details():
    clearpayrollFrame()
    global employee_listbox
    global employee
    global empstore
    mydb._open_connection()
    cursor = mydb.cursor()
    employee_listbox = tk.Listbox(payroll_frame, width=57, height=29, bg='darkblue', fg='white', font=('courier', 10))
    employee_listbox.place(x=650,y=70)

    search_label = Label(payroll_frame, text='Last Name:', width=12, height=1, bg='red', fg='white',
                           font=('Arial', 12), anchor='e')
    search_label.place(x=650, y=30)

    global searchlist_entry
    searchlist_entry = Entry(payroll_frame, width=15, font=('Arial', 12), justify='right', fg='red')
    searchlist_entry.place(x=780, y=30)

    btn_employeeDetails = Button(payroll_frame, text='Search', bd=2, bg='blue', fg='white',
                                 font=('arial', 12), width=10, height=1, command=insert_listbox)
    btn_employeeDetails.place(x=930, y=30)
    btn_employeeDetails.bind('<Return>', insert_listbox)

    query = 'Select employee_id,lastName,firstName,\
              salary_rate, taxCode, Salary_Detail from employee_details\
                ORDER BY employee_id ASC'
    cursor.execute(query)
    myresult = cursor.fetchall()
    cnt = 0
    employee = {}

    for row in myresult:
        cnt+=1


        data = {
            'empid': row[0],
            'lastname': row[1],
            'firstname': row[2],
            'salaryrate': row[3],
            'taxcode': row[4],
            'details': row[5],
            'count': cnt
        }
        employee.update(data)

        count1 =str(employee['count'])
        empsid = employee['empid']
        lname = employee['lastname']
        fname =  employee['firstname']
        salarate =  str(employee['salaryrate'])
        taxcode =  employee['taxcode']
        details = employee['details']

        empstore = (count1) + " " " " + empsid+ " " " " + lname + " " " "  " " " " + fname + \
                   " " " " " " " " + salarate+ " " " " + taxcode+" " " " + details

        employee_listbox.insert(END, (empstore))

        employee_listbox.bind("<KeyRelease>",insert_listbox)

        # typed = searchlist_entry.get()
        # if type == '':
        #     data = employee
        # else:
        #     data = []
        #     for item in employee:
        #         if typed.lower() in item.lower():
        #             data.append(item)

    emplye_id_lbl = Label(payroll_frame, text='Employee ID:', width=11, height=1, bg='red', fg='white',
                         font=('Arial', 10), anchor='e')
    emplye_id_lbl.place(x=10, y=30)

    global employee_id_entry
    employee_id_entry = Entry(payroll_frame, width=11, font=('Arial', 10), justify='right', fg='red')
    employee_id_entry.place(x=120, y=30)

    lastName_reg_lbl = Label(payroll_frame, text='Last Name:', width=11, height=1, bg='red', fg='white',
                          font=('Arial', 10), anchor='e')
    lastName_reg_lbl.place(x=10, y=55)

    global lastName_reg_entry
    lastName_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    lastName_reg_entry.place(x=120, y=55)

    firstName_reg_lbl = Label(payroll_frame, text='First Name:', width=11, height=1, bg='red', fg='white',
                             font=('Arial', 10), anchor='e')
    firstName_reg_lbl.place(x=10, y=80)

    global firstName_reg_entry
    firstName_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    firstName_reg_entry.place(x=120, y=80)

    middleName_reg_lbl = Label(payroll_frame, text='Middle Name:', width=11, height=1, bg='red', fg='white',
                              font=('Arial', 10), anchor='e')
    middleName_reg_lbl.place(x=10, y=105)

    global middleName_reg_entry
    middleName_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    middleName_reg_entry.place(x=120, y=105)

    gender_reg_lbl = Label(payroll_frame, text='Gender:', width=11, height=1, bg='red', fg='white',
                               font=('Arial', 10), anchor='e')
    gender_reg_lbl.place(x=10, y=130)

    global gender_description
    gender_description = ttk.Combobox(payroll_frame, width=11, font=('Arial', 10))
    gender_description['values'] = ("Male", "Female")
    gender_description.place(x=120, y=130)

    address_lbl = Label(payroll_frame, text='Address:', width=11, height=1, bg='red', fg='white',
                          font=('Arial', 10), anchor='e')
    address_lbl.place(x=10, y=155)

    global address_reg_entry
    address_reg_entry = scrolledtext.ScrolledText(payroll_frame,
                                                          wrap=tk.WORD,
                                                          width=23,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
    address_reg_entry.place(x=120, y=155)

    contactNum_reg_lbl = Label(payroll_frame, text='Contact No:', width=11, height=1, bg='red', fg='white',
                               font=('Arial', 10), anchor='e')
    contactNum_reg_lbl.place(x=10, y=215)

    global contactNum_reg_entry
    contactNum_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    contactNum_reg_entry.place(x=120, y=215)

    contactPerson_reg_lbl = Label(payroll_frame, text='Cont. Person:', width=11, height=1, bg='red', fg='white',
                               font=('Arial', 10), anchor='e')
    contactPerson_reg_lbl.place(x=10, y=240)

    global contactPerson_reg_entry
    contactPerson_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    contactPerson_reg_entry.place(x=120, y=240)

    emergPerson_reg_lbl = Label(payroll_frame, text='Emerg:Person:', width=11, height=1, bg='red', fg='white',
                                  font=('Arial', 10), anchor='e')
    emergPerson_reg_lbl.place(x=10, y=265)

    global emergPerson_reg_entry
    emergPerson_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    emergPerson_reg_entry.place(x=120, y=265)

    position_reg_lbl = Label(payroll_frame, text='Position:', width=11, height=1, bg='red', fg='white',
                                font=('Arial', 10), anchor='e')
    position_reg_lbl.place(x=10, y=290)

    global position_reg_entry
    position_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    position_reg_entry.place(x=120, y=290)

    date_from_label = Label(payroll_frame, text='Date Hire:', width=11, height=1, bg='red', fg='white',
                            font=('Arial', 10), anchor='e')
    date_from_label.place(x=10, y=315)

    global dateHire_reg
    dateHire_reg = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                     foreground='white', borderwidth=2, padx=10, pady=10)
    dateHire_reg.place(x=120, y=315)
    dateHire_reg.configure(justify='center')

    department_reg_lbl = Label(payroll_frame, text='Department:', width=11, height=1, bg='red', fg='white',
                             font=('Arial', 10), anchor='e')
    department_reg_lbl.place(x=10, y=340)

    global department_reg_entry
    department_reg_entry = ttk.Combobox(payroll_frame, width=20)
    department_reg_entry['values'] = ("Head Office", "Admin-Site", "Pampanga", "Rizal-R&F")
    department_reg_entry.place(x=120, y=340)

    date_from2_label = Label(payroll_frame, text='Date EOC:', width=11, height=1, bg='red', fg='white',
                            font=('Arial', 10), anchor='e')
    date_from2_label.place(x=10, y=365)

    global dateEOC_reg
    dateEOC_reg = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                             foreground='white', borderwidth=2, padx=10, pady=10)
    dateEOC_reg.place(x=120, y=365)
    dateEOC_reg.configure(justify='center')

    tin_reg_lbl = Label(payroll_frame, text='TIN:', width=11, height=1, bg='red', fg='white',
                               font=('Arial', 10), anchor='e')
    tin_reg_lbl.place(x=10, y=390)

    global tin_reg_entry
    tin_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    tin_reg_entry.place(x=120, y=390)

    sss_reg_lbl = Label(payroll_frame, text='SSS Num:', width=11, height=1, bg='red', fg='white',
                        font=('Arial', 10), anchor='e')
    sss_reg_lbl.place(x=10, y=415)

    global sss_reg_entry
    sss_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    sss_reg_entry.place(x=120, y=415)

    phic_reg_lbl = Label(payroll_frame, text='PHIC Num:', width=11, height=1, bg='red', fg='white',
                        font=('Arial', 10), anchor='e')
    phic_reg_lbl.place(x=10, y=440)

    global phic_reg_entry
    phic_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    phic_reg_entry.place(x=120, y=440)

    hdmf_reg_lbl = Label(payroll_frame, text='HDMF Num:', width=11, height=1, bg='red', fg='white',
                         font=('Arial', 10), anchor='e')
    hdmf_reg_lbl.place(x=10, y=465)

    global hdmf_reg_entry
    hdmf_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    hdmf_reg_entry.place(x=120, y=465)

    emp_status_reg_lbl = Label(payroll_frame, text='Emp Status:', width=11, height=1, bg='red', fg='white',
                         font=('Arial', 10), anchor='e')
    emp_status_reg_lbl.place(x=10, y=490)

    global emp_status_reg_entry
    emp_status_reg_entry = ttk.Combobox(payroll_frame, width=11, font=('Arial', 10))
    emp_status_reg_entry['values'] = ("Employeed", "Resigned","Terminated")
    emp_status_reg_entry.place(x=120, y=490)

    # emp_status_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    # emp_status_reg_entry.place(x=120, y=490)

    update_con_reg_lbl = Label(payroll_frame, text='Contract:', width=11, height=1, bg='red', fg='white',
                               font=('Arial', 10), anchor='e')
    update_con_reg_lbl.place(x=10, y=515)

    global update_con_reg_entry
    update_con_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    update_con_reg_entry.place(x=120, y=515)

    salaryRate_reg_lbl = Label(payroll_frame, text='Salary Rate:', width=11, height=1, bg='red', fg='white',
                               font=('Arial', 10), anchor='e')
    salaryRate_reg_lbl.place(x=10, y=515)

    global salaryRate__reg_entry
    salaryRate__reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    salaryRate__reg_entry.place(x=120, y=515)

    taxCode_reg_lbl = Label(payroll_frame, text='Tax Code:', width=11, height=1, bg='red', fg='white',
                           font=('Arial', 10), anchor='e')
    taxCode_reg_lbl.place(x=270, y=30)



    global taxCode_reg_entry
    taxCode_reg_entry = ttk.Combobox(payroll_frame, width=11, font=('Arial', 10))
    taxCode_reg_entry['values'] = ("Taxable", "MWE")
    taxCode_reg_entry.place(x=370, y=30)

    salaryDetail_reg_lbl = Label(payroll_frame, text='Salary Details:', width=11, height=1, bg='red', fg='white',
                            font=('Arial', 10), anchor='e')
    salaryDetail_reg_lbl.place(x=270, y=55)

    global salaryDetail_reg_entry
    salaryDetail_reg_entry = ttk.Combobox(payroll_frame, width=11, font=('Arial', 10))
    salaryDetail_reg_entry['values'] = ("Monthly", "Daily")
    salaryDetail_reg_entry.place(x=370, y=55)

# this is for search emp id to update employee!!!
    search_reg_lbl = Label(payroll_frame, text='Search ID:', width=11, height=1, bg='red', fg='white',
                         font=('Arial', 10), anchor='e')
    search_reg_lbl.place(x=270, y=215)

    global searchEmpID_reg_entry
    searchEmpID_reg_entry = Entry(payroll_frame, width=15, font=('Arial', 10), justify='right', fg='red')
    searchEmpID_reg_entry.place(x=370, y=215)
# Buttons for Employee Details============
    global btn_save_employeeDetails
    btn_save_employeeDetails = Button(payroll_frame, text='Save', bd=2, bg='blue', fg='white',
                                 font=('arial', 10), width=10, height=1, command=employee_registry)
    btn_save_employeeDetails.place(x=300, y=90)
    btn_save_employeeDetails.bind('<Return>', employee_registry)

    btn_update_employeeDetails = Button(payroll_frame, text='Update', bd=2, bg='yellow', fg='gray',
                                      font=('arial', 10), width=10, height=1, command=employee_update)
    btn_update_employeeDetails.place(x=400, y=90)
    btn_update_employeeDetails.bind('<Return>', employee_update)

    btn_search_employeeDetails = Button(payroll_frame, text='Search', bd=2, bg='yellow', fg='gray',
                                        font=('arial', 10), width=10, height=1, command=search_employee_reg)
    btn_search_employeeDetails.place(x=485, y=215)
    btn_search_employeeDetails.bind('<Return>', search_employee_reg)



#==============================================Frame for Payroll Transaction=========================================
def payroll_transactions():
    #("Head Office", "Admin-Site", "Pampanga", "Rizal-R&F")

    clearFrame()
    global payroll_frame

    mydb._open_connection()
    cursor = mydb.cursor()
    emp_status = 'Employeed'
    dept_stat = 'Rizal-R&F'
    dept_stat2 = 'Head Office'
    dept_stat3 = 'Pampanga'
    cursor.execute("SELECT \
               COUNT(employee_id) As TotalEMP\
               FROM employee_details  \
               WHERE employment_status = '"+emp_status+"' AND department = '"+dept_stat+"' \
                ")

    myresult = cursor.fetchall()
    result = 0

    for row in myresult:
        result = row[0]
#==================this is for Head office Employee Count=========================
    cursor.execute("SELECT \
                   COUNT(employee_id) As TotalEMP\
                   FROM employee_details  \
                   WHERE employment_status = '" + emp_status + "' AND department = '" + dept_stat2 + "' \
                    ")

    myresult = cursor.fetchall()
    result2 = 0

    for row in myresult:
        result2 = row[0]

# ==================this is for Pampanga Employee Count=========================
        cursor.execute("SELECT \
                       COUNT(employee_id) As TotalEMP\
                       FROM employee_details  \
                       WHERE employment_status = '" + emp_status + "' AND department = '" + dept_stat3 + "' \
                        ")

        myresult = cursor.fetchall()
        result3 = 0

        for row in myresult:
            result3 = row[0]

    payroll_frame = Frame(MidViewForm9, width=1120, height=575, bd=2, bg='gray', relief=SOLID)
    payroll_frame.place(x=160, y=8)

    totalEmp_rizal_lbl2 = Label(payroll_frame, text='TOTAL RIZAL EMPLOYEE', width=26, height=1, bg='red', fg='white',
                               font=('Arial', 10), anchor='c')
    totalEmp_rizal_lbl2.place(x=170, y=40)


    totalEmp_rizal_lbl = Label(payroll_frame, text='', width=23, height=2, bg='red', fg='white')
    totalEmp_rizal_lbl.place(x=170, y=62)
    totalEmp_rizal_lbl.config(text= f' {result}',
                              font=('Arial', 13), anchor='c')

    totalEmp_ho_lbl2 = Label(payroll_frame, text='TOTAL HO EMPLOYEE', width=26, height=1, bg='yellowgreen', fg='red',
                                font=('Arial', 10), anchor='c')
    totalEmp_ho_lbl2.place(x=450, y=40)

    totalEmp_ho_lbl = Label(payroll_frame, text='', width=23, height=2, bg='yellowgreen', fg='red')
    totalEmp_ho_lbl.place(x=450, y=62)
    totalEmp_ho_lbl.config(text=f' {result2}',
                              font=('Arial', 13), anchor='c')

    totalEmp_pampanga_lbl2 = Label(payroll_frame, text='TOTAL PAMPANGA EMPLOYEE',
                            width=26, height=1, bg='brown', fg='white',
                             font=('Arial', 10), anchor='c')
    totalEmp_pampanga_lbl2.place(x=730, y=40)

    totalEmp_pampanga_lbl = Label(payroll_frame, text='', width=23, height=2, bg='brown', fg='white')
    totalEmp_pampanga_lbl.place(x=730, y=62)
    totalEmp_pampanga_lbl.config(text=f' {result3}',
                           font=('Arial', 13), anchor='c')


    btn_pay_cut_off = Button(MidViewForm9, text='Cut-off Period', bd=2, bg='blue', fg='white',
                            font=('arial', 12), width=15, height=2, command=cut_off_period)
    btn_pay_cut_off.place(x=2, y=40)
    btn_pay_cut_off.bind('<Return>', cut_off_period)

    btn_payrollCal = Button(MidViewForm9, text='Payroll Computation', bd=2, bg='blue', fg='white',
                              font=('arial', 12), width=15, height=2, command=payrollComputation_module)
    btn_payrollCal.place(x=2, y=100)
    btn_payrollCal.bind('<Return>', payrollComputation_module)
# this button is for Employee Details
    btn_employeeDetails = Button(MidViewForm9, text='Employee Details', bd=2, bg='blue', fg='white',
                            font=('arial', 12), width=15, height=2, command=employee_details)
    btn_employeeDetails.place(x=2, y=160)
    btn_employeeDetails.bind('<Return>', employee_details)

    btn_1601C = Button(MidViewForm9, text='1601 C Report', bd=2, bg='blue', fg='white',
                                 font=('arial', 12), width=15, height=2, command=print_1601C)
    btn_1601C.place(x=2, y=220)
    btn_1601C.bind('<Return>', print_1601C)


#===============================================Log in and DashBoard Frame=============================================


def Logout():
    result = tkMessageBox.askquestion('JRS System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':

        root.deiconify()
        reportFrame.destroy()


def close():
    root.destroy()


def search():
    print('Hello World')


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
    #filemenu7 = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Logout", command = Logout)
    # filemenu.add_command(label="Exit")
    filemenu2.add_command(label="Product Registration",command=inventory_module)
    filemenu2.add_command(label="Add new")
    filemenu2.add_command(label="View")
    filemenu3.add_command(label="Payroll",command=payroll_transactions)
    filemenu3.add_command(label="Clients Registration")
    filemenu3.add_command(label="Daily Transactions")
    filemenu4.add_command(label="Accounting Module",command=accounting_frame)
    filemenu6.add_command(label="Equipment Module", command = equipment_module)
    filemenu5.add_command(label="Reports Module")
    #filemenu7.add_command(label="New Payroll", command = payroll_transactions)
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Inventory", menu=filemenu2)
    menubar.add_cascade(label="Payroll Transactions", menu=filemenu3)
    menubar.add_cascade(label="Accounting Transaction", menu=filemenu4)
    menubar.add_cascade(label="Equipment", menu=filemenu6)
    menubar.add_cascade(label="Reports", menu=filemenu5)
    #menubar.add_cascade(label="New Payroll", menu=filemenu7)

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
            cursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                cursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s",
                               (USERNAME.get(), PASSWORD.get()))
                data = cursor.fetchone()
                admin_id = data[0]

                PASSWORD.set("")
                lbl_result.config(text="")
                root.withdraw()
                dashboard()


            else:
                lbl_result.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
    elif user_description.get() =="Employee":
        if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result.config(text="Please complete the required field!", fg="red")
        else:
            cursor.execute("SELECT * FROM user_employee WHERE username = %s AND password = %s",
                           (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                cursor.execute("SELECT * FROM user_employee WHERE username = %s AND password = %s",
                               (USERNAME.get(), PASSWORD.get()))
                data = cursor.fetchone()
                admin_id = data[0]

                PASSWORD.set("")
                lbl_result.config(text="")
                root.withdraw()
                dashboard()


            else:
                lbl_result.config(text="Invalid username or password", fg="red")
                USERNAME.set("")
                PASSWORD.set("")
    elif user_description.get() == "":
        lbl_result.config(text="Please fill up sign in as in the required field!", fg="red")

# ================================================= label and entryfields ===========================================


global userName_entry
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

password_entry = Entry(root, width=22, textvariable = PASSWORD, font=('Arial', 12),show="*")
#password_entry.insert(0,u'enter password')
password_entry.place(x=350, y=290)

lbl_result = Label(root, text="", bg='skyblue', font=('arial', 13),anchor='c')
lbl_result.place(x=200, y=320)


btn_login = Button(root, text="Login", font=('arial', 12), width=39, command=Login)
btn_login.place(x=200, y=340)
btn_login.bind('<Return>', Login),



# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()

