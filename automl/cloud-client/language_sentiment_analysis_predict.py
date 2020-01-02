# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def predict(project_id, model_id, content):
    """Predict."""
    # [START automl_language_sentiment_analysis_predict]
    from google.cloud import automl

    # TODO(developer): Uncomment and set the following variables
    # project_id = "YOUR_PROJECT_ID"
    # model_id = "YOUR_MODEL_ID"
    # content = "text to predict"

    prediction_client = automl.PredictionServiceClient()

    # Get the full path of the model.
    model_full_id = prediction_client.model_path(
        project_id, "us-central1", model_id
    )

    text_snippet = automl.types.TextSnippet(
        content=content, mime_type="text/plain"
    )  # Types: 'text/plain', 'text/html'
    payload = automl.types.ExamplePayload(text_snippet=text_snippet)

    response = prediction_client.predict(model_full_id, payload)

    for annotation_payload in response.payload:
        print(
            "Predicted class name: {}".format(annotation_payload.display_name)
        )
        print(
            "Predicted sentiment score: {}".format(
                annotation_payload.text_sentiment.sentiment
            )
        )
    # [END automl_language_sentiment_analysis_predict]