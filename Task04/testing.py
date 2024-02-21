import os
from dotenv import load_dotenv
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

def load_configuration():
    load_dotenv()
    return (
        os.getenv('PredictionEndpoint'),
        os.getenv('PredictionKey'),
        os.getenv('ProjectID'),
        os.getenv('ModelName')
    )

def main():
    try:
        prediction_endpoint, prediction_key, project_id, model_name = load_configuration()
        prediction_client = CustomVisionPredictionClient(endpoint=prediction_endpoint, credentials=ApiKeyCredentials(in_headers={"Prediction-key": prediction_key}))
        for image_name in os.listdir(r'C:\Task04\testingImages'):
            with open(os.path.join(r'C:\Task04\testingImages', image_name), "rb") as image_data:
                results = prediction_client.classify_image(project_id, model_name, image_data)
                for prediction in results.predictions:
                    if prediction.probability > 0.5:
                        print(f"{image_name}: {prediction.tag_name} ({prediction.probability:.4f})")
    except Exception as ex:
        print(f"Error : {ex}")

if __name__ == "__main__":
    main()


