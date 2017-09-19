from __future__ import absolute_import, division
import numpy as np
import pytest

from astropy.utils.data import get_pkg_data_filename
from astropy import units as u

from ..spectra.spectrum1d import Spectrum1D

# TODO: Add more tests.
def test_spectrum1d_simple():
    sp = Spectrum1D([1, 2, 3])

def test_spectrum1d_wave_flux():
    wave=np.arange(3600., 9000., 1.)*u.AA
    sp = Spectrum1D(flux=np.ones(len(wave)), spectral_axis=wave)
    assert sp.wavelength.unit == u.AA

def test_spectrum1d_multispec():
    wave=np.arange(3600., 9000., 1.)
    wvarray = np.outer(np.ones(10), wave)
    fxarray = np.ones_like(wvarray)
    sp = Spectrum1D(flux=fxarray, spectral_axis=wvarray*u.AA)
    pytest.set_trace()


def test_spectrum1d_GMOSfits():
    optical_fits_file = get_pkg_data_filename('data/L5g_0355+11_Cruz09.fits')
    optical_spec_2 = Spectrum1D.read(optical_fits_file)
    assert len(optical_spec_2.data) == 3020

def test_specific_spec_axis_unit():
    optical_fits_file = get_pkg_data_filename('data/L5g_0355+11_Cruz09.fits')
    optical_spec =  Spectrum1D.read(optical_fits_file, spectral_axis_unit="Angstrom")
    assert optical_spec.spectral_axis.unit == "Angstrom"
