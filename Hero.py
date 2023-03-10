class Hero():
  def __init__(self, name, health, power, armor, weapon):
    self.name = name
    self.health = health
    self.power = power
    self.armor = armor
    self.weapon = weapon

  def print_info(self):
    print("New hero")
    print("Hero name is", self.name)
    print("Health", self.health)
    print("Power", self.power)
    print("Armor", self.armor)
    print("Weapon", self.weapon)

  def strike(self, enemy):
    print("Hit!", self.name, "attacking", enemy.name)
    enemy.armor = enemy.armor - self.power
    if enemy.armor <=0:
      enemy.health = enemy.health + enemy.armor
      enemy.armor = 0
    print(enemy.name, "armor:", enemy.armor, "and health:", enemy.health)
