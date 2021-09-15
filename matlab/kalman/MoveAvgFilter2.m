function avg = MoveAvgFilter2(x)
%
%
persistent n xbuf
persistent firstRun

if isempty(firstRun)
    n = 10;
    xbuf = x*ones(n, 1);n
    
    firstRun = 1
end

for m=1:n-1
    xbuf(m) = xbuf(m+1);
end
xbuf(n) = x;

avg = sum(xbuf) / n;