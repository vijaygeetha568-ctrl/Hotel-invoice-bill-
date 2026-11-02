print("================================")
print("       ABC HOTEL")
print("      HOTEL INVOICE")
print("================================")

name = input("Customer Name: ")
phone = input("Phone Number: ")

print("\nRoom Types")
print("1. Single Room - Rs.1000")
print("2. Double Room - Rs.2000")
print("3. Deluxe Room - Rs.3000")

room = int(input("Select Room: "))
days = int(input("Number of Days: "))

if room == 1:
    room_name = "Single Room"
    rent = 1000
elif room == 2:
    room_name = "Double Room"
    rent = 2000
elif room == 3:
    room_name = "Deluxe Room"
    rent = 3000
else:
    print("Invalid Room Selection")
    exit()

food = int(input("Enter Food Charges: "))

room_total = rent * days
subtotal = room_total + food
gst = subtotal * 0.05
total = subtotal + gst

print("\n================================")
print("          ABC HOTEL")
print("         INVOICE BILL")
print("================================")

print("Customer Name :", name)
print("Phone Number  :", phone)
print("Room Type     :", room_name)
print("Number of Days:", days)

print("--------------------------------")
print("Room Rent     : Rs.", room_total)
print("Food Charges  : Rs.", food)
print("Subtotal      : Rs.", subtotal)
print("GST (5%)      : Rs.", gst)
print("--------------------------------")
print("TOTAL AMOUNT  : Rs.", total)
print("================================")
print("       THANK YOU VISIT AGAIN!")
print("================================")
