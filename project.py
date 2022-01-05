import datetime as dt

FORMAT = '%H:%M:%S'
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    return False if len(data) != 2 or None in data else True


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if storage_data is not None:
        for item in storage_data:
            if dt.datetime.strptime(item, FORMAT).time() >= time:
                return False
        else:
            return True


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    return sum(storage_data.values()) + steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    return steps * STEP_M / 1000


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    hour = current_time.hour + current_time.minute / 60
    minutes = current_time.hour * 60 + current_time.minute
    mean_speed = dist / hour
    spent_calories = (.035 * WEIGHT + (mean_speed ** 2 / HEIGHT) * .029 * WEIGHT) * minutes
    return spent_calories


def get_achievement(dist):
    """Получить поздравления за пройденную дистанцию."""
    if dist >= 6.5:
        return 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        return 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        return 'Маловато, но завтра наверстаем!'
    else:
        return 'Лежать тоже полезно. Главное — участие, а не победа!'


def show_message(time, steps, dist, calories, achievement):
    print(f'''
Время: {time}.
Количество шагов за сегодня: {steps}.
Дистанция составила {dist:.2f} км.
Вы сожгли {calories:.2f} ккал.
{achievement}
''')


def accept_package(data):
    """Обработать пакет данных."""
    if check_correct_data(data) is False:
        return 'Некорректный пакет'
    time, steps = data
    pack_time = dt.datetime.strptime(time, FORMAT).time()
    if check_correct_time(pack_time) is False:
        return 'Некорректное значение времени'
    day_steps = get_step_day(steps)
    dist = get_distance(steps) + get_distance(sum(storage_data.values()))
    spent_calories = get_spent_calories(dist, pack_time)
    achievement = get_achievement(dist)
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    storage_data.update({data})
    return storage_data


package_0 = ('2:00:01', 505)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)
