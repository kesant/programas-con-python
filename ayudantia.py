#Crea un programa usando matemáticas y f-Strings que nos diga cuántos días, semanas, meses nos quedan si vivimos hasta los 90 años.
#Tomará su edad actual como entrada y salida de un mensaje con nuestro tiempo restante en este formato:
#Te quedan x días, y semanas y z meses.
age=input("Cual es tu edad actual ? : ")
age_as_int=int(age)
years_remaining= 90-age_as_int
days_remaining=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12
print(f"Te quedan {days_remaining}  días,{weeks_remaining}  semanas y{months_remaining}  meses.")
