# Cервис терминологии

Сервис терминологии позволяет добавлять новые справочники, новые версии справочников, указывать дату начала действия 
и наполнять справочники элементами. API предоставляет следующие методы:

- получение списка справочников
- получение списка справочников, актуальных на указанную дату
- получение элементов заданного справочника текущей версии
- валидация элементов заданного справочника текущей версии
- получение элементов заданного справочника указанной версии
- валидация элемента заданного справочника по указанной версии

### Как запустить

Для запуска сервиса вам понадобится Python >= 3.8:
- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Создайте файл базы данных и сразу примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

### Как использовать API

* получение списка справочников:
```sh
 GET /handbooks/?page=Номер страницы
```

* получение списка справочников, актуальных на указанную дату:
```sh
 GET /handbooks/?date=YYYY-MM-DD
```

* получение элементов заданного справочника текущей версии:
```sh
 GET /elements_handbook/?handbook_name=Название справочника
```

* валидация элементов заданного справочника текущей версии:
```sh
 GET /validate_elements_handbook/?handbook_name=Название справочника
```

* получение элементов заданного справочника указанной версии:
```sh
 GET /elements_handbook/?handbook_name=Название справочника&version=Номер версии
```

* валидация элемента заданного справочника по указанной версии:
```sh
 GET /validate_elements_handbook/?handbook_name=Название справочника&version=Номер версии
```