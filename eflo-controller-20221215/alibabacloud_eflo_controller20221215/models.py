# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class ApproveOperationRequest(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        operation_type: str = None,
    ):
        self.node_id = node_id
        self.operation_type = operation_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        return self


class ApproveOperationResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        request_id: str = None,
    ):
        self.error_message = error_message
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApproveOperationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ApproveOperationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ApproveOperationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_region_id = resource_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequestComponentsComponentConfig(TeaModel):
    def __init__(
        self,
        basic_args: Any = None,
        node_units: List[Any] = None,
    ):
        self.basic_args = basic_args
        self.node_units = node_units

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestComponents(TeaModel):
    def __init__(
        self,
        component_config: CreateClusterRequestComponentsComponentConfig = None,
        component_type: str = None,
    ):
        self.component_config = component_config
        self.component_type = component_type

    def validate(self):
        if self.component_config:
            self.component_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_config is not None:
            result['ComponentConfig'] = self.component_config.to_map()
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentConfig') is not None:
            temp_model = CreateClusterRequestComponentsComponentConfig()
            self.component_config = temp_model.from_map(m['ComponentConfig'])
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        return self


class CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds(TeaModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        self.name = name
        self.subnet = subnet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestNetworksIpAllocationPolicyBondPolicy(TeaModel):
    def __init__(
        self,
        bond_default_subnet: str = None,
        bonds: List[CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds] = None,
    ):
        self.bond_default_subnet = bond_default_subnet
        self.bonds = bonds

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_default_subnet is not None:
            result['BondDefaultSubnet'] = self.bond_default_subnet
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondDefaultSubnet') is not None:
            self.bond_default_subnet = m.get('BondDefaultSubnet')
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyBondPolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        return self


class CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds(TeaModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        self.name = name
        self.subnet = subnet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy(TeaModel):
    def __init__(
        self,
        bonds: List[CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds] = None,
        machine_type: str = None,
    ):
        self.bonds = bonds
        self.machine_type = machine_type

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        return self


class CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds(TeaModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        self.name = name
        self.subnet = subnet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestNetworksIpAllocationPolicyNodePolicy(TeaModel):
    def __init__(
        self,
        bonds: List[CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds] = None,
        node_id: str = None,
    ):
        self.bonds = bonds
        self.node_id = node_id

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyNodePolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateClusterRequestNetworksIpAllocationPolicy(TeaModel):
    def __init__(
        self,
        bond_policy: CreateClusterRequestNetworksIpAllocationPolicyBondPolicy = None,
        machine_type_policy: List[CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy] = None,
        node_policy: List[CreateClusterRequestNetworksIpAllocationPolicyNodePolicy] = None,
    ):
        self.bond_policy = bond_policy
        self.machine_type_policy = machine_type_policy
        self.node_policy = node_policy

    def validate(self):
        if self.bond_policy:
            self.bond_policy.validate()
        if self.machine_type_policy:
            for k in self.machine_type_policy:
                if k:
                    k.validate()
        if self.node_policy:
            for k in self.node_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_policy is not None:
            result['BondPolicy'] = self.bond_policy.to_map()
        result['MachineTypePolicy'] = []
        if self.machine_type_policy is not None:
            for k in self.machine_type_policy:
                result['MachineTypePolicy'].append(k.to_map() if k else None)
        result['NodePolicy'] = []
        if self.node_policy is not None:
            for k in self.node_policy:
                result['NodePolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondPolicy') is not None:
            temp_model = CreateClusterRequestNetworksIpAllocationPolicyBondPolicy()
            self.bond_policy = temp_model.from_map(m['BondPolicy'])
        self.machine_type_policy = []
        if m.get('MachineTypePolicy') is not None:
            for k in m.get('MachineTypePolicy'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyMachineTypePolicy()
                self.machine_type_policy.append(temp_model.from_map(k))
        self.node_policy = []
        if m.get('NodePolicy') is not None:
            for k in m.get('NodePolicy'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicyNodePolicy()
                self.node_policy.append(temp_model.from_map(k))
        return self


class CreateClusterRequestNetworksNewVpdInfoVpdSubnets(TeaModel):
    def __init__(
        self,
        subnet_cidr: str = None,
        subnet_type: str = None,
        zone_id: str = None,
    ):
        self.subnet_cidr = subnet_cidr
        self.subnet_type = subnet_type
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestNetworksNewVpdInfo(TeaModel):
    def __init__(
        self,
        cen_id: str = None,
        cloud_link_cidr: str = None,
        cloud_link_id: str = None,
        monitor_vpc_id: str = None,
        monitor_vswitch_id: str = None,
        vpd_cidr: str = None,
        vpd_subnets: List[CreateClusterRequestNetworksNewVpdInfoVpdSubnets] = None,
    ):
        self.cen_id = cen_id
        self.cloud_link_cidr = cloud_link_cidr
        self.cloud_link_id = cloud_link_id
        self.monitor_vpc_id = monitor_vpc_id
        self.monitor_vswitch_id = monitor_vswitch_id
        self.vpd_cidr = vpd_cidr
        self.vpd_subnets = vpd_subnets

    def validate(self):
        if self.vpd_subnets:
            for k in self.vpd_subnets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            for k in self.vpd_subnets:
                result['VpdSubnets'].append(k.to_map() if k else None)
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
            for k in m.get('VpdSubnets'):
                temp_model = CreateClusterRequestNetworksNewVpdInfoVpdSubnets()
                self.vpd_subnets.append(temp_model.from_map(k))
        return self


class CreateClusterRequestNetworksVpdInfo(TeaModel):
    def __init__(
        self,
        vpd_id: str = None,
        vpd_subnets: List[str] = None,
    ):
        # 专有网络 id
        self.vpd_id = vpd_id
        # 集群子网id列表
        self.vpd_subnets = vpd_subnets

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestNetworks(TeaModel):
    def __init__(
        self,
        ip_allocation_policy: List[CreateClusterRequestNetworksIpAllocationPolicy] = None,
        new_vpd_info: CreateClusterRequestNetworksNewVpdInfo = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        v_switch_zone_id: str = None,
        vpc_id: str = None,
        vpd_info: CreateClusterRequestNetworksVpdInfo = None,
    ):
        self.ip_allocation_policy = ip_allocation_policy
        self.new_vpd_info = new_vpd_info
        self.security_group_id = security_group_id
        self.v_switch_id = v_switch_id
        self.v_switch_zone_id = v_switch_zone_id
        self.vpc_id = vpc_id
        # 复用VPD信息
        self.vpd_info = vpd_info

    def validate(self):
        if self.ip_allocation_policy:
            for k in self.ip_allocation_policy:
                if k:
                    k.validate()
        if self.new_vpd_info:
            self.new_vpd_info.validate()
        if self.vpd_info:
            self.vpd_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['IpAllocationPolicy'] = []
        if self.ip_allocation_policy is not None:
            for k in self.ip_allocation_policy:
                result['IpAllocationPolicy'].append(k.to_map() if k else None)
        if self.new_vpd_info is not None:
            result['NewVpdInfo'] = self.new_vpd_info.to_map()
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id
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
            for k in m.get('IpAllocationPolicy'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicy()
                self.ip_allocation_policy.append(temp_model.from_map(k))
        if m.get('NewVpdInfo') is not None:
            temp_model = CreateClusterRequestNetworksNewVpdInfo()
            self.new_vpd_info = temp_model.from_map(m['NewVpdInfo'])
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VSwitchZoneId') is not None:
            self.v_switch_zone_id = m.get('VSwitchZoneId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VpdInfo') is not None:
            temp_model = CreateClusterRequestNetworksVpdInfo()
            self.vpd_info = temp_model.from_map(m['VpdInfo'])
        return self


class CreateClusterRequestNodeGroupsNodes(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        login_password: str = None,
        node_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.hostname = hostname
        self.login_password = login_password
        self.node_id = node_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestNodeGroups(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        machine_type: str = None,
        node_group_description: str = None,
        node_group_name: str = None,
        nodes: List[CreateClusterRequestNodeGroupsNodes] = None,
        user_data: str = None,
        zone_id: str = None,
    ):
        self.image_id = image_id
        self.machine_type = machine_type
        self.node_group_description = node_group_description
        self.node_group_name = node_group_name
        self.nodes = nodes
        self.user_data = user_data
        self.zone_id = zone_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.node_group_description is not None:
            result['NodeGroupDescription'] = self.node_group_description
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('NodeGroupDescription') is not None:
            self.node_group_description = m.get('NodeGroupDescription')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = CreateClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class CreateClusterRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_description: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        components: List[CreateClusterRequestComponents] = None,
        hpn_zone: str = None,
        ignore_failed_node_tasks: bool = None,
        networks: CreateClusterRequestNetworks = None,
        nimiz_vswitches: List[str] = None,
        node_groups: List[CreateClusterRequestNodeGroups] = None,
        resource_group_id: str = None,
        tag: List[CreateClusterRequestTag] = None,
    ):
        self.cluster_description = cluster_description
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.components = components
        self.hpn_zone = hpn_zone
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.networks = networks
        self.nimiz_vswitches = nimiz_vswitches
        self.node_groups = node_groups
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()
        if self.networks:
            self.networks.validate()
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
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
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
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
            for k in m.get('Components'):
                temp_model = CreateClusterRequestComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Networks') is not None:
            temp_model = CreateClusterRequestNetworks()
            self.networks = temp_model.from_map(m['Networks'])
        if m.get('NimizVSwitches') is not None:
            self.nimiz_vswitches = m.get('NimizVSwitches')
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = CreateClusterRequestNodeGroups()
                self.node_groups.append(temp_model.from_map(k))
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateClusterRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateClusterShrinkRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_description: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        components_shrink: str = None,
        hpn_zone: str = None,
        ignore_failed_node_tasks: bool = None,
        networks_shrink: str = None,
        nimiz_vswitches_shrink: str = None,
        node_groups_shrink: str = None,
        resource_group_id: str = None,
        tag: List[CreateClusterShrinkRequestTag] = None,
    ):
        self.cluster_description = cluster_description
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.components_shrink = components_shrink
        self.hpn_zone = hpn_zone
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.networks_shrink = networks_shrink
        self.nimiz_vswitches_shrink = nimiz_vswitches_shrink
        self.node_groups_shrink = node_groups_shrink
        self.resource_group_id = resource_group_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.components_shrink is not None:
            result['Components'] = self.components_shrink
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.networks_shrink is not None:
            result['Networks'] = self.networks_shrink
        if self.nimiz_vswitches_shrink is not None:
            result['NimizVSwitches'] = self.nimiz_vswitches_shrink
        if self.node_groups_shrink is not None:
            result['NodeGroups'] = self.node_groups_shrink
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Components') is not None:
            self.components_shrink = m.get('Components')
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Networks') is not None:
            self.networks_shrink = m.get('Networks')
        if m.get('NimizVSwitches') is not None:
            self.nimiz_vswitches_shrink = m.get('NimizVSwitches')
        if m.get('NodeGroups') is not None:
            self.node_groups_shrink = m.get('NodeGroups')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateClusterShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        return self


class DescribeClusterResponseBodyComponents(TeaModel):
    def __init__(
        self,
        component_id: str = None,
        component_type: str = None,
    ):
        self.component_id = component_id
        self.component_type = component_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_id is not None:
            result['ComponentId'] = self.component_id
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        return self


class DescribeClusterResponseBodyNetworks(TeaModel):
    def __init__(
        self,
        vpd_id: str = None,
    ):
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpd_id is not None:
            result['VpdId'] = self.vpd_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpdId') is not None:
            self.vpd_id = m.get('VpdId')
        return self


class DescribeClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        components: List[DescribeClusterResponseBodyComponents] = None,
        create_time: str = None,
        hpn_zone: str = None,
        networks: List[DescribeClusterResponseBodyNetworks] = None,
        node_count: int = None,
        node_group_count: int = None,
        operating_state: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        task_id: str = None,
        update_time: str = None,
        vpc_id: str = None,
    ):
        self.cluster_description = cluster_description
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.components = components
        self.create_time = create_time
        self.hpn_zone = hpn_zone
        self.networks = networks
        self.node_count = node_count
        self.node_group_count = node_group_count
        self.operating_state = operating_state
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.task_id = task_id
        self.update_time = update_time
        self.vpc_id = vpc_id

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()
        if self.networks:
            for k in self.networks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        result['Components'] = []
        if self.components is not None:
            for k in self.components:
                result['Components'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone
        result['Networks'] = []
        if self.networks is not None:
            for k in self.networks:
                result['Networks'].append(k.to_map() if k else None)
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_count is not None:
            result['NodeGroupCount'] = self.node_group_count
        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        self.components = []
        if m.get('Components') is not None:
            for k in m.get('Components'):
                temp_model = DescribeClusterResponseBodyComponents()
                self.components.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        self.networks = []
        if m.get('Networks') is not None:
            for k in m.get('Networks'):
                temp_model = DescribeClusterResponseBodyNetworks()
                self.networks.append(temp_model.from_map(k))
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupCount') is not None:
            self.node_group_count = m.get('NodeGroupCount')
        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class DescribeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInvocationsRequest(TeaModel):
    def __init__(
        self,
        content_encoding: str = None,
        include_output: bool = None,
        invoke_id: str = None,
        node_id: str = None,
    ):
        self.content_encoding = content_encoding
        self.include_output = include_output
        self.invoke_id = invoke_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.include_output is not None:
            result['IncludeOutput'] = self.include_output
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('IncludeOutput') is not None:
            self.include_output = m.get('IncludeOutput')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodesInvokeNode(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        dropped: int = None,
        error_code: bool = None,
        error_info: str = None,
        exit_code: int = None,
        finish_time: str = None,
        invocation_status: str = None,
        node_id: str = None,
        node_invoke_status: str = None,
        output: str = None,
        repeats: int = None,
        start_time: str = None,
        stop_time: str = None,
        timed: str = None,
        update_time: str = None,
    ):
        self.creation_time = creation_time
        self.dropped = dropped
        self.error_code = error_code
        self.error_info = error_info
        self.exit_code = exit_code
        self.finish_time = finish_time
        self.invocation_status = invocation_status
        self.node_id = node_id
        self.node_invoke_status = node_invoke_status
        self.output = output
        self.repeats = repeats
        self.start_time = start_time
        self.stop_time = stop_time
        self.timed = timed
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.dropped is not None:
            result['Dropped'] = self.dropped
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.node_invoke_status is not None:
            result['NodeInvokeStatus'] = self.node_invoke_status
        if self.output is not None:
            result['Output'] = self.output
        if self.repeats is not None:
            result['Repeats'] = self.repeats
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.stop_time is not None:
            result['StopTime'] = self.stop_time
        if self.timed is not None:
            result['Timed'] = self.timed
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Dropped') is not None:
            self.dropped = m.get('Dropped')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('NodeInvokeStatus') is not None:
            self.node_invoke_status = m.get('NodeInvokeStatus')
        if m.get('Output') is not None:
            self.output = m.get('Output')
        if m.get('Repeats') is not None:
            self.repeats = m.get('Repeats')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StopTime') is not None:
            self.stop_time = m.get('StopTime')
        if m.get('Timed') is not None:
            self.timed = m.get('Timed')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodes(TeaModel):
    def __init__(
        self,
        invoke_node: List[DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodesInvokeNode] = None,
    ):
        self.invoke_node = invoke_node

    def validate(self):
        if self.invoke_node:
            for k in self.invoke_node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InvokeNode'] = []
        if self.invoke_node is not None:
            for k in self.invoke_node:
                result['InvokeNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invoke_node = []
        if m.get('InvokeNode') is not None:
            for k in m.get('InvokeNode'):
                temp_model = DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodesInvokeNode()
                self.invoke_node.append(temp_model.from_map(k))
        return self


class DescribeInvocationsResponseBodyInvocationsInvocation(TeaModel):
    def __init__(
        self,
        command_content: str = None,
        command_description: str = None,
        command_name: str = None,
        creation_time: str = None,
        frequency: str = None,
        invocation_status: str = None,
        invoke_id: str = None,
        invoke_nodes: DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodes = None,
        invoke_status: str = None,
        parameters: str = None,
        repeat_mode: str = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        self.command_content = command_content
        self.command_description = command_description
        self.command_name = command_name
        self.creation_time = creation_time
        self.frequency = frequency
        self.invocation_status = invocation_status
        self.invoke_id = invoke_id
        self.invoke_nodes = invoke_nodes
        self.invoke_status = invoke_status
        self.parameters = parameters
        self.repeat_mode = repeat_mode
        self.timeout = timeout
        self.username = username
        self.working_dir = working_dir

    def validate(self):
        if self.invoke_nodes:
            self.invoke_nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.command_description is not None:
            result['CommandDescription'] = self.command_description
        if self.command_name is not None:
            result['CommandName'] = self.command_name
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.invoke_nodes is not None:
            result['InvokeNodes'] = self.invoke_nodes.to_map()
        if self.invoke_status is not None:
            result['InvokeStatus'] = self.invoke_status
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.username is not None:
            result['Username'] = self.username
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('CommandDescription') is not None:
            self.command_description = m.get('CommandDescription')
        if m.get('CommandName') is not None:
            self.command_name = m.get('CommandName')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('InvokeNodes') is not None:
            temp_model = DescribeInvocationsResponseBodyInvocationsInvocationInvokeNodes()
            self.invoke_nodes = temp_model.from_map(m['InvokeNodes'])
        if m.get('InvokeStatus') is not None:
            self.invoke_status = m.get('InvokeStatus')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class DescribeInvocationsResponseBodyInvocations(TeaModel):
    def __init__(
        self,
        invocation: List[DescribeInvocationsResponseBodyInvocationsInvocation] = None,
    ):
        self.invocation = invocation

    def validate(self):
        if self.invocation:
            for k in self.invocation:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Invocation'] = []
        if self.invocation is not None:
            for k in self.invocation:
                result['Invocation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocation = []
        if m.get('Invocation') is not None:
            for k in m.get('Invocation'):
                temp_model = DescribeInvocationsResponseBodyInvocationsInvocation()
                self.invocation.append(temp_model.from_map(k))
        return self


class DescribeInvocationsResponseBody(TeaModel):
    def __init__(
        self,
        invocations: DescribeInvocationsResponseBodyInvocations = None,
        request_id: str = None,
    ):
        self.invocations = invocations
        self.request_id = request_id

    def validate(self):
        if self.invocations:
            self.invocations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invocations is not None:
            result['Invocations'] = self.invocations.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Invocations') is not None:
            temp_model = DescribeInvocationsResponseBodyInvocations()
            self.invocations = temp_model.from_map(m['Invocations'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInvocationsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeInvocationsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeInvocationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeRequest(TeaModel):
    def __init__(
        self,
        node_id: str = None,
    ):
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeNodeResponseBodyNetworks(TeaModel):
    def __init__(
        self,
        bond_name: str = None,
        ip: str = None,
        subnet_id: str = None,
        vpd_id: str = None,
    ):
        self.bond_name = bond_name
        self.ip = ip
        self.subnet_id = subnet_id
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeNodeResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: str = None,
        expired_time: str = None,
        hostname: str = None,
        hpn_zone: str = None,
        image_id: str = None,
        image_name: str = None,
        machine_type: str = None,
        networks: List[DescribeNodeResponseBodyNetworks] = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_id: str = None,
        operating_state: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        sn: str = None,
        zone_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.create_time = create_time
        self.expired_time = expired_time
        self.hostname = hostname
        self.hpn_zone = hpn_zone
        self.image_id = image_id
        # 镜像名称
        self.image_name = image_name
        self.machine_type = machine_type
        self.networks = networks
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.node_id = node_id
        self.operating_state = operating_state
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.sn = sn
        self.zone_id = zone_id

    def validate(self):
        if self.networks:
            for k in self.networks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        result['Networks'] = []
        if self.networks is not None:
            for k in self.networks:
                result['Networks'].append(k.to_map() if k else None)
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sn is not None:
            result['Sn'] = self.sn
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
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        self.networks = []
        if m.get('Networks') is not None:
            for k in m.get('Networks'):
                temp_model = DescribeNodeResponseBodyNetworks()
                self.networks.append(temp_model.from_map(k))
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeNodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNodeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSendFileResultsRequest(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        node_id: str = None,
    ):
        self.invoke_id = invoke_id
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodesInvokeNode(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        error_code: str = None,
        error_info: str = None,
        finish_time: str = None,
        invocation_status: str = None,
        node_id: str = None,
        start_time: str = None,
        update_time: str = None,
    ):
        self.creation_time = creation_time
        self.error_code = error_code
        self.error_info = error_info
        self.finish_time = finish_time
        self.invocation_status = invocation_status
        self.node_id = node_id
        self.start_time = start_time
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_info is not None:
            result['ErrorInfo'] = self.error_info
        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorInfo') is not None:
            self.error_info = m.get('ErrorInfo')
        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodes(TeaModel):
    def __init__(
        self,
        invoke_node: List[DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodesInvokeNode] = None,
    ):
        self.invoke_node = invoke_node

    def validate(self):
        if self.invoke_node:
            for k in self.invoke_node:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InvokeNode'] = []
        if self.invoke_node is not None:
            for k in self.invoke_node:
                result['InvokeNode'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invoke_node = []
        if m.get('InvokeNode') is not None:
            for k in m.get('InvokeNode'):
                temp_model = DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodesInvokeNode()
                self.invoke_node.append(temp_model.from_map(k))
        return self


class DescribeSendFileResultsResponseBodyInvocationsInvocation(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        creation_time: str = None,
        description: str = None,
        file_group: str = None,
        file_mode: str = None,
        file_owner: str = None,
        invocation_status: str = None,
        invoke_nodes: DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodes = None,
        name: str = None,
        node_count: int = None,
        overwrite: bool = None,
        target_dir: str = None,
    ):
        self.content = content
        self.content_type = content_type
        self.creation_time = creation_time
        self.description = description
        self.file_group = file_group
        self.file_mode = file_mode
        self.file_owner = file_owner
        self.invocation_status = invocation_status
        self.invoke_nodes = invoke_nodes
        self.name = name
        self.node_count = node_count
        self.overwrite = overwrite
        self.target_dir = target_dir

    def validate(self):
        if self.invoke_nodes:
            self.invoke_nodes.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.description is not None:
            result['Description'] = self.description
        if self.file_group is not None:
            result['FileGroup'] = self.file_group
        if self.file_mode is not None:
            result['FileMode'] = self.file_mode
        if self.file_owner is not None:
            result['FileOwner'] = self.file_owner
        if self.invocation_status is not None:
            result['InvocationStatus'] = self.invocation_status
        if self.invoke_nodes is not None:
            result['InvokeNodes'] = self.invoke_nodes.to_map()
        if self.name is not None:
            result['Name'] = self.name
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileGroup') is not None:
            self.file_group = m.get('FileGroup')
        if m.get('FileMode') is not None:
            self.file_mode = m.get('FileMode')
        if m.get('FileOwner') is not None:
            self.file_owner = m.get('FileOwner')
        if m.get('InvocationStatus') is not None:
            self.invocation_status = m.get('InvocationStatus')
        if m.get('InvokeNodes') is not None:
            temp_model = DescribeSendFileResultsResponseBodyInvocationsInvocationInvokeNodes()
            self.invoke_nodes = temp_model.from_map(m['InvokeNodes'])
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')
        return self


class DescribeSendFileResultsResponseBodyInvocations(TeaModel):
    def __init__(
        self,
        invocation: List[DescribeSendFileResultsResponseBodyInvocationsInvocation] = None,
    ):
        self.invocation = invocation

    def validate(self):
        if self.invocation:
            for k in self.invocation:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Invocation'] = []
        if self.invocation is not None:
            for k in self.invocation:
                result['Invocation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.invocation = []
        if m.get('Invocation') is not None:
            for k in m.get('Invocation'):
                temp_model = DescribeSendFileResultsResponseBodyInvocationsInvocation()
                self.invocation.append(temp_model.from_map(k))
        return self


class DescribeSendFileResultsResponseBody(TeaModel):
    def __init__(
        self,
        invocations: DescribeSendFileResultsResponseBodyInvocations = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.invocations = invocations
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.invocations:
            self.invocations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invocations is not None:
            result['Invocations'] = self.invocations.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Invocations') is not None:
            temp_model = DescribeSendFileResultsResponseBodyInvocations()
            self.invocations = temp_model.from_map(m['Invocations'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeSendFileResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSendFileResultsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeSendFileResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DescribeTaskResponseBodyStepsSubTasks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        message: str = None,
        task_id: str = None,
        task_state: str = None,
        task_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.message = message
        self.task_id = task_id
        self.task_state = task_state
        self.task_type = task_type
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.message is not None:
            result['Message'] = self.message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeTaskResponseBodySteps(TeaModel):
    def __init__(
        self,
        message: str = None,
        stage_tag: str = None,
        start_time: str = None,
        step_name: str = None,
        step_state: str = None,
        step_type: str = None,
        sub_tasks: List[DescribeTaskResponseBodyStepsSubTasks] = None,
        update_time: str = None,
    ):
        self.message = message
        self.stage_tag = stage_tag
        self.start_time = start_time
        self.step_name = step_name
        self.step_state = step_state
        self.step_type = step_type
        self.sub_tasks = sub_tasks
        self.update_time = update_time

    def validate(self):
        if self.sub_tasks:
            for k in self.sub_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.stage_tag is not None:
            result['StageTag'] = self.stage_tag
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.step_name is not None:
            result['StepName'] = self.step_name
        if self.step_state is not None:
            result['StepState'] = self.step_state
        if self.step_type is not None:
            result['StepType'] = self.step_type
        result['SubTasks'] = []
        if self.sub_tasks is not None:
            for k in self.sub_tasks:
                result['SubTasks'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('StageTag') is not None:
            self.stage_tag = m.get('StageTag')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('StepName') is not None:
            self.step_name = m.get('StepName')
        if m.get('StepState') is not None:
            self.step_state = m.get('StepState')
        if m.get('StepType') is not None:
            self.step_type = m.get('StepType')
        self.sub_tasks = []
        if m.get('SubTasks') is not None:
            for k in m.get('SubTasks'):
                temp_model = DescribeTaskResponseBodyStepsSubTasks()
                self.sub_tasks.append(temp_model.from_map(k))
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeTaskResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: str = None,
        message: str = None,
        node_ids: List[str] = None,
        request_id: str = None,
        steps: List[DescribeTaskResponseBodySteps] = None,
        task_state: str = None,
        task_type: str = None,
        update_time: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.create_time = create_time
        self.message = message
        self.node_ids = node_ids
        self.request_id = request_id
        self.steps = steps
        self.task_state = task_state
        self.task_type = task_type
        self.update_time = update_time

    def validate(self):
        if self.steps:
            for k in self.steps:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.message is not None:
            result['Message'] = self.message
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Steps'] = []
        if self.steps is not None:
            for k in self.steps:
                result['Steps'].append(k.to_map() if k else None)
        if self.task_state is not None:
            result['TaskState'] = self.task_state
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.steps = []
        if m.get('Steps') is not None:
            for k in m.get('Steps'):
                temp_model = DescribeTaskResponseBodySteps()
                self.steps.append(temp_model.from_map(k))
        if m.get('TaskState') is not None:
            self.task_state = m.get('TaskState')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DescribeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        self.accept_language = accept_language

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeZonesResponseBodyZones(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        self.local_name = local_name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class DescribeZonesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        zones: List[DescribeZonesResponseBodyZones] = None,
    ):
        self.request_id = request_id
        self.zones = zones

    def validate(self):
        if self.zones:
            for k in self.zones:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Zones'] = []
        if self.zones is not None:
            for k in self.zones:
                result['Zones'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.zones = []
        if m.get('Zones') is not None:
            for k in m.get('Zones'):
                temp_model = DescribeZonesResponseBodyZones()
                self.zones.append(temp_model.from_map(k))
        return self


class DescribeZonesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeZonesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeZonesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExtendClusterRequestIpAllocationPolicyBondPolicyBonds(TeaModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        self.name = name
        self.subnet = subnet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ExtendClusterRequestIpAllocationPolicyBondPolicy(TeaModel):
    def __init__(
        self,
        bond_default_subnet: str = None,
        bonds: List[ExtendClusterRequestIpAllocationPolicyBondPolicyBonds] = None,
    ):
        self.bond_default_subnet = bond_default_subnet
        self.bonds = bonds

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_default_subnet is not None:
            result['BondDefaultSubnet'] = self.bond_default_subnet
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondDefaultSubnet') is not None:
            self.bond_default_subnet = m.get('BondDefaultSubnet')
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = ExtendClusterRequestIpAllocationPolicyBondPolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        return self


class ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds(TeaModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        self.name = name
        self.subnet = subnet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ExtendClusterRequestIpAllocationPolicyMachineTypePolicy(TeaModel):
    def __init__(
        self,
        bonds: List[ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds] = None,
        machine_type: str = None,
    ):
        self.bonds = bonds
        self.machine_type = machine_type

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = ExtendClusterRequestIpAllocationPolicyMachineTypePolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        return self


class ExtendClusterRequestIpAllocationPolicyNodePolicyBonds(TeaModel):
    def __init__(
        self,
        name: str = None,
        subnet: str = None,
    ):
        self.name = name
        self.subnet = subnet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ExtendClusterRequestIpAllocationPolicyNodePolicy(TeaModel):
    def __init__(
        self,
        bonds: List[ExtendClusterRequestIpAllocationPolicyNodePolicyBonds] = None,
        node_id: str = None,
    ):
        self.bonds = bonds
        self.node_id = node_id

    def validate(self):
        if self.bonds:
            for k in self.bonds:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Bonds'] = []
        if self.bonds is not None:
            for k in self.bonds:
                result['Bonds'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bonds = []
        if m.get('Bonds') is not None:
            for k in m.get('Bonds'):
                temp_model = ExtendClusterRequestIpAllocationPolicyNodePolicyBonds()
                self.bonds.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ExtendClusterRequestIpAllocationPolicy(TeaModel):
    def __init__(
        self,
        bond_policy: ExtendClusterRequestIpAllocationPolicyBondPolicy = None,
        machine_type_policy: List[ExtendClusterRequestIpAllocationPolicyMachineTypePolicy] = None,
        node_policy: List[ExtendClusterRequestIpAllocationPolicyNodePolicy] = None,
    ):
        self.bond_policy = bond_policy
        self.machine_type_policy = machine_type_policy
        self.node_policy = node_policy

    def validate(self):
        if self.bond_policy:
            self.bond_policy.validate()
        if self.machine_type_policy:
            for k in self.machine_type_policy:
                if k:
                    k.validate()
        if self.node_policy:
            for k in self.node_policy:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_policy is not None:
            result['BondPolicy'] = self.bond_policy.to_map()
        result['MachineTypePolicy'] = []
        if self.machine_type_policy is not None:
            for k in self.machine_type_policy:
                result['MachineTypePolicy'].append(k.to_map() if k else None)
        result['NodePolicy'] = []
        if self.node_policy is not None:
            for k in self.node_policy:
                result['NodePolicy'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondPolicy') is not None:
            temp_model = ExtendClusterRequestIpAllocationPolicyBondPolicy()
            self.bond_policy = temp_model.from_map(m['BondPolicy'])
        self.machine_type_policy = []
        if m.get('MachineTypePolicy') is not None:
            for k in m.get('MachineTypePolicy'):
                temp_model = ExtendClusterRequestIpAllocationPolicyMachineTypePolicy()
                self.machine_type_policy.append(temp_model.from_map(k))
        self.node_policy = []
        if m.get('NodePolicy') is not None:
            for k in m.get('NodePolicy'):
                temp_model = ExtendClusterRequestIpAllocationPolicyNodePolicy()
                self.node_policy.append(temp_model.from_map(k))
        return self


class ExtendClusterRequestNodeGroupsNodes(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        login_password: str = None,
        node_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.hostname = hostname
        self.login_password = login_password
        self.node_id = node_id
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ExtendClusterRequestNodeGroups(TeaModel):
    def __init__(
        self,
        node_group_id: str = None,
        nodes: List[ExtendClusterRequestNodeGroupsNodes] = None,
        user_data: str = None,
        zone_id: str = None,
    ):
        self.node_group_id = node_group_id
        self.nodes = nodes
        self.user_data = user_data
        self.zone_id = zone_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ExtendClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ExtendClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        ip_allocation_policy: List[ExtendClusterRequestIpAllocationPolicy] = None,
        node_groups: List[ExtendClusterRequestNodeGroups] = None,
        v_switch_zone_id: str = None,
        vpd_subnets: List[str] = None,
    ):
        self.cluster_id = cluster_id
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.ip_allocation_policy = ip_allocation_policy
        self.node_groups = node_groups
        self.v_switch_zone_id = v_switch_zone_id
        self.vpd_subnets = vpd_subnets

    def validate(self):
        if self.ip_allocation_policy:
            for k in self.ip_allocation_policy:
                if k:
                    k.validate()
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        result['IpAllocationPolicy'] = []
        if self.ip_allocation_policy is not None:
            for k in self.ip_allocation_policy:
                result['IpAllocationPolicy'].append(k.to_map() if k else None)
        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
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
            for k in m.get('IpAllocationPolicy'):
                temp_model = ExtendClusterRequestIpAllocationPolicy()
                self.ip_allocation_policy.append(temp_model.from_map(k))
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = ExtendClusterRequestNodeGroups()
                self.node_groups.append(temp_model.from_map(k))
        if m.get('VSwitchZoneId') is not None:
            self.v_switch_zone_id = m.get('VSwitchZoneId')
        if m.get('VpdSubnets') is not None:
            self.vpd_subnets = m.get('VpdSubnets')
        return self


class ExtendClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        ip_allocation_policy_shrink: str = None,
        node_groups_shrink: str = None,
        v_switch_zone_id: str = None,
        vpd_subnets_shrink: str = None,
    ):
        self.cluster_id = cluster_id
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.ip_allocation_policy_shrink = ip_allocation_policy_shrink
        self.node_groups_shrink = node_groups_shrink
        self.v_switch_zone_id = v_switch_zone_id
        self.vpd_subnets_shrink = vpd_subnets_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.ip_allocation_policy_shrink is not None:
            result['IpAllocationPolicy'] = self.ip_allocation_policy_shrink
        if self.node_groups_shrink is not None:
            result['NodeGroups'] = self.node_groups_shrink
        if self.v_switch_zone_id is not None:
            result['VSwitchZoneId'] = self.v_switch_zone_id
        if self.vpd_subnets_shrink is not None:
            result['VpdSubnets'] = self.vpd_subnets_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('IpAllocationPolicy') is not None:
            self.ip_allocation_policy_shrink = m.get('IpAllocationPolicy')
        if m.get('NodeGroups') is not None:
            self.node_groups_shrink = m.get('NodeGroups')
        if m.get('VSwitchZoneId') is not None:
            self.v_switch_zone_id = m.get('VSwitchZoneId')
        if m.get('VpdSubnets') is not None:
            self.vpd_subnets_shrink = m.get('VpdSubnets')
        return self


class ExtendClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ExtendClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExtendClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExtendClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.max_results = max_results
        self.next_token = next_token
        self.node_group_id = node_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        return self


class ListClusterNodesResponseBodyNodesNetworks(TeaModel):
    def __init__(
        self,
        bond_name: str = None,
        ip: str = None,
        subnet_id: str = None,
        vpd_id: str = None,
    ):
        self.bond_name = bond_name
        self.ip = ip
        self.subnet_id = subnet_id
        self.vpd_id = vpd_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListClusterNodesResponseBodyNodes(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expired_time: str = None,
        hostname: str = None,
        hpn_zone: str = None,
        image_id: str = None,
        machine_type: str = None,
        networks: List[ListClusterNodesResponseBodyNodesNetworks] = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_id: str = None,
        operating_state: str = None,
        sn: str = None,
        zone_id: str = None,
    ):
        self.create_time = create_time
        self.expired_time = expired_time
        self.hostname = hostname
        self.hpn_zone = hpn_zone
        self.image_id = image_id
        self.machine_type = machine_type
        self.networks = networks
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        self.node_id = node_id
        self.operating_state = operating_state
        self.sn = sn
        self.zone_id = zone_id

    def validate(self):
        if self.networks:
            for k in self.networks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        result['Networks'] = []
        if self.networks is not None:
            for k in self.networks:
                result['Networks'].append(k.to_map() if k else None)
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        self.networks = []
        if m.get('Networks') is not None:
            for k in m.get('Networks'):
                temp_model = ListClusterNodesResponseBodyNodesNetworks()
                self.networks.append(temp_model.from_map(k))
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListClusterNodesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        nodes: List[ListClusterNodesResponseBodyNodes] = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.nodes = nodes
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClusterNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClusterNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        components: Any = None,
        create_time: str = None,
        hpn_zone: str = None,
        node_count: int = None,
        node_group_count: int = None,
        operating_state: str = None,
        resource_group_id: str = None,
        task_id: str = None,
        update_time: str = None,
        vpc_id: str = None,
    ):
        self.cluster_description = cluster_description
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type
        self.components = components
        self.create_time = create_time
        self.hpn_zone = hpn_zone
        self.node_count = node_count
        self.node_group_count = node_group_count
        self.operating_state = operating_state
        self.resource_group_id = resource_group_id
        self.task_id = task_id
        self.update_time = update_time
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_description is not None:
            result['ClusterDescription'] = self.cluster_description
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.components is not None:
            result['Components'] = self.components
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.node_group_count is not None:
            result['NodeGroupCount'] = self.node_group_count
        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterDescription') is not None:
            self.cluster_description = m.get('ClusterDescription')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('Components') is not None:
            self.components = m.get('Components')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('NodeGroupCount') is not None:
            self.node_group_count = m.get('NodeGroupCount')
        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[ListClustersResponseBodyClusters] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.clusters = clusters
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['Clusters'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('Clusters') is not None:
            for k in m.get('Clusters'):
                temp_model = ListClustersResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClustersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFreeNodesRequest(TeaModel):
    def __init__(
        self,
        hpn_zone: str = None,
        machine_type: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        self.hpn_zone = hpn_zone
        self.machine_type = machine_type
        self.max_results = max_results
        self.next_token = next_token
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListFreeNodesResponseBodyNodes(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        expired_time: str = None,
        hpn_zone: str = None,
        machine_type: str = None,
        node_id: str = None,
        resource_group_id: str = None,
        sn: str = None,
        zone_id: str = None,
    ):
        self.create_time = create_time
        self.expired_time = expired_time
        self.hpn_zone = hpn_zone
        self.machine_type = machine_type
        self.node_id = node_id
        self.resource_group_id = resource_group_id
        self.sn = sn
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sn is not None:
            result['Sn'] = self.sn
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListFreeNodesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        nodes: List[ListFreeNodesResponseBodyNodes] = None,
        request_id: str = None,
    ):
        self.next_token = next_token
        self.nodes = nodes
        self.request_id = request_id

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ListFreeNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFreeNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFreeNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFreeNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        nodes: List[str] = None,
    ):
        self.cluster_id = cluster_id
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        return self


class RebootNodesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        nodes_shrink: str = None,
    ):
        self.cluster_id = cluster_id
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.nodes_shrink = nodes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')
        return self


class RebootNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RebootNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RebootNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RebootNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReimageNodesRequestNodes(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        image_id: str = None,
        login_password: str = None,
        node_id: str = None,
    ):
        self.hostname = hostname
        self.image_id = image_id
        self.login_password = login_password
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['Hostname'] = self.hostname
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ReimageNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        nodes: List[ReimageNodesRequestNodes] = None,
        user_data: str = None,
    ):
        self.cluster_id = cluster_id
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.nodes = nodes
        self.user_data = user_data

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ReimageNodesRequestNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class ReimageNodesShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        nodes_shrink: str = None,
        user_data: str = None,
    ):
        self.cluster_id = cluster_id
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.nodes_shrink = nodes_shrink
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class ReimageNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ReimageNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReimageNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ReimageNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCommandRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        command_content: str = None,
        content_encoding: str = None,
        description: str = None,
        enable_parameter: bool = None,
        frequency: str = None,
        name: str = None,
        node_id_list: List[str] = None,
        parameters: Dict[str, Any] = None,
        repeat_mode: str = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        self.client_token = client_token
        self.command_content = command_content
        self.content_encoding = content_encoding
        self.description = description
        self.enable_parameter = enable_parameter
        self.frequency = frequency
        self.name = name
        self.node_id_list = node_id_list
        self.parameters = parameters
        self.repeat_mode = repeat_mode
        self.timeout = timeout
        self.username = username
        self.working_dir = working_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.username is not None:
            result['Username'] = self.username
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class RunCommandShrinkRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        command_content: str = None,
        content_encoding: str = None,
        description: str = None,
        enable_parameter: bool = None,
        frequency: str = None,
        name: str = None,
        node_id_list_shrink: str = None,
        parameters_shrink: str = None,
        repeat_mode: str = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        self.client_token = client_token
        self.command_content = command_content
        self.content_encoding = content_encoding
        self.description = description
        self.enable_parameter = enable_parameter
        self.frequency = frequency
        self.name = name
        self.node_id_list_shrink = node_id_list_shrink
        self.parameters_shrink = parameters_shrink
        self.repeat_mode = repeat_mode
        self.timeout = timeout
        self.username = username
        self.working_dir = working_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.command_content is not None:
            result['CommandContent'] = self.command_content
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id_list_shrink is not None:
            result['NodeIdList'] = self.node_id_list_shrink
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.username is not None:
            result['Username'] = self.username
        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('CommandContent') is not None:
            self.command_content = m.get('CommandContent')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeIdList') is not None:
            self.node_id_list_shrink = m.get('NodeIdList')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')
        return self


class RunCommandResponseBody(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
    ):
        self.invoke_id = invoke_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCommandResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendFileRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        file_group: str = None,
        file_mode: str = None,
        file_owner: str = None,
        name: str = None,
        node_id_list: List[str] = None,
        overwrite: bool = None,
        target_dir: str = None,
        timeout: int = None,
    ):
        self.content = content
        self.content_type = content_type
        self.description = description
        self.file_group = file_group
        self.file_mode = file_mode
        self.file_owner = file_owner
        self.name = name
        self.node_id_list = node_id_list
        self.overwrite = overwrite
        self.target_dir = target_dir
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.description is not None:
            result['Description'] = self.description
        if self.file_group is not None:
            result['FileGroup'] = self.file_group
        if self.file_mode is not None:
            result['FileMode'] = self.file_mode
        if self.file_owner is not None:
            result['FileOwner'] = self.file_owner
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileGroup') is not None:
            self.file_group = m.get('FileGroup')
        if m.get('FileMode') is not None:
            self.file_mode = m.get('FileMode')
        if m.get('FileOwner') is not None:
            self.file_owner = m.get('FileOwner')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class SendFileShrinkRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_type: str = None,
        description: str = None,
        file_group: str = None,
        file_mode: str = None,
        file_owner: str = None,
        name: str = None,
        node_id_list_shrink: str = None,
        overwrite: bool = None,
        target_dir: str = None,
        timeout: int = None,
    ):
        self.content = content
        self.content_type = content_type
        self.description = description
        self.file_group = file_group
        self.file_mode = file_mode
        self.file_owner = file_owner
        self.name = name
        self.node_id_list_shrink = node_id_list_shrink
        self.overwrite = overwrite
        self.target_dir = target_dir
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.description is not None:
            result['Description'] = self.description
        if self.file_group is not None:
            result['FileGroup'] = self.file_group
        if self.file_mode is not None:
            result['FileMode'] = self.file_mode
        if self.file_owner is not None:
            result['FileOwner'] = self.file_owner
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id_list_shrink is not None:
            result['NodeIdList'] = self.node_id_list_shrink
        if self.overwrite is not None:
            result['Overwrite'] = self.overwrite
        if self.target_dir is not None:
            result['TargetDir'] = self.target_dir
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FileGroup') is not None:
            self.file_group = m.get('FileGroup')
        if m.get('FileMode') is not None:
            self.file_mode = m.get('FileMode')
        if m.get('FileOwner') is not None:
            self.file_owner = m.get('FileOwner')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeIdList') is not None:
            self.node_id_list_shrink = m.get('NodeIdList')
        if m.get('Overwrite') is not None:
            self.overwrite = m.get('Overwrite')
        if m.get('TargetDir') is not None:
            self.target_dir = m.get('TargetDir')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class SendFileResponseBody(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        request_id: str = None,
    ):
        self.invoke_id = invoke_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SendFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendFileResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SendFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ShrinkClusterRequestNodeGroupsNodes(TeaModel):
    def __init__(
        self,
        node_id: str = None,
    ):
        self.node_id = node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class ShrinkClusterRequestNodeGroups(TeaModel):
    def __init__(
        self,
        node_group_id: str = None,
        nodes: List[ShrinkClusterRequestNodeGroupsNodes] = None,
    ):
        self.node_group_id = node_group_id
        self.nodes = nodes

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ShrinkClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k))
        return self


class ShrinkClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        node_groups: List[ShrinkClusterRequestNodeGroups] = None,
    ):
        self.cluster_id = cluster_id
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.node_groups = node_groups

    def validate(self):
        if self.node_groups:
            for k in self.node_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        result['NodeGroups'] = []
        if self.node_groups is not None:
            for k in self.node_groups:
                result['NodeGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        self.node_groups = []
        if m.get('NodeGroups') is not None:
            for k in m.get('NodeGroups'):
                temp_model = ShrinkClusterRequestNodeGroups()
                self.node_groups.append(temp_model.from_map(k))
        return self


class ShrinkClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        node_groups_shrink: str = None,
    ):
        self.cluster_id = cluster_id
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        self.node_groups_shrink = node_groups_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.node_groups_shrink is not None:
            result['NodeGroups'] = self.node_groups_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('NodeGroups') is not None:
            self.node_groups_shrink = m.get('NodeGroups')
        return self


class ShrinkClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ShrinkClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ShrinkClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ShrinkClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopInvocationRequest(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        node_id_list: List[str] = None,
    ):
        self.invoke_id = invoke_id
        self.node_id_list = node_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')
        return self


class StopInvocationShrinkRequest(TeaModel):
    def __init__(
        self,
        invoke_id: str = None,
        node_id_list_shrink: str = None,
    ):
        self.invoke_id = invoke_id
        self.node_id_list_shrink = node_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invoke_id is not None:
            result['InvokeId'] = self.invoke_id
        if self.node_id_list_shrink is not None:
            result['NodeIdList'] = self.node_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvokeId') is not None:
            self.invoke_id = m.get('InvokeId')
        if m.get('NodeIdList') is not None:
            self.node_id_list_shrink = m.get('NodeIdList')
        return self


class StopInvocationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopInvocationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopInvocationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StopInvocationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


