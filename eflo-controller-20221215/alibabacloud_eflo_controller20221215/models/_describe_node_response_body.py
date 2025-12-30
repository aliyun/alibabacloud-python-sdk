# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class DescribeNodeResponseBody(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: str = None,
        disks: List[main_models.DescribeNodeResponseBodyDisks] = None,
        expired_time: str = None,
        file_system_mount_enabled: bool = None,
        hostname: str = None,
        hpn_zone: str = None,
        hyper_node_id: str = None,
        image_id: str = None,
        image_name: str = None,
        machine_type: str = None,
        networks: List[main_models.DescribeNodeResponseBodyNetworks] = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_id: str = None,
        node_type: str = None,
        operating_state: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        sn: str = None,
        user_data: str = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The creation time.
        self.create_time = create_time
        # The disks.
        self.disks = disks
        # The expiration time.
        self.expired_time = expired_time
        # Indicates whether file storage mounting is supported.
        self.file_system_mount_enabled = file_system_mount_enabled
        # The hostname.
        self.hostname = hostname
        # The cluster number.
        self.hpn_zone = hpn_zone
        self.hyper_node_id = hyper_node_id
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The instance type.
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
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The serial number of the node.
        self.sn = sn
        # The custom script.
        self.user_data = user_data
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()
        if self.networks:
            for v1 in self.networks:
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

        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.user_data is not None:
            result['UserData'] = self.user_data

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

        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.DescribeNodeResponseBodyDisks()
                self.disks.append(temp_model.from_map(k1))

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
                temp_model = main_models.DescribeNodeResponseBodyNetworks()
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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeNodeResponseBodyNetworks(DaraModel):
    def __init__(
        self,
        bond_name: str = None,
        ip: str = None,
        subnet_id: str = None,
        vpd_id: str = None,
    ):
        # The port information of the elastic network interface (ENI).
        self.bond_name = bond_name
        # The IP address of the node.
        self.ip = ip
        # The subnet ID.
        self.subnet_id = subnet_id
        # The ID of the cluster network.
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

class DescribeNodeResponseBodyDisks(DaraModel):
    def __init__(
        self,
        category: str = None,
        disk_id: str = None,
        performance_level: str = None,
        size: int = None,
        type: str = None,
    ):
        # The disk type. Valid values:
        # 
        # *   cloud_essd
        self.category = category
        # The disk ID.
        self.disk_id = disk_id
        # The performance level of the ESSD that is used as the system disk. Valid values:
        # 
        # *   PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        self.performance_level = performance_level
        # The disk size. Unit: GiB.
        self.size = size
        # The disk type. Valid values:
        # 
        # *   system: system disk
        # *   data: data disk
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

