''' Provided by Danny'''


import datetime as dt

class time_french():
    '''
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on a French WCA
    '''

    def __init__(self):
        self.prefix = range(0,2) +  range(3,6) # -> IT IS
        self.minutes=[[], \
            # -> CINQ
            range(94,98), \
            # -> DIX
            range(74,77), \
            # -> ET QUART
            range(77,79) + range(80,85), \
            # -> VINGT
            range(88,92), \
            # -> VINGT CINQ
            range(88,98), \
            # -> ET DEMI
            range(99,101) + range(102,106), \
            # -> MOINS VINGT CINQ
            range(66,71) + range(88,98), \
            # -> MOINS VINGT
            range(66,71) + range(88,92), \
            # -> MOINS LE QUART
            range(66,71) + range(72,74) + range(80,85), \
            # -> MOINS DIX
            range(66,71) + range(74,77), \
            # -> MOINS CINQ
            range(66,71) + range(94,98) ]
            # -> MINUIT
        self.hours= [range(49,55), \
            # -> UNE HEURE
            range(26,29) + range(60,65), \
            # -> DEUX HEURES
            range(7,11) + range(60,66), \
            # -> TROIS HEURES
            range(17,22) + range(60,66), \
            # -> QUATRE HEURES
            range(11,17) + range(60,66), \
            # -> CINQ HEURES
            range(40,44) + range(60,66), \
            # -> SIX HEURES
            range(37,40) + range(60,66), \
            # -> SEPT HEURES
            range(29,33) + range(60,66), \
            # -> HUIT HEURES
            range(33,37) + range(60,66), \
            # -> NEUF HEURES
            range(22,26) + range(60,66), \
            # -> DIX HEURES
            range(46,49) + range(60,66), \
            # -> ONZE HEURES
            range(55,59) + range(60,66), \
            # -> MIDI
            range(44,48)]
        # -> OCLOCK
        self.full_hour= range(104,110)

    def get_time(self, time, withPrefix=True):
        hour=time.hour%12+(1 if time.minute/5 >= 7 else 0)
        minute=time.minute/5
        # Assemble indices
        return  \
            (self.prefix if withPrefix else []) + \
            self.minutes[minute] + \
            self.hours[hour] + \
            (self.full_hour if (minute == 0) else [])
