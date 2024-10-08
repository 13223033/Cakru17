import random

class Robot: # Class Robot
    def __init__(self, name, health, attack_power):
        self.__name = name              # Enkapsulasi: menyembunyikan atribut robot
        self.__health = health 
        self.__attack_power = attack_power

    def get_name(self): # Metode untuk mendapatkan nama robot
        return self.__name

    def get_health(self):  # Metode untuk mendapatkan health robot
        return self.__health

    def is_alive(self): # Metode untuk mengecek apakah robot masih hidup
        return self.__health > 0

    def attack(self, other_robot): # Metode untuk menyerang robot lain
        damage = random.randint(1, self.__attack_power) # Menghitung damage yang diberikan secara random dengan range 1 hingga attack_power
        print(f"{self.__name} attacks {other_robot.get_name()} for {damage} damage!")
        other_robot.take_damage(damage) # Memanggil metode take_damage dari robot lain

    def take_damage(self, damage): # Metode untuk mengurangi health robot
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0
        print(f"{self.__name} has {self.__health} health left.") # Menampilkan health robot setelah diserang

class Battle: # Class Battle
    def __init__(self, robot1, robot2): # Constructor, Battle membutuhkan dua objek Robot
        self.__robot1 = robot1
        self.__robot2 = robot2

    def start_fight(self): # Metode untuk memulai pertarungan
        print("Battle Start!")
        print(f"{self.__robot1.get_name()} has {self.__robot1.get_health()} health.") # Menampilkan health awal robot pertama dan kedua
        print(f"{self.__robot2.get_name()} has {self.__robot2.get_health()} health.")
        while self.__robot1.is_alive() and self.__robot2.is_alive(): # Looping selama kedua robot masih hidup
            self.__robot1.attack(self.__robot2)
            if self.__robot2.is_alive(): # Cek apakah robot kedua masih hidup
                self.__robot2.attack(self.__robot1)
        
        self.declare_winner() # Memanggil metode declare_winner untuk deklarasi pemenang

    def declare_winner(self): # Metode untuk mendeklarasikan pemenang
        if self.__robot1.is_alive(): 
            print(f"{self.__robot2.get_name()} is defeated!")
            print(f"{self.__robot1.get_name()} wins!")
        else:
            print(f"{self.__robot1.get_name()} is defeated!")
            print(f"{self.__robot2.get_name()} wins!")

class Game: # Class Game
    def __init__(self): # Constructor, class Game tidak perlu atribut lainnya, karena hanya merupakan inisialisasi game
        self.__robots = [] # sef.__robots merupakan list yang berisi objek-objek Robot yang dipakai di game

    def add_robot(self, robot): # Metode untuk menambahkan robot ke dalam list robots
        self.__robots.append(robot)

    def start_game(self): # Metode untuk memulai game
        print("Choose robots for the battle:") 
        for index, robot in enumerate(self.__robots): # Menampilkan list robot yang bisa dipilih
            print(f"{index + 1}. {robot.get_name()}") 

        first_robot_index = int(input("Select the first robot: ")) - 1 
        second_robot_index = int(input("Select the second robot: ")) - 1

        robot1 = self.__robots[first_robot_index]
        robot2 = self.__robots[second_robot_index]

        battle = Battle(robot1, robot2) # Membuat objek Battle dengan dua robot yang dipilih
        battle.start_fight() # Memulai pertarungan`

# Contoh penggunaan
if __name__ == "__main__":
    game = Game()

    # Membuat beberapa objek Robot dengan berbagai atribut
    robot1 = Robot("RoboOne", 100, 30)
    robot2 = Robot("RoboTwo", 100, 25)
    robot3 = Robot("RoboThree", 100, 20)

    # Menambahkan robot-robot tersebut ke dalam objek Game
    game.add_robot(robot1)
    game.add_robot(robot2)
    game.add_robot(robot3)

    # Menjalankan game dan melakukan pertarungan antar robot
    game.start_game()
