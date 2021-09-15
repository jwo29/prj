scores = [77 66 72 75 90 86 58 98 89 59]
count = 0;
n = 0;
while n < length(scores)
    n = n + 1;
    if scores(n) > mean(scores)
        count = count + 1;
    end
end
display(scores)
display(n)
display(count)