import mysql.connector
from reportlab.lib import colors, pagesizes
from tabulate import tabulate
from prettytable import PrettyTable
import xlsxwriter
from os import startfile
import csv

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate,Paragraph,Table,TableStyle
from PollyReports import *


from datetime import date, timedelta


mydb = mysql.connector.connect(
            host="192.46.225.247",
            user="joeysabusido",
            password="Genesis@11",
            database="ldglobal",
            auth_plugin='mysql_native_password')
cursor = mydb.cursor()

# THIS IS TO CREATE TABLE FOR allowance
cursor.execute(
        "CREATE TABLE IF NOT EXISTS allowance (employee_id VARCHAR(250),\
             lastname VARCHAR(250) ,\
              firstname VARCHAR(250),\
                allowance DECIMAL (18,2),\
                id INT AUTO_INCREMENT PRIMARY KEY)")
mydb.commit()

def selection():

    """This function is for selection of transactions"""
    print('1001-Search for Rental Summary')
    print('1002-Search for Equipment')
    print('1003-Search for employee activate and Below 475')
    print('1004-Search for employee activate and above 475')
    print('1005-Search for DT Driver')
    print('1006-Enter Employee Allowance')
    print('1007-Search for Payroll')
    print('1008-Delete Payroll')
    print('1009-Total Diesel')
    print('1010-Diesel Running Balance')
    print('1011-Cost Entry')
    print('1012-Calculate Cost')
    print('1013- Test Cost Entry')
    print('1014- Test Test')
    print('1015- Classification')
    print('1016- Testing Cost')
    print('1017- Inner Join')
    print('1018- Rental Export')
    print('1019- Update Employee')
    print('1020- MWE Employee Computation')
    print('x-Exit')

    ans = input('Please enter code for your Desire transactio: ')

    if ans == '1001':
        return search_rental_sum()
    elif ans == '1002':
        return search_for_equipment()
    elif ans == '1003':
        return search_for_employee_below475()
    elif ans == '1004':
        return search_for_employee_above475()

    elif ans == '1005':
        return search_for_employee_driver()

    elif ans == '1006':
        return insert_allowance()

    elif ans == '1007':
        return search_payroll()

    elif ans == '1008':
        return delete_payroll()

    elif ans == '1009':
        return search_totaldiesel()
    elif ans == '1010':
        return search_totaldiesel2()
    elif ans == '1011':
        return search_costEntry()
    elif ans == '1012':
        return calculate_cost()

    elif ans == '1013':
        return test_cost()

    elif ans == '1014':
        return test_test()

    elif ans == '1015':
        return classification()
    
    elif ans == '1016':
        return test_test2()

    elif ans == '1017':
        return innerjoin()

    elif ans == '1018':
        return rental_export()

    elif ans == '1019':
        return update_employee_details_on()

    elif ans == '1020':
        return mwe_selection()


    elif ans == 'x' or ans =='X':
        exit

def search_rental_sum():
    """This function is for searching Rental Data"""

    mydb._open_connection()
    cursor = mydb.cursor()
    
    date1 = input("Enter Date From: ")
    date2 = input("Enter Date To: ")


    query = "Select\
                equipment_id,\
                sum(total_rental_hour) as TotalRental\
                from equipment_rental\
                where transaction_date\
                BETWEEN '" + date1 + "' and\
                '" + date2 + "' \
                GROUP BY equipment_id \
                ORDER BY equipment_id \
                "
    cursor.execute(query)
    myresult = cursor.fetchall()

    #print(tabulate(myresult, headers =['Equipment ID','Total Hours'], tablefmt='psql'))



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

    menu = PrettyTable()
    menu.field_names=['ID','Total Hours']
        
    for emp in rental_report:
        menu.add_row([emp,
                    rental_report[emp]['totalHours']])
                                
        print(menu)
    selection()

def search_for_equipment():
    """This function is to search for Equipment"""

    mydb._open_connection()
    cursor = mydb.cursor()

    query = """
            Select * 
            from equipment_details
            order by equipment_id
            """
    cursor.execute(query)
    myresult = cursor.fetchall()

    equipment ={}
    for row in myresult:
        equipment.update({row[0]:
        {
            'id': row[0],
            'equipmentID': row[1],
            'rentalRate': row[5],

        }
        })

    
    menu = PrettyTable()
    menu.field_names=['ID','EQUIPMENT ID','RENTAL RATE']
        
    for emp in equipment:      
        menu.add_row([emp,
                    equipment[emp]['equipmentID'],
                    equipment[emp]['rentalRate']])            
    print(menu)


def search_for_employee_below475():
    """This function is to query for employee <= 475"""

    mydb._open_connection()
    cursor = mydb.cursor()

    query = """
        SELECT employee_id,lastName,firstName,position,salary_rate
        FROM employee_details
        WHERE employment_status = 'Employeed' and 
        salary_rate <= 475
    """
    cursor.execute(query)
    myresult = cursor.fetchall()

    countTotal = 0

    for row in myresult:
        countTotal+=1


    print(tabulate(myresult, headers =['EMPLOYEE ID',
                                    'LAST NAME','FIRST NAME',
                                    'POSITION','SALARY RATE'], tablefmt='psql'))
    print('Total employee: ',countTotal)
    selection()

def search_for_employee_above475():
    """This function is to query for employee <= 475"""

    mydb._open_connection()
    cursor = mydb.cursor()

    query = """
        SELECT employee_id,lastName,firstName,position,salary_rate      
        FROM employee_details
        WHERE employment_status = 'Employeed' and
        salary_rate > 475
    """
    cursor.execute(query)
    myresult = cursor.fetchall()
    countTotal = 0

    for row in myresult:
        countTotal+=1
    

    print(tabulate(myresult, headers =['EMPLOYEE ID',
                                    'LAST NAME','FIRST NAME',
                                    'POSITION','SALARY RATE','TOTAL'], tablefmt='psql'))
    print('Total employee: ',countTotal)
    selection()

def search_for_employee_driver():
    """This function is to query for employee <= 475"""

    mydb._open_connection()
    cursor = mydb.cursor()
    dt = 'DT Driver'
    status = 'Employeed'

    #query = 'SELECT employee_id,lastName,firstName,position,salary_rate  FROM employee_details  WHERE employment_status = 'Employeed' and  salary_rate > 475 and position = '" + dt + "' \
    
    cursor.execute("SELECT employee_id,lastName,firstName,position,salary_rate \
                                  FROM employee_details\
                                where employment_status = '" + status + "' and  salary_rate <= 475\
                                     and position = '" + dt + "' ")

    # cursor.execute("SELECT employee_id,lastName,firstName,position,salary_rate \
    #      FROM employee_details \
    #     WHERE employment_status = 'Employeed' and  salary_rate < 475 and position = 'DT Driver' ")
    myresult = cursor.fetchall()
    countTotal = 0

    for row in myresult:
        countTotal+=1
    

    print(tabulate(myresult, headers =['EMPLOYEE ID',
                                    'LAST NAME','FIRST NAME',
                                    'POSITION','SALARY RATE','TOTAL'], tablefmt='psql'))
    print('Total employee: ',countTotal)
    selection()

def insert_allowance():
    """This function is to insert allowance for Employee"""
    mydb._open_connection()
    cursor = mydb.cursor()

    empID = input('Enter employee ID: ')
    lname = input('Enter Last Name: ')
    fname = input('Enter First Name: ')
    amount = input('Enter Allowance: ')

    try:
        cursor.execute("INSERT INTO allowance (employee_id,"
                           "lastname,firstname,allowance)"
                           
                           " VALUES(%s, %s, %s, %s)",

                           (empID, lname, fname, amount))

        mydb.commit()
        mydb.close()
        cursor.close()
        selection()
   
    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")

def search_payroll():
    """This function is to insert allowance for Employee"""
    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date to: ')

    cursor.execute("SELECT id,employee_id,last_name, SUM(grosspay_save) as totalGross,department,on_off_details,sum(taxwitheld_save) as TotalTaxW,\
                        sum(totalDem_save) as TotalDem, \
                        sum(otherforms_save) as Total_otherForms, sum(taxable_amount) as TotalAmount,taxable_mwe_detail,\
                            sum(cashadvance_save) as CashAdvance, cut_off_date \
                        FROM payroll_computation where cut_off_date BETWEEN '"+ date1 +"' and '"+ date2 +"' \
                      GROUP BY id,employee_id,last_name, department,on_off_details ,taxable_mwe_detail,cut_off_date")
   
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['ID','EMPLOYEE ID',
                                    'LAST NAME','GROSS PAY','DEPARTMENT','On & Off Status','Tax Widthheld','Total Deminimis','OTHERFORMS',
                                    'Tax Amount','Tax/MWE','Cash Advance','Cut off'], tablefmt='psql'))
    
def delete_payroll():
    

    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date to: ')

    cursor.execute("SELECT id,cut_off_date,employee_id,last_name, SUM(grosspay_save) as totalGross,department,on_off_details \
                        FROM payroll_computation where cut_off_date BETWEEN '"+ date1 +"' and '"+ date2 +"' \
                      GROUP BY id,employee_id,last_name, department,on_off_details ")
   
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['ID','DATE','EMPLOYEE ID',
                                    'LAST NAME','GROSS PAY','DEPARTMENT','On & Off Status'], tablefmt='psql'))

    transID = input('Enter trans id :  ')

    cursor.execute("Delete from payroll_computation where id = '"+ transID +"' ")
    mydb.commit
    mydb.close

    mydb._open_connection()
    cursor = mydb.cursor()

    cursor.execute("SELECT id,employee_id,last_name, SUM(grosspay_save) as totalGross,department,on_off_details \
                        FROM payroll_computation  \
                      GROUP BY id,employee_id,last_name, department,on_off_details ")
   
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['ID','EMPLOYEE ID',
                                    'LAST NAME','GROSS PAY','DEPARTMENT','On & Off Status'], tablefmt='psql'))

    selection()

def search_totaldiesel():
    """This function is to insert allowance for Employee"""
    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date to: ')

    cursor.execute("SELECT sum(use_liter) as totaldiesel FROM diesel_consumption \
                    where transaction_date BETWEEN '"+ date1 +"' and '"+ date2 +"' \
                      ")
   
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['TOTAL DIESEL'], tablefmt='psql'))
    selection()

def search_totaldiesel2():
    """This function is to insert allowance for Employee"""
    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date to: ')

    cursor.execute("SELECT equipment_id, sum(use_liter) as totaldiesel FROM diesel_consumption \
                    where transaction_date BETWEEN '"+ date1 +"' and '"+ date2 +"' \
                      GROUP BY equipment_id ORDER BY equipment_id ")
    
    diesel ={}
    count = 0
    balance = 0
    myresult = cursor.fetchall()

    for row in myresult:
        count+= 1
        totaldiesel = row[1]
        balance+= totaldiesel
        totaldiesel1 = '{:,.2f}'.format(totaldiesel)
        balance2 = '{:,.2f}'.format(balance)

        diesel.update({row[0]:
        {
            'totalDiesel': totaldiesel1,
            'balance': balance2,
            'count': count
        }
        })

    
    menu = PrettyTable()
    menu.field_names=['EQUIPMENT ID','TOTAL LITERS','RUNNING BALANCE','COUNT']
        
    for emp in diesel:      
        menu.add_row([emp,
                    diesel[emp]['totalDiesel'],
                    diesel[emp]['balance'],
                    diesel[emp]['count']])            
    print(menu)
    selection()



def search_costEntry():
    """This function is to insert allowance for Employee"""
    mydb._open_connection()
    cursor = mydb.cursor()

    cursor.execute("Select * from cost_entry")
    myresult = cursor.fetchall()

    for row in myresult:
        print(row)
   
def calculate_cost():
    """This function is to calculate """

    mydb._open_connection()
    cursor = mydb.cursor()
    
    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')

    

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

    transDate = ''
    equipID = ''
    rental_hour = 0
    totalrow = 0

    rental_report = {}
    for i in myresult:
        data = {i[0]:
                    {'totalHours': i[1],
                    'total_rental_amount': i[2]
                     }
                }

        rental_report.update(data)

    for j in rental_report:
        equipmID = j
        total1 = rental_report[j]['totalHours']

        query2 = "Select\
                    equipment_id,\
                    sum(use_liter) as diesel,\
                    sum(amount) as totalAmount \
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
                         {'totalliters': h[1],
                            'totalAmount': h[2]
                          }
                     }
            diesel_report.update(data2)
        liters_per_hour = 0
        for k in diesel_report:
            total2 = diesel_report[k]['totalliters']
            # if k == j:
            #     # liters_per_hour = diesel_report[k]['totalliters'] / rental_report[j]['totalHours']
            #     liters_per_hour =  total2 / total1
            #     liters_per_hour2 = '{:,.2f}'.format(liters_per_hour)
            #     # print(f'Liters/Hour: {liters_per_hour2}')
            #     totalliters =diesel_report[k]['totalliters']
            #     totalliters2 = '{:,.2f}'.format(totalliters)

            #     totalhours= rental_report[j]['totalHours']
            #     totalhours2 = '{:,.2f}'.format(totalhours)
            #     print(k,totalhours2,totalliters2, liters_per_hour2)
            

           

            query2 = "Select\
                    equipment_id, clasification,\
                    sum(cost_amount) as TotalCost\
                    from cost_entry\
                    where trans_date\
                    BETWEEN '" + date1 + "' and\
                    '" + date2 + "'  \
                    GROUP BY equipment_id,clasification \
                "
            cursor.execute(query2)
            myresult = cursor.fetchall()

            cost_report = {}
            for c in myresult:
                data2 = {c[0]:
                            {'classification': c[1],
                             'totalCost': c[2]
                            }
                        }
                cost_report.update(data2)
            total_cost = 0
            totalhours= 0
            total_dieselAmount = 0
            costing = 0
            cost_per_equipment = 0

            workbook = xlsxwriter.Workbook("cost.xlsx")
            worksheet = workbook.add_worksheet('rental')
            
            worksheet.write('A1', 'EQUIPMENT ID')
            worksheet.write('B1', 'TOTAL RENTAL HOURS')
            worksheet.write('C1', 'TOTAL DIESEL AMOUNT')
            worksheet.write('D1', 'EXPENSES')
            worksheet.write('E1', 'TOTAL EXPENSE')
            worksheet.write('F1', 'COST PER EQUIPMENT')
                
            
            
            rowIndex = 2


            for cost in cost_report:
               

                
                if k == cost and cost == j :
                    
                    totalhours= rental_report[j]['totalHours']
                    totalhours2 = '{:,.2f}'.format(totalhours)

                    total_dieselAmount =diesel_report[k]['totalAmount']
                    total_dieselAmount2 = '{:,.2f}'.format(total_dieselAmount)


                    costing =cost_report[cost]['totalCost']
                    costing2 = '{:,.2f}'.format(costing)

                    totalCost = total_dieselAmount + costing
                    totalCost2 = '{:,.2f}'.format(totalCost)

                    cost_per_equipment = totalCost / totalhours
                    cost_per_equipment2 = '{:,.2f}'.format(cost_per_equipment)

                    # print(k, totalhours2, total_dieselAmount2,  costing2, totalCost2, cost_per_equipment2)
                    # print('')

                    
                    
            
                    worksheet.write('A' + str(rowIndex),k)
                    worksheet.write('B' + str(rowIndex),totalhours)
                    worksheet.write('C' + str(rowIndex),total_dieselAmount)
                    worksheet.write('D' + str(rowIndex), costing)
                    worksheet.write('E' + str(rowIndex),totalCost)
                    worksheet.write('F' + str(rowIndex),cost_per_equipment)
                    
                
                    
                    rowIndex += 1

                    workbook.close()
                    

            # from os import startfile
            # startfile("cost.xlsx")

                # selection()

def test_cost():
    """This is for testing only for data for cost entry"""
    mydb._open_connection()
    cursor = mydb.cursor()
    
    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')

    query2 = "Select\
                    equipment_id, clasification,\
                    sum(cost_amount) as TotalCost\
                    from cost_entry\
                    where trans_date\
                    BETWEEN '" + date1 + "' and\
                    '" + date2 + "'  \
                    GROUP BY equipment_id,clasification \
                "
    cursor.execute(query2)
    myresult = cursor.fetchall()

    cost_report = {}
    for c in myresult:
        data2 = {c[0]:
                    {'classification': c[1],
                        'totalCost': c[2]
                    }
                }
        cost_report.update(data2)
    for row in cost_report:

        print(row,cost_report[row]['classification'],cost_report[row]['totalCost'])

def test_test():
    """This is for testing only for data for cost entry"""
    mydb._open_connection()
    cursor = mydb.cursor()
    
    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')

    query2 = "Select\
                    equipment_id,\
                    sum(use_liter) as diesel,\
                    sum(amount) as totalAmount \
                    from diesel_consumption\
                    where transaction_date\
                    BETWEEN '" + date1 + "' and\
                    '" + date2 + "'  \
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

           
            print(equipID_cost, amount_cost)

        
        # print(tabulate(myresult, headers =['EQUIPMENT ID','CLASSIFICATION','AMOUNT'], tablefmt='psql'))

def classification():
    """This function is for displaying classificaion"""
    mydb._open_connection()
    cursor = mydb.cursor()
    
    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')

    query2 = "Select\
                        clasification,\
                        sum(cost_amount) as TotalCost\
                        from cost_entry\
                        where trans_date\
                        BETWEEN '" + date1 + "' and\
                        '" + date2 + "'  \
                        GROUP BY clasification \
                    "
    cursor.execute(query2)
    myresult = cursor.fetchall()

    
    print(tabulate(myresult, headers =['EQUIPMENT ID','CLASSIFICATION','AMOUNT'], tablefmt='psql'))


def test_test2():
    """This is for testing only for data for cost entry"""
    mydb._open_connection()
    cursor = mydb.cursor()
    
    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')

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

            file_name = 'cost_report'
            pdf = SimpleDocTemplate(file_name + '.pdf', pagesizes =(letter))

            flow_obj = []
            td =[['EQUIPMENT ID','TOTAL RENTAL HOURS','TOTAL DIESEL AMOUNT','EXPENSES','TOTAL EXPENSE','COST PER EQUIPMENT']]

            result = []
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

                

                data = [equipID_cost,totalhours2, total_dieselAmount2,
                        costing2,totalCost2,cost_per_equipment2]
                td.append(data)

               
                table = Table(td)
                ts = TableStyle([("GRID", (0,0), (1,1), 1, colors.red)

                ])
            
                table.setStyle(ts)
                flow_obj.append(table)
                pdf.build(flow_obj)

            # startfile("costing_report.pdf")

                

                # with open("cost.csv", "w",newline='') as file:

                #     fieldnames = ['EQUIPMENT ID','TOTAL RENTAL HOURS','TOTAL DIESEL AMOUNT','EXPENSES',\
                #         'TOTAL EXPENSE','COST PER EQUIPMENT']
                #     thewriter = csv.DictWriter(file,fieldnames=fieldnames)
                #     thewriter.writeheader()
                #     for row in myresult:
                #         thewriter.writerow({'EQUIPMENT ID':equipID_cost,'TOTAL RENTAL HOURS':totalhours,
                #                             'TOTAL DIESEL AMOUNT':total_dieselAmount,'EXPENSES': costing,
                #                             'TOTAL EXPENSE':totalCost,'COST PER EQUIPMENT':cost_per_equipment})

               
                        
               
                    # startfile("cost.csv")


                # print(equipID_cost, totalhours2, total_dieselAmount2, costing2, totalCost2, cost_per_equipment2)
              
def innerjoin():
    """This function is for inner join""" 

    mydb._open_connection()
    cursor = mydb.cursor()
    
    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')


    query = "Select equipment_rental.equipment_id,\
            sum(equipment_rental.total_rental_hour) as TotalRental,\
            sum(cost_entry.cost_amount) as TotalAmount\
            from equipment_rental\
            INNER JOIN cost_entry\
                ON equipment_rental.equipment_id = cost_entry.equipment_id\
            where transaction_date\
            BETWEEN '" + date1 + "' and\
            '" + date2 + "' \
            GROUP BY equipment_rental.equipment_id, cost_entry.equipment_id, equipment_rental.total_rental_hour,cost_entry.cost_amount\
                "
    cursor.execute(query)
    myresult = cursor.fetchall()

    for row in myresult:
        print(row)

def rental_export():
    """This function is for generating Excel for Rental"""

    mydb._open_connection()
    cursor = mydb.cursor()
    
    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')

    workbook = xlsxwriter.Workbook("rental_report.xlsx")
    worksheet = workbook.add_worksheet('rental')
    
    worksheet.write('A1', 'EQUIPMENT ID')
    worksheet.write('B1', 'TOTAL RENTAL HOURS')
    worksheet.write('C1', 'RENTAL RATE')
    worksheet.write('D1', 'TOTAL AMOUNT ')
  

    rowIndex = 2
    query = "Select\
                equipment_id,\
                sum(total_rental_hour) as TotalRental,\
                rental_rate,\
                sum(rental_amount) as TotalRental \
                from equipment_rental\
                where transaction_date\
                BETWEEN '" + date1 + "' and\
                '" + date2 + "' \
                GROUP BY equipment_id,rental_rate \
                "
    cursor.execute(query)
    myresult = cursor.fetchall()

    for row  in myresult:
        equipID_rental = row[0]
        total_rental_hour = row[1]
        total_rental_rate = row[2]
        total_rental_amount = row[3]

        worksheet.write('A' + str(rowIndex),equipID_rental)
        worksheet.write('B' + str(rowIndex),total_rental_hour)
        worksheet.write('C' + str(rowIndex),total_rental_rate)
        worksheet.write('D' + str(rowIndex),total_rental_amount)
       
    
        rowIndex += 1

    workbook.close()
            

        # from os import startfile
    startfile("rental_report.xlsx")


def update_employee_details_on():
    """This function is to update employee for on off details"""

    mydb._open_connection()
    cursor = mydb.cursor()

    query ='Select employee_id,lastName,firstName,\
            salary_rate, taxCode,off_on_details,user,update_date,id from employee_details ORDER BY employee_id'
    cursor.execute(query)
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers =['ID','LAST NAME', 'FIRST NAME',
                                       'SALARY RATE','TAX CODE','On/Off Details',
                                       'USER','TIME','ID'], tablefmt='psql'))

    employeeID = input("Enter employee ID: ")
    off_on_Details = input("Enter details on/off: ")

    key = input("Would you like to update data yes/no?: ").lower()

    if key == 'yes':

        cursor.execute(
                    "UPDATE employee_details SET off_on_details ='"+ off_on_Details +"'\
                    WHERE employee_id =%s", (employeeID,)
                )
        mydb.commit()
        mydb.close()
        cursor.close()
        print("Data has been updated")
        print('')

        update_employee_details_on()
    else:
        selection()

def test_on():
    """This function is for test of on query"""
    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')
    miminum_wage = str(420)

    # cursor.execute("SELECT employee_id,on_off_details\
    #                    FROM payroll_computation \
    #                    where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
    #                      and on_off_details = 'on' ")

    cursor.execute("SELECT sum(grosspay_save) as GROSS, SUM(total_mandatory) AS TOTALMAN\
                       FROM payroll_computation \
                       where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                         and on_off_details = 'on' ")


    myresult = cursor.fetchall()
    print(tabulate(myresult, headers =['Gross','Total Mandatory'], tablefmt='psql'))


def update_employee_details_mwe_taxable():
    """This function is to update employee for on off details"""

    mydb._open_connection()
    cursor = mydb.cursor()

    query ='Select employee_id,lastName,firstName,\
            salary_rate, taxCode,off_on_details,user,update_date,id from employee_details ORDER BY employee_id'
    cursor.execute(query)
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers =['ID','LAST NAME', 'FIRST NAME',
                                       'SALARY RATE','TAX CODE','On/Off Details',
                                       'USER','TIME','ID'], tablefmt='psql'))

    employeeID = input("Enter employee ID: ")
    omwe_Details = input("Enter details Taxble/MWE: ")

    key = input("Would you like to update data yes/no?: ").lower()

    if key == 'yes':

        cursor.execute(
                    "UPDATE employee_details SET taxCode ='"+ omwe_Details +"'\
                    WHERE employee_id =%s", (employeeID,)
                )
        mydb.commit()
        mydb.close()
        cursor.close()
        print("Data has been updated")
        print('')

        update_employee_details_mwe_taxable()


def mwe_selection():
    """This function is for MWE """

    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')

    cursor.execute("SELECT \
                       employee_id,last_name,grosspay_save\
                       FROM payroll_computation \
                       where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                        AND  taxable_mwe_detail = 'MWE'  and on_off_details = 'on' ")

    myresult = cursor.fetchall()
    print(tabulate(myresult, headers =['EMPLOYEE ID','LASTNAME','GROSS PAY'], tablefmt='psql'))

def mwe_1601c_print():
    """This is for sample only for mwe for 1601c"""

    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')

    cursor.execute("SELECT employee_id, last_name, sum(grosspay_save) as GROSS, SUM(total_mandatory) AS TOTALMAN,\
                       sum(regularday_ot_cal) as REGOT,sum(regularsunday_ot_cal) as SUNOT,\
                       sum(spl_ot_cal) as SPLOT,sum(legal_day_ot_cal) as LGL2OT,\
                       sum(proviRate_day_ot_cal) as PROVIOT,sum(provisun_day_ot_cal) as PROVISUNOT,\
                       sum(nightdiff_day_cal) as NDIFF \
                       FROM payroll_computation \
                       where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                        AND  taxable_mwe_detail = 'MWE'  and on_off_details = 'on'\
                            GROUP BY employee_id, last_name ")

    myresult = cursor.fetchall()

    for row in myresult:
        empID = row[0]
        lastName = row[1]

def total_notsubject():
    """This is not subject to tax"""
    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date To: ')

    workbook = xlsxwriter.Workbook("notsubject.xlsx")
    worksheet = workbook.add_worksheet('notsubject')
    worksheet.write('A1', 'EMPLOYEE ID')
    worksheet.write('B1', 'LASTNAME')
    worksheet.write('C1', 'NOT SUBJECT')

    rowIndex = 2
    cursor.execute("SELECT employee_id, last_name, sum(taxable_amount) as totaltaxable_amount\
                                        FROM payroll_computation\
                                        where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "' \
                                            AND  taxable_mwe_detail = 'Taxable'  and on_off_details = 'on'\
                                            AND taxable_amount < 10417 \
                                                GROUP BY employee_id, last_name")
    myresult = cursor.fetchall()
    
    for data in myresult:
        empIDxlx = data[0]
        lastnamexlx = data[1]
        TAXaMOUNTxls = data[2]
    
        worksheet.write('A' + str(rowIndex),empIDxlx)
        worksheet.write('B' + str(rowIndex),lastnamexlx)
        worksheet.write('C' + str(rowIndex),TAXaMOUNTxls)

        rowIndex += 1

    workbook.close()
   
    # from os import startfile
    startfile("notsubject.xlsx")


def taxable_amount():
    """This is for taxable amount manual edit"""

    mydb._open_connection()
    cursor = mydb.cursor()

    search_payroll()
    transID = input('Enter Trans ID :')
    tax_amount = input('Enter Amount: ')

    key = input("Would you like to update data yes/no?: ").lower()

    if key == 'yes':
    
        cursor.execute(
            "UPDATE payroll_computation SET taxable_amount ='"+ tax_amount +"' \
                WHERE id = '" + transID + "' ")
        

        mydb.commit()
        mydb.close()
        cursor.close()

        print('data has been updated')

    taxable_amount()

def equipment_registry():
    """This function is for registration of Equipment"""
    mydb._open_connection()
    cursor = mydb.cursor()

    search_for_equipment()

    equipmentID = input('Enter Equipment ID :')
    rentalRate = input('Enter Rental Rate: ')


    try:
        cursor.execute("INSERT INTO equipment_details (equipment_id,"
                            "rental_rate)"
                            
                            " VALUES(%s, %s)",

                            (equipmentID, rentalRate))

        mydb.commit()
        mydb.close()
        cursor.close()
        
   
    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")

def insert_sssloan_deduction():
    mydb._open_connection()
    cursor = mydb.cursor()
    
    
    
    employee_id =input('Enter employee ID: ')
    last_name = input('Enter Last Name: ')
    first_name = input('Enter First Name: ')
    loan_deduction = input('Enter Amount Deduction: ')
    

    cursor.execute(
        "INSERT INTO sss_loanDeduction (employee_id,lastname,"
        "firstname,loan_deduction)"
        " VALUES(%s,%s,%s,%s)",
        (employee_id,last_name,first_name,loan_deduction))

    mydb.commit()
    mydb.close()
    cursor.close()
    

    
    key = input('would you like to Transact another: ').lower()
    if key == 'yes':
        return insert_sssloan_deduction()
    else:
        exit

def showdatabases():
    mydb._open_connection()
    cursor = mydb.cursor()

    query =("SHOW DATABASES")
    cursor.execute(query)
    
    for db in cursor:
        print(db)

def showtables():
    """This function is to show all Tables"""
    cursor.execute("Show tables;")
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['TABLE'], tablefmt='psql'))

    # for x in myresult:
    #     print(x)

def showColumns():
    query ='SHOW COLUMNS FROM ldglobal.employee_details;'
    cursor.execute(query)
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['TABLE'], tablefmt='psql'))

    # for x in myresult:
    #    print(x)

def show_sss_loandeduction():
    query ='Select * FROM sss_loanDeduction'
    cursor.execute(query)
    myresult = cursor
    for x in myresult:
        print(x)

def update_sssloan_deduction():
    mydb._open_connection()
    cursor = mydb.cursor()
    
    show_sss_loandeduction()
    
    trans_id =input('Enter id: ')
    employee_id =input('Enter Employee ID: ')
    loan_deduction = input('Enter Amount Deduction: ')
    

    cursor.execute(
        "UPDATE sss_loanDeduction SET loan_deduction='" + loan_deduction +"' \
            WHERE id = '" + trans_id +"' ")
       

    mydb.commit()
    mydb.close()
    cursor.close()
    

    
    key = input('would you like to Transact another: ').lower()
    if key == 'yes':
        return update_sssloan_deduction()
    else:
        exit

def cash_advance_data():
    """This function is for cash advance list"""
    mydb._open_connection()
    cursor = mydb.cursor()

    query ='Select * FROM cash_advance'
    cursor.execute(query)
    myresult = cursor
    for x in myresult:
        print(x)
def insert_equipment():
    """This function is to insert equipment"""   
    mydb._open_connection()
    cursor = mydb.cursor()

    equipID = input('Enter Equipment ID: ')
    rental_rate = input('Enter rental Rate: ')
    

    try:
        cursor.execute("INSERT INTO equipment_details (equipment_id,"
                           "rental_rate)"
                           
                           " VALUES(%s, %s)",

                           (equipID,rental_rate))

        mydb.commit()
        mydb.close()
        cursor.close()
        selection()
   
    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")

def edit_tax_table():
    """This function is for editing taxable"""
    mydb._open_connection()
    cursor = mydb.cursor()

    query ='SELECT * FROM ldglobal.tax_table;'
    cursor.execute(query)
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['ID', 'AMOUNT FROM','AMOUNT TO','AMOUNTBASE','PERCENTAGE'], tablefmt='psql'))

def search_payroll_withUpdate():
    """This function is to insert allowance for Employee"""
    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date to: ')

    cursor.execute("SELECT id,employee_id,last_name, SUM(grosspay_save) as totalGross,\
                        sum(otherforms_save) as Total_otherForms, sum(taxwitheld_save) as TotalAmount,\
                            sum(cashadvance_save) as CashAdvance, cut_off_date,on_off_details,taxable_amount \
                        FROM payroll_computation where cut_off_date BETWEEN '"+ date1 +"' and '"+ date2 +"' \
                      GROUP BY id,employee_id,last_name, cut_off_date,on_off_details,taxable_amount")
   
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['ID','EMPLOYEE ID',
                                    'LAST NAME','GROSS PAY''OTHERFORMS',
                                    'Tax Amount','Cash Advance','Cut off','On-Off','T-Amount'], tablefmt='psql'))

def diesel_search():
    """This function is to search for Diesel Registry"""

    mydb._open_connection()
    cursor = mydb.cursor()

    Date1 = input("Entry Date From: ")
    Date2 = input("Entry Date To: ")
    equipmentID = input('Equipment ID :')
    cursor.execute("Select \
            `transaction_date`,\
            `equipment_id` ,\
            `withdrawal_slip`, \
            `use_liter`, \
            `price`,\
            `amount`,\
            `id`\
            FROM  diesel_consumption\
            WHERE transaction_date BETWEEN '" + Date1 +"' AND '"+ Date2 + "' \
            AND equipment_id = '"+ equipmentID + "' \
            ORDER by id DESC\
                ")

    fetch = cursor.fetchall()

    print(tabulate(fetch, headers =['Date','Eqtp ID',
                                    'W Slip','Liter','price',
                                    'Amount','ID'], tablefmt='psql'))
    
def diesel_edit():
    """This function is to edit Diesel Registry"""
    mydb._open_connection()
    cursor = mydb.cursor()

    diesel_search()
    TransID = input('Transaction ID :')
    equipmentID = input('Equipment ID :')

    cursor.execute(
        "UPDATE diesel_consumption SET equipment_id='" + equipmentID +"' \
            WHERE id = '" + TransID +"' ")
       

    mydb.commit()
    mydb.close()
    cursor.close()
    

    
    key = input('would you like to Transact another: ').lower()
    if key == 'yes':
        return diesel_edit()
    else:
        exit


def search_for_splOT():
    """This function is for searching spl ot"""
    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input("Enter Date from :")
    date2 = input("Enter date to :")
    employeID = input("Enter EmpID: ")
    cursor.execute(
            "SELECT last_name,spl_ot\
            from payroll_computation \
                WHERE employee_id = '" + employeID +"' AND cut_off_date BETWEEN '" + date1 +"'AND '" + date2 +"' ")

    myresult = cursor.fetchall()

    for row in myresult:
        name1= row[0]
        spl_ot = row[1]

        print(name1)
        print(spl_ot)

def updatesalaryRate():
    """
    This function is to update salary rate
    of Employee

    """

    mydb._open_connection()
    cursor = mydb.cursor()

    query ='Select employee_id,lastName,firstName,\
            salary_rate, taxCode,off_on_details,user,update_date,id from employee_details ORDER BY employee_id'
    cursor.execute(query)
    myresult = cursor.fetchall()
    print(tabulate(myresult, headers =['ID','LAST NAME', 'FIRST NAME',
                                       'SALARY RATE','TAX CODE','On/Off Details',
                                       'USER','TIME','ID'], tablefmt='psql'))

    employeeID = input("Enter employee ID: ")
    salaryRate = input("Enter new Rate: ")

    key = input("Would you like to update data yes/no?: ").lower()

    if key == 'yes':

        cursor.execute(
                    "UPDATE employee_details SET salary_rate ='"+ salaryRate +"'\
                    WHERE employee_id =%s", (employeeID,)
                )
        mydb.commit()
        mydb.close()
        cursor.close()
        print("Data has been updated")
        print('')

        
    else:
        selection()


def comp13thMonth():
    """
    This function is for compution of 13 month fee
    for 
    """
    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter Date From : ')
    date2 = input('Enter date to : ')

    # department = 'Rizal-R&F'
    department = 'Pampanga'

    workbook = xlsxwriter.Workbook("site_13month.xlsx")
    worksheet = workbook.add_worksheet('rental')
    worksheet.write('A1', 'EMPLOYEE ID')
    worksheet.write('B1', 'LAST NAME')
    worksheet.write('C1', 'FIRST NAME')
    worksheet.write('D1', 'REGDAY CAL')
    worksheet.write('E1', 'REGSUN CAL')
    worksheet.write('F1', 'SPL CAL')
    worksheet.write('G1', 'LGL2 CAL')
    worksheet.write('H1', 'SHOP RATE CAL')
    worksheet.write('I1', 'PROVI RATE CAL')
    worksheet.write('J1', 'SUNDAY PROVI CAL')
    worksheet.write('K1', '13TH MONTH FEE CALL')
    worksheet.write('L1', 'DEPARTMENT')
   

    rowIndex = 2

    cursor.execute(
            "SELECT employee_id,last_name,\
                sum(regularday_cal)  as TotalRegday,\
                sum(regularsunday_cal) / 1.30  as TotalRegSun,\
                sum(spl_cal) / 1.30 as TotalSpl,\
                sum(legal_day_cal) / 2 as Totallgl2,\
                sum(shoprate_day_cal)  as Totalshoprate,\
                sum(proviRate_day_cal)  as TotalproviRate,\
                sum(provisun_day_cal)/1.30  as TotalproviSun,\
                first_name, department \
            from payroll_computation \
            WHERE cut_off_date BETWEEN '" + date1 +"'AND '" + date2 +"' AND department = '" + department +"' \
            GROUP BY employee_id ,last_name,first_name,department  ")

    # department = '" + department +"' AND \
    myresult = cursor.fetchall()
    count = 0
    for row in myresult:
        count+=1
        empId = row[0]
        lastName = row[1]
        regdayCal = row[2]
        regsunCal = row[3]
        splCal = row[4]
        lgl2Cal = row[5]
        shoprateCal = row[6]
        provirateCal = row[7]
        sunproviRateCal  = row[8]
        firstNameCal = row[9]
        Department = row[10]

        comp13th = float(regdayCal + regsunCal + splCal + lgl2Cal
                    + shoprateCal + provirateCal + sunproviRateCal) / 12

        comp13th_sample = float(regdayCal + regsunCal + splCal + lgl2Cal
                    + shoprateCal + provirateCal + sunproviRateCal)
        # print(empId, lastName, regdayCal,regsunCal,
        #  splCal, lgl2Cal, shoprateCal, provirateCal,
        #  sunproviRateCal, comp13th)
        # print(lastName,regdayCal,regsunCal,splCal,
        #       lgl2Cal,shoprateCal,provirateCal,
        #       sunproviRateCal,comp13th_sample)
        

        worksheet.write('A' + str(rowIndex),empId)
        worksheet.write('B' + str(rowIndex),lastName)
        worksheet.write('C' + str(rowIndex),firstNameCal)
        worksheet.write('D' + str(rowIndex),regdayCal)
        worksheet.write('E' + str(rowIndex),regsunCal)
        worksheet.write('F' + str(rowIndex),splCal)
        worksheet.write('G' + str(rowIndex),lgl2Cal)
        worksheet.write('H' + str(rowIndex),shoprateCal)
        worksheet.write('I' + str(rowIndex),provirateCal)
        worksheet.write('J' + str(rowIndex),sunproviRateCal)
        worksheet.write('K' + str(rowIndex),comp13th)
        worksheet.write('L' + str(rowIndex),Department)

        

        rowIndex += 1

    workbook.close()
    print('JRS', 'Data has been exported')    

    # from os import startfile
    startfile("site_13month.xlsx")
        
    print(count)


def computation_cosolidated():
    """This function is for computating cosolidation"""
    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter Date: ')
    # date2 = input('Enter Date to: ')
    
    date2 = str((date.fromisoformat(date1)) - timedelta(15))
    print(date2)
    # date2 = payCal_conso_date.get()
    empID_conso = input('Enter Employee ID: ')

   
    
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
            print("Error", "No record found during last payroll")
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

                
            print(gross_pay_conso)
            
    
                
                
#     except Exception as ex:
#         print("Error", f"Error due to :{str(ex)}") 
    
#     # gross_conso_cal = grosspay + float(gross_pay_conso)
#     # this is for taxabale amount consolidated
#     taxable_amount_conso_cal = 0 + float(taxable_conso)
#     # taxable_amount_conso_cal = taxable_amount + taxable_conso

# # THIS PART IS FOR  COMPUTATION OF TAXWITHHELD
#     taxWithheld = 0
#     if taxable_amount_conso_cal > 0:
#         cursor.execute("SELECT * FROM tax_table")
#         query_result = cursor.fetchall()
#         for row in query_result:

#             amountFrom_tax = float(row[1]) 

#             amountTo_tax = float(row[2])
#             baseAmount_tax = float(row[3]) 
#             percentage_tax = float(row[4])
#             if taxable_amount_conso_cal >= amountFrom_tax and taxable_amount_conso_cal <= amountTo_tax:

#                 taxbase = baseAmount_tax
#                 cal = taxable_amount_conso_cal - amountFrom_tax
#                 if cal <= 0:
#                     cal = 0
#                     taxWithheld = baseAmount_tax + (cal * percentage_tax)
#                 else:
#                     cal = cal
#                     taxWithheld = baseAmount_tax + (cal * percentage_tax)

#     else:
#         taxWithheld = 0

#     taxWithheld2 = '{:,.2f}'.format(taxWithheld)
    
#     print(taxWithheld2)


    
#     print(taxable_amount_conso_cal)
#         # try:
            

    except Exception as ex:
       
        print("Error", f"Error due to :{str(ex)}") 
    
def show_hdmf_loandeduction():
    query ='Select * FROM  HDMF_loanDeduction'
    cursor.execute(query)
    myresult = cursor
    for x in myresult:
        print(x)

def update_hdmfloan_deduction():
    mydb._open_connection()
    cursor = mydb.cursor()
    
    show_hdmf_loandeduction()
    
    trans_id =input('Enter id: ')
    employee_id =input('Enter Employee ID: ')
    loan_deduction = input('Enter Amount Deduction: ')
    

    cursor.execute(
        "UPDATE HDMF_loanDeduction SET loan_deduction='" + loan_deduction +"' \
            WHERE id = '" + trans_id +"' ")
       

    mydb.commit()
    mydb.close()
    cursor.close()
    

    
    key = input('would you like to Transact another: ').lower()
    if key == 'yes':
        return update_hdmfloan_deduction()
    else:
        exit

def UpdatetaxWithheld():
    """
    This function is to update Tax Withheld
    """
    search_payroll_withUpdate()

    # trans_id =input('Enter id: ')
    
    # tax_withheld_amount = input('Enter tax amount: ')


    # cursor.execute(
    #     "UPDATE payroll_computation SET taxwitheld_save='" + tax_withheld_amount +"' \
    #         WHERE id = '" + trans_id +"' ")
       

    # mydb.commit()

    key = input("Would you like to update data yes/no?: ").lower()

    while key == 'yes':
        trans_id =input('Enter id: ')
    
        tax_withheld_amount = input('Enter tax amount: ')


        cursor.execute(
            "UPDATE payroll_computation SET taxwitheld_save='" + tax_withheld_amount +"' \
                WHERE id = '" + trans_id +"' ")
        

        mydb.commit()

        key = input("Would you like to update data yes/no?: ").lower()
   

    print('Data has been updated')

    
    
def insert_cash_advance_data():
    """This function is for cash advance list"""
    mydb._open_connection()
    cursor = mydb.cursor()
    
    empID = input('Enter Emp ID:')
    lname = input('Last Name: ')
    fname = input('First Name:')
    amount_save = input('Enter Deduction Amount:')
    
    
    cursor.execute(
        "INSERT INTO cash_advance (employee_id,lastname,firstname,ca_deduction)"
        "VALUES(%s,%s,%s,%s)",
        (empID,lname,fname,amount_save))

    mydb.commit()
    mydb.close()
    cursor.close()
    print('Data has been saved')

def cf1604():
    """
    This function
    is for 1604cf
    """  
    
    mydb._open_connection()
    cursor = mydb.cursor()
    
    
    # Date_13thMonth = input('Enter Date for 13th Month:')
    date1 = input('Enter Date Beginning: ')
    date2 = input('Enter Date End:')
    
    workbook = xlsxwriter.Workbook("1604CF.xlsx")
    worksheet = workbook.add_worksheet('rental')
    worksheet.write('A1', 'EMPLOYEE ID')
    worksheet.write('B1', 'LAST NAME')
    worksheet.write('C1', 'FIRST NAME')
    worksheet.write('D1', 'GROSS PAY')
    worksheet.write('E1', 'TOTAL MANDATORY')
    worksheet.write('F1', 'OTHER FORMS')
    worksheet.write('G1', 'TAX WIDTHELD')
    worksheet.write('H1', 'TOTAL DEM')
    worksheet.write('I1', 'TOTAL TRANSACTIONS')
    worksheet.write('J1', 'FULL NAME')
   
   

    rowIndex = 2
    
    cursor.execute(
            "SELECT employee_id,last_name,first_name,\
                sum(grosspay_save)  as Totalgross,\
                sum(total_mandatory)   as TotalMandatory,\
                sum(otherforms_save)  as TotalOtherforms,\
                sum(taxwitheld_save)  as TotalTaxwidtheld,\
                sum(totalDem_save)  as TotalDem,\
                    count(employee_id) as TotalNumber\
            from payroll_computation \
            WHERE cut_off_date BETWEEN '" + date1 +"'AND '" + date2 +"'  \
            GROUP BY employee_id ,last_name,first_name \
            ORDER BY employee_id")

    myresult = cursor.fetchall()
    count = 0
    for row in myresult:
        count+=1
        empId = row[0]
        lastName = row[1].upper()
        firstName = row[2].upper()
        grossPay = row[3]
        totalMandatory = row[4]
        otherForms = row[5]
        taxwidtheld = row[6]
        totalDem = row[7]
        totalMonths = row[8]
        fullName = lastName + (' , ') + firstName
    
        # print(empId, lastName, firstName,grossPay,
        #       totalMandatory,otherForms,taxwidtheld,totalMonths)
        
        
        worksheet.write('A' + str(rowIndex),empId)
        worksheet.write('B' + str(rowIndex),lastName)
        worksheet.write('C' + str(rowIndex),firstName)
        worksheet.write('D' + str(rowIndex),grossPay)
        worksheet.write('E' + str(rowIndex),totalMandatory)
        worksheet.write('F' + str(rowIndex),otherForms)
        worksheet.write('G' + str(rowIndex),taxwidtheld)
        worksheet.write('H' + str(rowIndex),totalDem)
        worksheet.write('I' + str(rowIndex),totalMonths)
        worksheet.write('J' + str(rowIndex),fullName)
        
        

        rowIndex += 1

    workbook.close()
    print('JRS', 'Data has been exported')    

    # from os import startfile
    startfile("1604CF.xlsx")
    
def employee_salaryQuery():
    """
    This function is for searching
    salary of Employee
    """  
    mydb._open_connection()
    cursor = mydb.cursor()
    
    
    # Date_13thMonth = input('Enter Date for 13th Month:')
    empID = input('Enter Employee ID: ')
    date1 = input('Enter Date Beginning: ')
    date2 = input('Enter Date End:')
    
    workbook = xlsxwriter.Workbook("employeeSalary.xlsx")
    worksheet = workbook.add_worksheet('rental')
    worksheet.write('A1', '#')
    worksheet.write('B1', 'TRANS ID')
    worksheet.write('C1', 'DATE')
    worksheet.write('D1', 'EMPLOYEE ID')
    worksheet.write('E1', 'LAST NAME')
    worksheet.write('F1', 'FIRST NAME')
    worksheet.write('G1', 'ON/OFF DETAILS')
   
   
   
   

    rowIndex = 2
    
    
    cursor.execute(
            "SELECT id,cut_off_date,employee_id,last_name,first_name,on_off_details\
            from payroll_computation \
            WHERE cut_off_date BETWEEN '" + date1 +"'AND '" + date2 +"' \
                AND employee_id='" + empID +"'\
                ORDER BY cut_off_date")

    myresult = cursor.fetchall()
    count = 0
    for row in myresult:
        count+=1
        transID = row[0]
        cut_offDate = row[1]
        empId = row[2]
        lastName = row[3]
        firstName = row[4]
        trans = row[5]
        
    
        # print(transID, count,cut_offDate,empId, lastName, firstName,trans)
        
        worksheet.write('A' + str(rowIndex),count)
        worksheet.write('B' + str(rowIndex),transID)
        worksheet.write('C' + str(rowIndex),cut_offDate)
        worksheet.write('D' + str(rowIndex),empId)
        worksheet.write('E' + str(rowIndex),lastName)
        worksheet.write('F' + str(rowIndex),firstName)
        worksheet.write('G' + str(rowIndex),trans)
        
       
        

        rowIndex += 1

    workbook.close()
    print('JRS', 'Data has been exported')    

    # from os import startfile
    startfile("employeeSalary.xlsx")

def deleteCut_offPeriod():
    """
    This function is to delete cut-off 
    Period
    """  

    mydb._open_connection()
    cursor = mydb.cursor()

    query ='SELECT * FROM ldglobal.cut_off;'
    cursor.execute(query)
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['ID', 'DATE FROM','DATE TO','PAY DATE'], tablefmt='psql'))

    keyId = input("Enter id to Delete: ")

    cursor.execute("Delete from cut_off where id = '"+ keyId +"' ")

    print('Data has been deleted')

    mydb.commit
    mydb.close

def searchPayroll():
    """
    This function is for
    searching individual payroll
    """

    mydb._open_connection()
    cursor = mydb.cursor()


    date1 = input('Enter Date Beginning: ')
    date2 = input('Enter Date End:')
    empID =input('Enter employee ID: ')

    # query = "Select employee_id, last_name,first_name, \
    #             sum(taxwitheld_save)  as TotalTaxwidtheld\
    #             from payroll_computation \
    #             where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "'\
    #             AND employee_id = '" + empID + "' \
    #             GROUP BY employee_id ,last_name,first_name "

    query = "Select cut_off_date, employee_id, last_name,first_name, \
                taxwitheld_save\
                from payroll_computation \
                where cut_off_date BETWEEN '" + date1 + "' and '" + date2 + "'\
                AND employee_id = '" + empID + "' \
                 "

    cursor.execute(query)

    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['DATE','EMPLOYEE ID', 
                                        'LAST NAME','FIRST NAME','T-AMOUNT'], tablefmt='psql'))


def tin_Query():
    """
    This function is for searching
    salary of Employee
    """  
    mydb._open_connection()
    cursor = mydb.cursor()
    
   
    
    workbook = xlsxwriter.Workbook("employeeTIN.xlsx")
    worksheet = workbook.add_worksheet('rental')
    worksheet.write('A1', '#')
    worksheet.write('B1', 'ID')
    worksheet.write('C1', 'EMPLOYEE ID')
    worksheet.write('D1', 'LAST NAME')
    worksheet.write('E1', 'FIRST NAME')
    worksheet.write('F1', 'TIN')
    
   
    rowIndex = 2
    
    
    cursor.execute(
            "SELECT id,employee_id,lastname,firstname,tin\
            from employee_details \
            ")

    myresult = cursor.fetchall()
    count = 0
    for row in myresult:
        count+=1
        transID = row[0]
        empId = row[1]
        lastName = row[2]
        firstName = row[3]
        tin = row[4]
        
    
        # print(transID, count,cut_offDate,empId, lastName, firstName,trans)
        
        worksheet.write('A' + str(rowIndex),count)
        worksheet.write('B' + str(rowIndex),transID)
        worksheet.write('C' + str(rowIndex),empId)
        worksheet.write('D' + str(rowIndex),lastName)
        worksheet.write('E' + str(rowIndex),firstName)
        worksheet.write('F' + str(rowIndex),tin)
       
        
       
        

        rowIndex += 1

    workbook.close()
    print('JRS', 'Data has been exported')    

    # from os import startfile
    startfile("employeeTIN.xlsx")

def edit_off_on():
    """
    This function is for
    Editing the on and off
    columns
    """

    mydb._open_connection()
    cursor = mydb.cursor()

    date1 = input('Enter date from: ')
    date2 = input('Enter date to: ')

    cursor.execute("SELECT id,cut_off_date,employee_id,last_name, SUM(grosspay_save) as totalGross,department,on_off_details \
                        FROM payroll_computation where cut_off_date BETWEEN '"+ date1 +"' and '"+ date2 +"' \
                      GROUP BY id,employee_id,last_name, department,on_off_details ")
   
    myresult = cursor.fetchall()

    print(tabulate(myresult, headers =['ID','DATE','EMPLOYEE ID',
                                    'LAST NAME','GROSS PAY','DEPARTMENT','On & Off Status'], tablefmt='psql'))


    trans_id = input("Enter transaction ID: ")
    off_on_Details = input("Enter details on/off: ")

    key = input("Would you like to update data yes/no?: ").lower()

    if key == 'yes':

        cursor.execute(
                    "UPDATE payroll_computation SET on_off_details ='"+ off_on_Details +"'\
                    WHERE id =%s", (trans_id,)
                )
        mydb.commit()
        mydb.close()
        cursor.close()
        print("Data has been updated")
        print('')

        # update_employee_details_on()
    # else:
    #     selection()

def edit_cash_advances():
    """
    This function is
    for editing cash advance
    """

    mydb._open_connection()
    cursor = mydb.cursor()
    cash_advance_data()

    trans_id = input("Enter transaction ID: ")
    amountDeduction = input("Enter amount Deduction: ")

    key = input("Would you like to update data yes/no?: ").lower()

    if key == 'yes':

        cursor.execute(
                    "UPDATE cash_advance SET ca_deduction ='"+ amountDeduction +"'\
                    WHERE id =%s", (trans_id,)
                )
        mydb.commit()
        mydb.close()
        cursor.close()
        print("Data has been updated")
        
        edit_cash_advances()


# edit_cash_advances()
# edit_off_on()
# tin_Query()
# searchPayroll()
# deleteCut_offPeriod() 
# employee_salaryQuery()
# cf1604()
# insert_cash_advance_data()

# UpdatetaxWithheld()   

        
# comp13thMonth()
# updatesalaryRate()
# search_for_splOT()
# diesel_edit()

# diesel_search()
    
# edit_tax_table()
# insert_equipment()
# insert_sssloan_deduction()
# taxable_amount()
# total_notsubject()
# showdatabases() 

# update_sssloan_deduction()
show_sss_loandeduction()
# showColumns()
# equipment_registry()
# mwe_selection()
# test_on()
# selection()
# update_employee_details_mwe_taxable()
# update_employee_details_on()
# showtables()
# cash_advance_data()

# search_payroll()
# search_payroll_withUpdate()

# update_hdmfloan_deduction()


# computation_cosolidated()
