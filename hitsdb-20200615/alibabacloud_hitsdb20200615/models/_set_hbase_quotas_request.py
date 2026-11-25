# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetHBaseQuotasRequest(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        instance_id: str = None,
        limit: str = None,
        region_id: str = None,
        scope: str = None,
        security_token: str = None,
        time_unit: str = None,
        type: str = None,
        unit: str = None,
    ):
        self.dimension = dimension
        # This parameter is required.
        self.instance_id = instance_id
        self.limit = limit
        self.region_id = region_id
        self.scope = scope
        self.security_token = security_token
        self.time_unit = time_unit
        self.type = type
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.time_unit is not None:
            result['TimeUnit'] = self.time_unit

        if self.type is not None:
            result['Type'] = self.type

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TimeUnit') is not None:
            self.time_unit = m.get('TimeUnit')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

