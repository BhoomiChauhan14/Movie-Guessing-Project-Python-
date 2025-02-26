import random as r
import os
movie_collection= ["BHEDIYA","taare zamin par","SHAITAN","BAHUBALI","PUSHPA","HARI PUTTAR","GOLMAAL","HERA PHERI","HOUSEFULL,"]
while(1):
    movie = movie_collection[r.randint(0,len(movie_collection))]
    movie=movie.lower()
    in_st=""
    for i in movie:
        if i in"aeiou ":
            in_st+=i
        else:
            in_st+="_"
    key= "BOLLYWOOD"
    chance=9
    count=0
    while count<chance:
        os.system('cls')
        print("\n") 
        print("\t\t\t\t",key)
        print("\n") 
        print("\t\t\t\t",in_st.upper())
        char = input("Enter the Guessing Character:")
        char=char.lower()
        if char in movie:
            for i in range(len(movie)):
                if movie[i] == char:
                    in_st= in_st[:i]+char+in_st[i+1:]
            if in_st == movie:
                print(in_st.upper())
                print("Congratulations!!!!! You Won!!!!!")
                break
        else:
            key= key[:count]+char+key[count+1:]
            count+=1
    else:
        print("Better luck next time!!! You Lost!!!")
    c=input("do you want to play again?(y/n)")
    if c!='y':
        break
        