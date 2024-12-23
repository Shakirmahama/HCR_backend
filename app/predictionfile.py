import functionsfile, Variables
import tensorflow as tf

#shakirdatacopy.csv
# Define file path
# file = "C:/Users/nexgen/Desktop/shakirdatacopy.csv"

# def removalduplicat(givenlist):
#     import ast
#     if isinstance(givenlist, str):
#         try:
#             givenlist = ast.literal_eval(givenlist)
#         except Exception as e:
#             print(f"Error converting string to list: {e}")
#             return []
#
#     new_list = []
#     for one_val in givenlist:
#         if one_val not in new_list:
#             new_list.append(one_val)
#     if len(new_list) == 1:
#         x = new_list[0][0]
#         y = new_list[0][1]
#         new_list.append((x + 1, y))
#     return new_list
#
# def numofinterpolation(lenoflist, required):
#     i = 0
#     while True:
#         a = lenoflist + ((lenoflist - 1) * i)
#         if a > required:
#             return i
#         i += 1
#
# def interpolate_points(points, num_interpolations):
#     interpolated_points = []
#     for i in range(len(points) - 1):
#         x1, y1 = points[i]
#         x2, y2 = points[i + 1]
#         interpolated_points.append((x1, y1))
#         for j in range(1, num_interpolations + 1):
#             t = j / (num_interpolations + 1)
#             x_new = x1 + (x2 - x1) * t
#             y_new = y1 + (y2 - y1) * t
#             interpolated_points.append((x_new, y_new))
#     interpolated_points.append(points[-1])
#     return interpolated_points
#
# def equalateval(lst, equal):
#     while len(lst) > equal:
#         lst.pop(r.randint(0, len(lst) - 1))
#     return lst
#
# def scale_coordinates_sklearn(coordinates):
#     if not coordinates:
#         return []
#     coordinates_array = np.array(coordinates)
#     scaler = MinMaxScaler(feature_range=(0, 1))
#     scaled_array = scaler.fit_transform(coordinates_array)
#     return [tuple(coord) for coord in scaled_array]
#
# def flatten_coordinates(coordinate_list):
#     listx, listy = zip(*coordinate_list)  # Unzip into x and y coordinates
#     flattened = list(listx) + list(listy)  # Concatenate x and y values
#     return flattened
#
# def flattencoordmodelinput(coord_list, max_req):
#     norepeatcoord = removalduplicat(coord_list)
#     no_of_time_interpolate = numofinterpolation(len(norepeatcoord), max_req)
#     interpolate_list = interpolate_points(norepeatcoord, no_of_time_interpolate)
#     required_interpolate_point = equalateval(interpolate_list, max_req)
#     scaled_coord_list = scale_coordinates_sklearn(required_interpolate_point)
#     x_than_y = flatten_coordinates(scaled_coord_list)
#     return x_than_y
# def result_of_prediction(finalarray,ann_model):
#     a = np.array(finalarray)
#     a = a.reshape(1, -1)  # Reshapes to (1, 1262)
#     prediction = ann_model.predict(a)
#     # Get the index of the highest probability
#     predicted_class_index = np.argmax(prediction)
#     return predicted_class_index
#
#
# def strokeone_urdu_alphabet(index):
#     urdu_alphabets = ['ا', 'ح', 'د', 'ر', 'س', 'ص', 'ط', 'ع', 'ل', 'م', 'و', 'ہ',
#                       'ء', 'ی', 'ے', 'غلط']
#     if 0 <= index < len(urdu_alphabets):
#         print(urdu_alphabets[index])
#     else:
#         print("Invalid index! Please provide an index from 0 to 15.")
# # Function for the first list
# def stroketwo_urdu_alphabet(index):
#     first_list = ['ب','ج','خ','ذ','ز','ض','ظ','غ','ف','ن','غلط']
#     if 0 <= index < len(first_list):
#         print(first_list[index])
#     else:
#         print("Invalid index! Please provide an index from 0 to 10.")
#
# # Function for the second list
# def stroketwoA_urdu_alphabet(index):
#     second_list = ['آ', 'ٹ', 'ڈ', 'ڑ', 'ک', 'غلط']
#     if 0 <= index < len(second_list):
#         print(second_list[index])
#     else:
#         print("Invalid index! Please provide an index from 0 to 5.")
#
# # Function for the third list
# def strokethree_urdu_alphabet(index):
#     third_list = ['ت', 'ق', 'غلط']
#     if 0 <= index < len(third_list):
#         print(third_list[index])
#     else:
#         print("Invalid index! Please provide an index from 0 to 2.")
#
# # Function for the fourth list
# def strokethreeA_urdu_alphabet(index):
#     fourth_list = ['گ', 'غلط']
#     if 0 <= index < len(fourth_list):
#         print(fourth_list[index])
#     else:
#         print("Invalid index! Please provide an index from 0 to 1.")
#
# # Function for the fifth list
# def strokefour_urdu_alphabet(index):
#     fifth_list = ['پ', 'ث', 'چ', 'ش', 'غلط']
#     if 0 <= index < len(fifth_list):
#         print(fifth_list[index])
#     else:
#         print("Invalid index! Please provide an index from 0 to 4.")
#
#
# df = pd.read_csv(file, header=0)
#
#
# li = df.values.tolist()
#
# # Loop through each row and process based on the number of strokes
# for row_idx, row in enumerate(li):
#     noofstroke = li[row_idx][1]  # Extract stroke count



# coordinates= [[(72, 94), (70, 94), (70, 93), (70, 91), (70, 88), (73, 88), (81, 86), (103, 85), (109, 85), (115, 85), (120, 85), (126, 85), (131, 85), (135, 85), (140, 85), (143, 85), (151, 85), (158, 86), (162, 86), (166, 86), (170, 86), (174, 86), (182, 91), (188, 91), (193, 93), (194, 94), (197, 94), (200, 94), (202, 94), (203, 94), (205, 94), (208, 94), (210, 94), (211, 94), (210, 94), (208, 94), (203, 94), (202, 94), (197, 94), (193, 94), (190, 94), (185, 94), (182, 94), (179, 94), (174, 94), (170, 94), (165, 94), (162, 94), (155, 94), (151, 96), (149, 99), (143, 102), (141, 102), (138, 104), (135, 107), (134, 107), (128, 108), (125, 110), (123, 114), (118, 118), (112, 124), (104, 130), (101, 137), (96, 142), (92, 149), (87, 156), (86, 158), (81, 164), (81, 169), (78, 172), (76, 179), (73, 186), (72, 187), (70, 195), (69, 200), (66, 203), (66, 211), (64, 217), (64, 218), (64, 220), (64, 224), (64, 226), (64, 232), (64, 235), (64, 242), (64, 246), (64, 249), (64, 257), (66, 259), (66, 265), (66, 266), (66, 272), (69, 272), (70, 277), (73, 280), (73, 285), (78, 288), (81, 288), (81, 289), (84, 294), (89, 296), (92, 296), (93, 297), (96, 301), (103, 302), (109, 304), (112, 304), (120, 305), (123, 308), (125, 308), (131, 310), (132, 311), (135, 311), (140, 311), (143, 311), (148, 311), (149, 311), (154, 311), (157, 311), (158, 311), (163, 310), (166, 310), (171, 308), (174, 305), (179, 304), (182, 304), (187, 302), (190, 302), (194, 301), (197, 297), (197, 296), (197, 294), (202, 294), (205, 289), (208, 288), (211, 282), (213, 279), (218, 274), (221, 272), (221, 269), (224, 265), (226, 265), (227, 263), (229, 259), (232, 257), (233, 256), (233, 251), (236, 249), (236, 246), (239, 242), (242, 240), (242, 238), (244, 235), (244, 234), (247, 234), (247, 232), (249, 232), (249, 230), (250, 226), (252, 224), (252, 223), (252, 218), (252, 215), (252, 211), (252, 207)], [(154, 211), (154, 212), (151, 215)]]
# strokes=2
#


def predict(coordinates, noofstroke):
    print(coordinates)
    if noofstroke == 1:
        stroke1 = functionsfile.flattencoordmodelinput(coordinates[0], Variables.data['firststroke1'])
        model = tf.keras.models.load_model("model/onestrokemodel.h5")
        return_scaled_coord = functionsfile.scale_coordinates(stroke1)
        flattenarray = functionsfile.separate_coordinates(return_scaled_coord)
        s2 = functionsfile.result_of_prediction(flattenarray, model)
        result = functionsfile.strokeone_urdu_alphabet(s2)

    elif noofstroke == 2:
        len_of_sstroke = len(coordinates[1])
        if len_of_sstroke < 30:
            model = tf.keras.models.load_model("model/dotTwoStroke.h5")
            stroke1 = functionsfile.flattencoordmodelinput(coordinates[0], Variables.data['firststroke2'])
            stroke2 = functionsfile.flattencoordmodelinput(coordinates[1], Variables.data['secondstroke2'])
            orginaldata = stroke1,stroke2
            forscaled = stroke1+stroke2
            return_scaled_coord = functionsfile.scale_coordinates(forscaled)
            coord_reshap = functionsfile.reshape_coordinates(return_scaled_coord, orginaldata)
            flattenarray = functionsfile.flatten_coord(coord_reshap)
            s2 = functionsfile.result_of_prediction(flattenarray, model)
            result= functionsfile.stroketwo_urdu_alphabet(s2)

        else:
            model = tf.keras.models.load_model("model/twoAstrokemodel.h5")
            stroke1 = functionsfile.flattencoordmodelinput(coordinates[0], Variables.data['firststroke2A'])
            stroke2 = functionsfile.flattencoordmodelinput(coordinates[1], Variables.data['secondstroke2A'])
            orginaldata = stroke1, stroke2
            forscaled = stroke1 + stroke2
            return_scaled_coord = functionsfile.scale_coordinates(forscaled)
            coord_reshap = functionsfile.reshape_coordinates(return_scaled_coord, orginaldata)
            flattenarray = functionsfile.flatten_coord(coord_reshap)
            s2 = functionsfile.result_of_prediction(flattenarray, model)
            result= functionsfile.stroketwoA_urdu_alphabet(s2)
    elif noofstroke == 3:
        # givenlistcoord = ast.literal_eval(li[row_idx][0])
        len_of_sstroke = len(coordinates[1])
        if len_of_sstroke < 30:
            model = tf.keras.models.load_model("model/threestrokemodel.h5")
            stroke1 = functionsfile.flattencoordmodelinput(coordinates[0], Variables.data['firststroke3'])
            stroke2 = functionsfile.flattencoordmodelinput(coordinates[1], Variables.data['secondstroke3'])
            stroke3 = functionsfile.flattencoordmodelinput(coordinates[2], Variables.data['thridstroke3'])
            orginaldata = stroke1, stroke2,stroke3
            forscaled = stroke1 + stroke2 + stroke3
            return_scaled_coord = functionsfile.scale_coordinates(forscaled)
            coord_reshap = functionsfile.reshape_coordinates(return_scaled_coord, orginaldata)
            flattenarray = functionsfile.flatten_coord(coord_reshap)
            s2 = functionsfile.result_of_prediction(flattenarray, model)
            result= functionsfile.strokethree_urdu_alphabet(s2)
        else:
            model = tf.keras.models.load_model("model/threeAstrokemodel.h5")
            stroke1 = functionsfile.flattencoordmodelinput(coordinates[0], Variables.data['firststroke3A'])
            stroke2 = functionsfile.flattencoordmodelinput(coordinates[1], Variables.data['secondstroke3A'])
            stroke3 = functionsfile.flattencoordmodelinput(coordinates[2], Variables.data['thridstroke3A'])
            orginaldata = stroke1, stroke2, stroke3
            forscaled = stroke1 + stroke2 + stroke3
            return_scaled_coord = functionsfile.scale_coordinates(forscaled)
            coord_reshap = functionsfile.reshape_coordinates(return_scaled_coord, orginaldata)
            flattenarray = functionsfile.flatten_coord(coord_reshap)
            s2 = functionsfile.result_of_prediction(flattenarray, model)
            result= functionsfile.strokethreeA_urdu_alphabet(s2)
    elif noofstroke == 4:
        # givenlistcoord = ast.literal_eval(li[row_idx][0])
        model = tf.keras.models.load_model("model/fourstrokemodel.h5")
        stroke1 = functionsfile.flattencoordmodelinput(coordinates[0], Variables.data['firststroke4'])
        stroke2 = functionsfile.flattencoordmodelinput(coordinates[1], Variables.data['secondstroke4'])
        stroke3 = functionsfile.flattencoordmodelinput(coordinates[2], Variables.data['thirdstroke4'])
        stroke4 = functionsfile.flattencoordmodelinput(coordinates[3], Variables.data['fourthstroke4'])
        orginaldata = stroke1, stroke2, stroke3, stroke4
        forscaled = stroke1 + stroke2 + stroke3 + stroke4
        return_scaled_coord = functionsfile.scale_coordinates(forscaled)
        coord_reshap = functionsfile.reshape_coordinates(return_scaled_coord, orginaldata)
        flattenarray = functionsfile.flatten_coord(coord_reshap)
        s2 = functionsfile.result_of_prediction(flattenarray, model)
        result= functionsfile.strokefour_urdu_alphabet(s2)

    else:
        # Skip invalid stroke counts
        print(f"Skipping row with invalid stroke count: {noofstroke}")
        result='?'
        # continue
    return result

# predict(coordinates,strokes)