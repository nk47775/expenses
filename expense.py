import datetime

print("💰 Expense Tracker (खर्च का हिसाब)")
amt = input("कितने पैसे खर्च हुए?: ₹")
item = input("किस चीज़ पर खर्च किए?: ")

date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
with open("expenses.txt", "a") as f:
    f.write(f"{date} | ₹{amt} - {item}\n")

print("✅ खर्च सेव हो गया!")
