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

# import PyPDF2
# from docx import Document
# from docx.shared import Inches

from datetime import date, timedelta
from datetime import datetime

#from PIL import ImageTk, Image as PILImage
#from payroll import selectTransaction
import babel.numbers

from tkinter.scrolledtext import ScrolledText

from pymongo import MongoClient
import pandas as pd
import re

from bson.objectid import ObjectId
import dateutil.parser
import pymongo

import certifi
ca = certifi.where()


client = pymongo.MongoClient(f"mongodb+srv://joeysabusido:genesis11@cluster0.bmdqy.mongodb.net/ldglobal?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.ldglobal

def insert_login():
    """
    This function is
    for inserting data 
    """
    
    
    
    userName = input(str('Enter UserName: '))
    login_passowrd = input('Enter Password: ')
    login_status = input('Enter Status: ')
    
    collection = db['login']
    
    dataInsert = {
        'username': userName,
        'password': login_passowrd,
        'status': login_status,
        'created':datetime.now()
        
    }
    
    try:
        collection.insert_one(dataInsert)
        print('data has been saved')
    except Exception as ex:
                print("Error", f"Error due to :{str(ex)}")


def test_lookup():
    """
    this function is 
    for testing look up
    """
    dataSearch = db['journal_entry']

    agg_result= dataSearch.aggregate([
            # {"$lookup": {
            #     "from": "chart_of_account", 
            #     'localField':'acoount_number',
            #     'foreignField': 'acoount_number',
            #     'as':'accountDetails'
            #     }
            # },
            {"$group" : 
            {"_id" :  '$bsClass',
            "accountName": {'$first':'$account_disc'},
            "totalDebit" : {"$sum" : '$debit_amount'},
            "totalCredit" : {"$sum" : '$credit_amount'},
            
            }},
           
        ]);
    # bb = 0
    # cc = 0
    for x in agg_result:
        bb = x['_id']
        a = x['accountName']
        b = x['totalDebit']
       
        c = x['totalCredit']
        
        d = b-c

        print(bb,d)

    # agg_result= dataSearch.find()
    # listCusor = list(agg_result)
    # # print(listCusor)

    # df = pd.DataFrame(listCusor)
    # # test = df.head()
    # print(df)

def testing_dictionary():
    """
    this function is for
    testing dictionaries
    """
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
    while answer == 'yes':
        cnt+=1
        dateEntry =  input('Enter Date: ')
        date_time_obj = datetime.strptime(dateEntry, '%m/%d/%Y')

        journal = input('Enter Journal Entry: ')
        ref = input('Enter Ref: ')
        journalMemo = input('Enter Journal Memo :')
        acountNumber = input('Enter Account Number :')
        accountTitle = input('Enter Account title: ')
        bsClass = input('Enter BS Class: ')
        debit_amount = float(input('Enter Debit Amount: '))
        credit_amount = float(input('Enter Credit Amount: '))
        user = 'joeysabusido'
        answer = input("Would you like to add data yes/no?: ").lower()

        data.update({len(data)+1:{
            'date_entry': dateEntry,
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
    # print(data)
   
    for i in data:
        print(i,data[i]['account_disc'])
       
        # dataInsert = {
        # 'date_entry': data[i]['date_entry'],
        # 'journal': data[i]['journal'],
        # 'ref': data[i]['ref'],
        # 'descriptions': data[i]['descriptions'],
        # 'acoount_number':data[i]['acoount_number'],
        # 'account_disc': data[i]['account_disc'],
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

def apv():

    apv_num = input('Enter APV number : ')
    dataSearch = db['journal_entry']
    query = {'ref':apv_num}

    agg_result = dataSearch.find(query)
    result = {}
    cnt = 0
    for i in agg_result:
        cnt+=1
        
        data = {'count': cnt,
               
                'debit_amount': (i['debit_amount']),
                'credit_amount': (i['credit_amount']),
                'debit_amount_APV': '{:,.2f}'.format(i['credit_amount'] + i['credit_amount']),
                # 'credit_amount_TOTAL': i['credit_amount'] ,
                # 'credit_amount2': float('{:,.2f}'.format('credit_amount')),

                
                    }
                

        result.update(data)

        print(result['debit_amount_APV'])

def demo():
    """
    This function is for demosntration of printing Microsoft word
    """
    # document = Document()

    # x = document.add_heading('ACCOUNT PAYABLE VOUCHER', 1)
    # x.alignment = 1
    # p = document.add_paragraph('A plain paragraph having some ')
    # p.add_run('bold').bold = True
    # p.add_run(' and some ')
    # p.add_run('italic.').italic = True

    # document.add_heading('Heading, level 1', level=1)
    # document.add_paragraph('Intense quote', style='Intense Quote')

    # document.add_paragraph(
    #     'first item in unordered list', style='List Bullet'
    # )
    # document.add_paragraph(
    #     'first item in ordered list', style='List Number'
    # )

    # document.add_picture('D:\LD\ldproject\image\logo.jpg', width=Inches(1.25))

    # records = (
    #     (3, '101', 'Spam'),
    #     (7, '422', 'Eggs'),
    #     (4, '631', 'Spam, spam, eggs, and spam')
    # )

    # table = document.add_table(rows=1, cols=3)
    # hdr_cells = table.rows[0].cells
    # hdr_cells[0].text = 'Qty'
    # hdr_cells[1].text = 'Id'
    # hdr_cells[2].text = 'Desc'
    # for qty, id, desc in records:
    #     row_cells = table.add_row().cells
    #     row_cells[0].text = str(qty)
    #     row_cells[1].text = id
    #     row_cells[2].text = desc

    # document.add_page_break()

    # document.save('demo.docx')
    # startfile("demo.docx")

def testing_docx():
    """
    This function is 
    for printing documents
    using ms words
    """
    dataSearch = db['journal_entry']
    query = input('Enter APV no. ')

    query2 = {'ref':query}
    agg_result2 = dataSearch.find(query2)
    result = {}
    total_debit_amount = 0
    total_credit_amount = 0
    cnt = 0
    for i in agg_result2: 
        
        cnt+=1
        data = {'count': cnt,
                'date_entry': i['date_entry'],
                'journal': i['journal'],
                'ref': i['ref'],
                'descriptions': i['descriptions'],
                'acoount_number': i['acoount_number'],
                'account_disc': i['account_disc'],
                'bsClass': i['bsClass'],
                'debit_amount': i['debit_amount'],
                'debit_amount2': '{:,.2f}'.format(i['debit_amount']),
                'credit_amount': i['credit_amount'],
                'credit_amount2': '{:,.2f}'.format(i['credit_amount']),
                'due_date_apv': i['due_date_apv'],
                'terms_days': i['terms_days'],
                'supplier_Client': i['supplier/Client'],
                'totalCredit': i['credit_amount'],
                # 'totalDebit': '{:,.2f}'.format(i['debit_amount'] + i['debit_amount']),
                
                    }
                

        result.update(data)

        test_db = (result['account_disc'])

        records = (
            (result['account_disc'],result['debit_amount'])
        )
        
        # document = Document()

        # x = document.add_heading('ACCOUNT PAYABLE VOUCHER', 1)
        # x.alignment = 1
        
        # table = document.add_table(rows=1, cols=1)
        # hdr_cells = table.rows[0].cells
        # hdr_cells[0].text = ''
        # # hdr_cells[1].text = ''
        # # hdr_cells[2].text = ''
        # for qty, dbt in records:
        #     row_cells = table.add_row().cells
        #     row_cells[0].text = str(qty)
        #     row_cells[1].text = dbt
        #     # row_cells[2].text = float(credit)

        # document.add_page_break()

        # document.save('demo.docx')
        # startfile("demo.docx")


def pdf_to_word():
    """
    This function is for printing
    document pdf to word
    """

    # FILE_PATH = 'd:\LD\ldproject\\apv.pdf'

    # with open(FILE_PATH, mode='rb') as f:

    #     reader = PyPDF2.PdfFileReader(f)

    #     page = reader.getPage(0)

    #     print(page.extractText())
    
        # startfile("apv.doc")

def update_user_admin():
    """
    This function is for updating
    user status
    """

       
    dataSearch = db['login']
    
    try:
        search_data = dataSearch.find()
        listCusor = list(search_data)
        # print(listCusor)

        df = pd.DataFrame(listCusor)
        # test = df.head()
        print(df)
    
    

    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")   
        
    name_search = input('Enter Name: ')
    
    query = {'fullname':{"$regex": name_search}}
    status_update = input('Enter Update : ')
    
    try:
        newValue = { "$set": { "status": status_update } }
        dataSearch.update_one(query, newValue)
        print('Data has been updated')
    except:
        print('error occured')

def test_query():
    """
    This is to test regex query
    """
    dataSearch = db['login']

    name_search = input('Enter Name: ')
    
    query = {'fullname':{"$regex": name_search}}
   
    try:
        search_data = dataSearch.find(query)
        listCusor = list(search_data)
        # print(listCusor)

        df = pd.DataFrame(listCusor)
        # test = df.head()
        print(df)
    
    

    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")   


def update_user_employee():
    """
    This function is for updating
    user status
    """

       
    dataSearch = db['employee_login']
    
    try:
        search_data = dataSearch.find()
        listCusor = list(search_data)
        # print(listCusor)

        df = pd.DataFrame(listCusor)
        # test = df.head()
        print(df)
    
    

    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")   
        
    name_search = input('Enter Name: ')
    
    query = {'fullname':{"$regex": name_search}}
    status_update = input('Enter Update : ')
    
    try:
        newValue = { "$set": { "status": status_update } }
        dataSearch.update_one(query, newValue)
        print('Data has been updated')
    except:
        print('error occured')

def search_fundrequest():
    """
    This function is for
    searching fundrequest
    """
    fr_number = input('Enter fr Number : ')
    dataSearch = db['fund_request']
    query = {'fr_number': fr_number}

    fr_search = dataSearch.find(query)


    try:
        search_data = dataSearch.find(query)
        listCusor = list(search_data)
        # print(listCusor)

        df = pd.DataFrame(listCusor)
        # test = df.head()
        print(df)
    
    

    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")  

# search_fundrequest()


# update_user_employee()
# test_query()

# update_user_admin()


# pdf_to_word()
# testing_docx()


# demo()
# apv()
# testing_dictionary() 
# test_lookup()

testing_dictionary()