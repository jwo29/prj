function r = GetRadar(dt)
%
%
persistent posp


if isempty(posp)
    posp = 0;
end


vel = 100 + 5*randn;
alt = 1000 + 10*randn;

pos = posp + vel*dt;

v = 0 + pos*0.05*randn; % 측정 오류

r = sqrt(pos^2 + alt^2) + v; % 측정값

posp = pos;