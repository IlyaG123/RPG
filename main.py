import random
import time
class Player:
    def __init__(self, name, hp, dmg):
        self.name= name
        self.hp= hp
        self.dmg= dmg
        self.exp=0
        self.lvl=1
    def create_player(name, race1, prof1):
        hp=0
        dmg=0
        if race1==race[0]:
            hp+=50
            dmg+=100
        elif race1==race[1]:
            hp+=30
            dmg+=70
        elif race1==race[2]:
            hp+=100
            dmg+=150
        elif race1==race[3]:
            hp+=70
            dmg+=90
        else:
            print("Ошибка, напишите правильно")
        if prof1==prof[0]:
            hp+=50
            dmg+=100
        elif prof1==prof[1]:
            hp+=70
            dmg+=50
        elif prof1==prof[2]:
            hp+=40
            dmg+=100
        else:
            print("Ошибка, напишите правильно")
        return Player(name, hp, dmg)
    def attack(self, victim):
        max_ex=self.lvl*100
        victim.hp-=self.dmg
        if victim.hp<=0:
            print("Враг повержен, тебе плюс 20 очков опыта")
            self.exp+=20
            if self.exp>=max_ex:
                self.lvl_up(max_ex)
            thing=random.randint(0,3)
            if thing==1:
                wpn=self.create_weapon()
                print(f"Вам выпало оружие {wpn[0]}, {wpn[1]}")
                time.sleep(2)
            elif thing==2:
                arm=self.create_armor()
                print(f"Вам выпала броня {arm[0]}, {arm[1]} ")
                time.sleep(2)
            elif thing==3:
                food=self.create_food()
                print(f"Вам выпала еда {food}")
                time.sleep(2)
            else:
                print("Вам ничего не выпало")
                time.sleep(2)
            self.skill=random.choice(powers)
            print(f"У вас есть способность {self.skill} ")
            time.sleep(2)
            self.skill=random.choice(powers)
            print(f"Теперь у вас есть способность {self.skill}")
            return False
        else:
            print(f"Жертва жива hp= {enemy.hp}, dmg= {enemy.dmg}")
            return True
    def lvl_up(self, max_ex):
        self.exp-=max_ex
        self.lvl+=1
        self.dmg+=self.lvl*15
        self.hp+=self.lvl*20
        print(f"Уровень повышен {self.lvl}")
    def create_weapon(self):
        wpn_type=listg[random.randint(0,2)]
        wpn_rare=random.choice(list(dict.keys()))
        if wpn_type==listg[0]:
            self.dmg+=10*wpn_rare
        elif wpn_type==listg[1]:
            self.dmg+=20*wpn_rare
        elif wpn_type==listg[2]:
            self.dmg+=40*wpn_rare
        elif wpn_type==listg[3]:
            self.dmg+=70*wpn_rare
        return wpn_type, dict[wpn_rare]
    def create_armor(self):
        armor_type=lista[random.randint(0,2)]
        armor_rare = random.choice(list(dict.keys()))
        if armor_type==lista[0]:
            self.hp+=10*armor_rare
        elif armor_type==lista[1]:
            self.hp+=20*armor_rare
        elif armor_type==lista[2]:
            self.hp+=40*armor_rare
        elif armor_type==lista[3]:
            self.hp+=70*armor_rare
        return armor_type, dict1[armor_rare]
    def create_food(self):
        food_rare = random.choice(list(food1.keys()))
        self.hp+=food_rare
        return food1[food_rare]
class Enemy:
    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg
    def create_enemy():
        rnd_name=random.choice(enem)
        rnd_hp=random.randint(200,300)
        rnd_damage=random.randint(200,300)
        return Enemy(rnd_name, rnd_hp, rnd_damage)
    def attack(self, victim):
        victim.hp-=self.dmg
        if victim.hp<=0:
            print("Вы проиграли")
            quit()
        else:
            print(f"{victim.name}, hp={victim.hp}")
def choise():
    ask=input(f"Хотите ли вы сражаться с {enemy.name}? ")
    if ask=="Да":
        rezult=hero.attack(enemy)
        choise()
        if rezult==True:
            enemy.attack(hero)
            choise()
    elif ask=="Нет":
        print("Вы решили выйти")
        quit()
    else:
        print("Неверное слово")
        choise()
def create_ability(self):
    if hero.skill=="ice":
        print("Вы заморозили монстра")
        hero.dmg+= 25
        time.sleep(1)
    elif hero.skill=="poison":
        print("Вы отравили монстра!")
        hero.dmg+=80
        time.sleep(1)
    elif hero.skill=="heal":
        print("Вам прибавилось здоровье")
        hero.hp+=50
        time.sleep(1)
    elif hero.skill=="fire":
        print("Вы подожгли врага")
        hero.hp+=30
        time.sleep(1)
race=["elf","gnom","hobbit","trols"]
prof=["magician","warrior","archer"]
enem=["ghost", "dracula", "joker", "trol"]
listg=["poké ball", "bomb", "awp", "glock"]
lista=["щит", "шлем", "нагрудник", "бронированный костюм"]
powers=["ice", "poison", "heal", "fire"]
food1={10:"mana", 25:"medical", 40:"fruits", 65:"vegetables"}
name=input("Введите имя ")
race1=input(f"Какая ваша раса? {race} ").lower()
prof1=input(f"Какая ваша профессия? {prof} ").lower()
dict={1:"обычное", 10:"эпическое", 30:"мифическая", 50:"легендарная"}
dict1={1:"редкая", 10:"эпическая", 30:"мифическая", 50:"легендарная"}
hero=Player.create_player(name, race1, prof1)
print(hero.name, hero.hp, hero.dmg)
while True:
    event=random.randint(1,2)
    if event==1:
        print("Никто не пришёл")
        time.sleep(3)
    elif event==2:
        enemy=Enemy.create_enemy()
        print(f"Вы встретили {enemy.name}")
        time.sleep(2)
        print(f"Здоровье врага {enemy.hp}, Урон врага {enemy.dmg}")
        time.sleep(2)
        print(f" Ваше здоровье {hero.hp}, Ваш урон {hero.dmg}")
        time.sleep(2)
        print(f" Твой experience {hero.exp}, твой lvl {hero.lvl}")
        choise()