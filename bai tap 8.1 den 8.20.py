#bài 8.1
a=int(input("so a "))
b=int(input("so b "))
c=int(input("so c "))
d=int(input("so d "))
g=0
h=0
while(g<a)or(g<b)or(g<c)or(g<d):
     g+=1
h=g     
while(h>a)or(h>b)or(h>c)or(h>d):
     h-=1
print("max =",g)
print("min =",h)
#bai 8.2
a=int(input("nhap so "))
if a<0:
    print("|a| =",a*(-1))
else:
    print("|a| =",a)

#bai 8.3
a=int(input("nhap so "))
if a<0:
    print("|a| =",a*(-1))
else:
    print("|a| =",a)

#bai8.4
import math

a = int(input("canh thu nhat "))
b = int(input("canh thu hai "))
c = int(input("canh thu ba "))
p=(a+b+c)/2
h=math.sqrt(p*(p-a)*(p-c)*(p-b))
print("dien tich tam giac la",h)
 
 #bai 8.5
 a= int(input("nhap nam "))
if ((a%4==0)and(a%100!=0))or(a%400==0):
     print(a,"la nam nhuan")
else:
     print(a,"ko phai nam nhuan")

#bài 8.6
a = int(input("chon xe co 4 hay 7 cho "))
b = int(input("nhap so km "))
c = int(input("nhap thoi gian cho "))
if c<=5:
     c=0
if a==4 :
     if b<=0.8 :
         b= 11000
     if (b<=20)and(b>=0.8):
         b= b*12100
     else:
         b= (b-20)*10000 + 242000
     if c>5:
         c=(c-5)*800
     print("so tien phai tra",b+c)
if a==7 :
     if b<=0.8 :
         b= 13000
     if (b<=20)and(b>=0.8):
         b= b*14100
     else:
         b= (b-20)*12000 + 282000
     if c>5:
         c=(c-5)*800
     print("so tien phai tra",b+c)
if (a!=4)and(a!=7):
     print("khong co xe")
  
#bài 8.7
  a=int(input("nhap so kwh "))
if(a<=50):
     a= a*1678
if(a>50)and(a<=100):
     a= (a-50)*1734+50*1678
if(a>100)and(a<=200):
     a= (a-100)*2014+50*1734+50*1678
if(a>200)and(a<=300):
     a= (a-200)*2536+100*2014+50*1734+50*1678
if(a>300)and(a<=400):
     a= (a-300)*2834+100*2536+100*2014+50*1734+50*1678
if a>400:
     a= (a-400)*2927+100*2834+100*2536+100*2014+50*1734+50*1678
print("so tien phai tra",a)

#bài 8.8
a=int(input("nhap loai khach san "))
b=int(input("nhap loai khach dem "))
if a==1:
     if b==1 :
         print("so tien phai tra la 1260000")
     if (b>1)and(b<=3) :
         print("so tien phai tra la",((b*1260000)/100)*75) 
     if b>3:
         print("so tien phai tra la",((b*1260000)/100)*70)
if a==2:
     if b==1 :
         print("so tien phai tra la 1550000")
     if (b>1)and(b<=3) :
         print("so tien phai tra la",((b*1550000)/100)*75) 
     if b>3:
         print("so tien phai tra la",((b*1550000)/100)*70)
if a==3:
     if b==1 :
         print("so tien phai tra la 1830000")
     if (b>1)and(b<=3) :
         print("so tien phai tra la",((b*1830000)/100)*75) 
     if b>3:
         print("so tien phai tra la",((b*1830000)/100)*70)
if a==4:
     if b==1 :
         print("so tien phai tra la 1830000")
     if (b>1)and(b<=3) :
         print("so tien phai tra la",((b*1830000)/100)*75) 
     if b>3:
         print("so tien phai tra la",((b*1830000)/100)*70)
if a==5:
     if b==1 :
         print("so tien phai tra la 2120000")
     if (b>1)and(b<=3) :
         print("so tien phai tra la",((b*2120000)/100)*75) 
     if b>3:
         print("so tien phai tra la",((b*2120000)/100)*70)
if a==6:
     if b==1 :
         print("so tien phai tra la 2120000")
     if (b>1)and(b<=3) :
         print("so tien phai tra la",((b*2120000)/100)*75) 
     if b>3:
         print("so tien phai tra la",((b*2120000)/100)*70)
if a==7:
     if b==1 :
         print("so tien phai tra la 2540000")
     if (b>1)and(b<=3) :
         print("so tien phai tra la",((b*2540000)/100)*75) 
     if b>3:
         print("so tien phai tra la",((b*2540000)/100)*70)
if a==8:
     if b==1 :
         print("so tien phai tra la 480000000")
     if (b>1)and(b<=3) :
         print("so tien phai tra la",((b*480000000)/100)*75) 
     if b>3:
         print("so tien phai tra la",((b*480000000)/100)*70)    
a=int(input("nhap so "))
while a>0:
     print(a)
     if a==1:
         print("Start!!!")
     a-=1
#bài 8.10
a=int(input("nhap n "))
b=int(input("nhap x "))
t=(b*b+1)
i=1
h=1
while i<=a:
     h=h*t
     i+=1
print("S=(x*x+1)^n=",h)

#bài 8.12
a= int(input("nhap so "))
b = 2
if (a == 1 ) :
    print("không phải là số nguyên tố")
while (a>=b):
         if(a==b):
                  print(a,"là số nguyên tố")
                  break
         if (a%b==0):
                  print(a,"không phải là số nguyên tố")
                  break    
         b+=1       

#bài 8.13
a=int(input("nhap n "))
k=0
while a>0:
     print("nhap so thu ",a)
     h=int(input())
     k=k+h
     a-=1
     if a==0:
         print("tong cac so bang",k)
         break

#bài 8.13
h=1
k=0
while h!=0:
     h=eval(input("nhap h"))
     k=k+h
     if (h==0):
         print("tong cac so bang ",k)

#bài 8.16
a=int(input("nhap a "))
b=int(input("nhap b "))
c=2
while (a%c!=0)or(b%c!=0):
     c+=1
     if (a%c==0)and(b%c==0):
         print(c,"la uoc chung nho nhat")
         break
     if c>b and c>a:
         print("ko co uoc chung nho nhat")
         break    

#bài 8.17
a=int(input("nhap a "))
b=int(input("nhap b "))
if a>=b:
     c=a
else :
     c=b
if (a==b)or(a%b==0)or(b%a==0):
     print(a,"la boi chung nho nhat")
while (c%a!=0)or(c%b!=0):
     c+=1
     if (c%a==0)and(c%b==0):
         print(c,"la boi chung nho nhat")
         break

#bài 8.18.19
b=int(input("nhap so "))
c=1
h=0
while c<b:     
     if (b%c==0):
         h=h+c
         print(h)
     c+=1
if h==b:
     print(b,"la so hoan hao")
else :
     print(b," khong phai so hoan hao")

#bài 8.20
a=int(input("nhap e mu x "))
i=1
k=1
t=0
x=1
d=0
while i<=1000:
     k=k*a
     while t<=i:
         t+=1
         x=x*t
         if (t == i):
                 t=0
                 l=x
                 x=1
                 break
     m=k/l
     d=d+m   
     i+=1
print("e mu x=",d+1)
