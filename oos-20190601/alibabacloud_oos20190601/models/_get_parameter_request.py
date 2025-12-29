# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetParameterRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        parameter_version: int = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The name of the common parameter. The name can be up to 200 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.name = name
        # The version number of the common parameter. Valid values: 1 to 100.
        self.parameter_version = parameter_version
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.parameter_version is not None:
            result['ParameterVersion'] = self.parameter_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParameterVersion') is not None:
            self.parameter_version = m.get('ParameterVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

