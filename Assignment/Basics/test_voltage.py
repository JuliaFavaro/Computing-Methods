import math
#always import the file you want to test, this works only if the Module is in the same folder
from voltage import Reading 

def test_reading(timestamp=1., adc=12.):
    """ """
    r=Reading(timestamp, adc)
    assert math.isclose(r.timestamp, timestamp) #how to compare 2 floats
    assert math.isclose(r.adc, adc)

def test_reading_conversion(timestamp=1., adc=12.):
    """ """
    r=Reading(timestamp, adc)
    assert math.isclose(r.voltage(),Reading._adc_to_voltage(adc))

#then use pytest to run this test on terminal 
#use GitHub Actions to automatize the test