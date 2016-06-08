///////////////////////////////////////////////////
//    This is automatically genearted file       //
//    by sasfit_convert.py                       //
//    Some editting might be required            //
///////////////////////////////////////////////////

/*
* Author(s) of this file:
*   <your name> (<email address>)
*/
// define shortcuts for local parameters/variables
double sf_erf(double x) {


}

double Iq( double q,
	double G,
	double B,
	double R_I,
	double R_Ip1,
	double K,
	double P)
{
// insert your code here
double x, xs, tmp;
x = q*R_I;
xs = q*R_Ip1;
tmp = pow( gsl_sf_erf(x *K /sqrt(6.)), 3 ) / q;
return G*exp(-x*x/3.0) + B*exp(-xs*xs/3.)*pow(tmp,P);
}
double Fq( double q, 
	double G,
	double B,
	double R_I,
	double R_Ip1,
	double K,
	double P)
{
// insert your code here
return 0.0;
}
double form_volume( 
	double G,
	double B,
	double R_I,
	double R_Ip1,
	double K,
	double P)
{
// insert your code here
return 0.0;
}
double Iqxy( double qx, double qy,
	double G,
	double B,
	double R_I,
	double R_Ip1,
	double K,
	double P)
{
	double q = sqrt(qx*qx + qy*qy);
	return Iq( q, G, B, R_I, R_Ip1, K, P);
}