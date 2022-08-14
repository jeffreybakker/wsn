Calculating the Risk of Valve Failures when Maintaining Water Supply Networks
-----
_Read the accompanying paper on [essay.utwente.nl](http://essay.utwente.nl/87350/)_

This project contains the implementations for the different algorithms explored
in the Research Project of the Bachelor Study Technical Computer Science at the
University of Twente.

Run `main.py` for a general test suite that runs multiple example networks 
(that are defined in the paper) for multiple algorithms.

The following implementations correspond to the algorithms mentioned in the
paper:
- `basic.py`: Basic approach without BDDs
- `bdd.py`: Basic approach with BDDs
- `naive.py`: Naive approach
- `naive_optimized.py`: Naive approach with caching
- `search.py`: Search approach

## Troubleshooting

This code was developed using Python 3.9, if it does not work on your computer,
then make sure to up-/downgrade to this version.

Furthermore, make sure that you have installed all of the dependencies in
`requirements.txt`.

