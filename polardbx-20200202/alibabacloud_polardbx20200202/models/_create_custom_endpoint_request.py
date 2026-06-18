# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomEndpointRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        name: str = None,
        node_auto_enter: bool = None,
        node_ids: str = None,
        node_role: str = None,
        region_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        # The name of the access control instance. The name must be 2 to 128 characters in length and must start with a letter or a Chinese character. The name can contain digits, underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether a node automatically joins the cluster and starts providing services after the node is added or recovered.
        # 
        # This parameter is required.
        self.node_auto_enter = node_auto_enter
        # The IDs of the monitored nodes when RemindUnit (object type) is set to NODE (node). Separate multiple IDs with commas (,). A maximum of 50 nodes can be monitored per rule.
        # 
        # This parameter is required.
        self.node_ids = node_ids
        # To query the metrics of a read-only node in a cloud-native read/write splitting architecture instance, set this parameter to **READONLY** and specify the **NodeId** parameter.
        # >  In other cases, you do not need to specify this parameter or you can set it to **MASTER**.
        self.node_role = node_role
        # The region in which the instance resides.
        self.region_id = region_id
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) in which the endpoint resides.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.name is not None:
            result['Name'] = self.name

        if self.node_auto_enter is not None:
            result['NodeAutoEnter'] = self.node_auto_enter

        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids

        if self.node_role is not None:
            result['NodeRole'] = self.node_role

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeAutoEnter') is not None:
            self.node_auto_enter = m.get('NodeAutoEnter')

        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')

        if m.get('NodeRole') is not None:
            self.node_role = m.get('NodeRole')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

