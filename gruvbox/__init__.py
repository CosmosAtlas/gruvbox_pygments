"""Initialize the Gruvbox package."""
from pkg_resources import declare_namespace

declare_namespace(".")

from .ptgruvbox import PtGruvboxStyle
from .gruvbox import GruvboxStyle
