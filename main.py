from ms461xx.connection import VnaSocket
from ms461xx.commands import Query, Cmd


def main(address, timeout):
    '''Main function to run the script'''
    
    # 0. Instrument connection
    vna = VnaSocket(address, timeout)

    # 1. load commands
    query = Query(vna)
    cmd = Cmd(vna)

    # 2. Read Instrument type
    query.device_info()

    ##############################################################################
    # run additional scipi commands here



    ##############################################################################

    # 3. System reset (for testing purposes)
    cmd.reset()
    
    # 4. Connection closing
    vna.close()

if __name__ == "__main__":

    # run main
    main(address="TCPIP0::127.0.0.1::5001::SOCKET", timeout=5000)


