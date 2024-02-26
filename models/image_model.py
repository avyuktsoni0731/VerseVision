import tensorflow as tf
import tensorflow_hub as hub

image_model = hub.load("https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4")