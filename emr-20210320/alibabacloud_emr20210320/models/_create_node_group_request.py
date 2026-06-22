# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class CreateNodeGroupRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_group: main_models.NodeGroupConfig = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The information about the machine group.
        self.node_group = node_group
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.node_group:
            self.node_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.node_group is not None:
            result['NodeGroup'] = self.node_group.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('NodeGroup') is not None:
            temp_model = main_models.NodeGroupConfig()
            self.node_group = temp_model.from_map(m.get('NodeGroup'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

