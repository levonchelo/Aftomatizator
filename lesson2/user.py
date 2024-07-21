class Users:
    Age = 0
    def __init__(self, name):
        print ("i get home")
        self.username = name

    def seyName ( self ) :
        print ("я создался", self.username)
    
    def seyAge ( self ) :
        print ( self.Age )
    
    def setAge ( self, newAge ) :
        self.Age = newAge 
    
    def addCard(self, card):
        self.card = card
    
    def getCard ( self ):
        return self.card