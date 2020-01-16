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
    'night'
sat_id : string
    ['cha']
tag : string
    ['']

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
from pysat.instruments.methods import nasa_cdaweb as cdw

# the platform and name strings associated with this instrument
# need to be defined at the top level
# these attributes will be copied over to the Instrument object by pysat
# the strings used here should also be used to name this file
# platform_name.py
platform = 'gold'
name = 'night'

# dictionary of data 'tags' and corresponding description
tags = {'': 'Level 1c data'}  # this is the default

sat_ids = {'cha': ['']}

_test_dates = {'cha': {'': pysat.datetime(2019, 1, 1)}}

# specify using xarray (not using pandas)
pandas_format = False
multi_file_day = True

# specify file names
fname = ''.join(('GOLD_L1C_CHA_NI1_{year:4d}_{day:03d}_??_',
                 '??_v03_r01_c01.nc'))
supported_tags = {'cha': {'': fname}}

# use the CDAWeb methods list files routine
list_files = functools.partial(cdw.list_files,
                               supported_tags=supported_tags)

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
             'remote_fname': '{year:4d}/{day:03d}/' + fname,
             'local_fname': fname}
supported_tags = {'cha': {'': basic_tag}}
download = functools.partial(cdw.download, supported_tags,
                             multi_file_day=multi_file_day)

# support listing files currently on CDAWeb
list_remote_files = functools.partial(cdw.list_remote_files,
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


def load(fnames, tag=None, sat_id=None):
    """Loads GOLD nighttime_disk data using pysat into pandas.

    This routine is called as needed by pysat. It is not intended
    for direct user interaction.

    Parameters
    ----------
    fnames : array-like
        iterable of filename strings, full path, to data files to be loaded.
        This input is nominally provided by pysat itself.
    tag : string
        tag name used to identify particular data set to be loaded.
        This input is nominally provided by pysat itself.
    sat_id : string
        Satellite ID used to identify particular data set to be loaded.
        This input is nominally provided by pysat itself.
    **kwargs : extra keywords
        Passthrough for additional keyword arguments specified when
        instantiating an Instrument object. These additional keywords
        are passed through to this routine by pysat.

    Returns
    -------
    data, metadata
        Data and Metadata are formatted for pysat. Data is a pandas
        DataFrame while metadata is a pysat.Meta instance.

    Note
    ----
    Any additional keyword arguments passed to pysat.Instrument
    upon instantiation are passed along to this routine.

    Examples
    --------
    ::
        inst = pysat.Instrument('icon', 'ivm', sat_id='a', tag='level_2')
        inst.load(2019,1)

    """

    return pysat.utils.load_netcdf4(fnames, epoch_name='Epoch',
                                    units_label='Units',
                                    name_label='Long_Name',
                                    notes_label='Var_Notes',
                                    desc_label='CatDesc',
                                    plot_label='FieldNam',
                                    axis_label='LablAxis',
                                    scale_label='ScaleTyp',
                                    min_label='ValidMin',
                                    max_label='ValidMax',
                                    fill_label='FillVal')


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
