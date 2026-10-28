
class Logger:
    def __enter__(self):
        print("Start sekcji logowania")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Koniec sekcji logowania")


class FileWriter:
    def __init__(self,file_path):
        self._file_path = file_path
        self._file_handle = None

    def __enter__(self):
        self._file_handle = open(self._file_path, "w")
        return self._file_handle

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self._file_handle:
            self._file_handle.close()

        if exc_val is not None:
            print(f"Błąd podczas zapisu: {exc_val}")

        return False


class SafeDivision:

    def divide(self, a, b):
        return a/b

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is ZeroDivisionError:
            print("Nie można dzielić przez zero")
            return True
        else:
            return False


def main():
    with Logger():
        print("Hello from zadanie2!")

    with SafeDivision() as div:
        print(div.divide(6,3))
        print(div.divide(6,0))

    with FileWriter("test.txt") as file:
        file.write("test text !")
        raise FileNotFoundError("My error")


if __name__ == "__main__":
    main()
