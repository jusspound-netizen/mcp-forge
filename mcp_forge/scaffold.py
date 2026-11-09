import pathlib

PYPROJECT_TEMPLATE = """[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{package_name}"
version = "0.1.0"
description = "An MCP server for {server_name}."
readme = "README.md"
requires-python = ">=3.9"
dependencies = ["mcp>=2.0.0"]

[project.scripts]
{server_name} = "server:main"
"""

SERVER_JSON_TEMPLATE = """{{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.github.{github_user}/{server_name}",
  "description": "An MCP server for {server_name}.",
  "version": "0.1.0",
  "packages": [
    {{
      "registryType": "pypi",
      "identifier": "{package_name}",
      "version": "0.1.0",
      "transport": {{ "type": "stdio" }}
    }}
  ]
}}
"""

def scaffold(target_dir: pathlib.Path, package_name: str, server_name: str, github_user: str):
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "pyproject.toml").write_text(
        PYPROJECT_TEMPLATE.format(package_name=package_name, server_name=server_name),
        encoding="utf-8"
    )
    (target_dir / "server.json").write_text(
        SERVER_JSON_TEMPLATE.format(package_name=package_name, server_name=server_name, github_user=github_user),
        encoding="utf-8"
    )
    print(f"Scaffolded pyproject.toml and server.json in {target_dir}")
