E = 69e9;
LENGTH = 30;
I = 0.0032;

MASS1 = 4000;
MASS2 = 6000;
MASS3 = 5000;
MASS4 = 3000;
MASS5 = 1000;

k1 = calculateStiffness(0.1*LENGTH, E , I);
k2 = calculateStiffness(0.2*LENGTH, E, I);
k3 = calculateStiffness(0.2*LENGTH, E, I);
k4 = calculateStiffness(0.25*LENGTH, E, I);
k5 = calculateStiffness(0.25*LENGTH, E , I);


MASS_MATRIX = [
    MASS1 0 0 0 0;
    0 MASS2 0 0 0;
    0 0 MASS3 0 0;
    0 0 0 MASS4 0;
    0 0 0 0 MASS5;
];

STIFFNESS_MATRIX = [
    k2+k1 -k2 0 0 0;
    -k2 k3+k2 -k3 0 0;
    0 -k3 k4+k3 -k4 0;
    0 0 -k4 k5+k4 -k5;
    0 0 0 -k5 k5
];

% V --> Eigen Vector
% D --> Eigen Value
[V , D] = eig(STIFFNESS_MATRIX, MASS_MATRIX);


natural_freq = sqrt(D)/(2*pi);

disp(natural_freq);




function [k] = calculateStiffness(LENGTH, E , I)
k = (3*E*I)/(LENGTH^3);
end