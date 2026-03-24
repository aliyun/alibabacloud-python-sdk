# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCdnDomainByCertificateRequest(DaraModel):
    def __init__(
        self,
        exact: bool = None,
        sslpub: str = None,
        sslstatus: bool = None,
    ):
        # Specifies whether the domain name list to return match the SSL certificate.
        # 
        # *   true: The domain name list match the SSL certificate.
        # *   false: The domain name list do not match the SSL certificate.
        self.exact = exact
        # The public key of the SSL certificate. You must encode the public key in Base64 and then call the encodeURIComponent function to encode the public key again.
        # 
        # The public key must be in the PEM format.
        # 
        # This parameter is required.
        self.sslpub = sslpub
        # Specifies whether the domain name list to return contains only domain names with HTTPS enabled or disabled.
        # 
        # *   true: The domain name list contains only domain names with HTTPS enabled.
        # *   false: The domain name list contains only domain names with HTTPS disabled.
        self.sslstatus = sslstatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exact is not None:
            result['Exact'] = self.exact

        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub

        if self.sslstatus is not None:
            result['SSLStatus'] = self.sslstatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exact') is not None:
            self.exact = m.get('Exact')

        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')

        if m.get('SSLStatus') is not None:
            self.sslstatus = m.get('SSLStatus')

        return self

