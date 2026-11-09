import cyclopts
from rich.console import Console
from rich.panel import Panel
from mcp_forge.checker import check_pypi_name
from mcp_forge.scaffold import scaffold
import pathlib

app = cyclopts.App(help="MCP Forge: Package and publish your MCP server.")
console = Console()

@app.command
def check(name: str):
    """Check if a package name is available on PyPI."""
    available = check_pypi_name(name)
    if available:
        console.print(f"[green]✓ '{name}' is available on PyPI.[/green]")
    else:
        console.print(f"[red]✗ '{name}' is taken or unreachable. Pick a different name.[/red]")

@app.command
def init(package_name: str, server_name: str, github_user: str, output: str = "."):
    """Scaffold pyproject.toml and server.json for an MCP server."""
    if not check_pypi_name(package_name):
        console.print(f"[yellow]Warning: '{package_name}' may already be taken on PyPI.[/yellow]")
    scaffold(pathlib.Path(output), package_name, server_name, github_user)
    console.print(Panel.fit(
        "[bold]Next steps:[/bold]\n"
        "1. python -m build\n"
        "2. twine check dist/*\n"
        f"3. twine upload dist/*\n"
        f"4. mcp-publisher publish server.json",
        title="Publish Checklist"
    ))
