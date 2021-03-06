///////////////////////////////////////////////////
//    This is automatically genearted file       //
//    by sasfit_convert.py                       //
//    Some editting might be required            //
///////////////////////////////////////////////////

double Iq( double q, double T,  double SIGMA_T,  double D,  double SIGMA_D,
           double DUMMY1,  double DUMMY2,  double ETA_L,  double ETA_SOL,  double P0,
           double LB,  double B,  double L,  double EXVOL,  double CLB);
double Fq( double q,  double T,  double SIGMA_T,  double D,  double SIGMA_D,
           double DUMMY1,  double DUMMY2,  double ETA_L,  double ETA_SOL,  double P0,
           double LB,  double B,  double L,  double EXVOL,  double CLB);
double form_volume(  double T,  double SIGMA_T,  double D,  double SIGMA_D,
                     double DUMMY1,  double DUMMY2,  double ETA_L,  double ETA_SOL,  double P0,
                     double LB,  double B,  double L,  double EXVOL,  double CLB);
double Iqxy( double qx, double qy, double T, double SIGMA_T, double D,
             double SIGMA_D, double DUMMY1, double DUMMY2, double ETA_L, double ETA_SOL,
             double P0, double LB, double B, double L, double EXVOL, double CLB);
/*
* Author(s) of this file:
*   Joachim Kohlbrecher (joachim.kohlbrecher@psi.ch)
*/
// define shortcuts for local T, SIGMA_T, D, SIGMA_D, DUMMY1, DUMMY2, ETA_L, ETA_SOL, P0, LB, B, L, EXVOL, CLBeters/variables
double Iq( double q, double T,  double SIGMA_T,  double D,  double SIGMA_D,
           double DUMMY1,  double DUMMY2,  double ETA_L,  double ETA_SOL,  double P0,
           double LB,  double B,  double L,  double EXVOL,  double CLB)
{
    double Pcs, Pprime;
    sasfit_param subParam;
// insert your code here
    Pcs = sasfit_ff_pcs_homogeneousplate(q,T, SIGMA_T, D, SIGMA_D, DUMMY1, DUMMY2,
                                         ETA_L, ETA_SOL, P0, LB, B, L, EXVOL, CLB);
    sasfit_init_param( &subParam );
    subParam.p[0] = D/2.;
    subParam.p[1] = 0.0;
    subParam.p[2] = SIGMA_D;
    Pprime = sasfit_sq_p__q___thin_disc(q,&subParam);
    return Pcs*Pprime;
}
double Fq( double q,  double T,  double SIGMA_T,  double D,  double SIGMA_D,
           double DUMMY1,  double DUMMY2,  double ETA_L,  double ETA_SOL,  double P0,
           double LB,  double B,  double L,  double EXVOL,  double CLB)
{
// insert your code here
    return 0.0;
}
double form_volume(  double T,  double SIGMA_T,  double D,  double SIGMA_D,
                     double DUMMY1,  double DUMMY2,  double ETA_L,  double ETA_SOL,  double P0,
                     double LB,  double B,  double L,  double EXVOL,  double CLB)
{
// insert your code here
    return 0.0;
}
double Iqxy( double qx, double qy, double T, double SIGMA_T, double D,
             double SIGMA_D, double DUMMY1, double DUMMY2, double ETA_L, double ETA_SOL,
             double P0, double LB, double B, double L, double EXVOL, double CLB)
{
    double q = sqrt(qx*qx + qy*qy);
    return Iq( q, T, SIGMA_T, D, SIGMA_D, DUMMY1, DUMMY2, ETA_L, ETA_SOL, P0, LB, B,
               L, EXVOL, CLB);
}
