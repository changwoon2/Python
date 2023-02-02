# import travel.Australia
# trip_to = travel.Australia.AustraliaPackage()
# trip_to.detail()

# from travel.Australia import AustraliaPackage
# trip_to = AustraliaPackage()
# trip_to.detail()

# from travel import Vietnam
# trip_to = Vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
trip_to = australia.AustraliaPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(australia))