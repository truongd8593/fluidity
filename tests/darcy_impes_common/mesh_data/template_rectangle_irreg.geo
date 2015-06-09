lx = $DOMAIN_LENGTH_X;
ly = $DOMAIN_LENGTH_Y;
dx = $EL_SIZE_X;

Point(1) = {  0,  0, 0, dx};
Point(2) = { lx,  0, 0, dx};
Point(3) = { lx, ly, 0, dx};
Point(4) = {  0, ly, 0, dx};
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};
Line Loop(9) = {1, 2, 3, 4};
Plane Surface(10) = {9};

Physical Line(1) = {4}; 	// xmin
Physical Line(2) = {2}; 	// xmax
Physical Line(3) = {1}; 	// ymin
Physical Line(4) = {3}; 	// ymax
Physical Surface(5) = {10};
