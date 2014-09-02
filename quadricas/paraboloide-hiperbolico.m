u=linspace(-2,2,40);
v=linspace(-2,2,40);
[u,v] = meshgrid(u,v);
x = u;
y =	v;
z = u.*v;
surf(x,y,z);
hold on;
xlabel('x');
ylabel('y');
zlabel('z');
subplot (2, 1, 1)
surf(x,y,z);%preenche a figura
subplot (2, 1, 2);
mesh(x,y,z);


