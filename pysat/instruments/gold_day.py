# -*- coding: utf-8 -*-
"""This is a template for a pysat.Instrument support file that
utilizes CDAWeb methods. Copy and modify this file as needed when adding a
new Instrument to pysat.

This is a good area to introduce the instrument, provide background
on the mission, operations, instrumenation, and measurements.

Also a good place to provide contact information. This text will
be included in the pysat API documentation.

Parameters
----------
platform : string
    'gold'
name : string
    'day'
sat_id : string
    ['cha']
tag : string
    ['', 'l2c']

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
import pysat

# CDAWeb methods prewritten for pysat
from .methods import nasa_cdaweb as cdw

# the platform and name strings associated with this instrument
# need to be defined at the top level
# these attributes will be copied over to the Instrument object by pysat
# the strings used here should also be used to name this file
# platform_name.py
platform = 'gold'
name = 'day'

# dictionary of data 'tags' and corresponding description
tags = {'': 'Level 1 data',  # this is the default
        'l2c': 'Level 2 data'}  # new defaultonce level 2 data is released

sat_ids = {'cha': ['', 'l2c']}

test_dates = {'cha': {'': pysat.datetime(2019, 1, 1),
                      'l2c': pysat.datetime(2019, 1, 1)}}

# specify using xarray (not using pandas)
pandas_format = False
multi_file_day = True

# specify file names
fname = ''.join(('GOLD_L1C_CHA_DAY_{year:4d}_{doy:03d}_{hour:02d}_',
                 '{minute:02d}_v01_r01_c01.nc'))
supported_tags = {'cha': {'': fname,
                          'l2c': fname}}

# use the CDAWeb methods list files routine
list_files = functools.partial(cdw.list_files,
                               supported_tags=supported_tags)

#
# support load routine
#
# use the default CDAWeb method
load = cdw.load

#
# support download routine
#
# to use the default CDAWeb method
# we need to provide additional information
# directory location on CDAWeb ftp server
# formatting template for filenames on CDAWeb
# formatting template for files saved to the local disk
# a dictionary needs to be created for each sat_id and tag
# combination along with the file format template
# outer dict keyed by sat_id, inner dict keyed by tag
basic_tag = {'dir': '/pub/data/gold/level1c',
             'remote_fname': '{year:4d}/{doy:03d}/' + fname,
             'local_fname': fname}
supported_tags = {'cha': {'': basic_tag}}
download = functools.partial(cdw.download, supported_tags,
                             multi_file_day=multi_file_day)

# support listing files currently on CDAWeb
list_remote_files = functools.partial(cdw.list_remote_files,
                                      supported_tags=supported_tags,
                                      multi_file_day=multi_file_day)


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
