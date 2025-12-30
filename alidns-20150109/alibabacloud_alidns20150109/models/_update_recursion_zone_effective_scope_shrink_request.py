# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecursionZoneEffectiveScopeShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        effective_scopes_shrink: str = None,
        zone_id: str = None,
    ):
        self.client_token = client_token
        self.effective_scopes_shrink = effective_scopes_shrink
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.effective_scopes_shrink is not None:
            result['EffectiveScopes'] = self.effective_scopes_shrink

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('EffectiveScopes') is not None:
            self.effective_scopes_shrink = m.get('EffectiveScopes')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

