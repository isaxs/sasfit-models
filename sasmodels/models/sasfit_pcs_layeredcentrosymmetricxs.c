///////////////////////////////////////////////////
//    This is automatically genearted file       //
//    by sasfit_convert.py                       //
//    Some editting might be required            //
///////////////////////////////////////////////////

double Iq( double q, double LC,  double SIGMA_LC,  double LSH,
           double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,  double SH,
           double LL,  double Q,  double P0,  double LB,  double B,  double L,
           double EXVOL,  double CLB);
double Fq( double q,  double LC,  double SIGMA_LC,  double LSH,
           double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,  double SH,
           double LL,  double Q,  double P0,  double LB,  double B,  double L,
           double EXVOL,  double CLB);
double form_volume(  double LC,  double SIGMA_LC,  double LSH,
                     double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,  double SH,
                     double LL,  double Q,  double P0,  double LB,  double B,  double L,
                     double EXVOL,  double CLB);
double Iqxy( double qx, double qy, double LC, double SIGMA_LC, double LSH,
             double SIGMA_LSH, double ETA_C, double ETA_SH, double ETA_SOL, double SH,
             double LL, double Q, double P0, double LB, double B, double L, double EXVOL,
             double CLB);
/*
* Author(s) of this file:
*   Joachim Kohlbrecher (joachim.kohlbrecher@psi.ch)
*/
// define shortcuts for local LC, SIGMA_LC, LSH, SIGMA_LSH, ETA_C, ETA_SH, ETA_SOL, SH, LL, Q, P0, LB, B, L, EXVOL, CLBeters/variables
double layeredcentrosymmetric_FF( double LC,  double SIGMA_LC,  double LSH,
                                  double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,  double SH,
                                  double LL,  double Q,  double P0,  double LB,  double B,  double L,
                                  double EXVOL,  double CLB)
{
    double Fc, Fsh, Pcs, LNdistr, u, v;
    sasfit_param subParam;
    u = LL*Q/2.0;
    v = (LL+2*SH)*Q/2.0;
    if (v == 0)
    {
        Fc = (ETA_C-ETA_SOL)*(LL+2.0*SH);
    }
    else
    {
        Fc = (ETA_C-ETA_SOL)*(LL+2.0*SH)*sin(v)/v;
    }
    if (u == 0)
    {
        Fsh = (ETA_C-ETA_SH)*LL;
    }
    else
    {
        Fsh = (ETA_C-ETA_SH)*LL*sin(u)/u;
    }
    Pcs = sas_pow_2(Fc-Fsh);
    return Pcs;
}
double layeredcentrosymmetric_core(double x,  double LC,  double SIGMA_LC,
                                   double LSH,  double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,
                                   double SH,  double LL,  double Q,  double P0,  double LB,  double B,  double L,
                                   double EXVOL,  double CLB)
{
    double Fc, Fsh, Pcs, LNdistr, u, v;
    sasfit_param subParam;
    SH = x;
    Pcs = layeredcentrosymmetric_FF(LC, SIGMA_LC, LSH, SIGMA_LSH, ETA_C, ETA_SH,
                                    ETA_SOL, SH, LL, Q, P0, LB, B, L, EXVOL, CLB);
    sasfit_init_param( &subParam );
    subParam.p[0] = 1.0;
    subParam.p[1] = SIGMA_LSH;
    subParam.p[2] = 1.0;
    subParam.p[3] = LSH;
    LNdistr = sasfit_sd_LogNorm(x, &subParam);
    return LNdistr*Pcs;
}
double layeredcentrosymmetric_SH(double x,  double LC,  double SIGMA_LC,
                                 double LSH,  double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,
                                 double SH,  double LL,  double Q,  double P0,  double LB,  double B,  double L,
                                 double EXVOL,  double CLB)
{
    double SHstart = 0.0, SHend = 0.0;
    double Pcs;
    double LNdistr;
    sasfit_param subParam;
    if (SIGMA_LC == 0)
    {
        LL=LC;
        LNdistr = 1;
    }
    else
    {
        LL = x;
        sasfit_init_param( &subParam );
        subParam.p[0] = 1.0;
        subParam.p[1] = SIGMA_LC;
        subParam.p[2] = 1.0;
        subParam.p[3] = LC;
        LNdistr = sasfit_sd_LogNorm(x, &subParam);
    }
    if (SIGMA_LSH == 0.0)
    {
        SH = LSH;
        Pcs = layeredcentrosymmetric_FF(LC, SIGMA_LC, LSH, SIGMA_LSH, ETA_C, ETA_SH,
                                        ETA_SOL, SH, LL, Q, P0, LB, B, L, EXVOL, CLB);
    }
    else
    {
        find_LogNorm_int_range(2,LSH,SIGMA_LSH,&SHstart,&SHend,LC, SIGMA_LC, LSH,
                               SIGMA_LSH, ETA_C, ETA_SH, ETA_SOL, SH, LL, Q, P0, LB, B, L, EXVOL, CLB);
        Pcs = sasfit_integrate(SHstart, SHend, &layeredcentrosymmetric_core, LC,
                               SIGMA_LC, LSH, SIGMA_LSH, ETA_C, ETA_SH, ETA_SOL, SH, LL, Q, P0, LB, B, L,
                               EXVOL, CLB);
    }
    return LNdistr*Pcs;
    return Pcs;
}
double layeredcentrosymmetric_L(double q,  double LC,  double SIGMA_LC,
                                double LSH,  double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,
                                double SH,  double LL,  double Q,  double P0,  double LB,  double B,  double L,
                                double EXVOL,  double CLB)
{
    double Lstart = 0.0, Lend = 0.0;
    double Pcs;
    Q = q;
    if (SIGMA_LC == 0.0)
    {
        LL = LC;
        Pcs = layeredcentrosymmetric_SH(q,LC, SIGMA_LC, LSH, SIGMA_LSH, ETA_C, ETA_SH,
                                        ETA_SOL, SH, LL, Q, P0, LB, B, L, EXVOL, CLB);
    }
    else
    {
        find_LogNorm_int_range(2,LC,SIGMA_LC,&Lstart,&Lend,LC, SIGMA_LC, LSH, SIGMA_LSH,
                               ETA_C, ETA_SH, ETA_SOL, SH, LL, Q, P0, LB, B, L, EXVOL, CLB);
        Pcs = sasfit_integrate(Lstart, Lend, &layeredcentrosymmetric_SH, LC, SIGMA_LC,
                               LSH, SIGMA_LSH, ETA_C, ETA_SH, ETA_SOL, SH, LL, Q, P0, LB, B, L, EXVOL, CLB);
    }
    return Pcs;
}
double Iq( double q, double LC,  double SIGMA_LC,  double LSH,
           double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,  double SH,
           double LL,  double Q,  double P0,  double LB,  double B,  double L,
           double EXVOL,  double CLB)
{
// insert your code here
    return layeredcentrosymmetric_L(q,LC, SIGMA_LC, LSH, SIGMA_LSH, ETA_C, ETA_SH,
                                    ETA_SOL, SH, LL, Q, P0, LB, B, L, EXVOL, CLB);
}
double Fq( double q,  double LC,  double SIGMA_LC,  double LSH,
           double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,  double SH,
           double LL,  double Q,  double P0,  double LB,  double B,  double L,
           double EXVOL,  double CLB)
{
// insert your code here
    return 0.0;
}
double form_volume(  double LC,  double SIGMA_LC,  double LSH,
                     double SIGMA_LSH,  double ETA_C,  double ETA_SH,  double ETA_SOL,  double SH,
                     double LL,  double Q,  double P0,  double LB,  double B,  double L,
                     double EXVOL,  double CLB)
{
// insert your code here
    return 0.0;
}
double Iqxy( double qx, double qy, double LC, double SIGMA_LC, double LSH,
             double SIGMA_LSH, double ETA_C, double ETA_SH, double ETA_SOL, double SH,
             double LL, double Q, double P0, double LB, double B, double L, double EXVOL,
             double CLB)
{
    double q = sqrt(qx*qx + qy*qy);
    return Iq( q, LC, SIGMA_LC, LSH, SIGMA_LSH, ETA_C, ETA_SH, ETA_SOL, SH, LL, Q,
               P0, LB, B, L, EXVOL, CLB);
}
