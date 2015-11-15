from .make_coffee_service import MakeCoffeeService


def main():
    mcs = MakeCoffeeService()
    mcs.get_cup()


if __name__ == "__main__":
    main()