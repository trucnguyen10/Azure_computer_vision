from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image, ImageDraw, ImageFont
import sys
import time

subscription_key = '4e42c0f428d6442d984d5954293df993'
endpoint = 'https://indepro.cognitiveservices.azure.com/'
computervision_client = ComputerVisionClient(
    endpoint, CognitiveServicesCredentials(subscription_key))

# images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
# remote_image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/landmark.jpg"
folder = 'C:/Users/hersa/ComputerVision'
files = os.listdir(folder)
font = ImageFont.truetype('arial.ttf', 16)

for file in files:
    file_path = os.path.join(folder, file)
    image = Image.open(file_path)
    image_draw = ImageDraw.Draw(image)
    with open(file_path, mode='rb') as image_stream:
        results = computervision_client.detect_objects_in_stream(image_stream)

        for object in results.objects:
            left = object.rectangle.x
            top = object.rectangle.y
            width = object.rectangle.w
            height = object.rectangle.h

            shape = [(left, top), (left + width, top + height)]
            image_draw.rectangle(shape, outline='red', width=5)
            text = f'{ object.object_property } ({object.confidence * 100}%)'
            image_draw.text((left + 5 - 1, top + height - 30 + 1),
                            text, (0, 0, 0), font=font)
            image_draw.text((left + 5, top + height - 30),
                            text, (255, 0, 0), font=font)

        image.show()
#         description_results = computervision_client.describe_image_in_stream(
#             image_stream)
#         print("Description of remote iamge: ")
#         if (len(description_results.captions) == 0):
#             print("No description detected")
#         else:
#             for caption in description_results.captions:
#                 print("'{}' with confidence {:.2f}".format(
#                     caption.text, caption.confidence))
# # print("===== Tag an image - remote =====")
# # # Call API with remote image
# # tags_result_remote = computervision_client.tag_image(remote_image_url)

# # # Print results with confidence score
# # print("Tags in the remote image: ")
# # if (len(tags_result_remote.tags) == 0):
# #     print("No tags detected.")
# # else:
# #     for tag in tags_result_remote.tags:
# #         print("'{}' with confidence {:.2f}%".format(
# #             tag.name, tag.confidence * 100))
# # print()
# # '''
# # END - Tag an Image - remote
# # '''
# # print("End of Computer Vision quickstart.")
