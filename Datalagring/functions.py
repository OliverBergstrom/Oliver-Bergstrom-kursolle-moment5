from config import *

def balans():
    """ Beräknar saldot på kontot
    

    :return: saldot
    """  
    balans = 0
    for t in transactions:
        balans += t
    return balans

def validate_int(output, error_mess):
    while True:
        try:
            value = int(input(output))
            break
        except:
            print(error_mess)
    return value

def print_transactions():

    line = 0
    balans = 0
    output = ("\nAlla transaktioner:"
            "\n{:>3} {:>12} {:>12}"
            "\n______________________________").format("Nr", "Händelse", "Saldo")
    for t in transactions:
        line += 1
        balans += t
        output += ("\n{:>2}. {:>9} {:>9} kr".format(line, t, balans))

    return output

def check_file_exists():

    """ Om filen inte finns så skapas den och sedan så läggs en transaktion till
    Eftersom "x" returnerar ett error om filen finns kan vi utnyttja detta.
    :return: none
     """

    try:
        with open(filename, "x"):
            print("Filen skapades")
        
        with open(filename, "a") as f:
            f.write("{}\n".format(1000))
        
    except:
        return

def read_file():
    """ Läser in filens innehåll till transaktionslistan 
    
    :return: none
    """
    check_file_exists()

    with open(filename) as f:
        for rad in f:
            if len(rad) > 0:
                add_transaction(int(rad))


def add_transaction(transaction, toFile = False):
    """ Lagrar transaktion i transaktionslistan och till filen

    :param transaction: transaktionen
    :param toFile: True - lagra också till filen, False är förvalt
    :return: None
    """
    transactions.append(transaction)
    if toFile:
        write_transaction_to_file(transaction)

    
def write_transaction_to_file(transaction):
    """ Skriver en transaktion till filen 
    
    :param transaction: transaktionen
    :return: None
    """

    with open(filename, "a") as f:
        f.write("{}\n".format(transaction))