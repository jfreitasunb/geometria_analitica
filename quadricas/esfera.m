u=linspace(0,pi,40);
v=linspace(0,2*pi,40);
[u,v] = meshgrid(u,v);
x = sin(u).*cos(v);
y =	sin(u).*sin(v);
z = cos(u);
surf(x,y,z);
print("esfera.pdf", "-dpdf");
mesh(x,y,z);
print("esfera-contornos.pdf", "-dpdf");


