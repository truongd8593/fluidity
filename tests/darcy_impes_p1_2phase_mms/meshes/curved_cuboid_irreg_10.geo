lx = 1.0;
ly = 1.2;
lz = 0.8;
dx = 0.1;
sqrt2 = 1.4142135623730951;

Point(1) = {  0,  0,  0, dx};
Point(2) = { lx,  0,  0, dx};
Point(3) = { lx, ly,  0, dx};
Point(4) = {  0, ly,  0, dx};
Point(5) = {  0,  0, lz, dx};
Point(6) = { lx,  0, lz, dx};
Point(7) = { lx, ly, lz, dx};
Point(8) = {  0, ly, lz, dx};

Point(11) = {  lx/2,  -lx,  0, dx};
Point(12) = { lx+ly, ly/2,  0, dx};
Point(13) = {  lx/2,    0,  0, dx};
Point(14) = {    lx, ly/2,  0, dx};
Point(15) = {  lx/2,  -lx, lx, dx};
Point(16) = { lx+ly, ly/2, lx, dx};
Point(17) = {  lx/2,    0, lx, dx};
Point(18) = {    lx, ly/2, lx, dx};

Point(21) = {   -lz/sqrt2,    lz/sqrt2, lz/2, dx};
Point(22) = { lx-lz/sqrt2,    lz/sqrt2, lz/2, dx};
Point(23) = { lx-lz/sqrt2, ly+lz/sqrt2, lz/2, dx};
Point(24) = {   -lz/sqrt2, ly+lz/sqrt2, lz/2, dx};

Circle(1) = {1, 11, 2};
Circle(2) = {2, 12, 3};
Circle(3) = {3, 13, 4};
Circle(4) = {4, 14, 1};
Circle(5) = {5, 15, 6};
Circle(6) = {6, 16, 7};
Circle(7) = {7, 17, 8};
Circle(8) = {8, 18, 5};
Circle(9) = {1, 21, 5};
Circle(10) = {2, 22, 6};
Circle(11) = {3, 23, 7};
Circle(12) = {4, 24, 8};

Line Loop(21) = {1, 2, 3, 4};
Line Loop(22) = {5, 6, 7, 8};
Line Loop(23) = {10, 6, -11, -2};
Line Loop(24) = {9, -8, -12, 4};
Line Loop(25) = {9, 5, -10, -1};
Line Loop(26) = {12, -7, -11, 3};

Ruled Surface(21) = {21};
Ruled Surface(22) = {22};
Ruled Surface(23) = {23};
Ruled Surface(24) = {24};
Ruled Surface(25) = {25};
Ruled Surface(26) = {26};

Surface Loop(34) = {26, 24, 25, 22, 23, 21};
Volume(1) = {34};

Physical Surface(1) = {24};	// xmin
Physical Surface(2) = {23};	// xmax
Physical Surface(3) = {25};	// ymin
Physical Surface(4) = {26};	// ymax
Physical Surface(5) = {21};	// zmin
Physical Surface(6) = {22};	// zmax
Physical Volume(7) = {1};