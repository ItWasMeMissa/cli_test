import argparse


def main(args=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--age', type=int, required=True)
    parser.add_argument('--verbose', action='store_true')

    args = parser.parse_args(args)

    if args.verbose:
        print("Hello,", args.name)

    print("You are", args.age, "years old")
    if args.age in range(1, 3):
        print("You are newborn")
    if args.age in range(3, 6):
        print("You are preschooler")
    ...

if __name__ == '__main__':
    main()