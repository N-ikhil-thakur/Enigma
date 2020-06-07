from rotate import rotate_dict_keys , rotate_dict_values , interchange_keys_values


chars = ['A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' , 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z']


w1 = {'A':'Z' , 'B':'X' , 'C':'C' , 'D':'B' , 'E':'V' , 'F':'M' , 'G':'N' , 'H':'W' , 'I':'Q' , 'J':'R' , 'K':'E' , 'L':'Y' ,'M':'T' , 'N':'I' , 'O':'U' , 'P':'P' , 'Q':'O' , 'R':'A' , 'S':'S' , 'T':'D' , 'U':'F' , 'V':'G' , 'W':'H' , 'X':'J' , 'Y':'K' , 'Z':'L' }

w2 = {'A':'A' , 'B':'H' , 'C':'I' , 'D':'J' , 'E':'B' , 'F':'G' , 'G':'K' , 'H':'M' , 'I':'O' , 'J':'C' , 'K':'L' , 'L':'N' ,'M':'P' , 'N':'U' , 'O':'V' , 'P':'W' , 'Q':'X' , 'R':'D' , 'S':'Y' , 'T':'Z' , 'U':'E' , 'V':'Q' , 'W':'R' , 'X':'S' , 'Y':'T' , 'Z':'F' }

w3 = {'A':'A' , 'B':'O' , 'C':'P' , 'D':'U' , 'E':'B' , 'F':'Q' , 'G':'R' , 'H':'V' , 'I':'C' , 'J':'M' , 'K':'N' , 'L':'W' ,'M':'D' ,  'N':'K' , 'O':'L' , 'P':'Y' , 'Q':'E' , 'R':'H' , 'S':'I' , 'T':'T' , 'U':'F' , 'V':'G' , 'W':'J' , 'X':'S' , 'Y':'X' , 'Z':'Z'}


o_w1 = interchange_keys_values(w1)
o_w2 = interchange_keys_values(w2)
o_w3 = interchange_keys_values(w3)

crypto_type = str(input("Do you want to encrypt of decrypt ? \n Press 'E' for encryption and 'D' for decryption:")).upper()

if(crypto_type == 'E' or  crypto_type == 'D'):
    print(crypto_type)
    plain_text = input("Enter your text : ").upper()
    plain_text_alphabets =list(plain_text)
    cypher_text = plain_text_alphabets.copy()

    r1 = 0
    r2 = 0
    # r3 = 0


    for i in range(0 , len(plain_text_alphabets)):

        if(any(plain_text_alphabets[ i ] in lr for lr in chars)):
            if(crypto_type == 'E'):
                cypher_text[i] = w3[w2[w1[f'{plain_text_alphabets[i]}']]]
                r1+=1
                w1 = rotate_dict_values(w1 , 1)
                if(r1 == len(w1)):
                    r1 = 0
                    r2+=1
                    w2 = rotate_dict_values(w2 , 1)
                    if(r2 == len(w2)):
                        r2 = 0
                        w3 = rotate_dict_values(w3 , 1)
            elif( crypto_type == 'D'):
                cypher_text[i] = o_w1[o_w2[o_w3[f'{plain_text_alphabets[i]}']]]
                r1+=1
                o_w1 = rotate_dict_keys(o_w1 , 1)
                if(r1 == len(o_w1)):
                    r1 = 0
                    r2+=1
                    o_w2 = rotate_dict_keys(o_w2 , 1)
                    if(r2 == len(o_w2)):
                        r2 = 0
                        o_w3 = rotate_dict_keys(o_w3 , 1)
        else:
            pass
    print(  "Required Text :" + "".join(cypher_text))

else:
    print("Invalid operation")
