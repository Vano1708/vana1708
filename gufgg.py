import random

# Класс бойца
class Fighter:
    def __init__(self, name='Неизвестно', health=20, armour=3, damage=4):
        # Имя бойца
        self.name = name
        # Здоровье
        self.health = health
        # Броня
        self.armour = armour
        # Наносимый урон
        self.damage = damage

    # Перевод объекта в формат строки (чтобы работала запись типа print(player))
    def __str__(self):
        return f'👤 Имя: {self.name}\n♡ Здоровье: {self.health}\n🛡 Броня: {self.armour}\n🗡 Урон: {self.damage}'

    # Получение урона бойцом
    def take_damage(self, damage):
        # Механика брони реализована таким образом, что от урона отнимается случайное число от 0 до показателя брони
        # Т.е. при наносимом уроне в 10 единиц и броне в 3 единицы итоговый урон будет в диапазоне 7-10
        # Функция max позволяет ограничить минимальный урон нулём, исключая отрицательные значения
        final_damage = max(0, damage - random.randint(0, self.armour))
        # Функция min нужна для того, чтобы здоровье не упало ниже нуля
        self.health -= min(self.health, final_damage)
        # Возвращаем итоговый урон, чтобы вывести его в функции attack
        return final_damage

    # Нападение на другого бойца
    def attack(self, enemy):
        # Вызываем функцию получения урона противником, где реализован механизм брони
        final_damage = enemy.take_damage(self.damage)
        # Выводим результат нападения
        print(f' ⚔ {self.name} атаковал {enemy.name} и нанёс {final_damage} урона. У {enemy.name} осталось {enemy.health} здоровья.')


# Создание бойцов (объектов на основе класса Fighter)
player1 = Fighter()
print(' -- Игрок 1 --')
print(player1)

player2 = Fighter(name='Дима', health=30, armour=3, damage=3)
print('\n -- Игрок 2 --')
print(player2)

player3 = Fighter(name='Ваня', health=30, armour=6, damage=3)
print('\n -- Игрок 3 --')
print(player3)

player4 = Fighter(name='Михаил', health=25, armour=8, damage=5)
print('\n -- Игрок 4 --')
print(player4)

# Реализация боя
rounds = 1


players_alive = [player1, player2, player3, player4]
while len(players_alive) > 1:
    print(f' === РАУНД {rounds} ===')
    # Поиск и атака противника
    for player in players_alive:
        enemy = player
        while enemy == player:
            enemy = random.choice(players_alive)
        player.attack(enemy)

    # Удаление побеждённых игроков
    for player in players_alive:
        if player.health <= 0:
            players_alive.remove(player)

    rounds +=1

    if rounds == 40:
        break

