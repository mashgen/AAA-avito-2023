def user_input(options):
    option = ""
    while option not in options:
        print("Выберите: {}/{}".format(*options))
        option = input()
    return option


def step2_umbrella():
    print("На улице идет дождь?")
    options = {"да": True, "нет": False}
    option = user_input(options)
    if options[option]:
        print("Уточке повезло! Она дойдет до бара под зонтиком.")
        return
    print(
        "Хорошо, что зонт защищает ещё и от солнца! "
        "Теперь главное не забыть его в баре."
    )
    return


def step2_no_umbrella():
    print("На улице идет дождь?")
    options = {"да": True, "нет": False}
    option = user_input(options)
    if options[option]:
        print(
            "Хорошо, что уточке ей не нужен! "
            "Уткам не страшен дождь, они ведь умеют плавать."
        )
        return
    print("Отлично, и погода хорошая, и зонт нести не надо!")
    return


def step1():
    print("Утка-маляр 🦆 решила выпить зайти в бар. " "Взять ей зонтик? ☂️")
    options = {"да": True, "нет": False}
    option = user_input(options)
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == "__main__":
    step1()
