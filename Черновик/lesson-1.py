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