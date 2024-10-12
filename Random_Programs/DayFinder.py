d={
    0:"Saturday",
    1:"Sunday",
    2:"Monday",
    3:"Tuesday",
    4:"Wednesday",
    5:"Thursday",
    6:"Friday"
}
print("Enter Details Like \"1 14 2024\" " )
a=input()
s=a.strip().split()
if int(s[1])>12:
    year=int(s[2])-1
    year=str(year)
else:
    year=s[2]
h=int(((int(s[0]))+int((13*((int(s[1])+1)/5)))+int(year[2:5])+int((int(year[2:5])/4))+int((int(year[:2])/4))-2*(int(year[:2]))))%7
print(f"The day of the date {s} is {d[h]}") 