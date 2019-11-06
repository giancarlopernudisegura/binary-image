# binary-image
img.🖼

## Compressions steps:
- [ ] Save channels as YCbCr as opposed to RGB
- [ ] Save a whole channel at a time instead of per pixel
- [ ] Downsample the Cb and Cr channels to 1/2 size in checkerboard pattern
- [ ] Perform polynomial regression on the remaining pixels (Cb and Cr)
- [ ] Run rescaled image through an AI model that resharpens the image
