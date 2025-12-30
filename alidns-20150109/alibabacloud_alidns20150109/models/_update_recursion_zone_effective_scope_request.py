# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class UpdateRecursionZoneEffectiveScopeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        effective_scopes: List[main_models.UpdateRecursionZoneEffectiveScopeRequestEffectiveScopes] = None,
        zone_id: str = None,
    ):
        self.client_token = client_token
        self.effective_scopes = effective_scopes
        self.zone_id = zone_id

    def validate(self):
        if self.effective_scopes:
            for v1 in self.effective_scopes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['EffectiveScopes'] = []
        if self.effective_scopes is not None:
            for k1 in self.effective_scopes:
                result['EffectiveScopes'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.effective_scopes = []
        if m.get('EffectiveScopes') is not None:
            for k1 in m.get('EffectiveScopes'):
                temp_model = main_models.UpdateRecursionZoneEffectiveScopeRequestEffectiveScopes()
                self.effective_scopes.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class UpdateRecursionZoneEffectiveScopeRequestEffectiveScopes(DaraModel):
    def __init__(
        self,
        effective_type: str = None,
        scope: List[str] = None,
    ):
        self.effective_type = effective_type
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_type is not None:
            result['EffectiveType'] = self.effective_type

        if self.scope is not None:
            result['Scope'] = self.scope

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveType') is not None:
            self.effective_type = m.get('EffectiveType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        return self

