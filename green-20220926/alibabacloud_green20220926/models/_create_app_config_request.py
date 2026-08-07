# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAppConfigRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
        resource_type: str = None,
        sys_app_id: str = None,
        type: str = None,
    ):
        # The name.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The resource type.
        self.resource_type = resource_type
        # The system app ID.
        self.sys_app_id = sys_app_id
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sys_app_id is not None:
            result['SysAppId'] = self.sys_app_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SysAppId') is not None:
            self.sys_app_id = m.get('SysAppId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

