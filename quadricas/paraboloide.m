u=linspace(0,2,40);
v=linspace(0,2*pi,40);
h = 1;
[u,v] = meshgrid(u,v);
x = sqrt(u.*1/h).*cos(v);
y =	sqrt(u.*1/h).*sin(v);
z = u;
surf(x,y,z);
hold on;
xlabel('x');
ylabel('y');
zlabel('z');
subplot (2, 1, 1)
surf(x,y,z);%preenche a figura
subplot (2, 1, 2);
mesh(x,y,z);


view(b,90-a);
print("filename.pdf", "-dpdf");
