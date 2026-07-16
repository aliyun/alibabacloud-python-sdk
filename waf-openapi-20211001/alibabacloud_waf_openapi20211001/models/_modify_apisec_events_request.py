# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyApisecEventsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        event_ids: List[str] = None,
        event_scope: str = None,
        instance_id: str = None,
        note: str = None,
        region_id: str = None,
        resource_manager_resource_group_id: str = None,
        user_status: str = None,
    ):
        # The ID of the hybrid cloud cluster.
        # 
        # > This parameter is available only for hybrid cloud scenarios. Call [DescribeHybridCloudClusters](https://help.aliyun.com/document_detail/2849376.html) to obtain information about hybrid cloud clusters.
        self.cluster_id = cluster_id
        # A list of API security event IDs.
        # 
        # This parameter is required.
        self.event_ids = event_ids
        # The dimension of the security event. Valid values:
        # 
        # - **ip** (default): IP security event.
        # 
        # - **account**: account security event.
        self.event_scope = event_scope
        # The ID of the WAF instance.
        # 
        # > Call [DescribeInstance](https://help.aliyun.com/document_detail/433756.html) to obtain the ID of the current WAF instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The remarks.
        self.note = note
        # The region of the WAF instance. Valid values:
        # 
        # - **cn-hangzhou**: the Chinese mainland.
        # 
        # - **ap-southeast-1**: outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the Alibaba Cloud resource group.
        self.resource_manager_resource_group_id = resource_manager_resource_group_id
        # The status of the event. Valid values:
        # 
        # - **toBeConfirmed**: The event is pending confirmation.
        # 
        # - **confirmed**: The event is confirmed.
        # 
        # - **ignored**: The event is ignored.
        # 
        # This parameter is required.
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.event_ids is not None:
            result['EventIds'] = self.event_ids

        if self.event_scope is not None:
            result['EventScope'] = self.event_scope

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.note is not None:
            result['Note'] = self.note

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_manager_resource_group_id is not None:
            result['ResourceManagerResourceGroupId'] = self.resource_manager_resource_group_id

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EventIds') is not None:
            self.event_ids = m.get('EventIds')

        if m.get('EventScope') is not None:
            self.event_scope = m.get('EventScope')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceManagerResourceGroupId') is not None:
            self.resource_manager_resource_group_id = m.get('ResourceManagerResourceGroupId')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

