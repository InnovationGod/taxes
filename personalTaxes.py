'''
Created on 10 Mar 2013

@author: eidahil
'''

class TaxesData(object):

    def __init__(self, taxes_percentage):
        self.set_my_tax_in_percentage(taxes_percentage)

    def set_my_tax_in_percentage(self, my_taxes_percentage):
        self.taxes_percentage = my_taxes_percentage

    def get_my_tax_in_percentage(self):
        return self.taxes_percentage