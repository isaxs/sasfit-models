///////////////////////////////////////////////////
//    This is automatically genearted file       //
//    by sasfit_convert.py                       //
//    Some editting might be required            //
///////////////////////////////////////////////////

double Iq( double q, double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
           double POL);
double Iq( double q, double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
           double POL) double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
                  double POL);
double Iq( double q, double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
           double POL) double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
double POL) double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
double POL);
double Iqxy( double qx, double qy, double R_CORE, double SNAGG, double VBRUSH,
             double RG, double POL);
/*
* Author(s) of this file:
*   Joachim Kohlbrecher (joachim.kohlbrecher@psi.ch)
*/
// define shortcuts for local parameters/variables
double Iq( double q, double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
           double POL)
{
    double iso, aniso,ftmp,ftmp2;
// insert your code here
    RW_SAW = 1.0;
    RADAVG = 0.0;
    PEP    = 0.0;
    R_CORE = 0.0;
    if ((R_TOT-T_SHELL) > 0)
    {
        R_CORE=R_TOT-T_SHELL;
        T_SH = T_SHELL;
    }
    else
    {
        R_CORE = 0.0;
        T_SH = R_TOT;
    }
    ftmp = ETA_MAG_CORE;
    ftmp2 = ETA_MAG_SHELL;
    ETA_MAG_CORE=0.0;
    ETA_MAG_SHELL=0.0;
    iso = (1.0+POL)/2.0*(FFmicelle_pp(q,param)+FFmicelle_pm(q,param))
          + (1.0-POL)/2.0*(FFmicelle_mm(q,param)+FFmicelle_mp(q,param));
    ETA_MAG_CORE=ftmp;
    ETA_MAG_SHELL=ftmp2;
    PSI = sasfit_param_override_get_psi(PSIDEG*M_PI/180.);
    aniso =	(1.0+POL)/2.0*(FFmicelle_pp(q,param)+FFmicelle_pm(q,param))
            +	(1.0-POL)/2.0*(FFmicelle_mm(q,param)+FFmicelle_mp(q,param));
    aniso = aniso-iso;
    return aniso;
}
double Iq( double q, double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
           double POL) double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
double POL)
{
// insert your code here
    return 0.0;
}
double Iq( double q, double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
           double POL) double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
double POL) double R_CORE,  double SNAGG,  double VBRUSH,  double RG,
double POL)
{
// insert your code here
    return V(R_CORE+T_SH+2.*sqrt(5./3.)*RG,param);
}
double Iqxy( double qx, double qy, double R_CORE, double SNAGG, double VBRUSH,
             double RG, double POL)
{
    double q = sqrt(qx*qx + qy*qy);
    return Iq( q, R_CORE, SNAGG, VBRUSH, RG, POL);
}
