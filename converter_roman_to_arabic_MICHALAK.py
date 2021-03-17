def converter_roman_to_arabic(user_roman):
    roman_numbers = 'IVXLCDM'
    arabic_numbers = [1, 5, 10, 50, 100, 500, 1000]
    user_arabic = []
    user_arabic_final = []
    step_number = 0
    user_roman_upper = user_roman.upper()

    try:
        for y in user_roman_upper:
            assert(y in roman_numbers), "To nie jest rzymska liczba"
    except:
        raise

    for x in user_roman_upper:
        user_arabic.append(arabic_numbers[roman_numbers.find(x)])

    while step_number < len(user_arabic):
        if step_number < len(user_roman_upper):
            if len(user_arabic) == 1:
                user_arabic_final.append(user_arabic[step_number])
                break
            elif step_number < (len(user_arabic)-1) and user_arabic[step_number] < user_arabic[step_number+1]:
                user_arabic_final.append(user_arabic[step_number + 1] - user_arabic[step_number])
                #print(user_arabic_final)
                step_number = step_number + 2
                #print(step_number)
            else:
                user_arabic_final.append(user_arabic[step_number])
                #print(user_arabic_final)
                step_number = step_number + 1
                #print(step_number)
    print(f'Rzymskie: {user_roman_upper} to arabksie: {sum(user_arabic_final)}')


user_roman = (input('Podaj rzymska liczbe: '))


converter_roman_to_arabic(user_roman)
