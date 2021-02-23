import requests

"""
    Below class is called as logic file and the purpose of this class is 
    1) to hold the logic required to step file
    2) to preserve information and functionality required by test case in step files
    3) binded with test_weather_steps.py file
       auto_engine/tests/api/steps/test_weather_steps.py
    4) to be used in only in steps files, called as segregation of concerns [OOP principle]
    
"""
class WeatherLogic:
    def __init__(self): # constructor
        """
        purpose of below member variables
         1) is to store the value of parameters like location, response and endpoint
         from weather.feature file[auto_engine/tests/api/features/weather.feature]
         2) to share the information among member functions
         3) all of them are initialized to zero
        """
        self.var_loc = '' # store the value of location
        self.var_end_point = '' # store the value of end_point required to run the test case
        self.var_response = '' # store the end point response


    def fn_set_location(self,pstr_loc): # this function will set the value of [self.var_loc]
        try:
            self.var_loc = pstr_loc
        except Exception as e:
            """
                If the exception raises then I will doing following steps
                1) write the exception in file under outputs/exceptions/api/api_exception.txt
                   for back tracking purpose
                2) for writing exception we will use helper function defined in module
                   auto_code/auto_engine/helpers/helper.py
                3) continue execution 
                4) value of [self.var_loc] will be '' as initialized in constructor
            """
            pass


    def fn_set_end_point(self,pstr_endpoint): # setting the value of endpoint as above fn
        try:
            self.var_end_point = pstr_endpoint
        except Exception as e:
            pass

    def fn_send_get_request(self):
        """
            This function will send the request to below url
            1) send request to below resource after concatenating
                [self.var_end_point + self.var_loc]
                [https://www.metaweather.com/api/location/search/?query= + berlin]
                => https://www.metaweather.com/api/location/search/?query=berlin
            2)stores the response to member variable [self.var_response]
        """
        try:
            temp_res = requests.get(url=self.var_end_point + self.var_loc)
            self.var_response = temp_res
        except Exception as e:
            # write the exception in log file using helper method
            pass

    def fn_get_response_status_code(self):
        """
        This function will
            1) extract api response from member variable [self.var_response]
            2) returns the response, this response will be used in step file for assertion
            3) if exception occurs then it will be recorded in log file by helper function and
               the local variable[loc_status_code] will be settled to ''
        """
        loc_status_code = ''
        try:
            loc_status_code = self.var_response.status_code
        except Exception as e:
            # write the exception in log file for back tracking
            loc_status_code = ''
        finally:
            return loc_status_code

    def fn_get_resp_attri_lst(self):
        loc_lst_attr = []
        try:
            resp_json = self.var_response.json()
            attr = resp_json[0].keys()
            loc_lst_attr = list(attr)
        except Exception as e:
            """
            log the exception to log file using helper function in module 
            auto_code/auto_engine/helpers/helper.py
            """
            loc_lst_attr = None
        finally:
            return loc_lst_attr



