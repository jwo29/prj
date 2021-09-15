function [volt, Px, K] = SimpleKalman2(z) % 측정값을 매개변수로 받음
%
%
persistent A H Q R % 시스템 변수
persistent x Px % 추정값과 오차 공분산
persistent firstRun

if isempty(firstRun)
    A = 1;
    H = 1;
    
    Q = 0; % 시스템 잡음 w에 대한 공분산
    R = 4; % 측정 잡음 v에 대한 공분산
    
    x = 14;
    Px = 6;
    
    firstRun = 1;
end

xp = A*x; % 추정값 예측
Pp = A*Px*A' + Q; % 오차 공분산 예측

K = Pp*H'/(H*Pp*H' + R); % 칼만 이득 계산

x = xp + K*(z - H*xp); % 추정값 계산
Px = Pp - K*H*Pp; % 오차 공분산 계산

volt = x; % 추정값 반환