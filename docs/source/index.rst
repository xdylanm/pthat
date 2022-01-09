PTHat Documentation
===================

The **PTHat** is an 8 channel temperature and pressure sensing hat for the Raspberry Pi.
It is composed of a hardware module based on an array of MAX31856 ICs that handle conversion from the raw K-type thermocouple signal to a temperature value.
The MAX31856 includes an internal cold-junction reference and can report diagnostic information (temperature out of range, probe not connected). 
Communication between the host and sensor is handled over the SPI bus with address decoding used to multiplex the chip select lines. 
Pressure sensing is handled by a raw 5V analog transducer, whose value is digitized by an ADC120. 
The ADC120 is an 8 channel ADC, which can be read over the SPI bus. 

Please see the :doc:`installation` section for instructions on configuring the host Rasbperry Pi and installing the driver software. See the :doc:`usage` section for details and examples of calibrating and using the PTHat, and refer to the :doc:`api` section for the programming reference.

Contents
--------

.. toctree::

    installation
    usage
    api

