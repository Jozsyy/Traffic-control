clear all, close all, clc;
tspan = 0:0.01:50;
[t,y]=ode45(@fuggv,tspan,[0, 1.5, 1.9, 0.964]);
[t2,y2]=ode45(@fuggv2,tspan,[0, 1.5, 1.9, 0.964]);
[t3,y3]=ode45(@fuggv3,tspan,[0, 1.5, 1.9, 0.964]);
[t4,y4]=ode45(@fuggv4,tspan,[0, 1.5, 1.9, 0.964]);

figure(1), plot(t,y(:,2), t,y2(:,2), t,y3(:,2), t,y4(:,2)); grid
xlabel("Idő (s)"), ylabel("x(2)=dx/dt -> Sebesseg (m/s)")
legend('k=0','k=0.2','k=0.4','k=0.6','Location','northwest')

% Gyorsulás kiszámítása numerikusan (dx/dt)
acceleration = diff(y(:, 2)) ./ diff(t);
% Az időpontokat meg kell hosszabbítani, mivel az diff egy elemmel rövidebb lesz
t_acceleration = (t(1:end-1) + t(2:end)) / 2;

% Gyorsulás ábrázolása
figure(2)
plot(t_acceleration, acceleration); grid on;
xlabel("Idő (s)"); ylabel("(d^2x/dt^2) -> Gyorsulás (m/s^2)"); hold on;

% Gyorsulás kiszámítása numerikusan (dx/dt)
acceleration2 = diff(y2(:, 2)) ./ diff(t);  
plot(t_acceleration, acceleration2);    hold on;
acceleration3 = diff(y3(:, 2)) ./ diff(t);
plot(t_acceleration, acceleration3);    hold on;
acceleration4 = diff(y4(:, 2)) ./ diff(t);
plot(t_acceleration, acceleration4);
legend('k=0','k=0.2','k=0.4','k=0.6','Location','northwest')



figure(3), plot(y(:,3)-y(:,1),y(:,4))%,y2(:,3)-y2(:,1),y2(:,4),y3(:,3)-y3(:,1),y3(:,4),y4(:,3)-y4(:,1),y4(:,4))
xlabel("x(1) -> Pozicio kulonbseg (m)"), ylabel("x(2)=dx -> Sebesseg (m/s)")

figure(4), plot(t,y(:,1), t,y(:,3)), grid on
xlabel("Idő (s)"), ylabel(" pozicio")
legend('k=0')

function dx=fuggv(t,x)
    alfa=0.41;  %erzekenyseg
    lambda=0.5; %erzekenyseg
    k=0;  %Ha k=0 akkor FVDM, ha k!=0 akkor FVDAM
    x1 = x(1:2);
    x2 = x(3:4);
    
    dx2(1)=x2(2);
    dx2(2)=2;

    dx1(1)=x1(2);
    delta_x1=x2(1) - x1(1);
    delta_v1=dx2(1) - dx1(1);
    dx1(2)= alfa * (V(delta_x1) - dx1(1)) + lambda * delta_v1 + k*dx2(2);

    dx=[dx1(1);dx1(2); dx2(1);dx2(2)];
end

function dx=fuggv2(t,x)
    alfa=0.41;  %erzekenyseg
    lambda=0.5; %erzekenyseg
    k=0.2;  %Ha k=0 akkor FVDM, ha k!=0 akkor FVDAM
    x1 = x(1:2);
    x2 = x(3:4);
    
    dx2(1)=x2(2);
    dx2(2)=2;

    dx1(1)=x1(2);
    delta_x1=x2(1) - x1(1);
    delta_v1=dx2(1) - dx1(1);
    dx1(2)= alfa * (V(delta_x1) - dx1(1)) + lambda * delta_v1 + k*dx2(2);

    dx=[dx1(1);dx1(2); dx2(1);dx2(2)];
end

function dx=fuggv3(t,x)
    alfa=0.41;  %erzekenyseg
    lambda=0.5; %erzekenyseg
    k=0.4;  %Ha k=0 akkor FVDM, ha k!=0 akkor FVDAM
    x1 = x(1:2);
    x2 = x(3:4);
    
    dx2(1)=x2(2);
    dx2(2)=2;

    dx1(1)=x1(2);
    delta_x1=x2(1) - x1(1);
    delta_v1=dx2(1) - dx1(1);
    dx1(2)= alfa * (V(delta_x1) - dx1(1)) + lambda * delta_v1 + k*dx2(2);

    dx=[dx1(1);dx1(2); dx2(1);dx2(2)];
end

function dx=fuggv4(t,x)
    alfa=0.41;  %erzekenyseg
    lambda=0.5; %erzekenyseg
    k=0.6;  %Ha k=0 akkor FVDM, ha k!=0 akkor FVDAM
    x1 = x(1:2);
    x2 = x(3:4);
    
    dx2(1)=x2(2);
    dx2(2)=2;

    dx1(1)=x1(2);
    delta_x1=x2(1) - x1(1);
    delta_v1=dx2(1) - dx1(1);
    dx1(2)= alfa * (V(delta_x1) - dx1(1)) + lambda * delta_v1 + k*dx2(2);

    dx=[dx1(1);dx1(2); dx2(1);dx2(2)];
end

%Optimalis sebesseg 
function vs=V(delta_xn)
    v1=6.75;    %m/s
    v2=7.91;    %m/s
    c1=0.13;    %1/m
    c2=1.57; 
    lc=5;   %m

    vs=v1+v2*tanh(c1*(delta_xn-lc)-c2);
end

function a = exponencialisCsokkeno(t)
    % A függvény paraméterei
    kezdoErtek = 2; % Kezdeti érték
    csokkenesRata = 0.5; % Csökkenési arány
    
    % Exponenciális csökkenés a kezdeti értékből 1 felé
    a = kezdoErtek * exp(-csokkenesRata * t);
end


