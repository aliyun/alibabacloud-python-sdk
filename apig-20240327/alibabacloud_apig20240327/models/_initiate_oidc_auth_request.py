# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitiateOidcAuthRequest(DaraModel):
    def __init__(
        self,
        provider: str = None,
    ):
        # The OIDC provider identifier.
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.provider is not None:
            result['provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('provider') is not None:
            self.provider = m.get('provider')

        return self

