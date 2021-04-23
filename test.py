import random

class Player(object):
	# Персонаж игры.
	def __init__(self, name):
		self.name = name
		self.health = 100
	def __str__(self):
		rep = (f"\tПерсонаж {self.name}, {self.health} HP")
		return rep
	def ability_1(self, enemy):
		# Способность наносить урон в диапозоне  18 - 25.
		ability_power = random.randint(-25, -18)
		enemy.use(ability_power)
		print(f"Персонаж {self.name} наносит {-ability_power} едениц умеренного урона персонажу {enemy.name}.")
	def ability_2(self, enemy):
		# Способность наносить урон в диапозоне  10 - 35.
		ability_power = random.randint(-35, -10)
		enemy.use(ability_power)
		print(f"Персонаж {self.name} наносит {-ability_power} едениц большого урона персонажу {enemy.name}.")
	def ability_3(self, enemy):
		# Способность излечивать себя в диапозоне 18 - 25.
		ability_power = random.randint(18 ,25)
		enemy.use(ability_power)
		print(f"Персонаж {self.name} исцеляет себя на {ability_power} едениц здоровья.")
	def random_ability(self, enemy):
		# Выбор случайной сбособности.
		ability = [self.ability_1, self.ability_2, self.ability_3]
		ability = random.choices(ability, [1, 1, 1])
		# Вероятность выбора каждой способности 1/3.
		if ability[0] == self.ability_3:
			# Использовать способность на себя, если это способность - лечение.
			ability[0](self)
		else:
			ability[0](enemy)
	def use(self, ability_power):
		# Применение способности.
		self.health += ability_power
		if self.health <= 0:
			self.health = 0
		if self.health >= 100:
			self.health = 100
	def die(self):
		# Персонаж умер.
		if self.health <= 0:
			self.health = 0
			return True
	def lose(self):
		# Персонаж проиграл.
		print(f"Персонаж {self.name} проиграл!")
	def win(self):
		# Персонаж выиграл.
		print(f"\nПерсонаж {self.name} одержал победу!")
		
class Computer(Player):
	# Персонаж игры - Компьютер.
	def random_ability(self, enemy):
		ability = [self.ability_1, self.ability_2, self.ability_3]
		if self.health < 35:
			# Увеличение шанса на лечение при достижение здоровья персонажа < 35.
			print(f"Персонаж {self.name} увеличил шанс на исцеление.")
			ability = random.choices(ability, [1, 1, 2])
			# Вероятность выбора способностей 1/4, 1/4, 1/2 соответсвенно.
		else:
			ability = random.choices(ability, [1, 1, 1])
		if ability[0] == self.ability_3:
			ability[0](self)
		else:
			ability[0](enemy)	

class Game(object):
	# Игровой процесс.
	def __init__(self, name):
		self.player = Player(name)
		self.machine = Computer("Компьютер")
	def move_selection(self):
		# Случайный выбор хода.
		return random.randint(0, 1)
	def play(self):
		if self.move_selection():
			print(f"\nХодит персонаж - {self.player.name}:")
			self.player.random_ability(self.machine)
			print(self.player, self.machine, sep = '\n')
		else:
			print(f"\nХодит персонаж - {self.machine.name}:")
			self.machine.random_ability(self.player)
			print(self.player, self.machine, sep = '\n')
		if self.player.die():
			self.machine.win()
			self.player.lose()
		if self.machine.die():
			self.player.win()
			self.machine.lose()	

def main():
	input("Нажмите Enter, чтобы начать.")
	game = Game("Игрок")
	while(not game.player.die() and not game.machine.die()):
		game.play()
	input("\n\n Нажмите Enter, чтобы выйти.")

main()

