import sys

class ScipiCmds:
    '''Class to hold SCPI commands for the MS461xx VNA'''
    def __init__(self, vna):
        self.vna = vna
        
class Query:
    '''Class to hold SCPI query commands for the MS461xx VNA'''
    def __init__(self, vna):
        super().__init__(vna)

    def device_info(self):
        '''Query the instrument for its IDN info'''
        try:
            vna_info = self.vna.query("*IDN?")
        except Exception as e:
            self.vna.log_output("An unknown error occurred while gathering instrument info: ", e)
            sys.exit()
        self.vna.log_output(f"Instrument Info: {vna_info}")
        
class Cmd:
    '''Class to hold SCPI commands for the MS461xx VNA'''
    def __init__(self, vna):
        super().__init__(vna)
        
    def reset(self):
        '''Reset the VNA to its default state'''
        try:
            self.vna.write("*RST")
        except Exception as e:
            self.vna.log_output("An unknown error occurred during VNA Reset: ", e)
            sys.exit()
        self.vna.log_output("Reset command sent successfully")

