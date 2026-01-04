# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeVSwitchAttributesResponseBody(DaraModel):
    def __init__(
        self,
        available_ip_address_count: int = None,
        cidr_block: str = None,
        created_time: str = None,
        description: str = None,
        ens_region_id: str = None,
        ha_vip_ids: main_models.DescribeVSwitchAttributesResponseBodyHaVipIds = None,
        instance_ids: main_models.DescribeVSwitchAttributesResponseBodyInstanceIds = None,
        load_balancer_ids: main_models.DescribeVSwitchAttributesResponseBodyLoadBalancerIds = None,
        nat_gateway_ids: main_models.DescribeVSwitchAttributesResponseBodyNatGatewayIds = None,
        network_id: str = None,
        network_interface_ids: main_models.DescribeVSwitchAttributesResponseBodyNetworkInterfaceIds = None,
        request_id: str = None,
        status: str = None,
        v_switch_id: str = None,
        v_switch_name: str = None,
    ):
        # The number of available IP addresses in the VSwitch.
        self.available_ip_address_count = available_ip_address_count
        # The IPv4 CIDR block of the network.
        self.cidr_block = cidr_block
        # The creation time, in UTC format (yyyy-MM-ddTHH:mm:ssZ).
        self.created_time = created_time
        # The description of the VSwitch.
        self.description = description
        # The ENS node ID.
        self.ens_region_id = ens_region_id
        # A list of high-availability VIP instance IDs.
        self.ha_vip_ids = ha_vip_ids
        # A list of instance IDs.
        self.instance_ids = instance_ids
        # A list of load balancer instance IDs.
        self.load_balancer_ids = load_balancer_ids
        # A list of NAT gateway IDs.
        self.nat_gateway_ids = nat_gateway_ids
        # The network ID.
        self.network_id = network_id
        # A list of elastic network interface IDs.
        self.network_interface_ids = network_interface_ids
        # The request ID.
        self.request_id = request_id
        # The status of the VSwitch, as follows:
        # 
        # - Pending
        # - Available
        # - Releasing
        self.status = status
        # The ID of the VSwitch.
        self.v_switch_id = v_switch_id
        # The name of the VSwitch.
        self.v_switch_name = v_switch_name

    def validate(self):
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

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_ip_address_count is not None:
            result['AvailableIpAddressCount'] = self.available_ip_address_count

        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ha_vip_ids is not None:
            result['HaVipIds'] = self.ha_vip_ids.to_map()

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()

        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids.to_map()

        if self.nat_gateway_ids is not None:
            result['NatGatewayIds'] = self.nat_gateway_ids.to_map()

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.network_interface_ids is not None:
            result['NetworkInterfaceIds'] = self.network_interface_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_name is not None:
            result['VSwitchName'] = self.v_switch_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableIpAddressCount') is not None:
            self.available_ip_address_count = m.get('AvailableIpAddressCount')

        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('HaVipIds') is not None:
            temp_model = main_models.DescribeVSwitchAttributesResponseBodyHaVipIds()
            self.ha_vip_ids = temp_model.from_map(m.get('HaVipIds'))

        if m.get('InstanceIds') is not None:
            temp_model = main_models.DescribeVSwitchAttributesResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m.get('InstanceIds'))

        if m.get('LoadBalancerIds') is not None:
            temp_model = main_models.DescribeVSwitchAttributesResponseBodyLoadBalancerIds()
            self.load_balancer_ids = temp_model.from_map(m.get('LoadBalancerIds'))

        if m.get('NatGatewayIds') is not None:
            temp_model = main_models.DescribeVSwitchAttributesResponseBodyNatGatewayIds()
            self.nat_gateway_ids = temp_model.from_map(m.get('NatGatewayIds'))

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('NetworkInterfaceIds') is not None:
            temp_model = main_models.DescribeVSwitchAttributesResponseBodyNetworkInterfaceIds()
            self.network_interface_ids = temp_model.from_map(m.get('NetworkInterfaceIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchName') is not None:
            self.v_switch_name = m.get('VSwitchName')

        return self

class DescribeVSwitchAttributesResponseBodyNetworkInterfaceIds(DaraModel):
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

class DescribeVSwitchAttributesResponseBodyNatGatewayIds(DaraModel):
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

class DescribeVSwitchAttributesResponseBodyLoadBalancerIds(DaraModel):
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

class DescribeVSwitchAttributesResponseBodyInstanceIds(DaraModel):
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

class DescribeVSwitchAttributesResponseBodyHaVipIds(DaraModel):
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

