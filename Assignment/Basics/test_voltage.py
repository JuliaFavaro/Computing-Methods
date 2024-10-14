import math

from voltage import Reading #always import the file you want to test

def test_reading(timestamp=1., adc=12.):
    """ """
    r=Reading(timestamp, adc)
    assert math.isclose(r.timestamp, timestamp) #how to compare 2 floats
    assert math.isclose(r.adc, adc)

def test_reading_conversion(timestamp=1., adc=12.):
    """ """
    r=Reading(timestamp, adc)
    expect=adc* r._CONVERSION_SLOPE+ r._CONVERSION_OFFSET

    assert math.isclose(r.voltage(),expect)

#add this to our global variables inside Reading
   # _CONVERSION_SLOPE=1.653 
   # _CONVERSION_OFFSET=0.456
