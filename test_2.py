def filter_warna(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    mean_px = (r + g + b) / 3
    if abs(max(pixel) - mean_px) < 20:
        return 1
    else:
        return 0

image = [
    [(87,76,63),(67,76,73),(99,105,93),(178,173,189),(48,35,46)],
    [(22,20,18),(10,40,50),(67,76,73),(173,166,167),(87,76,63)],
    [(10,40,50),(99,105,93),(178,173,169),(67,76,73),(22,20,18)],
    [(22,20,18),(87,76,63),(140,132,139),(87,76,63),(99,105,83)],
    [(99,105,93),(87,76,63),(67,76,73),(173,166,167),(48,35,46)]
]

count_colorless = 0
for row in image:
    for pixel in row:
        count_colorless += filter_warna(pixel)
        
if count_colorless > 9:
    print('image is colorless')
else:
    print('image is colorful')

