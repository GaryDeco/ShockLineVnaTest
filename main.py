from ms461xx.vna_socket import VnaSocket


def main(address, timeout):

    # 0. Instrument connection
    vna = VnaSocket(address, timeout)

    # 1. Read Instrument type

    vna.query("*IDN?")
    vna.log_output(f"Instrument Info: {vna_info}")

    # 2. System reset
    vna.write("*RST")
    vna.log_output("Reset command sent")

    # 3. Connection closing
    vna.close()
    vna.log_output("Connection closed.")


if __name__ == "__main__":

    # define TCP address and timeout
    address="TCPIP0::127.0.0.1::5001::SOCKET"
    timeout=5000 

    # run main
    main(address, timeout)


