## Introduction 

Below are the key aspects of Histogram of Oriented Gradients (HoG) :-
* HoG focuses on the shape of the feature. It extracts not only gradients but orientation of the pixel as well. Thats what makes this algorithm better than normal edge detection methods
* These gradients and orientations are calculated  by sliding window approach by using a filter
* Finally, histogram of each region is generated separately

## Calculation of HoG
### Preprocessing
Original HoG paper used image width to height ratios as 1:2. So we will use the same values. 
### X and Y gradients
![matrix]("/matrix.png" "matrix")
 

Suppose we are calculating gradients for value 22
* X gradient = 13 - 16 = -3
* Y gradient = 19 - 3 = 16 

The magnitude would be higher when there is a sharp change in intensity, such as around the edges.

### Orientation and Magnitude 
Based on Pythagorum formula, we can define 
* magnitude =  √[(Gx)^2+(Gy)^2]
* orientation = atan(Gy / Gx)

### Histogram Calculation

For histogram calculation, add the contribution of a pixel’s gradient to the bins on either side of the pixel gradient. Higher contribution should be to the bin value which is closer to the orientation.

So, for block size of 8x8 histogram, a matrix of 9x1 is generated.

### Gradient Normalization 

To reduce the lighting effect on image as images are very sensitive towards lighting, normalization is used. A 16x16 block is used to normalize the image. After normalization, we will get a 36x1 vector for each block.

### Feature Calculation 
From an block of 16x16 on image of 64x128, we will get total 7x15 = 105 blocks.

And from normalization step we know that for each block we have a vector of 36x1.

So, we will have 105x36x1 = 3780 total features for image of 64x128 size.

## Repository Desription
* hog.py is used to calculate and and visualize histogram of an image

`python hog.py -i <image_path>` 