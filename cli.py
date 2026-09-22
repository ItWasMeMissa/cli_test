import sys, math

def main():
    match sys.argv[1]:
        case 'add':
            nums = [int(x) for x in sys.argv[2:]]
            print(sum(nums))

        case 'multiply':
            nums = [int(x) for x in sys.argv[2:]]
            print(math.prod(nums))

        case 'hello':
            print('Bob')

        case _:
            print('Unknown command')

if __name__ == '__main__':
    main()