# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eflo_controller20221215 import models as main_models
from darabonba.model import DaraModel

class ExtendClusterRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        ip_allocation_policy: List[main_models.ExtendClusterRequestIpAllocationPolicy] = None,
        node_groups: List[main_models.ExtendClusterRequestNodeGroups] = None,
        v_switch_zone_id: str = None,
        vpd_subnets: List[str] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to skip failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The combined IP allocation policy. Each policy can use only one policy type, and multiple policies can be combined.
        self.ip_allocation_policy = ip_allocation_policy
        # The node groups.
        self.node_groups = node_groups
        # The zone ID of the vSwitch.
        self.v_switch_zone_id = v_switch_zone_id
        # The list of cluster subnets.
        self.vpd_subnets = vpd_subnets

    def validate(self):
        if self.ip_allocation_policy:
            for v1 in self.ip_allocation_policy:
                 if v1:
                    v1.validate()
        if self.node_groups:
            for v1 in self.node_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks

        result['IpAllocationPolicy'] = []
        if self.ip_allocation_policy is not None:
            for k1 in self.ip_allocation_policy:
                result['IpAllocationPolicy'].append(k1.to_map() if k1 else None)

        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k1 in self.node_groups:
                result['NodeGroups'].append(k1.to_map() if k1 else None)

        if self.v_switch_zone_id is not None:
            result['VSwitchZoneId'] = self.v_switch_zone_id

        if self.vpd_subnets is not None:
            result['VpdSubnets'] = self.vpd_subnets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')

        self.ip_allocation_policy = []
        if m.get('IpAllocationPolicy') is not None:
            for k1 in m.get('IpAllocationPolicy'):
                temp_model = main_models.ExtendClusterRequestIpAllocationPolicy()
                self.ip_allocation_policy.append(temp_model.from_map(k1))

        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k1 in m.get('NodeGroups'):
                temp_model = main_models.ExtendClusterRequestNodeGroups()
                self.node_groups.append(temp_model.from_map(k1))

        if m.get('VSwitchZoneId') is not None:
            self.v_switch_zone_id = m.get('VSwitchZoneId')

        if m.get('VpdSubnets') is not None:
            self.vpd_subnets = m.get('VpdSubnets')

        return self

class ExtendClusterRequestNodeGroups(DaraModel):
    def __init__(
        self,
        amount: int = None,
        auto_renew: bool = None,
        charge_type: str = None,
        hostnames: List[str] = None,
        hyper_nodes: List[main_models.ExtendClusterRequestNodeGroupsHyperNodes] = None,
        login_password: str = None,
        node_group_id: str = None,
        node_tag: List[main_models.ExtendClusterRequestNodeGroupsNodeTag] = None,
        nodes: List[main_models.ExtendClusterRequestNodeGroupsNodes] = None,
        period: int = None,
        savings_plan_id: str = None,
        user_data: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # The number of nodes to purchase. Valid values: 0 to 500. If Amount is set to 0, no nodes are purchased and existing nodes are used for scale-out. If Amount is set to a value from 1 to 500, the specified number of nodes are purchased and used for scale-out. Default value: 0
        self.amount = amount
        # Specifies whether to enable auto-renewal for the purchased nodes. This parameter takes effect when Amount is not 0 and ChargeType is set to PREPAY or POSTPAY. Valid values: True: Enable auto-renewal. False: Disable auto-renewal. Default value: False.
        self.auto_renew = auto_renew
        # The billing method of the nodes. This parameter does not take effect when Amount is set to 0. Valid values: PREPAY: subscription. POSTPAY: pay-as-you-go. Default value: PREPAY.
        self.charge_type = charge_type
        # The hostnames of the purchased nodes. This parameter does not take effect when Amount is set to 0.
        self.hostnames = hostnames
        # The list of hyper nodes.
        self.hyper_nodes = hyper_nodes
        # The logon password of the purchased nodes. This parameter does not take effect when Amount is set to 0.
        self.login_password = login_password
        # The node group ID.
        self.node_group_id = node_group_id
        # The node tags.
        self.node_tag = node_tag
        # The node list.
        self.nodes = nodes
        # The subscription duration of the purchased nodes. Unit: months. Valid values: 1, 6, 12, 24, 36, and 48. This parameter takes effect when Amount is not 0 and ChargeType is set to PREPAY.
        self.period = period
        # The savings plan ID.
        self.savings_plan_id = savings_plan_id
        # The custom executable shell script. The script must be Base64-encoded. The maximum size of the raw data is 16 KB.
        self.user_data = user_data
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        self.vpc_id = vpc_id
        # The zone ID.
        self.zone_id = zone_id

    def validate(self):
        if self.hyper_nodes:
            for v1 in self.hyper_nodes:
                 if v1:
                    v1.validate()
        if self.node_tag:
            for v1 in self.node_tag:
                 if v1:
                    v1.validate()
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames

        result['HyperNodes'] = []
        if self.hyper_nodes is not None:
            for k1 in self.hyper_nodes:
                result['HyperNodes'].append(k1.to_map() if k1 else None)

        if self.login_password is not None:
            result['LoginPassword'] = self.login_password

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        result['NodeTag'] = []
        if self.node_tag is not None:
            for k1 in self.node_tag:
                result['NodeTag'].append(k1.to_map() if k1 else None)

        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.period is not None:
            result['Period'] = self.period

        if self.savings_plan_id is not None:
            result['SavingsPlanId'] = self.savings_plan_id

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')

        self.hyper_nodes = []
        if m.get('HyperNodes') is not None:
            for k1 in m.get('HyperNodes'):
                temp_model = main_models.ExtendClusterRequestNodeGroupsHyperNodes()
                self.hyper_nodes.append(temp_model.from_map(k1))

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        self.node_tag = []
        if m.get('NodeTag') is not None:
            for k1 in m.get('NodeTag'):
                temp_model = main_models.ExtendClusterRequestNodeGroupsNodeTag()
                self.node_tag.append(temp_model.from_map(k1))

        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.ExtendClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('SavingsPlanId') is not None:
            self.savings_plan_id = m.get('SavingsPlanId')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ExtendClusterRequestNodeGroupsNodes(DaraModel):
    def __init__(
        self,
        data_disk: List[main_models.ExtendClusterRequestNodeGroupsNodesDataDisk] = None,
        hostname: str = None,
        login_password: str = None,
        node_id: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The data cloud disk specifications.
        self.data_disk = data_disk
        # The hostname.
        self.hostname = hostname
        # The logon password.
        self.login_password = login_password
        # The node ID.
        self.node_id = node_id
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
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

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

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
                temp_model = main_models.ExtendClusterRequestNodeGroupsNodesDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ExtendClusterRequestNodeGroupsNodesDataDisk(DaraModel):
    def __init__(
        self,
        bursting_enabled: bool = None,
        category: str = None,
        delete_with_node: bool = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        # Specifies whether to enable burst (I/O burst).
        self.bursting_enabled = bursting_enabled
        # The type.
        self.category = category
        # Specifies whether the data cloud disk is deleted when the node is unsubscribed.
        self.delete_with_node = delete_with_node
        # The performance metric of the data cloud disk.
        self.performance_level = performance_level
        # The provisioned performance (IOPS). Valid values: 0 to 50000.
        self.provisioned_iops = provisioned_iops
        # The cloud disk size.
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

class ExtendClusterRequestNodeGroupsNodeTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the node.
        self.key = key
        # The tag value of the node.
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

class ExtendClusterRequestNodeGroupsHyperNodes(DaraModel):
    def __init__(
        self,
        data_disk: List[main_models.ExtendClusterRequestNodeGroupsHyperNodesDataDisk] = None,
        hostname: str = None,
        hyper_node_id: str = None,
        login_password: str = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The list of cloud disk information.
        self.data_disk = data_disk
        # The hostname.
        self.hostname = hostname
        # The hyper node ID.
        self.hyper_node_id = hyper_node_id
        # The logon password.
        self.login_password = login_password
        # The security group ID.
        self.security_group_id = security_group_id
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
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

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

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
                temp_model = main_models.ExtendClusterRequestNodeGroupsHyperNodesDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('HyperNodeId') is not None:
            self.hyper_node_id = m.get('HyperNodeId')

        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ExtendClusterRequestNodeGroupsHyperNodesDataDisk(DaraModel):
    def __init__(
        self,
        bursting_enabled: bool = None,
        category: str = None,
        delete_with_node: bool = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        # Specifies whether to enable burst (I/O burst).
        self.bursting_enabled = bursting_enabled
        # The cloud disk type. Valid values:
        # 
        #  - cloud_essd: ESSD.
        self.category = category
        # Specifies whether the data cloud disk is deleted when the node is unsubscribed.
        self.delete_with_node = delete_with_node
        # The performance level (PL) when an ESSD is used as a system cloud disk. Valid values:
        # - PL0: a maximum of 10,000 random read/write IOPS per disk.
        # - PL1: a maximum of 50,000 random read/write IOPS per disk.
        self.performance_level = performance_level
        # The provisioned performance (read/write IOPS) of a single ESSD AutoPL cloud disk.
        self.provisioned_iops = provisioned_iops
        # The cloud disk size. Unit: GiB.
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

class ExtendClusterRequestIpAllocationPolicy(DaraModel):
    def __init__(
        self,
        bond_policy: main_models.ExtendClusterRequestIpAllocationPolicyBondPolicy = None,
        machine_type_policy: List[main_models.ExtendClusterRequestIpAllocationPolicyMachineTypePolicy] = None,
        node_policy: List[main_models.ExtendClusterRequestIpAllocationPolicyNodePolicy] = None,
    ):
        # Specifies the cluster subnet ID based on the bond name.
        self.bond_policy = bond_policy
        # The machine type allocation policy.
        self.machine_type_policy = machine_type_policy
        # The node allocation policy.
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
            temp_model = main_models.ExtendClusterRequestIpAllocationPolicyBondPolicy()
            self.bond_policy = temp_model.from_map(m.get('BondPolicy'))

        self.machine_type_policy = []
        if m.get('MachineTypePolicy') is not None:
            for k1 in m.get('MachineTypePolicy'):
                temp_model = main_models.ExtendClusterRequestIpAllocationPolicyMachineTypePolicy()
                self.machine_type_policy.append(temp_model.from_map(k1))

        self.node_policy = []
        if m.get('NodePolicy') is not None:
            for k1 in m.get('NodePolicy'):
                temp_model = main_models.ExtendClusterRequestIpAllocationPolicyNodePolicy()
                self.node_policy.append(temp_model.from_map(k1))

        return self

class ExtendClusterRequestIpAllocationPolicyNodePolicy(DaraModel):
    def __init__(
        self,
        bonds: List[main_models.ExtendClusterRequestIpAllocationPolicyNodePolicyBonds] = None,
        hostname: str = None,
        node_id: str = None,
    ):
        # The bond information.
        self.bonds = bonds
        # The hostname.
        self.hostname = hostname
        # The node ID.
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

        if self.hostname is not None:
            result['Hostname'] = self.hostname

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k1 in m.get('Bonds'):
                temp_model = main_models.ExtendClusterRequestIpAllocationPolicyNodePolicyBonds()
                self.bonds.append(temp_model.from_map(k1))

        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        return self

class ExtendClusterRequestIpAllocationPolicyNodePolicyBonds(DaraModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        # The bond name.
        self.name = name
        # The cluster subnet from which the IP address is allocated.
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

class ExtendClusterRequestIpAllocationPolicyMachineTypePolicy(DaraModel):
    def __init__(
        self,
        bonds: List[main_models.ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds] = None,
        machine_type: str = None,
    ):
        # The bond information.
        self.bonds = bonds
        # The machine type.
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
                temp_model = main_models.ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds()
                self.bonds.append(temp_model.from_map(k1))

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        return self

class ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds(DaraModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        # The bond name.
        self.name = name
        # The cluster subnet from which the IP address is allocated.
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

class ExtendClusterRequestIpAllocationPolicyBondPolicy(DaraModel):
    def __init__(
        self,
        bond_default_subnet: str = None,
        bonds: List[main_models.ExtendClusterRequestIpAllocationPolicyBondPolicyBonds] = None,
    ):
        # The default bond cluster subnet.
        self.bond_default_subnet = bond_default_subnet
        # The bond information.
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
                temp_model = main_models.ExtendClusterRequestIpAllocationPolicyBondPolicyBonds()
                self.bonds.append(temp_model.from_map(k1))

        return self

class ExtendClusterRequestIpAllocationPolicyBondPolicyBonds(DaraModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        # The bond name.
        self.name = name
        # The cluster subnet from which the IP address is allocated.
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

