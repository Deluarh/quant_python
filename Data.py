# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 21:43:08 2018

@author: Phantom
"""

import csv
class MyData:
    csv_path = ''  
    def __init__(self, n):
        self.csv_path = n
    def detData(self):
        with open(self.csv_path, "r") as f_obj:
            reader = csv.reader(f_obj)
            test = []
            for row in reader:
                qwe= str(row[0]).split(';')
                test.append(qwe)
            print("массив обработан")
            return test