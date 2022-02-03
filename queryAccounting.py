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

testing_dictionary() 
# test_lookup()