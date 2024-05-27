#Program to get entered alphabet is Vowel or consonant or Neither 

a = input("Enter alphabet: ")

if (a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U'): 
        print("Vowel") 

elif (a== 'b' or a== 'B' or a== 'c' or a== 'C' or a== 'd' or a== 'D' or a== 'f' or a== 'F' or a== 'g' or a== 'G' or a== 'h' or a== 'H' or a== 'j' or a== 'J' or a== 'k' or a== 'K' or a== 'l' or a== 'L' or a== 'm' or a== 'M' or a== 'n' or a== 'N' or a== 'p' or a== 'P' or a== 'q' or a== 'Q' or a== 's' or a== 'S' or a== 't' or a== 'T' or a== 'v' or a== 'V' or a== 'w' or a== 'W' or a== 'x' or a== 'X' or a== 'y' or a== 'Y' or a== 'z' or a== 'Z'):

        print("Consonant")
else: 
        print("None")