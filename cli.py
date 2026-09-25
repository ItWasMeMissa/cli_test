import argparse

conversions = {
    'km': {
        'miles': 0.621371,
        'm': 1000,
    },
    'miles': {
        'km': 1.60934,
    },
    'm': {
        'km': 0.001,
    },
}
def main(args=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--value',required=True )
    parser.add_argument('--from', dest='from_unit', required=True)
    parser.add_argument('--to', dest='to_unit', required=True)
    parser.add_argument('--verbose',action='store_true')

    args = parser.parse_args(args)

    if (args.from_unit not in conversions or
            args.to_unit not in conversions):
        print('Unknown unit')
        raise SystemExit

    if args.to_unit not in conversions[args.from_unit]:
        print('Unavailable conversion')
        raise SystemExit

    factor = conversions[args.from_unit][args.to_unit]
    resalt = round(float(args.value) * factor, 2)

    if args.verbose:
        print(f'Converting {args.value} {args.from_unit} to {args.to_unit}\n'
              f'Resalt {resalt} {args.to_unit}')
    else:
        print(f'{args.value} {args.from_unit} = {resalt} {args.to_unit}')


if __name__ == '__main__':
    main()