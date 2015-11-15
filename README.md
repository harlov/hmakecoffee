# HMakeCoffee, version 1.0.0

It's ready for production use in coffee machines!

Install:
	pip install hmakecoffee

To use:

1. In console:

hmakecoffee-cli

2. As library:

from hmakecoffe import MakeCoffeeService
hms = MakeCoffeeService()
hms.get_cup()