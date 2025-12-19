# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateIdentityProviderRequest(DaraModel):
    def __init__(
        self,
        allowed_audience: List[str] = None,
        description: str = None,
        discovery_url: str = None,
        identity_provider_name: str = None,
    ):
        self.allowed_audience = allowed_audience
        self.description = description
        self.discovery_url = discovery_url
        self.identity_provider_name = identity_provider_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_audience is not None:
            result['AllowedAudience'] = self.allowed_audience

        if self.description is not None:
            result['Description'] = self.description

        if self.discovery_url is not None:
            result['DiscoveryURL'] = self.discovery_url

        if self.identity_provider_name is not None:
            result['IdentityProviderName'] = self.identity_provider_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedAudience') is not None:
            self.allowed_audience = m.get('AllowedAudience')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiscoveryURL') is not None:
            self.discovery_url = m.get('DiscoveryURL')

        if m.get('IdentityProviderName') is not None:
            self.identity_provider_name = m.get('IdentityProviderName')

        return self

