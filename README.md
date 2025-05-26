# Affinity MCP Server

- MCP Server for Affinity (www.affinity.co)

## Set up

1. Install UV (Python package manager) - not recommended to use Pip or Pypi due to higher complexity
2.

# Initial MCP set up

1. uv init . (set up inside your current directory)
2. uv add "mcp [cli]" (will add .venv)
3. mcp install main.py (containing mcp server code)
4. (optional) mcp dev main.py (uses MCP Inspector to test)
5. On Claude, File -> Settings -> Developer -> Edit Config (claude_desktop_config) to check if MCP server is found

# Common errors

1. After adding MCP servers in config, may not show up immediately. End the Claude Desktop task from the Task Manager and then reopen after few seconds.
2. If still not working, put absolute path for where uv is installed, by running "which uv", "where uv", "where uv.exe", find the default installation location is in C:\Users\User\.local\bin if installed with Powershell. Use \\ when setting up in the Claude Server "command" to \\uv.exe at the end.
