from colorama import init 
from termcolor import colored

def kth_piece(k: int):
    leading = 1/pow(16, k)
    inner_t1 = 4/(8*k+1) 
    inner_t2 = 2/(8*k+4) 
    inner_t3 = 1/(8*k+5) 
    inner_t4 = 1/(8*k+6) 
    return leading * (inner_t1 - inner_t2 - inner_t3 - inner_t4)
 
def pi(n: int=10) -> float:
   return sum([kth_piece(k) for k in range(n)])
pi_digit:str = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852'

def is_eq(pi_pred: str) -> int:
    
    for i, dig in enumerate(pi_pred):
        if pi_digit[i] != dig:
            return i 
    return len(dig) - 1

if __name__ == '__main__':
    init()
    for i in range(10):
        pi_pred = str(pi(n=i))
        eq_idx = is_eq(pi_pred)
        print(f'{i=} => ', colored(pi_pred[:eq_idx], 'white', 'on_green'), end='')
        print(colored(pi_pred[eq_idx:], 'white', 'on_red'))
    
