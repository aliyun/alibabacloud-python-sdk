# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateOrganizationalUnitDescriptionRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        organizational_unit_id: str = None,
    ):
        # The description of the organization. The value can be up to 256 characters in length.
        self.description = description
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The organization ID.
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
        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.organizational_unit_id is not None:
            result['OrganizationalUnitId'] = self.organizational_unit_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrganizationalUnitId') is not None:
            self.organizational_unit_id = m.get('OrganizationalUnitId')

        return self

