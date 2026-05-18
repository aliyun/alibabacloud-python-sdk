# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAccessGroupRequest(DaraModel):
    def __init__(
        self,
        access_group_id: str = None,
        access_group_name: str = None,
        description: str = None,
        input_region_id: str = None,
    ):
        # This parameter is required.
        self.access_group_id = access_group_id
        self.access_group_name = access_group_name
        self.description = description
        # This parameter is required.
        self.input_region_id = input_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_id is not None:
            result['AccessGroupId'] = self.access_group_id

        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.description is not None:
            result['Description'] = self.description

        if self.input_region_id is not None:
            result['InputRegionId'] = self.input_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupId') is not None:
            self.access_group_id = m.get('AccessGroupId')

        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InputRegionId') is not None:
            self.input_region_id = m.get('InputRegionId')

        return self

