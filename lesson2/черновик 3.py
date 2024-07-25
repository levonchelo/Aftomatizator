from user import Users
from card import Card

user1 = Users('Alex')
user1.seyName()
user1.setAge(44)
user1.seyAge()


card = Card( "4356 8459 5885 5848", "02/64" , "Alex F" )
user1.addCard (card)
user1.getCard().pay(1000)


