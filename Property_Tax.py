__author__ = 'dwight'

# A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual
# value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000. The property tax is then
# 64¢ for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $38.40. Write a program
# that asks for the actual value of a piece of property and displays the assessment value and property tax.


def main():
    property_value = float(input('Enter property value: $'))
    print('Assessment Value: $', format(calc_assessment_value(property_value), ',.2f'), sep='')
    print('Property Tax: $', format(calc_property_tax(property_value), ',.2f'), sep='')


def calc_assessment_value(property_value):
    assessment_rate = 0.6
    return property_value * assessment_rate


def calc_property_tax(property_value):
    property_tax_rate = 0.64
    property_tax_increment = 100
    return (int(calc_assessment_value(property_value) / property_tax_increment)) * property_tax_rate


main()
