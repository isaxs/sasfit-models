///////////////////////////////////////////////////
//    This is automatically genearted file       //
//    by sasfit_convert.py                       //
//    Some editting might be required            //
///////////////////////////////////////////////////
#include <gsl/gsl_math.h>
#include <gsl/gsl_sf.h>
#include <gsl/gsl_spline.h>

double Iq( double q, double XMIN,  double XMAX,  double Y1,  double Y2,
           double Y3,  double Y4,  double Y5,  double Y6,  double Y7,  double Y8,
           double P0);
double Fq( double q,  double XMIN,  double XMAX,  double Y1,  double Y2,
           double Y3,  double Y4,  double Y5,  double Y6,  double Y7,  double Y8,
           double P0);
double form_volume(  double XMIN,  double XMAX,  double Y1,  double Y2,
                     double Y3,  double Y4,  double Y5,  double Y6,  double Y7,  double Y8,
                     double P0);
double Iqxy( double qx, double qy, double XMIN, double XMAX, double Y1,
             double Y2, double Y3, double Y4, double Y5, double Y6, double Y7, double Y8,
             double P0);
/*
* Author(s) of this file:
*   Joachim Kohlbrecher (joachim.kohlbrecher@psi.ch)
*/
// define shortcuts for local XMIN, XMAX, Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, P0eters/variables
double Iq( double q, double XMIN,  double XMAX,  double Y1,  double Y2,
           double Y3,  double Y4,  double Y5,  double Y6,  double Y7,  double Y8,
           double P0)
{
    gsl_interp_accel *acc_cspline;
    acc_cspline = gsl_interp_accel_alloc();
    gsl_spline * ffakima8_T;
    ffakima8_T = gsl_spline_alloc (gsl_interp_akima, 10);

    double x = q;
    double tmp, xcs[10], ycs[10];
    int i;
    if (q < XMIN) return 0;
    if (q > XMAX) return 0;
    if (XMIN > XMAX)
    {
        tmp = XMAX;
        XMAX = XMIN;
        XMIN = tmp;
    }
    xcs[0]=XMIN;
    ycs[0]=0;
    xcs[9]=XMAX;
    ycs[9]=0;
    for (i=1; i<=8; i++)
    {
        xcs[i] = XMIN+i*(XMAX-XMIN)/(8.0+1.0);
    }
    gsl_spline_init(ffakima8_T, xcs, ycs, 10);
    return gsl_spline_eval (ffakima8_T, x, acc_cspline);
    //return sas_spline_eval(xcs, ycs, 10, q);
}
double Fq( double q,  double XMIN,  double XMAX,  double Y1,  double Y2,
           double Y3,  double Y4,  double Y5,  double Y6,  double Y7,  double Y8,
           double P0)
{
// insert your code here
    return 0.0;
}
double form_volume(  double XMIN,  double XMAX,  double Y1,  double Y2,
                     double Y3,  double Y4,  double Y5,  double Y6,  double Y7,  double Y8,
                     double P0)
{
// insert your code here
    return 0.0;
}
double Iqxy( double qx, double qy, double XMIN, double XMAX, double Y1,
             double Y2, double Y3, double Y4, double Y5, double Y6, double Y7, double Y8,
             double P0)
{
    double q = sqrt(qx*qx + qy*qy);
    return Iq( q, XMIN, XMAX, Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, P0);
}
