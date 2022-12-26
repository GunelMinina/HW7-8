import view
import model

def run():
    action = view.render_main_menu()
    print(action)
    if action == '1':
        view.render_list(model.get_all())
    if action == '2':
        search_string = view.render_search_form()
        find_rows = model.find(search_string)
        if len(find_rows) > 0:
            view.render_list(find_rows)
        else:
            view.error('Запись не найдена')
    if action == '3':
        data = view.render_input_form()
        result = model.insert_row(data)
        if result:
            view.render_success_message(data)
        else:
            view.error('Не удалось добавить запись')
    if action == '4':
        id = view.render_id_form()
        result = model.find_by_id(id)
        if result:
            view.render_row(result)
            data = view.render_input_form()
            model.update(id, data)
        else:
            view.error('Запись не найдена')
    run() 