import fractal, bmp

pixels = fractal.mandelbrot(448, 256)
print(pixels)

bmp.write_grayscale("mandel.bmp", pixels)
