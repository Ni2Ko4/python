def work_money (hours, hour_pay, prize):
    return (hours * hour_pay) + prize

print(work_money(int(input('Введи количество часов')), float(input('Введи сумму за час')),
                 float(input('Введи сумму бонуса'))))