function a = invmatrix(X)
new_matrix = []
for line = X
    new_matrix = [new_matrix; X]
end
a = inv(X);