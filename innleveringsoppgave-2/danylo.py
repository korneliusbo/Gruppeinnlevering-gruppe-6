class Project:
    def __init__(self, tid=3, lagånd=3):
        self.__tid = tid
        self.__lagånd = lagånd

    def print_options(self, options):
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

    def handle_scenario(self, name, options, effects):
        print(f"\n{name}")
        self.print_options(options)

        while True:
            choice = input(f"Skriv nummeret på ditt valg (1-{len(options)}): ")

            if not choice.isdigit():
                print("Ugyldig input! Vennligst skriv et tall.")
                continue

            choice_num = int(choice)

            if not (1 <= choice_num <= len(options)):
                print(f"Ugyldig valg! Skriv et tall mellom 1 og {len(options)}.")
                continue

            print(f"Du valgte: {options[choice_num - 1]}")

            if choice_num in effects:
                effect = effects[choice_num]
                self.__tid += effect.get("tiden", 0)
                self.__lagånd += effect.get("lagånd", 0)

            print(f"Tid: {self.__tid}, Lagånd: {self.__lagånd}")
            break

    def check_status(self):
        if self.__tid < 0:
            print("Prosjektplanleggingen har mislyktes: ikke nok tid igjen.")
        elif self.__lagånd < 0:
            print("Prosjektplanleggingen har mislyktes: lagånden har falt under null.")
        else:
            print("Prosjektplanleggingen var vellykket og fullført!")


project = Project()

project.handle_scenario(
    "Silje vs Sivert",
    ["Plenum", "Individuell", "Samtale", "HR"],
    {
        1: {"tiden": -2, "lagånd": 1},
        2: {"tiden": 1, "lagånd": -1},
        3: {"tiden": -1, "lagånd": 2},
        4: {"tiden": -3, "lagånd": -2},
    },
)

project.handle_scenario(
    "Hamdi vs Jabir",
    ["La dem være", "Velg Hamdi", "Velg Jabir"],
    {
        1: {"tiden": 0, "lagånd": -2},
        2: {"tiden": -1, "lagånd": 0},
        3: {"tiden": -1, "lagånd": 0},
    },
)

project.handle_scenario(
    "Team motivasjon",
    ["Hold en fin tale", "Styr prosjektet med jernhånd", "Pizza-party"],
    {
        1: {"tiden": -1, "lagånd": 2},
        2: {"tiden": -1, "lagånd": -1},
        3: {"tiden": -2, "lagånd": 3},
    },
)

project.check_status()
