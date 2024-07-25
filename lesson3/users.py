class User :
    def __init__ ( self , name , surname ):
        self.username = name
        self.Surname = surname
        self.family = name + surname

    def pName ( self ) :
        print ( " Имя: ", self.username )
 
    def pSurname ( self ) :
        print ( ' Фамилия : ' , self.Surname )
        
    def pFamily ( self ) :
       print ( " Имя и фамилия : " , self.family )