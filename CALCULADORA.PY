def addmultiplenumbers(numeros):
   
    total = 0
    for n in numeros:#Division
        total += n
    return total

def multiplymultiplenumbers(numeros):
   
    producto = 1
    for n in numeros:
        producto *= n#multiplicacion
    return producto

def isitaninteger(num):
   
    try:
        return float(num).is_integer()
    except (TypeError, ValueError):        #encontre como se puede convertir a float y Si es entero 4, 4.0
        return False

def isiteven(num):
    
    if not isitaninteger(num):
        return False
    return int(float(num)) % 2 == 0 #porcentaje 

def main():
    print("Jeison_Calculadora")# mensaje a mostar y en seguida digitas numero con signo
    

if __name__ == "__main__":
    main()