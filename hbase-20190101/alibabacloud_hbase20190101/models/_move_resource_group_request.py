# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MoveResourceGroupRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        new_resource_group_id: str = None,
    ):
        # The ID of the target instance. You can call the [DescribeInstances](https://help.aliyun.com/document_detail/144595.html) operation to obtain the instance ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the target resource group. You can call the [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html) operation to query the list of resource groups.
        # 
        # This parameter is required.
        self.new_resource_group_id = new_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.new_resource_group_id is not None:
            result['NewResourceGroupId'] = self.new_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NewResourceGroupId') is not None:
            self.new_resource_group_id = m.get('NewResourceGroupId')

        return self

