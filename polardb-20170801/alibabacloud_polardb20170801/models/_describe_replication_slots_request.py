# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeReplicationSlotsRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        sub_group_name: str = None,
    ):
        # The ID of the PolarDB cluster to query.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The child node name of the distributed instance, which is used to filter replication slots.
        self.sub_group_name = sub_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.sub_group_name is not None:
            result['SubGroupName'] = self.sub_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('SubGroupName') is not None:
            self.sub_group_name = m.get('SubGroupName')

        return self

