#FONKSİYONLAR
def selamla():
    print("Merhaba!")
    print("Nasılsın?")

selamla() #ekrana Merhaba! Nasılsın? yazdıran bir fonksiyon oluşturduk.

def selamla2(isim):
    print("İsminiz:",isim) #fonksiyonun içinde bir değişken oluşturduk

selamla2("Hakan") #fonksiyonu değişken atayarak çalıştırabilir şekilde oluşturduk

selamla2(2) #İsminiz: 2 çıktısını verir

"""selamla2(ali) #hata verir """

def toplam(a,b,c):
    print("Toplam: ",a+b+c)

toplam(2,3,5) #fonksiyona atanand değerlerin toplamını veren bir fonksiyon oluşturduk

def faktoriyel(sayi): #girilen sayının faktöriyelini bulan fonksiyon oluşturduk
    faktoriyel=1
    if(sayi==0 or sayi==1):
        print("Sayının faktöriyeli:",faktoriyel)
    else:
        while(sayi>=1):
            faktoriyel*=sayi
            sayi-=1
        print("Sayının faktöriyeli: ",faktoriyel)

faktoriyel(5)

#fonksiyonları return ile çağırmak

def toplam2(a,b,c):
    return a+b+c

def ikikati(a):
    return a*2
#return kullanmadığımız fonksiyonları başka bir yerde kullanamayız. bundan önce yaptıklarımızda sadece ekran çıktılarını aldırdık.

print(ikikati(toplam2(2,3,5))) #öncelikle 2,3,5 sayılarına toplam2 fonksiyonunu uyguladı. sonrada elde edilen sayıya ikikati fonlsiyonunu uyguladı

def selam3(isim="İsimsiz"): #fonksiyona default değer atadık ve kullanıcı tarafından bir değer girilmemesi halinde bu değerin kullanılmasını sağladık
    print("İsminiz:",isim)
selam3()
selam3("mali")

def toplam3(*a): # * işareti sayesinde fonksiyonun içine istediğimiz sayıda değişken yazabiliriz.
# * kullanmazsak eğer fonksiyonun içinde kaç tane değişken tanımlatmışsak o kadar değer atayabiliyorduk.
    toplam = 0
    for i in a:
        toplam+=i
    print(toplam)
toplam3(5,6,9)

c=10
def fonksiyon():
    c=2
    print(c)
fonksiyon()
print(c) #burada ilk tanımlattığımız c global değişken, ikinci tanımlattığımız c ise lokal değişken.
#fonksiyon içinde lokal c'yi ekrana yazdırdığımız için program önce ekrana 2 yazacak
#sonrasında da fonksiyondan çıkıp global değişkeni yazdıracak. yani alt alta önce 2 sonra da 10 yazdıracak
d=10
def fonk():
    global d #global komutu ile lokalde kullanacağımız değişkenin globaldeki değerini kullandık ve değişiklik yapabilecek duruma getirdik
    d=2
    print(d)
fonk()
print(d) #alt alta 2 ve 2 yazacak

#lambda kullanımı

ikiylecarp = lambda x: x*2 #fonksiyon oluşturma ile aynı görevi görmekte

print(ikiylecarp(3))

topla4 = lambda x,y,z:x+y+z
print("lambda toplamı:",topla4(1,2,3))

def ters(isim):
    return isim[::-1] #girilen metni ters çeviren fonksşton

print(ters("selamlık"))

terslambda = lambda isim: isim[::-1]
print(terslambda("selamlık")) #ters çevirme işlemi yapan fonksiyonun lambda ile yapılmış hali

#lambda uzun fonksiyonlarda kullanılmaz

#asal sayı bulma fonksiyonu

def asal_mi(sayı):
    if(sayı==1):
        return False
    elif(sayı==2):
        return True
    else:
        for i in range(2,sayı):
            if(sayı%i==0):
                return False
        return True
while True:
    sayı=input("Sayı:")
    if (sayı=="q"):
        break
    else:
        sayı=int(sayı)
        if (asal_mi(sayı)):
            print(sayı,"sayısı asal bir sayıdır.")
        else:
            print(sayı, "sayısı asal bir sayı değildir.")

def  tambölenleribul(sayılar):
    tambölenler=[]
    for i in range(2,sayılar):
        if (sayılar%i==0):
            tambölenler.append(i)
    return tambölenler

while True:
    sayılar=input("Sayı:")
    if(sayılar=="q"):
        break
    else:
        sayılar=int(sayılar)
        print("Tam Bölenler: ",tambölenleribul(sayılar)) #bir sayıya ait tam bölenleri bulan ve ekrana yazdıran fonksiyon

