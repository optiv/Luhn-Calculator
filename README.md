# Luhn Calculator
Something I put together on an engagement and debuted to a private audience at CircleCityCon 2018.  I might document it better at some point, but the idea is:
* One way or another, set up Intruder to be producing 15-digit integers as payloads.
* Add this extension as a payload processor.
* After this processor, your payloads will be 16-digit integers that pass a Luhn check.