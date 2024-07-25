class Card:
    number = '87245464687694'
    vaidDate = '01/11'
    holder = 'unknown'

    def __init__ ( self, number , date , holder ) :
        self.number = number
        self.vaidDate = date
        self.holder = holder

    def pay ( self, amout ) :
        print ("с карты", self.number , "списали", amout)

