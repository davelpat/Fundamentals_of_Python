import os


def displayFiles(pathname):
    if os.path.isdir(pathname) == True:
        os.chdir(pathname)
        dir_list = os.listdir(os.getcwd())
        for element in dir_list:
            displayFiles(element)
    elif os.path.isfile(pathname) == True:
        fid = open(pathname, 'r')
        print(pathname)
        print(fid.read())
    else:
        print("I don't know what this is:", pathname)


def main():
    pathanme = input("Enter a pathname: ")
    displayFiles(pathanme)


if __name__ == '__main__':
    main()
