import pandas as pd
import random as r
import ast
from sklearn.preprocessing import MinMaxScaler
import numpy as np

def separate_coordinates(coords):
    # Separate x and y values
    x_values = [point[0] for point in coords]  # Extract the x values
    y_values = [point[1] for point in coords]  # Extract the y values

    # Return the combined list
    return x_values + y_values



def removalduplicat(givenlist):
    import ast
    if isinstance(givenlist, str):
        try:
            givenlist = ast.literal_eval(givenlist)
        except Exception as e:
            print(f"Error converting string to list: {e}")
            return []

    new_list = []
    for one_val in givenlist:
        if one_val not in new_list:
            new_list.append(one_val)
    if len(new_list) == 1:
        x = new_list[0][0]
        y = new_list[0][1]
        new_list.append((x + 1, y))
    return new_list

def numofinterpolation(lenoflist, required):
    i = 0
    while True:
        a = lenoflist + ((lenoflist - 1) * i)
        if a > required:
            return i
        i += 1

def interpolate_points(points, num_interpolations):
    interpolated_points = []
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i + 1]
        interpolated_points.append((x1, y1))
        for j in range(1, num_interpolations + 1):
            t = j / (num_interpolations + 1)
            x_new = x1 + (x2 - x1) * t
            y_new = y1 + (y2 - y1) * t
            interpolated_points.append((x_new, y_new))
    interpolated_points.append(points[-1])
    return interpolated_points

def equalateval(lst, equal):
    while len(lst) > equal:
        lst.pop(r.randint(0, len(lst) - 1))
    return lst

def flatten_coordinates(parsed_data):
    flattened = [point for stroke in parsed_data for point in stroke]
    return np.array(flattened)

# Function to scale coordinates
def scale_coordinates(flattened_coords):
    # Create MinMaxScaler instance for 2D scaling
    scaler = MinMaxScaler()

    # Fit and transform coordinates using the MinMaxScaler
    scaled_coords = scaler.fit_transform(flattened_coords)

    return scaled_coords

# Function to reshape scaled coordinates back to original stroke structure
def reshape_coordinates(scaled_coords, original_data):
    reshaped_data = []
    index = 0
    for stroke in original_data:
        num_points = len(stroke)
        reshaped_data.append(scaled_coords[index:index + num_points].tolist())
        index += num_points

    return reshaped_data

def flatten_coord(scaled_strokes):
    formatted_coordinates = []  # To store formatted coordinates for this cell
    for i, stroke_coordinates in enumerate(scaled_strokes):
        x_coords, y_coords = zip(*stroke_coordinates)
        formatted_coordinates.extend(x_coords)
        formatted_coordinates.extend(y_coords)
    return formatted_coordinates
# def scale_coordinates_sklearn(coordinates):
#     if not coordinates:
#         return []
#     coordinates_array = np.array(coordinates)
#     scaler = MinMaxScaler(feature_range=(0, 1))
#     scaled_array = scaler.fit_transform(coordinates_array)
#     return [tuple(coord) for coord in scaled_array]

def flatten_coordinates(coordinate_list):
    listx, listy = zip(*coordinate_list)  # Unzip into x and y coordinates
    flattened = list(listx) + list(listy)  # Concatenate x and y values
    return flattened

def flattencoordmodelinput(coord_list, max_req):
    norepeatcoord = removalduplicat(coord_list)
    no_of_time_interpolate = numofinterpolation(len(norepeatcoord), max_req)
    interpolate_list = interpolate_points(norepeatcoord, no_of_time_interpolate)
    required_interpolate_point = equalateval(interpolate_list, max_req)
    return required_interpolate_point


def result_of_prediction(finalarray,ann_model):
    a = np.array(finalarray)
    a = a.reshape(1, -1)  # Reshapes to (1, 1262)
    prediction = ann_model.predict(a)
    # Get the index of the highest probability
    predicted_class_index = np.argmax(prediction)
    return predicted_class_index




def strokeone_urdu_alphabet(index):
    urdu_alphabets = ['ا', 'ح', 'د', 'ر', 'س', 'ص', 'ط', 'ع', 'ل', 'م', 'و', 'ہ',
                      'ء', 'ی', 'ے', '?']
    if 0 <= index < len(urdu_alphabets):
        predictedValue = urdu_alphabets[index]
    else:
        print("Invalid index! Please provide an index from 0 to 15.")
    return predictedValue





# Function for the first list
def stroketwo_urdu_alphabet(index):
    first_list = ['ب', 'ج', 'خ', 'ذ', 'ز', 'ض', 'ظ', 'غ', 'ف','ن','?']
    if 0 <= index < len(first_list):
        predictedValue = first_list[index]
    else:
        print("Invalid index! Please provide an index from 0 to 10.")
    return predictedValue


# Function for the second list
def stroketwoA_urdu_alphabet(index):
    second_list = ['آ', 'ٹ', 'ڈ', 'ڑ', 'ک', '?']
    if 0 <= index < len(second_list):
        predictedValue = second_list[index]
    else:
        print("Invalid index!")
    return predictedValue


# Function for the third list
def strokethree_urdu_alphabet(index):
    third_list = ['ت', 'ق', '?']
    if 0 <= index < len(third_list):
        predictedValue = third_list[index]
    else:
        print("Invalid index!")
    return predictedValue


# Function for the fourth list
def strokethreeA_urdu_alphabet(index):
    fourth_list = ['گ', '?']
    if 0 <= index < len(fourth_list):
        predictedValue = fourth_list[index]
    else:
        print("Invalid index! Please provide an index from 0 to 1.")
    return predictedValue


# Function for the fifth list
def strokefour_urdu_alphabet(index):
    fifth_list = ['پ', 'ث', 'چ', 'ش', '?']
    if 0 <= index < len(fifth_list):
        predictedValue = fifth_list[index]
    else:
        print("Invalid index!.")
    return predictedValue





def convert(coordinates):
    formatted_coordinates = []
    for stroke in coordinates:
        stroke_data = []
        for coord in stroke:
            # Remove parentheses and split into integers
            x, y = map(int, coord.strip("()").split(", "))
            # Append as a tuple
            stroke_data.append((x, y))
        formatted_coordinates.append(stroke_data)
    return formatted_coordinates





