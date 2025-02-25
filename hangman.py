import random
secret_words=['APPLE','MANGO','GUAVA','CHERRY','STRSWBERRY','BANANA']
word=random.choice((secret_words))
chances=(len(word))+2
user_input=""
# the p is a list created to maintain the status of the game
p=["?"]*len(word)
p[0]=word[0]
p[-1]=word[-1]
print(" ".join(p))


while chances>0:
    counter=0
    guesses=input("enter a desired character: ").upper()
    user_input+=guesses

    for i,char in enumerate(word):
        if char in user_input:
            p[i]=char
        else:
            p[i]="?"
            counter+=1
    p[0]=word[0]
    p[-1]=word[-1]
    print(" ".join(p))

    if "?" not in p:
        print("you won")
        break
    if guesses not in word:
        chances-=1
        print(chances,"more chances are left")
    if chances==0:
        print("sorry you lost")
        break
