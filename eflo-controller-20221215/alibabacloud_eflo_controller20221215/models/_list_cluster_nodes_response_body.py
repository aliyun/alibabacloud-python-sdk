# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ListClusterNodesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        nodes: List[main_models.ListClusterNodesResponseBodyNodes] = None,
        request_id: str = None,
    ):
        # The returned pagination token which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The nodes.
        self.nodes = nodes
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ListClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClusterNodesResponseBodyNodes(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        create_time: str = None,
        expired_time: str = None,
        file_system_mount_enabled: bool = None,
        hostname: str = None,
        hpn_zone: str = None,
        hyper_node_id: str = None,
        image_id: str = None,
        image_name: str = None,
        machine_type: str = None,
        networks: List[main_models.ListClusterNodesResponseBodyNodesNetworks] = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_id: str = None,
        node_type: str = None,
        operating_state: str = None,
        sn: str = None,
        tags: List[main_models.ListClusterNodesResponseBodyNodesTags] = None,
        task_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The commodity code.
        self.commodity_code = commodity_code
        # The creation time.
        self.create_time = create_time
        # The time when the node expires.
        self.expired_time = expired_time
        # Indicates whether file storage mounting is supported.
        self.file_system_mount_enabled = file_system_mount_enabled
        # The hostname.
        self.hostname = hostname
        # The cluster number.
        self.hpn_zone = hpn_zone
        self.hyper_node_id = hyper_node_id
        # The system image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The node type.
        self.machine_type = machine_type
        # The network information.
        self.networks = networks
        # The node group ID.
        self.node_group_id = node_group_id
        # The node group name.
        self.node_group_name = node_group_name
        # The node ID.
        self.node_id = node_id
        self.node_type = node_type
        # The node status.
        # 
        # Valid values:
        # 
        # *   Extending
        # *   UnusedNodeStopped
        # *   UnusedNodeStopping
        # *   Unused
        # *   Using
        # *   ReleaseLocking
        # *   Operating
        # *   Cutting
        # *   ClusterNodeStopped
        # *   UnusedNodeRecovering
        # *   ClusterNodeStopping
        # *   ClusterNodeRecovering
        # *   Replacing
        self.operating_state = operating_state
        # The serial number of the node.
        self.sn = sn
        # The tags.
        self.tags = tags
        # The job ID.
        self.task_id = task_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.networks:
            for v1 in self.networks:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time

        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.hyper_node_id is not None:
            result['HyperNodeId'] = self.hyper_node_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        result['Networks'] = []
        if self.networks is not None:
            for k1 in self.networks:
                result['Networks'].append(k1.to_map() if k1 else None)

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state

        if self.sn is not None:
            result['Sn'] = self.sn

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')

        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('HyperNodeId') is not None:
            self.hyper_node_id = m.get('HyperNodeId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        self.networks = []
        if m.get('Networks') is not None:
            for k1 in m.get('Networks'):
                temp_model = main_models.ListClusterNodesResponseBodyNodesNetworks()
                self.networks.append(temp_model.from_map(k1))

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListClusterNodesResponseBodyNodesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ListClusterNodesResponseBodyNodesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListClusterNodesResponseBodyNodesNetworks(DaraModel):
    def __init__(
        self,
        bond_name: str = None,
        ip: str = None,
        subnet_id: str = None,
        vpd_id: str = None,
    ):
        # The name of the network port for the node.
        self.bond_name = bond_name
        # The IP address of the node in the virtual private cloud (VPC).
        self.ip = ip
        # The subnet ID.
        self.subnet_id = subnet_id
        # The VPC ID.
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond_name is not None:
            result['BondName'] = self.bond_name

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondName') is not None:
            self.bond_name = m.get('BondName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        return self

