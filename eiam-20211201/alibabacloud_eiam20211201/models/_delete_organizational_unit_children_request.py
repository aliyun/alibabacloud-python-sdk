# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteOrganizationalUnitChildrenRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        organizational_unit_id: str = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Organizational Unit ID.
        # 
        # This parameter is required.
        self.organizational_unit_id = organizational_unit_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        return self

