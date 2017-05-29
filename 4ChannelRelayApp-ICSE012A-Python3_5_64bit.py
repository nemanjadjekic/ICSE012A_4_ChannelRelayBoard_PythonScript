import sys
import serial
import time


def userManual():

    print('-----------------------------------------------------------------')
    print('\t\tPYTHON RELAY APPLICATION')
    print('-----------------------------------------------------------------')
    print('\n\tType in 1 to turn on Relay 1')
    print('\tType in 2 to turn on Relay 2')
    print('\tType in 3 to turn on Relay 3')
    print('\tType in 4 to turn on Relay 4')
    print('')
    print('\tType in 12 to turn on Relay 1 and Relay 2')
    print('\tType in 13 to turn on Relay 1 and Relay 3')
    print('\tType in 14 to turn on Relay 1 and Relay 4')
    print('\tType in 23 to turn on Relay 2 and Relay 3')
    print('\tType in 24 to turn on Relay 2 and Relay 4')
    print('\tType in 34 to turn on Relay 3 and Relay 4')
    print('')
    print('\tType in 123 to turn on Relay 1, Relay 2 and Relay 3')
    print('\tType in 124 to turn on Relay 1, Relay 2 and Relay 3')
    print('\tType in 134 to turn on Relay 1, Relay 2 and Relay 3')
    print('\tType in 234 to turn on Relay 1, Relay 2 and Relay 3')
    print('')
    print('\tType in 1234 to turn all Relays on')
    print('\tType in 00 to turn all relays off')
    print('')
    print('\tType in UM to open user manual during the work')
    print('\tType in Q to quit program or control loop')
    print('\n-----------------------------------------------------------------')
    print('\t\t\tTHE END')
    print('-----------------------------------------------------------------')

    
def initialization():

    command_1=b"\x50"
    command_2=b"\x51"
    command_3=b"\x01"
    command_4=b"\x00"

    print("System initialization in progress. Please wait...\n")
    #Initialization
    time.sleep(1)
    ser.write(command_1)
    time.sleep(1)
    ser.write(command_2)
    time.sleep(1)
    ser.write(command_3)
    time.sleep(1)
    ser.write(command_4)
    time.sleep(1)    

    userManual()

    
def mainLoop():

    #Defines

    '''
    Table 1:

    \n (HEX 0x00) 0000 - All relays are on. Char: all_on/1234
    \n (HEX 0x01) 0001 - Relays 4,3 and 2 are on. Char: 234
    \n (HEX 0x02) 0010 - Relays 4,3 and 1 are on. Char: 134
    \n (HEX 0x03) 0011 - Relays 4 and 3 are on \n. Char: 34
    '''
    all_relays_on = b"\x00"
    relays_432_on = b"\x01"
    relays_431_on = b"\x02"
    relays_43_on = b"\x03"

    '''
    Table 2:
    \n (HEX 0x04) 0100 - Relays 4,2 and 1 are on. Char: 124
    \n (HEX 0x05) 0101 - Relays 4 and 2 are on. Char: 24
    \n (HEX 0x06) 0110 - Relays 4 and 1 are on. Char: 14
    \n (HEX 0x07) 0111 - Relay 4 is on. Char: 4 \n
    '''
    relays_421_on = b"\x04"
    relays_42_on = b"\x05"
    relays_41_on = b"\x06"
    relay_4_on = b"\x07"

    '''
    Table 3:
    \n (HEX 0x08) 1000 - Relays 3,2 and 1 are on. Char: 123
    \n (HEX 0x09) 1001 - Relays 3 and 2 are on. Char: 23
    \n (HEX 0x0A) 1010 - Relays 3 and 1 are on. Char: 13
    \n (HEX 0x0B) 1011 - Relay 3 is on. Char: 3 \n
    '''
    relays_321_on = b"\x08"
    relays_32_on = b"\x09"
    relays_31_on = b"\x0A"
    relay_3_on = b"\x0B"

    '''
    Table 4:
    \n (HEX 0x0C) 1100 - Relays 2 and 1 are on. Char: 12
    \n (HEX 0x0D) 1101 - Relay 2 is on. Char: 2
    \n (HEX 0x0E) 1110 - Relay 1 is on. Char: 1
    \n (HEX 0x0F) 1111 - All relays are off. Char: all_off \n
    '''
    relays_21_on = b"\x0C"
    relay_2_on = b"\x0D"
    relay_1_on = b"\x0E"
    all_relays_off = b"\x0F"


    #Loop booleans
    loopProgram = True
    

    #Initialization function call
    initialization()
    
   
    while loopProgram:
        
        inputCommand = input('\nType in Y to continiue or Q to quit program.\nType in UM to open user manual.\nType in your choice here:\t')

        if inputCommand == 'y':

            relayLoop = True
                
            while relayLoop:

                controlCommand = input('\nType in commands to turn on selected relays:\t')

                #First section
                if controlCommand == '1':
                    ser.write(relay_1_on)
                    print('\nRelay 1 is on!')

                elif controlCommand == '2':
                    ser.write(relay_2_on)
                    print('\nRelay 2 is on!')

                elif controlCommand == '3':
                    ser.write(relay_3_on)
                    print('\nRelay 3 is on!')

                elif controlCommand == '4':
                    ser.write(relay_4_on)
                    print('\nRelay 4 is on!')

                #Second sectrion   
                elif controlCommand == '12':
                    ser.write(relays_21_on)
                    print('\nRelays 1 and 2 are on!')

                elif controlCommand == '13':
                    ser.write(relays_31_on)
                    print('\nRelays 1 and 3 are on!')

                elif controlCommand == '14':
                    ser.write(relays_41_on)
                    print('\nRelays 1 and 4 are on!')

                elif controlCommand == '23':
                    ser.write(relays_32_on)
                    print('\nRelays 2 and 3 are on!')

                elif controlCommand == '24':
                    ser.write(relays_42_on)
                    print('\nRelays 2 and 4 are on!')

                elif controlCommand == '34':
                    ser.write(relays_43_on)
                    print('\nRelays 3 and 4 are on!')
                    
                #Third section
                elif controlCommand == '123':
                    ser.write(relays_321_on)
                    print('\nRelays 1, 2 and 3 are on!')

                elif controlCommand == '124':
                    ser.write(relays_421_on)
                    print('\nRelays 1, 2 and 4 are on!')

                elif controlCommand == '134':
                    ser.write(relays_431_on)
                    print('\nRelays 1, 3 and 4 are on!')

                elif controlCommand == '234':
                    ser.write(relays_432_on)
                    print('\nRelays 2, 3 and 4 are on!')
                    
                #Fourth section
                elif controlCommand == '1234':
                    ser.write(all_relays_on)
                    print('\nAll relays are on!')

                elif controlCommand == '00':
                    ser.write(all_relays_off)
                    print('\nAll relays are off!')
                    
                #Fifth section
                elif controlCommand == 'q' or controlCommand == 'Q':
                    relayLoop = False
                    print('\nYou exited control loop!')

                elif controlCommand == 'um' or controlCommand == 'uM' or controlCommand == 'Mm' or controlCommand == 'UM':
                    userManual()

                else:
                    print('\nWrong input! Try again!')
                    

        elif inputCommand == 'q' or inputCommand == 'Q':
            quit()

        elif inputCommand == 'um' or inputCommand == 'uM' or inputCommand == 'Um' or inputCommand == 'UM':
            userManual()

        else:
            print('\nWrong input! Try again!')    
  


if __name__ == "__main__":

    while True:
   
        try:
            portName = input("Type COM port name here: \t")
            baudRate = 9600#input('Type baud rate: \n')

            if portName == 'q' or portName == 'Q':
                quit()
                break
    
            else:
                ser = serial.Serial(
                    portName,
                    baudRate,
                )
                        
            mainLoop()
            break
 
        except Exception as e:
            print('\nCOM port name not found! Please type in new name again or Q to exit program!')

            
    
    
    
    

    
       
        
    

