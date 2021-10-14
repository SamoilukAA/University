import pandas as pd

plan = pd.read_csv("curriculum.csv")
payment = pd.read_csv("payment.csv")
online = pd.read_csv("online.csv")
offline = pd.read_csv("offline.csv")

# 22 - кол-во студентов в группе, 16 - кол-во групп(4 курса по 4 группы на каждом)
n = 22
k = 16 

print(plan['professors'][7])
# Зарплаты для всех работников
salary = 0;
# Зарплата преподавателям
for i in range (0, 8):
    salary += plan['professors'][i] * payment['professor'][0] * 12
# Зарплата двум бухгалтерам, системному администратору, двум методистам
salary += (payment['accountant'][0] * 2 + payment['system_administrator'][0] + payment['methodist'][0]) * 2 * 12
salary = salary + salary * 0.301 # налоги, которые отправляются в фонд оплаты труда

# Затраты для онлайн обучения (зарплаты и 5 платных аккаунтов в zoom)
cost_online = salary + 5 * online['zoom'][0] * 12

# Затраты на оффлайн обучение (зарплаты и допольнительные расходы)
s = 20 # аудитория площадью 20 кв. м на одну группу
ts = 20 * 16 + 4 * 5 # общая площадь аудиторий + площадь двух комнат для преподавателей, комнаты для методистов, охранника 
# и гардеробщицы по 4 кв. м
# Дополнительные расходы
cost = offline['rent'][0] * ts * 12 # затраты на аренду
# Запрлата охраннику, гардеробщице, уборщицам
sal = offline['security'][0] * 12 + offline['housemaid'][0] * 2 * 12 + offline['checkroom_attendant'][0] * 12
sal = sal + sal * 0.301
cost += sal
cost += offline['Internet'][0] * 12 + offline['equipment'][0] / 5 # затраты на интернет и обновление оборудования раз в 5 лет
cost += offline['communal_payment'] * 12 + offline['expenses'] * 12 # затраты на коммунальные платежи и ежемесечная закупка
# канцелярии, бумаги, антисептика и т.д.
cost_offline = salary + cost

n = n * k # общее число студентов
c_online = cost_online // n
c_offline = cost_offline // n
print('Стоимость онлайн обучения в год = ', c_online)
print('Стоимость оффлайн обучения в год = ', c_offline) 