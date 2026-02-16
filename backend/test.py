import google.genai as genai

genai.configure(api_key="AIzaSyA3V0QZgfpPSB5LcllWqYCxS21QNnnOlxw")

for model in genai.list_models():
    print(model.name)
