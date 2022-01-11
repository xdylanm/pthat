Usage
=====

Basic Test
----------

This basic test will flash the onboard LEDs in sequence.

>>> import pthat.board as board
>>> hat = board.Controller()
[ ... ]
>>> hat.blink_start()

Read Temperature
----------------

The read_T method will read the temperature from selected channels and report the value (degrees C):

>>> import pthat.board as board
>>> hat = board.Controller()
[ ... ]
>>> hat.read_T(ch=4)        # Read a single channel
[(4, 21.17, [])]
>>> hat.read_T(ch=[0,4])    # Read a list of channels from 0..7
[(0, 1372.05, ['TC_RANGE', 'OPEN']), (4, 21.17, [])]

The returned values are tuples that include the channel ID, the temperature reading and a list of error codes.
In the example above, channel 0 is open (no probe connected).

Read Pressure
-------------

The read_P method will read the analog level from the pressure sensor and report the raw value on the range 0..1.
Similar to the read_T method, the returned values are a tuple containing the channel ID and the raw value.
The pressure channels do not report errors. A disconnected probe will return 0.0.

>>> import pthat.board as board
>>> hat = board.Controller()
[ ... ]
>>> hat.read_P(ch=[1,5])
[(1, 0.1177045177045177), (5, 0.6046398046398046)]

