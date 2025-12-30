# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class CreateClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_description: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        components: List[main_models.CreateClusterRequestComponents] = None,
        hpn_zone: str = None,
        ignore_failed_node_tasks: bool = None,
        networks: main_models.CreateClusterRequestNetworks = None,
        nimiz_vswitches: List[str] = None,
        node_groups: List[main_models.CreateClusterRequestNodeGroups] = None,
        open_eni_jumbo_frame: bool = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateClusterRequestTag] = None,
    ):
        # Cluster description
        self.cluster_description = cluster_description
        # Cluster name
        self.cluster_name = cluster_name
        # Cluster type
        self.cluster_type = cluster_type
        # Components (software instances)
        self.components = components
        # Cluster number
        self.hpn_zone = hpn_zone
        # Whether to allow skipping failed nodes, the default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # Network information
        self.networks = networks
        # Node VSwitches
        self.nimiz_vswitches = nimiz_vswitches
        # Node group list
        self.node_groups = node_groups
        # Whether the network interface supports jumbo frames
        self.open_eni_jumbo_frame = open_eni_jumbo_frame
        # Resource group ID
        self.resource_group_id = resource_group_id
        # Resource tags
        self.tag = tag

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()
        if self.networks:
            self.networks.validate()
        if self.node_groups:
            for v1 in self.node_groups:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks

        if self.networks is not None:
            result['Networks'] = self.networks.to_map()

        if self.nimiz_vswitches is not None:
            result['NimizVSwitches'] = self.nimiz_vswitches

        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k1 in self.node_groups:
                result['NodeGroups'].append(k1.to_map() if k1 else None)

        if self.open_eni_jumbo_frame is not None:
            result['OpenEniJumboFrame'] = self.open_eni_jumbo_frame

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.CreateClusterRequestComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')

        if m.get('Networks') is not None:
            temp_model = main_models.CreateClusterRequestNetworks()
            self.networks = temp_model.from_map(m.get('Networks'))

        if m.get('NimizVSwitches') is not None:
            self.nimiz_vswitches = m.get('NimizVSwitches')

        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k1 in m.get('NodeGroups'):
                temp_model = main_models.CreateClusterRequestNodeGroups()
                self.node_groups.append(temp_model.from_map(k1))

        if m.get('OpenEniJumboFrame') is not None:
            self.open_eni_jumbo_frame = m.get('OpenEniJumboFrame')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateClusterRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateClusterRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Key
        self.key = key
        # Value
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

class CreateClusterRequestNodeGroups(DaraModel):
    def __init__(
        self,
        file_system_mount_enabled: bool = None,
        hyper_nodes: List[main_models.CreateClusterRequestNodeGroupsHyperNodes] = None,
        image_id: str = None,
        key_pair_name: str = None,
        login_password: str = None,
        machine_type: str = None,
        node_group_description: str = None,
        node_group_name: str = None,
        nodes: List[main_models.CreateClusterRequestNodeGroupsNodes] = None,
        system_disk: main_models.CreateClusterRequestNodeGroupsSystemDisk = None,
        user_data: str = None,
        virtual_gpu_enabled: bool = None,
        zone_id: str = None,
    ):
        # Whether to support file system mounting
        self.file_system_mount_enabled = file_system_mount_enabled
        self.hyper_nodes = hyper_nodes
        # System image ID
        self.image_id = image_id
        # Key pair name.
        self.key_pair_name = key_pair_name
        # Login password
        self.login_password = login_password
        # Machine type
        self.machine_type = machine_type
        # Node group description
        self.node_group_description = node_group_description
        # Node group name
        self.node_group_name = node_group_name
        # Node list
        self.nodes = nodes
        # System disk information
        self.system_disk = system_disk
        # Instance custom data. It needs to be encoded in Base64, and the original data should not exceed 16 KB.
        self.user_data = user_data
        # Whether to enable gpu virtualization or not
        self.virtual_gpu_enabled = virtual_gpu_enabled
        # Zone ID
        self.zone_id = zone_id

    def validate(self):
        if self.hyper_nodes:
            for v1 in self.hyper_nodes:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled

        result['HyperNodes'] = []
        if self.hyper_nodes is not None:
            for k1 in self.hyper_nodes:
                result['HyperNodes'].append(k1.to_map() if k1 else None)

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.login_password is not None:
            result['LoginPassword'] = self.login_password

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.node_group_description is not None:
            result['NodeGroupDescription'] = self.node_group_description

        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.virtual_gpu_enabled is not None:
            result['VirtualGpuEnabled'] = self.virtual_gpu_enabled

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')

        self.hyper_nodes = []
        if m.get('HyperNodes') is not None:
            for k1 in m.get('HyperNodes'):
                temp_model = main_models.CreateClusterRequestNodeGroupsHyperNodes()
                self.hyper_nodes.append(temp_model.from_map(k1))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('NodeGroupDescription') is not None:
            self.node_group_description = m.get('NodeGroupDescription')

        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.CreateClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.CreateClusterRequestNodeGroupsSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VirtualGpuEnabled') is not None:
            self.virtual_gpu_enabled = m.get('VirtualGpuEnabled')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateClusterRequestNodeGroupsSystemDisk(DaraModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # Disk type. The value range is:
        # 
        # - cloud_essd: ESSD disk.
        self.category = category
        # When creating an ESSD disk as the system disk, set the performance level of the disk. The value range is:
        # - PL0: Maximum random read/write IOPS for a single disk is 10,000.
        # - PL1: Maximum random read/write IOPS for a single disk is 50,000.
        self.performance_level = performance_level
        # Unit: GB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class CreateClusterRequestNodeGroupsNodes(DaraModel):
    def __init__(
        self,
        data_disk: List[main_models.CreateClusterRequestNodeGroupsNodesDataDisk] = None,
        hostname: str = None,
        login_password: str = None,
        node_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Data disk specifications.
        self.data_disk = data_disk
        # Hostname
        self.hostname = hostname
        # Login password
        self.login_password = login_password
        # Node ID
        self.node_id = node_id
        # VSwitch ID
        self.v_switch_id = v_switch_id
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.login_password is not None:
            result['LoginPassword'] = self.login_password

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.CreateClusterRequestNodeGroupsNodesDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateClusterRequestNodeGroupsNodesDataDisk(DaraModel):
    def __init__(
        self,
        bursting_enabled: bool = None,
        category: str = None,
        delete_with_node: bool = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        self.bursting_enabled = bursting_enabled
        # Type
        self.category = category
        # Whether the data disk is deleted with the node when it is unsubscribed
        self.delete_with_node = delete_with_node
        # Data disk performance level
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        # Disk size
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.delete_with_node is not None:
            result['DeleteWithNode'] = self.delete_with_node

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithNode') is not None:
            self.delete_with_node = m.get('DeleteWithNode')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class CreateClusterRequestNodeGroupsHyperNodes(DaraModel):
    def __init__(
        self,
        data_disk: List[main_models.CreateClusterRequestNodeGroupsHyperNodesDataDisk] = None,
        hostname: str = None,
        hyper_node_id: str = None,
        login_password: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.data_disk = data_disk
        self.hostname = hostname
        self.hyper_node_id = hyper_node_id
        self.login_password = login_password
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.hyper_node_id is not None:
            result['HyperNodeId'] = self.hyper_node_id

        if self.login_password is not None:
            result['LoginPassword'] = self.login_password

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.CreateClusterRequestNodeGroupsHyperNodesDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('HyperNodeId') is not None:
            self.hyper_node_id = m.get('HyperNodeId')

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateClusterRequestNodeGroupsHyperNodesDataDisk(DaraModel):
    def __init__(
        self,
        bursting_enabled: bool = None,
        category: str = None,
        delete_with_node: bool = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        self.bursting_enabled = bursting_enabled
        self.category = category
        self.delete_with_node = delete_with_node
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.delete_with_node is not None:
            result['DeleteWithNode'] = self.delete_with_node

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithNode') is not None:
            self.delete_with_node = m.get('DeleteWithNode')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class CreateClusterRequestNetworks(DaraModel):
    def __init__(
        self,
        ip_allocation_policy: List[main_models.CreateClusterRequestNetworksIpAllocationPolicy] = None,
        new_vpd_info: main_models.CreateClusterRequestNetworksNewVpdInfo = None,
        security_group_id: str = None,
        tail_ip_version: str = None,
        v_switch_id: str = None,
        v_switch_zone_id: str = None,
        vpc_id: str = None,
        vpd_info: main_models.CreateClusterRequestNetworksVpdInfo = None,
    ):
        # IP allocation policy
        self.ip_allocation_policy = ip_allocation_policy
        # Vpd configuration information
        self.new_vpd_info = new_vpd_info
        # Security group ID
        self.security_group_id = security_group_id
        # IP version
        self.tail_ip_version = tail_ip_version
        # VSwitch ID
        self.v_switch_id = v_switch_id
        # VSwitch Zone ID
        self.v_switch_zone_id = v_switch_zone_id
        # VPC ID
        self.vpc_id = vpc_id
        # Reuse VPD information
        self.vpd_info = vpd_info

    def validate(self):
        if self.ip_allocation_policy:
            for v1 in self.ip_allocation_policy:
                 if v1:
                    v1.validate()
        if self.new_vpd_info:
            self.new_vpd_info.validate()
        if self.vpd_info:
            self.vpd_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpAllocationPolicy'] = []
        if self.ip_allocation_policy is not None:
            for k1 in self.ip_allocation_policy:
                result['IpAllocationPolicy'].append(k1.to_map() if k1 else None)

        if self.new_vpd_info is not None:
            result['NewVpdInfo'] = self.new_vpd_info.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.tail_ip_version is not None:
            result['TailIpVersion'] = self.tail_ip_version

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_zone_id is not None:
            result['VSwitchZoneId'] = self.v_switch_zone_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpd_info is not None:
            result['VpdInfo'] = self.vpd_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_allocation_policy = []
        if m.get('IpAllocationPolicy') is not None:
            for k1 in m.get('IpAllocationPolicy'):
                temp_model = main_models.CreateClusterRequestNetworksIpAllocationPolicy()
                self.ip_allocation_policy.append(temp_model.from_map(k1))

        if m.get('NewVpdInfo') is not None:
            temp_model = main_models.CreateClusterRequestNetworksNewVpdInfo()
            self.new_vpd_info = temp_model.from_map(m.get('NewVpdInfo'))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('TailIpVersion') is not None:
            self.tail_ip_version = m.get('TailIpVersion')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchZoneId') is not None:
            self.v_switch_zone_id = m.get('VSwitchZoneId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpdInfo') is not None:
            temp_model = main_models.CreateClusterRequestNetworksVpdInfo()
            self.vpd_info = temp_model.from_map(m.get('VpdInfo'))

        return self

class CreateClusterRequestNetworksVpdInfo(DaraModel):
    def __init__(
        self,
        vpd_id: str = None,
        vpd_subnets: List[str] = None,
    ):
        # VPC ID
        self.vpd_id = vpd_id
        # List of cluster subnet IDs
        self.vpd_subnets = vpd_subnets

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id

        if self.vpd_subnets is not None:
            result['VpdSubnets'] = self.vpd_subnets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')

        if m.get('VpdSubnets') is not None:
            self.vpd_subnets = m.get('VpdSubnets')

        return self

class CreateClusterRequestNetworksNewVpdInfo(DaraModel):
    def __init__(
        self,
        cen_id: str = None,
        cloud_link_cidr: str = None,
        cloud_link_id: str = None,
        monitor_vpc_id: str = None,
        monitor_vswitch_id: str = None,
        vpd_cidr: str = None,
        vpd_subnets: List[main_models.CreateClusterRequestNetworksNewVpdInfoVpdSubnets] = None,
    ):
        # Cloud Enterprise Network ID
        self.cen_id = cen_id
        # Cloud link CIDR
        self.cloud_link_cidr = cloud_link_cidr
        # Cloud link ID
        self.cloud_link_id = cloud_link_id
        # Virtual Private Cloud (VPC)
        self.monitor_vpc_id = monitor_vpc_id
        # VPC switch
        self.monitor_vswitch_id = monitor_vswitch_id
        # Cluster network segment
        self.vpd_cidr = vpd_cidr
        # Cluster subnets
        self.vpd_subnets = vpd_subnets

    def validate(self):
        if self.vpd_subnets:
            for v1 in self.vpd_subnets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cloud_link_cidr is not None:
            result['CloudLinkCidr'] = self.cloud_link_cidr

        if self.cloud_link_id is not None:
            result['CloudLinkId'] = self.cloud_link_id

        if self.monitor_vpc_id is not None:
            result['MonitorVpcId'] = self.monitor_vpc_id

        if self.monitor_vswitch_id is not None:
            result['MonitorVswitchId'] = self.monitor_vswitch_id

        if self.vpd_cidr is not None:
            result['VpdCidr'] = self.vpd_cidr

        result['VpdSubnets'] = []
        if self.vpd_subnets is not None:
            for k1 in self.vpd_subnets:
                result['VpdSubnets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CloudLinkCidr') is not None:
            self.cloud_link_cidr = m.get('CloudLinkCidr')

        if m.get('CloudLinkId') is not None:
            self.cloud_link_id = m.get('CloudLinkId')

        if m.get('MonitorVpcId') is not None:
            self.monitor_vpc_id = m.get('MonitorVpcId')

        if m.get('MonitorVswitchId') is not None:
            self.monitor_vswitch_id = m.get('MonitorVswitchId')

        if m.get('VpdCidr') is not None:
            self.vpd_cidr = m.get('VpdCidr')

        self.vpd_subnets = []
        if m.get('VpdSubnets') is not None:
            for k1 in m.get('VpdSubnets'):
                temp_model = main_models.CreateClusterRequestNetworksNewVpdInfoVpdSubnets()
                self.vpd_subnets.append(temp_model.from_map(k1))

        return self

class CreateClusterRequestNetworksNewVpdInfoVpdSubnets(DaraModel):
    def __init__(
        self,
        subnet_cidr: str = None,
        subnet_type: str = None,
        zone_id: str = None,
    ):
        # Subnet CIDR
        self.subnet_cidr = subnet_cidr
        # Subnet type
        self.subnet_type = subnet_type
        # Zone ID
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.subnet_cidr is not None:
            result['SubnetCidr'] = self.subnet_cidr

        if self.subnet_type is not None:
            result['SubnetType'] = self.subnet_type

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubnetCidr') is not None:
            self.subnet_cidr = m.get('SubnetCidr')

        if m.get('SubnetType') is not None:
            self.subnet_type = m.get('SubnetType')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateClusterRequestNetworksIpAllocationPolicy(DaraModel):
    def __init__(
        self,
        bond_policy: main_models.CreateClusterRequestNetworksIpAllocationPolicyBondPolicy = None,
        machine_type_policy: List[main_models.CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy] = None,
        node_policy: List[main_models.CreateClusterRequestNetworksIpAllocationPolicyNodePolicy] = None,
    ):
        # Bond policy
        self.bond_policy = bond_policy
        # Machine type allocation policy
        self.machine_type_policy = machine_type_policy
        # Node allocation policy
        self.node_policy = node_policy

    def validate(self):
        if self.bond_policy:
            self.bond_policy.validate()
        if self.machine_type_policy:
            for v1 in self.machine_type_policy:
                 if v1:
                    v1.validate()
        if self.node_policy:
            for v1 in self.node_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond_policy is not None:
            result['BondPolicy'] = self.bond_policy.to_map()

        result['MachineTypePolicy'] = []
        if self.machine_type_policy is not None:
            for k1 in self.machine_type_policy:
                result['MachineTypePolicy'].append(k1.to_map() if k1 else None)

        result['NodePolicy'] = []
        if self.node_policy is not None:
            for k1 in self.node_policy:
                result['NodePolicy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondPolicy') is not None:
            temp_model = main_models.CreateClusterRequestNetworksIpAllocationPolicyBondPolicy()
            self.bond_policy = temp_model.from_map(m.get('BondPolicy'))

        self.machine_type_policy = []
        if m.get('MachineTypePolicy') is not None:
            for k1 in m.get('MachineTypePolicy'):
                temp_model = main_models.CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy()
                self.machine_type_policy.append(temp_model.from_map(k1))

        self.node_policy = []
        if m.get('NodePolicy') is not None:
            for k1 in m.get('NodePolicy'):
                temp_model = main_models.CreateClusterRequestNetworksIpAllocationPolicyNodePolicy()
                self.node_policy.append(temp_model.from_map(k1))

        return self

class CreateClusterRequestNetworksIpAllocationPolicyNodePolicy(DaraModel):
    def __init__(
        self,
        bonds: List[main_models.CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds] = None,
        node_id: str = None,
    ):
        # Bond information
        self.bonds = bonds
        # Node ID
        self.node_id = node_id

    def validate(self):
        if self.bonds:
            for v1 in self.bonds:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bonds'] = []
        if self.bonds is not None:
            for k1 in self.bonds:
                result['Bonds'].append(k1.to_map() if k1 else None)

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k1 in m.get('Bonds'):
                temp_model = main_models.CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds()
                self.bonds.append(temp_model.from_map(k1))

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

class CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds(DaraModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        # Bond name
        self.name = name
        # IP source subnet for the cluster
        self.subnet = subnet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.subnet is not None:
            result['Subnet'] = self.subnet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')

        return self

class CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy(DaraModel):
    def __init__(
        self,
        bonds: List[main_models.CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds] = None,
        machine_type: str = None,
    ):
        # Bond information
        self.bonds = bonds
        # Machine type
        self.machine_type = machine_type

    def validate(self):
        if self.bonds:
            for v1 in self.bonds:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bonds'] = []
        if self.bonds is not None:
            for k1 in self.bonds:
                result['Bonds'].append(k1.to_map() if k1 else None)

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k1 in m.get('Bonds'):
                temp_model = main_models.CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds()
                self.bonds.append(temp_model.from_map(k1))

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        return self

class CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds(DaraModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        # Bond name
        self.name = name
        # IP source subnet for the cluster
        self.subnet = subnet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.subnet is not None:
            result['Subnet'] = self.subnet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')

        return self

class CreateClusterRequestNetworksIpAllocationPolicyBondPolicy(DaraModel):
    def __init__(
        self,
        bond_default_subnet: str = None,
        bonds: List[main_models.CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds] = None,
    ):
        # Default bond subnet for the cluster
        self.bond_default_subnet = bond_default_subnet
        # Bond information
        self.bonds = bonds

    def validate(self):
        if self.bonds:
            for v1 in self.bonds:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bond_default_subnet is not None:
            result['BondDefaultSubnet'] = self.bond_default_subnet

        result['Bonds'] = []
        if self.bonds is not None:
            for k1 in self.bonds:
                result['Bonds'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondDefaultSubnet') is not None:
            self.bond_default_subnet = m.get('BondDefaultSubnet')

        self.bonds = []
        if m.get('Bonds') is not None:
            for k1 in m.get('Bonds'):
                temp_model = main_models.CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds()
                self.bonds.append(temp_model.from_map(k1))

        return self

class CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds(DaraModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        # Bond name
        self.name = name
        # IP source subnet for the cluster
        self.subnet = subnet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.subnet is not None:
            result['Subnet'] = self.subnet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')

        return self

class CreateClusterRequestComponents(DaraModel):
    def __init__(
        self,
        component_config: main_models.CreateClusterRequestComponentsComponentConfig = None,
        component_type: str = None,
    ):
        # Component configuration
        self.component_config = component_config
        # Component type
        self.component_type = component_type

    def validate(self):
        if self.component_config:
            self.component_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_config is not None:
            result['ComponentConfig'] = self.component_config.to_map()

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentConfig') is not None:
            temp_model = main_models.CreateClusterRequestComponentsComponentConfig()
            self.component_config = temp_model.from_map(m.get('ComponentConfig'))

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        return self

class CreateClusterRequestComponentsComponentConfig(DaraModel):
    def __init__(
        self,
        basic_args: Any = None,
        node_units: List[Any] = None,
    ):
        # Basic component parameters
        self.basic_args = basic_args
        # Node pool configuration, used to establish the correspondence between node groups and node pools. Required when ComponentType is "ACKEdge", otherwise it can be empty.
        self.node_units = node_units

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.basic_args is not None:
            result['BasicArgs'] = self.basic_args

        if self.node_units is not None:
            result['NodeUnits'] = self.node_units

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BasicArgs') is not None:
            self.basic_args = m.get('BasicArgs')

        if m.get('NodeUnits') is not None:
            self.node_units = m.get('NodeUnits')

        return self

