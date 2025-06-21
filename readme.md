# 🌾 Crested Verses

**Crested Verses** is a Flask-powered web application that generates daily poetic reflections based on news in Uganda. By blending language models and curated local content, Crested Verses turns current events into thoughtful verse, bringing a soulful dimension to the day's headlines.

---

## 📜 Features

- 📰 **News-Inspired Poetry**: Automatically generates a poem each day based on Uganda’s latest news.
- 📅 **One Poem Per Day**: Fetches or generates a poem for the current date.
- ⚡ **AI-Powered Content**: Uses AI to craft original, meaningful poems.
- 🔁 **Automatic Generation**: If no poem exists for today, it creates one on demand.
- 📦 **RESTful API**: Exposes a clean API endpoint for frontend or mobile apps.

---

## 🚀 API Endpoint

### `GET /api/poems`

- **Description**: Fetches the poem for the current day. If not already created, it triggers the generation process.

- **Response**:
```json
{
  "status": "Success",
  "message": "Successfully loaded todays poems",
  "data": {
    "title": "...",
    "content": "...",
    "date": "YYYY-MM-DD"
  },
  "status_code": 200
}
