from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = "5451686640:AAEt545Vy-ER_7krmVA5_yqSZ35OnwHSnhE"  # Bot toekn
ADMINS = [876709435]  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
