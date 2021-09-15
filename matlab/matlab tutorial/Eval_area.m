function area = Eval_area(r)
circle = pi*r^2;
circle_area = 2*circle;
l = 2*r;
w = 4*r;
rect = w*l;
area = rect - circle_area
end