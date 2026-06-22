# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Node(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_duration: int = None,
        auto_renew_duration_unit: str = None,
        create_time: int = None,
        expire_time: int = None,
        instance_type: str = None,
        maintenance_status: str = None,
        node_group_id: str = None,
        node_group_type: str = None,
        node_id: str = None,
        node_name: str = None,
        node_state: str = None,
        private_ip: str = None,
        public_ip: str = None,
        zone_id: str = None,
    ):
        # Whether auto-renewal is enabled for the node. Valid values:
        # 
        # - true: Auto-renewal is enabled.
        # 
        # - false: Auto-renewal is disabled.
        self.auto_renew = auto_renew
        # The auto-renewal duration for the node.
        self.auto_renew_duration = auto_renew_duration
        # The unit of the auto-renewal duration.
        self.auto_renew_duration_unit = auto_renew_duration_unit
        # The creation time of the node.
        self.create_time = create_time
        # The expiration time of the node.
        self.expire_time = expire_time
        # The instance type of the node. This corresponds to an ECS instance type. You can call the ECS [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query the available instance types.
        self.instance_type = instance_type
        # The maintenance status of the node. Valid values:
        # 
        # - ON: The node is in maintenance mode.
        # 
        # - OFF: The node is not in maintenance mode.
        # 
        # If this parameter is empty, the node is not in maintenance mode.
        self.maintenance_status = maintenance_status
        # The ID of the node group.
        self.node_group_id = node_group_id
        # The type of the node group. Valid values:
        # 
        # - MASTER: A master node group.
        # 
        # - CORE: A core node group.
        # 
        # - TASK: A task node group.
        self.node_group_type = node_group_type
        # The ID of the node.
        self.node_id = node_id
        # The name of the node.
        self.node_name = node_name
        # The state of the node. Valid values:
        # 
        # - Pending: The node is being created.
        # 
        # - Starting: The node is starting up.
        # 
        # - Running: The node is operational and running services.
        # 
        # - Stopping: The node is shutting down.
        # 
        # - Stopped: The node is powered off.
        # 
        # - Terminated: The node has been permanently deleted.
        self.node_state = node_state
        # The private IP address of the node.
        self.private_ip = private_ip
        # The public IP address of the node.
        self.public_ip = public_ip
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_duration is not None:
            result['AutoRenewDuration'] = self.auto_renew_duration

        if self.auto_renew_duration_unit is not None:
            result['AutoRenewDurationUnit'] = self.auto_renew_duration_unit

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.maintenance_status is not None:
            result['MaintenanceStatus'] = self.maintenance_status

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_type is not None:
            result['NodeGroupType'] = self.node_group_type

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.node_state is not None:
            result['NodeState'] = self.node_state

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewDuration') is not None:
            self.auto_renew_duration = m.get('AutoRenewDuration')

        if m.get('AutoRenewDurationUnit') is not None:
            self.auto_renew_duration_unit = m.get('AutoRenewDurationUnit')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaintenanceStatus') is not None:
            self.maintenance_status = m.get('MaintenanceStatus')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupType') is not None:
            self.node_group_type = m.get('NodeGroupType')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('NodeState') is not None:
            self.node_state = m.get('NodeState')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

