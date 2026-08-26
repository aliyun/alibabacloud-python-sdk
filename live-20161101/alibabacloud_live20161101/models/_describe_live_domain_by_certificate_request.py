# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainByCertificateRequest(DaraModel):
    def __init__(
        self,
        owner_id: int = None,
        region_id: str = None,
        sslpub: str = None,
        sslstatus: bool = None,
    ):
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The public key of the certificate. The public key must be Base64 encoding and then URL-encoded (encodeURIComponent). The PEM format is supported.
        # 
        # This parameter is required.
        self.sslpub = sslpub
        # Specifies whether the returned domain name list includes only domain names with HTTPS enabled or disabled.
        # - **true**: HTTPS is enabled.
        # - **false**: HTTPS is disabled.
        self.sslstatus = sslstatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sslpub is not None:
            result['SSLPub'] = self.sslpub

        if self.sslstatus is not None:
            result['SSLStatus'] = self.sslstatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SSLPub') is not None:
            self.sslpub = m.get('SSLPub')

        if m.get('SSLStatus') is not None:
            self.sslstatus = m.get('SSLStatus')

        return self

