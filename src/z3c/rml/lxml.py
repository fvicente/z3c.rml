try:
    from lxml import etree
except:
    try:
        import xml.etree.cElementTree as etree
    except:
        import xml.etree.ElementTree as etree

    def _tounicode(element_or_tree, method="xml", pretty_print=False, with_tail=True, doctype=None):
        return unicode(etree.tostring(element_or_tree))
    etree.tounicode = _tounicode
