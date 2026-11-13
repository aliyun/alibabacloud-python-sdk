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
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The creation time in ISO 8601 format. The Z in the example indicates UTC.
        self.create_time = create_time
        # The expiration time in ISO 8601 format.
        self.expire_time = expire_time
        # Indicates whether file system mounting is supported.
        self.file_system_mount_enabled = file_system_mount_enabled
        # The hostname.
        self.hostname = hostname
        # The cluster number.
        self.hpn_zone = hpn_zone
        # The ID of the supernode.
        self.hyper_node_id = hyper_node_id
        # The machine type.
        self.machine_type = machine_type
        # The ID of the node group.
        self.node_group_id = node_group_id
        # The name of the node group.
        self.node_group_name = node_group_name
        # The list of nodes.
        self.nodes = nodes
        # The status of the supernode.
        self.operating_state = operating_state
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The status of the node.
        self.status = status
        # The zone ID.
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
        # The cloud disk information.
        self.disks = disks
        # The hostname.
        self.hostname = hostname
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The network information.
        self.networks = networks
        # The ID of the node.
        self.node_id = node_id
        # The status of the node.
        self.operating_state = operating_state
        # The status.
        self.status = status
        # The user-defined script.
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
        # The name of the network interface.
        self.bond_name = bond_name
        # The IP address of the machine in the VPC.
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
        encrypted: bool = None,
        kmskey_id: str = None,
        performance_level: str = None,
        size: int = None,
        type: str = None,
    ):
        # The data packet classification. Valid values:
        # 
        # - **DOWNLINK_PACKET**: downlink packets
        # - **UPLINK_PACKET**: uplink packets
        self.category = category
        # The ID of the cloud disk.
        self.disk_id = disk_id
        # Indicates whether the system cloud disk is encrypted. Valid values:
        # - true: The disk is encrypted.
        # - false: The disk is not encrypted.
        # 
        # Default value: false.
        # 
        # 
        # >Notice: When you create a cloud disk from an encrypted snapshot by using a shared encrypted image, you must specify the request parameter Encrypted=true for the cloud disk to ensure that the created cloud disk is encrypted by using the recipient\\"s key.
        # 
        # > System cloud disk encryption during instance creation is not supported in Hong Kong (China) Zone D and Singapore Zone A.
        self.encrypted = encrypted
        # The KMS key ID corresponding to the system cloud disk.
        # 
        # If the Encrypted parameter is set to true and the KMSKeyId parameter is not specified, the default key is used for encryption, and the KMSKeyId value is returned after the instance is created.
        # - If the cloud disk is created from an unshared encrypted snapshot, the encryption key used for the snapshot is used by default.
        # - If the cloud disk is created from a shared encrypted snapshot, the service key is used by default.
        # - If the cloud disk is created in a region where account-level default encryption for Block Storage is enabled, the specified account-level key is used by default.
        # - In other cases, the service key is used by default.
        self.kmskey_id = kmskey_id
        # The performance level of the ESSD when it is used as the system cloud disk. Valid values:
        # - PL0: A single disk can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single disk can deliver up to 50,000 random read/write IOPS.
        self.performance_level = performance_level
        # The size of the cloud disk. Unit: GiB.
        self.size = size
        # The type of the cloud disk. Valid values:
        # 
        # - system: system cloud disk
        # - data: data cloud disk
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

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

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

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

