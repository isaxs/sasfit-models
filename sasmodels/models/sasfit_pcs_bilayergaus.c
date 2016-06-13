///////////////////////////////////////////////////
//    This is automatically genearted file       //
//    by sasfit_convert.py                       //
//    Some editting might be required            //
///////////////////////////////////////////////////

/*
* Author(s) of this file:
*   Joachim Kohlbrecher (joachim.kohlbrecher@psi.ch)
*/
// define shortcuts for local parameters/variables
double Iq( double q, double SIGMA_CORE fabs(param->p[0])
           , double B_CORE param->p[1]
           , double SIGMA_OUT fabs(param->p[2])
           , double B_OUT param->p[3]
           , double D)
{
// insert your code here
    double Fq( double q,  double SIGMA_CORE fabs(param->p[0])
               , double B_CORE param->p[1]
               , double SIGMA_OUT fabs(param->p[2])
               , double B_OUT param->p[3]
               , double D)
}
double Fq( double q,  double SIGMA_CORE fabs(param->p[0])
           , double B_CORE param->p[1]
           , double SIGMA_OUT fabs(param->p[2])
           , double B_OUT param->p[3]
           , double D)
double SIGMA_CORE fabs(param->p[0])
, double B_CORE param->p[1]
, double SIGMA_OUT fabs(param->p[2])
, double B_OUT param->p[3]
, double D)
{
    double u_out, u_core, M, Pprime, R, Fout, Fcore;
// insert your code here
    u_core = sas_pow_2(q*SIGMA_CORE);
    u_out  = sas_pow_2(q*SIGMA_OUT);
    R = 0.5*D;
//	M = 2.0*sqrt(2.*M_PI)*SIGMA_OUT *B_OUT+sqrt(2.*M_PI)*SIGMA_CORE*B_CORE;
//
//	if (M == 0.0) {
//		M = 1.0;
//        sasfit_param_set_err(param, DBGINFO("BiLayerGauss is divergent"));
//	}
    Fout  = sqrt(2.*M_PI)*SIGMA_OUT *B_OUT  *exp(-0.5*u_out) *cos(q*R);
    Fcore = sqrt(2.*M_PI)*SIGMA_CORE*B_CORE *exp(-0.5*u_core);
    return Fcore+2.0*Fout;
}
double form_volume(  double SIGMA_CORE fabs(param->p[0])
                     , double B_CORE param->p[1]
                     , double SIGMA_OUT fabs(param->p[2])
                     , double B_OUT param->p[3]
                     , double D)
{
// insert your code here
    return 0.0;
}
double Iqxy( double qx, double qy, double SIGMA_CORE fabs(param->p[0])
             , double B_CORE param->p[1]
             , double SIGMA_OUT fabs(param->p[2])
             , double B_OUT param->p[3]
             , double D)
{
    double q = sqrt(qx*qx + qy*qy);
    return Iq( q, SIGMA_CORE fabs(param->p[0])
               , B_CORE param->p[1]
               , SIGMA_OUT fabs(param->p[2])
               , B_OUT param->p[3]
               , D);
}