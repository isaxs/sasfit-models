r"""
This file has been automatically gereated by sasfit_convert
The model calculates an empirical functional form for SAS data characterized
by ellcylsh_sd_rod

Definition:
-----------

References:
-----------

"""
from numpy import inf

name = "ellcylsh_sd_rod"
title = " "
description = ""
category = " "
#pylint: disable=bad-whitespace, line-too-long
parameters = [
 [ "R0", 	"", 	10.0, 	[-inf, inf], 	"", 	""],
 [ "SIGMA_R0", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "EPSILON", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "T", 	"", 	1.0, 	[-inf, inf], 	"", 	""],
 [ "DUMMY1", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "LL", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "SIGMA_L", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "ETA_CORE", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "ETA_SHELL", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "ETA_SOLV", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "R", 	"", 	0.0, 	[-inf, inf], 	"", 	" "],
 [ "Q", 	"", 	0.0, 	[-inf, inf], 	"", 	" "],
]
 #pylint: enable=bad-whitespace, line-too-long

source = [  "sasfit_ellcylsh_sd_rod.c" ]

demo = dict(
	R0 = 10.0,
	SIGMA_R0 = 0.0,
	EPSILON = 0.0,
	T = 1.0,
	DUMMY1 = 0.0,
	LL = 0.0,
	SIGMA_L = 0.0,
	ETA_CORE = 0.0,
	ETA_SHELL = 0.0,
	ETA_SOLV = 0.0,
	R = 0.0,
	Q = 0.0)
