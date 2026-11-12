import tkinter as tk


def action1():
    s = entry.get()
    s = s.replace(',', '.')
    parts = s.split(' ')
    numbers = []
    result.delete(0, tk.END)
    try:
        for p in parts:
            if p != '':
                numbers.append(float(p))
    except ValueError:
        result.insert(0, 'Помилка: введіть дійсні числа')
        return
    if len(numbers) == 0:
        result.insert(0, 'Числа не введено')
        return
    mn = numbers[0]
    mx = numbers[0]
    for x in numbers:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    result.insert(0, 'Мінімальне: ' + str(mn) + '   Максимальне: ' + str(mx))


win = tk.Tk()
lb = tk.Label(text='Введіть дійсні числа через пробіл')
entry = tk.Entry(width=55)
button = tk.Button(text='Знайти', width=15, height=1, command=action1)
lb2 = tk.Label(text='Результат:')
result = tk.Entry(width=55)
lb.pack()
entry.pack()
button.pack()
lb2.pack()
result.pack()
win.mainloop()