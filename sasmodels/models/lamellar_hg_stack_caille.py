# Note: model title and parameter table are inserted automatically
r"""
This model provides the scattering intensity, $I(q) = P(q)S(q)$, for a lamellar
phase where a random distribution in solution are assumed. Here a Caille $S(q)$
is used for the lamellar stacks.

The scattering intensity $I(q)$ is

.. math::

    I(q) = 2 \pi \frac{P(q)S(q)}{q^2\delta }


The form factor $P(q)$ is

.. math::

        P(q) = \frac{4}{q^2}\big\{
        \Delta\rho_H \left[\sin[q(\delta_H + \delta_T)] - \sin(q\delta_T)\right]
            + \Delta\rho_T\sin(q\delta_T)\big\}^2

and the structure factor $S(q)$ is

.. math::

    S(q) = 1 + 2 \sum_1^{N-1}\left(1-\frac{n}{N}\right)
        \cos(qdn)\exp\left(-\frac{2q^2d^2\alpha(n)}{2}\right)

where

.. math::
    :nowrap:

    \begin{align*}
    \alpha(n) &= \frac{\eta_{cp}}{4\pi^2} \left(\ln(\pi n)+\gamma_E\right)
              &&  \\
    \gamma_E  &= 0.5772156649
              && \text{Euler's constant} \\
    \eta_{cp} &= \frac{q_o^2k_B T}{8\pi\sqrt{K\overline{B}}}
              && \text{Caille constant}
    \end{align*}


$\delta_T$ is the tail length (or *tail_length*), $\delta_H$ is the head
thickness (or *head_length*), $\Delta\rho_H$ is SLD(headgroup) - SLD(solvent),
and $\Delta\rho_T$ is SLD(tail) - SLD(headgroup). Here $d$ is (repeat) spacing,
$K$ is smectic bending elasticity, $B$ is compression modulus, and $N$ is the
number of lamellar plates (*Nlayers*).

NB: **When the Caille parameter is greater than approximately 0.8 to 1.0, the
assumptions of the model are incorrect.**  And due to a complication of the
model function, users are responsible for making sure that all the assumptions
are handled accurately (see the original reference below for more details).

Non-integer numbers of stacks are calculated as a linear combination of
results for the next lower and higher values.

Be aware that the computations may be very slow.

The 2D scattering intensity is calculated in the same way as 1D, where
the $q$ vector is defined as

.. math::

    q = \sqrt{q_x^2 + q_y^2}


References
----------

F Nallet, R Laversanne, and D Roux, J. Phys. II France, 3, (1993) 487-502

also in J. Phys. Chem. B, 105, (2001) 11081-11088
"""
from numpy import inf

name = "lamellar_hg_stack_caille"
title = "Random lamellar head/tail/tail/head sheet with Caille structure factor"
description = """\
    [Random lamellar phase with Caille  structure factor]
        randomly oriented stacks of infinite sheets
        with Caille S(Q), having polydisperse spacing.
        layer thickness =(H+T+T+H) = 2(Head+Tail)
        sld = Tail scattering length density
        sld_head = Head scattering length density
        sld_solvent = solvent scattering length density
        background = incoherent background
        scale = scale factor
"""
category = "shape:lamellae"

single = False  # TODO: check
parameters = [
    #   [ "name", "units", default, [lower, upper], "type",
    #     "description" ],
    ["tail_length", "Ang", 10, [0, inf], "volume",
     "Tail thickness"],
    ["head_length", "Ang", 2, [0, inf], "volume",
     "head thickness"],
    ["Nlayers", "", 30, [0, inf], "",
     "Number of layers"],
    ["spacing", "Ang", 40., [0.0, inf], "volume",
     "d-spacing of Caille S(Q)"],
    ["Caille_parameter", "", 0.001, [0.0, 0.8], "",
     "Caille parameter"],
    ["sld", "1e-6/Ang^2", 0.4, [-inf, inf], "sld",
     "Tail scattering length density"],
    ["sld_head", "1e-6/Ang^2", 2.0, [-inf, inf], "sld",
     "Head scattering length density"],
    ["sld_solvent", "1e-6/Ang^2", 6, [-inf, inf], "sld",
     "Solvent scattering length density"],
    ]

source = ["lamellar_hg_stack_caille_kernel.c"]

# No volume normalization despite having a volume parameter
# This should perhaps be volume normalized?
form_volume = """
    return 1.0;
    """

# ER defaults to 0.0
# VR defaults to 1.0

demo = dict(
    scale=1, background=0,
    Nlayers=20, spacing=200., Caille_parameter=0.05,
    tail_length=15, head_length=10,
    #sld=-1, sld_head=4.0, sld_solvent=6.0,
    sld=-1, sld_head=4.1, sld_solvent=6.0,
    tail_length_pd=0.1, tail_length_pd_n=20,
    head_length_pd=0.05, head_length_pd_n=30,
    spacing_pd=0.2, spacing_pd_n=40,
    )

#
tests = [[{'scale': 1.0, 'background': 0.0, 'tail_length': 10.0, 'head_length': 2.0,
           'Nlayers': 30.0, 'spacing': 40., 'Caille_parameter': 0.001, 'sld': 0.4,
           'sld_head': 2.0, 'sld_solvent': 6.0, 'tail_length_pd': 0.0,
           'head_length_pd': 0.0, 'spacing_pd': 0.0}, [0.001], [6838238.571488]]]
# ADDED by: RKH  ON: 18Mar2016  converted from sasview previously, now renaming everything & sorting the docs
