@api
Feature: Testing MetaWeather api
  As a QA member
  I want to test end point
  So that user can have useful data

  @smoke @high_priority @positive
  Scenario Outline: verify metaweather api response for a get request is valid
    Given user have valid location <location>
    When user hits the end point <end_point>
    Then the response of api should be <response>
  Examples:
      |location |  response |end_point |
      |berlin   |     200   |https://www.metaweather.com/api/location/search/?query=|


  @regression @high_priority @positive
  Scenario Outline: verify metaweather api response attributes for get request
    Given user have valid location <location>
    When user hits the end point <end_point>
    Then attributes in api json response should be <json_attr>
  Examples:
      |location |json_attr                             |end_point |
      |berlin   |title, location_type, woeid, latt_long|https://www.metaweather.com/api/location/search/?query=|