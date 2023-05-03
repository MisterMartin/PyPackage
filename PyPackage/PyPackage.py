import AnotherModule as an

class PyPackage:
    def __init__(self):
        print(f'Welcome to {__file__}')
        print(f'We are also accessing {an.AnotherModule().myName()}')

def main():
    pp = PyPackage()

if __name__ == '__main__':
    pp = PyPackage()
