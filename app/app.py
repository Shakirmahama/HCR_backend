
from flask import Flask, request, jsonify
import functionsfile
import predictionfile


app = Flask(__name__)

@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        # Parse the incoming JSON payload
        data = request.json

        # Extract coordinates and numStroke from the JSON data
        coordinates = data.get('coordinates', [])
        num_stroke = data.get('numStroke', 0)
        print(len(coordinates))
        formated_data= functionsfile.convert(coordinates)
        print(len(formated_data))
        result= predictionfile.predict(formated_data, num_stroke)
        # Display the received data on the console
        print("Received Data:")
        print(result)
        print(f"Coordinates: {coordinates}")
        print(f"formatedCoordinates: {formated_data }")
        print(f"Number of Strokes: {num_stroke}")

        # Prepare a response to send back to the client
        response = {
            'data':  result,
            "message": "Data received successfully",
            "receivedCoordinates": "success",
        }

        # Return the response as JSON
        return jsonify(response), 200
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"message": "An error occurred", "error": str(e)}), 400


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)





























# if noofstroke == 1:
#     max_points = 631
#     provied_coord = formatted_coordinates[0]
#
#     points_in_row = function.flattencoordmodelinput(provied_coord, max_points)
#     model = tf.keras.models.load_model("model/onestrokemodel.h5")
#
#     z = function.result_of_prediction(points_in_row, model)
#     function.strokeone_urdu_alphabet(z)
#     # print(li[row_idx][2])
#
# elif noofstroke == 2:
#     givenlistcoord = formatted_coordinates
#     len_of_sstroke = len(givenlistcoord[1])
#     if len_of_sstroke < 35:
#         model = tf.keras.models.load_model("model/twostrokemodel.h5")
#         print(model)
#         stroke1 = function.flattencoordmodelinput(givenlistcoord[0], 564)
#         stroke2 = function.flattencoordmodelinput(givenlistcoord[1], 50)
#         flattenarray = list(stroke1) + list(stroke2)
#         s2 = function.result_of_prediction(flattenarray, model)
#         function.stroketwo_urdu_alphabet(s2)
#         # print(li[row_idx][2])
#     else:
#         model = tf.keras.models.load_model("model/twoAstrokemodel.h5")
#         stroke1 = flattencoordmodelinput(givenlistcoord[0], 444)
#         stroke2 = flattencoordmodelinput(givenlistcoord[1], 433)
#         flattenarray = list(stroke1) + list(stroke2)
#         s2 = result_of_prediction(flattenarray, model)
#         stroketwoA_urdu_alphabet(s2)
#         print(li[row_idx][2])
# elif noofstroke == 3:
#     givenlistcoord = ast.literal_eval(li[row_idx][0])
#     len_of_sstroke = len(givenlistcoord[1])
#     if len_of_sstroke < 35:
#         model = tf.keras.models.load_model("model/threestrokemodel.h5")
#         stroke1 = flattencoordmodelinput(givenlistcoord[0], 498)
#         stroke2 = flattencoordmodelinput(givenlistcoord[1], 69)
#         stroke3 = flattencoordmodelinput(givenlistcoord[2], 48)
#         flattenarray = list(stroke1) + list(stroke2) + list(stroke3)
#         s2 = result_of_prediction(flattenarray, model)
#         strokethree_urdu_alphabet(s2)
#         print(li[row_idx][2])
#     else:
#         model = tf.keras.models.load_model("model/threeAstrokemodel.h5")
#         stroke1 = flattencoordmodelinput(givenlistcoord[0], 256)
#         stroke2 = flattencoordmodelinput(givenlistcoord[1], 113)
#         stroke3 = flattencoordmodelinput(givenlistcoord[2], 232)
#         flattenarray = list(stroke1) + list(stroke2) + list(stroke3)
#         s2 = result_of_prediction(flattenarray, model)
#         strokethreeA_urdu_alphabet(s2)
#         print(li[row_idx][2])
# elif noofstroke == 4:
#     givenlistcoord = ast.literal_eval(li[row_idx][0])
#     model = tf.keras.models.load_model("model/fourstrokemodel.h5")
#     stroke1 = flattencoordmodelinput(givenlistcoord[0], 577)
#     stroke2 = flattencoordmodelinput(givenlistcoord[1], 47)
#     stroke3 = flattencoordmodelinput(givenlistcoord[2], 43)
#     stroke4 = flattencoordmodelinput(givenlistcoord[3], 48)
#     flattenarray = list(stroke1) + list(stroke2) + list(stroke3) + list(stroke4)
#     s4 = result_of_prediction(flattenarray, model)
#     strokefour_urdu_alphabet(s4)
#     print(li[row_idx][2])
#
# else:
#     # Skip invalid stroke counts
#     print(f"Skipping row with invalid stroke count: {noofstroke}")
#
# flattenarray = []
#
#
#
#



























# Loop through each row and process based on the number of strokes
# for row_idx, row in enumerate(li):
#     noofstroke = li[row_idx][1]  # Extract stroke count
#         noofstroke=strokes
#
#     if noofstroke == 1:
#         max_points = 631
#         provied_coord = li[row_idx][0]
#         points_in_row = flattencoordmodelinput(provied_coord,max_points)
#         model = tf.keras.models.load_model("model/onestrokemodel.h5")
#
#         z = result_of_prediction(points_in_row,model)
#         strokeone_urdu_alphabet(z)
#         print(li[row_idx][2])
#
#     elif noofstroke == 2:
#         givenlistcoord = ast.literal_eval(li[row_idx][0])
#         len_of_sstroke = len(givenlistcoord[1])
#         if len_of_sstroke < 35:
#             model = tf.keras.models.load_model("model/twostrokemodel.h5")
#             print(model)
#             stroke1 = flattencoordmodelinput(givenlistcoord[0], 564)
#             stroke2 = flattencoordmodelinput(givenlistcoord[1], 50)
#             flattenarray = list(stroke1)+ list(stroke2)
#             s2 = result_of_prediction(flattenarray,model)
#             stroketwo_urdu_alphabet(s2)
#             print(li[row_idx][2])
#         else:
#             model = tf.keras.models.load_model("model/twoAstrokemodel.h5")
#             stroke1 = flattencoordmodelinput(givenlistcoord[0], 444)
#             stroke2 = flattencoordmodelinput(givenlistcoord[1], 433)
#             flattenarray = list(stroke1) + list(stroke2)
#             s2 = result_of_prediction(flattenarray, model)
#             stroketwoA_urdu_alphabet(s2)
#             print(li[row_idx][2])
#     elif noofstroke == 3:
#         givenlistcoord = ast.literal_eval(li[row_idx][0])
#         len_of_sstroke = len(givenlistcoord[1])
#         if len_of_sstroke < 35:
#             model = tf.keras.models.load_model("model/threestrokemodel.h5")
#             stroke1 = flattencoordmodelinput(givenlistcoord[0], 498)
#             stroke2 = flattencoordmodelinput(givenlistcoord[1], 69)
#             stroke3 = flattencoordmodelinput(givenlistcoord[2], 48)
#             flattenarray = list(stroke1) + list(stroke2) + list(stroke3)
#             s2 = result_of_prediction(flattenarray, model)
#             strokethree_urdu_alphabet(s2)
#             print(li[row_idx][2])
#         else:
#             model = tf.keras.models.load_model("model/threeAstrokemodel.h5")
#             stroke1 = flattencoordmodelinput(givenlistcoord[0], 256)
#             stroke2 = flattencoordmodelinput(givenlistcoord[1], 113)
#             stroke3 = flattencoordmodelinput(givenlistcoord[2], 232)
#             flattenarray = list(stroke1) + list(stroke2) + list(stroke3)
#             s2 = result_of_prediction(flattenarray, model)
#             strokethreeA_urdu_alphabet(s2)
#             print(li[row_idx][2])
#     elif noofstroke == 4:
#         givenlistcoord = ast.literal_eval(li[row_idx][0])
#         model = tf.keras.models.load_model("model/fourstrokemodel.h5")
#         stroke1 = flattencoordmodelinput(givenlistcoord[0], 577)
#         stroke2 = flattencoordmodelinput(givenlistcoord[1], 47)
#         stroke3 = flattencoordmodelinput(givenlistcoord[2], 43)
#         stroke4 = flattencoordmodelinput(givenlistcoord[3], 48)
#         flattenarray = list(stroke1) + list(stroke2) + list(stroke3) +list(stroke4)
#         s4 = result_of_prediction(flattenarray,model)
#         strokefour_urdu_alphabet(s4)
#         print(li[row_idx][2])
#
#     else:
#         # Skip invalid stroke counts
#         print(f"Skipping row with invalid stroke count: {noofstroke}")
#         continue
#     flattenarray = []







