import json
from sqlalchemy import null
from CorrectingInputData import CorrectingInputData


class GettingRequestFromClient :

    def __init__(self,request):
        self.request = request
        self.input_JSONcontent = None
        self.input_listcontent = None
        self.correcting_input_handler = None
        self.train_neural_network = None
        self.create_response_request = None
        pass

    def parse_JSONcontent(self):
        self.input_JSONcontent = self.request.get_json()
        content_list = json.loads(self.input_JSONcontent)
        return content_list
    
    def run_server_program(self):
        self.input_listcontent = self.parse_JSONcontent()
        self.correcting_input_handler = CorrectingInputData(self.input_listcontent)
        if self.correcting_input_handler != null and len(self.input_listcontent) != 0:
            self.correcting_input_handler.correct_input_data()
        return