# file-search-cli

> A command-line tool for searching files on IRCHighway's `#ebooks`

[![Version](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/release/python-3130/)

## Installation
1. Install python
2. Create virtual environment
```
python -m venv .venv
```
3. Activate virtual environment
```
source .venv/bin/activate
```
4. Install requirements
```
pip install -r requirements.txt
```
## Usage

```
python main.py [options]
```

### Basic Examples

```bash
# Basic usage
python main.py --help

# Search with author
python main.py --author "Stephen King"

# Search with title
python main.py --title "Piranesi"

# Search with author and title
python main.py --title "Piranesi" --author "Susanna Clarke"

# Search with retail flag
python main.py --title "Piranesi" --author "Susanna Clarke" -r
```

## Options

- `-t, --title <title>` - Title to search for
- `-a, --author <author>` - Author to search for
- `-r, --retail` - Only searches for retail books

### Configuration File

Add your source `txt` files to `sources` folder