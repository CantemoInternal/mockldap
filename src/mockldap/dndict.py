from ldap.cidict import cidict
from ldap.dn import str2dn, dn2str


class DNDict(cidict):
    """
    A dictionary which uses LDAP distinguished names as keys
    """

    def __getitem__(self, key):
        return cidict.__getitem__(self, _canonalize_dn(key))

    def __setitem__(self, key, value):
        return cidict.__setitem__(self, _canonalize_dn(key), value)

    def __delitem__(self, key):
        return cidict.__delitem__(self, _canonalize_dn(key))

    def update(self, srcdict):
        d = {}
        for key in srcdict.keys():
            d[_canonalize_dn(key)] = srcdict[key]

        return cidict.update(self, d)

    def __contains__(self, key):
        return cidict.__contains__(self, _canonalize_dn(key))

    def has_key(self, key):
        return cidict.has_key(self, _canonalize_dn(key))

    def get(self, key):
        return cidict.get(self, _canonalize_dn(key))


def _canonalize_dn(dn):
    return dn2str(str2dn(dn))
