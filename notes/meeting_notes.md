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

## 11/24/2021

- Objectives:
    - Evan: Explore clustering and plotting clustering
    - Adam: Read about Python implementations of Markov models
    - Boston: Finish the output current caculation, including adding
    a column to the data
- We discovered how to calculate the maximum power
- We realized that the `i_out` variable needs the voltage that maximizes
the power, meaning we should not get maximum power, but rather the `i_out`
resulting from maximum power.

## 12/1/2021
- Discussion of bootstrapping methods for current output data
    - Time series bootstrap over 24 hours or over only daylight hours
- Discussion of reproducibility and conversion from Python to R
    - Functions written in Python read and process data
    - RMarkdown file (final paper) will read in data and produce plots and tables with ggplot, etc.
    - Plots and tables will be exported to local directory for upload into separate RMarkdown (pres)
- Objectives:
    - Evan: Perform bootstrapping on current output data and generate plots on interest
    - Boston: Push templates for paper and presentation RMarkdowns and begin writing 
    - Adam: Begin filling out skeleton for presentation and begin writing paper
- These tasks should be mostly finished by the end of the week and then we can all begin focusing on the paper and presentation.
