x = input('please input first number: ')
y = input('please input second number: ')
sum = int(x) + int(y)
print(sum)


#or
#Mặc định, số thực (float) trong Python chỉ có độ chính xác với tối đa 15 chữ số ở phần thập phân. Chúng ta có thể sử dụng module decimal được cài đặt sẵn trong Python để xác định độ chính xác là bao nhiêu số thập phân

#sum = decimal.Decimal(x) + decimal.Decimal(y)

#Để kiểm soát độ chính xác phần thập phân có bao nhiêu chữ số, chúng ta có thể sử dụng hàm getcontext() với thuộc tính prec. Ví dụ:
#decimal.getcontext().prec = 10

#---> full code
import decimal

x = input('please input first number: ')
y = input('please input second number: ')
decimal.getcontext().prec = 6
sum = decimal.Decimal(x) + decimal.Decimal(y)


#--->result we get 5 number after a decimal point, 1 before a decimal point, totally is 6
