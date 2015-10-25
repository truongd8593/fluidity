# THIS FILE HAS BEEN AUTOMATICALLY GENERATED.

from numpy import sin, cos, pi, exp, sqrt

py_dict = {
    "domain_extents" : (1.0, 1.2, 0.8, ),

    "finish_time" : 1.0,

    "pressure_scale" : 1000.0,

    "saturation_scale" : 0.5,

    "gravity_magnitude" : 1.0,

    "viscosity1" : 1.725e-05,

    "viscosity2" : 0.001,

    "density1" : 1.284,

    "density2" : 1000.0,

    "permeability1" : lambda (s1, s2): 1.567346939e-9*(s1 - 0.2)**2,

    "permeability2" : lambda (s1, s2): 1.567346939e-9*(s2 - 0.3)**2,

    "porosity" : 0.4,

    "absolute_permeability" : 1.567346939e-09,

    "gravity_direction_1D" : 1,

    "pressure1_1D" : lambda x, t: (250.0*cos(pi*t) + 750.0)*cos(pi*x),

    "saturation1_1D" : lambda x, t: 1. - 0.5*exp(-1.0*x)/(1.0*t + 1.),

    "pressure2_1D" : lambda x, t: (250.0*cos(pi*t) + 750.0)*cos(pi*x),

    "saturation2_1D" : lambda x, t: 0.5*exp(-1.0*x)/(1.0*t + 1.),

    "darcy_velocity1_x_1D" : lambda x, t: -9.0860692115942e-5*(0.8 - 0.5*exp(-1.0*x)/(1.0*t + 1.))**2*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x) - 1.284),

    "darcy_velocity1_magnitude_1D" : lambda x, t: 9.0860692115942e-5*sqrt((0.8 - 0.5*exp(-1.0*x)/(1.0*t + 1.))**4*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x) - 1.284)**2),

    "source_saturation1_1D" : lambda x, t: 9.0860692115942e-5*pi**2*(0.8 - 0.5*exp(-1.0*x)/(1.0*t + 1.))**2*(250.0*cos(pi*t) + 750.0)*cos(pi*x) - 9.0860692115942e-5*(0.8 - 0.5*exp(-1.0*x)/(1.0*t + 1.))*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x) - 1.284)*exp(-1.0*x)/(1.0*t + 1.) + 0.2*exp(-1.0*x)/(1.0*t + 1.)**2,

    "darcy_velocity2_x_1D" : lambda x, t: -1.567346939e-6*(-0.3 + 0.5*exp(-1.0*x)/(1.0*t + 1.))**2*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x) - 1000.0),

    "darcy_velocity2_magnitude_1D" : lambda x, t: 1.567346939e-6*sqrt((-0.3 + 0.5*exp(-1.0*x)/(1.0*t + 1.))**4*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x) - 1000.0)**2),

    "source_saturation2_1D" : lambda x, t: 1.567346939e-6*pi**2*(-0.3 + 0.5*exp(-1.0*x)/(1.0*t + 1.))**2*(250.0*cos(pi*t) + 750.0)*cos(pi*x) + 1.567346939e-6*(-0.3 + 0.5*exp(-1.0*x)/(1.0*t + 1.))*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x) - 1000.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.2*exp(-1.0*x)/(1.0*t + 1.)**2,

    "gravity_direction_2D" : (1, 0, ),

    "pressure1_2D" : lambda x, y, t: (250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*cos(pi*x),

    "saturation1_2D" : lambda x, y, t: -0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1,

    "pressure2_2D" : lambda x, y, t: (250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*cos(pi*x),

    "saturation2_2D" : lambda x, y, t: 0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.),

    "darcy_velocity1_x_2D" : lambda x, y, t: -9.0860692115942e-5*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y) - 1.284)*(-0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**2,

    "darcy_velocity1_y_2D" : lambda x, y, t: -7.57172434299517e-5*pi*(-0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*cos(pi*x)*cos(0.833333333333333*pi*y),

    "darcy_velocity1_magnitude_2D" : lambda x, y, t: sqrt(8.25566537178801e-9*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y) - 1.284)**2*(-0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**4 + 5.73310095263056e-9*pi**2*(-0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**4*(250.0*cos(pi*t) + 750.0)**2*cos(pi*x)**2*cos(0.833333333333333*pi*y)**2),

    "source_saturation1_2D" : lambda x, y, t: -0.000141969831431159*y**2*(-2.5*y + 3.0)*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y) - 1.284)*(-0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)*exp(-1.0*x)/(1.0*t + 1.) + 0.3125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.)**2 - 7.57172434299517e-5*pi*(3.90625*y**2*exp(-1.0*x)/(1.0*t + 1.) - 3.125*y*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(-0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)*(250.0*cos(pi*t) + 750.0)*cos(pi*x)*cos(0.833333333333333*pi*y) + 0.000153958394974235*pi**2*(-0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*cos(pi*x),

    "darcy_velocity2_x_2D" : lambda x, y, t: -1.567346939e-6*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y) - 1000.0)*(0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**2,

    "darcy_velocity2_y_2D" : lambda x, y, t: -1.30612244916667e-6*pi*(0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*cos(pi*x)*cos(0.833333333333333*pi*y),

    "darcy_velocity2_magnitude_2D" : lambda x, y, t: sqrt(2.45657642719267e-12*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y) - 1000.0)**2*(0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**4 + 1.70595585221713e-12*pi**2*(0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**4*(250.0*cos(pi*t) + 750.0)**2*cos(pi*x)**2*cos(0.833333333333333*pi*y)**2),

    "source_saturation2_2D" : lambda x, y, t: 2.4489795921875e-6*y**2*(-2.5*y + 3.0)*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y) - 1000.0)*(0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)*exp(-1.0*x)/(1.0*t + 1.) - 0.3125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.)**2 - 1.30612244916667e-6*pi*(-3.90625*y**2*exp(-1.0*x)/(1.0*t + 1.) + 3.125*y*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)*(250.0*cos(pi*t) + 750.0)*cos(pi*x)*cos(0.833333333333333*pi*y) + 2.65578231330556e-6*pi**2*(0.78125*y**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*cos(pi*x),

    "gravity_direction_3D" : (1, 0, 0, ),

    "pressure1_3D" : lambda x, y, z, t: (250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z)*cos(pi*x),

    "saturation1_3D" : lambda x, y, z, t: -2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 1,

    "pressure2_3D" : lambda x, y, z, t: (250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z)*cos(pi*x),

    "saturation2_3D" : lambda x, y, z, t: 2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.),

    "darcy_velocity1_x_3D" : lambda x, y, z, t: -9.0860692115942e-5*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z) - 1.284)*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**2,

    "darcy_velocity1_y_3D" : lambda x, y, z, t: -7.57172434299517e-5*pi*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*sin(1.25*pi*z)*cos(pi*x)*cos(0.833333333333333*pi*y),

    "darcy_velocity1_z_3D" : lambda x, y, z, t: -0.000113575865144928*pi*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*cos(pi*x)*cos(1.25*pi*z),

    "darcy_velocity1_magnitude_3D" : lambda x, y, z, t: sqrt(8.25566537178801e-9*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z) - 1.284)**2*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**4 + 1.28994771434188e-8*pi**2*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**4*(250.0*cos(pi*t) + 750.0)**2*sin(0.833333333333333*pi*y)**2*cos(pi*x)**2*cos(1.25*pi*z)**2 + 5.73310095263056e-9*pi**2*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**4*(250.0*cos(pi*t) + 750.0)**2*sin(1.25*pi*z)**2*cos(pi*x)**2*cos(0.833333333333333*pi*y)**2),

    "source_saturation1_3D" : lambda x, y, z, t: -0.00049911268862517*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z) - 1.284)*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)*exp(-1.0*x)/(1.0*t + 1.) + 1.0986328125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.)**2 - 0.000113575865144928*pi*(20.599365234375*y**2*z**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 10.986328125*y**2*z*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*cos(pi*x)*cos(1.25*pi*z) - 7.57172434299517e-5*pi*(13.73291015625*y**2*z**2*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 10.986328125*y*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)*(250.0*cos(pi*t) + 750.0)*sin(1.25*pi*z)*cos(pi*x)*cos(0.833333333333333*pi*y) + 0.000295928226405395*pi**2*(-2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z)*cos(pi*x),

    "darcy_velocity2_x_3D" : lambda x, y, z, t: -1.567346939e-6*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z) - 1000.0)*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**2,

    "darcy_velocity2_y_3D" : lambda x, y, z, t: -1.30612244916667e-6*pi*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*sin(1.25*pi*z)*cos(pi*x)*cos(0.833333333333333*pi*y),

    "darcy_velocity2_z_3D" : lambda x, y, z, t: -1.95918367375e-6*pi*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*cos(pi*x)*cos(1.25*pi*z),

    "darcy_velocity2_magnitude_3D" : lambda x, y, z, t: sqrt(2.45657642719267e-12*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z) - 1000.0)**2*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**4 + 3.83840066748855e-12*pi**2*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**4*(250.0*cos(pi*t) + 750.0)**2*sin(0.833333333333333*pi*y)**2*cos(pi*x)**2*cos(1.25*pi*z)**2 + 1.70595585221713e-12*pi**2*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**4*(250.0*cos(pi*t) + 750.0)**2*sin(1.25*pi*z)**2*cos(pi*x)**2*cos(0.833333333333333*pi*y)**2),

    "source_saturation2_3D" : lambda x, y, z, t: 8.60969387878418e-6*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*x)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z) - 1000.0)*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)*exp(-1.0*x)/(1.0*t + 1.) - 1.0986328125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.)**2 - 1.95918367375e-6*pi*(-20.599365234375*y**2*z**2*(-2.5*y + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 10.986328125*y**2*z*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*cos(pi*x)*cos(1.25*pi*z) - 1.30612244916667e-6*pi*(-13.73291015625*y**2*z**2*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) + 10.986328125*y*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.))*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)*(250.0*cos(pi*t) + 750.0)*sin(1.25*pi*z)*cos(pi*x)*cos(0.833333333333333*pi*y) + 5.10476190549306e-6*pi**2*(2.74658203125*y**2*z**2*(-2.5*y + 3.0)*(-3.75*z + 3.0)*exp(-1.0*x)/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*y)*sin(1.25*pi*z)*cos(pi*x),

    }

text_dict = {
    "DOMAIN_EXTENTS" : "1.0 1.2 0.8 ",

    "FINISH_TIME" : "1.0",

    "PRESSURE_SCALE" : "1000.0",

    "SATURATION_SCALE" : "0.5",

    "GRAVITY_MAGNITUDE" : "1.0",

    "VISCOSITY1" : "1.725e-05",

    "VISCOSITY2" : "0.001",

    "DENSITY1" : "1.284",

    "DENSITY2" : "1000.0",

    "PERMEABILITY1" : "1.567346939e-9*(s1 - 0.2)**2",

    "PERMEABILITY2" : "1.567346939e-9*(s2 - 0.3)**2",

    "POROSITY" : "0.4",

    "ABSOLUTE_PERMEABILITY" : "1.567346939e-09",

    "GRAVITY_DIRECTION_1D" : "1",

    "PRESSURE1_1D" : "(250.0*cos(pi*t) + 750.0)*cos(pi*X[0])",

    "SATURATION1_1D" : "1 - 0.5*exp(-1.0*X[0])/(1.0*t + 1.)",

    "PRESSURE2_1D" : "(250.0*cos(pi*t) + 750.0)*cos(pi*X[0])",

    "SATURATION2_1D" : "0.5*exp(-1.0*X[0])/(1.0*t + 1.)",

    "DARCY_VELOCITY1_X_1D" : "-9.0860692115942e-5*(0.8 - 0.5*exp(-1.0*X[0])/(1.0*t + 1.))**2*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0]) - 1.284)",

    "DARCY_VELOCITY1_MAGNITUDE_1D" : "9.0860692115942e-5*sqrt((0.8 - 0.5*exp(-1.0*X[0])/(1.0*t + 1.))**4*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0]) - 1.284)**2)",

    "SOURCE_SATURATION1_1D" : "9.0860692115942e-5*pi**2*(0.8 - 0.5*exp(-1.0*X[0])/(1.0*t + 1.))**2*(250.0*cos(pi*t) + 750.0)*cos(pi*X[0]) - 9.0860692115942e-5*(0.8 - 0.5*exp(-1.0*X[0])/(1.0*t + 1.))*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0]) - 1.284)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.2*exp(-1.0*X[0])/(1.0*t + 1.)**2",

    "DARCY_VELOCITY2_X_1D" : "-1.567346939e-6*(-0.3 + 0.5*exp(-1.0*X[0])/(1.0*t + 1.))**2*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0]) - 1000.0)",

    "DARCY_VELOCITY2_MAGNITUDE_1D" : "1.567346939e-6*sqrt((-0.3 + 0.5*exp(-1.0*X[0])/(1.0*t + 1.))**4*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0]) - 1000.0)**2)",

    "SOURCE_SATURATION2_1D" : "1.567346939e-6*pi**2*(-0.3 + 0.5*exp(-1.0*X[0])/(1.0*t + 1.))**2*(250.0*cos(pi*t) + 750.0)*cos(pi*X[0]) + 1.567346939e-6*(-0.3 + 0.5*exp(-1.0*X[0])/(1.0*t + 1.))*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0]) - 1000.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.2*exp(-1.0*X[0])/(1.0*t + 1.)**2",

    "GRAVITY_DIRECTION_2D" : "1 0. ",

    "PRESSURE1_2D" : "(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*cos(pi*X[0])",

    "SATURATION1_2D" : "-0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.",

    "PRESSURE2_2D" : "(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*cos(pi*X[0])",

    "SATURATION2_2D" : "0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)",

    "DARCY_VELOCITY1_X_2D" : "-9.0860692115942e-5*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1]) - 1.284)*(-0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**2",

    "DARCY_VELOCITY1_Y_2D" : "-7.57172434299517e-5*pi*(-0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*cos(pi*X[0])*cos(0.833333333333333*pi*X[1])",

    "DARCY_VELOCITY1_MAGNITUDE_2D" : "sqrt(8.25566537178801e-9*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1]) - 1.284)**2*(-0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**4 + 5.73310095263056e-9*pi**2*(-0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**4*(250.0*cos(pi*t) + 750.0)**2*cos(pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)",

    "SOURCE_SATURATION1_2D" : "-0.000141969831431159*X[1]**2*(-2.5*X[1] + 3.0)*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1]) - 1.284)*(-0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.3125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 7.57172434299517e-5*pi*(3.90625*X[1]**2*exp(-1.0*X[0])/(1.0*t + 1.) - 3.125*X[1]*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)*(250.0*cos(pi*t) + 750.0)*cos(pi*X[0])*cos(0.833333333333333*pi*X[1]) + 0.000153958394974235*pi**2*(-0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*cos(pi*X[0])",

    "DARCY_VELOCITY2_X_2D" : "-1.567346939e-6*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1]) - 1000.0)*(0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**2",

    "DARCY_VELOCITY2_Y_2D" : "-1.30612244916667e-6*pi*(0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*cos(pi*X[0])*cos(0.833333333333333*pi*X[1])",

    "DARCY_VELOCITY2_MAGNITUDE_2D" : "sqrt(2.45657642719267e-12*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1]) - 1000.0)**2*(0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**4 + 1.70595585221713e-12*pi**2*(0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**4*(250.0*cos(pi*t) + 750.0)**2*cos(pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)",

    "SOURCE_SATURATION2_2D" : "2.4489795921875e-6*X[1]**2*(-2.5*X[1] + 3.0)*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1]) - 1000.0)*(0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 1.30612244916667e-6*pi*(-3.90625*X[1]**2*exp(-1.0*X[0])/(1.0*t + 1.) + 3.125*X[1]*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)*(250.0*cos(pi*t) + 750.0)*cos(pi*X[0])*cos(0.833333333333333*pi*X[1]) + 2.65578231330556e-6*pi**2*(0.78125*X[1]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*cos(pi*X[0])",

    "GRAVITY_DIRECTION_3D" : "1 0. 0. ",

    "PRESSURE1_3D" : "(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])*cos(pi*X[0])",

    "SATURATION1_3D" : "-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.",

    "PRESSURE2_3D" : "(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])*cos(pi*X[0])",

    "SATURATION2_3D" : "2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)",

    "DARCY_VELOCITY1_X_3D" : "-9.0860692115942e-5*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2]) - 1.284)*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**2",

    "DARCY_VELOCITY1_Y_3D" : "-7.57172434299517e-5*pi*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*sin(1.25*pi*X[2])*cos(pi*X[0])*cos(0.833333333333333*pi*X[1])",

    "DARCY_VELOCITY1_Z_3D" : "-0.000113575865144928*pi*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*cos(pi*X[0])*cos(1.25*pi*X[2])",

    "DARCY_VELOCITY1_MAGNITUDE_3D" : "sqrt(8.25566537178801e-9*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2]) - 1.284)**2*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**4 + 1.28994771434188e-8*pi**2*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**4*(250.0*cos(pi*t) + 750.0)**2*sin(0.833333333333333*pi*X[1])**2*cos(pi*X[0])**2*cos(1.25*pi*X[2])**2 + 5.73310095263056e-9*pi**2*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**4*(250.0*cos(pi*t) + 750.0)**2*sin(1.25*pi*X[2])**2*cos(pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)",

    "SOURCE_SATURATION1_3D" : "-0.00049911268862517*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2]) - 1.284)*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)*exp(-1.0*X[0])/(1.0*t + 1.) + 1.0986328125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 0.000113575865144928*pi*(20.599365234375*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 10.986328125*X[1]**2*X[2]*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*cos(pi*X[0])*cos(1.25*pi*X[2]) - 7.57172434299517e-5*pi*(13.73291015625*X[1]**2*X[2]**2*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 10.986328125*X[1]*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)*(250.0*cos(pi*t) + 750.0)*sin(1.25*pi*X[2])*cos(pi*X[0])*cos(0.833333333333333*pi*X[1]) + 0.000295928226405395*pi**2*(-2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 0.8)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])*cos(pi*X[0])",

    "DARCY_VELOCITY2_X_3D" : "-1.567346939e-6*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2]) - 1000.0)*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**2",

    "DARCY_VELOCITY2_Y_3D" : "-1.30612244916667e-6*pi*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*sin(1.25*pi*X[2])*cos(pi*X[0])*cos(0.833333333333333*pi*X[1])",

    "DARCY_VELOCITY2_Z_3D" : "-1.95918367375e-6*pi*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*cos(pi*X[0])*cos(1.25*pi*X[2])",

    "DARCY_VELOCITY2_MAGNITUDE_3D" : "sqrt(2.45657642719267e-12*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2]) - 1000.0)**2*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**4 + 3.83840066748855e-12*pi**2*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**4*(250.0*cos(pi*t) + 750.0)**2*sin(0.833333333333333*pi*X[1])**2*cos(pi*X[0])**2*cos(1.25*pi*X[2])**2 + 1.70595585221713e-12*pi**2*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**4*(250.0*cos(pi*t) + 750.0)**2*sin(1.25*pi*X[2])**2*cos(pi*X[0])**2*cos(0.833333333333333*pi*X[1])**2)",

    "SOURCE_SATURATION2_3D" : "8.60969387878418e-6*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*(-pi*(250.0*cos(pi*t) + 750.0)*sin(pi*X[0])*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2]) - 1000.0)*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)*exp(-1.0*X[0])/(1.0*t + 1.) - 1.0986328125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.)**2 - 1.95918367375e-6*pi*(-20.599365234375*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 10.986328125*X[1]**2*X[2]*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*cos(pi*X[0])*cos(1.25*pi*X[2]) - 1.30612244916667e-6*pi*(-13.73291015625*X[1]**2*X[2]**2*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) + 10.986328125*X[1]*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.))*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)*(250.0*cos(pi*t) + 750.0)*sin(1.25*pi*X[2])*cos(pi*X[0])*cos(0.833333333333333*pi*X[1]) + 5.10476190549306e-6*pi**2*(2.74658203125*X[1]**2*X[2]**2*(-2.5*X[1] + 3.0)*(-3.75*X[2] + 3.0)*exp(-1.0*X[0])/(1.0*t + 1.) - 0.3)**2*(250.0*cos(pi*t) + 750.0)*sin(0.833333333333333*pi*X[1])*sin(1.25*pi*X[2])*cos(pi*X[0])",

    }
