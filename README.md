# Hausarbeit Programmieren mit Python

## How to use requirements.txt file?

```console
pip install -r requirements.txt
```

## How to run the script?

### Default script

```console
python main.py
```

### With optional export

```console
python main.py --export
```

### With additional backup

```console
python main.py --backup
```

### Backup and export combined

```console
python main.py --export --backup
```

## How to run unit tests?

```console
python -m unittest discover -s .\tests\ -p '*Test.py'
```