u=linspace(-4,4,40);
v=linspace(0,pi,40);
[u,v] = meshgrid(u,v);
x = sinh(u).*cos(v);
y =	sinh(u).*sin(v);
z = cosh(u);
surf(x,y,z);
hold on;
x1 = sinh(u).*cos(v);
y1 =	sinh(u).*sin(v);
z1 = -cosh(u);
surf(x1,y1,z1);

xlabel('x');
ylabel('y');
zlabel('z');
subplot (2, 1, 1)
surf(x,y,z);%preenche a figura
subplot (2, 1, 2);
mesh(x,y,z);


