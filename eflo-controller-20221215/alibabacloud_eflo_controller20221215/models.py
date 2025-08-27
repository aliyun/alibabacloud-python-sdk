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
        # The node ID.
        self.node_id = node_id
        # The O\\&M operation type
        # 
        # Valid value:
        # 
        # *   RepairMachine
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
        # The error message.
        self.error_message = error_message
        # The request ID.
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
        # The ID of the resource group into which you want to change.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The resource ID.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The region ID.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # The resource type.
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
        # The request ID.
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
        # The session ID.
        self.session_id = session_id
        # Session token.
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
        # The request ID.
        self.request_id = request_id
        # The session ID.
        self.session_id = session_id
        # status of session
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
        # IP source subnet for the cluster
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
        # Default bond subnet for the cluster
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
        # IP source subnet for the cluster
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
        # IP source subnet for the cluster
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


class CreateClusterRequestNodeGroupsNodesDataDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        delete_with_node: bool = None,
        performance_level: str = None,
        size: int = None,
    ):
        # Type
        self.category = category
        # Whether the data disk is deleted with the node when it is unsubscribed
        self.delete_with_node = delete_with_node
        # Data disk performance level
        self.performance_level = performance_level
        # Disk size
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_node is not None:
            result['DeleteWithNode'] = self.delete_with_node
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithNode') is not None:
            self.delete_with_node = m.get('DeleteWithNode')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class CreateClusterRequestNodeGroupsNodes(TeaModel):
    def __init__(
        self,
        data_disk: List[CreateClusterRequestNodeGroupsNodesDataDisk] = None,
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
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
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
            for k in m.get('DataDisk'):
                temp_model = CreateClusterRequestNodeGroupsNodesDataDisk()
                self.data_disk.append(temp_model.from_map(k))
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


class CreateClusterRequestNodeGroupsSystemDisk(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterRequestNodeGroups(TeaModel):
    def __init__(
        self,
        file_system_mount_enabled: bool = None,
        image_id: str = None,
        key_pair_name: str = None,
        login_password: str = None,
        machine_type: str = None,
        node_group_description: str = None,
        node_group_name: str = None,
        nodes: List[CreateClusterRequestNodeGroupsNodes] = None,
        system_disk: CreateClusterRequestNodeGroupsSystemDisk = None,
        user_data: str = None,
        virtual_gpu_enabled: bool = None,
        zone_id: str = None,
    ):
        # Whether to support file system mounting
        self.file_system_mount_enabled = file_system_mount_enabled
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
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled
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
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
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
            for k in m.get('Nodes'):
                temp_model = CreateClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('SystemDisk') is not None:
            temp_model = CreateClusterRequestNodeGroupsSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VirtualGpuEnabled') is not None:
            self.virtual_gpu_enabled = m.get('VirtualGpuEnabled')
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
        # Whether to allow skipping failed nodes, the default value is False
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # Network information
        self.networks_shrink = networks_shrink
        # Node VSwitches
        self.nimiz_vswitches_shrink = nimiz_vswitches_shrink
        # Node group list
        self.node_groups_shrink = node_groups_shrink
        # Whether the network interface supports jumbo frames
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
        # Task ID
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
        # The sending date in the yyyymmdd format.
        self.datetime = datetime
        # The log content.
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
        # The instance ID.
        self.ai_instance = ai_instance
        # The logs.
        self.logs = logs
        # The node ID.
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
        # The task logs.
        self.ai_job_logs = ai_job_logs
        # The end time. The value is in the timestamp format. Unit: seconds.
        # 
        # >  This timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time
        # The start time. The value is in the timestamp format. Unit: seconds.
        # 
        # >  This timestamp must indicate a point in time that is accurate to the minute.
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
        # The log information.
        self.ai_job_log_info = ai_job_log_info
        # The cluster ID.
        self.cluster_id = cluster_id
        # The diagnostics type.
        self.diagnostic_type = diagnostic_type
        # The IDs of the nodes.
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
        # The log information.
        self.ai_job_log_info_shrink = ai_job_log_info_shrink
        # The cluster ID.
        self.cluster_id = cluster_id
        # The diagnostics type.
        self.diagnostic_type = diagnostic_type
        # The IDs of the nodes.
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
        # The ID of the diagnostics task.
        self.diagnostic_id = diagnostic_id
        # The request ID.
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
        # The IP address.
        self.ip = ip
        # The node ID.
        self.node_id = node_id
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
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
        # The number of GPUs.
        self.gpunum = gpunum
        # The host IDs.
        self.hosts = hosts
        # The communication library model.
        self.model = model
        # The CommTest type, which can be ACCL or NCCL.
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
        # The bonding of network interface card.
        self.bond = bond
        # The IP address of the node.
        self.ip = ip
        # The node ID.
        self.node_id = node_id
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
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
        # The hosts of the test node.
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
        # The bonding of network interface card.
        self.bond = bond
        # The IP address of the node.
        self.ip = ip
        # The node ID.
        self.node_id = node_id
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
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
        # The bonding of network interface card.
        self.bond = bond
        # The IP address of the node.
        self.ip = ip
        # The node ID.
        self.node_id = node_id
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
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
        # The client IDs.
        self.clients = clients
        # The running duration of the pipeline job. Unit: seconds.
        self.duration = duration
        # If the protocol is RDMA, enter True or False. If the protocol is TCP, leave this field empty.
        self.gdr = gdr
        # The network protocol, which can be RDMA or TCP.
        self.protocol = protocol
        # If the protocol is TCP, enter the number of concurrent connections. If the protocol is RDMA, enter the configured QP value.
        self.qp = qp
        # The services.
        self.servers = servers
        # The traffic model, which can be MTON or Fullmesh.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # Specify when NetTestType is CommTest.
        self.comm_test = comm_test
        # Specify when NetTestType is DelayTest.
        self.delay_test = delay_test
        # The type of the network test. Valid values: DelayTest, TrafficTest, and CommTest.
        self.net_test_type = net_test_type
        # The network mode.
        self.network_mode = network_mode
        # The port number.
        self.port = port
        # If the TrafficModel is Fullmesh, leave this parameter empty.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # Specify when NetTestType is CommTest.
        self.comm_test_shrink = comm_test_shrink
        # Specify when NetTestType is DelayTest.
        self.delay_test_shrink = delay_test_shrink
        # The type of the network test. Valid values: DelayTest, TrafficTest, and CommTest.
        self.net_test_type = net_test_type
        # The network mode.
        self.network_mode = network_mode
        # The port number.
        self.port = port
        # If the TrafficModel is Fullmesh, leave this parameter empty.
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
        # Id of the request
        self.request_id = request_id
        # The ID of the test task. The unique identifier of a network test task.
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


class CreateNodeGroupRequestNodeGroupSystemDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        # Disk type. Value range:
        # 
        #  - cloud_essd: ESSD cloud disk.
        self.category = category
        # When creating an ESSD cloud disk as a system disk, set the performance level of the cloud disk. Value range:
        # - PL0: Maximum random read/write IOPS per disk 10,000.
        # - PL1: Maximum random read/write IOPS per disk 50,000.
        self.performance_level = performance_level
        # Unit: GB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateNodeGroupRequestNodeGroup(TeaModel):
    def __init__(
        self,
        az: str = None,
        file_system_mount_enabled: bool = None,
        image_id: str = None,
        key_pair_name: str = None,
        login_password: str = None,
        machine_type: str = None,
        node_group_description: str = None,
        node_group_name: str = None,
        system_disk: CreateNodeGroupRequestNodeGroupSystemDisk = None,
        user_data: str = None,
        virtual_gpu_enabled: bool = None,
    ):
        # Availability Zone
        # 
        # This parameter is required.
        self.az = az
        # Whether file storage mounting is supported
        self.file_system_mount_enabled = file_system_mount_enabled
        # Image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # Key pair name.
        self.key_pair_name = key_pair_name
        # Password
        self.login_password = login_password
        # Machine type
        # 
        # This parameter is required.
        self.machine_type = machine_type
        # Node group description
        self.node_group_description = node_group_description
        # Node group name
        # 
        # This parameter is required.
        self.node_group_name = node_group_name
        # Details of the node system disk configuration.
        self.system_disk = system_disk
        # User-defined data
        self.user_data = user_data
        # Whether to enable gpu virtualization or not
        self.virtual_gpu_enabled = virtual_gpu_enabled

    def validate(self):
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.az is not None:
            result['Az'] = self.az
        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled
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
        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()
        if self.user_data is not None:
            result['UserData'] = self.user_data
        if self.virtual_gpu_enabled is not None:
            result['VirtualGpuEnabled'] = self.virtual_gpu_enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Az') is not None:
            self.az = m.get('Az')
        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')
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
        if m.get('SystemDisk') is not None:
            temp_model = CreateNodeGroupRequestNodeGroupSystemDisk()
            self.system_disk = temp_model.from_map(m['SystemDisk'])
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VirtualGpuEnabled') is not None:
            self.virtual_gpu_enabled = m.get('VirtualGpuEnabled')
        return self


class CreateNodeGroupRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        node_group: CreateNodeGroupRequestNodeGroup = None,
        node_unit: Dict[str, Any] = None,
    ):
        # Cluster ID
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Node ID.
        # 
        # This parameter is required.
        self.node_group = node_group
        # Node information
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
        # Cluster ID
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Node ID.
        # 
        # This parameter is required.
        self.node_group_shrink = node_group_shrink
        # Node information
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
        # Node group ID
        self.node_group_id = node_group_id
        # NodeGroupName
        self.node_group_name = node_group_name
        # ID of the request
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
        # The instance ID.
        self.node_id = node_id
        # The type of the session corresponding to the session package.
        self.session_type = session_type
        # The start time. The value is a 13-digit timestamp.
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
        # The request ID.
        self.request_id = request_id
        # The node ID.
        self.server_sn = server_sn
        # The session ID.
        self.session_id = session_id
        # The session credential.
        self.session_token = session_token
        # The WebSocket address.
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


class CreateVscRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The resource tag key.
        self.key = key
        # The resource tag value.
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


class CreateVscRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        node_id: str = None,
        resource_group_id: str = None,
        tag: List[CreateVscRequestTag] = None,
        vsc_name: str = None,
        vsc_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The node ID.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource tags.
        self.tag = tag
        # The custom name of the VSC, which is unique on a compute node.
        self.vsc_name = vsc_name
        # The VSC type. Valid values: primary and standard. Default value: primary.
        self.vsc_type = vsc_type

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name
        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = CreateVscRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')
        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')
        return self


class CreateVscResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        vsc_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The VSC ID.
        self.vsc_id = vsc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')
        return self


class CreateVscResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateVscResponseBody = None,
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
            temp_model = CreateVscResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The cluster ID.
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
        # The request ID.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The node group ID.
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


class DeleteVscRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        vsc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The ID of the VSC that you want to delete.
        # 
        # This parameter is required.
        self.vsc_id = vsc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['ClientToken'] = self.client_token
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')
        return self


class DeleteVscResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class DeleteVscResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteVscResponseBody = None,
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
            temp_model = DeleteVscResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        # The cluster ID.
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
        # The component ID.
        self.component_id = component_id
        # The component type.
        # 
        # Valid values:
        # 
        # *   ARMS
        # *   ACKEdge
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
        # The ID of the CIDR block for the cluster.
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
        networks: DescribeClusterResponseBodyNetworks = None,
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
        # The cluster description.
        self.cluster_description = cluster_description
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The cluster type.
        self.cluster_type = cluster_type
        # The component information.
        self.components = components
        # The IP type of the computing network.
        self.computing_ip_version = computing_ip_version
        # The creation time.
        self.create_time = create_time
        # The cluster number.
        self.hpn_zone = hpn_zone
        # The network information.
        self.networks = networks
        # The number of nodes.
        self.node_count = node_count
        # The number of node groups.
        self.node_group_count = node_group_count
        # The status of Jumbo Frames for the elastic network interface (ENI).
        self.open_eni_jumbo_frame = open_eni_jumbo_frame
        # The cluster status.
        self.operating_state = operating_state
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The job ID.
        self.task_id = task_id
        # The update time.
        self.update_time = update_time
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()
        if self.networks:
            self.networks.validate()

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
        if self.networks is not None:
            result['Networks'] = self.networks.to_map()
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
        if m.get('Networks') is not None:
            temp_model = DescribeClusterResponseBodyNetworks()
            self.networks = temp_model.from_map(m['Networks'])
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
        # The diagnostic task ID.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The creation time.
        self.created_time = created_time
        # The diagnostic task ID.
        self.diagnostic_id = diagnostic_id
        # The diagnostic information.
        self.diagnostic_results = diagnostic_results
        # The diagnostic status.
        self.diagnostic_state = diagnostic_state
        # The type of the diagnostic task.
        self.diagnostic_type = diagnostic_type
        # The end time of the instance exception. The time format with time zone based on the ISO8601 standard. The format is yyyy-MM-ddTHH:mm:ss +0800.
        self.end_time = end_time
        # The node IDs.
        self.node_ids = node_ids
        # The request ID.
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
        # The encoding mode of the `CommandContent` and `Output` response parameters. Valid values:
        # 
        # *   PlainText: returns the original command content and command outputs.
        # *   Base64 (default): returns the Base64-encoded command content and command output.
        self.content_encoding = content_encoding
        # Specifies whether to return the command outputs in the response.
        # 
        # *   true: returns the command outputs. When this parameter is set to true, you must specify `InvokeId`, `InstanceId`, or both.
        # *   false (default)
        self.include_output = include_output
        # The execution ID.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # The instance ID.
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
        # The start time of the execution.
        self.creation_time = creation_time
        # The size of the Output text that was truncated and discarded because the Output value exceeded 24 KB in size.
        self.dropped = dropped
        # The error code returned when the file failed to be sent to the instance. Valid values:
        # 
        # *   Null: The file is sent to the instance.
        # *   NodeNotExists: The specified instance does not exist or has been released.
        # *   NodeReleased: The instance was released while the file was being sent.
        # *   NodeNotRunning: The instance was not running while the file sending task was being created.
        # *   AccountNotExists: The specified account does not exist.
        # *   ClientNotRunning: Cloud Assistant Agent is not running.
        # *   ClientNotResponse: Cloud Assistant Agent does not respond.
        # *   ClientIsUpgrading: Cloud Assistant Agent is being upgraded.
        # *   ClientNeedUpgrade: Cloud Assistant Agent needs to be upgraded.
        # *   DeliveryTimeout: The file sending task timed out.
        # *   FileCreateFail: The file failed to be created.
        # *   FileAlreadyExists: A file with the same name exists in the specified directory.
        # *   FileContentInvalid: The file content is invalid.
        # *   FileNameInvalid: The file name is invalid.
        # *   FilePathInvalid: The specified directory is invalid.
        # *   FileAuthorityInvalid: The specified permissions on the file are invalid.
        # *   UserGroupNotExists: The specified user group does not exist.
        self.error_code = error_code
        # The error message returned when the command cannot be sent or run.
        # 
        # *   If this parameter is empty, the command was run as expected.
        # *   the specified node does not exists: The specified instance does not exist or is released.
        # *   the node has node when create task: The instance is released when the command is being run.
        # *   the node is not running when create task: The instance is not in the Running state while the command is being run.
        # *   the command is not applicable: The command is not applicable to the specified instance.
        # *   the specified account does not exists: The specified account does not exist.
        # *   the specified directory does not exists: The specified directory does not exist.
        # *   the cron job expression is invalid: The cron expression that specifies the execution time is invalid.
        # *   the aliyun service is not running on the instance: Cloud Assistant Agent is not running.
        # *   the aliyun service in the instance does not response: Cloud Assistant Agent does not respond.
        # *   the aliyun service in the node is upgrading now: Cloud Assistant Agent is being upgraded.
        # *   the aliyun service in the node need upgrade: Cloud Assistant Agent needs to be upgraded.
        # *   the command delivery has been timeout: The request to send the command timed out.
        # *   the command execution has been timeout: The command execution timed out.
        # *   the command execution got an exception: An exception occurred when the command is being run.
        # *   the command execution has been interrupted: The command execution is interrupted.
        # *   the command execution exit code is not zero: The command execution completes, but the exit code is not 0.
        # *   the specified node has been released: The instance is released while the file is being sent.
        self.error_info = error_info
        # The exit code of the execution. Valid values:
        # 
        # *   For Linux instances, the value is the exit code of the shell process.
        # *   For Windows instances, the value is the exit code of the batch or PowerShell process.
        self.exit_code = exit_code
        # The end time of the execution.
        self.finish_time = finish_time
        # The execution status of the command on a single instance. Valid values:
        # 
        # *   Pending: The command was being verified or sent.
        # 
        # *   Invalid: The specified command type or parameter is invalid.
        # 
        # *   Aborted: The command failed to be sent to the instance. To send a command to an instance, make sure that the instance is in the Running state and the command can be sent to the instance within 1 minute.
        # 
        # *   Running: The command is being run on the instance.
        # 
        # *   Success:
        # 
        #     *   One-time task: The execution was complete, and the exit code was 0.
        #     *   Recurring execution: The previous occurrence of the execution is complete, and the exit code is 0. The specified recurring period during which the command is run ends.
        # 
        # *   Failed:
        # 
        #     *   One-time task: The execution was complete, but the exit code was not 0.
        #     *   Recurring execution: The previous occurrence of the execution is complete, but the exit code is not 0. The specified recurring period during which the command is run is about to end.
        # 
        # *   Error: The execution cannot proceed due to an exception.
        # 
        # *   Timeout: The execution timed out.
        # 
        # *   Cancelled: The execution was canceled before it started.
        # 
        # *   Stopping: The command task is being stopped.
        # 
        # *   Terminated: The execution was terminated before completion.
        # 
        # *   Scheduled:
        # 
        #     *   One-time task: The execution state can never be Scheduled.
        #     *   Recurring execution: The command is waiting to be run.
        self.invocation_status = invocation_status
        # The node ID.
        self.node_id = node_id
        # The execution status of the command on a single instance.
        self.node_invoke_status = node_invoke_status
        # The command output.
        # 
        # *   If ContentEncoding is set to PlainText in the request, the original command output is returned.
        # *   If ContentEncoding is set to Base64 in the request, the Base64-encoded command output is returned.
        self.output = output
        # The number of times that the command was run on the instance.
        # 
        # *   If the command is set to run only once, the value is 0 or 1.
        # *   If the command is set to run on a schedule, the value is the number of times that the command has been run on the instance.
        self.repeats = repeats
        # The start time.
        self.start_time = start_time
        # The time when the command task was stopped. If you call the StopInvocation operation to stop the command task, the value of this parameter is the time when the operation is called.
        self.stop_time = stop_time
        # Indicates whether the command is to be automatically run. Valid values:
        # 
        # *   true: The command is run by calling the `RunCommand` or `InvokeCommand` operation with `RepeatMode` set to `Period`, `NextRebootOnly`, or `EveryReboot`.
        # 
        # *   false (default): The command meets the following requirements.
        # 
        #     *   The command is run by calling the `RunCommand` or `InvokeCommand` operation with `RepeatMode` set to `Once`.
        #     *   The command task is canceled, stopped, or completed.
        self.timed = timed
        # The update time of the execution.
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
        # The command execution records of the node.
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
        # The executed command.
        # 
        # *   If ContentEncoding is set to PlainText in the request, the original command content is returned.
        # *   If ContentEncoding is set to Base64 in the request, the Base64-encoded command content is returned.
        self.command_content = command_content
        # The command description.
        self.command_description = command_description
        # The command name.
        self.command_name = command_name
        # The time when the command task was created.
        self.creation_time = creation_time
        # The schedule on which the command was run.
        self.frequency = frequency
        # The overall execution state of the command task. The value of this parameter depends on the execution states of the command task on all the involved instances. Valid values:
        # 
        # *   Pending: The command was being verified or sent. If the execution state on at least one instance is Pending, the overall execution state is Pending.
        # 
        # *   Scheduled: The command that is set to run on a schedule is sent and waiting to be run. If the execution state on at least one instance is Scheduled, the overall execution state is Scheduled.
        # 
        # *   Running: The command is being run on the instance. When the execution state on at least one instance is Running, the overall execution state is Running.
        # 
        # *   Success: When the execution state on at least one instance is Success and the execution state on the other instances is Stopped or Success, the overall execution state is Success.
        # 
        #     *   One-time task: The execution is complete, and the exit code is 0.
        #     *   Scheduled task: The last execution was complete, the exit code was 0, and the specified period ended.
        # 
        # *   Failed: When the execution state on all instances is Stopped or Failed, the overall execution state is Failed. When the execution state on an instance is one of the following values, Failed is returned as the overall execution state:
        # 
        #     *   Invalid: The command is invalid.
        #     *   Aborted: The command failed to be sent.
        #     *   Failed: The execution was complete, but the exit code was not 0.
        #     *   Timeout: The execution timed out.
        #     *   Error: An error occurred while the command was being run.
        # 
        # *   Stopping: The command task is being stopped. When the execution state on at least one instance is Stopping, the overall execution state is Stopping.
        # 
        # *   Stopped: The task was stopped. When the execution state on all instances is Stopped, the overall execution state is Stopped. When the execution state on an instance is one of the following values, Stopped is returned as the overall execution state:
        # 
        #     *   Cancelled: The task was canceled.
        #     *   Terminated: The task was terminated.
        # 
        # *   PartialFailed: The execution was complete on some instances and failed on other instances. When the execution state is Success on some instances and is Failed or Stopped on the other instances, the overall execution state is PartialFailed.
        # 
        # >  The value of the `InvokeStatus` response parameter is similar to the value of InvocationStatus. We recommend that you ignore InvokeStatus and check the value of InvocationStatus.
        self.invocation_status = invocation_status
        # The execution ID.
        self.invoke_id = invoke_id
        # The command execution records.
        self.invoke_nodes = invoke_nodes
        # The overall execution status of the command task. The value of this parameter depends on the execution states of the command task on all involved instances. Valid values:
        # 
        # *   Running:
        # 
        #     *   Scheduled task: Before you stop the scheduled execution of the command, the overall execution state is always Running.
        #     *   One-time task: If the command is being run on instances, the overall execution state is Running.
        # 
        # *   Finished:
        # 
        #     *   Scheduled task: The overall execution state can never be Finished.
        #     *   One-time task: The execution is complete on all instances, or the execution is stopped on some instances and is complete on the other instances.
        # 
        # *   Failed:
        # 
        #     *   Scheduled task: The overall execution state can never be Failed.
        #     *   One-time task: The execution failed on all instances.
        # 
        # *   Stopped: The task is stopped.
        # 
        # *   Stopping: The task is being stopped.
        # 
        # *   PartialFailed: The task fails on some instances. If you specify both this parameter and `InstanceId`, this parameter does not take effect.
        self.invoke_status = invoke_status
        # The custom parameters in the command.
        self.parameters = parameters
        # The execution mode of the command. Valid values:
        # 
        # *   Once: The command is run immediately.
        # *   Period: The command is run on a schedule.
        # *   NextRebootOnly: The command is run the next time the instances start.
        # *   EveryReboot: runs the command every time the instances start.
        self.repeat_mode = repeat_mode
        # The timeout period for the command execution. Unit: seconds.
        self.timeout = timeout
        # The username that is used to run the command.
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
        # The file sending records.
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
        # The command execution record.
        self.invocations = invocations
        # The request ID.
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
        # The ID of the test task. The unique identifier of a network test task.
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
        # The IP address.
        self.ip = ip
        # The resource ID.
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
        # All hosts infomation
        self.hosts = hosts
        # The communication library model.
        self.model = model
        # The CommTest type, which can be ACCL or NCCL.
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
        # The bonding of network interface card.
        self.bond = bond
        # The IP address.
        self.ip = ip
        # The resource ID.
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


class DescribeNetTestResultResponseBodyDelayTest(TeaModel):
    def __init__(
        self,
        hosts: List[DescribeNetTestResultResponseBodyDelayTestHosts] = None,
    ):
        # All hosts infomation
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
        # Network interface bond port
        self.bond = bond
        # IP address.
        self.ip = ip
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
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
        # Network interface bond port
        self.bond = bond
        # The IP address.
        self.ip = ip
        # The resource ID.
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
        # All clients information
        self.clients = clients
        # Call duration, in seconds.
        self.duration = duration
        # When the protocol is RDMA, fill in True/False,
        # when the protocol is TCP, this field is empty.
        self.gdr = gdr
        # Network protocol, either RDMA or TCP.
        self.protocol = protocol
        # When the protocol is TCP, fill in the number of concurrent connections; when the protocol is RDMA, fill in the configured QP value.
        self.qp = qp
        # Servers infomation.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # Specify when NetTestType is CommTest.
        self.comm_test = comm_test
        # create time
        self.creation_time = creation_time
        # Fill in when the network test type is a delay test.
        self.delay_test = delay_test
        # finish time
        self.finished_time = finished_time
        # The type of the network test.
        self.net_test_type = net_test_type
        # Test port number.
        self.port = port
        # The request ID.
        self.request_id = request_id
        # result detail
        self.result_detial = result_detial
        # status of session
        self.status = status
        # The ID of the test task. The unique identifier of a network test task.
        self.test_id = test_id
        # Fill in when the network test type is a traffic test.
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
        # The node ID.
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


class DescribeNodeResponseBodyDisks(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeNodeResponseBodyNetworks(TeaModel):
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
        disks: List[DescribeNodeResponseBodyDisks] = None,
        expired_time: str = None,
        file_system_mount_enabled: bool = None,
        hostname: str = None,
        hpn_zone: str = None,
        image_id: str = None,
        image_name: str = None,
        machine_type: str = None,
        networks: List[DescribeNodeResponseBodyNetworks] = None,
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
            for k in self.disks:
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
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['Disks'] = []
        if self.disks is not None:
            for k in self.disks:
                result['Disks'].append(k.to_map() if k else None)
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled
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
            for k in m.get('Disks'):
                temp_model = DescribeNodeResponseBodyDisks()
                self.disks.append(temp_model.from_map(k))
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')
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


class DescribeNodeTypeRequest(TeaModel):
    def __init__(
        self,
        node_type: str = None,
    ):
        self.node_type = node_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_type is not None:
            result['NodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')
        return self


class DescribeNodeTypeResponseBody(TeaModel):
    def __init__(
        self,
        eni_high_dense_quantity: int = None,
        eni_ipv_6address_quantity: int = None,
        eni_private_ip_address_quantity: int = None,
        eni_quantity: int = None,
        request_id: str = None,
    ):
        self.eni_high_dense_quantity = eni_high_dense_quantity
        self.eni_ipv_6address_quantity = eni_ipv_6address_quantity
        self.eni_private_ip_address_quantity = eni_private_ip_address_quantity
        self.eni_quantity = eni_quantity
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eni_high_dense_quantity is not None:
            result['EniHighDenseQuantity'] = self.eni_high_dense_quantity
        if self.eni_ipv_6address_quantity is not None:
            result['EniIpv6AddressQuantity'] = self.eni_ipv_6address_quantity
        if self.eni_private_ip_address_quantity is not None:
            result['EniPrivateIpAddressQuantity'] = self.eni_private_ip_address_quantity
        if self.eni_quantity is not None:
            result['EniQuantity'] = self.eni_quantity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EniHighDenseQuantity') is not None:
            self.eni_high_dense_quantity = m.get('EniHighDenseQuantity')
        if m.get('EniIpv6AddressQuantity') is not None:
            self.eni_ipv_6address_quantity = m.get('EniIpv6AddressQuantity')
        if m.get('EniPrivateIpAddressQuantity') is not None:
            self.eni_private_ip_address_quantity = m.get('EniPrivateIpAddressQuantity')
        if m.get('EniQuantity') is not None:
            self.eni_quantity = m.get('EniQuantity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeNodeTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNodeTypeResponseBody = None,
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
            temp_model = DescribeNodeTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # The natural language that is used to filter responses. For more information, see RFC 7231.
        # 
        # zh-CN en-US Default value: zh-CN.
        # 
        # Valid values:
        # 
        # *   en-US
        # *   zh-CN
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
        # The region name.
        self.local_name = local_name
        # The region ID.
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
        # The regions.
        self.regions = regions
        # The request ID.
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
        # The command execution ID.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # The node ID.
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
        # The time when the file sending task was created.
        self.creation_time = creation_time
        # The error code returned when the file failed to be sent to the instance. Valid values:
        # 
        # Null: The file is sent to the instance. NodeNotExists: The specified instance does not exist or has been released. NodeReleased: The instance was released while the file was being sent. NodeNotRunning: The instance was not running while the file sending task was being created. AccountNotExists: The specified account does not exist. ClientNotRunning: Cloud Assistant Agent is not running. ClientNotResponse: Cloud Assistant Agent did not respond. ClientIsUpgrading: Cloud Assistant Agent was being upgraded. ClientNeedUpgrade: Cloud Assistant Agent needs to be upgraded. DeliveryTimeout: The file sending task timed out. FileCreateFail: The file failed to be created. FileAlreadyExists: A file with the same name exists in the specified directory. FileContentInvalid: The file content is invalid. FileNameInvalid: The file name is invalid. FilePathInvalid: The specified directory is invalid. FileAuthorityInvalid: The specified permissions on the file are invalid. UserGroupNotExists: The specified user group does not exist.
        self.error_code = error_code
        # The error message returned if the command failed to be sent or run. Valid values:
        # 
        # *   null: The command is run as expected.
        # *   the specified instance does not exists: The specified instance does not exist or is released.
        # *   the node has released when create task: The instance is released when the command is being run.
        # *   the node is not running when create task: The instance is not in the Running state while the command is being run.
        # *   the command is not applicable: The command is not applicable to the specified instance.
        # *   the specified account does not exists: The specified account does not exist.
        # *   the specified directory does not exists: The specified directory does not exist.
        # *   the cron job expression is invalid: The cron expression that specifies the execution time is invalid.
        # *   the aliyun service is not running on the instance: Cloud Assistant Agent is not running.
        # *   the aliyun service in the instance does not response: Cloud Assistant Agent does not respond.
        # *   the aliyun service in the node is upgrading now: Cloud Assistant Agent is being upgraded.
        # *   the aliyun service in the node need upgrade: Cloud Assistant Agent needs to be upgraded.
        # *   the command delivery has been timeout: The request to send the command timed out.
        # *   the command execution has been timeout: The command execution timed out.
        # *   the command execution got an exception: An exception occurred when the command is being run.
        # *   the command execution has been interrupted: The command execution is interrupted.
        # *   the command execution exit code is not zero: The command execution completes, but the exit code is not 0.
        # *   the specified instance has been released: The instance is released while the file is being sent.
        self.error_info = error_info
        # The time when the file sending task ends. The time is in the 2020-05-22T17:04:18 format.
        self.finish_time = finish_time
        # The status of the file sending task on an instance. Valid values:
        # 
        # *   Pending: The file is being verified or sent.
        # *   Invalid: The file is invalid.
        # *   Running: The file is being sent to the instance.
        # *   Aborted: The file failed to be sent to the instance.
        # *   Success: The file is sent.
        # *   Failed: The file failed to be created on the instance.
        # *   Error: An error occurred and interrupted the file sending task.
        # *   Timeout: The file sending task timed out.
        self.invocation_status = invocation_status
        # The node ID.
        self.node_id = node_id
        # The start time.
        self.start_time = start_time
        # The update time.
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
        # The file sending records on a node.
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
        # The command output.
        # 
        # If ContentEncoding is set to PlainText in the request, the original command output is returned. If ContentEncoding is set to Base64 in the request, the Base64-encoded command output is returned.
        self.content = content
        # The content type of the file.
        # 
        # PlainText: The file content is not encoded. Base64: The file content is encoded in Base64. Default value: PlainText.
        self.content_type = content_type
        # The time when the file sending task was created.
        self.creation_time = creation_time
        # The command description.
        self.description = description
        # The user group of the file.
        self.file_group = file_group
        # The permissions on the file.
        self.file_mode = file_mode
        # The owner of the file.
        self.file_owner = file_owner
        # The overall sending status of the file. The overall sending status of the file varies based on the sending status of the file on all destination instances. Valid values:
        # 
        # *   Pending: The file is being verified or sent. If the sending state of the file on at least one instance is Pending, the overall sending state of the file is Pending.
        # 
        # *   Running: The file is being sent to the instance. If the sending state of the file on at least one instance is Running, the overall sending state of the file is Running.
        # 
        # *   Success: If the sending state of the file on all instances is Success, the overall sending state of the file is Success.
        # 
        # *   Failed: If the sending state of the file on all instances is Failed, the overall sending state of the file is Failed. If the sending state of the file on one or more instances is one of the following values, the overall sending state of the file is Failed:
        # 
        #     *   Invalid: The file is invalid.
        #     *   Aborted: The file failed to be sent to the instances.
        #     *   Failed: The file failed to be created on the instances.
        #     *   Timeout: The file sending task timed out.
        #     *   Error: An error occurred and interrupted the file sending task.
        # 
        # *   PartialFailed: The file sending task was completed on some instances but failed on other instances. If the sending state of the file is Success on some instances and is Failed on other instances, the overall sending state of the file is PartialFailed.
        self.invocation_status = invocation_status
        # The file sending records.
        self.invoke_nodes = invoke_nodes
        # The name of the file sending task.
        self.name = name
        # The number of nodes.
        self.node_count = node_count
        # Indicates whether a file was overwritten in the destination directory if the file has the same name as the sent file.
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.overwrite = overwrite
        # The destination directory.
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
        # The command execution ID.
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
        # The file sending records.
        self.invocations = invocations
        # The request ID.
        self.request_id = request_id
        # The total number of the commands.
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
        # The task ID.
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
        # The creation time.
        self.create_time = create_time
        # The error message returned for failed sub tasks.
        self.message = message
        # The task ID.
        self.task_id = task_id
        # The task status.
        self.task_state = task_state
        # The task type.
        # 
        # Valid values:
        # 
        # *   reclone_node_sub_task
        # *   initialize_bare_cluster
        # *   extend_bare_cluster
        # *   reclone_node
        # *   reboot_node
        # *   extend_ack_edge_cluster
        # *   extend_cluster
        # *   initialize_ack_edge_cluster
        # *   cut_node_sub_task
        # *   reboot_node_sub_task
        # *   reclone_ack_edge_node
        # *   initialize_cluster
        # *   cut_cluster
        # *   reclone_bare_node
        # *   cut_bare_cluster
        self.task_type = task_type
        # The update time.
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
        # The error message of the step.
        self.message = message
        # The stage marker.
        # 
        # Valid values:
        # 
        # *   机器释放: Machine release.
        # *   节点并发初始化: Node concurrent initialization.
        # *   节点释放: Node release.
        # *   机器替换: Machine replacement.
        # *   节点缩容: Node scale-in.
        # *   提前续费: Early renewal.
        # *   物理机清理: Physical machine cleanup.
        # *   节点清理: Node cleanup.
        # *   创建K8s集群: Create Kubernetes cluster.
        # *   网络初始化: Network initialization.
        # *   节点重启: Node restart.
        # *   节点退订: Node unsubscribe.
        # *   集群扩容: Cluster scale-out.
        # *   异常机器释放: Abnormal machine release.
        self.stage_tag = stage_tag
        # The start time.
        self.start_time = start_time
        # The name of the step.
        self.step_name = step_name
        # The step status.
        # 
        # Valid values:
        # 
        # *   execution_success
        # *   execution_failed
        self.step_state = step_state
        # The type of the step.
        # 
        # Valid values:
        # 
        # *   normal: A normal step has only one successor step.
        # *   dispersive: A dispersive step has multiple successor steps.
        self.step_type = step_type
        # The sub tasks.
        self.sub_tasks = sub_tasks
        # The update time.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The create time.
        self.create_time = create_time
        # The error message returned for failed tasks.
        self.message = message
        # The IDs of the nodes.
        self.node_ids = node_ids
        # The request ID.
        self.request_id = request_id
        # The steps.
        self.steps = steps
        # The task status.
        # 
        # Valid values:
        # 
        # *   running
        # *   execution_success
        # *   execution_fail
        # *   waiting_to_run
        self.task_state = task_state
        # The task type.
        # 
        # Valid values:
        # 
        # *   reclone_node_sub_task
        # *   initialize_bare_cluster
        # *   extend_bare_cluster
        # *   reclone_node
        # *   reboot_node
        # *   extend_ack_edge_cluster
        # *   extend_cluster
        # *   initialize_ack_edge_cluster
        # *   cut_node_sub_task
        # *   reboot_node_sub_task
        # *   reclone_ack_edge_node
        # *   initialize_cluster
        # *   cut_cluster
        # *   reclone_bare_node
        # *   cut_bare_cluster
        self.task_type = task_type
        # The update time.
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


class DescribeVscRequest(TeaModel):
    def __init__(
        self,
        vsc_id: str = None,
    ):
        # The VSC ID.
        # 
        # This parameter is required.
        self.vsc_id = vsc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')
        return self


class DescribeVscResponseBody(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        vsc_id: str = None,
        vsc_name: str = None,
        vsc_type: str = None,
    ):
        # The ID of the compute node in which the VSC resides.
        self.node_id = node_id
        # The request ID.
        self.request_id = request_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The VSC status.
        # 
        # Valid values:
        # 
        # *   Creating
        # *   Normal
        # *   Deleting
        self.status = status
        # The VSC ID.
        self.vsc_id = vsc_id
        # The custom name of the VSC.
        self.vsc_name = vsc_name
        # The VSC type.
        self.vsc_type = vsc_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id
        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name
        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')
        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')
        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')
        return self


class DescribeVscResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeVscResponseBody = None,
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
            temp_model = DescribeVscResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeZonesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
    ):
        # The natural language that is used to filter responses. For more information, see RFC 7231. Valid values:
        # 
        # zh-CN en-US Default value: zh-CN.
        # 
        # Valid values:
        # 
        # *   en-US
        # *   zh-CN
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
        # The zone name.
        self.local_name = local_name
        # The zone ID.
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
        # The request ID.
        self.request_id = request_id
        # The list of zones.
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
        hostname: str = None,
        node_id: str = None,
    ):
        # Bond information
        self.bonds = bonds
        # Hostname
        self.hostname = hostname
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
        if self.hostname is not None:
            result['Hostname'] = self.hostname
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
        if m.get('Hostname') is not None:
            self.hostname = m.get('Hostname')
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


class ExtendClusterRequestNodeGroupsNodeTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Node tag key
        self.key = key
        # Node tag value
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


class ExtendClusterRequestNodeGroupsNodesDataDisk(TeaModel):
    def __init__(
        self,
        category: str = None,
        delete_with_node: bool = None,
        performance_level: str = None,
        size: int = None,
    ):
        # Type
        self.category = category
        # Whether the data disk is deleted with the node
        self.delete_with_node = delete_with_node
        # Data Disk Performance Level
        self.performance_level = performance_level
        # Disk Size
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['Category'] = self.category
        if self.delete_with_node is not None:
            result['DeleteWithNode'] = self.delete_with_node
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('DeleteWithNode') is not None:
            self.delete_with_node = m.get('DeleteWithNode')
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ExtendClusterRequestNodeGroupsNodes(TeaModel):
    def __init__(
        self,
        data_disk: List[ExtendClusterRequestNodeGroupsNodesDataDisk] = None,
        hostname: str = None,
        login_password: str = None,
        node_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # Data Disk Specifications
        self.data_disk = data_disk
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
        if self.data_disk:
            for k in self.data_disk:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataDisk'] = []
        if self.data_disk is not None:
            for k in self.data_disk:
                result['DataDisk'].append(k.to_map() if k else None)
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
            for k in m.get('DataDisk'):
                temp_model = ExtendClusterRequestNodeGroupsNodesDataDisk()
                self.data_disk.append(temp_model.from_map(k))
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
        amount: int = None,
        auto_renew: bool = None,
        charge_type: str = None,
        hostnames: List[str] = None,
        login_password: str = None,
        node_group_id: str = None,
        node_tag: List[ExtendClusterRequestNodeGroupsNodeTag] = None,
        nodes: List[ExtendClusterRequestNodeGroupsNodes] = None,
        period: int = None,
        user_data: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        zone_id: str = None,
    ):
        # Number of nodes to purchase. Range: 0~500. If the Amount parameter is set to 0, it means no new nodes will be purchased and existing nodes will be used for scaling. If the Amount parameter is set to 1~500, it means a certain number of nodes will be purchased and used for scaling. Default value: 0
        self.amount = amount
        # Whether to automatically renew the purchased nodes. This parameter takes effect when the Amount parameter is not 0 and the ChargeType is set to PrePaid. Valid values: True (auto-renewal); False (no auto-renewal). Default value: False
        self.auto_renew = auto_renew
        # Payment method for the nodes. When the Amount parameter is set to 0, this parameter does not take effect. Valid values: PrePaid (Subscription); PostPaid (Pay-As-You-Go). Default value: PrePaid.
        self.charge_type = charge_type
        # Set the hostnames for the purchased nodes. This parameter does not take effect when the Amount parameter is set to 0.
        self.hostnames = hostnames
        # Set the login password for the purchased nodes. This parameter is not effective when the Amount parameter is set to 0.
        self.login_password = login_password
        # Node Group ID
        self.node_group_id = node_group_id
        # Node tags
        self.node_tag = node_tag
        # List of Nodes
        self.nodes = nodes
        # Duration of the node purchase (in months). Valid values: 1, 6, 12, 24, 36, 48. This parameter takes effect when the Amount parameter is not 0 and the ChargeType is set to PrePaid.
        self.period = period
        # Custom Data
        self.user_data = user_data
        # VSwitch ID
        self.v_switch_id = v_switch_id
        # VPC ID
        self.vpc_id = vpc_id
        # Zone ID
        self.zone_id = zone_id

    def validate(self):
        if self.node_tag:
            for k in self.node_tag:
                if k:
                    k.validate()
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['Amount'] = self.amount
        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew
        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        result['NodeTag'] = []
        if self.node_tag is not None:
            for k in self.node_tag:
                result['NodeTag'].append(k.to_map() if k else None)
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        if self.period is not None:
            result['Period'] = self.period
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
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')
        self.node_tag = []
        if m.get('NodeTag') is not None:
            for k in m.get('NodeTag'):
                temp_model = ExtendClusterRequestNodeGroupsNodeTag()
                self.node_tag.append(temp_model.from_map(k))
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = ExtendClusterRequestNodeGroupsNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
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
        # IP allocation combination policy: Each policy can only choose one type, and multiple policies can be combined
        self.ip_allocation_policy = ip_allocation_policy
        # Node Groups
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
        # IP allocation combination policy: Each policy can only choose one type, and multiple policies can be combined
        self.ip_allocation_policy_shrink = ip_allocation_policy_shrink
        # Node Groups
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
        # The tag key for the node.
        self.key = key
        # The tag value for the node.
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
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The number of entries per page. Default value: 20.
        self.max_results = max_results
        # The token that determines the start position of the query. Set this parameter to the value of the NextToken parameter that is returned from the last call.
        self.next_token = next_token
        # The node group ID.
        self.node_group_id = node_group_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        file_system_mount_enabled: bool = None,
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
        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled
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
        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')
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
        # The returned pagination token which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The nodes.
        self.nodes = nodes
        # The request ID.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        # The number of entries per page. Default value: 20.
        self.max_results = max_results
        # The token that determines the start position of the query. Set this parameter to the value of the NextToken parameter that is returned from the last call.
        self.next_token = next_token
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        # The cluster description.
        self.cluster_description = cluster_description
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The cluster type.
        # 
        # Valid values:
        # 
        # *   AckEdgePro
        # *   ExclusiveBareCluster
        # *   Lite
        self.cluster_type = cluster_type
        # The component information.
        self.components = components
        # The IP type of the computing network.
        self.computing_ip_version = computing_ip_version
        # The creation time.
        self.create_time = create_time
        # The cluster number.
        self.hpn_zone = hpn_zone
        # The number of nodes.
        self.node_count = node_count
        # The number of node groups.
        self.node_group_count = node_group_count
        # The cluster status.
        # 
        # Valid values:
        # 
        # *   running
        # *   expanding
        # *   shrinking
        # *   initializing
        self.operating_state = operating_state
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tags = tags
        # The job ID.
        self.task_id = task_id
        # The update time.
        self.update_time = update_time
        # The virtual private cloud (VPC) ID.
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
        # The clusters.
        self.clusters = clusters
        # The returned pagination token which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
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
        # Type of diagnosis, indicating which diagnostic rules are hit.
        self.diag_type = diag_type
        # Number of items per page in a paginated query. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 20, the default value is 20.
        # - If the set value is greater than 100, the default value is 100.
        self.max_results = max_results
        # NextToken for the next page. Include this value when requesting the next page.
        self.next_token = next_token
        # The resource group ID.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # Cluster Name
        self.cluster_name = cluster_name
        # Creation time of the diagnostic task.
        self.creation_time = creation_time
        # Diagnostic content. For example, in network diagnostics, there are static configuration checks, dynamic operation checks, and other diagnostic contents.
        self.diag_content = diag_content
        # Diagnosis ID
        self.diag_id = diag_id
        # Diagnostic result, either success or failure.
        self.diag_result = diag_result
        # Completion time of the diagnostic task.
        self.finished_time = finished_time
        # The resource ID.
        self.resource_id = resource_id
        # Server name.
        self.server_name = server_name
        # Status of the diagnostic task. Possible values:
        # - InProgress: Diagnosing.
        # - Finished: Diagnosis completed.
        # - Failed: Diagnosis failed.
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
        # The diagnostic information.
        self.diagnostic_results = diagnostic_results
        # Number of items per page in a paginated query. The maximum value is 100.
        # 
        # Default value:
        # 
        # - If no value is set or the set value is less than 20, the default value is 20.
        # - If the set value is greater than 100, the default value is 100.
        self.max_results = max_results
        # NextToken for the next page. Include this value when requesting the next page.
        self.next_token = next_token
        # The request ID.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        operating_states: List[str] = None,
        resource_group_id: str = None,
        tags: List[ListFreeNodesRequestTags] = None,
    ):
        # The cluster number.
        self.hpn_zone = hpn_zone
        # The instance type.
        self.machine_type = machine_type
        # The number of entries per page. Default value: 20.
        self.max_results = max_results
        # The token that determines the start position of the query. Set this parameter to the value of the NextToken parameter that is returned from the last call.
        self.next_token = next_token
        # The types of the returned nodes that are not used.
        self.operating_states = operating_states
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
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
        if self.operating_states is not None:
            result['OperatingStates'] = self.operating_states
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
        if m.get('OperatingStates') is not None:
            self.operating_states = m.get('OperatingStates')
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
        # The tag key.
        self.key = key
        # The tag value.
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
        # The commodity code.
        self.commodity_code = commodity_code
        # The creation time.
        self.create_time = create_time
        # The time when the node expires.
        self.expired_time = expired_time
        # The cluster number.
        self.hpn_zone = hpn_zone
        # The instance type.
        self.machine_type = machine_type
        # The node ID.
        self.node_id = node_id
        # The node status.
        self.operating_state = operating_state
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The serial number of the node.
        self.sn = sn
        # The tags.
        self.tags = tags
        # The zone ID.
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
        # The returned pagination token which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The nodes.
        self.nodes = nodes
        # The request ID.
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
        # The architecture.
        self.architecture = architecture
        # The image version.
        self.image_version = image_version
        # The platform.
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
        release_file_size: str = None,
        type: str = None,
    ):
        # The architecture.
        self.architecture = architecture
        # The description.
        self.description = description
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image version.
        self.image_version = image_version
        # The number of nodes.
        self.node_count = node_count
        # The platform.
        self.platform = platform
        # The MD5 hash value of the file.
        self.release_file_md_5 = release_file_md_5
        # The image size.
        self.release_file_size = release_file_size
        # The image type.
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
        # The image details.
        self.images = images
        # The token that is used in the next request to retrieve a new page of results.
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
        # hpn zone infomation
        self.hpn_zone = hpn_zone
        # The type of machine.
        self.machine_type = machine_type
        # The ID of the region in which the application is located.
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
        # hpn information of machine
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
        # hpn information of machine
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
        # Network of cluster
        self.cluster_net = cluster_net
        # Specifies whether to enable the Jumbo Frames feature for the instance. Valid values:
        # 
        # *   true: The Jumbo Frame feature is enabled for the instance.
        # *   false: The Jumbo Frame feature is disabled for the instance.
        # 
        # Take note of the following items:
        # 
        # *   The instance must be in the Running (`Running`) or Stopped (`Stopped`) state.
        # *   The instance must reside in a VPC.
        # *   After the Jumbo Frames feature is enabled, the MTU value of the instance is set to 8500. After the Jumbo Frames feature is disabled, the MTU value of the instance is set to 1500. You can enable the Jumbo Frames feature only for specific instance types. For more information, see [Jumbo Frames](https://help.aliyun.com/document_detail/200512.html).
        self.enable_jumbo_frame = enable_jumbo_frame
        # HPN zone
        self.hpn_zone = hpn_zone
        # Specifies whether dpu machine.
        self.is_dpu_mode = is_dpu_mode
        # The type of machine.
        self.machine_type = machine_type
        # Network architecture
        self.net_arch = net_arch
        # The ID of the region in which the application is located.
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
        # machine network infomation
        self.machine_network_info = machine_network_info
        # Id of the request
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
        # The name of the instance type.
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
        # The number of bonds.
        self.bond_num = bond_num
        # The CPU information.
        self.cpu_info = cpu_info
        # The disk information.
        self.disk_info = disk_info
        # The GPU information.
        self.gpu_info = gpu_info
        # The storage information.
        self.memory_info = memory_info
        # The name of the instance type.
        self.name = name
        # The network information.
        self.network_info = network_info
        # The number of nodes.
        self.node_count = node_count
        # The number of vCPUs.
        self.total_cpu_core = total_cpu_core
        # The access type.
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
        # The instance types.
        self.machine_types = machine_types
        # The token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
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
        # The number of entries to return on each page. Maximum value: 100.
        # 
        # Default value:
        # 
        # *   If you do not configure this parameter or if you set this parameter to a value less than 20, the default value is 20.
        # *   If you set this parameter to a value that is greater than 100, the default value is 100.
        self.max_results = max_results
        # The type of the network test.
        self.net_test_type = net_test_type
        # The token that determines the start position of the query. Set this parameter to the value of the NextToken parameter that is returned from the last call.
        self.next_token = next_token
        # The resource group ID.
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
        # The IP address of the node.
        self.ip = ip
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
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
        # The number of GPUs.
        self.gpunum = gpunum
        # The hosts of the test node.
        self.hosts = hosts
        # The communication library model.
        self.model = model
        # The CommTest type, which can be ACCL or NCCL.
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
        # The bonding of network interface card.
        self.bond = bond
        # The IP address of the node.
        self.ip = ip
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
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
        # The hosts.
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
        # The bonding of network interface card.
        self.bond = bond
        # The IP address.
        self.ip = ip
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
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
        # The bonding of network interface card.
        self.bond = bond
        # The IP address of the node.
        self.ip = ip
        # The resource ID.
        self.resource_id = resource_id
        # The name of the service.
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
        # The clients.
        self.clients = clients
        # The running duration of the pipeline job. Unit: seconds.
        self.duration = duration
        # If the protocol is RDMA, can be True or False. If the protocol is TCP, this field is empty.
        self.gdr = gdr
        # The network protocol, which can be RDMA or TCP.
        self.protocol = protocol
        # If the protocol is TCP, the number of concurrent connections. If the protocol is RDMA, the configured QP value.
        self.qp = qp
        # If the TrafficModel is Fullmesh, this parameter is empty.
        self.servers = servers
        # The traffic model, which can be MTON or Fullmesh.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # Returned when NetTestType is CommTest.
        self.comm_test = comm_test
        # The creation time.
        self.creation_time = creation_time
        # Returned when NetTestType is DelayTest.
        self.delay_test = delay_test
        # The finish time.
        self.finished_time = finished_time
        # The type of the network test.
        self.net_test_type = net_test_type
        # The network mode.
        self.network_mode = network_mode
        # The port number.
        self.port = port
        # The status of the network test task. Valid values:\\
        # ● InProgress\\
        # ● Finished\\
        # ● Failed
        self.status = status
        # The test ID. The unique identifier of the resource test task.
        self.test_id = test_id
        # Returned when NetTestType is TrafficTest.
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
        # The number of entries to return on each page. Maximum value: 100.
        # 
        # Default value:
        # 
        # *   If you do not configure this parameter or if you set this parameter to a value less than 20, the default value is 20.
        # *   If you set this parameter to a value that is greater than 100, the default value is 100.
        self.max_results = max_results
        # The results.
        self.net_test_results = net_test_results
        # The token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The number of entries per page. Maximum value: 100.
        # 
        # Default value:
        # 
        # • If you do not configure this parameter or if you set this parameter to a value less than 20, the default value is 20.
        # 
        # • If you set this parameter to a value greater than 100, the default value is 100.
        self.max_results = max_results
        # The token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The node group ID.
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
        file_system_mount_enabled: bool = None,
        group_id: str = None,
        group_name: str = None,
        image_id: str = None,
        image_name: str = None,
        machine_type: str = None,
        node_count: int = None,
        update_time: str = None,
        virtual_gpu_enabled: bool = None,
        zone_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # The creation time.
        self.create_time = create_time
        # The description.
        self.description = description
        # Indicates whether file storage mounting is supported.
        self.file_system_mount_enabled = file_system_mount_enabled
        # The group ID.
        self.group_id = group_id
        # The group name.
        self.group_name = group_name
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The instance type.
        self.machine_type = machine_type
        # The number of nodes.
        self.node_count = node_count
        # The update time.
        self.update_time = update_time
        # Whether to enable gpu virtualization or not
        self.virtual_gpu_enabled = virtual_gpu_enabled
        # The zone ID.
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
        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled
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
        if self.virtual_gpu_enabled is not None:
            result['VirtualGpuEnabled'] = self.virtual_gpu_enabled
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
        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')
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
        if m.get('VirtualGpuEnabled') is not None:
            self.virtual_gpu_enabled = m.get('VirtualGpuEnabled')
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
        # The node groups.
        self.groups = groups
        # The token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        # The token that determines the start position of the query. Set this parameter to the value of the NextToken parameter that is returned from the last call.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources.
        self.resource_id = resource_id
        # The resource type.
        # 
        # Valid values:
        # 
        # *   Node
        # *   Vcc
        # *   Cluster
        # *   Subnet
        # *   Vpd
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
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
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        # 
        # Valid values:
        # 
        # *   Node
        # *   Cluster
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
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
        # The token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tags.
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
        # The access type of cluster type
        self.access_type = access_type
        # The name of cluster type
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
        # The list of cluster types. Number of elements in the array: 1 to 100.
        self.cluster_types = cluster_types
        # NextToken for the next page. Include this value when requesting the next page.
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


class ListVscsRequestTag(TeaModel):
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


class ListVscsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_ids: List[str] = None,
        resource_group_id: str = None,
        tag: List[ListVscsRequestTag] = None,
        vsc_name: str = None,
    ):
        # The maximum number of data entries to return.
        self.max_results = max_results
        # The token that is used in the next request to retrieve a new page of results. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The IDs of the nodes.
        self.node_ids = node_ids
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag = tag
        # The VSC name.
        self.vsc_name = vsc_name

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_ids is not None:
            result['NodeIds'] = self.node_ids
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeIds') is not None:
            self.node_ids = m.get('NodeIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListVscsRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')
        return self


class ListVscsShrinkRequestTag(TeaModel):
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


class ListVscsShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_ids_shrink: str = None,
        resource_group_id: str = None,
        tag: List[ListVscsShrinkRequestTag] = None,
        vsc_name: str = None,
    ):
        # The maximum number of data entries to return.
        self.max_results = max_results
        # The token that is used in the next request to retrieve a new page of results. If you leave this parameter empty, the query starts from the beginning.
        self.next_token = next_token
        # The IDs of the nodes.
        self.node_ids_shrink = node_ids_shrink
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The tags.
        self.tag = tag
        # The VSC name.
        self.vsc_name = vsc_name

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
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.node_ids_shrink is not None:
            result['NodeIds'] = self.node_ids_shrink
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('NodeIds') is not None:
            self.node_ids_shrink = m.get('NodeIds')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListVscsShrinkRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')
        return self


class ListVscsResponseBodyVscsTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListVscsResponseBodyVscs(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[ListVscsResponseBodyVscsTags] = None,
        vsc_id: str = None,
        vsc_name: str = None,
        vsc_type: str = None,
    ):
        # The ID of the Lingjun node.
        self.node_id = node_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The VSC status.
        # 
        # Valid values:
        # 
        # *   Creating
        # *   Normal
        # *   Deleting
        self.status = status
        # The tags.
        self.tags = tags
        # The VSC ID.
        self.vsc_id = vsc_id
        # The custom name of the VSC.
        self.vsc_name = vsc_name
        # The VSC type. Valid values: primary and standard.
        self.vsc_type = vsc_type

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
        if self.node_id is not None:
            result['NodeId'] = self.node_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.status is not None:
            result['Status'] = self.status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.vsc_id is not None:
            result['VscId'] = self.vsc_id
        if self.vsc_name is not None:
            result['VscName'] = self.vsc_name
        if self.vsc_type is not None:
            result['VscType'] = self.vsc_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListVscsResponseBodyVscsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('VscId') is not None:
            self.vsc_id = m.get('VscId')
        if m.get('VscName') is not None:
            self.vsc_name = m.get('VscName')
        if m.get('VscType') is not None:
            self.vsc_type = m.get('VscType')
        return self


class ListVscsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        vscs: List[ListVscsResponseBodyVscs] = None,
    ):
        # No response is returned. The TotalCount parameter is used.
        self.max_results = max_results
        # The token. It can be used in the next request to retrieve a new page of results. If this parameter is empty, no next page exists.
        # 
        # This parameter is required.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of VSCs.
        self.total_count = total_count
        # The VSCs.
        self.vscs = vscs

    def validate(self):
        if self.vscs:
            for k in self.vscs:
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Vscs'] = []
        if self.vscs is not None:
            for k in self.vscs:
                result['Vscs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vscs = []
        if m.get('Vscs') is not None:
            for k in m.get('Vscs'):
                temp_model = ListVscsResponseBodyVscs()
                self.vscs.append(temp_model.from_map(k))
        return self


class ListVscsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVscsResponseBody = None,
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
            temp_model = ListVscsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RebootNodesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        ignore_failed_node_tasks: bool = None,
        nodes: List[str] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The nodes.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The nodes.
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
        # The request ID.
        self.request_id = request_id
        # The job ID.
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
        # The hostname.
        self.hostname = hostname
        # The system image ID.
        self.image_id = image_id
        # The logon password.
        self.login_password = login_password
        # The node ID.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The nodes.
        self.nodes = nodes
        # The user data.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The nodes.
        self.nodes_shrink = nodes_shrink
        # The user data.
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
        # The request ID.
        self.request_id = request_id
        # The job ID.
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
        # The client token to ensure the idempotency of the request. Use your client to generate the token that is unique among requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see "How to ensure idempotence".
        self.client_token = client_token
        # The command content. Take note of the following:
        # 
        # *   When `EnableParameter` is set to true, you can use custom parameters in the command.
        # *   Define custom parameters in the {{}} format. Within `{{}}`, the spaces and line feeds before and after the parameter names are ignored.
        # *   You can specify up to 20 custom parameters.
        # *   A custom parameter name can contain only letters, digits, underscores (_), and hyphens (-). The name is not case-sensitive.
        # *   Each custom parameter name is up to 64 bytes in length.
        self.command_content = command_content
        # The ID of the command.
        self.command_id = command_id
        # The encoding mode of the command content. Valid values:
        # 
        # *   PlainText
        # *   Base64
        # 
        # Default value: PlainText. If the specified value of this parameter is invalid, PlainText is used by default.
        self.content_encoding = content_encoding
        # The command description.
        self.description = description
        # Specifies whether to use custom parameters in the command.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The schedule to run the command. Supported schedule types: at a fixed interval based on a rate expression, run only once at a specific time, or run at specific times based on a cron expression.
        # 
        # *   To run the command at a fixed interval, use a rate expression to specify the interval. The interval can be in seconds, minutes, hours, or days. This option is suitable for scenarios in which tasks need to be executed at a fixed interval. Format: rate(\\<Execution interval value> \\<Execution interval unit>). For example, rate(5m) means to run the command every 5 minutes. When you specify an interval, take note of the following limits:
        # 
        #     *   The interval can be anywhere from 60 seconds to 7 days, but must be longer than the timeout period of the scheduled task.
        #     *   The interval is the time between two consecutive executions, irrelevant of the time required to run the command. For example, assume that you set the interval to 5 minutes and that it takes 2 minutes to run the command each time. The system waits 3 minutes before running the command again.
        #     *   The command is not immediately executed after the task is created. For example, assume that you set the interval to 5 minutes. The task begins to be executed 5 minutes after it is created.
        # 
        # *   To run a command only once at a specific point in time, specify a point in time and a time zone. Format: at(yyyy-MM-dd HH:mm:ss \\<Time zone>). If you do not specify a time zone, the Coordinated Universal Time (UTC) time zone is used by default. The time zone name supports the following formats: Full name, such as Asia/Shanghai and America/Los_Angeles. The time offset from GMT. Examples: GMT+8:00 (UTC+8) and GMT-7:00 (UTC-7). If you use the GMT format, you cannot add leading zeros to the hour value. The time zone abbreviation. Only UTC is supported. For example, to configure a command to run only once at 13:15:30 on June 6, 2022 (Shanghai time), set the time to at(2022-06-06 13:15:30 Asia/Shanghai). To configure a command to run only once at 13:15:30 on June 6, 2022 (UTC-7), set the time to at(2022-06-06 13:15:30 GMT-7:00).
        # 
        # *   To run a command at designated points in time, use a cron expression to define the schedule. Format: \\<Cron expression> \\<Time zone>. Example: \\<Seconds> \\<Minutes> \\<Hours> \\<Day of the month> \\<Month> \\<Day of the week> \\<Year (optional)> \\<Time zone>. The system calculates the execution times of the command based on the specified cron expression and time zone and runs the command as scheduled. If you do not specify a time zone, the system time zone of the instance is used by default. For more information, see Cron expressions. The time zone name supports the following formats:
        # 
        #     *   Full name, such as Asia/Shanghai and America/Los_Angeles.
        #     *   The time offset from GMT. Examples: GMT+8:00 (UTC+8) and GMT-7:00 (UTC-7). If you use the GMT format, you cannot add leading zeros to the hour value.
        #     *   The time zone abbreviation. Only UTC is supported.
        # 
        #     For example, if you specify a command to run at 10:15:00 every day in 2022 in China/Shanghai time, set the time to 0 15 10 ? \\* \\* 2022 Asia/Shanghai. To configure a command to run every half an hour from 10:00:00 to 11:30:00 every day in 2022 (UTC+8), set the schedule to 0 0/30 10-11 \\* \\* ? 2022 GMT+8:00. To configure a command to run every 5 minutes from 14:00:00 to 14:55:00 every October every two years from 2022 in UTC, set the schedule to 0 0/5 14 \\* 10 ? 2022/2 UTC.
        self.frequency = frequency
        # The launcher for script execution. Cannot exceed 1 KB.
        self.launcher = launcher
        # The command name.
        self.name = name
        # The node list.
        self.node_id_list = node_id_list
        # The key-value pairs of custom parameters to pass in when the command includes custom parameters. For example, the command content is `echo {{name}}`. You can use `Parameters` to pass in the `{"name":"Jack"}` key-value pair. The `name` key of the custom parameter is automatically replaced by the paired Jack value to generate a new command. As a result, the `echo Jack` command is run.
        # 
        # You can specify 0 to 10 custom parameters. Take note of the following:
        # 
        # *   The key of a custom parameter can be up to 64 characters in length, and cannot be an empty string.
        # *   The value of a custom parameter can be an empty string.
        # *   If you want to retain a command, make sure that the command after Base64 encoding, including custom parameters and original command content, does not exceed 18 KB in size. If you do not want to retain the command, make sure that the command after Base64 encoding does not exceed 24 KB in size. You can set `KeepCommand` to specify whether to retain the command.
        # *   The specified custom parameter names must be included in the custom parameter names that you specify when you create the command. You can use empty strings to represent the parameters that are not passed in.
        # 
        # This parameter is left empty by default, which indicates that the custom parameter feature is disabled.
        self.parameters = parameters
        # The mode to run the command. Valid values:
        # 
        # *   Once: runs the command immediately.
        # *   Period: runs the command based on a schedule. When set to `Period`, `Frequency` is required.
        # *   NextRebootOnly: runs the command the next time the instances is started.
        # *   EveryReboot: runs the command every time the instance is started.
        # 
        # Default value:
        # 
        # *   If you do not specify `Frequency`, the default value is `Once`.
        # *   If you specify `Frequency`, RepeatMode is set to `Period` regardless of whether a value is already specified.
        self.repeat_mode = repeat_mode
        # Indicates how the command task is stopped when a command execution is manually stopped or times out. Valid values:
        # 
        # Process: The process of the command is stopped. ProcessTree: The process tree of the command is stopped. In this case, the process of the command and all subprocesses are stopped.
        self.termination_mode = termination_mode
        # The timeout period for the command. Unit: seconds. A timeout error occurs if the command cannot be run because the process slows down or because a specific module or Cloud Assistant Agent does not exist. When the specified timeout period ends, the command process is forcefully terminated. Default value: 60.
        self.timeout = timeout
        # The username that you use to run the command. The name can be up to 255 characters in length. For Linux instances, the root user is used by default.
        self.username = username
        # The working path of the command. You can specify a custom path. Default path:
        # 
        # Linux instances: By default, the path is in the /home directory of the root user.
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
        # The client token to ensure the idempotency of the request. Use your client to generate the token that is unique among requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see "How to ensure idempotence".
        self.client_token = client_token
        # The command content. Take note of the following:
        # 
        # *   When `EnableParameter` is set to true, you can use custom parameters in the command.
        # *   Define custom parameters in the {{}} format. Within `{{}}`, the spaces and line feeds before and after the parameter names are ignored.
        # *   You can specify up to 20 custom parameters.
        # *   A custom parameter name can contain only letters, digits, underscores (_), and hyphens (-). The name is not case-sensitive.
        # *   Each custom parameter name is up to 64 bytes in length.
        self.command_content = command_content
        # The ID of the command.
        self.command_id = command_id
        # The encoding mode of the command content. Valid values:
        # 
        # *   PlainText
        # *   Base64
        # 
        # Default value: PlainText. If the specified value of this parameter is invalid, PlainText is used by default.
        self.content_encoding = content_encoding
        # The command description.
        self.description = description
        # Specifies whether to use custom parameters in the command.
        # 
        # Default value: false.
        self.enable_parameter = enable_parameter
        # The schedule to run the command. Supported schedule types: at a fixed interval based on a rate expression, run only once at a specific time, or run at specific times based on a cron expression.
        # 
        # *   To run the command at a fixed interval, use a rate expression to specify the interval. The interval can be in seconds, minutes, hours, or days. This option is suitable for scenarios in which tasks need to be executed at a fixed interval. Format: rate(\\<Execution interval value> \\<Execution interval unit>). For example, rate(5m) means to run the command every 5 minutes. When you specify an interval, take note of the following limits:
        # 
        #     *   The interval can be anywhere from 60 seconds to 7 days, but must be longer than the timeout period of the scheduled task.
        #     *   The interval is the time between two consecutive executions, irrelevant of the time required to run the command. For example, assume that you set the interval to 5 minutes and that it takes 2 minutes to run the command each time. The system waits 3 minutes before running the command again.
        #     *   The command is not immediately executed after the task is created. For example, assume that you set the interval to 5 minutes. The task begins to be executed 5 minutes after it is created.
        # 
        # *   To run a command only once at a specific point in time, specify a point in time and a time zone. Format: at(yyyy-MM-dd HH:mm:ss \\<Time zone>). If you do not specify a time zone, the Coordinated Universal Time (UTC) time zone is used by default. The time zone name supports the following formats: Full name, such as Asia/Shanghai and America/Los_Angeles. The time offset from GMT. Examples: GMT+8:00 (UTC+8) and GMT-7:00 (UTC-7). If you use the GMT format, you cannot add leading zeros to the hour value. The time zone abbreviation. Only UTC is supported. For example, to configure a command to run only once at 13:15:30 on June 6, 2022 (Shanghai time), set the time to at(2022-06-06 13:15:30 Asia/Shanghai). To configure a command to run only once at 13:15:30 on June 6, 2022 (UTC-7), set the time to at(2022-06-06 13:15:30 GMT-7:00).
        # 
        # *   To run a command at designated points in time, use a cron expression to define the schedule. Format: \\<Cron expression> \\<Time zone>. Example: \\<Seconds> \\<Minutes> \\<Hours> \\<Day of the month> \\<Month> \\<Day of the week> \\<Year (optional)> \\<Time zone>. The system calculates the execution times of the command based on the specified cron expression and time zone and runs the command as scheduled. If you do not specify a time zone, the system time zone of the instance is used by default. For more information, see Cron expressions. The time zone name supports the following formats:
        # 
        #     *   Full name, such as Asia/Shanghai and America/Los_Angeles.
        #     *   The time offset from GMT. Examples: GMT+8:00 (UTC+8) and GMT-7:00 (UTC-7). If you use the GMT format, you cannot add leading zeros to the hour value.
        #     *   The time zone abbreviation. Only UTC is supported.
        # 
        #     For example, if you specify a command to run at 10:15:00 every day in 2022 in China/Shanghai time, set the time to 0 15 10 ? \\* \\* 2022 Asia/Shanghai. To configure a command to run every half an hour from 10:00:00 to 11:30:00 every day in 2022 (UTC+8), set the schedule to 0 0/30 10-11 \\* \\* ? 2022 GMT+8:00. To configure a command to run every 5 minutes from 14:00:00 to 14:55:00 every October every two years from 2022 in UTC, set the schedule to 0 0/5 14 \\* 10 ? 2022/2 UTC.
        self.frequency = frequency
        # The launcher for script execution. Cannot exceed 1 KB.
        self.launcher = launcher
        # The command name.
        self.name = name
        # The node list.
        self.node_id_list_shrink = node_id_list_shrink
        # The key-value pairs of custom parameters to pass in when the command includes custom parameters. For example, the command content is `echo {{name}}`. You can use `Parameters` to pass in the `{"name":"Jack"}` key-value pair. The `name` key of the custom parameter is automatically replaced by the paired Jack value to generate a new command. As a result, the `echo Jack` command is run.
        # 
        # You can specify 0 to 10 custom parameters. Take note of the following:
        # 
        # *   The key of a custom parameter can be up to 64 characters in length, and cannot be an empty string.
        # *   The value of a custom parameter can be an empty string.
        # *   If you want to retain a command, make sure that the command after Base64 encoding, including custom parameters and original command content, does not exceed 18 KB in size. If you do not want to retain the command, make sure that the command after Base64 encoding does not exceed 24 KB in size. You can set `KeepCommand` to specify whether to retain the command.
        # *   The specified custom parameter names must be included in the custom parameter names that you specify when you create the command. You can use empty strings to represent the parameters that are not passed in.
        # 
        # This parameter is left empty by default, which indicates that the custom parameter feature is disabled.
        self.parameters_shrink = parameters_shrink
        # The mode to run the command. Valid values:
        # 
        # *   Once: runs the command immediately.
        # *   Period: runs the command based on a schedule. When set to `Period`, `Frequency` is required.
        # *   NextRebootOnly: runs the command the next time the instances is started.
        # *   EveryReboot: runs the command every time the instance is started.
        # 
        # Default value:
        # 
        # *   If you do not specify `Frequency`, the default value is `Once`.
        # *   If you specify `Frequency`, RepeatMode is set to `Period` regardless of whether a value is already specified.
        self.repeat_mode = repeat_mode
        # Indicates how the command task is stopped when a command execution is manually stopped or times out. Valid values:
        # 
        # Process: The process of the command is stopped. ProcessTree: The process tree of the command is stopped. In this case, the process of the command and all subprocesses are stopped.
        self.termination_mode = termination_mode
        # The timeout period for the command. Unit: seconds. A timeout error occurs if the command cannot be run because the process slows down or because a specific module or Cloud Assistant Agent does not exist. When the specified timeout period ends, the command process is forcefully terminated. Default value: 60.
        self.timeout = timeout
        # The username that you use to run the command. The name can be up to 255 characters in length. For Linux instances, the root user is used by default.
        self.username = username
        # The working path of the command. You can specify a custom path. Default path:
        # 
        # Linux instances: By default, the path is in the /home directory of the root user.
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
        # The ID of the execution.
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
        # The content of the file. The file must not exceed 32 KB in size after it is encoded in Base64.
        # 
        # *   If `ContentType` is set to `PlainText`, the value of Content is in plaintext.
        # *   If `ContentType` is set to `Base64`, the value of Content is Base64-encoded.
        # 
        # This parameter is required.
        self.content = content
        # The content type of the file. Valid values:
        # 
        # PlainText Base64 Default value: PlainText.
        self.content_type = content_type
        # The description of the file. The description can be up to 512 characters in length and can contain any characters.
        self.description = description
        # The user group of the file. This parameter takes effect only on Linux instances. Default value: root. The value can be up to 64 characters in length.
        # 
        # Note If you want to use a non-root user group, make sure that the user group exists in the instances.
        self.file_group = file_group
        # The permissions on the file. This parameter takes effect only on Linux instances. You can configure this parameter in the same way as you configure the chmod command.
        # 
        # Default value: 0644: the owner of the file has the read and write permission. The user group of the file and other users have read-only permission.
        self.file_mode = file_mode
        # The owner of the file. This parameter takes effect only on Linux instances. Default value: root.
        self.file_owner = file_owner
        # The file name. The name can be up to 255 characters in length and can contain any characters.
        # 
        # This parameter is required.
        self.name = name
        # The node list.
        # 
        # This parameter is required.
        self.node_id_list = node_id_list
        # Specifies whether to overwrite file with the same name in the destination directory.
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.overwrite = overwrite
        # The directory in the Lingjun node to which the file is sent. If the specified directory does not exist, the system creates the directory automatically.
        # 
        # This parameter is required.
        self.target_dir = target_dir
        # The timeout period for the file sending task. Unit: seconds.
        # 
        # *   A timeout error occurs when a file cannot be sent because the process slows down or because a specific module or Cloud Assistant Agent does not exist.
        # *   If the specified timeout period is less than 10 seconds, the system sets the timeout period to 10 seconds to ensure that the file can be sent.
        # 
        # Default value: 60.
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
        # The content of the file. The file must not exceed 32 KB in size after it is encoded in Base64.
        # 
        # *   If `ContentType` is set to `PlainText`, the value of Content is in plaintext.
        # *   If `ContentType` is set to `Base64`, the value of Content is Base64-encoded.
        # 
        # This parameter is required.
        self.content = content
        # The content type of the file. Valid values:
        # 
        # PlainText Base64 Default value: PlainText.
        self.content_type = content_type
        # The description of the file. The description can be up to 512 characters in length and can contain any characters.
        self.description = description
        # The user group of the file. This parameter takes effect only on Linux instances. Default value: root. The value can be up to 64 characters in length.
        # 
        # Note If you want to use a non-root user group, make sure that the user group exists in the instances.
        self.file_group = file_group
        # The permissions on the file. This parameter takes effect only on Linux instances. You can configure this parameter in the same way as you configure the chmod command.
        # 
        # Default value: 0644: the owner of the file has the read and write permission. The user group of the file and other users have read-only permission.
        self.file_mode = file_mode
        # The owner of the file. This parameter takes effect only on Linux instances. Default value: root.
        self.file_owner = file_owner
        # The file name. The name can be up to 255 characters in length and can contain any characters.
        # 
        # This parameter is required.
        self.name = name
        # The node list.
        # 
        # This parameter is required.
        self.node_id_list_shrink = node_id_list_shrink
        # Specifies whether to overwrite file with the same name in the destination directory.
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.overwrite = overwrite
        # The directory in the Lingjun node to which the file is sent. If the specified directory does not exist, the system creates the directory automatically.
        # 
        # This parameter is required.
        self.target_dir = target_dir
        # The timeout period for the file sending task. Unit: seconds.
        # 
        # *   A timeout error occurs when a file cannot be sent because the process slows down or because a specific module or Cloud Assistant Agent does not exist.
        # *   If the specified timeout period is less than 10 seconds, the system sets the timeout period to 10 seconds to ensure that the file can be sent.
        # 
        # Default value: 60.
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
        # The ID of the execution.
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
        # The node ID.
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
        # The node group ID.
        self.node_group_id = node_group_id
        # The nodes.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The node groups.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The node groups.
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
        # The request ID.
        self.request_id = request_id
        # The job ID.
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
        # The execution ID.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # The nodes.
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
        # The execution ID.
        # 
        # This parameter is required.
        self.invoke_id = invoke_id
        # The nodes.
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
        # The request ID.
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
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The nodes.
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
        # Specifies whether to allow skipping failed nodes. Default value: False.
        self.ignore_failed_node_tasks = ignore_failed_node_tasks
        # The nodes.
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
        # The request ID.
        self.request_id = request_id
        # The task ID.
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
        # The tag key.
        self.key = key
        # The tag value.
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
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # Valid values:
        # 
        # *   Node
        # *   Vcc
        # *   Cluster
        # *   Vpd
        # *   Subnet
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags.
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
        # The request ID.
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
        # Specifies whether to remove all tags. This parameter takes effect only when TagKey.N is not specified. Valid values:
        # 
        # *   True
        # *   False
        # 
        # Default value: false.
        self.all = all
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The resource type.
        # 
        # Valid values:
        # 
        # *   Node
        # *   Cluster
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys.
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
        # The request ID.
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
        file_system_mount_enabled: bool = None,
        image_id: str = None,
        key_pair_name: str = None,
        login_password: str = None,
        new_node_group_name: str = None,
        node_group_id: str = None,
        user_data: str = None,
    ):
        # Whether file storage mounting is supported
        self.file_system_mount_enabled = file_system_mount_enabled
        # The default image ID of the node group. If not set, it will not change.
        self.image_id = image_id
        # Key pair name.
        self.key_pair_name = key_pair_name
        # Login password for machines within the node group
        self.login_password = login_password
        # Node group name
        self.new_node_group_name = new_node_group_name
        # Node group ID
        self.node_group_id = node_group_id
        # User-defined script
        self.user_data = user_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_system_mount_enabled is not None:
            result['FileSystemMountEnabled'] = self.file_system_mount_enabled
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name
        if self.login_password is not None:
            result['LoginPassword'] = self.login_password
        if self.new_node_group_name is not None:
            result['NewNodeGroupName'] = self.new_node_group_name
        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id
        if self.user_data is not None:
            result['UserData'] = self.user_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemMountEnabled') is not None:
            self.file_system_mount_enabled = m.get('FileSystemMountEnabled')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')
        if m.get('LoginPassword') is not None:
            self.login_password = m.get('LoginPassword')
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


