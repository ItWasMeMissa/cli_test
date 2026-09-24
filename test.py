import cli, pytest


#case -- python cli.py --name Bob
def test_only_one_argument(capsys):
    with pytest.raises(SystemExit):
        cli.main(['--name', 'Bob'])


#case -- python cli.py --name Bob --age 25
def test_two_right_arguments(capsys):
    cli.main(['--name', 'Bob', '--age', '25' ])

    assert capsys.readouterr().out == 'You are 25 years old\n'


#case -- python cli.py --name Bob --age 25 --verbose
def test_verbose(capsys):
    cli.main(['--name', 'Bob', '--age', '25', '--verbose'])

    assert capsys.readouterr().out == ('Hello, Bob\n'
                                       'You are 25 years old\n')


#case -- python cli.py
def test_no_arguments():
    with pytest.raises(SystemExit):
        cli.main()
