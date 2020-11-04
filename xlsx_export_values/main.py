import xlrd
import xlsxwriter as xw
import time

#xlsx file where the accounts and the account numbers are
path1 = "collection_of_key_values.xlsx"

#xlsx where only the account number is given
path2 = "only_the_key_is_given.xlsx"

#The path3 is only needed because xlsxwriter cannot append items to an xlsx file where data is written already
path3 = "value_for_keys_in_order.xlsx"

#Importing the first excel sheet where the account name and number is being loaded
workbook1 = xlrd.open_workbook(path1)
sheet1 = workbook1.sheet_by_index(0)

#Importing the 2nd excel sheet where the account number will be written by the code
workbook2 = xlrd.open_workbook(path2)
sheet2 = workbook2.sheet_by_index(0)

#Importing a 3rd empty xlsx file that can be used for writing, you can pick the entire row and paste it into the 2nd file
writeto = xw.Workbook(path3)
output = writeto.add_worksheet()

#The amount of repeated runs are equal to the amount cells in the given row in the 2nd excel sheet
for y in range(sheet2.nrows):

    #Using a different for loop for the items on the first list, the run is equal to the number of cells under the given column
    for i in range(sheet1.nrows):

        #The number 0 needs to be modified depending on the column where the items are
        if sheet2.cell_value(y, 0) == sheet1.cell_value(i, 0):
            print(f"Match at cell number {i} in sheet1 for the following sheet2 item: {sheet2.cell_value(y, 0)}")

            #The number 1 needs to be modified depending on where the value can be found for the items
            print(f"Cell value is {int(sheet1.cell_value(i, 1))}")

            #Adding + 1 since H0 for example doesn't exist at the columns for excel
            output.write(f"H{y + 1}", int(sheet1.cell_value(i, 1)))
            time.sleep(1)
        else:
            pass

writeto.close()