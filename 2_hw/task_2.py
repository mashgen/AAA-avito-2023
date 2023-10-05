def menu():
    """ Print the available menu commands to the screen"""
    print(
        "В меню есть следующие команды:\n"
        "1: Вывести в понятном виде иерархию команд, "
        "т.е. департамент и все команды, которые входят в него\n"
        "2: Вывести сводный отчёт по департаментам: название, численность, "
        '"вилка" зарплат в виде мин – макс, среднюю зарплату\n'
        "3: Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. "
        "При этом необязательно вызывать сначала команду из п.2\n"
        "menu: Вывести какие существуют команды в меню\n"
        "exit: Завершение программы\n"
    )


def read_from_csv():
    """Reading all lines from a file
    Return list[str] of lines
    """
    with open("./Corp_Summary.csv", "r", encoding="utf-8") as f:
        all_info = f.readlines()
    f.closed
    return all_info


def department_info(corp_info):
    """Collecting information from a file about departments
    in the form of a dict.
    Return dict, where
    keys is departaments,
    values is dict, where keys are teams, count, min, max, sum, mean
    """
    dep_dict = {}
    for lines in corp_info:
        # Срез убирает символ \n в конце каждой строки
        line = lines[:-1].split(sep=";")
        # Заголовок файла, узнаем индексы нужных столбцов
        if "Департамент" in line:
            ind_dep = line.index("Департамент")
            ind_team = line.index("Отдел")
            ind_salary = line.index("Оклад")
        else:
            # Основная информация из файла
            deparment = line[ind_dep]
            salary = int(line[ind_salary])
            team = line[ind_team]
            if deparment in dep_dict.keys():
                info = dep_dict.get(deparment)
                teams = info.get("teams")
                if team not in teams:
                    teams = teams + ", " + team
                count_ = info.get("count") + 1
                max_ = max(info.get("max"), salary)
                min_ = min(info.get("min"), salary)
                sum_ = info.get("sum") + salary
                info.update(
                    {
                        "teams": teams,
                        "count": count_,
                        "max": max_,
                        "min": min_,
                        "sum": sum_,
                    }
                )
                dep_dict.update({deparment: info})
            else:
                dep_dict.update(
                    {
                        deparment: {
                            "teams": team,
                            "count": 1,
                            "max": salary,
                            "min": salary,
                            "sum": salary,
                        }
                    }
                )
    for key, value in dep_dict.items():
        count_ = value.get("count")
        sum_ = value.get("sum")
        mean_ = round(sum_ / count_, 2)
        value.setdefault("mean", mean_)
        dep_dict.update({key: value})
    return dep_dict


def hierarchy(report_info):
    """Function from the first menu item
    that prints departments and teams in them from dict
    """
    for key, value in report_info.items():
        team = value.get("teams")
        print("{0}: {1}".format(key, team))


def consolidated_report_print(report_info):
    """Function from the second menu item
    that prints report about depataments from dict
    """
    print(
        "Департамент: Численность  Мин. зарплата" "  Макс. зарплата  Средняя зарплата"
    )
    for key, value in report_info.items():
        count_ = value.get("count")
        max_ = value.get("max")
        min_ = value.get("min")
        mean_ = value.get("mean")
        print(f"{key:<11} {count_:^14} {min_:^15} {max_:^15} {mean_:^17}")


def consolidated_report_to_save_csv(report_info):
    """Function from the third menu item
    that saves report about depataments from dict in csv
    """
    with open("./cons_report.csv", "w+", encoding="utf-8") as f:
        f.write(
            "Департамент;Численность;Мин.зарплата;" "Макс.зарплата;Средняя зарплата\n"
        )
        for key, value in report_info.items():
            count_ = value.get("count")
            max_ = value.get("max")
            min_ = value.get("min")
            mean_ = value.get("mean")
            f.write(f"{key};{count_};{min_};{max_};{mean_}\n")
    f.closed


def main():
    """The main function in which the file is read,
    a dictionary is built on it
    and work is going on with the user
    who enters commands from the menu
    """
    inputs = ["1", "2", "3", "menu", "exit"]
    user_input = "start"
    corp_info = read_from_csv()
    dep_info = department_info(corp_info)
    while user_input != "exit":
        if user_input == "start":
            menu()
        user_input = ""
        while user_input not in inputs:
            print("Введите одну из команд: ", end="")
            print(*inputs, sep=", ")
            user_input = input()
        if user_input == "1":
            hierarchy(dep_info)
        elif user_input == "2":
            consolidated_report_print(dep_info)
        elif user_input == "3":
            consolidated_report_to_save_csv(dep_info)
        elif user_input == "menu":
            menu()
        else:
            break


if __name__ == "__main__":
    main()
