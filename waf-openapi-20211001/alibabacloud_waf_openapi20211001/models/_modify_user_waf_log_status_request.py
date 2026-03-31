# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyUserWafLogStatusRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        log_region_id: str = None,
        log_status: int = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.log_region_id = log_region_id
        # This parameter is required.
        self.log_status = log_status
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

        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_status is not None:
            result['LogStatus'] = self.log_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStatus') is not None:
            self.log_status = m.get('LogStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

