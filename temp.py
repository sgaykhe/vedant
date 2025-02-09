# # Take the current date - year, month, day
# from datetime import date
# # Function to compare year
# def compare_year(cyear, eyear, cmonth, emonth, cday, eday):
#     if(cyear <= eyear):
#         # Check Month 2025 2025
#         #print("Your product is not expired")
#         if(cmonth <= emonth): 
#             # Check Day 02 03
#             #print("Your product is not expired.")
#             if(cday <= eday):## 03 05
#                print("Your product is expired")
#             else:
#                 print("Your product is not expired. Please use as soon as possible.")
#         else:
#             print("Your product is not expired. Please use as soon as possible.")
#     else:
#         print("Your product is not expired. Please use as soon as possible.")
#     return
# # Function to suggest recipe
# def sugggest_recipe(pname):
#     if(pname == "bread"):
#         print("Time to eat a sandwitch")
#     return
# current_date = date.today()
# current_year = current_date.year
# current_month = current_date.month
# current_day = current_date.day
# # Ask for the product name and expiry date
# product_name = input("Enter the product name:- ")
# #expiry_date = int(input("Enter the expiry date in YYYY-MM-DD format:- "))
# expiry_year = int(input("Enter the expiry year in YYYY format:- "))
# expiry_month = int(input("Enter the expiry month in MM format:- "))
# expiry_day = int(input("Enter the expiry day in DD format:- "))
# compare_year(current_year, expiry_year, current_month, expiry_month, current_day, expiry_day)
# sugggest_recipe(product_name)



# Take the current date - year, month, day
from datetime import date
# Function to compare year
def compare_year(cyear, eyear, cmonth, emonth, cday, eday):
    if(cyear <= eyear):
        # Check Month 2025 2025
        #print("Your product is not expired")
        if(cmonth <= emonth):
            # Check Day 02 03 
            #print("Your product is not expired.")
            if(cday < eday):
               #3 5
               print("Your product is not expired. Please use as soon as possible.")
            else:
                print("Your product is expired")
        else:
            print("Your product is expired")
    else:
        print("Your product is expired")
    return
# Function to suggest recipe
def sugggest_recipe(pname):
    if(pname == "bread"):
        print("Time to eat a sandwitch")
    return
current_date = date.today()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day
# Ask for the product name and expiry date
product_name = input("Enter the product name:- ")
#expiry_date = int(input("Enter the expiry date in YYYY-MM-DD format:- "))
expiry_year = int(input("Enter the expiry year in YYYY format:- "))
expiry_month = int(input("Enter the expiry month in MM format:- "))
expiry_day = int(input("Enter the expiry day in DD format:- "))
compare_year(current_year, expiry_year, current_month, expiry_month, current_day, expiry_day)
sugggest_recipe(product_name)