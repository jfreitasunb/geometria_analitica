u=linspace(-2,2,40);
v=linspace(0,2*pi,40);
[u,v] = meshgrid(u,v);
x = cosh(u).*cos(v);
y = cosh(u).*sin(v);
z = sinh(u);
hold on;
xlabel('x');
ylabel('y');
zlabel('z');
subplot (2, 1, 1)
surf(x,y,z);%preenche a figura
subplot (2, 1, 2);
mesh(x,y,z);