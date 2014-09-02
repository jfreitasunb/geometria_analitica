u=linspace(0,2*pi,40);
v=linspace(0,pi,40);
[u,v] = meshgrid(u,v);
x = 3*cos(u).*sin(v);
y =	2*sin(u).*sin(v);
z = 4*cos(v);
surf(x,y,z);
print("elipsoide.pdf", "-dpdf");
mesh(x,y,z);
print("elipsoide-contornos.pdf", "-dpdf");




p1=linspace(0,%pi,40);
p2=linspace(0,2*%pi,40);
deff("[x,y,z]=scp(p1,p2)",["x=cos(p1).*sin(p2)";..
                           "y=sin(p1).*sin(p2)";..
                           "z=cos(p2)"])
[Xf,Yf,Zf]=eval3dp(scp,p1,p2);
plot3d(Xf,Yf,Zf,theta = 60, alpha = 80)