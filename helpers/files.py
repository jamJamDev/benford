# File related helpers

def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def parse_census_file_and_gather_data(folder, file):
    file_path = folder + "/" + file.filename
    opened_file = open(file_path, "r")
    lines = opened_file.readlines()
    column_names = lines.pop(0)
    census = {}
    num_data_points = 0
    benford_count = {}

    # How should I store? dictionary by state, then town then #
    for line in lines:
        num_data_points += 1

        # replace any tabs w/spaces & split by space, then lower case
        data = line.replace('\t', ' ').split(' ')
        for i in range(len(data)):
            data[i] = data[i].lower()

        # get the state name, consider states with 2 words
        # new, north, south, west
        state = ''
        if data[0] == 'new' or data[0] == 'n' or data[0] == 's' or data[0] == 'w' or data[0] == 'north' or data[0] == 'south' or data[0]  == 'west':
            state += data[0]
            data.pop(0)
        state += data[0]
        data.pop(0)

        count = data.pop(-1).replace('\n', '')
        # update benford_count
        first_num = int(str(count)[0])
        if first_num in benford_count:
            benford_count[first_num] += 1
        else:
            benford_count[first_num] = 1

        town = ' '.join(data)

        if state in census:
            census[state].append({
                town: count
            })
        else:
            census[state] = [{
                town: count
            }]

    # return the number of data points, dict of starting numbers & total, census data, census column names
    return [num_data_points, benford_count, census, column_names]