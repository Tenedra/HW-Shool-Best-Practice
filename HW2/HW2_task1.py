Message = input()
Message_length = len(Message) 
cost_R = Message_length*23//100 #подсчет рублей
cost_K = Message_length*23%100 #подчет копеек
print(cost_R,"р.",cost_K,"коп.")