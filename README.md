# Affinity MCP Server

MCP Server for Affinity CRM (www.affinity.co) - enables AI assistants to access deal flow, relationship data, and investment insights through the Model Context Protocol.

## 🎯 Intended Use

This server is designed for **authorized business integration** of Affinity CRM data. Please ensure you have proper permissions and follow [responsible use guidelines](GUIDELINES.md).

## Quick Start

### 1. Install UV

Install UV Python package manager (recommended over pip for simpler dependency management)

### 2. Set up Environment

Create a `.env` file with your Affinity API key:

```bash
AFFINITY_API_KEY=your_api_key_here
```

### 3. Test the Server (using MCP Inspector)

```bash
mcp dev main.py
```

### 4. Add to Claude Desktop

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

## Available Tools

- `get_lists` - Get metadata on all Lists
- `get_companies` - Get all Companies (requires "Export All Organizations directory" permission)
- `get_company_fields` - Get Company Fields metadata
- `get_persons` - Get all Persons (requires "Export All People directory" permission)
- `get_person_fields` - Get Person Fields metadata

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

## License & Guidelines

MIT License - See [LICENSE](LICENSE) for details  
Responsible Use - See [GUIDELINES.md](GUIDELINES.md) for best practices
