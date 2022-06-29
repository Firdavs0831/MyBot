from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

tugmalar = ["🧑🏻‍💻Abdurahmonov Firdavs","Turdimatov Muhammadqodir","Zohidov Samandar","Toshpo'latov Asadbek","Jumaboyev Muhammadnosir","Ahmadaliyev Shuhrat","Ahmedov Aziz","Mirzatillayev Izzatillo","Hamidov Sardor",
"Rasulov Izzat","Ahmadaliyev Ramzbek","Muhtorov Doston","Abduvahobov Mirzohid","Jaloliddinov Egamberdi","Yigitaliyev Dior","Isoqov Otabek","Majidov Muhammadali","Hazratqulov Nuriddin","Samijonov Shoxruh","/qaytish"]
button= ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,input_field_placeholder="2001-yillar")
for i in tugmalar:
    button.insert(i)
