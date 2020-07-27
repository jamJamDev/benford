# All helpers relating to Benford's Law
# Benford's law observes that a number data set will have a higher frequncy of numbers
# that lead with a small digit (i.e. nums leading with 1 is ~30% while leading 9s are ~5% or less)
from . import files

def get_benford_data_from_file(folder, file):
    census_data = files.parse_census_file_and_gather_data(folder, file)
    # [ total count, dict of starting numbers & total, census data, census column names ]
    return census_data

def calc_percents(num_data_points, benford_data):
    percents = {}
    for key in benford_data:
        percents[key] = round((benford_data[key]/num_data_points) * 100)
    return percents

def validate_benfords_law(data):
    is_valid = False

    # Using 28 since Benford's law is "about 30%"
    if data[1] >= 28 and data[9] >= 5:
        is_valid = True

    return is_valid