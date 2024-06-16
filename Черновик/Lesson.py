age ="17"
if (age>="18"):
    print('ok')
else:
    print('no')

rate_numb = input("оцените работу оператора от 1 до 5:")
rate = int(rate_numb)
if (rate<1):
    rate = 1
if (rate>5):
    rate = 5
print(rate)

feedback=""
if rate ==1:
    feedback = input("Расскажите что вам не понравилось:")
elif rate == 4 and 5:
     feedback = input("Спасибо за оценку!, оставьте отзыв:")
else:
        if rate == 2:
             feedback = input("Расскажите что вас смутило:")
        else:
             if rate == 3:
                  feedback = input("Расскажите как повысить качество:")


print(feedback)

#for x in range(1,10):
 #   print("X=",x,"x*x",x*x)

students = ["Алексей","Полина","Маша","Игорь","Олег","Popa","Lev"]
for x in range(0,len(students)):
 #   print(students[x])
#user_log ="fafa"
#user_pas ="popo"
#log=input("Login:")
#pas=input("Password:")
#if (log==user_log) and (pas==user_pas):
#    print("Доступ разрешён")
#else:
#    print("Доступ запрещён")

crit1 = "red"
crit2 = "lock"
Color=input("color:")
Feture=input("Feture:")
if (Color==crit1) or (Feture==crit2):
    print("Buy it!")
else:
    print("Ssory:(")

# ИСПРАВИТЬ ОШИБКИ
X = 5000 #Вклад
Y = ( 7 ) #На сколько лет
#P = ( 1 , Y + 1 )
M = ( 0.1 * X )# 
D = ( X + M )
X = 5000 + D
# P = D + X
#while n < Y :
#    n = n + 1
for bank in range  ( Y ) :
    print ( X )