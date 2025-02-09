# Import the Flask class from the flask module

from flask import Flask, render_template, request

# Import functions from other files (utils.py in this case)

from utils import greet_user

## utils is name of the python files and greet_user is the function name

# Create an instance of the Flask class

app = Flask(__name__)

# Take the current date - year, month, day

from datetime import date



# Function to compare year, month, and day

def compare_year(cyear, eyear, cmonth, emonth, cday, eday):

    eyear = int(eyear)

    emonth = int(emonth)

    eday = int(eday)

    print(cyear, eyear, cmonth, emonth, cday, eday)



    if cyear < eyear:

        return True  # Product is not expired

    elif cyear == eyear:

        if cmonth < emonth:

            return True  # Product is not expired

        elif cmonth == emonth:

            if cday <= eday:

                return True  # Product is not expired

            else:

                return False  # Product is expired

        else:

            return False  # Product is expired

    else:

        return False  # Product is expired

# Function to suggest recipe

def sugggest_recipe(pname, isExpired):

    if not isExpired:

        return "Time to throw away the product: " + pname

    else:

        if pname == "bread":

            return "You can make a sandwich with the bread"
        elif pname == "cookie" or pname == "cookies":

            return "You can have cookies with milk"

        else:

            return "No specific recipe suggestion for this product."



# Get the current date

current_date = date.today()

current_year = current_date.year

current_month = current_date.month

current_day = current_date.day



# Define a route for the root URL ("/")

@app.route('/checkexpiry', methods=['GET', 'POST'])

def checkexpiry():

    if request.method == 'POST':

        # Get the name from the form input

        expiry_year = request.form.get('year')

        expiry_month = request.form.get('month')

        expiry_day = request.form.get('day')

        product_name = request.form.get('pname')



        # Check if the product is expired

        isExpired = compare_year(current_year, expiry_year, current_month, expiry_month, current_day, expiry_day)

        print(isExpired)



        # Prepare messages based on expiry status

        if isExpired:

            msg1 = "Your product is not expired. Please use as soon as possible."

        else:

            msg1 = "Your product is expired. Please throw it away."

        msg2 = sugggest_recipe(product_name, isExpired)



        # Render the template with the messages

        return render_template('checkexpiry.html', msg1=msg1, msg2=msg2)



    # If it's a GET request, just render the form

    return render_template('checkexpiry.html', msg1=None, msg2=None)
@app.route('/info', methods=['GET'])
def info():
    return render_template('info.html')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



# Run the application

if __name__ == '__main__':

    app.run(debug=True)
