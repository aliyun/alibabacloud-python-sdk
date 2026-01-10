# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AiServiceConfig(DaraModel):
    def __init__(
        self,
        address: str = None,
        api_keys: List[str] = None,
        enable_health_check: bool = None,
        protocols: List[str] = None,
        provider: str = None,
    ):
        self.address = address
        self.api_keys = api_keys
        self.enable_health_check = enable_health_check
        self.protocols = protocols
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['address'] = self.address

        if self.api_keys is not None:
            result['apiKeys'] = self.api_keys

        if self.enable_health_check is not None:
            result['enableHealthCheck'] = self.enable_health_check

        if self.protocols is not None:
            result['protocols'] = self.protocols

        if self.provider is not None:
            result['provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            self.address = m.get('address')

        if m.get('apiKeys') is not None:
            self.api_keys = m.get('apiKeys')

        if m.get('enableHealthCheck') is not None:
            self.enable_health_check = m.get('enableHealthCheck')

        if m.get('protocols') is not None:
            self.protocols = m.get('protocols')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        return self

