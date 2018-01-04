import numpy as np

from scipy import interpolate
from scipy.constants import physical_constants

from pvpy.PowerSpectrum import PhotonSpectrum


hv = (physical_constants['Planck constant in eV s'][0] *
      physical_constants['speed of light in vacuum'][0])


def alpha2conc(energies, absorption, wavelength_limits=(280, 2000),
               thickness=2e-5, delta_wavelength=5, delta_thickness=1e-7,
               carrier_lifetime=1e-5):
    """Calculate the carrier concentration of a material based on its absorption

    Args:
        energies (np.array): Photon energies in eV
        absorption (np.array): Optical absorption in cm^-1
        wavelength_limits (tuple): Integration limits for the photon wavelengths
            as (min, max), in cm^-1.
        thickness (float): Thickness of material in cm
        delta_wavelength (float): Wavelength integration step size
        delta_thickness (float): Thickness integraton step size
        carrier_lifetime (float): Carrier lifetime of excited carriers

    Returns:
        Carrier concentration in cm^-3.
    """
    ps = PhotonSpectrum()
    flux_spectrum = ps.get_spectrum()

    # convert spectrum from m^-2 s^-1 nm to cm^-2 s^-1 nm and interpolate
    flux = interpolate.interp1d(flux_spectrum[0, :], flux_spectrum[1, :] * 1e-4)

    # convert energies to cm^-1 and interpolate absorption
    alpha = interpolate.interp1d(hv * 1e9 / energies, absorption)

    # widths and wavelengths over which to integrate
    widths = np.arange(0, thickness, delta_thickness)
    wavelengths = np.arange(wavelength_limits[0], wavelength_limits[1],
                            delta_wavelength)

    gen_total = 0
    for w in widths:
        exps = np.exp(-alpha(wavelengths) * w)
        gen_total += (np.sum(alpha(wavelengths) * flux(wavelengths) * exps) *
                      delta_wavelength)
    gen_total = gen_total * delta_thickness

    return(gen_total * carrier_lifetime)
