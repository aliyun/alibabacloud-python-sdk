# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class GetRegionStatusResponseBody(DaraModel):
    def __init__(
        self,
        service_role_exists: bool = None,
        status: str = None,
    ):
        self.service_role_exists = service_role_exists
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_role_exists is not None:
            result['serviceRoleExists'] = self.service_role_exists

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceRoleExists') is not None:
            self.service_role_exists = m.get('serviceRoleExists')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

