## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/CipherX.git
cd CipherX
```

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the virtual environment

> **Important:** You must activate the virtual environment before installing dependencies or running CipherX.

#### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows (Command Prompt)

```cmd
.venv\Scripts\activate.bat
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
## ❓ Common Issues

### ModuleNotFoundError

If you see an error like:

```text
ModuleNotFoundError: No module named 'disnake'
```

it usually means the virtual environment is not activated.

Activate the virtual environment first, then run:

```bash
pip install -r requirements.txt
python main.py
```
## ⚙️ Configuration

Create a `.env` file:

```env
TOKEN=YOUR_DISCORD_BOT_TOKEN
```

Start the bot:

```bash
python main.py
```

> **Note:** If you receive an error such as `ModuleNotFoundError`, make sure the virtual environment is activated before running the bot.
Made with ❤️ by a Vietnamese developer.