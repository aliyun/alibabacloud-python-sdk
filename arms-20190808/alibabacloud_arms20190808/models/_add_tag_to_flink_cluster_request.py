# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddTagToFlinkClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        flink_work_space_id: str = None,
        flink_work_space_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        target_user_id: str = None,
    ):
        # The ID of the Prometheus instance.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The ID of the Flink workspace.
        # 
        # This parameter is required.
        self.flink_work_space_id = flink_work_space_id
        # The name of the Flink workspace.
        # 
        # This parameter is required.
        self.flink_work_space_name = flink_work_space_name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the Alibaba Cloud account to which the Flink workspace belongs.
        # 
        # This parameter is required.
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.flink_work_space_id is not None:
            result['FlinkWorkSpaceId'] = self.flink_work_space_id

        if self.flink_work_space_name is not None:
            result['FlinkWorkSpaceName'] = self.flink_work_space_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('FlinkWorkSpaceId') is not None:
            self.flink_work_space_id = m.get('FlinkWorkSpaceId')

        if m.get('FlinkWorkSpaceName') is not None:
            self.flink_work_space_name = m.get('FlinkWorkSpaceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')

        return self

