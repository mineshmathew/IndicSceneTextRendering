# Generating Synthetic Word Images for training Indian Scripts Scene Text OCR
This repo  provides a script we used to generate scene text style synthetic word images for a work concering scene text recognition in Indian scripts.
Along with the rendering script we also provide, a collection of fonts we compiled for the project.
Better not to use the rendering script in this repo for rendering English/Latin. The python script invokes bash commands (using *os.system()*) which is generally not recommended and there are multiple Disk I/O operations which makes the rendering slow. We had to render in this way since rendering with common tools/libraries resulted in incorrect ordering of certain Unicode glyphs in Indian Scripts.



We encourate you to use this script for non Latin scripts where you want to use Unicode fonts and especially in cases where you have difficulty rendeirng Unicode text correctly while using commonly used libraries for font rendering.


![Sample Synthetic Images rendered using the script given here](https://github.com/mineshmathew/SyntheticWordImagesGenerationIndianScripts/blob/master/IL_synth.png?raw=true)

Shown above is a few sample word images we rendered for our work using the rendering script.

Please cite the following work if you use the rendering script.


```
@INPROCEEDINGS{
  IL-SCENETEXT_MINESH,
  author={M. {Mathew} and M. {Jain} and C. V. {Jawahar}},
  booktitle={ICDAR MOCR Workshop}, 
  title={Benchmarking Scene Text Recognition in Devanagari, Telugu and Malayalam}, 
  year={2017}}

```
We used the same script for our work on Arabic Scene text recognition, titled [Unconstrained scene text and video text recognition for arabic script](https://cvit.iiit.ac.in/research/projects/cvit-projects/arabic-text-recognition)
## Fonts
Fonts need to be installed  on the machine where you render the images. Easiest option is to copy fonts to .fonts directory in your home directory and then run `fc-cache` command from terminal.
Rendering using Pango + IM , require that a font is  installed.
Wee use Pango since none of the tools/libraries which we tried out  back then could render Indian scripts correctly. The ordering of Unicodes were getting messed up with other libraries.<br>


Use `fc-list` command in Unix to get the font list and the fontnames in this list must be the ones you use with the rendering script
Font lists we created using `fc-list` command are given inside the fontlists directory.


## Rendering Script

`render_Indian_language_scenetext.py` takes command line arguments (see the script)
Make sure you have Pango, Cairo , PangoCairo and Imagemagick Installed in your Unix machine.
For a good introduction on using Pango with IM for rendering text as images please refer to this  [manual](https://legacy.imagemagick.org/Usage/text/#pango).
While rendering we use crops of random natural images as background images of the rendered word images. We used images from [Places Dataset](http://places.csail.mit.edu/). You are free to use images of your choice.
The rendering parameters, alpha blending setting  and   of foreground and backhround colors are set so that resutlant images are mostly legible. We dont guarantee that these settings are the best to obtain the most diverse set of images which closely match with the real scene text images. We request the users to review these settings before rendering images for your task.


## Disclaimer
The font  collection was compiled for a reserach project. No commercial interests involved.
Copyrights of the fonts is with the original developers of the fonts. The fonts are uploaded here with the sole purpose of helping researchers to generate synthetic data to train OCRs in Indian scripts. By downloading any of the fonts   you explicitly state that your final purpose is to perform non-commercial research in the conditions mentioned above and you agree to comply with these terms and conditions. For any other uses we request you to get explicit permission from the font developer.
