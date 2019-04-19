From the directory where setup.sh is present, run: 'sh setup.sh'. This script downloads the stage-5.pth file and moves it to model_data/models. The stage-5.pth is the model weights file but it is heavy (around 100mb) and hence I am providing the download link for that. Please make sure that the models folder has stage1.pth after the script finishes running.
The script also installs the fastai deep learning library which the application requires. It just uses the command: pip install fastai==1.0.47
Now, please cd into the gui folder and run “python gui.py” as shown in the video (https://www.youtube.com/watch?v=8zwNPAdJ-oQ)
A demo xray image can be found inside the gui folder. Please use it to test.
