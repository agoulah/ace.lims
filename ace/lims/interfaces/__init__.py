from zope.interface import Interface


class IACELIMS(Interface):

    """Marker interface that defines a Zope 3 browser layer.
       If you need to register a viewlet only for the
       "ace.lims" product, this interface must be its layer
    """
