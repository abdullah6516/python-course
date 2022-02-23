user = 'ahmad'

print( f'hello {user}') #general form f'what i want to say: [mark] {variable1,variable2,....:,}' you can use """ or '''

price= 14.99

quantity = 10

print(f"total: ${price * quantity:,}") 

print(f"total: ${price * quantity:,.2f}") #for decimals we add ,.Nf

percent = .15

print(f"percentage: {percent:.2%}") #for percentage we add 

user1 = "ahmad"
user2 = "ibrahim"
user3 = "alaa"
output =f"{user1} \n{user2} \n {user3}"
print(output)
output =f"{user1:>20} \n{user2:>20} \n{user3:>20}"
print(output)


