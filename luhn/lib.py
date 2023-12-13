"""Luhn algorithm implementation"""

from .errors import Unimplemented


#met les chiffres sous forme de liste / séparé par des ","
def digits_of(n):
        return [int(d) for d in str(n)]

def is_valid(credit_card_number: str) -> bool:
    """Returns whether the specified credit card number is valid or not"""
    
    if not credit_card_number.replace(" ", "").isdigit():  
        raise Unimplemented("Invalid characters in the credit card number")
    
    if len(credit_card_number.replace(" ", "")) != 16 :
        raise Unimplemented("Invalid credit card length")
     
    if not ' ' in credit_card_number:
        
        #divise la chaine en groupe de 4 et sépare tout les 4 caractères 
        credit_card_number = ' '.join(credit_card_number[i:i+4] for i in range(0, len(credit_card_number), 4))

    
    credit_card_number = credit_card_number.replace(" ", "") #supprime les espaces
    
    digits = digits_of(credit_card_number) #application de la fonction
    
    #Isolation des chiffres en position paire 
    odd_digits = digits[-1::-2] #liste des chiffres seulement en position impair en commençant par le droite
    even_digits = digits[-2::-2] #liste des chiffres seulement en position pair en commençant par le droite
    
    checksum = 0 #initilisation de la somme
    checksum += sum(odd_digits) #somme des chiffres de position impair 

    #rajout de la somme des chiffres en position pair 
    for d in even_digits:
        temp = int(d) * 2
        #si le double > 9 alors on soustrait 9 au double sinon on prend le double
        checksum += temp - 9 if temp > 9 else temp 
    
    #doit retourner True/False 
    return checksum % 10 == 0

    