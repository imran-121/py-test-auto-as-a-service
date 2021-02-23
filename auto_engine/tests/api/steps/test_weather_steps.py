"""

This is python file named as steps file, the purpose of step file is to
    1) connects feature file  and logic file. In our case feature file is [weather.feature]
       and logic file is [weather_logic.py]
    2) Defines the all feature file steps like [Given, When, Then etc]
    3) Provides data on run time to logic files

As we are following BDD approach for maintaining and automating test cases.

Logic drives from feature file => step file => logic file. Ideally we should be using one 1 to 1
relation between feature, step and logic file for robust and elegant framework but agains its our
choice.

"""
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
    parsers
)
import sys
import os
sys.path.append(os.getcwd())


# importing logic
from auto_engine.logic.api.weather_logic import WeatherLogic



obj_weather_log = WeatherLogic()



@scenario(r'../features/weather.feature', 'verify metaweather api response for a get request is valid')
def test_verify_report_should_open_using_public_folder_path():
    pass


@scenario(r'../features/weather.feature', 'verify metaweather api response attributes for get request')
def test_metawaether_attributes():
    pass



@given('user have valid location <location>')
def user_have_valid_location(location):
    obj_weather_log.fn_set_location(pstr_loc=location)


@when('user hits the end point <end_point>')
def user_hits_the_end_point(end_point):
    obj_weather_log.fn_set_end_point(pstr_endpoint=end_point)
    obj_weather_log.fn_send_get_request()


@then('the response of api should be <response>')
def verify_api_response(response):
    exp_response = response
    act_response = obj_weather_log.fn_get_response_status_code()
    assert (exp_response,act_response)


@then('attributes in api json response should be <json_attr>')
def verify_api_attributes(json_attr):
    exp_attri_lst = str(json_attr).split(",")
    act_attri_lst = obj_weather_log.fn_get_resp_attri_lst()
    assert(exp_attri_lst,act_attri_lst)
