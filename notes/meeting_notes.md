# Group 2 Meeting notes

## 11/17/2021

- Boston got an API key, hasn't pulled any data
    - Interested in solar irradiance and wind speed data
    - Paper indicates LA data from 1991 to 2010 was used
    - Fort Collins could be done after LA as our "extension" of the project
- Each node (or household) should be an instance of a defined class - use python for OOP capabilities
- PV droop controller should be written as a helper function
- Goals:
    - Adam: Figure out the test case model, and list what attributes, functions, etc. might be needed
    - Evan: Figure out the PV system model and see how it is used in each test case
    - Boston: Use the API or website to get a more-or-less complete
    data set; if that gets done, do a Kernel Density Estimate
- NREL API: https://nsrdb.nrel.gov/data-sets/api-instructions.html#Take-a-Look-at-the-Results

## 11/23/2021

- New paper similar to previous one but more simplified and with more detailed method descriptions
    - Astronomical model for converting solar irradiance to effective irradiance
    - PV module for converting effective irradiance into current output
    - Power processor for converting current output into system power
    - Markov chain model for estimating state transition probabilities
    - Clustering for day/night states
- Python classes should be written for the first three sections
    - Boston already drafted astronomical model class
    - Adam to test Boston's class and develop second two classes
    - Boston to search for python implementation of Markov model
    - Evan to research state transitions and clustering
- Use black python package to format documents and include docstrings
- Meet tomorrow to discuss progress and figure out what is needed for next week