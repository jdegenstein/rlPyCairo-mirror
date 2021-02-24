=====================================
README
=====================================

(C) Copyright ReportLab Europe Ltd. 2000-2021.
See ``LICENSE.txt`` for license details.

This is a plugin for the ReportLab PDF Toolkit.
of rich PDF documents, and also creation of charts in a variety
of bitmap and vector formats.

This library is also the foundation for our commercial product
Report Markup Language (RML), available in the ReportLab PLUS
package. RML offers many more features, a template-based style
of document development familiar to all web developers, and
higher development productivity.  Please consider trying out
RML for your project, as the license sales support our open
source development.

Contents of this file:

1. Licensing

2. Installation

   2.1 General Prerequisites

   2.2 Source Distribution mercurial


3. Prerequisites / Dependencies

4. Documentation

5. Tests

6. Acknowledgements and Thanks


1. Licensing
============
BSD license.  See ``LICENSE.txt`` for details.


2. Installation
===============

In most cases, pip install reportlab`` will do the job.


2.1 General prerequisites
--------------------------
You need to have installed Python (versions 2.7 or >=3.6) and reportlab
and ideally PIL or Pillow with Freetype support; more notes on prerequisites
follow below.

2.2. Where to get the code
------------------------------------------
Latest sources are available from ReportLab's
open source download area::

    https://hg.reportlab.com/hg-pulic/rlPyCairo

You can obtain the latest code from our Mercurial repository with::

    hg clone https://hg.reportlab.com/hg-public/rlPyCairo

All released packages are available from our pypi at

	https://www.reportlab.com/pypi/


Main releases are also available from the Python Package Index:

    https://pypi.python.org/

A mirror only repository is available for git users at

	https://github.com/MrBitBucket/rlPyCairo-mirror

please do not use this for issue reporting etc; use the mail list at

    https://pairlist2.pair.net/mailman/listinfo/reportlab-users


3. Prerequisites / Dependencies
===============================
This works with Python versions 2.7 or >=3.6. Older versions are available
going back to Python 1.5 or thereabouts.

There are no absolute prerequisites beyond the Python
standard library; but the Python Imaging Library (PIL or Pillow)
is needed to produce images with this package.

4. Documentation
================
There is no documentation other than that provided in the reportlab package
about the standard renderPM renderer. This package is intended as an
alternative to the lgpl_libart based backend reportlab.graphics._renderPM.

To enable this backend the reportlab.rl_config.renderPMBackend should be set
to the string 'rlPyCairo'. Use any of the methods outlined in
reportlab/rl_config.py to accomplish this.

5. Test suite
=============
Tests are in the ``reportlab/tests/`` directory.  They can be executed by cd'ing into the
directory and executing ``python runAll.py``, or from ``python setup.py tests``.

6. Acknowledgements and Thanks
==============================
Claude Paroz for failing examples of the base backend.
