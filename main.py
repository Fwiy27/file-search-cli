import os
import typer
from typing import Optional

def open_file(file_name: str, reqs: list[str]) -> list[str]:
    with open(file_name, 'r') as file:
        return [line for line in file.readlines() if line_contains_reqs(line, reqs)]
    
def line_contains_reqs(line: str, reqs: list[str]) -> bool:
    return all(req in line for req in reqs)

def get_valid_lines(reqs: list[str]) -> list[str]:
    valid_lines: list[str] = list()
    
    # Get all files in the sources directory
    sources_dir = './sources'
    source_files = [os.path.join(sources_dir, f) for f in os.listdir(sources_dir) if os.path.isfile(os.path.join(sources_dir, f))]
    
    for source in source_files:
        valid_lines.extend(open_file(source, reqs))
    
    return valid_lines

def main(
    author: Optional[str] = typer.Option(None, "-a", "--author", help="Filter by author name"),
    title: Optional[str] = typer.Option(None, "-t", "--title", help="Filter by title"),
    limit: Optional[int] = typer.Option(50, "-l", "--limit", help="Limit search entries"),
    retail: bool = typer.Option(False, "-r", "--retail", help="Filter for retail releases")
):
    # Build requirements list from provided flags
    reqs = []
    
    if author:
        reqs.append(author)
    
    if title:
        reqs.append(title)
    
    if retail:
        reqs.append('retail')
        
    # If no filters provided, show help
    if not reqs:
        typer.echo("Please provide at least one filter option.")
        raise typer.Exit(1)
    
    valid_lines = get_valid_lines(reqs)
    
    if limit:
        valid_lines = valid_lines[:limit]
    
    for line in valid_lines:
        print(line.strip())

if __name__ == '__main__':
    typer.run(main)