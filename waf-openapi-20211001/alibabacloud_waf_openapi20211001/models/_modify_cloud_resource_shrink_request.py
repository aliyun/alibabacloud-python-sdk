# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyCloudResourceShrinkRequest(DaraModel):
    def __init__(
        self,
        cloud_resource_id: str = None,
        instance_id: str = None,
        listen_shrink: str = None,
        redirect_shrink: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
    ):
        self.cloud_resource_id = cloud_resource_id
        # The ID of the WAF instance.
        # 
        # >  You can call the [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) operation to query the ID of the WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The listener configurations.
        # 
        # This parameter is required.
        self.listen_shrink = listen_shrink
        # The forwarding configurations.
        self.redirect_shrink = redirect_shrink
        # The region in which the WAF instance is deployed. Valid values:
        # 
        # *   **cn-hangzhou**: the Chinese mainland.
        # *   **ap-southeast-1**: outside the Chinese mainland.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_resource_id is not None:
            result['CloudResourceId'] = self.cloud_resource_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.listen_shrink is not None:
            result['Listen'] = self.listen_shrink

        if self.redirect_shrink is not None:
            result['Redirect'] = self.redirect_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudResourceId') is not None:
            self.cloud_resource_id = m.get('CloudResourceId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Listen') is not None:
            self.listen_shrink = m.get('Listen')

        if m.get('Redirect') is not None:
            self.redirect_shrink = m.get('Redirect')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        return self

