pars = {
    ")" : "(",
    "]" : "["
}
def par_checker(string):
    stack = []

    for s in string:  # читаем строку посимвольно
        if s in pars.values():  # если открывающая скобка,
             stack.append(s)
        elif s in pars.keys():
            # если встретилась закрывающая скобка, то проверяем,
            # пуст ли стек и является ли верхний элемент открывающей скобкой
            if len(stack) and stack[-1] == pars[s]:
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0

print(par_checker("((([)))]"))