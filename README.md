# binary-image
img.🖼

## Presentation
[Google Slides](https://docs.google.com/presentation/d/1FvD-HUjSb7XyvyUZqgzm-19n-88lS7RXcrUrqMsy2mI/edit?usp=sharing)

## Compressions steps:
- [x] Save channels as YCbCr as opposed to RGB
- [x] Save a whole channel at a time instead of per pixel
- [x] Downsample the Cb and Cr channels to 1/2 size in checkerboard pattern
- [ ] Perform polynomial regression on the remaining pixels (Cb and Cr)
- [ ] Run rescaled image through an AI model that resharpens the image
