from decimal import *

def evaluate_6_6(x, limit):
    retval = 0.5 + 0.25 + 0.125
    for i in range(3, limit):
        retval += pow(0.5, i+1)*pow(x, pow(2, i-1)-3)

    return retval
                

def evaluate_15_15(x, limit):
    with localcontext() as ctx:
        ctx.prec = 1000
        
        preval = 0.5+0.25+0.125+0.0625
        retval = Decimal(preval)
        for i in range(4, limit):
            retval += ctx.power(Decimal(0.5), i+1)*ctx.power(Decimal(x), ctx.power(2, i)-14)
        return retval

def evaluate_2_2(x, limit):
    retval = 0
    for i in range(0, limit):
        retval += pow(0.5, i+1)*pow(x, pow(2, i)-1)

    return retval


def find_optimal_6_6(lower_limit, upper_limit, increment_amount, error_margin, LIMIT):
    min_diff = 1
    best_val = 0
    i = lower_limit

    while(i <= upper_limit):
        val = i + i*i + pow(i, 2.5) 
        differential = abs(val - evaluate_6_6(i, LIMIT))
        if(min_diff > differential):
            min_diff = differential
            best_val = i
            
        i += increment_amount

    if(increment_amount <= error_margin):
        return best_val
    
    return find_optimal(best_val - increment_amount, best_val + increment_amount, increment_amount/10, error_margin, LIMIT)




    

def find_optimal(lower_limit, upper_limit, increment_amount, error_margin, LIMIT):
    min_diff = 1
    best_val = 0
    i = lower_limit
    while(i <= upper_limit):
        differential = abs(Decimal(i)-evaluate_15_15(i, LIMIT))
        if(min_diff > differential):
            min_diff = differential
            best_val = i
            
        i += increment_amount

    if(increment_amount <= error_margin):
        return best_val
    
    return find_optimal(best_val - increment_amount, best_val + increment_amount, increment_amount/10, error_margin, LIMIT)



LIMIT = 100
INCREMENT_LIMIT = 10
ERROR_MARGIN = 0.0000000000001



print(find_optimal_6_6(1/INCREMENT_LIMIT, 1-1/INCREMENT_LIMIT, 1/INCREMENT_LIMIT, ERROR_MARGIN, LIMIT))

