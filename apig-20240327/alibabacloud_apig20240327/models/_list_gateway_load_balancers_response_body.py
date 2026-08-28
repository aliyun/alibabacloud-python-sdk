# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class ListGatewayLoadBalancersResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListGatewayLoadBalancersResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.ListGatewayLoadBalancersResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListGatewayLoadBalancersResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.ListGatewayLoadBalancersResponseBodyDataItems] = None,
    ):
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListGatewayLoadBalancersResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        return self

class ListGatewayLoadBalancersResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        default_gateway_ingress: bool = None,
        edit_enable: bool = None,
        gateway_id: str = None,
        load_balancer_address: str = None,
        load_balancer_address_ip_version: str = None,
        load_balancer_address_type: str = None,
        load_balancer_available_status: str = None,
        load_balancer_id: str = None,
        load_balancer_mode: str = None,
        load_balancer_name: str = None,
        load_balancer_spec: str = None,
        load_balancer_status: str = None,
        load_balancer_type: str = None,
        load_balancer_zone_mappings: List[main_models.ListGatewayLoadBalancersResponseBodyDataItemsLoadBalancerZoneMappings] = None,
        ports: List[main_models.ListGatewayLoadBalancersResponseBodyDataItemsPorts] = None,
        service_weight: int = None,
        v_server_group_meta_info: str = None,
        virtual_server_group_list: List[main_models.ListGatewayLoadBalancersResponseBodyDataItemsVirtualServerGroupList] = None,
    ):
        self.default_gateway_ingress = default_gateway_ingress
        self.edit_enable = edit_enable
        self.gateway_id = gateway_id
        self.load_balancer_address = load_balancer_address
        self.load_balancer_address_ip_version = load_balancer_address_ip_version
        self.load_balancer_address_type = load_balancer_address_type
        self.load_balancer_available_status = load_balancer_available_status
        self.load_balancer_id = load_balancer_id
        self.load_balancer_mode = load_balancer_mode
        self.load_balancer_name = load_balancer_name
        self.load_balancer_spec = load_balancer_spec
        self.load_balancer_status = load_balancer_status
        self.load_balancer_type = load_balancer_type
        self.load_balancer_zone_mappings = load_balancer_zone_mappings
        self.ports = ports
        self.service_weight = service_weight
        self.v_server_group_meta_info = v_server_group_meta_info
        self.virtual_server_group_list = virtual_server_group_list

    def validate(self):
        if self.load_balancer_zone_mappings:
            for v1 in self.load_balancer_zone_mappings:
                 if v1:
                    v1.validate()
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()
        if self.virtual_server_group_list:
            for v1 in self.virtual_server_group_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_gateway_ingress is not None:
            result['defaultGatewayIngress'] = self.default_gateway_ingress

        if self.edit_enable is not None:
            result['editEnable'] = self.edit_enable

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.load_balancer_address is not None:
            result['loadBalancerAddress'] = self.load_balancer_address

        if self.load_balancer_address_ip_version is not None:
            result['loadBalancerAddressIpVersion'] = self.load_balancer_address_ip_version

        if self.load_balancer_address_type is not None:
            result['loadBalancerAddressType'] = self.load_balancer_address_type

        if self.load_balancer_available_status is not None:
            result['loadBalancerAvailableStatus'] = self.load_balancer_available_status

        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id

        if self.load_balancer_mode is not None:
            result['loadBalancerMode'] = self.load_balancer_mode

        if self.load_balancer_name is not None:
            result['loadBalancerName'] = self.load_balancer_name

        if self.load_balancer_spec is not None:
            result['loadBalancerSpec'] = self.load_balancer_spec

        if self.load_balancer_status is not None:
            result['loadBalancerStatus'] = self.load_balancer_status

        if self.load_balancer_type is not None:
            result['loadBalancerType'] = self.load_balancer_type

        result['loadBalancerZoneMappings'] = []
        if self.load_balancer_zone_mappings is not None:
            for k1 in self.load_balancer_zone_mappings:
                result['loadBalancerZoneMappings'].append(k1.to_map() if k1 else None)

        result['ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['ports'].append(k1.to_map() if k1 else None)

        if self.service_weight is not None:
            result['serviceWeight'] = self.service_weight

        if self.v_server_group_meta_info is not None:
            result['vServerGroupMetaInfo'] = self.v_server_group_meta_info

        result['virtualServerGroupList'] = []
        if self.virtual_server_group_list is not None:
            for k1 in self.virtual_server_group_list:
                result['virtualServerGroupList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('defaultGatewayIngress') is not None:
            self.default_gateway_ingress = m.get('defaultGatewayIngress')

        if m.get('editEnable') is not None:
            self.edit_enable = m.get('editEnable')

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('loadBalancerAddress') is not None:
            self.load_balancer_address = m.get('loadBalancerAddress')

        if m.get('loadBalancerAddressIpVersion') is not None:
            self.load_balancer_address_ip_version = m.get('loadBalancerAddressIpVersion')

        if m.get('loadBalancerAddressType') is not None:
            self.load_balancer_address_type = m.get('loadBalancerAddressType')

        if m.get('loadBalancerAvailableStatus') is not None:
            self.load_balancer_available_status = m.get('loadBalancerAvailableStatus')

        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')

        if m.get('loadBalancerMode') is not None:
            self.load_balancer_mode = m.get('loadBalancerMode')

        if m.get('loadBalancerName') is not None:
            self.load_balancer_name = m.get('loadBalancerName')

        if m.get('loadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('loadBalancerSpec')

        if m.get('loadBalancerStatus') is not None:
            self.load_balancer_status = m.get('loadBalancerStatus')

        if m.get('loadBalancerType') is not None:
            self.load_balancer_type = m.get('loadBalancerType')

        self.load_balancer_zone_mappings = []
        if m.get('loadBalancerZoneMappings') is not None:
            for k1 in m.get('loadBalancerZoneMappings'):
                temp_model = main_models.ListGatewayLoadBalancersResponseBodyDataItemsLoadBalancerZoneMappings()
                self.load_balancer_zone_mappings.append(temp_model.from_map(k1))

        self.ports = []
        if m.get('ports') is not None:
            for k1 in m.get('ports'):
                temp_model = main_models.ListGatewayLoadBalancersResponseBodyDataItemsPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('serviceWeight') is not None:
            self.service_weight = m.get('serviceWeight')

        if m.get('vServerGroupMetaInfo') is not None:
            self.v_server_group_meta_info = m.get('vServerGroupMetaInfo')

        self.virtual_server_group_list = []
        if m.get('virtualServerGroupList') is not None:
            for k1 in m.get('virtualServerGroupList'):
                temp_model = main_models.ListGatewayLoadBalancersResponseBodyDataItemsVirtualServerGroupList()
                self.virtual_server_group_list.append(temp_model.from_map(k1))

        return self

class ListGatewayLoadBalancersResponseBodyDataItemsVirtualServerGroupList(DaraModel):
    def __init__(
        self,
        listeners: List[main_models.ListGatewayLoadBalancersResponseBodyDataItemsVirtualServerGroupListListeners] = None,
        virtual_service_group_id: str = None,
        virtual_service_group_name: str = None,
    ):
        self.listeners = listeners
        self.virtual_service_group_id = virtual_service_group_id
        self.virtual_service_group_name = virtual_service_group_name

    def validate(self):
        if self.listeners:
            for v1 in self.listeners:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['listeners'] = []
        if self.listeners is not None:
            for k1 in self.listeners:
                result['listeners'].append(k1.to_map() if k1 else None)

        if self.virtual_service_group_id is not None:
            result['virtualServiceGroupId'] = self.virtual_service_group_id

        if self.virtual_service_group_name is not None:
            result['virtualServiceGroupName'] = self.virtual_service_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.listeners = []
        if m.get('listeners') is not None:
            for k1 in m.get('listeners'):
                temp_model = main_models.ListGatewayLoadBalancersResponseBodyDataItemsVirtualServerGroupListListeners()
                self.listeners.append(temp_model.from_map(k1))

        if m.get('virtualServiceGroupId') is not None:
            self.virtual_service_group_id = m.get('virtualServiceGroupId')

        if m.get('virtualServiceGroupName') is not None:
            self.virtual_service_group_name = m.get('virtualServiceGroupName')

        return self

class ListGatewayLoadBalancersResponseBodyDataItemsVirtualServerGroupListListeners(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class ListGatewayLoadBalancersResponseBodyDataItemsPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        self.port = port
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['port'] = self.port

        if self.protocol is not None:
            result['protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        return self

class ListGatewayLoadBalancersResponseBodyDataItemsLoadBalancerZoneMappings(DaraModel):
    def __init__(
        self,
        load_balancer_addresses: List[main_models.ListGatewayLoadBalancersResponseBodyDataItemsLoadBalancerZoneMappingsLoadBalancerAddresses] = None,
        status: str = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.load_balancer_addresses = load_balancer_addresses
        self.status = status
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.load_balancer_addresses:
            for v1 in self.load_balancer_addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['loadBalancerAddresses'] = []
        if self.load_balancer_addresses is not None:
            for k1 in self.load_balancer_addresses:
                result['loadBalancerAddresses'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['status'] = self.status

        if self.v_switch_id is not None:
            result['vSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['zoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.load_balancer_addresses = []
        if m.get('loadBalancerAddresses') is not None:
            for k1 in m.get('loadBalancerAddresses'):
                temp_model = main_models.ListGatewayLoadBalancersResponseBodyDataItemsLoadBalancerZoneMappingsLoadBalancerAddresses()
                self.load_balancer_addresses.append(temp_model.from_map(k1))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('vSwitchId') is not None:
            self.v_switch_id = m.get('vSwitchId')

        if m.get('zoneId') is not None:
            self.zone_id = m.get('zoneId')

        return self

class ListGatewayLoadBalancersResponseBodyDataItemsLoadBalancerZoneMappingsLoadBalancerAddresses(DaraModel):
    def __init__(
        self,
        allocation_id: str = None,
        eni_id: str = None,
        ipv_4local_addresses: List[str] = None,
        ipv_6address: str = None,
        ipv_6local_addresses: List[str] = None,
        private_ipv_4address: str = None,
        private_ipv_4hc_status: str = None,
        private_ipv_6hc_status: str = None,
        public_ipv_4address: str = None,
    ):
        self.allocation_id = allocation_id
        self.eni_id = eni_id
        self.ipv_4local_addresses = ipv_4local_addresses
        self.ipv_6address = ipv_6address
        self.ipv_6local_addresses = ipv_6local_addresses
        self.private_ipv_4address = private_ipv_4address
        self.private_ipv_4hc_status = private_ipv_4hc_status
        self.private_ipv_6hc_status = private_ipv_6hc_status
        self.public_ipv_4address = public_ipv_4address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_id is not None:
            result['allocationId'] = self.allocation_id

        if self.eni_id is not None:
            result['eniId'] = self.eni_id

        if self.ipv_4local_addresses is not None:
            result['ipv4LocalAddresses'] = self.ipv_4local_addresses

        if self.ipv_6address is not None:
            result['ipv6Address'] = self.ipv_6address

        if self.ipv_6local_addresses is not None:
            result['ipv6LocalAddresses'] = self.ipv_6local_addresses

        if self.private_ipv_4address is not None:
            result['privateIPv4Address'] = self.private_ipv_4address

        if self.private_ipv_4hc_status is not None:
            result['privateIPv4HcStatus'] = self.private_ipv_4hc_status

        if self.private_ipv_6hc_status is not None:
            result['privateIPv6HcStatus'] = self.private_ipv_6hc_status

        if self.public_ipv_4address is not None:
            result['publicIPv4Address'] = self.public_ipv_4address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allocationId') is not None:
            self.allocation_id = m.get('allocationId')

        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')

        if m.get('ipv4LocalAddresses') is not None:
            self.ipv_4local_addresses = m.get('ipv4LocalAddresses')

        if m.get('ipv6Address') is not None:
            self.ipv_6address = m.get('ipv6Address')

        if m.get('ipv6LocalAddresses') is not None:
            self.ipv_6local_addresses = m.get('ipv6LocalAddresses')

        if m.get('privateIPv4Address') is not None:
            self.private_ipv_4address = m.get('privateIPv4Address')

        if m.get('privateIPv4HcStatus') is not None:
            self.private_ipv_4hc_status = m.get('privateIPv4HcStatus')

        if m.get('privateIPv6HcStatus') is not None:
            self.private_ipv_6hc_status = m.get('privateIPv6HcStatus')

        if m.get('publicIPv4Address') is not None:
            self.public_ipv_4address = m.get('publicIPv4Address')

        return self

