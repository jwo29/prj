function [L, P] = field(W, A)
L = (A-W.^2/8)./W;
P = 2*L+W+2*W/sqrt(2);
end