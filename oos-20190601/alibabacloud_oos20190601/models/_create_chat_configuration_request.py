# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateChatConfigurationRequest(DaraModel):
    def __init__(
        self,
        configuration: str = None,
        name: str = None,
        ram_role: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        self.configuration = configuration
        self.name = name
        self.ram_role = ram_role
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration is not None:
            result['Configuration'] = self.configuration

        if self.name is not None:
            result['Name'] = self.name

        if self.ram_role is not None:
            result['RamRole'] = self.ram_role

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RamRole') is not None:
            self.ram_role = m.get('RamRole')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

