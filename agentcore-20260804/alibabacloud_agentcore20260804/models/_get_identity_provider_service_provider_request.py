# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetIdentityProviderServiceProviderRequest(DaraModel):
    def __init__(
        self,
        protocol: str = None,
    ):
        # The query parameter is required and only supports the exact value SAML. The response returns SAML.
        # 
        # This parameter is required.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

