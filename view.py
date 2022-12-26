def render_main_menu():
   print('Выберите действие:')
   print('1 - Отобразить весь справочник')
   print('2 - Поиск записи')
   print('3 - Добавить запись')
   print('4 - Изменить запись')
   
   num = input('Введите цифру: ')
   if (num != '1' and num != '2' and num != '3'  and num != '4'):
        print('Некорректный ввод')
        return render_main_menu()
   else:
        return num

def render_list(data):
    for row in data:
        render_row(row)

def render_row(row):
    print(f"{row['id']}  {row['lastname']} {row['firstname']}, тел.: {row['phone']}")

def render_search_form():
    return input('Введите Имя, Фамилию или телефон: ')

def render_success_message(data):
    print('')
    print('Запись добавлена в БД:')
    render_row(data)
    print('')

def render_input_form():
    data = {}
    data['firstname'] = input('Введите имя: ')
    data['lastname'] = input('Введите фамилию: ')
    data['phone'] = input('Введите телефон: ')
    return data

def render_id_form():
    return input('Введите id записи: ')

def error(errorMsg):
    print(errorMsg)