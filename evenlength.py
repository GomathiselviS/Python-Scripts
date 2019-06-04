# -*- coding: utf-8 -*-
"""


Go through the string below and if the length of a word is even print "even!"


"""


st = 'Print every word in this sentence that has an even number of letters'
result={s:"EVEN!" for s in st.split() if len(s)%2==0}
print(result)