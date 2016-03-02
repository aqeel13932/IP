function f = lanczos4(x)
f = (sin(pi*x) .* sin(pi*x/4) + eps) ./ ((pi^2 * x.^2 / 4) + eps);
f = f .* (abs(x) <4);
end