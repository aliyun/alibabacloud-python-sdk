# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeTwoWayRequest(DaraModel):
    def __init__(
        self,
        instance_class: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The instance class of the two-way synchronization task. Valid values: **large**, **medium**, **micro**, and **small**.
        # 
        # >  For more information, see [Specifications of data synchronization instances](https://help.aliyun.com/document_detail/26605.html).
        # 
        # This parameter is required.
        self.instance_class = instance_class
        # The ID of the data synchronization instance. You can call the [DescribeDtsJobs](https://help.aliyun.com/document_detail/209702.html) operation to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the DTS instance. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

