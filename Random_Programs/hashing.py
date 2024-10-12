s={
    1:[],
    2:[],
    3:[],
    4:[],
    5:[],
    6:[],
    7:[],
    8:[],
    9:[],
    0:[]
}
def hashfun(word):
    s=0
    for i in word:
        s=s+ord(i)
    return s%10
def addhash(hv,word):
    s[hv].append(word)
def findhash(hv,a):
    for i in s[hv]:
        if i == a:
            print(i)

    
data= ['Jones','Lisa','Stuart','Bob','Siri','Pete']
for i in data:
    hv=hashfun(i)
    addhash(hv,i)
print(s)
a=input("Enter the name ")
findhash(hashfun(a),a)

