# Hook up our custom paragraph parser.
import z3c.rml.paraparser
import z3c.rml.rlfix

try:
    import pkg_resources
    __version__ = pkg_resources.require('z3c.rml')[0].version
except:
    pass

from reportlab.lib.styles import getSampleStyleSheet
SampleStyleSheet = getSampleStyleSheet()
