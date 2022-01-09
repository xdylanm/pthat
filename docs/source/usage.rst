Usage
=====

Basic Test
----------

This basic test will flash the onboard LEDs in sequence.

>>> from pthat.pthat import PTHat
>>> driver = PTHat()
[ ... ]
>>> driver.blink_start()
