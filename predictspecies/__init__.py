import logging

import azure.functions as func

import json
import os
import io

# Imports for the REST API
from flask import Flask, request, jsonify

# Imports for image processing
from PIL import Image

# Imports for prediction
from . import predict

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    predict.initialize()

    image_url = req.params.get('img')

    results = predict.predict_url(image_url)

    logging.info(type(results))

    return json.dumps(results)
