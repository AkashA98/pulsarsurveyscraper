"""
Definitions for each survey
Includes:
* the main URL
* the type (HTML, JSON, ATNF)
* period_units (ms or s)
* start_row
* pulsar_column, period_column, DM_column, ra_column, dec_column (the last two optional)
* coordinate_frame, ra_unit, dec_unit (if ra_column/dec_column supplied)
* table_index: which table number on a given page
"""
# update this as needed
ATNF_version = "1.64"
Surveys = {
    "ATNF": {
        "url": "https://www.atnf.csiro.au/research/pulsar/psrcat/proc_form.php?version={}&Name=Name&RaJ=RaJ&DecJ=DecJ&P0=P0&DM=DM&startUserDefined=true&c1_val=&c2_val=&c3_val=&c4_val=&sort_attr=jname&sort_order=asc&condition=&pulsar_names=&ephemeris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&coords_2=&style=Short+without+errors&no_value=*&fsize=3&x_axis=&x_scale=linear&y_axis=&y_scale=linear&state=query&table_bottom.x=51&table_bottom.y=23".format(
            ATNF_version
        ),
        "type": "ATNF",
        "period_units": "s",
    },
    "GalacticMSPs": {
        "url": "http://astro.phys.wvu.edu/GalacticMSPs/GalacticMSPs.txt",
        "type": "ASCII",
        "pulsar_column": 0,
        "period_column": 1,
        "DM_column": 2,
        "ra_column": 3,
        "dec_column": 4,
        "period_units": "ms",
        "coordinate_frame": "galactic",
        "ra_unit": "deg",
        "dec_unit": "deg",
    },
    "AO327": {
        "url": "http://www.naic.edu/~deneva/drift-search/index.html",
        "type": "HTML",
        "pulsar_column": 1,
        "period_column": 2,
        "DM_column": 3,
        "start_row": 1,
        "period_units": "ms",
    },
    "GBNCC": {
        "url": "http://astro.phys.wvu.edu/GBNCC/",
        "type": "HTML",
        "pulsar_column": 1,
        "period_column": 2,
        "DM_column": 3,
        "start_row": 1,
        "period_units": "ms",
        "table_index": 1,
    },
    "GBT820": {
        "url": "http://astro.phys.wvu.edu/GBNCC/",
        "type": "HTML",
        "pulsar_column": 1,
        "period_column": 2,
        "DM_column": 3,
        "start_row": 1,
        "period_units": "ms",
        "table_index": 0,
    },
    "GBT350": {
        "url": "http://astro.phys.wvu.edu/GBTdrift350/",
        "type": "HTML",
        "pulsar_column": 0,
        "period_column": 1,
        "DM_column": 2,
        "start_row": 1,
        "period_units": "ms",
    },
    "PALFA": {
        "url": "http://www2.naic.edu/~palfa/newpulsars/index.html",
        "type": "HTML",
        "pulsar_column": 1,
        "period_column": 2,
        "DM_column": 3,
        "start_row": 1,
        "period_units": "ms",
    },
    "DMB": {
        "url": "http://astro.phys.wvu.edu/dmb",
        "type": "HTML",
        "pulsar_column": 0,
        "period_column": 1,
        "DM_column": 2,
        "start_row": 0,
        "period_units": "ms",
    },
    "SUPERB": {
        "url": "https://sites.google.com/site/publicsuperb/discoveries",
        "type": "HTML",
        "pulsar_column": 0,
        "period_column": 3,
        "DM_column": 4,
        "start_row": 1,
        "period_units": "ms",
        "ra_column": 1,
        "dec_column": 2,
    },
    "HTRU-S Low-latitude": {
        "url": "https://sites.google.com/site/htrusouthdeep/home/discoveries",
        "type": "HTML",
        "pulsar_column": 1,
        "period_column": 8,
        "DM_column": 9,
        "start_row": 4,
        "period_units": "ms",
        "ra_column": 6,
        "dec_column": 7,
    },
    "LOTAAS": {
        "url": "http://old.astron.nl/lotaas/index.php?sort=1",
        "type": "HTML",
        "pulsar_column": 1,
        "period_column": 2,
        "DM_column": 3,
        "start_row": 1,
        "period_units": "ms",
    },
    "RRATalog": {
        "url": "http://astro.phys.wvu.edu/rratalog",
        "type": "HTML",
        "pulsar_column": 0,
        "period_column": 1,
        "DM_column": 3,
        "start_row": 2,
        "period_units": "s",
    },
    "CHIME": {
        "url": "http://catalog.chime-frb.ca/galactic",
        "type": "JSON",
        "period_units": "s",
    },
    "FAST": {
        "url": "http://crafts.bao.ac.cn/pulsar/",
        "type": "HTML",
        "pulsar_column": 1,
        "period_column": 4,
        "DM_column": 5,
        "start_row": 1,
        "period_units": "ms",
        "ra_column": 2,
        "dec_column": 3,
    },
    "FAST-GPPS": {
        "url": "http://zmtt.bao.ac.cn/GPPS/GPPSnewPSR.html",
        "type": "HTML",
        "pulsar_column": 0,
        "period_column": 2,
        "DM_column": 3,
        "start_row": 1,
        "period_units": "s",
        "ra_column": 4,
        "dec_column": 5,
    },
    "MWA": {
        "url": "https://wiki.mwatelescope.org/display/MP/SMART+survey+candidates",
        "type": "HTML",
        "pulsar_column": 0,
        "period_column": 1,
        "DM_column": 2,
        "start_row": 1,
        "period_units": "ms",
    },
    "TRAPUM": {
        "url": "http://www.trapum.org/discoveries.html",
        "type": "HTML",
        "pulsar_column": 1,
        "period_column": 3,
        "DM_column": 4,
        "period_units": "ms",
        "start_row": 1,
    },
    "GHRSS": {
        "url": "http://www.ncra.tifr.res.in/~bhaswati/GHRSS.html",
        "type": "HTML",
        "pulsar_column": 0,
        "period_column": 2,
        "DM_column": 3,
        "period_units": "ms",
        "start_row": 1,
    },
}
