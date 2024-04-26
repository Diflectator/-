print("\nРасчёт стоимости тиражирования")
while True:
    additionally = 1
    error_message1 = "Требуется ввести целое положительное число"
    while True:
        try:
            edition = int(input("\nТираж (шт.): "))
            if edition > 0:
                break;
            else:
                print(error_message1)
        except ValueError:
            print(error_message1)
    while True:
        try:
            sheet_format = int(input("Формат листа А (от 0 до 5): "))
            if 0 <= sheet_format <= 5:
                break;
            else:
                print("Неверный формат листа")
        except ValueError:
            print(error_message1)
    while True:
        delayed_printing = input("Отложенная печать?(y/n): ")
        if delayed_printing == "y" or delayed_printing == "n":
            break;
    if delayed_printing == "y":
        additionally = additionally + 0.25
        customer = "при клиенте"
    else:
        customer = "отложенно"
    cost = 2**(5-sheet_format)*edition*additionally
    remainder = edition % 10
    if remainder == 1:
        word_ending = "а"
    else:
        word_ending = "ов"
    sheet_format = str(sheet_format)
    print("Стоимость печати",edition,"лист"+word_ending,"А"+sheet_format,customer,"-",cost,"руб.")
    while True:
        continuation = input("\nВыйти?(y/n): ")
        if delayed_printing == "y" or delayed_printing == "n":
            break;
    if continuation == "y":
        break;
