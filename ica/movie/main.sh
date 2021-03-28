ffmpeg -i ../mix1.wav -i ../mix2.wav -filter_complex amerge=inputs=2 Mix.wav -y
ffmpeg -i person1.png -i person2.png -filter_complex hstack image.png -y
ffmpeg -loop 1 -i image.png -i Mix.wav -t 2.0 output.mp4 -y
