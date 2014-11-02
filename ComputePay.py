# Python program to compute total pay using
# hours worked, pay rate, and overtime multiplier as inputs.
# License: CC0 1.0 Universal
# Programer: Julien BRAGA

# A dictionary of prompts for soliciting user input.
userprompts = {
    'hours':'Enter hours worked: ',
    'rate':'Enter pay rate: ',
    'ot':'Enter OT multiplier: '
}

# Function to compute pay.
def compute_pay(hours, rate, otmultiplier):
    # Break hours into hours and othours if more than 40 hours were worked.
    # Set othours to the number of hours worked over 40 and hours to 40.
    if hours > 40:
        othours = hours - 40
        hours = 40
    # If 40 or less hours were worked, set othours to 0. Leave hours as is.
    else:
        othours = 0
    # Caculate the overtime rate.
    otrate = rate * otmultiplier
    # Calculate total pay and return it.
    pay = (hours * rate) + (othours * otrate)
    return pay

# Function to solicit user input and convert to float type.
def get_float_input(varname):
    # Determine which prompt to use when asking for input.
    try:
        userprompt = userprompts[varname.lower()]
    except:
        print 'Error: Prompt not defined.'
    # Loop until the user inputs a value that can be converted to float type.
    while True:
        userinput = raw_input(userprompt)
        try:
            userinput = float(userinput)
            break
        except:
            print 'Enter a numerical value.'
            continue
    # Return the input once a float type is entered.
    return userinput

# Get inputs from the user.
hours = get_float_input('hours')
rate = get_float_input('rate')
if hours > 40:
    print ''
    print '''The overtime (OT) multiplier is required to calculate the 
        pay correctly because more than 40 hours were entered. The OT
        multiplier is the factor by which OT hours and the standard
        pay rate are multiplied to calculate the correct total pay amount.
        For example, "time-and-a-half" overtime would be entered as an OT
        multiplier of 1.5. "Double-time" would be entered as 2.0.
        
        '''
    otmultiplier = get_float_input('ot')
else:
    otmultiplier = 0

# Compute and print the pay.
print 'Total Pay:', compute_pay(hours, rate, otmultiplier)

