# Contador: Imprime los números del 1 al 10 usando un while.
import time
def contador():
    num = 0;
    while num <= 11:
        num += 1
        print(num)
        time.sleep(1)

contador()