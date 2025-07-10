# file-search-cli

> A command-line tool for searching files on IRCHighway's `#ebooks`

[![Version](https://img.shields.io/npm/v/file-search-cli.svg)](https://npmjs.org/package/file-search-cli)
[![License](https://img.shields.io/npm/l/file-search-cli.svg)](https://github.com/username/file-search-cli/blob/main/LICENSE)

## Description

Brief description of what your CLI tool does and why it's useful.

## Features

- 🔍 Search sources

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
```