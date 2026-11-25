# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RestartDBInstanceRequest(DaraModel):
    def __init__(
        self,
        computing_group_id: str = None,
        dbinstance_id: str = None,
        node_list: List[str] = None,
        region_id: str = None,
    ):
        # The compute group ID. This parameter is required when NodeList is specified. If only ComputingGroupId is specified without NodeList, the entire compute group is restarted. If neither is specified, the entire instance is restarted.
        self.computing_group_id = computing_group_id
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The list of node IDs to restart. The elements are the NodeId values returned by DescribeDBInstanceNodes. The parameter format is NodeList.N. If this parameter is not specified or is empty, the entire instance or compute group is restarted based on the original logic. If this parameter is not empty, ComputingGroupId is required, and a maximum of 50 nodes can be specified at a time.
        self.node_list = node_list
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.node_list is not None:
            result['NodeList'] = self.node_list

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('NodeList') is not None:
            self.node_list = m.get('NodeList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

