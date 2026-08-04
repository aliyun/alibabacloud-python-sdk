# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryBindsByOuterIdRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        minor_outer_id: str = None,
        outer_id: str = None,
        tenant_id: str = None,
    ):
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.minor_outer_id = minor_outer_id
        # This parameter is required.
        self.outer_id = outer_id
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.minor_outer_id is not None:
            result['MinorOuterId'] = self.minor_outer_id

        if self.outer_id is not None:
            result['OuterId'] = self.outer_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('MinorOuterId') is not None:
            self.minor_outer_id = m.get('MinorOuterId')

        if m.get('OuterId') is not None:
            self.outer_id = m.get('OuterId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

