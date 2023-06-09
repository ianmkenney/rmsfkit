"""
rmsfkit
A package to perform RMSF analysis on molecular dynamics data.
"""

# Add imports here
from .rmsfkit import RMSF

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
