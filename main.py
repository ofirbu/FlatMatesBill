from flat import Bill, Flatmate
from reports import PdfReport

the_bill = Bill(amount=120, period="May 2020")
john = Flatmate("John", days_in_the_house=25)
marry = Flatmate("Marry", days_in_the_house=20)
report = PdfReport(john, marry)

print("John pays: ", john.pays(the_bill, marry))
print("Marry pays: ", marry.pays(the_bill, john))

report = PdfReport(john, marry)
report.generate_pdf(the_bill)
