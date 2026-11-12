# MCP Forge
[![M8ven Verified](https://m8ven.ai/badge/mcp/jusspound-netizen-mcp-forge-1bzqgm?variant=verified)](https://m8ven.ai/mcp/jusspound-netizen-mcp-forge-1bzqgm)

Package and publish your MCP server to PyPI and the Official Registry in seconds.

MCP Forge is a CLI tool that takes the pain out of shipping a Python MCP server. It checks your package name for conflicts, scaffolds the required pyproject.toml and server.json, and gives you the exact commands to publish.

## Why use it?

Publishing an MCP server is a multi-step process:
1. Pick a PyPI package name that isn't taken.
2. Write a pyproject.toml with the right entry points.
3. Create a server.json that matches the Official Registry schema.
4. Run mcp-publisher login and mcp-publisher publish.

MCP Forge automates the boring parts and verifies the name before you waste time building.

## Installation

pip install mcp-forge-publisher

## Usage

Check if a name is available on PyPI:
mcp-forge check my-cool-server

Scaffold the config files:
mcp-forge init my-cool-server my_cool_server your-github-username --output ./my-server

This generates:
- pyproject.toml (with the correct entry point)
- server.json (with your GitHub namespace pre-filled)

## Publish

Follow the checklist printed by the CLI:
1. python -m build
2. twine check dist/*
3. twine upload dist/*
4. mcp-publisher publish server.json

## License
MIT
