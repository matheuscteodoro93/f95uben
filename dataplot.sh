echo > gnuplot.in 
for FILE in output/*; do
 echo "set term png" >> gnuplot.in
 echo "set output \"${FILE}.png\"" >> gnuplot.in
 echo "splot \"${FILE}\" u 1:2:3 w l" >> gnuplot.in
 echo \"${FILE}\" 
done
gnuplot gnuplot.in
ffmpeg -r 12 -i output/%d.png -vcodec libx264 -y -an video.mp4 -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2"
rm output/*.png

