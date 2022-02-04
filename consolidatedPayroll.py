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

from datetime import date, timedelta
from datetime import datetime

#from PIL import ImageTk, Image as PILImage
#from payroll import selectTransaction
import babel.numbers

from tkinter.scrolledtext import ScrolledText

mydb = mysql.connector.connect(
            host="192.46.225.247",
            user="joeysabusido",
            password="Genesis@11",
            database="ldglobal",
            auth_plugin='mysql_native_password')
cursor = mydb.cursor()


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

# global mwe_monthly
# mwe_monthly = 12350/2 # monthly Minimum Wage Earner
total_deminimis = 3883.34/2

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

def clearpayrollFrame():
    # destroy all widgets from frame
    for widget in payroll_frame.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    payroll_frame.pack_forget()

def clearFrame():
    # destroy all widgets from frame
    for widget in MidViewForm9.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    MidViewForm9.pack_forget()

#===============================================Payroll Transactions===================================================
def print1601c_report():
    """This function is to print 1601C"""

    mydb._open_connection()
    cursor = mydb.cursor()
    date1 = cal7.get()
    date2 = cal8.get()
    user_reg = userName_entry.get()



    miminum_wage = str(420)

    cursor.execute("SELECT employee_id,department\
                            FROM payroll_computation where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' ")
    myresult = list(cursor.fetchall())
    result = []

    cnt = 0
    for row in myresult:
        cnt += 1
        dept_print = row[1]

        data = {'count': cnt,
                'employeeid': row[0],

                }

        result.append(data)

        # if dept_print == 'Rizal-R&F':
        #     miminum_wage = str(373)
        # elif dept_print == 'Head Office':
        #     miminum_wage = str(537)
        # elif dept_print == 'Pampanga':
        #     miminum_wage = str(420)
        
        # print(miminum_wage)
    # this query is for total Gross
        cursor.execute("SELECT sum(grosspay_save) as GROSS\
                                    FROM payroll_computation\
                                    where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                      and on_off_details = 'on'  ")
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
                        AND  taxable_mwe_detail = 'MWE'  and on_off_details = 'on' ")
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
                        AND  taxable_mwe_detail = 'MWE'  and on_off_details = 'on' ")


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
                                             AND  taxable_mwe_detail = 'Taxable'  and on_off_details = 'on'\
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
                                                AND  taxable_mwe_detail = 'Taxable'  and on_off_details = 'on'\
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



#=========================================Export to Excel==========================================================

def payroll_export():
    """This function is for exporting payroll """
    
    mydb._open_connection()
    cursor = mydb.cursor()
    
    date1 = datefrom_export.get()
    date2 = dateto_export.get()

    workbook = xlsxwriter.Workbook("payroll.xlsx")
    worksheet = workbook.add_worksheet('rental')
    worksheet.write('A1', 'ID')
    worksheet.write('B1', 'EMPLOYEE NAME')
    worksheet.write('C1', 'POSITION')
    worksheet.write('D1', 'RATE')
    worksheet.write('E1', 'GROSS PAY')
    worksheet.write('F1', 'DEPARTMENT')
    worksheet.write('G1', 'SSS PROVI')
    worksheet.write('G1', 'TOTALDEM')
    worksheet.write('H1', 'OTHER FORMS')
    worksheet.write('I1', 'TAXABLE AMOUNT')
    worksheet.write('J1', 'TAX WIDTHEL')
    worksheet.write('K1', 'TAX/MWE')
    
   
   
    rowIndex = 2

    cursor.execute("SELECT employee_id,last_name,\
                        first_name,position_name, salary_rate,SUM(grosspay_save) as totalGross,department,\
                        Sum(sss_save) as TotalSSS,\
                        sum(phic_save) as totalphic,sum(hmdf_save) as totalhdmf,sum(totalDem_save) as totalDem,\
                        sum(taxwitheld_save) as TotalWtax,\
                       sum(cashadvance_save) as totalCA,sum(sssloan_save) as totalsssloan,\
                        sum(hdmfloan_save) as totalhdmfloan,sum(netpay_save) as totalnetpay, \
                        sum(sss_provi_save) as TotalProvi,\
                        sum(totalDem_save) as TotalDemi,\
                        sum(otherforms_save) as TotalOtherforms,\
                        sum(taxable_amount) as TotaltaxAmount,\
                        sum(taxwitheld_save) as TotalWitheld,\
                        sum(total_mandatory)as totalMandatory,taxable_mwe_detail\
                        FROM payroll_computation where cut_off_date BETWEEN '"+ date1 +"' and '"+ date2 +"' \
                            AND on_off_details = 'on' \
                      GROUP BY employee_id,last_name,first_name, position_name,salary_rate,department,\
                          taxable_mwe_detail ")
   
    myresult = cursor.fetchall()

    for data in myresult:
        empIDxlx = data[0]
        lastnamexlx = data[1]
        fnamexls = data[2]
        full_name_xlx = lastnamexlx + ',' + fnamexls
        position_xlx = data[3]
        salaryRate_xlx = data[4]
        grosspay_xlx = data[5]
        department_xlx = data[6]
        sss_provi_xlx = data[16]
        totalDem_xlx = data[17]
        otherforms_xlx = data[18]
        taxableAmount_xlx = data[19]
        tax_WIDTHEL_xlx = data[20]
        tax_mwe_detail_xlx = data[22]
      

       
       
       

        worksheet.write('A' + str(rowIndex),empIDxlx)
        worksheet.write('B' + str(rowIndex),full_name_xlx)
        worksheet.write('C' + str(rowIndex),position_xlx)
        worksheet.write('D' + str(rowIndex),salaryRate_xlx)
        worksheet.write('E' + str(rowIndex),grosspay_xlx)
        worksheet.write('F' + str(rowIndex),department_xlx)
        worksheet.write('G' + str(rowIndex),sss_provi_xlx)
        worksheet.write('G' + str(rowIndex),totalDem_xlx)
        worksheet.write('H' + str(rowIndex),otherforms_xlx)
        worksheet.write('I' + str(rowIndex),taxableAmount_xlx)
        worksheet.write('J' + str(rowIndex),tax_WIDTHEL_xlx)
        worksheet.write('K' + str(rowIndex),tax_mwe_detail_xlx)
       
        
       
        
        rowIndex += 1

    workbook.close()
    messagebox.showinfo('JRS', 'Data has been exported')    

    # from os import startfile
    startfile("payroll.xlsx")

def payroll_excel_export_frame():
    """This function is to payroll excel export frame"""
    clearpayrollFrame()
    mydb._open_connection()
    cursor = mydb.cursor()

    

    date_from_label = Label(payroll_frame, text='Date From:', width=10, height=1, bg='yellow', fg='gray',
                              font=('Arial', 10), anchor='e')
    date_from_label.place(x=250, y=150)


    # date_from_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    # date_from_entry.place(x=350, y=150)

    global datefrom_export
    datefrom_export = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                            foreground='white', borderwidth=2, padx=10, pady=10)
    datefrom_export.place(x=350, y=150)
    datefrom_export.configure(justify='center')

    date_to_label = Label(payroll_frame, text='Date To:', width=10, height=1, bg='yellow', fg='gray',
                            font=('Arial', 10), anchor='e')
    date_to_label.place(x=550, y=150)

    # date_to_entry = Entry(payroll_frame, width=22, font=('Arial', 10), justify='right')
    # date_to_entry.place(x=650, y=150)

    global dateto_export
    dateto_export = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                               foreground='white', borderwidth=2, padx=10, pady=10)
    dateto_export.place(x=650, y=150)
    dateto_export.configure(justify='center')

    btn_search = Button(payroll_frame, text="Export", bg='gray', fg='yellow', font=('arial', 9),
                                width=12, command=payroll_export)
    btn_search.place(x=820, y=150)
    btn_search.bind('<Return>', payroll_export)
# ==================================================Payroll computation Frame ============================================ 
def update_salary_comp():
    """This function is for updating salary computation"""
    mydb._open_connection()
    cursor = mydb.cursor()

    date_update_edit = payCal_date.get()
    sss_update = sss_entry.get()
    phic_update = phic_entry.get()
    hdmf_update = hdmf_entry.get()
    sss_provi_update = sssPro_entry.get()
    total_mandatory_update = totl_mandatory_entry.get()
    uniform_update  = uniform_entry.get()
    rice_save_update = rice_entry.get()
    laundry_save_update = laundry_entry.get()
    medical1_save_update = medical1_entry.get()
    medical2_save_update = medical2_entry.get()
    totalDem_save_update = totalDem_entry.get()
    # totalDem_save_update2 = '{:.2f}'.format(medical2_save_update)
    otherforms_save_update = otherForms_entry.get()
    taxable_amount_update = taxable_amount
    taxable_amount_update2 = str(taxable_amount_update)
    witheld_save_update = taxWitheld_entry.get()
    provi_rate_update = provincialRate_entry.get()
    on_off_update =  on_off_saving
    mwe_taxable_update = tax_mwe_entry.get()
    net_pay_update = netpay_entry.get()
    cash_advace_update = cashAdvance_entry.get()
    hdmf_loan_update = hdmfLoan_entry.get()
    sss_loan_update =sssLoan_entry.get()
    gross_pay_update = gross_pay_entry.get()
    spltOT_update = splOT_entry.get()
    department_update = department_list.get()

    lastname = lastname_entry.get()
    firstname = firstname_entry.get()
    posittion = position_entry.get()
    salRate_entry = salaryRate_entry.get()
    empID = empID_entry.get()

    try:
        if id_searchTrans_entry.get()== "":
            messagebox.showerror("Error", "Search  fields  Must be required")

        else:
            cursor.execute(
                "UPDATE payroll_computation SET sss_save ='"+ sss_update +"', \
                phic_save ='"+ phic_update +"',\
                hmdf_save ='"+ hdmf_update +"',\
                sss_provi_save ='"+ sss_provi_update +"',\
                on_off_details='" + on_off_update + "',\
                taxwitheld_save='" + witheld_save_update + "',\
                provicaial_rate='" + provi_rate_update + "',\
                total_mandatory ='"+total_mandatory_update+"',\
                uniform_save='"+uniform_update+"',\
                rice_save='" + rice_save_update + "',\
                laundry_save ='" + laundry_save_update + "',\
                medical1_save='" + medical1_save_update + "',\
                medical2_save='" + medical2_save_update + "',\
                totalDem_save='" + totalDem_save_update + "',\
                otherforms_save='" + otherforms_save_update + "',\
                taxable_amount = '" + taxable_amount_update2 + "',\
                taxable_mwe_detail = '" + mwe_taxable_update + "',\
                netpay_save = '" + net_pay_update + "',\
                cashadvance_save = '" + cash_advace_update + "',\
                hdmfloan_save = '" + hdmf_loan_update + "',\
                sssloan_save = '" + sss_loan_update + "',\
                grosspay_save = '" + gross_pay_update + "',\
                employee_id = '" + empID + "',\
                last_name = '" + lastname + "',\
                first_name = '" + firstname + "',\
                salary_rate = '" + salRate_entry + "',\
                department = '" + department_update + "',\
                cut_off_date = '" + date_update_edit + "'\
                WHERE id =%s", (id_searchTrans_entry.get(),)
            )
            mydb.commit()
            mydb.close()
            cursor.close()
            messagebox.showinfo('JRS', 'Data has been updated')
       
         
        #   taxable_amount='" + taxable_amount_update + "'\  
           
            # uniform_save='"+uniform_update+"',\
            # rice_save='" + rice_save_update + "',\
            # laundry_save ='" + laundry_save_update + "',\
            # medical1_save='" + medical1_save_update + "',\
            # medical2_save='" + medical2_save_update + "',\
            # totalDem_save='" + totalDem_save_update + "',\
            # otherforms_save='" + otherforms_save_update + "',\
            # taxable_amount='" + taxable_amount_update + "',\
            # cut_off_date = '" + date_update_edit + "'\
           
# netpay_save = '" + net_pay_update + "'\
#  cut_off_date = '" + date_update_edit + "'\

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")   
   


def search_id_trans_edit():
    """This function is for searching payroll transaction tru trans ID"""
    btn_saveComp["state"] = DISABLED
    mydb._open_connection()
    cursor = mydb.cursor()

    try:
        if id_searchTrans_entry.get()== "":
            messagebox.showerror("Error", "Search  fields  Must be required")
        else:
            cursor.execute(
            "SELECT department,cut_off_date,employee_id,last_name,\
            first_name,position_name,salary_rate,provicaial_rate,regular_day, regularday_cal,\
            regularday_ot,regularday_ot_cal,regularsunday, regularsunday_cal,regularsunday_ot,regularsunday_ot_cal, \
            spl,spl_cal,spl_ot,spl_ot_cal, legal_day,legal_day_cal,legal_day_ot,legal_day_ot_cal,\
            shoprate_day,shoprate_day_cal,proviRate_day,proviRate_day_cal,proviRate_day_ot,\
            proviRate_day_ot_cal,provisun_day,provisun_day_cal,provisun_day_ot,provisun_day_ot_cal,\
            nightdiff_day,nightdiff_day_cal,adjustment,adjustment_cal,grosspay_save,salaryDetails_save,\
            sss_save,phic_save,hmdf_save,sss_provi_save,total_mandatory,uniform_save,rice_save,laundry_save,\
            medical1_save,\
            medical2_save,totalDem_save,otherforms_save,taxable_amount,taxwitheld_save,cashadvance_save,\
            sssloan_save,hdmfloan_save,netpay_save,\
            userlog,time_update,on_off_details\
            from payroll_computation \
            WHERE id = %s",(id_searchTrans_entry.get(),))

            myresult = cursor.fetchall()

            for row in myresult:
                dep_search = row[0]
                date_search =row[1]
                employeeID = row[2]
                regday_search = row[8]
                regdayOT_search = row[10]
                regSun_search = row[12]
                regSunOT_search = row[14]
                spl_search = row[16]
                splOT_search = row[18]
                legalDay_search = row[20]
                legalOT_search = row[22]
                shopRate_search = row[24]
                proviDay_search = row[26]
                proviDayOT_search = row[28]
                provisun_search = row[30]
                provisunOT_search = row[32]
                nightshif_search = row[34]
                adjustment_search = row[36]
                sss_search = row[40]
                phic_search = row[41]
                hdmf_search = row[42]
                hdmf_priv_search = row[43]
                sss_loanSearch = row[55]
                # tax_mwe_search_update = row[44]



                department_list.delete(0, END)
                department_list.insert(0, (dep_search))

                payCal_date.delete(0, END)
                payCal_date.insert(0, (date_search))

                empID_entry.delete(0, END)
                empID_entry.insert(0, (employeeID))

                regday_entry.delete(0, END)
                regday_entry.insert(0, (regday_search))

                regdayOT_entry.delete(0, END)
                regdayOT_entry.insert(0, (regdayOT_search))

                regsun_entry.delete(0, END)
                regsun_entry.insert(0, (regSun_search))

                sunOT_entry.delete(0, END)
                sunOT_entry.insert(0, (regSunOT_search))

                spl_entry.delete(0, END)
                spl_entry.insert(0, (spl_search))

                splOT_entry.delete(0, END)
                splOT_entry.insert(0, (splOT_search))

                legal_entry.delete(0, END)
                legal_entry.insert(0, (legalDay_search))

                legalOT_entry.delete(0, END)
                legalOT_entry.insert(0, (legalOT_search))

                shopRate_entry.delete(0, END)
                shopRate_entry.insert(0, (shopRate_search))

                proviRate_entry.delete(0, END)
                proviRate_entry.insert(0, (proviDay_search))

                proviOT_entry.delete(0, END)
                proviOT_entry.insert(0, (proviDayOT_search))

                proviSun_entry.delete(0, END)
                proviSun_entry.insert(0, (provisun_search))

                proviSunOT_entry.delete(0, END)
                proviSunOT_entry.insert(0, (provisunOT_search))

                nightdiff_entry.delete(0, END)
                nightdiff_entry.insert(0, (nightshif_search))

                adjustment_entry.delete(0, END)
                adjustment_entry.insert(0, (adjustment_search))

                sss_entry.delete(0, END)
                sss_entry.insert(0, (sss_search))

                phic_entry.delete(0, END)
                phic_entry.insert(0, (phic_search))

                hdmf_entry.delete(0, END)
                hdmf_entry.insert(0, (hdmf_search))

                sssPro_entry.delete(0, END)
                sssPro_entry.insert(0, (hdmf_priv_search))

                sssLoan_entry.delete(0, END)
                sssLoan_entry.insert(0, (sss_loanSearch))

                # tax_mwe_entry.delete(0, END)
                # tax_mwe_entry.insert(0, (tax_mwe_search_update))
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")   
def payroll_comp_treeview_display():
    """This function is to display treeview withou duplication of data"""

    payroll_computation_treeview.delete(*payroll_computation_treeview.get_children())
    return payroll_comp_treeview()

def payroll_comp_treeview():
    """This function is for treeview to display"""

    mydb._open_connection()
    cursor = mydb.cursor()
    department = department_list.get()


    date1 = payCal_search_date.get()
    date2 = payCal_search_date_to.get()

    cursor.execute("SELECT employee_id,last_name,\
                        first_name,salary_rate,grosspay_save,sss_save,\
                        phic_save,hmdf_save,totalDem_save,taxwitheld_save,\
                       cashadvance_save,sssloan_save,hdmfloan_save,netpay_save,id\
                        FROM payroll_computation where cut_off_date BETWEEN '"+ date1 +"' and '"+ date2 +"' \
                      AND department = '" + department + "'")
    myresult = list(cursor.fetchall())
    result = []

    cnt = 0
    for row in myresult:
        cnt+=1
        employeeID = row[0]
        lastName = row[1]
        fname = row[2]
        grossPay_tree = row[4]
        netPay_treeview = row[13]
        trans_id = row[14]
               
        payroll_computation_treeview.insert('', 'end', values=(cnt,trans_id,
                                employeeID, lastName, fname, grossPay_tree,netPay_treeview ))




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
        provshare_save = sssPro_entry.get()

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

        ca_deduct_save2 = ca_deduct_save
        sss_loandeduct_save = sss_loandeduct
        netPay_save = netPay





        user_reg = userName_entry.get()
        
        # date_time_update = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        date_time_update = datetime.now()

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
            "userlog,time_update,on_off_details,taxable_mwe_detail)" 
            " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
            "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

            (department, date1, empID, lastname,
             firstname, posittion, salRate_entry,  provicialRate, regday_save, regdaycal_save,
             regdayot_save, regdaycalOT_save, regsun_save, regsuncal_save, regsunOT_save, regsuncalOT_save,
             spl_save, splCal_save, splOT_entry.get(), splOTcal_save, legal_save, legalCal_save, legalOT_save, legalOTcal_save,
             shoprate_save, shoprateCal_save, proviRate_save, proviRateCal_save, proviRateOT_save,
             proviRateOTcal_save, proviRateSun_save, proviRateSunCal_save,proviSunRateOT_save,proviSunRateOTcal_save,
             nightdiff_save,nightdiffCal_save, adjustments_save, adjustmentCal_save, grosspay_save, salaryDetails_save,
             sss_save, phic_save, hdmf_save, provshare_save, totalMadatory_save, uniform_save, rice_save, laundry_save,
             medical1_save,
             medical2_save, totalDem_save,otherForms_save, taxable_amount_save, taxWitheld_entry.get(), ca_deduct_save2,
             sss_loandeduct_save, hdmfdeduct_save, netPay_save,
             user_reg,
             date_time_update,on_off_saving,tax_mwe_entry.get()))
        # 58
        messagebox.showinfo('JRS','Data has been Save')


        mydb.commit()
        mydb.close()
        cursor.close()
        payroll_comp_treeview_display()

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
    global mwe_monthly
    netPay = 0
    global salaryRate
    global ca_deduct_save
    ca_deduct_save = cashAdvance_entry.get()
    #ca_deduct_save2 = '{:.2f}'.format(ca_deduct_save)
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

        # mwe_monthly determinition!!!
        mwe_monthly = 0
        if department_list.get() == "Rizal-R&F" or   department_list.get() == "Admin-Site" :
            mwe_monthly = float(373 * 13)
        elif  department_list.get() == "Head Office":
            mwe_monthly = float(537 * 13)
        elif  department_list.get() == "Pampanga":
            mwe_monthly = float(420 * 13)

        # print(mwe_monthly)
        # print(salRate)
        #salRate = salaryRate * 13


        basic_taxable = grosspay - mwe_monthly
        totalDem = 0


        if basic_taxable <=0:
            basic_taxable = 0
        else:
            basic_taxable = basic_taxable


        if  on_off_saving =='off' or on_off_saving == None :
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

        elif salRate <= mwe_monthly and on_off_saving =='on':
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

        elif salRate <= mwe_monthly and grossPay <= mwe_monthly and basic_taxable <= 0 and on_off_saving =='off':
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

        elif salRate >= mwe_monthly and grossPay <= mwe_monthly and basic_taxable <= 0 and on_off_saving =='on':
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

        # and grossPay <= mwe_monthly
        # and grossPay <= total_deminimis
        # and basic_taxable <= 0
        elif salRate > mwe_monthly  and basic_taxable <= 0  and on_off_saving =='on':

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

        # and grossPay <= mwe_monthly(ito yong tinanggal para don sa gross < mwe_monthly
        # and basic_taxable <= 0
        elif salRate > mwe_monthly and grossPay <= mwe_monthly and grossPay > total_deminimis  and on_off_saving =='on':

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
        elif salRate > mwe_monthly and basic_taxable > 0 and basic_taxable > total_deminimis and on_off_saving =='on':

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
        elif salRate > mwe_monthly and basic_taxable > 0 and basic_taxable <= total_deminimis and on_off_saving =='on':

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

        if on_off_saving =='off' or on_off_saving ==None and  basic_taxable <= 0:
            otherForms = 0

        if afterDem >= 0 and salRate + float(allowance_search) >= mwe_monthly and on_off_saving =='on'and  basic_taxable > 0:
            if salRate + float(allowance_search) <= 15000 and salRate + float(allowance_search) >= mwe_monthly and on_off_saving =='on' :
                CalotherForms = ((90000 - (salRate * 2)) / 24)

                if afterDem <= CalotherForms:
                    otherForms = afterDem
                else:
                    otherForms = CalotherForms
            
            

            elif salRate + float(allowance_search) > 15000 and salRate + float(allowance_search) >= mwe_monthly and on_off_saving =='on'and  basic_taxable > 0:
                CalotherForms = (90000 -30000) / 24

                if afterDem <= CalotherForms:
                    otherForms = afterDem
                else:
                    otherForms = CalotherForms
        taxable_amount = taxable_amount - otherForms

        # this portion is edited 1.25.22 for error debugging employee 3001 taxwithheld
        if checkvar1.get() >= 1: # only this if is added to debug
            if taxable_amount > 0:
                cursor.execute("SELECT * FROM tax_table")
                query_result = cursor.fetchall()
                for row in query_result:

                    amountFrom_tax = float(row[1])

                    amountTo_tax = float(row[2]) 
                    baseAmount_tax = float(row[3])
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
        else:
            taxWithheld = 0
    taxWithheld2 = '{:.2f}'.format(taxWithheld)
    taxWitheld_entry.delete(0, END)
    taxWitheld_entry.insert(0, (taxWithheld2))


    totalDem = uniform + rice + laundry + medical1 + medical2
    totalDem2 = '{:.2f}'.format(totalDem)
    totalDem_entry.delete(0, END)
    totalDem_entry.insert(0, (totalDem2))

    otherForms2 = '{:.2f}'.format(otherForms)
    otherForms_entry.delete(0, END)
    otherForms_entry.insert(0, (otherForms2))





    netPay = grossPay - taxWithheld - totalMadatory - float(sss_loandeduct) - float(hdmfdeduct) - float(ca_deduct_save)
    netPay2 = '{:,.2f}'.format(netPay)
    netpay_entry.delete(0, END)
    netpay_entry.insert(0, (netPay2))

    # print(taxable_amount)
def net_pay_conso_calculation():
    """This function is for calculation of Net pay with consolidation of Taxwithheld"""
    netPay = grosspay - float(taxWitheld_entry.get()) - totalMadatory - float(sss_loandeduct) - float(hdmfdeduct) - float(ca_deduct_save)
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


        


        sss_loandeduct = 0
        sss_loandeduct2 = '{:,.2f}'.format(sss_loandeduct)
        sssLoan_entry.delete(0, END)
        sssLoan_entry.insert(0, (sss_loandeduct2))

    

# this function is for computation of gross consolidation!!!
def computation_cosolidated():
    """This function is for computating cosolidation"""
    mydb._open_connection()
    cursor = mydb.cursor()

    # date1 = datetime.now()
    date1 = payCal_date.get() 
    dated2 =  timedelta(16)
    # date2 = date1 - dated2

    
    # date2 = str((date.fromisoformat(date1)) - dated2 )

    date2 = payCal_conso_date.get()
    
    # date2 = payCal_conso_date.get()
    empID_conso = empID_entry.get()

    check2 = checkvar2.get()

    if check2 == 1:
        gross_pay_conso = 0
        uniform_conso = 0
        rice_conso = 0
        laundry_conso = 0
        medical1_conso = 0
        medical2_conso = 0
        totaldem_conso = 0
        otherforms_conso = 0
        taxable_conso = 0
        try:
            cursor.execute("Select * from payroll_computation \
                            where cut_off_date BETWEEN '" + date2 + "' and '" + date1 + "'\
                        AND employee_id = '" + empID_conso + "'")
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "No record found during last payroll")
                gross_pay_conso = 0
                uniform_conso = 0
                rice_conso = 0
                laundry_conso = 0
                medical1_conso = 0
                medical2_conso = 0
                totaldem_conso = 0
                otherforms_conso = 0
                taxable_conso = 0
               
                
            else:
                cursor.execute("Select grosspay_save, uniform_save,rice_save,laundry_save,medical1_save, \
                    medical2_save,totalDem_save,otherforms_save,taxable_amount\
                    from payroll_computation \
                            where cut_off_date BETWEEN '" + date2 + "' and '" + date1 + "'\
                        AND employee_id = '" + empID_conso + "'")

                # grosspay_save, uniform_save,rice_save,laundry_save,medical1_save,medical2_save,totalDem_save,otherforms_save,cut_off_date\
                myresult = cursor.fetchall()

                for row in myresult:
                    gross_pay_conso = row[0]
                    uniform_conso = row[1]
                    rice_conso = row[2]
                    laundry_conso = row[3]
                    medical1_conso = row[4]
                    medical2_conso = row[5]
                    totaldem_conso = row[6]
                    otherforms_conso = row[7]
                    taxable_conso = row[8]

                    uniform_entry_conso.delete(0, END)
                    uniform_entry_conso.insert(0, (uniform_conso))

                    rice_entry_conso.delete(0, END)
                    rice_entry_conso.insert(0, (rice_conso))

                    laundry_entry_conso.delete(0, END)
                    laundry_entry_conso.insert(0, (laundry_conso))

                    medical1_entry_conso.delete(0, END)
                    medical1_entry_conso.insert(0, (medical1_conso))

                    medical2_entry_conso.delete(0, END)
                    medical2_entry_conso.insert(0, (medical2_conso))

                    totalDem_entry_conso.delete(0, END)
                    totalDem_entry_conso.insert(0, (totaldem_conso))

                    otherForms_entry_conso.delete(0, END)
                    otherForms_entry_conso.insert(0, (otherforms_conso))
                # print(gross_pay_conso)
                # grosspay_save, uniform_save,rice_save,laundry_save,\
                #     medical1_save,medical2_save,totalDem_save,otherforms_save\

        
                    
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}") 
        
        gross_conso_cal = grosspay + float(gross_pay_conso)
        # this is for taxabale amount consolidated
        taxable_amount_conso_cal = taxable_amount + float(taxable_conso)
        # taxable_amount_conso_cal = taxable_amount + taxable_conso

# THIS PART IS FOR  COMPUTATION OF TAXWITHHELD
        taxWithheld = 0
        if taxable_amount_conso_cal > 0:
            cursor.execute("SELECT * FROM tax_table")
            query_result = cursor.fetchall()
            for row in query_result:

                amountFrom_tax = float(row[1]) 

                amountTo_tax = float(row[2])
                baseAmount_tax = float(row[3]) 
                percentage_tax = float(row[4])
                if taxable_amount_conso_cal >= amountFrom_tax and taxable_amount_conso_cal <= amountTo_tax:

                    taxbase = baseAmount_tax
                    cal = taxable_amount_conso_cal - amountFrom_tax
                    if cal <= 0:
                        cal = 0
                        taxWithheld = baseAmount_tax + (cal * percentage_tax)
                    else:
                        cal = cal
                        taxWithheld = baseAmount_tax + (cal * percentage_tax)

        else:
            taxWithheld = 0

        taxWithheld2 = '{:.2f}'.format(taxWithheld)
        taxWitheld_entry.delete(0, END)
        taxWitheld_entry.insert(0, (taxWithheld2))


        # print(gross_conso_cal)
        # print(taxable_amount_conso_cal)
        # try:
            

        # except Exception as ex:
        # messagebox.showerror("Error", f"Error due to :{str(ex)}") 
    

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
                proviRateOTcal + proviRateSunCal + proviSunRateOTcal + nightdiffCal + adjustmentCal + float(allowance_search))
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

    global ca_deduct
    global allowance_search
    global on_off_saving
    allowance_search = 0

    on_off_deterent = ''

    cursor.execute("SELECT employee_id, lastName, firstName, position, salary_rate\
              FROM employee_details where employee_id  = '" + empID + "' ")

    fetch = cursor.fetchall()
    

    # ("Head Office", "Admin-Site", "Pampanga", "Rizal-R&F")

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
        cursor.execute("SELECT employee_id, lastName, firstName, position, salary_rate, Salary_Detail,off_on_details,taxCode \
                                  FROM employee_details where employee_id  = '" + empID + "' ")

        fetch = cursor.fetchall()
        mwe = 0
        # this statement is for getting the mwe per propective place !!!!!
        if department_list.get() == "Rizal-R&F" or   department_list.get() == "Admin-Site" :
            mwe = float(373)
        elif  department_list.get() == "Head Office":
            mwe = float(537)
        elif  department_list.get() == "Pampanga":
            mwe = float(420)
        
        # this is for determination of on & off employee!!!
        
        on_off_saving = ''
        for data in fetch:

            id_num = data[0]
            lname = data[1]
            fname = data[2]
            post = data[3]
            salaryRate = float(data[4])
            details   = data[5]
            on_off_saving = data[6]
            tax_mwe_search = data[7]

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

            tax_mwe_entry.delete(0, END)
            tax_mwe_entry.insert(0, (tax_mwe_search))


            # if salaryRate <= on_off_deterent and \
            #     department_list.get() == "Rizal-R&F":
            #     on_off_saving = 'off'
            # if salaryRate <= on_off_deterent and department_list.get() == "Pampanga":
            #     on_off_saving = 'off'
            # else:
            #     on_off_saving = 'on'

# this function is for searching of allowance for employee if there is !!!
    try:

        cursor.execute("SELECT allowance\
                FROM allowance where employee_id  = '" + empID + "' ")

        fetch = cursor.fetchall()
        row_count = cursor.rowcount

        if row_count == 0:
            allowance_search = 0
            allowance_search2 =  '{:,.2f}'.format(allowance_search)
            allowance_entry.delete(0, END)
            allowance_entry.insert(0, (allowance_search2))
        else:

            cursor.execute("SELECT allowance\
                    FROM allowance where employee_id  = '" + empID + "' ")

            myresult = cursor.fetchall()

            for row in myresult:
                allowance_search = row[0]
                allowance_search2 =  '{:,.2f}'.format(row[0])

                allowance_entry.delete(0, END)
                allowance_entry.insert(0, (allowance_search2))

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")       

    # print(on_off_saving)
 # this function is for getting the cash advance  deduction
    cursor.execute("SELECT employee_id,ca_deduction\
                            FROM cash_advance\
                            WHERE employee_id ='" + empID + "'  \
                    ")

    fetch = cursor.fetchall()
    row_count = cursor.rowcount

    if row_count == 0:
        ca_deduct = 0
        ca_deduct2 = '{:.2f}'.format(ca_deduct)
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
            ca_deduct2 = '{:.2f}'.format(ca_deduct)
            cashAdvance_entry.delete(0, END)
            cashAdvance_entry.insert(0, (ca_deduct2))


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

    allowance_label = Label(payroll_frame, text='Allowance:', width=10, height=1, bg='yellow', fg='gray',
                      font=('Arial', 10), anchor='e')
    allowance_label.place(x=10, y=360)

    global allowance_entry
    allowance_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    allowance_entry.place(x=200, y=360)

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
    sss_label = Label(payroll_frame, text='Tax/MWE:', width=10, height=1, bg='yellow', fg='gray',
                             font=('Arial', 10), anchor='e')
    sss_label.place(x=595, y=35)

    global tax_mwe_entry
    tax_mwe_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    tax_mwe_entry.place(x=685, y=35)

    
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

#===================This is for consolidated function!!!!======================================================
    
    global checkvar2
    checkvar2 = IntVar()
    checkbutton2 = Checkbutton(payroll_frame, text ="Consolidated", variable = checkvar2,\
                               onvalue = 1, offvalue = 0, height = 1, width = 15)
    checkbutton2.place(x =475,y=5)

    global payCal_conso_date
    payCal_conso_date = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    payCal_conso_date.place(x=620, y=5)
    payCal_conso_date.configure(justify='center')

    global uniform_entry_conso
    uniform_entry_conso = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    uniform_entry_conso.place(x=980, y=8)
    # uniform_entry_conso.bind("<KeyRelease>",computation_cosolidated)

    global rice_entry_conso
    rice_entry_conso = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    rice_entry_conso.place(x=980, y=33)

   

    global laundry_entry_conso
    laundry_entry_conso = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    laundry_entry_conso.place(x=980, y=58)

   

    global medical1_entry_conso
    medical1_entry_conso = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    medical1_entry_conso.place(x=980, y=83)

    

    global medical2_entry_conso
    medical2_entry_conso = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right')
    medical2_entry_conso.place(x=980, y=108)

   

    global totalDem_entry_conso
    totalDem_entry_conso = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right', fg='red')
    totalDem_entry_conso.place(x=980, y=133)

    global otherForms_entry_conso
    otherForms_entry_conso = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right', fg='red')
    otherForms_entry_conso.place(x=980, y=158)

    

    btn_netpay_conso = Button(payroll_frame, text="Cosolidation ", bg='gray', fg='yellow', font=('arial', 9),
                                width=12, command= computation_cosolidated)
    btn_netpay_conso.place(x=870, y=310)
    btn_netpay_conso.bind('<Return>', computation_cosolidated)

    btn_netpay_conso_cal = Button(payroll_frame, text="Net Pay Conso ", bg='white', fg='black', font=('arial', 9),
                                width=12, command= net_pay_conso_calculation)
    btn_netpay_conso_cal.place(x=970, y=310)
    btn_netpay_conso_cal.bind('<Return>', net_pay_conso_calculation)




#"""This button is for Salary Computation with function def!!!!"""

    btn_salaryComp = Button(payroll_frame, text="CalCulate Gross", bg='green', fg='white', font=('arial', 9), width=15,
                        command=gross_computation)
    btn_salaryComp.place(x=477, y=285)
    btn_salaryComp.bind('<Return>', gross_computation)

    global btn_saveComp
    btn_saveComp = Button(payroll_frame, text="Save", bg='yellowgreen', fg='black', font=('arial', 9), width=15,
                            command=save_payroll)
    btn_saveComp.place(x=990, y=205)
    btn_saveComp.bind('<Return>', save_payroll)

    btn_printPayroll = Button(payroll_frame, text="Print Payroll", bg='khaki', fg='red', font=('arial', 9), width=15,
                          command=print_payroll)
    btn_printPayroll.place(x=990, y=235)
    btn_printPayroll.bind('<Return>', print_payroll)

    btn_update_payroll = Button(payroll_frame, text="Update Payroll", bg='cyan', fg='red', font=('arial', 9), width=15,
                          command=update_salary_comp)
    btn_update_payroll.place(x=990, y=265)
    btn_update_payroll.bind('<Return>', update_salary_comp)

# This function is for for treeview for payroll computation!!!!

    payCal_date_label = Label(payroll_frame, text='Date from:', width=10, height=1, bg='white', fg='black',
                          font=('Arial', 10), anchor='e')
    payCal_date_label.place(x=340, y=360)

    global payCal_search_date
    payCal_search_date = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    payCal_search_date.place(x=440, y=360)
    payCal_search_date.configure(justify='center')


    global payCal_search_date_to
    
    payCal_search_date_to = DateEntry(payroll_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    payCal_search_date_to.place(x=580, y=360)
    payCal_search_date_to.configure(justify='center')

    btn_search_treview = Button(payroll_frame, text="Search", bg='white', fg='red', font=('arial', 9), width=15,
                          command=payroll_comp_treeview_display)
    btn_search_treview.place(x=700, y=360)
    btn_search_treview.bind('<Return>', payroll_comp_treeview_display)


# this is for transaction id Search!!!

    global  id_searchTrans_entry
    id_searchTrans_entry = Entry(payroll_frame, width=10, font=('Arial', 10), justify='right', fg='red')
    id_searchTrans_entry.place(x=820, y=360)

    btn_searchTrans_treview = Button(payroll_frame, text="Search ID", bg='white', fg='red', font=('arial', 9), width=15,
                          command=search_id_trans_edit)
    btn_searchTrans_treview.place(x=920, y=360)
    btn_searchTrans_treview.bind('<Return>', search_id_trans_edit)


# this is for treeview for payroll computation
    payroll_view_Form = Frame(payroll_frame, width=500, height=25)
    payroll_view_Form.place(x=15, y=390)

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
                                             columns=("COUNT",'TRANS ID', "EMPLOYEEID",
                                              "LASTNAME", "FIRSTNAME",
                                              "GROSSPAY",'NETPAY'),
                                             selectmode="extended", height=6, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=payroll_computation_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=payroll_computation_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    payroll_computation_treeview.heading('COUNT', text="COUNT", anchor=CENTER)
    payroll_computation_treeview.heading('TRANS ID', text="TRANS ID", anchor=CENTER)
    payroll_computation_treeview.heading('EMPLOYEEID', text="EMPLOYEE ID", anchor=CENTER)
    payroll_computation_treeview.heading('LASTNAME', text="LAST NAME", anchor=CENTER)
    payroll_computation_treeview.heading('FIRSTNAME', text="FIRST NAME", anchor=CENTER)
    payroll_computation_treeview.heading('GROSSPAY', text="GROSSPAY", anchor=CENTER)
    payroll_computation_treeview.heading('NETPAY', text="NET PAY", anchor=CENTER)


    payroll_computation_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    payroll_computation_treeview.column('#1', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#2', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#3', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#4', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#5', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#6', stretch=NO, minwidth=0, width=150, anchor='e')
    payroll_computation_treeview.column('#7', stretch=NO, minwidth=0, width=150, anchor='e')



    
    payroll_computation_treeview.pack()




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
    # update_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    update_time = datetime.now()
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
    on_off = on_off_reg_entry.get()
    sala_details = salaryDetail_reg_entry.get()
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
                position='" + position_update + "',\
                Salary_Detail='" + sala_details + "',\
                off_on_details ='" + on_off + "'\
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
                    on_off_sch = row[23]
                    



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
                    
                    on_off_reg_entry.delete(0, END)
                    on_off_reg_entry.insert(0, (on_off_sch))

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")

def employee_registry():
    """This function is to insert employee or Employee Registry"""
    # ts = time.time()
    mydb._open_connection()
    cursor = mydb.cursor()
    user_name = userName_entry.get()
    # update_time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    update_time = datetime.now()
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
                    "Salary_Detail, user, update_date,off_on_details)" 
                                       
                    " VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                    "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,"
                    "%s,%s,%s,%s,%s)",

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
                     update_time,on_off_reg_entry.get()))

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

    on_off_reg_lbl = Label(payroll_frame, text='On & Off Details:', width=11, height=1, bg='red', fg='white',
                           font=('Arial', 10), anchor='e')
    on_off_reg_lbl.place(x=270, y=55)



    global on_off_reg_entry
    on_off_reg_entry = ttk.Combobox(payroll_frame, width=11, font=('Arial', 10))
    on_off_reg_entry['values'] = ("on", "off")
    on_off_reg_entry.place(x=370, y=55)

    salaryDetail_reg_lbl = Label(payroll_frame, text='Salary Details:', width=11, height=1, bg='red', fg='white',
                            font=('Arial', 10), anchor='e')
    salaryDetail_reg_lbl.place(x=270, y=80)

    global salaryDetail_reg_entry
    salaryDetail_reg_entry = ttk.Combobox(payroll_frame, width=11, font=('Arial', 10))
    salaryDetail_reg_entry['values'] = ("Monthly", "Daily")
    salaryDetail_reg_entry.place(x=370, y=80)

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
    btn_save_employeeDetails.place(x=300, y=120)
    btn_save_employeeDetails.bind('<Return>', employee_registry)

    btn_update_employeeDetails = Button(payroll_frame, text='Update', bd=2, bg='yellow', fg='gray',
                                      font=('arial', 10), width=10, height=1, command=employee_update)
    btn_update_employeeDetails.place(x=400, y=120)
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

    btn_payroll_export = Button(MidViewForm9, text='Export Excel', bd=2, bg='blue', fg='white',
                                 font=('arial', 12), width=15, height=2, command=payroll_excel_export_frame)
    btn_payroll_export.place(x=2, y=280)
    btn_payroll_export.bind('<Return>', payroll_excel_export_frame)

    btn_payroll_comp2 = Button(MidViewForm9, text='Payroll Computation 2', bd=2, bg='blue', fg='white',
                                 font=('arial', 12), width=15, height=2, command=payroll_excel_export_frame)
    btn_payroll_comp2.place(x=2, y=340)
    btn_payroll_comp2.bind('<Return>', payroll_excel_export_frame)

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
    filemenu3.add_command(label="Clients Registration")
    filemenu3.add_command(label="Daily Transactions")
    filemenu4.add_command(label="Accounting Module")
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