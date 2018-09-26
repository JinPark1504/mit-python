# def remainingBalance(balance, annualInterestRate, monthlyPaymentRate):
#     '''
#     balance: the outstanding balance on the credit card
#     annualInterestRate: annual interest rate as a decimal
#     monthlyPaymentRate: minimum monthly payment rate as a decimal
    
#     return: remaining balance as two decimal
#     '''
#     for i in range(12):
#         monthlyInterestRate = annualInterestRate / 12.0
#         minimumMonthlyPayment = monthlyPaymentRate * balance
#         monthlyUnpaidBalance = balance - minimumMonthlyPayment
#         balance = monthlyUnpaidBalance + ( monthlyInterestRate * monthlyUnpaidBalance )
#         #print('Month '+ str(i + 1) + ' Remaining Balance: ' + str(round(balance,2)))
        
#     return 'Remaining Balance: ' + str(round(balance,2))

# def fixedMonthlyPayment(balance, annualInterestRate):
#     '''
#     balance: the outstanding balance on the credit card
#     annualInterestRate: annual interest rate as a decimal
    
#     return: fixed monthly payment 
#     '''
#     minimumFixedMonthlyPayment = round(balance / 12 / 10) * 10
#     while True:
#         balance1 = balance
#         for i in range(12):
#             monthlyInterestRate = annualInterestRate / 12.0
#             monthlyUnpaidBalance = balance1 - minimumFixedMonthlyPayment
#             balance1 = monthlyUnpaidBalance + ( monthlyInterestRate * monthlyUnpaidBalance )
#         if(balance1 <= 0):
#             #print('fix',minimumFixedMonthlyPayment, 'bal', balance1)
#             return 'Lowest Payment: ' + str(round(minimumFixedMonthlyPayment))
#         else:
#             #print('fix',minimumFixedMonthlyPayment, 'bal', balance1)
#             minimumFixedMonthlyPayment += 10
            
def bisectionSearchIteration(balance, annualInterestRate):
    '''
    balance: the outstanding balance on the credit card
    annualInterestRate: annual interest rate as a decimal
    
    return lowest payment by two decimal
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    monthlyPaymentLowerBound = balance / 12
    monthlyPaymentUpperBound = ( balance * ( 1 + monthlyInterestRate ) ** 12 ) / 12.0
    
    minimumFixedMonthlyPayment = monthlyPaymentLowerBound
    while True:
        balance1 = balance
        for i in range(12):
            monthlyUnpaidBalance = balance1 - minimumFixedMonthlyPayment
            balance1 = monthlyUnpaidBalance + ( monthlyInterestRate * monthlyUnpaidBalance )
        if round(balance1, 2) == 0:
            print('fix',minimumFixedMonthlyPayment, 'bal', balance1)
            return 'Lowest Payment: ' + str( round(minimumFixedMonthlyPayment, 2))
        elif balance1 > 0:
            print('fix',minimumFixedMonthlyPayment, 'bal', balance1)
            monthlyPaymentLowerBound = minimumFixedMonthlyPayment
            minimumFixedMonthlyPayment = ( minimumFixedMonthlyPayment + monthlyPaymentUpperBound ) / 2 
        else:
            print('higher fix',minimumFixedMonthlyPayment, 'bal', balance1, 'monthlyPaymentUpperBound:', monthlyPaymentUpperBound)
            monthlyPaymentUpperBound = minimumFixedMonthlyPayment
            minimumFixedMonthlyPayment = ( minimumFixedMonthlyPayment + monthlyPaymentLowerBound ) / 2 
            print('monthlyPaymentUpperBound:', monthlyPaymentUpperBound, 'minimumFixedMonthlyPayment:',minimumFixedMonthlyPayment)
            
def bisectionSearchRecursion(balance, annualInterestRate):
    '''
    balance: the outstanding balance on the credit card
    annualInterestRate: annual interest rate as a decimal
    
    return lowest payment by two decimal
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    #monthlyPaymentLowerBound = balance / 12
    #monthlyPaymentUpperBound = ( balance * ( 1 + monthlyInterestRate ) ** 12 ) / 12.0

    def bisectionSearch(lowerBound, upperBound, minimumFixed=False):    
        if not minimumFixed:
            minimumFixed = lowerBound
    
        # while True:
        balance1 = balance
        for i in range(12):
            monthlyUnpaidBalance = balance1 - minimumFixed
            balance1 = monthlyUnpaidBalance + ( monthlyInterestRate * monthlyUnpaidBalance )
        if round(balance1, 2) == 0:
            print('fix',minimumFixed, 'bal', balance1)
            return 'Lowest Payment: ' + str( round(minimumFixed, 2))
        elif balance1 > 0:
            print('fix',minimumFixed, 'bal', balance1)
            lowerBound = minimumFixed
            minimumFixed = ( minimumFixed + upperBound ) / 2
            return bisectionSearch(lowerBound, upperBound, minimumFixed)
        else:
            print('higher fix',minimumFixed, 'bal', balance1, 'upperBound:', upperBound)
            upperBound = minimumFixed
            minimumFixed = ( minimumFixed + lowerBound ) / 2 
            return bisectionSearch(lowerBound, upperBound, minimumFixed)
            #print('upperBound:', upperBound, 'minimumFixedMonthlyPayment:',minimumFixed)
    
    return bisectionSearch(balance/12, (balance*(1+monthlyInterestRate)**12)/12.0)