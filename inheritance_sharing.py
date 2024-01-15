es_var_mi = input("Murisin  esi var mi ?  (evet icin e hayir icin hersey) :  ")
while True:
    try:
        cocuk_var_mi = int(input("Murisin hayatta olan ve ya ölmüş olup altsoyu olan cocuk sayisi? : "))
        if cocuk_var_mi < 0:
            raise ValueError("Hata: Negatif sayi giremezsiniz. Lütfen 0 ve ya pozitif sayi giriniz.")
        break  
    except ValueError as e:
        print("Hata: Sayisal deger giriniz ,- 0 ve ya pozitif herhangi bir sayi-")  


    
miras_miktari=100

if cocuk_var_mi>=1:
    if es_var_mi == "e":
        es= 25
        cocuklar= 75/cocuk_var_mi
        print(f'Miras paylaşimi :  Esinin payi : {es}, hayatta ve ya ölmüş olup altsoyu olan cocuk sayisi : {cocuk_var_mi} , her birine düsen pay : {cocuklar}')
    elif es_var_mi != "e":
        cocuklar = 100 /cocuk_var_mi
        print(f'Miras paylaşimi : Hayatta ve ya ölmüş olup altsoyu olan cocuk sayisi : {cocuk_var_mi} , her birine düsen pay : {cocuklar}')

elif cocuk_var_mi==0:
    if es_var_mi == "e":
        anne_hayatta_mi= input("Murisin annesi hayatta  mi ? (evet için e , hayir için diger her sey): ")
        baba_hayatta_mi= input("Murisin babasi hayatta  mi ? (evet için e , hayir için diger her sey): ")
        while True:
            try:
                kardes_sayisi = int(input ("Murisin hayatta olan ve ya ölmüs olup altsoyu olan kardes sayisi kactir ? : "))
                if kardes_sayisi < 0:
                    raise ValueError("Hata: Negatif sayi giremezsiniz. Lütfen 0 ve ya pozitif sayi giriniz.")
                break  
            except ValueError as e:
                print("Hata: Sayisal deger giriniz ,- 0 ve ya pozitif herhangi bir sayi-")  
        
        if anne_hayatta_mi == "e"and baba_hayatta_mi == "e" :
            es= 50
            anne= 25
            baba = 25
            print(f'Miras paylasimi :  Es: {es}, Annesi :{anne},Baba: {baba}')
        elif anne_hayatta_mi != "e"and baba_hayatta_mi == "e" :
            es=50
            baba=25 
            kardesler = 25 / kardes_sayisi
            print(f'Miras paylasimi : Es: {es}, Babasi : {baba}, Hayatta olan ve ya ölmüs olup altsoyu olan her bir kardes payi: {kardesler}')
        elif anne_hayatta_mi == "e"and baba_hayatta_mi != "e" :
            es=50
            anne=25 
            kardesler = 25 / kardes_sayisi
            print(f'Miras paylasimi : Es: {es}, anne : {anne}, Hayatta olan ve ya ölmüs olup altsoyu olan her bir kardes payi: {kardesler}')
        elif anne_hayatta_mi != "e" and baba_hayatta_mi != "e" and kardes_sayisi >= 1 :
            es=50
            kardesler = 50 / kardes_sayisi
            print(f'Miras paylasimi : Es: {es}, Hayatta olan ve ya ölmüs olup altsoyu olan her bir kardes payi: {kardesler}')
        elif anne_hayatta_mi != "e" and baba_hayatta_mi != "e" and kardes_sayisi == 0:
            
            payhakkiolanlar = []

            anneanne_hayatta_mi = input("Murisin anneannesi hayatta mi ve ya ölmüş ise alt soyu var mi? (evet için 'e', hayir için diğer her şey): ")
            annebaba_hayatta_mi = input("Murisin anne tarafindan dedesi hayatta mi ve ya ölmüş ise alt soyu var mi? (evet için 'e', hayir için diğer her şey): ")
            babaanne_hayatta_mi = input("Murisin babaannesi hayatta mi ve ya ölmüş ise alt soyu var mi? (evet için 'e', hayir için diğer her şey): ")
            babababa_hayatta_mi = input("Murisin baba tarafindan dedesi hayatta mi ve ya ölmüş ise alt soyu var mi? (evet için 'e', hayir için diğer her şey): ")

            if anneanne_hayatta_mi.lower() == 'e':
                payhakkiolanlar.append("Anneanne")
                
            if annebaba_hayatta_mi.lower() == 'e':
                payhakkiolanlar.append("Anne tarafindan Dede")
                
            if babaanne_hayatta_mi.lower() == 'e':
                payhakkiolanlar.append("Babaanne")
                
            if babababa_hayatta_mi.lower() == 'e':
                payhakkiolanlar.append("Baba tarafindan Dede")
                
            if len(payhakkiolanlar)== 0 :
                print("Miras paylasimi Es :100")
            elif len(payhakkiolanlar)==1 :
                print("Miras paylasimi Es :75 ve pay hakki kisi basina 25 , pay hakki olanlar: ", ",".join(payhakkiolanlar))
            elif len(payhakkiolanlar)==2 :
                print("Miras paylasimi Es :75 ve pay hakki kisi basina 12.5 , pay hakki olanlar: ", ",".join(payhakkiolanlar))
            elif len(payhakkiolanlar)==3 :
                print("Miras paylasimi Es :75 ve pay hakki kisi basina 8.33, pay hakki olanlar: ", ",".join(payhakkiolanlar))
            elif len(payhakkiolanlar)==4 :
                print("Miras paylasimi Es :75 ve pay hakki kisi basina 6.25, pay hakki olanlar: ", ",".join(payhakkiolanlar))
                
         
    elif es_var_mi != "e":
        anne_hayatta_mi= input("Murisin annesi hayatta  mi ?(evet için e , hayir için diger her sey) : ")
        baba_hayatta_mi= input("Murisin babasi hayatta  mi ?(evet için e , hayir için diger her sey) : ")
        while True:
            try:
                kardes_sayisi = int(input ("Murisin hayatta olan ve ya ölmüs olup altsoyu olan kardes sayisi kactir ? : "))
                if kardes_sayisi < 0:
                    raise ValueError("Hata: Negatif sayi giremezsiniz. Lütfen 0 ve ya pozitif sayi giriniz.")
                break  
            except ValueError as e:
                print("Hata: Sayisal deger giriniz ,- 0 ve ya pozitif herhangi bir sayi-") 
        if anne_hayatta_mi == "e"and baba_hayatta_mi == "e" :
            anne= 50
            baba = 50
            print(f'Miras paylasimi : Annesi :{anne},Baba: {baba}')
        elif anne_hayatta_mi != "e"and baba_hayatta_mi == "e"  and kardes_sayisi != 0 :
            baba=50
            kardesler = 50 / kardes_sayisi
            print(f'Miras paylasimi : Babasi : {baba}, Hayatta olan ve ya ölmüs olup altsoyu olan kardes sayisi :{kardes_sayisi}, her birine dusen pay: {kardesler}')
        elif anne_hayatta_mi == "e"and baba_hayatta_mi != "e" and kardes_sayisi != 0 :
            anne=50 
            kardesler = 50 / kardes_sayisi
            print(f'Miras paylasimi : Anne : {anne}, Hayatta olan ve ya ölmüs olup altsoyu olan kardes sayisi :{kardes_sayisi}, her birine dusen pay: {kardesler}')
        elif anne_hayatta_mi != "e" and baba_hayatta_mi != "e" and kardes_sayisi != 0  :
           
            kardesler = 100 / kardes_sayisi
            print(f'Miras paylasimi : Hayatta olan ve ya ölmüs olup altsoyu olan kardes sayisi :{kardes_sayisi}, her birine dusen pay: {kardesler}')
        elif anne_hayatta_mi != "e" and baba_hayatta_mi != "e" and kardes_sayisi == 0 :
            payhakki = []

            anneanne_hayatta_mi = input("Murisin anneannesi hayatta mi ve ya ölmüş ise alt soyu var mi? (evet için 'e', hayir için diğer her şey): ")
            annebaba_hayatta_mi = input("Murisin anne tarafindan dedesi hayatta mi ve ya ölmüş ise alt soyu var mi? (evet için 'e', hayir için diğer her şey): ")
            babaanne_hayatta_mi = input("Murisin babaannesi hayatta mi ve ya ölmüş ise alt soyu var mi? (evet için 'e', hayir için diğer her şey): ")
            babababa_hayatta_mi = input("Murisin baba tarafindan dedesi hayatta mi ve ya ölmüş ise alt soyu var mi? (evet için 'e', hayir için diğer her şey): ")

            if anneanne_hayatta_mi.lower() == 'e':
                payhakki.append("Anneanne")
                
            if annebaba_hayatta_mi.lower() == 'e':
                payhakki.append("Anne tarafindan Dede ")
                
            if babaanne_hayatta_mi.lower() == 'e':
                payhakki.append("Babaanne ")
                
            if babababa_hayatta_mi.lower() == 'e':
                payhakki.append("Baba tarafindan Dede ")
                
            if len(payhakki)== 0 :
                print("Mirasin tamami devlete aittir !")
            elif len(payhakki)==1 :
                print("Miras paylasimi : pay hakki kisi basina 100 , pay hakki olanlar: ", ", ".join(payhakki))
            elif len(payhakki)==2 :
                print("Miras paylasimi : pay hakki kisi basina 50 , pay hakki olanlar: ", ", ".join(payhakki))
            elif len(payhakki)==3 :
                print("Miras paylasimi : pay hakki kisi basina 33.3, pay hakki olanlar: ", ", ".join(payhakki))
            elif len(payhakki)==4 :
                print("Miras paylasimi : pay hakki kisi basina 25, pay hakki olanlar: ", ", ".join(payhakki))
