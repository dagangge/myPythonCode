import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md

master=mt.TcpMaster("127.0.0.1",6001,5.0)

# hold_value=master.execute(slave=1,function_code=md.READ_HOLDING_REGISTERS,starting_address=1,quantity_of_x=5,output_value=5)
# print(hold_value)

coils_value=master.execute(slave=1,function_code=md.READ_COILS,starting_address=1,quantity_of_x=5,output_value=0)
print(coils_value)