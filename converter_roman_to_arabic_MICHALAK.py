def converter_roman_to_arabic(user_roman):
    roman_numbers = 'IVXLCDM'   # deklaracja stringa liter odpowiadających rzymskim liczbom
    arabic_numbers = [1, 5, 10, 50, 100, 500, 1000]     # deklaracja arabskich wartosci dla odpowiednich indeksow rzymskich znakow
    user_arabic = []    # deklaracja ciagu do ktorego zostana zapisane arabksie odpowiedniki wprowadzonego rzmyskiego ciagu
    user_arabic_final = []  # deklaracja ciagu do ktorego zostanie zapisana ostateczne arabska wersja ciagu uwzgledniajaca takie liczby jak np.: IV, IX, itd...
    step_number = 0  # deklaracja kroku uzytego w funkcji if pozwalajacego na laczenie znakow: np.: IV w 4
    user_roman_upper = user_roman.upper()   # zabezpieczenie przed wprowadzeniem malych liter. Zamiana wprowadzonego ciagu liter na ciag wielkich liter

    for x in user_roman_upper:
        user_arabic.append(arabic_numbers[roman_numbers.find(x)]) # przekonwertowanie ciagu liter na ciag odpowiadajacych im wartosci

    while step_number < len(user_arabic):
        if step_number < len(user_roman_upper):     # jezeli podany przez uzytkowanika ciag ma tylko jedna litere
            if len(user_arabic) == 1:
                user_arabic_final.append(user_arabic[step_number])
                break
            elif step_number < (len(user_arabic)-1) and user_arabic[step_number] < user_arabic[step_number+1]:
                user_arabic_final.append(user_arabic[step_number + 1] - user_arabic[step_number])
                print(user_arabic_final)
                step_number = step_number + 2
                print(step_number)
            else:
                user_arabic_final.append(user_arabic[step_number])
                print(user_arabic_final)
                step_number = step_number + 1
                print(step_number)
    print(f'Rzymskie: {user_roman_upper} to arabksie: {sum(user_arabic_final)}')


user_roman = (input('Podaj rzymska liczbe: '))


converter_roman_to_arabic(user_roman)
