paragraf="""Son dönemde petrol fiyatlarindaki küresel gerileme
 ve döviz kurlarindaki değişimler, Türkiye'de akaryakit fiyatlarina indirim olarak yansidi.
 Ancak uluslararasi piyasalarda brent petrol fiyatlari
 yeniden yükselişe geçti. Bu nedenle benzin
ve motorin grubunda zam beklentisi oluştu."""


kelimeler=paragraf.split(' ')


def donustur(a):

    sayac = []

    for kelime in a:

       print(kelime)

       sayici = 0

       for harf in range(len(kelime)):

        sayici+=1

       print(sayici)

       sayac.append(sayici)

    return sayac

b = donustur(kelimeler)

print(b)   