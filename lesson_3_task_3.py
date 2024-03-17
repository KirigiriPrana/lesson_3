from address import Address
from mailing  import Mailing

sending = Mailing
sending (sending.komu, sending.otkuda, 1200, 1234567890)

sending.komu = 236040, "г. Москва", "ул. Невская", 25, 15
sending.otkuda = 236404,"г. Калиниград", "ул. Черняховского", 43, 12

print("Отправление",sending.track, "из" , sending.otkuda,
      "в", sending.komu,". Стоимость", sending.cost, "рублей.")

