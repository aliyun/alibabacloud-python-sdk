# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveFingerprintFromOIDCProviderRequest(DaraModel):
    def __init__(
        self,
        fingerprint: str = None,
        oidcprovider_name: str = None,
    ):
        self.fingerprint = fingerprint
        self.oidcprovider_name = oidcprovider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fingerprint is not None:
            result['Fingerprint'] = self.fingerprint

        if self.oidcprovider_name is not None:
            result['OIDCProviderName'] = self.oidcprovider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Fingerprint') is not None:
            self.fingerprint = m.get('Fingerprint')

        if m.get('OIDCProviderName') is not None:
            self.oidcprovider_name = m.get('OIDCProviderName')

        return self

