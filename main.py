# Dictionary for morse code
MORSE_CODE_DICT={'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.',
                'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
                'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--',
                'X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
                '4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                '0':'-----'
    
}
new_text=''
message=input("Enter Your Message: ").upper()
for letter in message:
    if letter !=' ':
        new_text+=MORSE_CODE_DICT[letter] +' '
    else:
        new_text+='....... '
print(new_text)
