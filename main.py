import webbrowser
from fpdf import FPDF


class Bill:
    """
    object that contains data of a bill
    Total amount and period of a bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    '''
    create a flatmate person who lives in the house and play the share
    of the bill
    '''

    def __init__(self, name, days_in_the_house):
        self.days_in_the_house = days_in_the_house
        self.name = name

    def pays(self, bill, flatmate2):
        total_days = self.days_in_the_house + flatmate2.days_in_the_house
        fraction = self.days_in_the_house / total_days
        return bill.amount * fraction


class PdfReport:
    '''
    creates a pdf file that contains data about the flatmates such are their names
    their due anmount and the period of the bills
    '''

    def __init__(self, flatmate1, flatmate2):
        self.flatmate2 = flatmate2
        self.flatmate1 = flatmate1

    def generate_pdf(self, bill):
        flat_mate_1_pay = round(self.flatmate1.pays(bill, self.flatmate2), 2)
        flat_mate_2_pay = round(self.flatmate2.pays(bill, self.flatmate1), 2)
        data = (
            (self.flatmate1.name, self.flatmate2.name),
            (flat_mate_1_pay, flat_mate_2_pay),
        )
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Times', 'B', 20)
        pdf.image("house-png.png", w=30, h=30)
        pdf.cell(175, 40, 'Flatmates Bill', 0, 1, align='C')
        pdf.cell(60, 10, f"Period: {bill.period}", 0, 1, align='C')

        line_height = pdf.font_size * 10
        col_width = 65  # distribute content evenly
        th = pdf.font_size
        for row in data:
            for datum in row:
                # Enter data in colums
                # Notice the use of the function str to coerce any input to the
                # string type. This is needed
                # since pyFPDF expects a string, not a number.
                pdf.cell(col_width, th, str(datum), border=1)

            pdf.ln(th)

        pdf.output('bill.pdf', 'F')
        webbrowser.open(self.filename)


the_bill = Bill(amount=120, period="May 2020")
john = Flatmate("John", days_in_the_house=25)
marry = Flatmate("Marry", days_in_the_house=20)
report = PdfReport(john, marry)

print("John pays: ", john.pays(the_bill, marry))
print("Marry pays: ", marry.pays(the_bill, john))

report = PdfReport(john, marry)
report.generate_pdf(the_bill)
