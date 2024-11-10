import tkinter
import requests


def get_usd_to_ils_rate(curr1, curr2):
    url = f"https://v6.exchangerate-api.com/v6/bb59235afc96f3f0372f4fcd/latest/{curr1}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and "conversion_rates" in data:
            usd_to_ils = data["conversion_rates"].get(curr2)

            return usd_to_ils
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None
    

    
def refresh(curr1, curr2):
    rate = get_usd_to_ils_rate(curr1, curr2)
    return rate


currency_abbreviations = (
    "USD", "EUR", "GBP", "AUD", "CAD", "JPY", "CHF", "CNY", "INR", "MXN",
    "BRL", "RUB", "ZAR", "SEK", "NZD", "SGD", "HKD", "KRW", "NOK", "TRY",
    "IDR", "MYR", "THB", "PHP", "SAR", "AED", "ILS", "PLN", "EGP", "COP",
    "DKK", "HUF", "CZK", "CLP", "MAD", "RON", "VND", "PEN", "LKR", "KZT",
    "QAR", "BGN", "HRK", "ISK", "BDT", "OMR", "KWD", "JOD", "TWD", "PAB",
    "COP", "MKD", "JMD", "BMD", "MUR", "SYP", "ZWL", "TZS", "KES", "LAK",
    "UGX", "MWK", "MDL", "PYG", "KGS", "NPR", "BWP", "FJD", "MNT", "GHS",
    "AFN", "NGN", "AWG", "KYD", "FOK", "GEL", "BIF", "SLL", "STN", "DJF"
)

def curr_calc(ent, opt1, opt2):
    try:
        return str(float((ent)) * refresh(opt1, opt2)) + opt2
    except:
        return 0
    

win = tkinter.Tk()
win.title("Currency Calculator")

win.geometry("300x400")

text = tkinter.Label(win, text="Enter amount:")
text.pack()

entry = tkinter.Entry()
entry.pack()

textvar = tkinter.StringVar()
textvar.set("")

text2 = tkinter.Label(win, textvariable=textvar)
text2.pack()


selectedOption = tkinter.StringVar()
selectedOption.set("USD")

dropdown = tkinter.OptionMenu(win, selectedOption, *currency_abbreviations)
dropdown.pack()

text3 = tkinter.Label(win, text="to:")
text3.pack()

selectedOption2 = tkinter.StringVar()
selectedOption2.set("USD")

dropdown2 = tkinter.OptionMenu(win, selectedOption2, *currency_abbreviations)
dropdown2.pack()



printButton = tkinter.Button(win, text = "convert",  command = lambda:textvar.set(curr_calc(entry.get(), selectedOption.get(), selectedOption2.get())))
printButton.pack()

win.bind('<Return>', lambda event: printButton.invoke())



win.mainloop()
