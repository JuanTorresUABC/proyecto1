import random
print('Bienvenido a jugar piedra, papel o tijeras\n')
def play():
    user = input("Elige una opcion para combatir: 'r' para Roca, 'p' para Papel, 't' para Tijeras\n")
    user = user.lower()

    computer = random.choice(['r','p','t'])

    if user == computer:
        return "Tu y la computadora tienen la misma opcion {}. Es un empate".format(computer)

    # r > t, t > p, p > r
    if is_win(user, computer):
        return "Elegiste {} y la computadora eligio {}. Lo destruiste!".format(user,computer)

    return "Elegiste {} y la computadora eligio {}. Te destruyeron :(".format(user,computer)
def is_win(player, opponent):
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

if __name__ == '__main__':
    print(play())