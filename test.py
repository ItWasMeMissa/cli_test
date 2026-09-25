import cli, pytest

#case python cli.py
def test_convertor():
    with pytest.raises(SystemExit):
        cli.main()


#case python cli.py --value 100 --from km --to miles
def test_convertor_with_args(capsys):
    cli.main([
        '--value', '100',
        '--from', 'km',
        '--to', 'miles'
    ])

    assert capsys.readouterr().out == (
        '100 km = 62.14 miles\n'
    )


#case python cli.py --value 100 --from km --to miles --verbose
def test_convertor_verbose(capsys):
    cli.main([
        '--value', '100',
        '--from', 'km',
        '--to', 'miles',
        '--verbose'
    ])

    assert capsys.readouterr().out == (
        'Converting 100 km to miles\n'
        'Resalt 62.14 miles\n'
    )


#case python cli.py --value 100 --from banana --to miles
def test_unknown_unit(capsys):
    with pytest.raises(SystemExit):
        cli.main([
            '--value', '100',
            '--from', 'banana',
            '--to', 'miles'
        ])

    assert capsys.readouterr().out == (
        'Unknown unit\n'
    )

def test_unavailable_conversion(capsys):
    with pytest.raises(SystemExit):
        cli.main([
            '--value', '100',
            '--from', 'm',
            '--to', 'miles',
        ])

    assert capsys.readouterr().out == (
        'Unavailable conversion\n'
    )