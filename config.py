import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8288797778:AAF1f0Pq9kwMNk_V_LSJI-yRRGd8N1sZtYo")

# Channel and link configuration
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/pokemon13channel")
FREE_SPIN_URL = os.getenv("FREE_SPIN_URL", "https://pkm9aus.com/RFPOKEMON9BOT")
FREE_CREDIT_URL = os.getenv("FREE_CREDIT_URL", "https://pkm9aus.com/RFPOKEMON9BOT")

# Promotional images (local file paths - hardcoded in code)
FREE_SPIN_IMAGE_PATH = "public/free_spin.jpg"
HOT_GAME_TIPS_IMAGE_PATH = "public/hot_game_tips.jpg"

# Bot information
BOT_NAME = "Pokemon9 Promo Bot"
BOT_DESCRIPTION = "Pokemon9 Marketing Assistant - Provides latest promotions and event information"
