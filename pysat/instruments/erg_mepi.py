# -*- coding: utf-8 -*-
"""Supports the MEPi instrument on the ERG (Arase) satellite.

Rules of the Road at
https://ergsc.isee.nagoya-u.ac.jp/data_info/rules_of_the_road.shtml.en

Parameters
----------
platform : string
    'erg'
name : string
    'mepi'
sat_id : string
    ''
tag : string
    ''

Note
----
::

    Notes

Warnings
--------


Authors
-------

"""

from __future__ import print_function
from __future__ import absolute_import

import functools
import numpy as np
import sys
import pandas as pds
import pysat

# CDAWeb methods prewritten for pysat
from .methods import nasa_cdaweb as cdw

platform = 'erg'
name = 'mepi'

# dictionary of data 'tags' and corresponding description
tags = {'': 'omni flux data'}
sat_ids = {'': ['']}
test_dates = {'': {'': pysat.datetime(2017, 4, 1)}}

remote_site = 'https://ergsc.isee.nagoya-u.ac.jp'
fname = 'erg_mepi_l2_omniflux_{year:04d}{month:02d}{day:02d}_v01_00.cdf'
supported_tags = {'': {'': fname}}
# use the CDAWeb methods list files routine
# the command below presets some of the methods inputs, leaving
# those provided by pysat available when invoked
list_files = functools.partial(cdw.list_files,
                               supported_tags=supported_tags)

# use the default CDAWeb method
# no other information needs to be supplied here
# pysatCDF is used to load data
load = cdw.load
basic_tag = {'dir': '/data/ergsc/satellite/erg/mepi/l2/omniflux/',
             'remote_fname': '{year:4d}/{month:2d}/' + fname,
             'local_fname': fname}
supported_tags = {'': {'': basic_tag}}
download = functools.partial(cdw.download, supported_tags,
                             remote_site=remote_site)

# support listing files currently on CDAWeb
list_remote_files = functools.partial(cdw.list_remote_files,
                                      remote_site=remote_site,
                                      supported_tags=supported_tags)


# code should be defined below as needed
def default(self):
    """Default customization function.

    This routine is automatically applied to the Instrument object
    on every load by the pysat nanokernel (first in queue).

    Parameters
    ----------
    self : pysat.Instrument
        This object

    Returns
    --------
    Void : (NoneType)
        Object modified in place.


    """

    return


# code should be defined below as needed
def clean(inst):
    """Routine to return PLATFORM/NAME data cleaned to the specified level

    Cleaning level is specified in inst.clean_level and pysat
    will accept user input for several strings. The clean_level is
    specified at instantiation of the Instrument object.

    'clean' All parameters should be good, suitable for statistical and
            case studies
    'dusty' All paramers should generally be good though same may
            not be great
    'dirty' There are data areas that have issues, data should be used
            with caution
    'none'  No cleaning applied, routine not called in this case.


    Parameters
    -----------
    inst : (pysat.Instrument)
        Instrument class object, whose attribute clean_level is used to return
        the desired level of data selectivity.

    Returns
    --------
    Void : (NoneType)
        data in inst is modified in-place.

    Notes
    -----

    """

    return
