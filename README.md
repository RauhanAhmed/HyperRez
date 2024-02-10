
# HyperRez: Sharpen Blurry Memories


Enhance and upscale your images effortlessly with HyperRez, a Python library crafted by Rauhan Ahmed Siddiqui. Leveraging the power of GFPGAN and RealESRGAN, state-of-the-art Generative Adversarial Networks, this library provides advanced image enhancement capabilities. Real-ESRGAN focuses on upscaling backgrounds, while GFPGAN excels in refining the faces of human subjects.


## Features

- **Dual Network Integration:** Combines Real-ESRGAN and GFPGAN for comprehensive image enhancement.
- **Gradio Interface:** Seamlessly deployed into production using Gradio Interface for an interactive and user-friendly experience.
- **GPU Acceleration:** Optimized for GPU processing, ensuring fast and efficient image enhancement (Note: Performance may be suboptimal on CPUs).
- **PyPI Integration:** Available on PyPI as the "HyperRez" library for easy installation and use.


## Screenshots

![App Screenshot](https://i.ibb.co/wRTQwrt/Beige-and-White-Be-Yourself-Square-Pillow-2.png)

![App Screenshot](https://i.ibb.co/VLsXqY6/Screenshot-2024-02-11-005136.png)

![App Screenshot](https://i.ibb.co/BBKh0BR/Screenshot-2024-02-11-005236.png)

## Installation
```bash
  pip install HyperRez
```
    
## Usage

```python
from HyperRez import ImageUpscaler

# Initialise the upscaler
upscaler = ImageUpscaler()

# Launch the Gradio Interface
upscaler.launchInterface()
```


## Authors

[Rauhan Ahmed Siddiqui](https://linkedin.com/in/rauhan-ahmed/)


## License

[MIT](https://choosealicense.com/licenses/mit/)
