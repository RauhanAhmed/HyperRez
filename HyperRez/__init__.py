import shutil
import os
import gradio as gr
import cv2
import math

class ImageUpscaler:

  def __init__(self):
    pass

  def upscale(self, image, scale_factor, model_version, _):
    try:
      shutil.rmtree("inputs")
      shutil.rmtree("results")
    except:
      pass
    os.mkdir("inputs")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite("inputs/image.jpg", image)
    os.system(f"python -m ImageUpscaler.inference_realesrgan -n RealESRGAN_x4plus -i inputs -o results --outscale {scale_factor} --face_enhance --face_enhance_model {model_version}")
    filename = os.listdir("results")[0]
    file_path = os.path.join("results", filename)
    result_image = cv2.imread(file_path)
    result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    return result_image

  def launchInterface(self):
    interface = gr.Interface(
        fn = self.upscale,
        inputs = [
            "image",
            gr.Slider(2, 10, value = 2, label = "Upscale Factor", info = "Resolution upscaling factor"),
            gr.Dropdown(
                choices = ["v1.4", "v1.3", "v1.2"],
                value = "v1.3",
                label = "Model Version",
                info = """
                Model variants based on different functionalities (See detailed info below)
                """
            ),
            gr.Markdown(
                """
                - **v1.4** :  More details and better identity.
                - **v1.3** :  Better quality, natural outputs.
                - **v1.2** :  Sharper outputs with slight beautification of faces.
                """
            )
        ],
        outputs = [
            "image"
        ],
        title = "Sharpen Blurry Memories: Supercharge Your Images with Generative AI (GFPGAN + RealESRGAN)",
        article = "HyperRez, a Python library built by Rauhan Ahmed Siddiqui, utilizes AI's power to upscale and enhance images. Leverage GFPGAN for face restoration and RealESRGAN for background upscaling, all deployed in a GPU-powered Gradio interface for lightning-fast results. Enhance your images like never before!",
    )
    interface.launch(debug = True)
