from functions import *
read_file() 
check_file_exists()


while True:
    menu = ("\n" 
            "\n Swedbank deluxe"
            "\n Saldo: {} kr" 
            "\n 1. Saldo" 
            "\n 2. Insättning" 
            "\n 3. Uttag" 
            "\n 4. Avsluta"
            "\n 5. Nollställ kontot"
            "\nGör ditt val").format(balans())

    val = validate_int(menu, "Felaktig inmatning!")

    if val == 1:
        print(print_transactions())

    elif val == 2:
        insättning = validate_int("Hur mycket vill du lägga in på kontot?", "Felaktig inmatning!")
        if insättning > 0:
            add_transaction(insättning, True)
        else:
            print("Måste vara större än 0")
    elif val == 3:
        uttag = validate_int("Hur mycket vill du dra ut?", "Felaktig inmatning!")
        if uttag <= balans() and uttag >= 0:
            add_transaction(-uttag, True)
        elif uttag < 0:
            print("Måste vara större än 0")
        else:
            print("Du har inte tillräckligt med pengar på kontot, fattiglapp")
    elif val == 4:
        break

    elif val == 5:
        os.remove(filename)         # Ta bort filen
        transactions.clear()        # Töm listan
        read_file()                 # Skapa filen och läs in den


    else:
        print("Fel input")

print("Adjöken fröken/herrn")