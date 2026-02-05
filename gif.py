import imageio.v3 as iio

#Put your image path names in the list below
file_names = ['frame_00_delay-0.1s.gif', 'frame_01_delay-0.1s.gif', 
              'frame_02_delay-0.1s.gif', 'frame_03_delay-0.1s.gif', 
              'frame_04_delay-0.1s.gif', 'frame_05_delay-0.1s.gif',
              'frame_06_delay-0.1s.gif', 'frame_07_delay-0.1s.gif',
              'frame_08_delay-0.1s.gif', 'frame_09_delay-0.1s.gif',]
images = []

for filename in file_names:
    images.append(iio.imread(filename, index=0))

iio.imwrite("evernight.gif", images, duration = 95, loop = 0)

