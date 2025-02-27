# Webex API Integration

## 📌 Project Overview
This project provides a structured and clean integration with the Webex API, allowing users to create, manage, and retrieve details for rooms and teams asynchronously using `aiohttp`.

## 🚀 Features
- **Create Webex Rooms**: Easily create rooms with specified titles.
- **Retrieve Room Details**: Fetch details of a specific room by providing the `roomId`.
- **Create Teams**: Manage teams by creating new teams dynamically.
- **Delete Teams**: Remove teams using their `teamId`.
- **Add Team Members**: Add users to specific teams by their email.

## 🛠️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/webex-api-integration.git
   cd webex-api-integration
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Webex API token:
   ```ini
   WEBEX_TOKEN=your_webex_api_token_here
   ```

## 🔧 Usage
Run the `run.py` file to interact with the Webex API:
```bash
python run.py
```

## 📂 API Endpoints
| Function | Description |
|----------|------------|
| `create_room(payload)` | Creates a Webex room. |
| `get_room()` | Retrieves all Webex rooms. |
| `create_team(payload)` | Creates a new team. |
| `delete_team(payload)` | Deletes a team. |

## ✅ Testing
Run tests using `pytest`:
```bash
pytest -v
```

