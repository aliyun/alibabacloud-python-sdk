# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetStackGroupRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        stack_group_id: str = None,
        stack_group_name: str = None,
    ):
        # The name of the stack group. The name must be unique within a region.
        # 
        # The name can be up to 255 characters in length, and can contain digits, letters, hyphens (-), and underscores (_). It must start with a digit or letter.
        # 
        # >  You must specify one of the StackGroupName and StackGroupId parameters.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the request.
        self.stack_group_id = stack_group_id
        # The ID of the stack group.
        # 
        # >  You must specify one of the StackGroupName and StackGroupId parameters.
        self.stack_group_name = stack_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_group_id is not None:
            result['StackGroupId'] = self.stack_group_id

        if self.stack_group_name is not None:
            result['StackGroupName'] = self.stack_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackGroupId') is not None:
            self.stack_group_id = m.get('StackGroupId')

        if m.get('StackGroupName') is not None:
            self.stack_group_name = m.get('StackGroupName')

        return self

