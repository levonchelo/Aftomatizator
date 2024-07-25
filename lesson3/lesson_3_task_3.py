from address import Address
from mailing import Mailing

to_address = Address
from_address = Address
to_address = 364040, "г. Братск", "ул. Некрасова", 25, 1
from_address = 285204, "г. Иркутск", "ул. Ленина", 58, 2

sending = Mailing
sending(to_address, from_address, 5000, 1234567890)

print(
    "Отправление",
    sending.track,
    "из",
    from_address,
    "в",
    to_address,
    ". Стоимость",
    sending.cost,
    "рублей.",
)