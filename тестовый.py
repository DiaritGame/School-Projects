animals = {'тигр': 'ррррррррррррррррр!',
    'корова': 'муууууууууууу!',
    'дельфин': 'ррр ииииуууу! ррр ииииуууу!'}

while True:
    available_animals = ', '.join(animals.keys())
    choice = input(f"Какое животное аы бы хотели услышать: {available_animals} или хотите придумать своё животное? (ведите название или 'придумать'): ")

    if choice == 'придумать':
        name = input("Как будет звать ваше новое животное? ")
        sound = input(f"Какой звук издаёт {name}? ")
        animals[name] = sound
        print("Животное создано!\n")
    elif choice in animals:
        print(f"{animals[choice]}\n")
    else:
        print("Такое животное не найдено. Попробуйте ещё раз.\n")
