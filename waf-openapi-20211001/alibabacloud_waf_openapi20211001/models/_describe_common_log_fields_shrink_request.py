# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCommonLogFieldsShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        is_default: bool = None,
        is_required: bool = None,
        log_key_list_shrink: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.is_default = is_default
        self.is_required = is_required
        self.log_key_list_shrink = log_key_list_shrink
        self.region_id = region_id
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.is_required is not None:
            result['IsRequired'] = self.is_required

        if self.log_key_list_shrink is not None:
            result['LogKeyList'] = self.log_key_list_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('IsRequired') is not None:
            self.is_required = m.get('IsRequired')

        if m.get('LogKeyList') is not None:
            self.log_key_list_shrink = m.get('LogKeyList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

