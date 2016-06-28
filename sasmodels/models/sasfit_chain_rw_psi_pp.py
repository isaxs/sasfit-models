r"""
This file has been automatically gereated by sasfit_convert
The model calculates an empirical functional form for SAS data characterized
by chain_rw_psi_pp

Definition:
-----------

References:
-----------

"""
from numpy import inf

name = "chain_rw_psi_pp"
title = " "
description = ""
category = " "
#pylint: disable=bad-whitespace, line-too-long
parameters = [
 [ "R_CORE", 	"", 	10.0, 	[-inf, inf], 	"", 	""],
 [ "SNAGG", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "VBRUSH", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
 [ "RG", 	"", 	1.0, 	[-inf, inf], 	"", 	""],
 [ "POL", 	"", 	0.0, 	[-inf, inf], 	"", 	""],
]
 #pylint: enable=bad-whitespace, line-too-long

source = [  "sasfit_chain_rw_psi_pp.c" ]

demo = dict(
	R_CORE = 10.0,
	SNAGG = 0.0,
	VBRUSH = 0.0,
	RG = 1.0,
	POL = 0.0)
