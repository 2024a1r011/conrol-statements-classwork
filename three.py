#    Write a program to calculate the final bill amount after applying a discount . The prorgam should take the total bill amount as input from the user and aplly the discount according to the following rules. After calculating the discount , the program should display the discount amount and final bill amount payable by the customer.

# Bill amount    discount
# above 5000     20 %
# 3000 -5000     10 %
# Below 3000      No discount


bill = float(input("Enter the total bill : "))

if bill > 5000:
    discount = bill*20/100
elif bill > 3000 and bill <= 5000:
    discount = bill * 10/100
else:
    discount =0
final_bill = bill - discount

print("Discount is : ",discount)
print("Final bill : ",final_bill)