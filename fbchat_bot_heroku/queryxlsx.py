import random
import xlrd
from class_for_functions import *
import time

class Readexcel:

    def __init__(self, path, ACCESS_TOKEN):
        self.path = path
        self.ACCESS_TOKEN = ACCESS_TOKEN

    def import_excel(self):
        self.inputWorkbook = xlrd.open_workbook(self.path)
        self.inputWorksheet = self.inputWorkbook.sheet_by_index(0)
        print('\x1b[6;30;42m' + "Successfully imported the file." + '\x1b[0m')

    def append_items(self):
        self.bejovo_uzenetek = []
        self.index = []
        self.index_int = []
        for y in range(1, self.inputWorksheet.nrows):
            self.bejovo_uzenetek.append(self.inputWorksheet.cell_value(y, 1))
            self.index.append(self.inputWorksheet.cell_value(y, 2))

        self.index_int = [int(i) for i in self.index]
        print('\x1b[6;30;42m' + "Successfully imported the bejovo uzenetek and the index number." + '\x1b[0m')

    def append_items_2(self, text_input):
        for i, items in enumerate(self.bejovo_uzenetek):
            if str.lower(text_input) in str.lower(items):
                self.number_order = (i)
                break

    def find_answer(self, user_id):
        self.answer_index = (self.index_int[self.number_order])
        print('\x1b[6;30;42m' + "Found a matching text in the bejovo uzenetek." + '\x1b[0m')
        random_answers = []
        for z in range(4, self.inputWorksheet.ncols):
            if self.inputWorksheet.cell_value(self.answer_index, z) == "":
                pass
            else:
                random_answers.append(self.inputWorksheet.cell_value(self.answer_index, z))
        del self.inputWorkbook
        self.random_answers = random.choice(random_answers)
        if "function" in self.random_answers:
            d = Functions(self.ACCESS_TOKEN)
            print('\x1b[6;30;42m' + "Looking for a function." + '\x1b[0m')
            exec(f'd.{self.random_answers}({user_id})')
            print('\x1b[6;30;42m' + "Function processed." + '\x1b[0m')
            try:
                self.random_answers = d.value
            except:
                print('\x1b[0;30;43m' + "--- Couldn't find the 'value' in the function ---" + '\x1b[0m')
                self.random_answers = ""
                pass
        else:
            print('\x1b[6;30;42m' + "Processing the answer from the excel sheet." + '\x1b[0m')
            pass

#These are the functions that allow you to test this script manually:
#Since there is error handling i think it's no longer required, but still if you want to
#you can use it.
#r = Readexcel('answers.xlsx')

#r.import_excel()
#r.append_items()
#r.append_items_2(text_input)
#r.find_answer(user_id)