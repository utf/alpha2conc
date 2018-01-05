import numpy as np
from scipy import interpolate, constants

h = constants.physical_constants['Planck constant in eV s'][0]
c = constants.physical_constants['speed of light in vacuum'][0]


def alpha2conc(energies, absorption, thickness, tau, energy_limits=None,
               de=0.001, dt=1e-7):
    """Calculate the carrier concentration of a material based on its absorption

    Args:
        energies (np.array): Photon energies in eV.
        absorption (np.array): Optical absorption in cm^-1.
        thickness (float): Thickness of material in cm.
        tau (float): Carrier lifetime of excited carriers in s.
        energy_limits (tuple): Integration limits for the photon energy
            as (min, max), in eV. Default is None (all energies).
        de (float): Energy integration step size in eV. Default 0.05 eV.
        dt (float): Thickness integraton step size in cm. Default 2 nm.

    Returns:
        Carrier concentration in cm^-3.
    """
    am_eners, am_spec = np.loadtxt('AM15G.csv', unpack=True, delimiter=',')

    # convert to photon flux -- from Watts/(meter**2 nm) to #/(s meter**2 nm)
    flux = am_spec * am_eners * 1e-9 / (constants.c * constants.h)

    # convert photon flux and energies from nm to eV
    flux = (flux * am_eners**2 * 1e-9) / (h * c)
    am_eners = (h * c) / (am_eners * 1e-9)

    # convert flux from m^-2 s^-1 eV^-1 to cm^-2 s^-1 eV^-1 and interpolate
    flux = interpolate.interp1d(am_eners, flux * 1e-4)

    # interpolate absorption
    alpha = interpolate.interp1d(energies, absorption)

    # widths and wavelengths over which to integrate
    widths = np.arange(0, thickness, dt)

    if not energy_limits:
        energy_limits = [max([min(energies), min(am_eners)]),
                         min([max(energies), max(am_eners)])]
    int_eners = np.arange(energy_limits[0], energy_limits[1], de)

    gen_total = 0
    for w in widths:
        exps = np.exp(-alpha(int_eners) * w)
        gen_total += np.sum(alpha(int_eners) * flux(int_eners) * exps) * de
    gen_total = gen_total * dt

    return(gen_total * tau / thickness)
