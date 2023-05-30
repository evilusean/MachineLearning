Stable Diffusion: </br>
https://stablediffusionweb.com/ </br>
PyTriton: </br>
https://github.com/triton-inference-server/pytriton </br>
HuggingFace: </br>
https://github.com/triton-inference-server/tutorials/tree/main/HuggingFace </br>
https://www.youtube.com/watch?v=JgP2WgNIq_w </br>

Stable Diffusion is an AI art text to image generation model; it takes text input and generates some kind of image </br>
PyTriton from NVidia is a Flask Framework/Library that is a wrapper around their serverand allows you to run Stable Diffusion (or any machine learning model) locally,
on your own machine. Has many of the features prebuilt into the flask application that you won't need to manually code before launching a model, also scalable. </br>
Requires Linux. WSL(Windows Subsystem for Linux) </br>
https://medium.com/htc-research-engineering-blog/nvidia-docker-on-wsl2-f891dfe34ab </br>
https://www.youtube.com/watch?v=6sUDDsHVM90 </br>

Requirements:
pip install nvidia-triton </br>
pip install torch </br>
pip install diffusers </br>
pip install transformers </br>
pip install torch-vision </br>
