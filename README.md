!!!!!!! READ FIRST !!!!!!!!

Very simple ComfyUI script that CLEARS input folder (should clear additional paths set as input folders too) every time the server starts (it will leave files that you specify inside the code). Put main.py (can rename to whatever) or folder inside ComfyUI/custom_nodes folder. Why use it? Because comfy will create a copy of every file that you load or copy-paste even if it's already inside input folder.

Set filenames here:

![image](https://github.com/Gwynennen/ComfyUI_clear_inputFolder_onRun/assets/96996569/77e24706-1f5f-4afc-ac4e-a0d466400bad)

Notes:
- consider creating copy of important files for first time use;
- server cli will show import fail but it worked when tested;
