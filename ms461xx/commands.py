import sys

class ScipiCmds:
    def __init__(self, vna):
        self.vna = vna

    def get_device_info(self):
        try:
            vna_info = vna.query("*IDN?")
        except Exception as e:
            vna.log_output("An unknown error occurred while gathering instrument info: ", e)
            sys.exit()
        vna.log_output(f"Instrument Info: {vna_info}")

    def reset(self):
        try:
            vna.write("*RST")
        except Exception as e:
            vna.log_output("An unknown error occurred during VNA Reset: ", e)
            sys.exit()
        vna.log_output("Reset command sent successfully")

        
 
