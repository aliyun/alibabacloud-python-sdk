# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ObtainJwtAuthenticationTokenByDerivedShortTokenRequest(DaraModel):
    def __init__(
        self,
        derived_short_token: str = None,
    ):
        # This parameter is required.
        self.derived_short_token = derived_short_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.derived_short_token is not None:
            result['derivedShortToken'] = self.derived_short_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('derivedShortToken') is not None:
            self.derived_short_token = m.get('derivedShortToken')

        return self

