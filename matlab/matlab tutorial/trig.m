i = 0;
for t=0:pi/180:2*pi
    i = i + 1;
    y(i) = sin(t);
    z(i) = cos(t);
end
plot(y);
axis([0 360 -1 1]);
hold;
plot(z, ':');
axis([0 360 -1 1]);
xlabel('Degree');
ylabel('Magnitude');
title('Sine and Cosine Function');
grid;
gtext('sin(t)');
gtext('cos(t)');