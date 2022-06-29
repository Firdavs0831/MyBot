from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5577230075:AAFmWJeHTJk6UTvXkedNvMuM0lt9436-pGU"  # Bot toekn
ADMINS = [876709435]  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
