- lb12
директория содержит автотесты для Лабораторной работы №12

- example.py автотест из примера Лабораторной работы №12

- example2.py автотест из примера Лабораторной работы №12

- test1.py 
Название	Авторизация с корректными учетными данными
Предусловие	Пользователь не авторизован в системе
Шаги	
-	Перейти на сайт магазина «ССО» на страницу авторизации
-	В поле «эл.почта» ввести почту kristina.puma8@gmail.com
-	В поле «Пароль» ввести пароль qazxsw12
Ожидаемый результат	Пользователь успешно авторизовался в системе.
На странице отображается имя текущего пользователя.
---
- test2.py 
Название	Добавление товара в корзину
Предусловие	Пользователь не авторизован в системе
Шаги	
-	Перейти на страницу товара
-	Кликнуть на кнопку «Купить»
Ожидаемый результат	Открывается страница корзины, доступно её содержимое.
---
- test3.py 
Название	Чтение новостей.
Предусловие	Пользователь не авторизован в системе
Шаги	
-	Перейти на страницу Новости
-	Кликнуть на новость под названием «СКИДКИ ДО 20% С 1 ПО 4 ИЮЛЯ!»
Ожидаемый результат	Открывается новая страница, на ней отображается информация по новости.
---
pr5
---
директория содержит автотесты для Практической работы №6
---
- test1.py 
Название	Успешная регистрация пользователя 
Предусловие	Пользователь находится на главной странице сайта
Шаги	
-	Кликаем на кнопку на кнопку «Войти»
-	Кликаем на кнопку «Зарегистрироваться»
-	Вводим данные в поля:
Логин: aobywa
Пароль: qazxsw12
Адрес электронной почты: aobywa@mailto.plus
-	Кликаем на кнопку «Зарегистрироваться»
Ожидаемый результат	Переход на главную страницу авторизированного пользователя.
---
- test2.py 
Название	Успешная авторизация пользователя
Предусловие	Пользователь находится на главной странице сайта, уже зарегистрирован.
Шаги	
-	Нажимаем на кнопку «Вход»
- В поле «Адрес электронной почты» вводим «aobywa@mailto.plus»
- В поле пароль вводим «qazxsw12»
- Кликаем на кнопку «Войти»
Ожидаемый результат	Авторизация прошла успешно, отображается главная страница авторизированного пользователя.
---
- test3.py 
Название	Переход с Главной страницы на страницу Ассортимент
Предусловие	Пользователь находится на сайте
Шаги	
-	Открыта главная страница.
-	Нажать на ссылку в меню «Ассортимент»
Ожидаемый результат	Переход на другую страницу выполнен успешно. 
---
- test4.py 
Название	Регистрация пользователя с уже существующей почтой.
Предусловие	Пользователь находится на главной странице сайта
Шаги	
-	Кликаем на кнопку на кнопку «Войти»
-	Кликаем на кнопку «Зарегистрироваться»
-	Вводим данные в поля:
Логин: fffff
Пароль: qazxsw12
Адрес электронной почты: aobywa@mailto.plus
-	Кликаем на кнопку «Зарегистрироваться»
Ожидаемый результат	Ошибка с сообщением, что пользователь уже зарегестрирован.
---
- test5.py 
Название	Регистрация пользователя с пустыми полями
Предусловие	Пользователь находится на главной странице сайта
Шаги	
-	Кликаем на кнопку на кнопку «Войти»
-	Кликаем на кнопку «Зарегистрироваться»
-	Пропустить заполнение полей
-	Кликаем «Зарегистрироваться»
Ожидаемый результат	Сработает валидация полей «Обязательное поле!»
---
- test6.py 
Название	Авторизация с не верным паролем
Предусловие	Пользователь находится на главной странице сайта
- Шаги	
  -	Кликаем на кнопку на кнопку «Войти» 
  - В поле Эл. Почта вводим «aobywa@mailto.plus»
  - В поле пароль вводим «123456789»
  - Кликаем на кнопку «Войти»
Ожидаемый результат	Ошибка о вводе неверных данных «Неверный пароль».
---
- test7.py 
Название	Переход на главную страницу по логотипу в меню
Предусловие	Пользователь находится на сайте
- Шаги	
  -	Открываем страницу «Ассортимент»
  -	Нажимаем на логотип
Ожидаемый результат	Перейдем на главную страницу сайта.
