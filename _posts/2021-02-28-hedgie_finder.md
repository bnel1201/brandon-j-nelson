---
title: HedgieFinder, a tiny ML project for a tiny hedgehog
toc: true
layout: post 
hide: false 
categories: [machine learning]
---


![xiaomi]({{ site.baseurl }}/images/hedgiefinder/xiaomi.JPG)

I'd like to share a weekend project that demonstrates how the basic steps of a machine learning project including:

  1. setting up a dataset
  2. model training
  3. inference as a command line program
  4. some sample anaylsis with the results

Please enjoy the code and included videos should you want to reproduce the results or experiment on your own!

- Everything can be found here: **[github.com/bnel1201/hog_finder](https://github.com/bnel1201/hog_finder)**

## Making the dataset

### Raw Data

All videos were recorded from our night vision baby monitor camera, that we've adapted to monitor our hedgehog at night. The camera allows `.mp4` video downloads.

- using [convert_video.bat](convert_videos.bat) these `.mp4` videos were converted into a series of `.png` images

### Generating Ground Truth Annotations

Using the `.png` image files hand annotations highlighting the location of our hedgehog Xiaomi were done with [slicer](https://www.slicer.org/). A single region covering her whole body was generated and exported as a `.nrrd` file.

![slicer annotation]({{ site.baseurl }}/images/hedgiefinder/slicer_annotation.jpg)

The `.nrrd` annotations were then converted to `.png` files for training using [prepare_dataset.py](https://github.com/bnel1201/hog_finder/blob/main/segmentation/prepare_dataset.py). Note I added a morphological [dilation step](https://scikit-image.org/docs/dev/api/skimage.morphology.html) to make a 2nd region which includes an outline for easier visualization of her location. This dataset was then used for subsequent training.

## Automated Segmentation

### [model training]([segmentation/segmentation_train.ipynb](https://github.com/bnel1201/hog_finder/blob/main/segmentation/segmentation_train.ipynb))

- The current version utilizes transfer learning and data augmentation with [the fastai library](https://docs.fast.ai/tutorial.vision.html) to train a segmentation model with a small hand-annotated dataset

### [model inference]([segmentation/inference.py](https://github.com/bnel1201/hog_finder/blob/main/segmentation/inference.py))

- turned into a command line program using [hedgiefinder](https://github.com/bnel1201/hog_finder/blob/main/segmentation/hedgiefinder.py):

```bash
python segmentation/hogfinder.py path/to/hedgehog_video.mp4
```

![finder gif]({{ site.baseurl }}/images/hedgiefinder/hog_finder.gif)

- gif made with [make_preview_gif.bat](segmentation/make_preview_gif.bat)

### Analysis

- using the segmentation maps generated with [hedgiefinder](https://github.com/bnel1201/hog_finder/blob/main/segmentation/hedgiefinder.py), Xiaomi's location over time can be tracked as the coordinates (x, y) at the center of each segmentation, (found using [sci-kit image regionprops](https://scikit-image.org/docs/dev/api/skimage.measure.html))
  - [label_centers](https://github.com/bnel1201/hog_finder/blob/main/center_of_mass/label_centers.py) is the relevant script for finding these coordinates
  - Finally, the sum of all these points over time is overlaid across a single from using [[where_is_xiaomi.py](https://github.com/bnel1201/hog_finder/blob/main/center_of_mass/where_is_xiaomi.py) to get a heat map of the night's activity

![hedhedgehog activity map]({{ site.baseurl }}/images/hedgiefinder/xiaomi_map_1.png)
