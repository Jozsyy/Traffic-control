clear all, close all, clc;

%[0, 1.5, 7.4, 0.964, 14.8, 0, 22.2, 0, 29.6, 0, 37, 0, 44.4, 0, 51.8, 0, 59.2, 0, 66.6, 0]
%[0, 1.5, 1.9, 0.964, 10, 0, 15, 0, 20, 0, 30, 0, 40, 0, 50, 0, 70, 0, 80, 0]
[t,y]=ode45(@fuggv,[0,30],[0, 0, 7.4, 0, 14.8, 0, 22.2, 0, 29.6, 0, 37, 0, 44.4, 0, 51.8, 0, 59.2, 0, 66.6, 0]);

figure(1), plot(t,y(:,1),t,y(:,3),t,y(:,5),t,y(:,7),t,y(:,9),t,y(:,11),t,y(:,13),t,y(:,15),t,y(:,17),t,y(:,19)); grid
xlabel("Idő (s)"), ylabel("Pozició (m)")
%text(5,400,"Távolság")


%  figure(2), plot(y(:,3)-y(:,1),y(:,2),y(:,5)-y(:,3),y(:,4),y(:,7)-y(:,5),y(:,6))%,y(:,7),y(:,8),y(:,9),y(:,10),y(:,11),y(:,12),y(:,13),y(:,14),y(:,15),y(:,16),y(:,17),y(:,18),y(:,19),y(:,20)); grid
%  xlabel("Poziciókülönbség (m)"), ylabel("Sebesség (m/s)")

 figure(3), plot(t,y(:,2),t,y(:,4),t,y(:,6),t,y(:,8),t,y(:,10),t,y(:,12),t,y(:,14),t,y(:,16),t,y(:,18),t,y(:,20)); grid
xlabel("Idő (s)"), ylabel("Sebesség (m/s)")

% Gyorsulás kiszámítása numerikusan (dx/dt)
acceleration = diff(y(:, 2:2:end)) ./ diff(t);
% Az időpontokat meg kell hosszabbítani, mivel az diff egy elemmel rövidebb lesz
t_acceleration = (t(1:end-1) + t(2:end)) / 2;

% Gyorsulás ábrázolása
figure(4)
plot(t_acceleration, acceleration);
grid on;
xlabel("Idő (s)"); ylabel("Gyorsulás (m/s^2)");


function dx=fuggv(t,x)
    alfa=0.41;  %erzekenyseg
    lambda=0.5; %erzekenyseg
    k=0.5;  %Ha k=0 akkor FVDM, ha k!=0 akkor FVDAM
    x1 = x(1:2);
    x2 = x(3:4);
    x3 = x(5:6);
    x4 = x(7:8);
    x5 = x(9:10);
    x6 = x(11:12);
    x7 = x(13:14);
    x8 = x(15:16);
    x9 = x(17:18);
    x10 = x(19:20);
    
    %Elso auto a sorban
    dx10(1)=x10(2);
    dx10(2)=exponencialisCsokkeno(t);

    %Maosik auto a sorban
    dx9(1)=x9(2);
    delta_x9=x10(1) - x9(1);
    delta_v9=dx10(1) - dx9(1); %vagy x10(2)-x10(2);
    dx9(2)= alfa * (V(delta_x9) - dx9(1)) + lambda * delta_v9 + k*dx10(2);

    dx8(1)=x8(2);
    delta_x8=x9(1) - x8(1);
    delta_v8=dx9(1) - dx8(1);
    dx8(2)= alfa * (V(delta_x8) - dx8(1)) + lambda * delta_v8 + k*dx9(2);

    dx7(1)=x7(2);
    delta_x7=x8(1) - x7(1);
    delta_v7=dx8(1) - dx7(1);
    dx7(2)= alfa * (V(delta_x7) - dx7(1)) + lambda * delta_v7 + k*dx8(2);

    dx6(1)=x6(2);
    delta_x6=x7(1) - x6(1);
    delta_v6=dx7(1) - dx6(1);
    dx6(2)= alfa * (V(delta_x6) - dx6(1)) + lambda * delta_v6 + k*dx7(2);

    dx5(1)=x5(2);
    delta_x5=x6(1) - x5(1);
    delta_v5=dx6(1) - dx5(1);
    dx5(2)= alfa * (V(delta_x5) - dx5(1)) + lambda * delta_v5 + k*dx6(2);

    dx4(1)=x4(2);
    delta_x4=x5(1) - x4(1);
    delta_v4=dx5(1) - dx4(1);
    dx4(2)= alfa * (V(delta_x4) - dx4(1)) + lambda * delta_v4 + k*dx5(2);

    dx3(1)=x3(2);
    delta_x3=x4(1) - x3(1);
    delta_v3=dx4(1) - dx3(1);
    dx3(2)= alfa * (V(delta_x3) - dx3(1)) + lambda * delta_v3 + k*dx4(2);
    
    dx2(1)=x2(2);
    delta_x2=x3(1) - x2(1);
    delta_v2=dx3(1) - dx2(1);
    dx2(2)= alfa * (V(delta_x2) - dx2(1)) + lambda * delta_v2 + k*dx3(2);
    
    %Tizedik auto a sorban
    dx1(1)= x1(2);
    delta_x1=x2(1) - x1(1);
    delta_v1=dx2(1) - dx1(1);
    dx1(2)= alfa * (V(delta_x1) - dx1(1)) + lambda * delta_v1 + k*dx2(2);

    dx=[dx1(1);dx1(2); dx2(1);dx2(2); dx3(1); dx3(2); dx4(1); dx4(2); dx5(1); dx5(2); dx6(1); dx6(2); dx7(1);dx7(2); dx8(1); dx8(2); dx9(1); dx9(2); dx10(1); dx10(2)];
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
    kezdoErtek = 6; % Kezdeti érték
    csokkenesRata = 0.4; % Csökkenési arány
    
    % Exponenciális csökkenés a kezdeti értékből 0 felé
    a = kezdoErtek * exp(-csokkenesRata * t);
end
