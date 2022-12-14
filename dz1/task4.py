
"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


def acces1(users: dict, user_login: str, user_password: str):
    '''
    Функция реализует проверку может ли пользователь быть допущен к ресурсу

    Сложность O(N)
    '''

    for key, value in users.items():                                            #O(N)
        if key == user_login:                                                   #O(1)
            if value['password'] == user_password and value['activate']:        #O(1)
                return "Добро пожаловать!"                                      #O(1)
            elif value['password'] == user_password and not value['activate']:  #O(1)
                return "Необходимо активировать учетную запись"                 #O(1)
            elif value['password'] != user_password:                            #O(1)
                return "Неверный пароль"                                        #O(1)
    return "Неверный логин"                                                     #O(1)


def acces2(users: dict, user_login: str, user_password: str):
    '''
    Функция реализует проверку может ли пользователь быть допущен к ресурсу

    Сложность O(1)
    '''
    if users.get(user_login):                                                                       #O(1)
        if users[user_login]['password'] == user_password and users[user_login]['activate']:        #O(1)
            return "Добро пожаловать!"                                                              #O(1)
        elif users[user_login]['password'] == user_password and not users[user_login]['activate']:  #O(1)
            return "Необходимо активировать учетную запись"                                         #O(1)
        elif users[user_login]['password'] != user_password:                                        #O(1)
            return "Неверный пароль"                                                                #O(1)
    else: return "Неверный логин"                                                                   #O(1)


'''
Вторая функция эфективнее так как ее сложность константная
'''


base_users = {'user1': {'password': '1234', 'activate': True},
              'user2': {'password': '1234', 'activate': True},
              'user3': {'password': '1234', 'activate': False},
              'user4': {'password': '1234', 'activate': True}
          }


print(acces1(base_users, 'user4', '1134'))

print(acces2(base_users, 'user2', '1234'))

