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
        # Node ID
        self.node_id = node_id
        # Operation Type
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
        # Error Message
        self.error_message = error_message
        # Request ID
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
        resource_type: str = None,
    ):
        # System-defined parameter. Value: **ChangeResourceGroup**.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # $.parameters[1].schema.example
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # Resource Group Change
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # $.parameters[3].schema.enumValueTitles
        self.resource_type = resource_type

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
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
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


class CloseSessionRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
        session_token: str = None,
    ):
        # Session ID
        self.session_id = session_id
        # Session token
        self.session_token = session_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_token is not None:
            result['SessionToken'] = self.session_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionToken') is not None:
            self.session_token = m.get('SessionToken')
        return self


class CloseSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        session_id: str = None,
        state: str = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Session ID.
        self.session_id = session_id
        # ClosingActive
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class CloseSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseSessionResponseBody = None,
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
            temp_model = CloseSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterRequestComponentsComponentConfig(TeaModel):
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
        # Component configuration
        self.component_config = component_config
        # Component type
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
        # Bond name
        self.name = name
        # IP source cluster subnet
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
        # Default bond cluster subnet
        self.bond_default_subnet = bond_default_subnet
        # Bond information
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
        # Bond name
        self.name = name
        # IP source cluster subnet
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
        # Bond information
        self.bonds = bonds
        # Machine type
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
        # Bond name
        self.name = name
        # IP source cluster subnet
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
        # Bond information
        self.bonds = bonds
        # Node ID
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
        # Subnet CIDR
        self.subnet_cidr = subnet_cidr
        # Subnet type
        self.subnet_type = subnet_type
        # Zone ID
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
        # Cloud Enterprise Network ID
        self.cen_id = cen_id
        # Cloud link CIDR
        self.cloud_link_cidr = cloud_link_cidr
        # Cloud link ID
        self.cloud_link_id = cloud_link_id
        # VPC
        self.monitor_vpc_id = monitor_vpc_id
        # VPC switch
        self.monitor_vswitch_id = monitor_vswitch_id
        # Cluster Network Segment
        self.vpd_cidr = vpd_cidr
        # Cluster subnets
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
        # VPC ID
        self.vpd_id = vpd_id
        # List of cluster subnet IDs
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
        tail_ip_version: str = None,
        v_switch_id: str = None,
        v_switch_zone_id: str = None,
        vpc_id: str = None,
        vpd_info: CreateClusterRequestNetworksVpdInfo = None,
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
            for k in m.get('IpAllocationPolicy'):
                temp_model = CreateClusterRequestNetworksIpAllocationPolicy()
                self.ip_allocation_policy.append(temp_model.from_map(k))
        if m.get('NewVpdInfo') is not None:
            temp_model = CreateClusterRequestNetworksNewVpdInfo()
            self.new_vpd_info = temp_model.from_map(m['NewVpdInfo'])
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
        # Hostname
        self.hostname = hostname
        # Login password
        self.login_password = login_password
        # Node ID
        self.node_id = node_id
        # Virtual switch ID
        self.v_switch_id = v_switch_id
        # VPC ID
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
        # System image ID
        self.image_id = image_id
        # Machine type
        self.machine_type = machine_type
        # Node group description
        self.node_group_description = node_group_description
        # Node group name
        self.node_group_name = node_group_name
        # Node list
        self.nodes = nodes
        # Instance custom data. It needs to be Base64 encoded, and the original data should not exceed 16 KB.
        self.user_data = user_data
        # Zone ID
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
        # Key
        self.key = key
        # Value
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
        open_eni_jumbo_frame: bool = None,
        resource_group_id: str = None,
        tag: List[CreateClusterRequestTag] = None,
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
        # Whether to allow skipping failed nodes, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # Network information
        self.networks = networks
        # Node VSwitches
        self.nimiz_vswitches = nimiz_vswitches
        # Node group list
        self.node_groups = node_groups
        # Open Eni Jumbo Frame
        self.open_eni_jumbo_frame = open_eni_jumbo_frame
        # Resource group ID
        self.resource_group_id = resource_group_id
        # Resource tags
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
        if self.open_eni_jumbo_frame is not None:
            result['OpenEniJumboFrame'] = self.open_eni_jumbo_frame
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
        if m.get('OpenEniJumboFrame') is not None:
            self.open_eni_jumbo_frame = m.get('OpenEniJumboFrame')
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
        # Key
        self.key = key
        # Value
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
        open_eni_jumbo_frame: bool = None,
        resource_group_id: str = None,
        tag: List[CreateClusterShrinkRequestTag] = None,
    ):
        # Cluster description
        self.cluster_description = cluster_description
        # Cluster name
        self.cluster_name = cluster_name
        # Cluster type
        self.cluster_type = cluster_type
        # Components (software instances)
        self.components_shrink = components_shrink
        # Cluster number
        self.hpn_zone = hpn_zone
        # Whether to allow skipping failed nodes, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # Network information
        self.networks_shrink = networks_shrink
        # Node VSwitches
        self.nimiz_vswitches_shrink = nimiz_vswitches_shrink
        # Node group list
        self.node_groups_shrink = node_groups_shrink
        # Open Eni Jumbo Frame
        self.open_eni_jumbo_frame = open_eni_jumbo_frame
        # Resource group ID
        self.resource_group_id = resource_group_id
        # Resource tags
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
        if self.open_eni_jumbo_frame is not None:
            result['OpenEniJumboFrame'] = self.open_eni_jumbo_frame
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
        if m.get('OpenEniJumboFrame') is not None:
            self.open_eni_jumbo_frame = m.get('OpenEniJumboFrame')
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
        # Cluster ID
        self.cluster_id = cluster_id
        # Request ID
        self.request_id = request_id
        # Task Id
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


class CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogsLogs(TeaModel):
    def __init__(
        self,
        datetime: str = None,
        log_content: str = None,
    ):
        # Sent date, in the format yyyymmdd.
        self.datetime = datetime
        # Log content
        self.log_content = log_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.datetime is not None:
            result['Datetime'] = self.datetime
        if self.log_content is not None:
            result['LogContent'] = self.log_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Datetime') is not None:
            self.datetime = m.get('Datetime')
        if m.get('LogContent') is not None:
            self.log_content = m.get('LogContent')
        return self


class CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogs(TeaModel):
    def __init__(
        self,
        ai_instance: str = None,
        logs: List[CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogsLogs] = None,
        node_id: str = None,
    ):
        # Instance ID
        self.ai_instance = ai_instance
        # Log object
        self.logs = logs
        # Node ID
        self.node_id = node_id

    def validate(self):
        if self.logs:
            for k in self.logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_instance is not None:
            result['AiInstance'] = self.ai_instance
        result['Logs'] = []
        if self.logs is not None:
            for k in self.logs:
                result['Logs'].append(k.to_map() if k else None)
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiInstance') is not None:
            self.ai_instance = m.get('AiInstance')
        self.logs = []
        if m.get('Logs') is not None:
            for k in m.get('Logs'):
                temp_model = CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogsLogs()
                self.logs.append(temp_model.from_map(k))
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        return self


class CreateDiagnosticTaskRequestAiJobLogInfo(TeaModel):
    def __init__(
        self,
        ai_job_logs: List[CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogs] = None,
        end_time: str = None,
        start_time: str = None,
    ):
        # Task logs
        self.ai_job_logs = ai_job_logs
        # End time. In timestamp format, unit: seconds.
        # > Must be on the hour or half-hour mark.
        self.end_time = end_time
        # Start time. In timestamp format, unit: seconds.
        # > Must be on the hour or half-hour mark.
        self.start_time = start_time

    def validate(self):
        if self.ai_job_logs:
            for k in self.ai_job_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AiJobLogs'] = []
        if self.ai_job_logs is not None:
            for k in self.ai_job_logs:
                result['AiJobLogs'].append(k.to_map() if k else None)
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ai_job_logs = []
        if m.get('AiJobLogs') is not None:
            for k in m.get('AiJobLogs'):
                temp_model = CreateDiagnosticTaskRequestAiJobLogInfoAiJobLogs()
                self.ai_job_logs.append(temp_model.from_map(k))
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateDiagnosticTaskRequest(TeaModel):
    def __init__(
        self,
        ai_job_log_info: CreateDiagnosticTaskRequestAiJobLogInfo = None,
        cluster_id: str = None,
        diagnostic_type: str = None,
        node_ids: List[str] = None,
    ):
        # Log information
        self.ai_job_log_info = ai_job_log_info
        # Cluster ID
        self.cluster_id = cluster_id
        # Diagnostic type.
        self.diagnostic_type = diagnostic_type
        # List of node IDs
        self.node_ids = node_ids

    def validate(self):
        if self.ai_job_log_info:
            self.ai_job_log_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_job_log_info is not None:
            result['AiJobLogInfo'] = self.ai_job_log_info.to_map()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.diagnostic_type is not None:
            result['DiagnosticType'] = self.diagnostic_type
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiJobLogInfo') is not None:
            temp_model = CreateDiagnosticTaskRequestAiJobLogInfo()
            self.ai_job_log_info = temp_model.from_map(m['AiJobLogInfo'])
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DiagnosticType') is not None:
            self.diagnostic_type = m.get('DiagnosticType')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        return self


class CreateDiagnosticTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        ai_job_log_info_shrink: str = None,
        cluster_id: str = None,
        diagnostic_type: str = None,
        node_ids_shrink: str = None,
    ):
        # Log information
        self.ai_job_log_info_shrink = ai_job_log_info_shrink
        # Cluster ID
        self.cluster_id = cluster_id
        # Diagnostic type.
        self.diagnostic_type = diagnostic_type
        # List of node IDs
        self.node_ids_shrink = node_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ai_job_log_info_shrink is not None:
            result['AiJobLogInfo'] = self.ai_job_log_info_shrink
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.diagnostic_type is not None:
            result['DiagnosticType'] = self.diagnostic_type
        if self.node_ids_shrink is not None:
            result['NodeIds'] = self.node_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AiJobLogInfo') is not None:
            self.ai_job_log_info_shrink = m.get('AiJobLogInfo')
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('DiagnosticType') is not None:
            self.diagnostic_type = m.get('DiagnosticType')
        if m.get('NodeIds') is not None:
            self.node_ids_shrink = m.get('NodeIds')
        return self


class CreateDiagnosticTaskResponseBody(TeaModel):
    def __init__(
        self,
        diagnostic_id: str = None,
        request_id: str = None,
    ):
        # Diagnosis ID
        self.diagnostic_id = diagnostic_id
        # Request ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnostic_id is not None:
            result['DiagnosticId'] = self.diagnostic_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosticId') is not None:
            self.diagnostic_id = m.get('DiagnosticId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDiagnosticTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDiagnosticTaskResponseBody = None,
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
            temp_model = CreateDiagnosticTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNetTestTaskRequestCommTestHosts(TeaModel):
    def __init__(
        self,
        ip: str = None,
        node_id: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # IP address.
        self.ip = ip
        # Node ID.
        self.node_id = node_id
        # Resource ID
        self.resource_id = resource_id
        # Service name.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class CreateNetTestTaskRequestCommTest(TeaModel):
    def __init__(
        self,
        gpunum: int = None,
        hosts: List[CreateNetTestTaskRequestCommTestHosts] = None,
        model: str = None,
        type: str = None,
    ):
        # Number of GPUs
        self.gpunum = gpunum
        # Resource ID
        self.hosts = hosts
        # Communication library model
        self.model = model
        # Communication library test category: ACCL or NCCL
        self.type = type

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpunum is not None:
            result['GPUNum'] = self.gpunum
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.model is not None:
            result['Model'] = self.model
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GPUNum') is not None:
            self.gpunum = m.get('GPUNum')
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = CreateNetTestTaskRequestCommTestHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateNetTestTaskRequestDelayTestHosts(TeaModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        node_id: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network interface bond port
        self.bond = bond
        # Node IP
        self.ip = ip
        # Node ID.
        self.node_id = node_id
        # Resource ID
        self.resource_id = resource_id
        # Service name.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond is not None:
            result['Bond'] = self.bond
        if self.ip is not None:
            result['IP'] = self.ip
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class CreateNetTestTaskRequestDelayTest(TeaModel):
    def __init__(
        self,
        hosts: List[CreateNetTestTaskRequestDelayTestHosts] = None,
    ):
        # 输入测试节点的hosts
        self.hosts = hosts

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = CreateNetTestTaskRequestDelayTestHosts()
                self.hosts.append(temp_model.from_map(k))
        return self


class CreateNetTestTaskRequestTrafficTestClients(TeaModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        node_id: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network card bond interface
        self.bond = bond
        # Node IP
        self.ip = ip
        # Node ID
        self.node_id = node_id
        # Resource ID
        self.resource_id = resource_id
        # Service name.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond is not None:
            result['Bond'] = self.bond
        if self.ip is not None:
            result['IP'] = self.ip
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class CreateNetTestTaskRequestTrafficTestServers(TeaModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        node_id: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network card bond interface
        self.bond = bond
        # Node IP
        self.ip = ip
        # Node ID
        self.node_id = node_id
        # Resource ID
        self.resource_id = resource_id
        # Service name.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond is not None:
            result['Bond'] = self.bond
        if self.ip is not None:
            result['IP'] = self.ip
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class CreateNetTestTaskRequestTrafficTest(TeaModel):
    def __init__(
        self,
        clients: List[CreateNetTestTaskRequestTrafficTestClients] = None,
        duration: int = None,
        gdr: bool = None,
        protocol: str = None,
        qp: int = None,
        servers: List[CreateNetTestTaskRequestTrafficTestServers] = None,
        traffic_model: str = None,
    ):
        # Resource ID.
        self.clients = clients
        # The duration of the workflow task in seconds.
        self.duration = duration
        # Enter True/False when the protocol is RDMA, 
        # this field is empty when the protocol is TCP.
        self.gdr = gdr
        # Network protocol, either RDMA or TCP.
        self.protocol = protocol
        # Enter the number of concurrent connections when the protocol is TCP, or enter the configured QP value when the protocol is RDMA.
        self.qp = qp
        # Service list
        self.servers = servers
        # Traffic model, either MTON or Fullmesh.
        self.traffic_model = traffic_model

    def validate(self):
        if self.clients:
            for k in self.clients:
                if k:
                    k.validate()
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clients'] = []
        if self.clients is not None:
            for k in self.clients:
                result['Clients'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.gdr is not None:
            result['GDR'] = self.gdr
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.qp is not None:
            result['QP'] = self.qp
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        if self.traffic_model is not None:
            result['TrafficModel'] = self.traffic_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clients = []
        if m.get('Clients') is not None:
            for k in m.get('Clients'):
                temp_model = CreateNetTestTaskRequestTrafficTestClients()
                self.clients.append(temp_model.from_map(k))
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('GDR') is not None:
            self.gdr = m.get('GDR')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('QP') is not None:
            self.qp = m.get('QP')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = CreateNetTestTaskRequestTrafficTestServers()
                self.servers.append(temp_model.from_map(k))
        if m.get('TrafficModel') is not None:
            self.traffic_model = m.get('TrafficModel')
        return self


class CreateNetTestTaskRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        comm_test: CreateNetTestTaskRequestCommTest = None,
        delay_test: CreateNetTestTaskRequestDelayTest = None,
        net_test_type: str = None,
        network_mode: str = None,
        port: str = None,
        traffic_test: CreateNetTestTaskRequestTrafficTest = None,
    ):
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster name
        self.cluster_name = cluster_name
        # Required when the test type is communication library testing
        self.comm_test = comm_test
        # Fill in this field when the network test type is delay testing.
        self.delay_test = delay_test
        # Network test type.
        # For example: DelayTest for latency testing, TrafficTest for traffic testing, CommTest for communication library testing.
        self.net_test_type = net_test_type
        # Network mode
        self.network_mode = network_mode
        # Test port number.
        self.port = port
        # This field is empty if the TrafficModel is Fullmesh.
        self.traffic_test = traffic_test

    def validate(self):
        if self.comm_test:
            self.comm_test.validate()
        if self.delay_test:
            self.delay_test.validate()
        if self.traffic_test:
            self.traffic_test.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.comm_test is not None:
            result['CommTest'] = self.comm_test.to_map()
        if self.delay_test is not None:
            result['DelayTest'] = self.delay_test.to_map()
        if self.net_test_type is not None:
            result['NetTestType'] = self.net_test_type
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.port is not None:
            result['Port'] = self.port
        if self.traffic_test is not None:
            result['TrafficTest'] = self.traffic_test.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CommTest') is not None:
            temp_model = CreateNetTestTaskRequestCommTest()
            self.comm_test = temp_model.from_map(m['CommTest'])
        if m.get('DelayTest') is not None:
            temp_model = CreateNetTestTaskRequestDelayTest()
            self.delay_test = temp_model.from_map(m['DelayTest'])
        if m.get('NetTestType') is not None:
            self.net_test_type = m.get('NetTestType')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('TrafficTest') is not None:
            temp_model = CreateNetTestTaskRequestTrafficTest()
            self.traffic_test = temp_model.from_map(m['TrafficTest'])
        return self


class CreateNetTestTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        comm_test_shrink: str = None,
        delay_test_shrink: str = None,
        net_test_type: str = None,
        network_mode: str = None,
        port: str = None,
        traffic_test_shrink: str = None,
    ):
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster name
        self.cluster_name = cluster_name
        # Required when the test type is communication library testing
        self.comm_test_shrink = comm_test_shrink
        # Fill in this field when the network test type is delay testing.
        self.delay_test_shrink = delay_test_shrink
        # Network test type.
        # For example: DelayTest for latency testing, TrafficTest for traffic testing, CommTest for communication library testing.
        self.net_test_type = net_test_type
        # Network mode
        self.network_mode = network_mode
        # Test port number.
        self.port = port
        # This field is empty if the TrafficModel is Fullmesh.
        self.traffic_test_shrink = traffic_test_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.comm_test_shrink is not None:
            result['CommTest'] = self.comm_test_shrink
        if self.delay_test_shrink is not None:
            result['DelayTest'] = self.delay_test_shrink
        if self.net_test_type is not None:
            result['NetTestType'] = self.net_test_type
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.port is not None:
            result['Port'] = self.port
        if self.traffic_test_shrink is not None:
            result['TrafficTest'] = self.traffic_test_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CommTest') is not None:
            self.comm_test_shrink = m.get('CommTest')
        if m.get('DelayTest') is not None:
            self.delay_test_shrink = m.get('DelayTest')
        if m.get('NetTestType') is not None:
            self.net_test_type = m.get('NetTestType')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('TrafficTest') is not None:
            self.traffic_test_shrink = m.get('TrafficTest')
        return self


class CreateNetTestTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        test_id: str = None,
    ):
        # ID of the request
        self.request_id = request_id
        # 启动测试任务ID，网络测试任务的唯一标志。
        self.test_id = test_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.test_id is not None:
            result['TestId'] = self.test_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')
        return self


class CreateNetTestTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNetTestTaskResponseBody = None,
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
            temp_model = CreateNetTestTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNodeGroupRequestNodeGroup(TeaModel):
    def __init__(
        self,
        az: str = None,
        image_id: str = None,
        machine_type: str = None,
        node_group_description: str = None,
        node_group_name: str = None,
        user_data: str = None,
    ):
        # This parameter is required.
        self.az = az
        # This parameter is required.
        self.image_id = image_id
        # This parameter is required.
        self.machine_type = machine_type
        self.node_group_description = node_group_description
        # This parameter is required.
        self.node_group_name = node_group_name
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az is not None:
            result['Az'] = self.az
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.node_group_description is not None:
            result['NodeGroupDescription'] = self.node_group_description
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Az') is not None:
            self.az = m.get('Az')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('NodeGroupDescription') is not None:
            self.node_group_description = m.get('NodeGroupDescription')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class CreateNodeGroupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_group: CreateNodeGroupRequestNodeGroup = None,
        node_unit: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.node_group = node_group
        self.node_unit = node_unit

    def validate(self):
        if self.node_group:
            self.node_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node_group is not None:
            result['NodeGroup'] = self.node_group.to_map()
        if self.node_unit is not None:
            result['NodeUnit'] = self.node_unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeGroup') is not None:
            temp_model = CreateNodeGroupRequestNodeGroup()
            self.node_group = temp_model.from_map(m['NodeGroup'])
        if m.get('NodeUnit') is not None:
            self.node_unit = m.get('NodeUnit')
        return self


class CreateNodeGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_group_shrink: str = None,
        node_unit_shrink: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.node_group_shrink = node_group_shrink
        self.node_unit_shrink = node_unit_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.node_group_shrink is not None:
            result['NodeGroup'] = self.node_group_shrink
        if self.node_unit_shrink is not None:
            result['NodeUnit'] = self.node_unit_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeGroup') is not None:
            self.node_group_shrink = m.get('NodeGroup')
        if m.get('NodeUnit') is not None:
            self.node_unit_shrink = m.get('NodeUnit')
        return self


class CreateNodeGroupResponseBody(TeaModel):
    def __init__(
        self,
        node_group_id: str = None,
        node_group_name: str = None,
        request_id: str = None,
    ):
        self.node_group_id = node_group_id
        self.node_group_name = node_group_name
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.node_group_name is not None:
            result['NodeGroupName'] = self.node_group_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('NodeGroupName') is not None:
            self.node_group_name = m.get('NodeGroupName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNodeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNodeGroupResponseBody = None,
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
            temp_model = CreateNodeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSessionRequest(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        session_type: str = None,
        start_time: str = None,
    ):
        # Instance ID.
        self.node_id = node_id
        # Session type corresponding to the session package.
        self.session_type = session_type
        # Initiation time, 13-digit timestamp.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.session_type is not None:
            result['SessionType'] = self.session_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class CreateSessionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        server_sn: str = None,
        session_id: str = None,
        session_token: str = None,
        wss_endpoint: str = None,
    ):
        # ID of the request
        self.request_id = request_id
        # 节点  ID。
        self.server_sn = server_sn
        # Session ID.
        self.session_id = session_id
        # Session token.
        self.session_token = session_token
        # WebSocket address
        self.wss_endpoint = wss_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.server_sn is not None:
            result['ServerSn'] = self.server_sn
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.session_token is not None:
            result['SessionToken'] = self.session_token
        if self.wss_endpoint is not None:
            result['WssEndpoint'] = self.wss_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServerSn') is not None:
            self.server_sn = m.get('ServerSn')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('SessionToken') is not None:
            self.session_token = m.get('SessionToken')
        if m.get('WssEndpoint') is not None:
            self.wss_endpoint = m.get('WssEndpoint')
        return self


class CreateSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSessionResponseBody = None,
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
            temp_model = CreateSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # Cluster ID
        # 
        # This parameter is required.
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
        # Request Id
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


class DeleteNodeGroupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_group_id: str = None,
    ):
        self.cluster_id = cluster_id
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
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        return self


class DeleteNodeGroupResponseBody(TeaModel):
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


class DeleteNodeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteNodeGroupResponseBody = None,
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
            temp_model = DeleteNodeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # Cluster ID.
        # 
        # This parameter is required.
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
        # Component ID
        self.component_id = component_id
        # Component Type
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
        # VPC Segment ID
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
        computing_ip_version: str = None,
        create_time: str = None,
        hpn_zone: str = None,
        networks: List[DescribeClusterResponseBodyNetworks] = None,
        node_count: int = None,
        node_group_count: int = None,
        open_eni_jumbo_frame: str = None,
        operating_state: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        task_id: str = None,
        update_time: str = None,
        vpc_id: str = None,
    ):
        # Cluster Description
        self.cluster_description = cluster_description
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster Name
        self.cluster_name = cluster_name
        # Cluster Type
        self.cluster_type = cluster_type
        # Component Information
        self.components = components
        # Type of IP in the compute network
        self.computing_ip_version = computing_ip_version
        # Creation Time
        self.create_time = create_time
        # Cluster Number
        self.hpn_zone = hpn_zone
        # Network Information
        self.networks = networks
        # Number of Nodes
        self.node_count = node_count
        # Number of Node Groups
        self.node_group_count = node_group_count
        # Open Eni Jumbo Frame
        self.open_eni_jumbo_frame = open_eni_jumbo_frame
        # Cluster State
        self.operating_state = operating_state
        # Request ID.
        self.request_id = request_id
        # Resource Group ID
        self.resource_group_id = resource_group_id
        # Task ID
        self.task_id = task_id
        # Update Time
        self.update_time = update_time
        # VPC ID
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
        if self.computing_ip_version is not None:
            result['ComputingIpVersion'] = self.computing_ip_version
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
        if self.open_eni_jumbo_frame is not None:
            result['OpenEniJumboFrame'] = self.open_eni_jumbo_frame
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
        if m.get('ComputingIpVersion') is not None:
            self.computing_ip_version = m.get('ComputingIpVersion')
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
        if m.get('OpenEniJumboFrame') is not None:
            self.open_eni_jumbo_frame = m.get('OpenEniJumboFrame')
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


class DescribeDiagnosticResultRequest(TeaModel):
    def __init__(
        self,
        diagnostic_id: str = None,
    ):
        self.diagnostic_id = diagnostic_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnostic_id is not None:
            result['DiagnosticId'] = self.diagnostic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagnosticId') is not None:
            self.diagnostic_id = m.get('DiagnosticId')
        return self


class DescribeDiagnosticResultResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        created_time: str = None,
        diagnostic_id: str = None,
        diagnostic_results: List[Any] = None,
        diagnostic_state: str = None,
        diagnostic_type: str = None,
        end_time: str = None,
        node_ids: List[str] = None,
        request_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.created_time = created_time
        self.diagnostic_id = diagnostic_id
        self.diagnostic_results = diagnostic_results
        self.diagnostic_state = diagnostic_state
        self.diagnostic_type = diagnostic_type
        self.end_time = end_time
        self.node_ids = node_ids
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.diagnostic_id is not None:
            result['DiagnosticId'] = self.diagnostic_id
        if self.diagnostic_results is not None:
            result['DiagnosticResults'] = self.diagnostic_results
        if self.diagnostic_state is not None:
            result['DiagnosticState'] = self.diagnostic_state
        if self.diagnostic_type is not None:
            result['DiagnosticType'] = self.diagnostic_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('DiagnosticId') is not None:
            self.diagnostic_id = m.get('DiagnosticId')
        if m.get('DiagnosticResults') is not None:
            self.diagnostic_results = m.get('DiagnosticResults')
        if m.get('DiagnosticState') is not None:
            self.diagnostic_state = m.get('DiagnosticState')
        if m.get('DiagnosticType') is not None:
            self.diagnostic_type = m.get('DiagnosticType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeDiagnosticResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeDiagnosticResultResponseBody = None,
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
            temp_model = DescribeDiagnosticResultResponseBody()
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
        # Sets the encoding method for the `CommandContent` and `Output` fields in the returned data. Possible values:
        # 
        # - PlainText: Returns the original command content and output information.
        # - Base64: Returns the Base64-encoded command content and output information.
        # 
        # Default value: Base64.
        self.content_encoding = content_encoding
        # Indicates whether to return the output information of the command execution in the result.
        # 
        # - true: Return. In this case, you must specify at least the `InvokeId` or `InstanceId` parameter.
        # - false: Do not return.
        # 
        # Default value: false.
        self.include_output = include_output
        # Command execution ID
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # Instance ID
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
        error_code: str = None,
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
        # The start time of the command execution.
        self.creation_time = creation_time
        # The length of the text that is truncated and discarded when the length of the `Output` field exceeds 24 KB.
        self.dropped = dropped
        # Reason code for file delivery failure. Possible values:
        # - Empty: File delivery is normal. 
        # - NodeNotExists: The specified instance does not exist or has been released. 
        # - NodeReleased: The instance was released during the file delivery process. 
        # - NodeNotRunning: The instance was not running when the file delivery task was created. 
        # - AccountNotExists: The specified account does not exist. 
        # - ClientNotRunning: The Cloud Assistant Agent is not running. 
        # - ClientNotResponse: The Cloud Assistant Agent is not responding. 
        # - ClientIsUpgrading: The Cloud Assistant Agent is currently upgrading. 
        # - ClientNeedUpgrade: The Cloud Assistant Agent needs to be upgraded. 
        # - DeliveryTimeout: File sending timed out. 
        # - FileCreateFail: File creation failed. 
        # - FileAlreadyExists: A file with the same name already exists at the specified path. 
        # - FileContentInvalid: The file content is invalid. - FileNameInvalid: The file name is invalid. 
        # - FilePathInvalid: The file path is invalid. 
        # - FileAuthorityInvalid: The file permissions are invalid. 
        # - UserGroupNotExists: The user group specified for file sending does not exist.
        self.error_code = error_code
        # Details of the reason for command delivery failure or execution failure, possible values: 
        # - Empty: The command executed normally. 
        # - the specified node does not exist: The specified instance does not exist or has been released. 
        # - the node was released when creating the task: The instance was released during command execution. 
        # - the node is not running when creating the task: The instance was not in a running state when the command was executed. 
        # - the command is not applicable: The command is not applicable to the specified instance. 
        # - the specified account does not exist: The specified account does not exist. 
        # - the specified directory does not exist: The specified directory does not exist. 
        # - the cron job expression is invalid: The specified execution time expression is invalid. 
        # - the aliyun service is not running on the instance: The Cloud Assistant Agent is not running. 
        # - the aliyun service in the instance does not respond: The Cloud Assistant Agent is not responding. 
        # - the aliyun service in the node is upgrading now: The Cloud Assistant Agent is currently being upgraded. 
        # - the aliyun service in the node needs upgrade: The Cloud Assistant Agent needs an upgrade. 
        # - the command delivery has timed out: Command delivery has timed out. 
        # - the command execution has timed out: Command execution has timed out. 
        # - the command execution got an exception: An exception occurred during command execution. 
        # - the command execution was interrupted: Command execution was interrupted. 
        #  - the command execution exit code is not zero: Command execution completed with a non-zero exit code. 
        # - the specified node has been released: The instance was released during file delivery.
        self.error_info = error_info
        # The exit code of the command process. Possible values:
        # - For Linux instances, it is the exit code of the Shell process. - For Windows instances, it is the exit code of the Bat or PowerShell process.
        self.exit_code = exit_code
        # Completion time.
        self.finish_time = finish_time
        # The command progress status for a single instance. Possible values:
        # -  Pending: The system is validating or sending the command.
        # -  Invalid: The specified command type or parameters are incorrect.
        # -  Aborted: Failed to send the command to the instance. The instance must be running, and the command should be sent within 1 minute.
        # -  Running: The command is running on the instance.
        # -  Success:
        #     -  For a one-time execution command: The command has completed with an exit code of 0.
        #     -  For a periodic execution command: The last run was successful with an exit code of 0, and the specified period has ended.
        # -  Failed:
        #     -  For a one-time execution command: The command has completed with a non-zero exit code.
        #     -  For a periodic execution command: The last run was successful with a non-zero exit code, and the specified period will be terminated.
        # -  Error: An exception occurred during command execution, and it cannot continue.
        # -  Timeout: The command execution timed out.
        # -  Cancelled: The command execution action has been canceled, and the command was never started.
        # -  Stopping: The task is being stopped.
        # -  Terminated: The command was terminated while running.
        # -  Scheduled:
        #     -  For a one-time execution command: Not applicable, will not appear.
        #     -  For a periodic execution command: Waiting to run.
        self.invocation_status = invocation_status
        # Node ID
        self.node_id = node_id
        # The command progress status of a single instance.
        self.node_invoke_status = node_invoke_status
        # The output information of the command.
        # 
        # - If `ContentEncoding` is set to `PlainText`, the original output information is returned.
        # - If `ContentEncoding` is set to `Base64`, the Base64-encoded output information is returned.
        self.output = output
        # The number of times the command has been executed on this instance.
        # -  If the execution mode is one-time, the value is 0 or 1.
        # -  If the execution mode is periodic, the value is the number of times it has been executed.
        self.repeats = repeats
        # Start Time
        self.start_time = start_time
        # The time when `StopInvocation` was called to stop the command execution.
        self.stop_time = stop_time
        # Whether the queried command will be automatically executed in the future. The value range is as follows:
        # - true: The command, when executed by calling `RunCommand` or `InvokeCommand`, has the `RepeatMode` parameter set to `Period`, `NextRebootOnly`, or `EveryReboot`. 
        # - false: Queries commands in the following two states. 
        # - When executing a command via `RunCommand` or `InvokeCommand`, the `RepeatMode` parameter is set to `Once`. 
        # - Commands that have been canceled, stopped, or completed.
        # 
        # Default value: false.
        self.timed = timed
        # Update Time
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
        # Command execution records for nodes.
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
        # Command content.
        # 
        # - If `ContentEncoding` is set to `PlainText`, the original script content is returned.
        # - If `ContentEncoding` is set to `Base64`, the Base64-encoded script content is returned.
        self.command_content = command_content
        # Command description.
        self.command_description = command_description
        # Command name.
        self.command_name = command_name
        # The creation time of the task.
        self.creation_time = creation_time
        # The execution time for scheduled commands.
        self.frequency = frequency
        # The overall execution status of the command, which depends on the common execution status of all instances involved in the call. Possible values:
        # - Pending: The system is validating or sending the command. If at least one instance has a command execution status of Pending, the overall status is Pending.
        # - Scheduled: The scheduled command has been sent and is waiting to run. If at least one instance has a command execution status of Scheduled, the overall status is Scheduled.
        # - Running: The command is running on the instance. If at least one instance has a command execution status of Running, the overall status is Running.
        # - Success: The command execution status of all instances is Stopped or Success, and at least one instance\\"s command execution status is Success. The overall status is Success.
        #     - For immediately executed tasks: The command has completed with an exit code of 0.
        #     - For periodically executed tasks: The most recent execution was successful with an exit code of 0, and the specified times have all been completed.
        # - Failed: The command execution status of all instances is Stopped or Failed. The overall status is Failed if any of the following conditions apply to the instance\\"s command execution status:
        #     - Command validation failed (Invalid).
        #     - Command sending failed (Aborted).
        #     - Command completed but the exit code is not 0 (Failed).
        #     - Command execution timed out (Timeout).
        #     - Command execution encountered an error (Error).
        # - Stopping: The task is being stopped. If at least one instance has a command execution status of Stopping, the overall status is Stopping.
        # - Stopped: The task has been stopped. If all instances\\" command execution statuses are Stopped, the overall status is Stopped. The overall status is Stopped if the instance\\"s command execution status is any of the following:
        #     - The task was canceled (Cancelled).
        #     - The task was terminated (Terminated).
        # - PartialFailed: Some instances succeeded and some failed. If the command execution statuses of all instances are Success, Failed, or Stopped, the overall status is PartialFailed.
        # 
        # > The `InvokeStatus` in the response parameters is similar in meaning to this parameter, but it is recommended that you check this return value.
        self.invocation_status = invocation_status
        # Command execution ID.
        self.invoke_id = invoke_id
        # Command execution records.
        self.invoke_nodes = invoke_nodes
        # The overall execution status of the command. The overall execution status depends on the common execution status of one or more instances in the execution. Possible values: 
        # - Running:
        #     - For scheduled execution: The execution status remains ongoing until the scheduled command is manually stopped.
        #     - For single execution: If there is any command process running, the overall execution status is ongoing.
        # - Finished:
        #     - For scheduled execution: The command process cannot be completed.
        #     - For single execution: All instances have completed execution, or some instances\\" command processes are manually stopped and the rest have completed.
        # - Failed:
        #     - For scheduled execution: The command process cannot fail.
        #     - For single execution: All instances have failed to execute.
        # - Stopped: The command has been stopped.
        # - Stopping: The command is being stopped.
        # - PartialFailed: Partial failure; if the `InstanceId` parameter is set, this does not apply.
        self.invoke_status = invoke_status
        # Custom parameters in the command.
        self.parameters = parameters
        # 命令执行的方式。可能值：
        # 
        # Once：立即执行命令。
        # Period：定时执行命令。
        # NextRebootOnly：当实例下一次启动时，自动执行命令。
        # EveryReboot：实例每一次启动都将自动执行命令。
        self.repeat_mode = repeat_mode
        # Timeout for executing the command, in seconds.
        self.timeout = timeout
        # Username for executing the command.
        self.username = username
        # The working directory of the command on the instance.
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
        # File delivery record.
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
        # Script execution record object.
        self.invocations = invocations
        # Request ID
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


class DescribeNetTestResultRequest(TeaModel):
    def __init__(
        self,
        test_id: str = None,
    ):
        # Test task ID.
        self.test_id = test_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.test_id is not None:
            result['TestId'] = self.test_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')
        return self


class DescribeNetTestResultResponseBodyCommTestHosts(TeaModel):
    def __init__(
        self,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # IP address
        self.ip = ip
        # Resource ID
        self.resource_id = resource_id
        # 服务名称。
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class DescribeNetTestResultResponseBodyCommTest(TeaModel):
    def __init__(
        self,
        gpunum: str = None,
        hosts: List[DescribeNetTestResultResponseBodyCommTestHosts] = None,
        model: str = None,
        type: str = None,
    ):
        # Number of GPUs
        self.gpunum = gpunum
        # Resource ID
        self.hosts = hosts
        # Communication library model
        self.model = model
        # Communication library test category: ACCL or NCCL
        self.type = type

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpunum is not None:
            result['GPUNum'] = self.gpunum
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.model is not None:
            result['Model'] = self.model
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GPUNum') is not None:
            self.gpunum = m.get('GPUNum')
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = DescribeNetTestResultResponseBodyCommTestHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DescribeNetTestResultResponseBodyDelayTestHosts(TeaModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network card bond interface
        self.bond = bond
        # Node IP
        self.ip = ip
        # Resource ID
        self.resource_id = resource_id
        # Service name
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond is not None:
            result['Bond'] = self.bond
        if self.ip is not None:
            result['IP'] = self.ip
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class DescribeNetTestResultResponseBodyDelayTest(TeaModel):
    def __init__(
        self,
        hosts: List[DescribeNetTestResultResponseBodyDelayTestHosts] = None,
    ):
        # Input the hosts of the test nodes
        self.hosts = hosts

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = DescribeNetTestResultResponseBodyDelayTestHosts()
                self.hosts.append(temp_model.from_map(k))
        return self


class DescribeNetTestResultResponseBodyTrafficTestClients(TeaModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network card bond interface
        self.bond = bond
        # Node IP
        self.ip = ip
        # Resource ID
        self.resource_id = resource_id
        # 服务名称。
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond is not None:
            result['Bond'] = self.bond
        if self.ip is not None:
            result['IP'] = self.ip
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class DescribeNetTestResultResponseBodyTrafficTestServers(TeaModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network card bond interface
        self.bond = bond
        # Node IP
        self.ip = ip
        # Resource ID
        self.resource_id = resource_id
        # Service name
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond is not None:
            result['Bond'] = self.bond
        if self.ip is not None:
            result['IP'] = self.ip
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class DescribeNetTestResultResponseBodyTrafficTest(TeaModel):
    def __init__(
        self,
        clients: List[DescribeNetTestResultResponseBodyTrafficTestClients] = None,
        duration: int = None,
        gdr: str = None,
        protocol: str = None,
        qp: int = None,
        servers: List[DescribeNetTestResultResponseBodyTrafficTestServers] = None,
        traffic_model: str = None,
    ):
        # Resource ID.
        self.clients = clients
        # Duration of the workflow task in seconds.
        self.duration = duration
        # For RDMA, enter True/False; for TCP, this field is empty.
        self.gdr = gdr
        # Network protocol, either RDMA or TCP.
        self.protocol = protocol
        # For TCP, enter the number of concurrent test connections; for RDMA, enter the configured QP value.
        self.qp = qp
        # List of servers
        self.servers = servers
        # Traffic model, either MTON or Fullmesh.
        self.traffic_model = traffic_model

    def validate(self):
        if self.clients:
            for k in self.clients:
                if k:
                    k.validate()
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clients'] = []
        if self.clients is not None:
            for k in self.clients:
                result['Clients'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.gdr is not None:
            result['GDR'] = self.gdr
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.qp is not None:
            result['QP'] = self.qp
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        if self.traffic_model is not None:
            result['TrafficModel'] = self.traffic_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clients = []
        if m.get('Clients') is not None:
            for k in m.get('Clients'):
                temp_model = DescribeNetTestResultResponseBodyTrafficTestClients()
                self.clients.append(temp_model.from_map(k))
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('GDR') is not None:
            self.gdr = m.get('GDR')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('QP') is not None:
            self.qp = m.get('QP')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = DescribeNetTestResultResponseBodyTrafficTestServers()
                self.servers.append(temp_model.from_map(k))
        if m.get('TrafficModel') is not None:
            self.traffic_model = m.get('TrafficModel')
        return self


class DescribeNetTestResultResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        comm_test: DescribeNetTestResultResponseBodyCommTest = None,
        creation_time: str = None,
        delay_test: DescribeNetTestResultResponseBodyDelayTest = None,
        finished_time: str = None,
        net_test_type: str = None,
        port: str = None,
        request_id: str = None,
        result_detial: str = None,
        status: str = None,
        test_id: str = None,
        traffic_test: DescribeNetTestResultResponseBodyTrafficTest = None,
    ):
        # Cluster ID.
        self.cluster_id = cluster_id
        # Cluster name.
        self.cluster_name = cluster_name
        # Fill in when the traffic test type is communication library test
        self.comm_test = comm_test
        # Diagnosis task creation time.
        self.creation_time = creation_time
        # Fill in when the network test type is latency test
        self.delay_test = delay_test
        # Diagnosis task completion time.
        self.finished_time = finished_time
        # Network test type.
        self.net_test_type = net_test_type
        # Test port number.
        self.port = port
        # Request ID
        self.request_id = request_id
        # Details of the diagnosis result. Returned as a JSON string.
        self.result_detial = result_detial
        # Diagnosis task status. Possible values:
        # - InProgress: Diagnosis in progress.
        # - Finished: Diagnosis completed.
        # - Failed: Diagnosis failed.
        self.status = status
        # Initiated test task ID, which is the unique identifier for the network test task.
        self.test_id = test_id
        # This field is empty if the traffic model (TrafficModel) is Fullmesh.
        self.traffic_test = traffic_test

    def validate(self):
        if self.comm_test:
            self.comm_test.validate()
        if self.delay_test:
            self.delay_test.validate()
        if self.traffic_test:
            self.traffic_test.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.comm_test is not None:
            result['CommTest'] = self.comm_test.to_map()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.delay_test is not None:
            result['DelayTest'] = self.delay_test.to_map()
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.net_test_type is not None:
            result['NetTestType'] = self.net_test_type
        if self.port is not None:
            result['Port'] = self.port
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_detial is not None:
            result['ResultDetial'] = self.result_detial
        if self.status is not None:
            result['Status'] = self.status
        if self.test_id is not None:
            result['TestId'] = self.test_id
        if self.traffic_test is not None:
            result['TrafficTest'] = self.traffic_test.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CommTest') is not None:
            temp_model = DescribeNetTestResultResponseBodyCommTest()
            self.comm_test = temp_model.from_map(m['CommTest'])
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DelayTest') is not None:
            temp_model = DescribeNetTestResultResponseBodyDelayTest()
            self.delay_test = temp_model.from_map(m['DelayTest'])
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('NetTestType') is not None:
            self.net_test_type = m.get('NetTestType')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultDetial') is not None:
            self.result_detial = m.get('ResultDetial')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')
        if m.get('TrafficTest') is not None:
            temp_model = DescribeNetTestResultResponseBodyTrafficTest()
            self.traffic_test = temp_model.from_map(m['TrafficTest'])
        return self


class DescribeNetTestResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNetTestResultResponseBody = None,
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
            temp_model = DescribeNetTestResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeNodeRequest(TeaModel):
    def __init__(
        self,
        node_id: str = None,
    ):
        # Node ID
        # 
        # This parameter is required.
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
        # Network interface port information
        self.bond_name = bond_name
        # Machine IP
        self.ip = ip
        # Cluster subnet ID
        self.subnet_id = subnet_id
        # Cluster network ID
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
        user_data: str = None,
        zone_id: str = None,
    ):
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster name
        self.cluster_name = cluster_name
        # Creation time
        self.create_time = create_time
        # Expiration time
        self.expired_time = expired_time
        # Hostname
        self.hostname = hostname
        # Cluster number
        self.hpn_zone = hpn_zone
        # Image ID
        self.image_id = image_id
        # Image name
        self.image_name = image_name
        # Machine type
        self.machine_type = machine_type
        # Network information
        self.networks = networks
        # Node group ID
        self.node_group_id = node_group_id
        # Node group name
        self.node_group_name = node_group_name
        # Node ID
        self.node_id = node_id
        # Node status
        self.operating_state = operating_state
        # Request ID
        self.request_id = request_id
        # 资源组ID
        self.resource_group_id = resource_group_id
        # Unique machine identifier
        self.sn = sn
        self.user_data = user_data
        # Zone ID
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
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
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
        # Filter the returned results based on Chinese, English, and Japanese. For more information, see RFC7231. Valid values:
        # 
        # zh-CN
        # en-US
        # Default value: zh-CN
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
        # Region name
        self.local_name = local_name
        # region id
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
        # List of region information.
        self.regions = regions
        # Request ID
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
        # Command execution ID.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # Node ID
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
        # The creation time of the file distribution task.
        self.creation_time = creation_time
        # The failure reason code for file distribution. Possible values:
        # - Empty: The file was distributed normally. 
        # - NodeNotExists: The specified instance does not exist or has been released. 
        # - NodeReleased: The instance was released during the file distribution process. 
        # - NodeNotRunning: The instance was not running when the file distribution task was created. 
        # - AccountNotExists: The specified account does not exist. 
        # - ClientNotRunning: The Cloud Assistant Agent is not running. 
        # - ClientNotResponse: The Cloud Assistant Agent is not responding. 
        # - ClientIsUpgrading: The Cloud Assistant Agent is currently being upgraded. 
        # - ClientNeedUpgrade: The Cloud Assistant Agent needs to be upgraded. 
        # - DeliveryTimeout: File delivery timed out. 
        # - FileCreateFail: Failed to create the file. 
        # - FileAlreadyExists: A file with the same name already exists at the specified path. 
        # - FileContentInvalid: The file content is invalid. 
        # - FileNameInvalid: The file name is invalid. 
        # - FilePathInvalid: The file path is invalid. 
        # - FileAuthorityInvalid: The file permissions are invalid. 
        # - UserGroupNotExists: The user group specified for file delivery does not exist.
        self.error_code = error_code
        # Details of the reason for command delivery failure or execution failure, possible values: 
        # - Empty: The command executed normally. 
        # - the specified instance does not exist: The specified instance does not exist or has been released. 
        # - the node has been released when creating task: The instance was released during the command execution. 
        # - the node is not running when creating task: The instance was not in a running state when the command was executed. 
        # - the command is not applicable: The command is not applicable to the specified instance. 
        # - the specified account does not exist: The specified account does not exist. 
        # - the specified directory does not exist: The specified directory does not exist. 
        # - the cron job expression is invalid: The specified execution time expression is invalid. 
        # - the aliyun service is not running on the instance: The Cloud Assistant Agent is not running. 
        # - the aliyun service in the instance does not respond: The Cloud Assistant Agent is not responding. 
        # - the aliyun service in the node is upgrading now: The Cloud Assistant Agent is currently being upgraded. 
        # - the aliyun service in the node needs upgrade: The Cloud Assistant Agent needs an upgrade. 
        # - the command delivery has timed out: Command delivery has timed out. 
        # - the command execution has timed out: Command execution has timed out. 
        # - the command execution got an exception: An exception occurred during command execution. 
        # - the command execution has been interrupted: The command execution was interrupted. 
        # - the command execution exit code is not zero: The command execution completed with a non-zero exit code. 
        # - the specified instance has been released: The instance was released during file delivery.
        self.error_info = error_info
        # Completion time, format: "2020-05-22T17:04:18".
        self.finish_time = finish_time
        # Status of the task on a single instance. Possible values:
        # - Pending: The system is validating or distributing the file.
        # - Invalid: The specified file parameters are incorrect, and validation failed.
        # - Running: The file is being distributed to the instance.
        # - Aborted: Failed to distribute the file to the instance.
        # - Success: The file distribution is complete.
        # - Failed: The file creation failed within the instance.
        # - Error: An exception occurred during file distribution and could not continue.
        # - Timeout: The file distribution timed out.
        self.invocation_status = invocation_status
        # Node ID.
        self.node_id = node_id
        # Start Time
        self.start_time = start_time
        # Update Time
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
        # Record of file distribution for the node.
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
        # Output information after command execution.
        # 
        # If ContentEncoding is specified as PlainText, the original output information is returned.
        # If ContentEncoding is specified as Base64, the Base64 encoded output information is returned.
        self.content = content
        # File content type.
        # 
        # PlainText: Plain text.
        # Base64: Base64 encoding.
        # The default value is PlainText.
        self.content_type = content_type
        # Creation time of the distribution.
        self.creation_time = creation_time
        # Command description.
        self.description = description
        # The user group of the file.
        self.file_group = file_group
        # File permissions.
        self.file_mode = file_mode
        # The owner of the file.
        self.file_owner = file_owner
        # Overall status of the file distribution. The overall status depends on the common execution status of all instances involved in this distribution, possible values are:
        # 
        # - Pending: The system is verifying or distributing the file. If at least one instance has a file distribution status of Pending, the overall execution status will be Pending.
        # - Running: The file is being distributed on the instance. If at least one instance has a file distribution status of Running, the overall execution status will be Running.
        # - Success: All instances have a file distribution status of Success, then the overall execution status will be Success.
        # - Failed: All instances have a file distribution status of Failed, then the overall execution status will be Failed. If any of the following conditions occur for the file distribution status on an instance, the return value will be Failed:
        #     - The specified file parameters are incorrect, verification failed (Invalid).
        #     - Failed to distribute the file to the instance (Aborted).
        #     - The file creation failed within the instance (Failed).
        #     - The file distribution timed out (Timeout).
        #     - An exception occurred during file distribution and could not continue (Error).
        # - PartialFailed: Some instances successfully received the file while others failed. If the file distribution status of all instances is either Success or Failed, the overall execution status will be PartialFailed.
        self.invocation_status = invocation_status
        # Record of file distribution.
        self.invoke_nodes = invoke_nodes
        # Name of the file distribution.
        self.name = name
        # Number of nodes
        self.node_count = node_count
        # Whether to overwrite the file if a file with the same name already exists in the target directory.
        # - true: Overwrite.
        # - false: Do not overwrite.
        # 
        # The default value is false.
        self.overwrite = overwrite
        # Target path.
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
        # Command execution ID.
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
        # Record of file distribution.
        self.invocations = invocations
        # ID of the request
        self.request_id = request_id
        # Total number of commands.
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
        # Task ID
        # 
        # This parameter is required.
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
        # Creation Time
        self.create_time = create_time
        # Subtask Failure Message
        self.message = message
        # Task ID
        self.task_id = task_id
        # Task Execution State
        self.task_state = task_state
        # Task Type
        self.task_type = task_type
        # Update Time
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
        # Step Failure Message
        self.message = message
        # Stage Tag
        self.stage_tag = stage_tag
        # Start Time
        self.start_time = start_time
        # Step Name
        self.step_name = step_name
        # Step Execution State
        self.step_state = step_state
        # Step Type
        self.step_type = step_type
        # Subtasks
        self.sub_tasks = sub_tasks
        # Update Time
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
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster Name
        self.cluster_name = cluster_name
        # Start Time
        self.create_time = create_time
        # Task Failure Message
        self.message = message
        # List of node IDs
        self.node_ids = node_ids
        # Request ID
        self.request_id = request_id
        # Execution Steps
        self.steps = steps
        # Task State
        self.task_state = task_state
        # Task Type
        self.task_type = task_type
        # Update Time
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
        # Filter the returned results based on Chinese or English. For more information, see RFC7231. Valid values:
        # 
        # zh-CN
        # en-US
        # Default value: zh-CN
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
        # Zone name
        self.local_name = local_name
        # Zone ID
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
        # Request ID
        self.request_id = request_id
        # List of available zones
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
        # Bond name
        self.name = name
        # IP source cluster subnet
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
        # Default bond cluster subnet
        self.bond_default_subnet = bond_default_subnet
        # Bond information
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
        # Bond name
        self.name = name
        # IP source cluster subnet
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
        # Bond information
        self.bonds = bonds
        # Machine Type
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
        # Bond name
        self.name = name
        # IP source cluster subnet
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
        # Bond information
        self.bonds = bonds
        # Node ID
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
        # Specify the cluster subnet ID based on the bond name
        self.bond_policy = bond_policy
        # Machine type allocation policy
        self.machine_type_policy = machine_type_policy
        # Node allocation policy
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
        # Hostname
        self.hostname = hostname
        # Login Password
        self.login_password = login_password
        # Node ID
        self.node_id = node_id
        # VSwitch ID
        self.v_switch_id = v_switch_id
        # VPC ID
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
        # Node Group ID
        self.node_group_id = node_group_id
        # List of Nodes
        self.nodes = nodes
        # Custom Data
        self.user_data = user_data
        # Zone ID
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
        # Cluster ID
        self.cluster_id = cluster_id
        # Whether to allow skipping failed node tasks, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # IP allocation policy combination: Each policy can only choose one type, and multiple policies can be combined
        self.ip_allocation_policy = ip_allocation_policy
        # Node Group
        self.node_groups = node_groups
        # VSwitch availability zone ID
        self.v_switch_zone_id = v_switch_zone_id
        # List of cluster subnets
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
        # Cluster ID
        self.cluster_id = cluster_id
        # Whether to allow skipping failed node tasks, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # IP allocation policy combination: Each policy can only choose one type, and multiple policies can be combined
        self.ip_allocation_policy_shrink = ip_allocation_policy_shrink
        # Node Group
        self.node_groups_shrink = node_groups_shrink
        # VSwitch availability zone ID
        self.v_switch_zone_id = v_switch_zone_id
        # List of cluster subnets
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
        # Request ID
        self.request_id = request_id
        # Task ID
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


class ListClusterNodesRequestTags(TeaModel):
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


class ListClusterNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_id: str = None,
        resource_group_id: str = None,
        tags: List[ListClusterNodesRequestTags] = None,
    ):
        # Cluster ID
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Number of items per page in a paginated query, with a default value of 20.
        self.max_results = max_results
        # Query token (Token), which is the value of the NextToken parameter returned by the previous API call.
        self.next_token = next_token
        # Node group ID
        self.node_group_id = node_group_id
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListClusterNodesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListClusterNodesResponseBodyNodesNetworks(TeaModel):
    def __init__(
        self,
        bond_name: str = None,
        ip: str = None,
        subnet_id: str = None,
        vpd_id: str = None,
    ):
        # Machine network interface name
        self.bond_name = bond_name
        # IP address within the VPC
        self.ip = ip
        # VPC subnet ID
        self.subnet_id = subnet_id
        # VPC ID
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


class ListClusterNodesResponseBodyNodesTags(TeaModel):
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


class ListClusterNodesResponseBodyNodes(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        create_time: str = None,
        expired_time: str = None,
        hostname: str = None,
        hpn_zone: str = None,
        image_id: str = None,
        image_name: str = None,
        machine_type: str = None,
        networks: List[ListClusterNodesResponseBodyNodesNetworks] = None,
        node_group_id: str = None,
        node_group_name: str = None,
        node_id: str = None,
        operating_state: str = None,
        sn: str = None,
        tags: List[ListClusterNodesResponseBodyNodesTags] = None,
        task_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        self.commodity_code = commodity_code
        # Creation time
        self.create_time = create_time
        # Machine expiration time
        self.expired_time = expired_time
        # Hostname
        self.hostname = hostname
        # Hpn Zone
        self.hpn_zone = hpn_zone
        # System image ID
        self.image_id = image_id
        self.image_name = image_name
        # Machine type
        self.machine_type = machine_type
        # Network information
        self.networks = networks
        # Node group ID
        self.node_group_id = node_group_id
        # Node group name
        self.node_group_name = node_group_name
        # Node ID
        self.node_id = node_id
        # Node status
        self.operating_state = operating_state
        # Machine SN
        self.sn = sn
        self.tags = tags
        self.task_id = task_id
        # 专有网络交换机ID
        self.v_switch_id = v_switch_id
        # 专有网络ID
        self.vpc_id = vpc_id
        # Zone ID
        self.zone_id = zone_id

    def validate(self):
        if self.networks:
            for k in self.networks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
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
        if self.sn is not None:
            result['Sn'] = self.sn
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListClusterNodesResponseBodyNodesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
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
        # The query token value returned by this call.
        self.next_token = next_token
        # List of nodes
        self.nodes = nodes
        # Request ID
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


class ListClustersRequestTags(TeaModel):
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


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        tags: List[ListClustersRequestTags] = None,
    ):
        # Number of items per page for paginated queries, with a default value of 20.
        self.max_results = max_results
        # Query token, which is the value of the NextToken parameter returned by the previous API call.
        self.next_token = next_token
        # Resource group ID
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListClustersRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListClustersResponseBodyClustersTags(TeaModel):
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


class ListClustersResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_description: str = None,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
        components: Any = None,
        computing_ip_version: str = None,
        create_time: str = None,
        hpn_zone: str = None,
        node_count: int = None,
        node_group_count: int = None,
        operating_state: str = None,
        resource_group_id: str = None,
        tags: List[ListClustersResponseBodyClustersTags] = None,
        task_id: str = None,
        update_time: str = None,
        vpc_id: str = None,
    ):
        # Cluster description
        self.cluster_description = cluster_description
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster name
        self.cluster_name = cluster_name
        # Cluster type
        self.cluster_type = cluster_type
        # Component information
        self.components = components
        # IP version of the computing network
        self.computing_ip_version = computing_ip_version
        # Creation time
        self.create_time = create_time
        # Cluster number
        self.hpn_zone = hpn_zone
        # Number of nodes
        self.node_count = node_count
        # Number of node groups
        self.node_group_count = node_group_count
        # Cluster status
        self.operating_state = operating_state
        # Resource group ID
        self.resource_group_id = resource_group_id
        self.tags = tags
        # Task ID
        self.task_id = task_id
        # Update time
        self.update_time = update_time
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        if self.tags:
            for k in self.tags:
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
        if self.components is not None:
            result['Components'] = self.components
        if self.computing_ip_version is not None:
            result['ComputingIpVersion'] = self.computing_ip_version
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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('ComputingIpVersion') is not None:
            self.computing_ip_version = m.get('ComputingIpVersion')
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListClustersResponseBodyClustersTags()
                self.tags.append(temp_model.from_map(k))
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
        # Cluster information
        self.clusters = clusters
        # The query token value returned by this call.
        self.next_token = next_token
        # Request ID
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


class ListDiagnosticResultsRequest(TeaModel):
    def __init__(
        self,
        diag_type: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        # Type of diagnosis
        self.diag_type = diag_type
        # Number of items per page in a paginated query. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 20, the default is 20.
        # - If the set value is greater than 100, the default is 100.
        self.max_results = max_results
        # Query token (Token), the value should be the NextToken parameter value returned from the previous API call.
        self.next_token = next_token
        # Resource group ID
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diag_type is not None:
            result['DiagType'] = self.diag_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiagType') is not None:
            self.diag_type = m.get('DiagType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListDiagnosticResultsResponseBodyDiagnosticResults(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        creation_time: str = None,
        diag_content: str = None,
        diag_id: str = None,
        diag_result: str = None,
        finished_time: str = None,
        resource_id: str = None,
        server_name: str = None,
        status: str = None,
    ):
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster name
        self.cluster_name = cluster_name
        # Creation time of the diagnostic task.
        self.creation_time = creation_time
        # Diagnosis content. For example, in network diagnosis, there are static configuration checks, dynamic operation checks, etc.
        self.diag_content = diag_content
        # Diagnosis ID
        self.diag_id = diag_id
        # Diagnosis result, success or failure.
        self.diag_result = diag_result
        # Completion time of the diagnostic task.
        self.finished_time = finished_time
        # Resource ID
        self.resource_id = resource_id
        # Service name.
        self.server_name = server_name
        # Governance status
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.diag_content is not None:
            result['DiagContent'] = self.diag_content
        if self.diag_id is not None:
            result['DiagId'] = self.diag_id
        if self.diag_result is not None:
            result['DiagResult'] = self.diag_result
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DiagContent') is not None:
            self.diag_content = m.get('DiagContent')
        if m.get('DiagId') is not None:
            self.diag_id = m.get('DiagId')
        if m.get('DiagResult') is not None:
            self.diag_result = m.get('DiagResult')
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListDiagnosticResultsResponseBody(TeaModel):
    def __init__(
        self,
        diagnostic_results: List[ListDiagnosticResultsResponseBodyDiagnosticResults] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # Diagnostic information
        self.diagnostic_results = diagnostic_results
        # 分页查询时每页行数。最大值为100。
        # 
        # 默认值：
        # 
        # •当不设置值或设置的值小于20时，默认值为20。
        # 
        # •当设置的值大于100时，默认值为100。
        self.max_results = max_results
        # NextToken for the next page. Include this value when requesting the next page.
        self.next_token = next_token
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.diagnostic_results:
            for k in self.diagnostic_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DiagnosticResults'] = []
        if self.diagnostic_results is not None:
            for k in self.diagnostic_results:
                result['DiagnosticResults'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.diagnostic_results = []
        if m.get('DiagnosticResults') is not None:
            for k in m.get('DiagnosticResults'):
                temp_model = ListDiagnosticResultsResponseBodyDiagnosticResults()
                self.diagnostic_results.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDiagnosticResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDiagnosticResultsResponseBody = None,
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
            temp_model = ListDiagnosticResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFreeNodesRequestTags(TeaModel):
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


class ListFreeNodesRequest(TeaModel):
    def __init__(
        self,
        hpn_zone: str = None,
        machine_type: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        tags: List[ListFreeNodesRequestTags] = None,
    ):
        # Cluster number
        self.hpn_zone = hpn_zone
        # Machine type
        self.machine_type = machine_type
        # Number of items per page for paginated queries, default is 20.
        self.max_results = max_results
        # Query token (Token), the value should be the NextToken parameter value returned from the previous API call.
        self.next_token = next_token
        # Resource group ID
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListFreeNodesRequestTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListFreeNodesResponseBodyNodesTags(TeaModel):
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


class ListFreeNodesResponseBodyNodes(TeaModel):
    def __init__(
        self,
        commodity_code: str = None,
        create_time: str = None,
        expired_time: str = None,
        hpn_zone: str = None,
        machine_type: str = None,
        node_id: str = None,
        operating_state: str = None,
        resource_group_id: str = None,
        sn: str = None,
        tags: List[ListFreeNodesResponseBodyNodesTags] = None,
        zone_id: str = None,
    ):
        self.commodity_code = commodity_code
        # Creation time
        self.create_time = create_time
        # Expiration time of the machine
        self.expired_time = expired_time
        # Cluster number
        self.hpn_zone = hpn_zone
        # Machine type
        self.machine_type = machine_type
        # Node ID
        self.node_id = node_id
        self.operating_state = operating_state
        # Resource group ID
        self.resource_group_id = resource_group_id
        # Machine SN
        self.sn = sn
        self.tags = tags
        # Availability zone ID
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
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
        if self.operating_state is not None:
            result['OperatingState'] = self.operating_state
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sn is not None:
            result['Sn'] = self.sn
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
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
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('OperatingState') is not None:
            self.operating_state = m.get('OperatingState')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListFreeNodesResponseBodyNodesTags()
                self.tags.append(temp_model.from_map(k))
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
        # The query token value returned by this call.
        self.next_token = next_token
        # List of nodes
        self.nodes = nodes
        # Request ID
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


class ListImagesRequest(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        image_version: str = None,
        platform: str = None,
    ):
        # Architecture
        self.architecture = architecture
        # Image version
        self.image_version = image_version
        # Platform
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class ListImagesResponseBodyImages(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        description: str = None,
        image_id: str = None,
        image_name: str = None,
        image_version: str = None,
        node_count: int = None,
        platform: str = None,
        release_file_md_5: str = None,
        release_file_size: int = None,
        type: str = None,
    ):
        # Architecture
        self.architecture = architecture
        # Description
        self.description = description
        # Image ID
        self.image_id = image_id
        # Image name
        self.image_name = image_name
        # Image version
        self.image_version = image_version
        # node count
        self.node_count = node_count
        # Platform
        self.platform = platform
        # File MD5
        self.release_file_md_5 = release_file_md_5
        # Image size
        self.release_file_size = release_file_size
        # image type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.description is not None:
            result['Description'] = self.description
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.release_file_md_5 is not None:
            result['ReleaseFileMd5'] = self.release_file_md_5
        if self.release_file_size is not None:
            result['ReleaseFileSize'] = self.release_file_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('ReleaseFileMd5') is not None:
            self.release_file_md_5 = m.get('ReleaseFileMd5')
        if m.get('ReleaseFileSize') is not None:
            self.release_file_size = m.get('ReleaseFileSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListImagesResponseBody(TeaModel):
    def __init__(
        self,
        images: List[ListImagesResponseBodyImages] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # Image details
        self.images = images
        # NextToken for the next page, include this value when requesting the next page
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListImagesResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListImagesResponseBody = None,
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
            temp_model = ListImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMachineNetworkInfoRequestMachineHpnInfo(TeaModel):
    def __init__(
        self,
        hpn_zone: str = None,
        machine_type: str = None,
        region_id: str = None,
    ):
        # Cluster ID
        self.hpn_zone = hpn_zone
        # Machine type
        self.machine_type = machine_type
        # Region ID
        self.region_id = region_id

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListMachineNetworkInfoRequest(TeaModel):
    def __init__(
        self,
        machine_hpn_info: List[ListMachineNetworkInfoRequestMachineHpnInfo] = None,
    ):
        # Array
        self.machine_hpn_info = machine_hpn_info

    def validate(self):
        if self.machine_hpn_info:
            for k in self.machine_hpn_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MachineHpnInfo'] = []
        if self.machine_hpn_info is not None:
            for k in self.machine_hpn_info:
                result['MachineHpnInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machine_hpn_info = []
        if m.get('MachineHpnInfo') is not None:
            for k in m.get('MachineHpnInfo'):
                temp_model = ListMachineNetworkInfoRequestMachineHpnInfo()
                self.machine_hpn_info.append(temp_model.from_map(k))
        return self


class ListMachineNetworkInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        machine_hpn_info_shrink: str = None,
    ):
        # Array
        self.machine_hpn_info_shrink = machine_hpn_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.machine_hpn_info_shrink is not None:
            result['MachineHpnInfo'] = self.machine_hpn_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MachineHpnInfo') is not None:
            self.machine_hpn_info_shrink = m.get('MachineHpnInfo')
        return self


class ListMachineNetworkInfoResponseBodyMachineNetworkInfo(TeaModel):
    def __init__(
        self,
        cluster_net: str = None,
        enable_jumbo_frame: bool = None,
        hpn_zone: str = None,
        is_dpu_mode: bool = None,
        machine_type: str = None,
        net_arch: str = None,
        region_id: str = None,
    ):
        # Cluster network
        self.cluster_net = cluster_net
        # Whether jumbo frame capability is enabled
        self.enable_jumbo_frame = enable_jumbo_frame
        # Cluster ID
        self.hpn_zone = hpn_zone
        # Whether it is in DPU mode
        self.is_dpu_mode = is_dpu_mode
        # Machine type
        self.machine_type = machine_type
        # Network architecture
        self.net_arch = net_arch
        # 地域ID。
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_net is not None:
            result['ClusterNet'] = self.cluster_net
        if self.enable_jumbo_frame is not None:
            result['EnableJumboFrame'] = self.enable_jumbo_frame
        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone
        if self.is_dpu_mode is not None:
            result['IsDpuMode'] = self.is_dpu_mode
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.net_arch is not None:
            result['NetArch'] = self.net_arch
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterNet') is not None:
            self.cluster_net = m.get('ClusterNet')
        if m.get('EnableJumboFrame') is not None:
            self.enable_jumbo_frame = m.get('EnableJumboFrame')
        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')
        if m.get('IsDpuMode') is not None:
            self.is_dpu_mode = m.get('IsDpuMode')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('NetArch') is not None:
            self.net_arch = m.get('NetArch')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListMachineNetworkInfoResponseBody(TeaModel):
    def __init__(
        self,
        machine_network_info: List[ListMachineNetworkInfoResponseBodyMachineNetworkInfo] = None,
        request_id: str = None,
    ):
        # Array
        self.machine_network_info = machine_network_info
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.machine_network_info:
            for k in self.machine_network_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MachineNetworkInfo'] = []
        if self.machine_network_info is not None:
            for k in self.machine_network_info:
                result['MachineNetworkInfo'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machine_network_info = []
        if m.get('MachineNetworkInfo') is not None:
            for k in m.get('MachineNetworkInfo'):
                temp_model = ListMachineNetworkInfoResponseBodyMachineNetworkInfo()
                self.machine_network_info.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMachineNetworkInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMachineNetworkInfoResponseBody = None,
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
            temp_model = ListMachineNetworkInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMachineTypesRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # Machine name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListMachineTypesResponseBodyMachineTypes(TeaModel):
    def __init__(
        self,
        bond_num: int = None,
        cpu_info: str = None,
        disk_info: str = None,
        gpu_info: str = None,
        memory_info: str = None,
        name: str = None,
        network_info: str = None,
        node_count: str = None,
        total_cpu_core: int = None,
        type: str = None,
    ):
        # Number of bonds
        self.bond_num = bond_num
        # CPU information
        self.cpu_info = cpu_info
        # Disk information
        self.disk_info = disk_info
        # GPU information
        self.gpu_info = gpu_info
        # Memory information
        self.memory_info = memory_info
        # Machine name
        self.name = name
        # Network information
        self.network_info = network_info
        # Number of nodes
        self.node_count = node_count
        # Number of CPU cores
        self.total_cpu_core = total_cpu_core
        # Type of machine
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond_num is not None:
            result['BondNum'] = self.bond_num
        if self.cpu_info is not None:
            result['CpuInfo'] = self.cpu_info
        if self.disk_info is not None:
            result['DiskInfo'] = self.disk_info
        if self.gpu_info is not None:
            result['GpuInfo'] = self.gpu_info
        if self.memory_info is not None:
            result['MemoryInfo'] = self.memory_info
        if self.name is not None:
            result['Name'] = self.name
        if self.network_info is not None:
            result['NetworkInfo'] = self.network_info
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.total_cpu_core is not None:
            result['TotalCpuCore'] = self.total_cpu_core
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BondNum') is not None:
            self.bond_num = m.get('BondNum')
        if m.get('CpuInfo') is not None:
            self.cpu_info = m.get('CpuInfo')
        if m.get('DiskInfo') is not None:
            self.disk_info = m.get('DiskInfo')
        if m.get('GpuInfo') is not None:
            self.gpu_info = m.get('GpuInfo')
        if m.get('MemoryInfo') is not None:
            self.memory_info = m.get('MemoryInfo')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NetworkInfo') is not None:
            self.network_info = m.get('NetworkInfo')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('TotalCpuCore') is not None:
            self.total_cpu_core = m.get('TotalCpuCore')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListMachineTypesResponseBody(TeaModel):
    def __init__(
        self,
        machine_types: List[ListMachineTypesResponseBodyMachineTypes] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # Details of the machine types
        self.machine_types = machine_types
        # NextToken for the next page, include this value when requesting the next page
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.machine_types:
            for k in self.machine_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MachineTypes'] = []
        if self.machine_types is not None:
            for k in self.machine_types:
                result['MachineTypes'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.machine_types = []
        if m.get('MachineTypes') is not None:
            for k in m.get('MachineTypes'):
                temp_model = ListMachineTypesResponseBodyMachineTypes()
                self.machine_types.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMachineTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMachineTypesResponseBody = None,
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
            temp_model = ListMachineTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNetTestResultsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        net_test_type: str = None,
        next_token: str = None,
        resource_group_id: str = None,
    ):
        # Number of items per page in a paginated query. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 20, the default is 20.
        # 
        # - If the set value is greater than 100, the default is 100.
        self.max_results = max_results
        # Type of network test.
        self.net_test_type = net_test_type
        # Query token (Token), which should be the value of the NextToken parameter returned from the previous API call.
        self.next_token = next_token
        # Resource group ID
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
        if self.net_test_type is not None:
            result['NetTestType'] = self.net_test_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NetTestType') is not None:
            self.net_test_type = m.get('NetTestType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListNetTestResultsResponseBodyNetTestResultsCommTestHosts(TeaModel):
    def __init__(
        self,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Node IP
        self.ip = ip
        # Resource ID
        self.resource_id = resource_id
        # Service name
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['IP'] = self.ip
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class ListNetTestResultsResponseBodyNetTestResultsCommTest(TeaModel):
    def __init__(
        self,
        gpunum: str = None,
        hosts: List[ListNetTestResultsResponseBodyNetTestResultsCommTestHosts] = None,
        model: str = None,
        type: str = None,
    ):
        # Number of GPUs
        self.gpunum = gpunum
        # Input hosts for the test nodes
        self.hosts = hosts
        # Communication library model
        self.model = model
        # Communication library test category: ACCL or NCCL
        self.type = type

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gpunum is not None:
            result['GPUNum'] = self.gpunum
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.model is not None:
            result['Model'] = self.model
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GPUNum') is not None:
            self.gpunum = m.get('GPUNum')
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListNetTestResultsResponseBodyNetTestResultsCommTestHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('Model') is not None:
            self.model = m.get('Model')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListNetTestResultsResponseBodyNetTestResultsDelayTestHosts(TeaModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Bond interface of the network card
        self.bond = bond
        # Node IP
        self.ip = ip
        # 资源id
        self.resource_id = resource_id
        # Service name
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond is not None:
            result['Bond'] = self.bond
        if self.ip is not None:
            result['IP'] = self.ip
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class ListNetTestResultsResponseBodyNetTestResultsDelayTest(TeaModel):
    def __init__(
        self,
        hosts: List[ListNetTestResultsResponseBodyNetTestResultsDelayTestHosts] = None,
    ):
        # Resource list
        self.hosts = hosts

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListNetTestResultsResponseBodyNetTestResultsDelayTestHosts()
                self.hosts.append(temp_model.from_map(k))
        return self


class ListNetTestResultsResponseBodyNetTestResultsTrafficTestClients(TeaModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network interface bond port
        self.bond = bond
        # IP address.
        self.ip = ip
        # Resource ID.
        self.resource_id = resource_id
        # Service name.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond is not None:
            result['Bond'] = self.bond
        if self.ip is not None:
            result['IP'] = self.ip
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class ListNetTestResultsResponseBodyNetTestResultsTrafficTestServers(TeaModel):
    def __init__(
        self,
        bond: str = None,
        ip: str = None,
        resource_id: str = None,
        server_name: str = None,
    ):
        # Network interface bond port
        self.bond = bond
        # Node IP
        self.ip = ip
        # Resource ID.
        self.resource_id = resource_id
        # Service name.
        self.server_name = server_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bond is not None:
            result['Bond'] = self.bond
        if self.ip is not None:
            result['IP'] = self.ip
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.server_name is not None:
            result['ServerName'] = self.server_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bond') is not None:
            self.bond = m.get('Bond')
        if m.get('IP') is not None:
            self.ip = m.get('IP')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ServerName') is not None:
            self.server_name = m.get('ServerName')
        return self


class ListNetTestResultsResponseBodyNetTestResultsTrafficTest(TeaModel):
    def __init__(
        self,
        clients: List[ListNetTestResultsResponseBodyNetTestResultsTrafficTestClients] = None,
        duration: int = None,
        gdr: str = None,
        protocol: str = None,
        qp: int = None,
        servers: List[ListNetTestResultsResponseBodyNetTestResultsTrafficTestServers] = None,
        traffic_model: str = None,
    ):
        # Clients
        self.clients = clients
        # Duration of the workflow task, in seconds.
        self.duration = duration
        # 协议为RDMA时，填写True/False，
        # 协议为TCP时，此字段为空。
        self.gdr = gdr
        # Network protocol, either RDMA or TCP.
        self.protocol = protocol
        # For TCP, enter the number of concurrent connections; for RDMA, enter the configured QP value.
        self.qp = qp
        # This field is empty when the traffic model (TrafficModel) is Fullmesh.
        self.servers = servers
        # Traffic model, either MTON or Fullmesh.
        self.traffic_model = traffic_model

    def validate(self):
        if self.clients:
            for k in self.clients:
                if k:
                    k.validate()
        if self.servers:
            for k in self.servers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Clients'] = []
        if self.clients is not None:
            for k in self.clients:
                result['Clients'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.gdr is not None:
            result['GDR'] = self.gdr
        if self.protocol is not None:
            result['Protocol'] = self.protocol
        if self.qp is not None:
            result['QP'] = self.qp
        result['Servers'] = []
        if self.servers is not None:
            for k in self.servers:
                result['Servers'].append(k.to_map() if k else None)
        if self.traffic_model is not None:
            result['TrafficModel'] = self.traffic_model
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clients = []
        if m.get('Clients') is not None:
            for k in m.get('Clients'):
                temp_model = ListNetTestResultsResponseBodyNetTestResultsTrafficTestClients()
                self.clients.append(temp_model.from_map(k))
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('GDR') is not None:
            self.gdr = m.get('GDR')
        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')
        if m.get('QP') is not None:
            self.qp = m.get('QP')
        self.servers = []
        if m.get('Servers') is not None:
            for k in m.get('Servers'):
                temp_model = ListNetTestResultsResponseBodyNetTestResultsTrafficTestServers()
                self.servers.append(temp_model.from_map(k))
        if m.get('TrafficModel') is not None:
            self.traffic_model = m.get('TrafficModel')
        return self


class ListNetTestResultsResponseBodyNetTestResults(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        comm_test: ListNetTestResultsResponseBodyNetTestResultsCommTest = None,
        creation_time: str = None,
        delay_test: ListNetTestResultsResponseBodyNetTestResultsDelayTest = None,
        finished_time: str = None,
        net_test_type: str = None,
        network_mode: str = None,
        port: str = None,
        status: str = None,
        test_id: str = None,
        traffic_test: ListNetTestResultsResponseBodyNetTestResultsTrafficTest = None,
    ):
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster name
        self.cluster_name = cluster_name
        # To be filled when the network test type is communication library test
        self.comm_test = comm_test
        # Creation time.
        self.creation_time = creation_time
        # Fill in when the network test type is latency test
        self.delay_test = delay_test
        # Completion time.
        self.finished_time = finished_time
        # Type of network test.
        self.net_test_type = net_test_type
        # Network mode
        self.network_mode = network_mode
        # Test port number.
        self.port = port
        # Status of the network test task. Possible values:</br>
        # - InProgress: Testing in progress.</br>
        # - Finished: Test completed.</br>
        # - Failed: Test failed.
        self.status = status
        # Test ID. A unique identifier for the resource test task.
        self.test_id = test_id
        # Fill in when the network test type is traffic test.
        self.traffic_test = traffic_test

    def validate(self):
        if self.comm_test:
            self.comm_test.validate()
        if self.delay_test:
            self.delay_test.validate()
        if self.traffic_test:
            self.traffic_test.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.comm_test is not None:
            result['CommTest'] = self.comm_test.to_map()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.delay_test is not None:
            result['DelayTest'] = self.delay_test.to_map()
        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time
        if self.net_test_type is not None:
            result['NetTestType'] = self.net_test_type
        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode
        if self.port is not None:
            result['Port'] = self.port
        if self.status is not None:
            result['Status'] = self.status
        if self.test_id is not None:
            result['TestId'] = self.test_id
        if self.traffic_test is not None:
            result['TrafficTest'] = self.traffic_test.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')
        if m.get('CommTest') is not None:
            temp_model = ListNetTestResultsResponseBodyNetTestResultsCommTest()
            self.comm_test = temp_model.from_map(m['CommTest'])
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('DelayTest') is not None:
            temp_model = ListNetTestResultsResponseBodyNetTestResultsDelayTest()
            self.delay_test = temp_model.from_map(m['DelayTest'])
        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')
        if m.get('NetTestType') is not None:
            self.net_test_type = m.get('NetTestType')
        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TestId') is not None:
            self.test_id = m.get('TestId')
        if m.get('TrafficTest') is not None:
            temp_model = ListNetTestResultsResponseBodyNetTestResultsTrafficTest()
            self.traffic_test = temp_model.from_map(m['TrafficTest'])
        return self


class ListNetTestResultsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        net_test_results: List[ListNetTestResultsResponseBodyNetTestResults] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # 分页查询时每页行数。最大值为100。
        # 
        # 默认值：
        # 
        # •当不设置值或设置的值小于20时，默认值为20。
        # 
        # •当设置的值大于100时，默认值为100。
        self.max_results = max_results
        # List of nodes
        self.net_test_results = net_test_results
        # NextToken for the next page, to be included in the request for the next page
        self.next_token = next_token
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.net_test_results:
            for k in self.net_test_results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        result['NetTestResults'] = []
        if self.net_test_results is not None:
            for k in self.net_test_results:
                result['NetTestResults'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        self.net_test_results = []
        if m.get('NetTestResults') is not None:
            for k in m.get('NetTestResults'):
                temp_model = ListNetTestResultsResponseBodyNetTestResults()
                self.net_test_results.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNetTestResultsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNetTestResultsResponseBody = None,
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
            temp_model = ListNetTestResultsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNodeGroupsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        max_results: int = None,
        next_token: str = None,
        node_group_id: str = None,
    ):
        # Cluster ID
        self.cluster_id = cluster_id
        # Number of items per page in a paginated query. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 20, the default value is 20.
        # - If the set value is greater than 100, the default value is 100.
        self.max_results = max_results
        # NextToken for the next page, include this value when requesting the next page
        self.next_token = next_token
        # Node group ID
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


class ListNodeGroupsResponseBodyGroups(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
        image_id: str = None,
        image_name: str = None,
        machine_type: str = None,
        node_count: int = None,
        update_time: str = None,
        zone_id: str = None,
    ):
        # Cluster ID
        self.cluster_id = cluster_id
        # Cluster name
        self.cluster_name = cluster_name
        # Creation time
        self.create_time = create_time
        # Description
        self.description = description
        # Group ID.
        self.group_id = group_id
        # Group name.
        self.group_name = group_name
        # Image ID
        self.image_id = image_id
        # Image name
        self.image_name = image_name
        # Machine type
        self.machine_type = machine_type
        # Number of nodes
        self.node_count = node_count
        # Update time
        self.update_time = update_time
        # 可用区id
        self.zone_id = zone_id

    def validate(self):
        pass

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
        if self.description is not None:
            result['Description'] = self.description
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_name is not None:
            result['ImageName'] = self.image_name
        if self.machine_type is not None:
            result['MachineType'] = self.machine_type
        if self.node_count is not None:
            result['NodeCount'] = self.node_count
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
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
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')
        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class ListNodeGroupsResponseBody(TeaModel):
    def __init__(
        self,
        groups: List[ListNodeGroupsResponseBodyGroups] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # Cluster group information
        self.groups = groups
        # NextToken for the next page, include this value when requesting the next page
        self.next_token = next_token
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['Groups'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k in m.get('Groups'):
                temp_model = ListNodeGroupsResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListNodeGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNodeGroupsResponseBody = None,
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
            temp_model = ListNodeGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key
        self.key = key
        # Tag value
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
        # Query token (Token), the value should be the NextToken returned from the previous API call
        self.next_token = next_token
        # Region ID
        # 
        # This parameter is required.
        self.region_id = region_id
        # List of resource IDs
        self.resource_id = resource_id
        # Resource type
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # List of tags
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
        # Resource ID
        self.resource_id = resource_id
        # Resource type
        self.resource_type = resource_type
        # Tag key
        self.tag_key = tag_key
        # Tag value
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
        # NextToken for the next page, include this returned value when requesting the next page
        self.next_token = next_token
        # Request ID
        self.request_id = request_id
        # Tagged resources.
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


class ListUserClusterTypesResponseBodyClusterTypes(TeaModel):
    def __init__(
        self,
        access_type: str = None,
        type_name: str = None,
    ):
        # 访问类型。
        self.access_type = access_type
        # Type name
        self.type_name = type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_type is not None:
            result['AccessType'] = self.access_type
        if self.type_name is not None:
            result['TypeName'] = self.type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessType') is not None:
            self.access_type = m.get('AccessType')
        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')
        return self


class ListUserClusterTypesResponseBody(TeaModel):
    def __init__(
        self,
        cluster_types: List[ListUserClusterTypesResponseBodyClusterTypes] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # List of cluster types. The number of array elements N ranges from 1 to 100.
        self.cluster_types = cluster_types
        # The NextToken for the next page. Include this value when requesting the next page.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.cluster_types:
            for k in self.cluster_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ClusterTypes'] = []
        if self.cluster_types is not None:
            for k in self.cluster_types:
                result['ClusterTypes'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_types = []
        if m.get('ClusterTypes') is not None:
            for k in m.get('ClusterTypes'):
                temp_model = ListUserClusterTypesResponseBodyClusterTypes()
                self.cluster_types.append(temp_model.from_map(k))
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListUserClusterTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserClusterTypesResponseBody = None,
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
            temp_model = ListUserClusterTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        nodes: List[str] = None,
    ):
        # Cluster ID
        self.cluster_id = cluster_id
        # Whether to allow skipping failed node tasks, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # List of nodes
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
        # Cluster ID
        self.cluster_id = cluster_id
        # Whether to allow skipping failed node tasks, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # List of nodes
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
        # Request ID
        self.request_id = request_id
        # Task Id
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
        # Hostname
        self.hostname = hostname
        # System image ID
        self.image_id = image_id
        # Login password
        self.login_password = login_password
        # Node ID
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
        # Cluster ID
        self.cluster_id = cluster_id
        # Whether to allow skipping failed node tasks, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # Node list
        self.nodes = nodes
        # Custom data
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
        # Cluster ID
        self.cluster_id = cluster_id
        # Whether to allow skipping failed node tasks, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # Node list
        self.nodes_shrink = nodes_shrink
        # Custom data
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
        # Request ID
        self.request_id = request_id
        # Task ID
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
        command_id: str = None,
        content_encoding: str = None,
        description: str = None,
        enable_parameter: bool = None,
        frequency: str = None,
        launcher: str = None,
        name: str = None,
        node_id_list: List[str] = None,
        parameters: Dict[str, Any] = None,
        repeat_mode: str = None,
        termination_mode: str = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        # Ensures idempotence of the request. Generate a unique parameter value from your client to ensure that the value is unique across different requests. 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters. For more information, see How to Ensure Idempotence.
        self.client_token = client_token
        # Command content. Please note the following:
        # 
        # - Specify `EnableParameter=true` to enable custom parameters in the command content.
        # - Define custom parameters using the {{}} format; spaces and newlines within `{{}}` will be ignored.
        # - The number of custom parameters cannot exceed 20.
        # - Custom parameter names can only contain a-zA-Z0-9-_, and are case-insensitive.
        # - A single custom parameter name cannot exceed 64 bytes.
        self.command_content = command_content
        # Command ID
        self.command_id = command_id
        # Encoding method for the script content. Valid values:
        # 
        # - PlainText: No encoding, transmitted in plain text.
        # - Base64: Base64 encoding.
        # 
        # Default value: PlainText. If an invalid value is provided, it will be treated as PlainText.
        self.content_encoding = content_encoding
        # Command description.
        self.description = description
        # Whether the command contains custom parameters.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # Execution time for scheduled commands. Currently, three types of scheduling methods are supported: fixed interval (based on Rate expression), one-time execution at a specific time, and clock-based scheduling (based on Cron expression).
        # 
        # Fixed interval execution: Based on the Rate expression, the command is executed at the set interval. The interval can be set in seconds (s), minutes (m), hours (h), and days (d), suitable for scenarios where tasks need to be executed at fixed intervals. The format is rate(<interval value><interval unit>), such as rate(5m) for every 5 minutes. The following restrictions apply to fixed interval execution:
        # - The interval should not exceed 7 days and should be no less than 60 seconds, and it must be greater than the timeout of the scheduled task.
        # - The interval is based on a fixed frequency and is independent of the actual execution time of the task. For example, if the command is set to execute every 5 minutes and the task takes 2 minutes to complete, the next round will start 3 minutes after the completion of the task.
        # - The task will not be executed immediately upon creation. For example, if the command is set to execute every 5 minutes, it will not be executed immediately upon creation but will start 5 minutes after the task is created.
        # One-time execution at a specific time: Executes the command once at the specified time and timezone. The format is at(yyyy-MM-dd HH:mm:ss <timezone>), which is at(year-month-day hour:minute:second <timezone>). If no timezone is specified, UTC is used by default. Timezones support the following three formats:
        # - Full timezone name: e.g., Asia/Shanghai (China/Shanghai time), America/Los_Angeles (America/Los Angeles time), etc.
        # - Timezone offset from GMT: e.g., GMT+8:00 (UTC+8:00), GMT-7:00 (UTC-7:00). When using the GMT format, leading zeros are not allowed in the hour position.
        # - Timezone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        # 
        # For example, to execute once at 13:15:30 on June 6, 2022, in Shanghai, China, the format would be: at(2022-06-06 13:15:30 Asia/Shanghai); to execute once at 13:15:30 on June 6, 2022, in the GMT-7:00 timezone, the format would be: at(2022-06-06 13:15:30 GMT-7:00).
        # 
        # Clock-based scheduling (based on Cron expression): Based on the Cron expression, the command is executed according to the set schedule. The format is <second> <minute> <hour> <day> <month> <weekday> <year (optional)> <timezone>, i.e., <Cron expression> <timezone>. In the specified timezone, the scheduled task execution time is calculated based on the Cron expression and then executed. If no timezone is specified, the system\\"s internal timezone of the instance running the scheduled task is used by default. For more information about Cron expressions, see Cron Expressions. Timezones support the following three formats:
        # - Full timezone name: e.g., Asia/Shanghai (China/Shanghai time), America/Los_Angeles (America/Los Angeles time), etc.
        # - Timezone offset from GMT: e.g., GMT+8:00 (UTC+8:00), GMT-7:00 (UTC-7:00). When using the GMT format, leading zeros are not allowed in the hour position.
        # - Timezone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        # 
        # For example, to execute the command at 10:15 AM every day in 2022 in Shanghai, China, the format would be 0 15 10 ? * * 2022 Asia/Shanghai; to execute the command every 30 minutes between 10:00 AM and 11:30 AM every day in 2022 in the GMT+8:00 timezone, the format would be 0 0/30 10-11 * * ? 2022 GMT+8:00; to execute the command every 5 minutes between 2:00 PM and 2:55 PM every day in October every two years starting from 2022 in UTC, the format would be 0 0/5 14 * 10 ? 2022/2 UTC.
        self.frequency = frequency
        # Bootstrap for script execution. The length must not exceed 1 KB.
        self.launcher = launcher
        # Command name.
        self.name = name
        # List of nodes.
        self.node_id_list = node_id_list
        # When the command contains custom parameters, you need to pass in key-value pairs of these custom parameters when executing the command. For example, if the command content is `echo {{name}}`, you can pass in the key-value pair `{"name":"Jack"}` through the `Parameter` parameter. The custom parameter will automatically replace the variable value `name`, resulting in a new command, which actually executes as `echo Jack`.
        # 
        # The number of custom parameters ranges from 0 to 10, and you should note:
        # 
        # - Keys cannot be empty strings and support up to 64 characters at most.
        # - Values can be empty strings.
        # - When combined with the original command content and Base64 encoded, if the command is saved, the size after Base64 encoding must not exceed 18 KB; if the command is not saved, the size after Base64 encoding must not exceed 24 KB. You can set whether to keep the command via `KeepCommand`.
        # - The set of custom parameter names must be a subset of the parameter set defined during command creation. For parameters that are not passed in, you can use an empty string as a substitute.
        # 
        # The default value is empty, indicating that the parameter is not set, thus disabling custom parameters.
        self.parameters = parameters
        # Set the command execution mode. Valid values:
        # 
        # - Once: Execute the command immediately.
        # - Period: Execute the command at a scheduled time. When this parameter is set to `Period`, you must also specify the `Frequency` parameter.
        # - NextRebootOnly: Automatically execute the command when the instance starts next time.
        # - EveryReboot: Automatically execute the command every time the instance starts.
        # 
        # Default value:
        # - If the `Frequency` parameter is not specified, the default value is `Once`.
        # - If the `Frequency` parameter is specified, regardless of whether this parameter is already set, it will be processed as `Period`.
        self.repeat_mode = repeat_mode
        # The mode when stopping a task (manually or due to execution timeout). Possible values:
        # Process: Stops the current script process. ProcessTree: Stops the current process tree (a collection of the script process and all its child processes).
        self.termination_mode = termination_mode
        # Timeout for executing the command, in seconds. If the command cannot run due to process issues, missing modules, or the absence of the Cloud Assistant Agent, a timeout will occur. After a timeout, the command process will be forcibly terminated. Default value: 60.
        self.timeout = timeout
        # The username to execute the command in the instance. The length must not exceed 255 characters.
        #     For Linux systems, the command is executed by the root user by default.
        self.username = username
        # You can customize the execution path of the command. The default paths are as follows:
        # 
        # - Linux instances: The default execution path is under the /home directory of the root user.
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
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.launcher is not None:
            result['Launcher'] = self.launcher
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id_list is not None:
            result['NodeIdList'] = self.node_id_list
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode
        if self.termination_mode is not None:
            result['TerminationMode'] = self.termination_mode
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
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeIdList') is not None:
            self.node_id_list = m.get('NodeIdList')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')
        if m.get('TerminationMode') is not None:
            self.termination_mode = m.get('TerminationMode')
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
        command_id: str = None,
        content_encoding: str = None,
        description: str = None,
        enable_parameter: bool = None,
        frequency: str = None,
        launcher: str = None,
        name: str = None,
        node_id_list_shrink: str = None,
        parameters_shrink: str = None,
        repeat_mode: str = None,
        termination_mode: str = None,
        timeout: int = None,
        username: str = None,
        working_dir: str = None,
    ):
        # Ensures idempotence of the request. Generate a unique parameter value from your client to ensure that the value is unique across different requests. 
        # ClientToken supports only ASCII characters and cannot exceed 64 characters. For more information, see How to Ensure Idempotence.
        self.client_token = client_token
        # Command content. Please note the following:
        # 
        # - Specify `EnableParameter=true` to enable custom parameters in the command content.
        # - Define custom parameters using the {{}} format; spaces and newlines within `{{}}` will be ignored.
        # - The number of custom parameters cannot exceed 20.
        # - Custom parameter names can only contain a-zA-Z0-9-_, and are case-insensitive.
        # - A single custom parameter name cannot exceed 64 bytes.
        self.command_content = command_content
        # Command ID
        self.command_id = command_id
        # Encoding method for the script content. Valid values:
        # 
        # - PlainText: No encoding, transmitted in plain text.
        # - Base64: Base64 encoding.
        # 
        # Default value: PlainText. If an invalid value is provided, it will be treated as PlainText.
        self.content_encoding = content_encoding
        # Command description.
        self.description = description
        # Whether the command contains custom parameters.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # Execution time for scheduled commands. Currently, three types of scheduling methods are supported: fixed interval (based on Rate expression), one-time execution at a specific time, and clock-based scheduling (based on Cron expression).
        # 
        # Fixed interval execution: Based on the Rate expression, the command is executed at the set interval. The interval can be set in seconds (s), minutes (m), hours (h), and days (d), suitable for scenarios where tasks need to be executed at fixed intervals. The format is rate(<interval value><interval unit>), such as rate(5m) for every 5 minutes. The following restrictions apply to fixed interval execution:
        # - The interval should not exceed 7 days and should be no less than 60 seconds, and it must be greater than the timeout of the scheduled task.
        # - The interval is based on a fixed frequency and is independent of the actual execution time of the task. For example, if the command is set to execute every 5 minutes and the task takes 2 minutes to complete, the next round will start 3 minutes after the completion of the task.
        # - The task will not be executed immediately upon creation. For example, if the command is set to execute every 5 minutes, it will not be executed immediately upon creation but will start 5 minutes after the task is created.
        # One-time execution at a specific time: Executes the command once at the specified time and timezone. The format is at(yyyy-MM-dd HH:mm:ss <timezone>), which is at(year-month-day hour:minute:second <timezone>). If no timezone is specified, UTC is used by default. Timezones support the following three formats:
        # - Full timezone name: e.g., Asia/Shanghai (China/Shanghai time), America/Los_Angeles (America/Los Angeles time), etc.
        # - Timezone offset from GMT: e.g., GMT+8:00 (UTC+8:00), GMT-7:00 (UTC-7:00). When using the GMT format, leading zeros are not allowed in the hour position.
        # - Timezone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        # 
        # For example, to execute once at 13:15:30 on June 6, 2022, in Shanghai, China, the format would be: at(2022-06-06 13:15:30 Asia/Shanghai); to execute once at 13:15:30 on June 6, 2022, in the GMT-7:00 timezone, the format would be: at(2022-06-06 13:15:30 GMT-7:00).
        # 
        # Clock-based scheduling (based on Cron expression): Based on the Cron expression, the command is executed according to the set schedule. The format is <second> <minute> <hour> <day> <month> <weekday> <year (optional)> <timezone>, i.e., <Cron expression> <timezone>. In the specified timezone, the scheduled task execution time is calculated based on the Cron expression and then executed. If no timezone is specified, the system\\"s internal timezone of the instance running the scheduled task is used by default. For more information about Cron expressions, see Cron Expressions. Timezones support the following three formats:
        # - Full timezone name: e.g., Asia/Shanghai (China/Shanghai time), America/Los_Angeles (America/Los Angeles time), etc.
        # - Timezone offset from GMT: e.g., GMT+8:00 (UTC+8:00), GMT-7:00 (UTC-7:00). When using the GMT format, leading zeros are not allowed in the hour position.
        # - Timezone abbreviation: Only UTC (Coordinated Universal Time) is supported.
        # 
        # For example, to execute the command at 10:15 AM every day in 2022 in Shanghai, China, the format would be 0 15 10 ? * * 2022 Asia/Shanghai; to execute the command every 30 minutes between 10:00 AM and 11:30 AM every day in 2022 in the GMT+8:00 timezone, the format would be 0 0/30 10-11 * * ? 2022 GMT+8:00; to execute the command every 5 minutes between 2:00 PM and 2:55 PM every day in October every two years starting from 2022 in UTC, the format would be 0 0/5 14 * 10 ? 2022/2 UTC.
        self.frequency = frequency
        # Bootstrap for script execution. The length must not exceed 1 KB.
        self.launcher = launcher
        # Command name.
        self.name = name
        # List of nodes.
        self.node_id_list_shrink = node_id_list_shrink
        # When the command contains custom parameters, you need to pass in key-value pairs of these custom parameters when executing the command. For example, if the command content is `echo {{name}}`, you can pass in the key-value pair `{"name":"Jack"}` through the `Parameter` parameter. The custom parameter will automatically replace the variable value `name`, resulting in a new command, which actually executes as `echo Jack`.
        # 
        # The number of custom parameters ranges from 0 to 10, and you should note:
        # 
        # - Keys cannot be empty strings and support up to 64 characters at most.
        # - Values can be empty strings.
        # - When combined with the original command content and Base64 encoded, if the command is saved, the size after Base64 encoding must not exceed 18 KB; if the command is not saved, the size after Base64 encoding must not exceed 24 KB. You can set whether to keep the command via `KeepCommand`.
        # - The set of custom parameter names must be a subset of the parameter set defined during command creation. For parameters that are not passed in, you can use an empty string as a substitute.
        # 
        # The default value is empty, indicating that the parameter is not set, thus disabling custom parameters.
        self.parameters_shrink = parameters_shrink
        # Set the command execution mode. Valid values:
        # 
        # - Once: Execute the command immediately.
        # - Period: Execute the command at a scheduled time. When this parameter is set to `Period`, you must also specify the `Frequency` parameter.
        # - NextRebootOnly: Automatically execute the command when the instance starts next time.
        # - EveryReboot: Automatically execute the command every time the instance starts.
        # 
        # Default value:
        # - If the `Frequency` parameter is not specified, the default value is `Once`.
        # - If the `Frequency` parameter is specified, regardless of whether this parameter is already set, it will be processed as `Period`.
        self.repeat_mode = repeat_mode
        # The mode when stopping a task (manually or due to execution timeout). Possible values:
        # Process: Stops the current script process. ProcessTree: Stops the current process tree (a collection of the script process and all its child processes).
        self.termination_mode = termination_mode
        # Timeout for executing the command, in seconds. If the command cannot run due to process issues, missing modules, or the absence of the Cloud Assistant Agent, a timeout will occur. After a timeout, the command process will be forcibly terminated. Default value: 60.
        self.timeout = timeout
        # The username to execute the command in the instance. The length must not exceed 255 characters.
        #     For Linux systems, the command is executed by the root user by default.
        self.username = username
        # You can customize the execution path of the command. The default paths are as follows:
        # 
        # - Linux instances: The default execution path is under the /home directory of the root user.
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
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding
        if self.description is not None:
            result['Description'] = self.description
        if self.enable_parameter is not None:
            result['EnableParameter'] = self.enable_parameter
        if self.frequency is not None:
            result['Frequency'] = self.frequency
        if self.launcher is not None:
            result['Launcher'] = self.launcher
        if self.name is not None:
            result['Name'] = self.name
        if self.node_id_list_shrink is not None:
            result['NodeIdList'] = self.node_id_list_shrink
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.repeat_mode is not None:
            result['RepeatMode'] = self.repeat_mode
        if self.termination_mode is not None:
            result['TerminationMode'] = self.termination_mode
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
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EnableParameter') is not None:
            self.enable_parameter = m.get('EnableParameter')
        if m.get('Frequency') is not None:
            self.frequency = m.get('Frequency')
        if m.get('Launcher') is not None:
            self.launcher = m.get('Launcher')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('NodeIdList') is not None:
            self.node_id_list_shrink = m.get('NodeIdList')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('RepeatMode') is not None:
            self.repeat_mode = m.get('RepeatMode')
        if m.get('TerminationMode') is not None:
            self.termination_mode = m.get('TerminationMode')
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
        # ID of the command execution.
        self.invoke_id = invoke_id
        # ID of the request
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
        # The content of the file. After Base64 encoding, the size cannot exceed 32 KB.
        # 
        # - When the `ContentType` parameter is `PlainText`, this field is plain text.
        # - When the `ContentType` parameter is `Base64`, this field is Base64 encoded text.
        # 
        # This parameter is required.
        self.content = content
        # The content type of the file.
        # 
        # PlainText: Plain text.
        # Base64: Base64 encoded.
        # The default value is PlainText.
        self.content_type = content_type
        # Description information. Supports all character sets, and the length must not exceed 512 characters.
        self.description = description
        # The group of the file. Applies only to Linux instances, and the default is root. The length must not exceed 64 characters.
        # 
        # Note
        # When using other groups, ensure that the group exists in the instance.
        self.file_group = file_group
        # The permissions of the file. Applies only to Linux instances, and the setting method is the same as the chmod command.
        # 
        # The default value is 0644, which means the user has read and write permissions, while the group and other users have read-only permissions.
        self.file_mode = file_mode
        # The owner of the file. Applies only to Linux instances, and the default is root.
        self.file_owner = file_owner
        # The name of the file. Supports all character sets, and the length must not exceed 255 characters.
        # 
        # This parameter is required.
        self.name = name
        # List of nodes.
        # 
        # This parameter is required.
        self.node_id_list = node_id_list
        # Whether to overwrite the file if a file with the same name already exists in the target directory.
        # - true: Overwrite.
        # - false: Do not overwrite.
        # 
        # The default value is false.
        self.overwrite = overwrite
        # The directory in the target Lingjun node where the file will be sent. If it does not exist, it will be automatically created.
        # 
        # This parameter is required.
        self.target_dir = target_dir
        # The timeout for sending the file. Unit: seconds.
        # 
        # - A timeout may occur due to process reasons, missing modules, or missing Cloud Assistant Agent.
        # - If the set timeout is less than 10 seconds, to ensure successful delivery, the system will automatically set the timeout to 10 seconds.
        # 
        # The default value is 60.
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
        # The content of the file. After Base64 encoding, the size cannot exceed 32 KB.
        # 
        # - When the `ContentType` parameter is `PlainText`, this field is plain text.
        # - When the `ContentType` parameter is `Base64`, this field is Base64 encoded text.
        # 
        # This parameter is required.
        self.content = content
        # The content type of the file.
        # 
        # PlainText: Plain text.
        # Base64: Base64 encoded.
        # The default value is PlainText.
        self.content_type = content_type
        # Description information. Supports all character sets, and the length must not exceed 512 characters.
        self.description = description
        # The group of the file. Applies only to Linux instances, and the default is root. The length must not exceed 64 characters.
        # 
        # Note
        # When using other groups, ensure that the group exists in the instance.
        self.file_group = file_group
        # The permissions of the file. Applies only to Linux instances, and the setting method is the same as the chmod command.
        # 
        # The default value is 0644, which means the user has read and write permissions, while the group and other users have read-only permissions.
        self.file_mode = file_mode
        # The owner of the file. Applies only to Linux instances, and the default is root.
        self.file_owner = file_owner
        # The name of the file. Supports all character sets, and the length must not exceed 255 characters.
        # 
        # This parameter is required.
        self.name = name
        # List of nodes.
        # 
        # This parameter is required.
        self.node_id_list_shrink = node_id_list_shrink
        # Whether to overwrite the file if a file with the same name already exists in the target directory.
        # - true: Overwrite.
        # - false: Do not overwrite.
        # 
        # The default value is false.
        self.overwrite = overwrite
        # The directory in the target Lingjun node where the file will be sent. If it does not exist, it will be automatically created.
        # 
        # This parameter is required.
        self.target_dir = target_dir
        # The timeout for sending the file. Unit: seconds.
        # 
        # - A timeout may occur due to process reasons, missing modules, or missing Cloud Assistant Agent.
        # - If the set timeout is less than 10 seconds, to ensure successful delivery, the system will automatically set the timeout to 10 seconds.
        # 
        # The default value is 60.
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
        # Command execution ID.
        self.invoke_id = invoke_id
        # ID of the request
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
        # Node ID
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
        # Node group ID
        self.node_group_id = node_group_id
        # List of nodes
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
        # Cluster ID
        self.cluster_id = cluster_id
        # Whether to allow skipping failed node tasks, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # Node group information
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
        # Cluster ID
        self.cluster_id = cluster_id
        # Whether to allow skipping failed node tasks, default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # Node group information
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
        # Request ID
        self.request_id = request_id
        # task id
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
        # Command execution ID.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # List of nodes.
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
        # Command execution ID.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # List of nodes.
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


class StopNodesRequest(TeaModel):
    def __init__(
        self,
        ignore_failed_node_tasks: bool = None,
        nodes: List[str] = None,
    ):
        # Whether to allow skipping failed node tasks, default value is False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # List of nodes.
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.nodes is not None:
            result['Nodes'] = self.nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Nodes') is not None:
            self.nodes = m.get('Nodes')
        return self


class StopNodesShrinkRequest(TeaModel):
    def __init__(
        self,
        ignore_failed_node_tasks: bool = None,
        nodes_shrink: str = None,
    ):
        # Whether to allow skipping failed node tasks, default value is False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # List of nodes.
        self.nodes_shrink = nodes_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ignore_failed_node_tasks is not None:
            result['IgnoreFailedNodeTasks'] = self.ignore_failed_node_tasks
        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreFailedNodeTasks') is not None:
            self.ignore_failed_node_tasks = m.get('IgnoreFailedNodeTasks')
        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')
        return self


class StopNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # Request ID
        self.request_id = request_id
        # Task ID
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


class StopNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopNodesResponseBody = None,
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
            temp_model = StopNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key
        self.key = key
        # Tag value
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
        # Region ID
        # 
        # This parameter is required.
        self.region_id = region_id
        # List of resource IDs
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # Resource type
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # Tags
        # 
        # This parameter is required.
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
        # ID of the request
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
        # Whether to remove all, only effective when TagKey.N is empty. Valid values:
        # 
        # - True, remove all
        # - False, do not remove all
        # 
        # Default is False
        self.all = all
        # Region ID
        # 
        # This parameter is required.
        self.region_id = region_id
        # List of resource IDs
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # Resource type
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # List of tag keys
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
        # request id
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


class UpdateNodeGroupRequest(TeaModel):
    def __init__(
        self,
        new_node_group_name: str = None,
        node_group_id: str = None,
        user_data: str = None,
    ):
        self.new_node_group_name = new_node_group_name
        self.node_group_id = node_group_id
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.new_node_group_name is not None:
            result['NewNodeGroupName'] = self.new_node_group_name
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewNodeGroupName') is not None:
            self.new_node_group_name = m.get('NewNodeGroupName')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        return self


class UpdateNodeGroupResponseBody(TeaModel):
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


class UpdateNodeGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateNodeGroupResponseBody = None,
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
            temp_model = UpdateNodeGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


