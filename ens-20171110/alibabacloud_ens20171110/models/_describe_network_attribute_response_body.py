# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeNetworkAttributeResponseBody(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        cloud_resources: main_models.DescribeNetworkAttributeResponseBodyCloudResources = None,
        created_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        gateway_route_table_id: str = None,
        ha_vip_ids: main_models.DescribeNetworkAttributeResponseBodyHaVipIds = None,
        instance_ids: main_models.DescribeNetworkAttributeResponseBodyInstanceIds = None,
        load_balancer_ids: main_models.DescribeNetworkAttributeResponseBodyLoadBalancerIds = None,
        nat_gateway_ids: main_models.DescribeNetworkAttributeResponseBodyNatGatewayIds = None,
        network_acl_id: str = None,
        network_id: str = None,
        network_interface_ids: main_models.DescribeNetworkAttributeResponseBodyNetworkInterfaceIds = None,
        network_name: str = None,
        request_id: str = None,
        route_table_id: str = None,
        route_table_ids: main_models.DescribeNetworkAttributeResponseBodyRouteTableIds = None,
        router_table_id: str = None,
        secondary_cidr_blocks: main_models.DescribeNetworkAttributeResponseBodySecondaryCidrBlocks = None,
        status: str = None,
        v_switch_ids: main_models.DescribeNetworkAttributeResponseBodyVSwitchIds = None,
    ):
        # The IPv4 CIDR block of the network.
        self.cidr_block = cidr_block
        # The list of resources in the network.
        self.cloud_resources = cloud_resources
        # The time when the network was created. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time is displayed in UTC.
        self.created_time = created_time
        # The description of the network.
        self.description = description
        # The ID of the edge node.
        self.ens_region_id = ens_region_id
        # The ID of the gateway route table.
        self.gateway_route_table_id = gateway_route_table_id
        # List of HaVipIds.
        self.ha_vip_ids = ha_vip_ids
        # The instance IDs.
        self.instance_ids = instance_ids
        # List of ELB instances.
        self.load_balancer_ids = load_balancer_ids
        # List of NAT Gateways.
        self.nat_gateway_ids = nat_gateway_ids
        # The ID of the network access control list (ACL).
        self.network_acl_id = network_acl_id
        # The ID of the network.
        self.network_id = network_id
        # A list of multicast source IDs.
        self.network_interface_ids = network_interface_ids
        # The name of the network.
        self.network_name = network_name
        # The request ID.
        self.request_id = request_id
        # The ID of the route table.
        self.route_table_id = route_table_id
        # List of routing table IDs.
        self.route_table_ids = route_table_ids
        # The ID of the route table.
        self.router_table_id = router_table_id
        self.secondary_cidr_blocks = secondary_cidr_blocks
        # The status of the network. Valid values:
        # 
        # *   Pending
        # *   Available
        self.status = status
        # The list of vSwitches in the network.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.cloud_resources:
            self.cloud_resources.validate()
        if self.ha_vip_ids:
            self.ha_vip_ids.validate()
        if self.instance_ids:
            self.instance_ids.validate()
        if self.load_balancer_ids:
            self.load_balancer_ids.validate()
        if self.nat_gateway_ids:
            self.nat_gateway_ids.validate()
        if self.network_interface_ids:
            self.network_interface_ids.validate()
        if self.route_table_ids:
            self.route_table_ids.validate()
        if self.secondary_cidr_blocks:
            self.secondary_cidr_blocks.validate()
        if self.v_switch_ids:
            self.v_switch_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.cloud_resources is not None:
            result['CloudResources'] = self.cloud_resources.to_map()

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.gateway_route_table_id is not None:
            result['GatewayRouteTableId'] = self.gateway_route_table_id

        if self.ha_vip_ids is not None:
            result['HaVipIds'] = self.ha_vip_ids.to_map()

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()

        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids.to_map()

        if self.nat_gateway_ids is not None:
            result['NatGatewayIds'] = self.nat_gateway_ids.to_map()

        if self.network_acl_id is not None:
            result['NetworkAclId'] = self.network_acl_id

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids.to_map()

        if self.network_name is not None:
            result['NetworkName'] = self.network_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.route_table_ids is not None:
            result['RouteTableIds'] = self.route_table_ids.to_map()

        if self.router_table_id is not None:
            result['RouterTableId'] = self.router_table_id

        if self.secondary_cidr_blocks is not None:
            result['SecondaryCidrBlocks'] = self.secondary_cidr_blocks.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CloudResources') is not None:
            temp_model = main_models.DescribeNetworkAttributeResponseBodyCloudResources()
            self.cloud_resources = temp_model.from_map(m.get('CloudResources'))

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('GatewayRouteTableId') is not None:
            self.gateway_route_table_id = m.get('GatewayRouteTableId')

        if m.get('HaVipIds') is not None:
            temp_model = main_models.DescribeNetworkAttributeResponseBodyHaVipIds()
            self.ha_vip_ids = temp_model.from_map(m.get('HaVipIds'))

        if m.get('InstanceIds') is not None:
            temp_model = main_models.DescribeNetworkAttributeResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m.get('InstanceIds'))

        if m.get('LoadBalancerIds') is not None:
            temp_model = main_models.DescribeNetworkAttributeResponseBodyLoadBalancerIds()
            self.load_balancer_ids = temp_model.from_map(m.get('LoadBalancerIds'))

        if m.get('NatGatewayIds') is not None:
            temp_model = main_models.DescribeNetworkAttributeResponseBodyNatGatewayIds()
            self.nat_gateway_ids = temp_model.from_map(m.get('NatGatewayIds'))

        if m.get('NetworkAclId') is not None:
            self.network_acl_id = m.get('NetworkAclId')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkInterfaceIds') is not None:
            temp_model = main_models.DescribeNetworkAttributeResponseBodyNetworkInterfaceIds()
            self.network_interface_ids = temp_model.from_map(m.get('NetworkInterfaceIds'))

        if m.get('NetworkName') is not None:
            self.network_name = m.get('NetworkName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('RouteTableIds') is not None:
            temp_model = main_models.DescribeNetworkAttributeResponseBodyRouteTableIds()
            self.route_table_ids = temp_model.from_map(m.get('RouteTableIds'))

        if m.get('RouterTableId') is not None:
            self.router_table_id = m.get('RouterTableId')

        if m.get('SecondaryCidrBlocks') is not None:
            temp_model = main_models.DescribeNetworkAttributeResponseBodySecondaryCidrBlocks()
            self.secondary_cidr_blocks = temp_model.from_map(m.get('SecondaryCidrBlocks'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchIds') is not None:
            temp_model = main_models.DescribeNetworkAttributeResponseBodyVSwitchIds()
            self.v_switch_ids = temp_model.from_map(m.get('VSwitchIds'))

        return self

class DescribeNetworkAttributeResponseBodyVSwitchIds(DaraModel):
    def __init__(
        self,
        v_switch_id: List[str] = None,
    ):
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeNetworkAttributeResponseBodySecondaryCidrBlocks(DaraModel):
    def __init__(
        self,
        secondary_cidr_block: List[str] = None,
    ):
        self.secondary_cidr_block = secondary_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.secondary_cidr_block is not None:
            result['SecondaryCidrBlock'] = self.secondary_cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecondaryCidrBlock') is not None:
            self.secondary_cidr_block = m.get('SecondaryCidrBlock')

        return self

class DescribeNetworkAttributeResponseBodyRouteTableIds(DaraModel):
    def __init__(
        self,
        route_table_id: List[str] = None,
    ):
        self.route_table_id = route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        return self

class DescribeNetworkAttributeResponseBodyNetworkInterfaceIds(DaraModel):
    def __init__(
        self,
        network_interface_id: List[str] = None,
    ):
        self.network_interface_id = network_interface_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_interface_id is not None:
            result['NetworkInterfaceId'] = self.network_interface_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkInterfaceId') is not None:
            self.network_interface_id = m.get('NetworkInterfaceId')

        return self

class DescribeNetworkAttributeResponseBodyNatGatewayIds(DaraModel):
    def __init__(
        self,
        nat_gateway_id: List[str] = None,
    ):
        self.nat_gateway_id = nat_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        return self

class DescribeNetworkAttributeResponseBodyLoadBalancerIds(DaraModel):
    def __init__(
        self,
        load_balancer_id: List[str] = None,
    ):
        self.load_balancer_id = load_balancer_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        return self

class DescribeNetworkAttributeResponseBodyInstanceIds(DaraModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class DescribeNetworkAttributeResponseBodyHaVipIds(DaraModel):
    def __init__(
        self,
        ha_vip_id: List[str] = None,
    ):
        self.ha_vip_id = ha_vip_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha_vip_id is not None:
            result['HaVipId'] = self.ha_vip_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVipId') is not None:
            self.ha_vip_id = m.get('HaVipId')

        return self

class DescribeNetworkAttributeResponseBodyCloudResources(DaraModel):
    def __init__(
        self,
        cloud_resource_set_type: List[main_models.DescribeNetworkAttributeResponseBodyCloudResourcesCloudResourceSetType] = None,
    ):
        self.cloud_resource_set_type = cloud_resource_set_type

    def validate(self):
        if self.cloud_resource_set_type:
            for v1 in self.cloud_resource_set_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudResourceSetType'] = []
        if self.cloud_resource_set_type is not None:
            for k1 in self.cloud_resource_set_type:
                result['CloudResourceSetType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_resource_set_type = []
        if m.get('CloudResourceSetType') is not None:
            for k1 in m.get('CloudResourceSetType'):
                temp_model = main_models.DescribeNetworkAttributeResponseBodyCloudResourcesCloudResourceSetType()
                self.cloud_resource_set_type.append(temp_model.from_map(k1))

        return self

class DescribeNetworkAttributeResponseBodyCloudResourcesCloudResourceSetType(DaraModel):
    def __init__(
        self,
        resource_count: int = None,
        resource_type: str = None,
    ):
        # The number of resources in the network.
        self.resource_count = resource_count
        # The resource type. VSwitch.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_count is not None:
            result['ResourceCount'] = self.resource_count

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceCount') is not None:
            self.resource_count = m.get('ResourceCount')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

