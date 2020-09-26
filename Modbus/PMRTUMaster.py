import serial
import modbus_tk.modbus_rtu as mr
import modbus_tk.defines as md

master=mr.RtuMaster(serial.Serial(port="COM2",baudrate=19200,bytesize=8,parity='N',stopbits=1,xonxoff=0))
master.set_timeout(5.0)
master.set_verbose(True)

# master.execute(slave=1,function_code=md.READ_COILS,starting_address=1,quantity_of_x=5)
hold_value=master.execute(slave=1,function_code=md.READ_HOLDING_REGISTERS,starting_address=110,quantity_of_x=5,output_value=5)
print(hold_value)

coils_value=master.execute(slave=1,function_code=md.READ_COILS,starting_address=1,quantity_of_x=5,output_value=0)
print(coils_value)

def main():
    """main"""
    logger = modbus_tk.utils.create_logger(name="console", record_format="%(message)s")

    #Create the master
    master=mr.RtuMaster(serial.Serial(port="COM2",baudrate=19200,bytesize=8,parity='N',stopbits=1,xonxoff=0))
    master.set_timeout(5.0)
    master.set_verbose(True)
    
    try:
        logger.info("running...")
        logger.info("enter 'quit' for closing the server")

        server.start()

        slave_1 = server.add_slave(1)
        slave_1.add_block('0', cst.HOLDING_REGISTERS, 0, 100)
        while True:
            cmd = sys.stdin.readline()
            args = cmd.split(' ')

            if cmd.find('quit') == 0:
                sys.stdout.write('bye-bye\r\n')
                break

            elif args[0] == 'add_slave':
                slave_id = int(args[1])
                server.add_slave(slave_id)
                sys.stdout.write('done: slave %d added\r\n' % (slave_id))

            elif args[0] == 'add_block':
                slave_id = int(args[1])
                name = args[2]
                block_type = int(args[3])
                starting_address = int(args[4])
                length = int(args[5])
                slave = server.get_slave(slave_id)
                slave.add_block(name, block_type, starting_address, length)
                sys.stdout.write('done: block %s added\r\n' % (name))

            elif args[0] == 'set_values':
                slave_id = int(args[1])
                name = args[2]
                address = int(args[3])
                values = []
                for val in args[4:]:
                    values.append(int(val))
                slave = server.get_slave(slave_id)
                slave.set_values(name, address, values)
                values = slave.get_values(name, address, len(values))
                sys.stdout.write('done: values written: %s\r\n' % (str(values)))

            elif args[0] == 'get_values':
                slave_id = int(args[1])
                name = args[2]
                address = int(args[3])
                length = int(args[4])
                slave = server.get_slave(slave_id)
                values = slave.get_values(name, address, length)
                sys.stdout.write('done: values read: %s\r\n' % (str(values)))

            else:
                sys.stdout.write("unknown command %s\r\n" % (args[0]))
    
    except :
        logger.info("发生错误")

if __name__ == "__main__":
    main()