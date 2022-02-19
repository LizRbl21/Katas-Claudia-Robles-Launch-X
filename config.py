"""def main():
    try:
        configuration = open('D:\CERO\Archivos Ely\Archivos LAUNCH-X\config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")
"""
def main():
    try:
        open("D:\CERO\Archivos Ely\Archivos LAUNCH-X\config.txt")
    except OSError as err:
        if err.errno == 2:#Para error FileNotFoundError
            print("Couldn't find the config.txt file!")
        elif err.errno == 13:#Para error IsADirectoryError
            print("Found config.txt but couldn't read it")



if __name__ == '__main__':
    main()