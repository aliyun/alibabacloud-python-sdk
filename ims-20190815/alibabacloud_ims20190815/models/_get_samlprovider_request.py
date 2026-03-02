# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSAMLProviderRequest(DaraModel):
    def __init__(
        self,
        samlprovider_name: str = None,
    ):
        # The name of the SAML provider.
        # 
        # This parameter is required.
        self.samlprovider_name = samlprovider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.samlprovider_name is not None:
            result['SAMLProviderName'] = self.samlprovider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SAMLProviderName') is not None:
            self.samlprovider_name = m.get('SAMLProviderName')

        return self

