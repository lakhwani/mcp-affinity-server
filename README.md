# Affinity MCP Server

MCP Server for Affinity (www.affinity.co)

## Quick Start

### 1. Install UV

Install UV Python package manager (recommended over pip for simpler dependency management)

### 2. Test the Server (using MCP Inspector)

```bash
mcp dev main.py
```

### 3. Add to Claude Desktop

```bash
mcp install main.py
```

To verify, go to: **File → Settings → Developer → Edit Config**
Check MCP server configuration to `claude_desktop_config.json`

## Setup (First Time Only)

### 1. Install UV

Install UV Python package manager (recommended over pip for simpler dependency management)

### 2. Create MCP Server

```bash
uv init .
uv add "mcp[cli]"
mcp install main.py
```

## Troubleshooting

**Server not appearing after config change:**

- Close Claude Desktop completely via Task Manager
- Wait a few seconds, then reopen

**Server still not working:**

- Find UV path: `which uv` (Mac/Linux) or `where uv.exe` (Windows)
- Use absolute path in config (typically `C:\Users\User\.local\bin\uv.exe` on Windows)
- Use `\\` for Windows paths in JSON config

**In error logs, with TLS error**

- Add to Claude config the following flag: "--native-tls" into the top of args.
