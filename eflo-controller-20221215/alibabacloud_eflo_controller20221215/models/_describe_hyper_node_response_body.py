# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeHyperNodeResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: str = None,
        expire_time: str = None,
        file_system_mount_enabled: bool = None,
        hostname: str = None,
        hpn_zone: str = None,
        hyper_node_id: str = None,
        machine_type: str = None,
        node_group_id: str = None,
        node_group_name: str = None,
        nodes: List[main_models.DescribeHyperNodeResponseBodyNodes] = None,
        operating_state: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        zone_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.create_time = create_time
        self.expire_time = expire_time
        self.file_system_mount_enabled = file_system_mount_enabled
        self.hostname = hostname
        self.hpn_zone = hpn_zone
        self.hyper_node_id = hyper_node_id
        self.machine_type = machine_type
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.nodes = nodes
        self.operating_state = operating_state
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.status = status
        self.zone_id = zone_id

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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.hyper_node_id is not None:
            result['HyperNodeId'] = self.hyper_node_id

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('HyperNodeId') is not None:
            self.hyper_node_id = m.get('HyperNodeId')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeHyperNodeResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeHyperNodeResponseBodyNodes(DaraModel):
    def __init__(
        self,
        disks: List[main_models.DescribeHyperNodeResponseBodyNodesDisks] = None,
        hostname: str = None,
        image_id: str = None,
        image_name: str = None,
        networks: main_models.DescribeHyperNodeResponseBodyNodesNetworks = None,
        node_id: str = None,
        operating_state: str = None,
        status: str = None,
        user_data: str = None,
    ):
        self.disks = disks
        self.hostname = hostname
        self.image_id = image_id
        self.image_name = image_name
        self.networks = networks
        self.node_id = node_id
        self.operating_state = operating_state
        self.status = status
        self.user_data = user_data

    def validate(self):
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()
        if self.networks:
            self.networks.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.networks is not None:
            result['Networks'] = self.networks.to_map()

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state

        if self.status is not None:
            result['Status'] = self.status

        if self.user_data is not None:
            result['UserData'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.DescribeHyperNodeResponseBodyNodesDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('Networks') is not None:
            temp_model = main_models.DescribeHyperNodeResponseBodyNodesNetworks()
            self.networks = temp_model.from_map(m.get('Networks'))

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        return self

class DescribeHyperNodeResponseBodyNodesNetworks(DaraModel):
    def __init__(
        self,
        bond_name: str = None,
        ip: str = None,
    ):
        self.bond_name = bond_name
        self.ip = ip

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondName') is not None:
            self.bond_name = m.get('BondName')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

class DescribeHyperNodeResponseBodyNodesDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        disk_id: str = None,
        performance_level: str = None,
        size: int = None,
        type: str = None,
    ):
        self.category = category
        self.disk_id = disk_id
        self.performance_level = performance_level
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

