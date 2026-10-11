# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class GetEgressProxyIpPoolAttributeResponseBody(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        create_time: str = None,
        description: str = None,
        egress_proxy_gateway_id: str = None,
        egress_proxy_ip_pool_id: str = None,
        egress_proxy_ip_pool_name: str = None,
        hash_factor: str = None,
        hash_header_name: str = None,
        request_id: str = None,
        scheduler: str = None,
        status: str = None,
        tags: List[main_models.GetEgressProxyIpPoolAttributeResponseBodyTags] = None,
        zone_mappings: List[main_models.GetEgressProxyIpPoolAttributeResponseBodyZoneMappings] = None,
    ):
        self.address_type = address_type
        self.create_time = create_time
        self.description = description
        self.egress_proxy_gateway_id = egress_proxy_gateway_id
        self.egress_proxy_ip_pool_id = egress_proxy_ip_pool_id
        self.egress_proxy_ip_pool_name = egress_proxy_ip_pool_name
        self.hash_factor = hash_factor
        self.hash_header_name = hash_header_name
        self.request_id = request_id
        self.scheduler = scheduler
        self.status = status
        self.tags = tags
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.zone_mappings:
            for v1 in self.zone_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_type is not None:
            result['AddressType'] = self.address_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_gateway_id is not None:
            result['EgressProxyGatewayId'] = self.egress_proxy_gateway_id

        if self.egress_proxy_ip_pool_id is not None:
            result['EgressProxyIpPoolId'] = self.egress_proxy_ip_pool_id

        if self.egress_proxy_ip_pool_name is not None:
            result['EgressProxyIpPoolName'] = self.egress_proxy_ip_pool_name

        if self.hash_factor is not None:
            result['HashFactor'] = self.hash_factor

        if self.hash_header_name is not None:
            result['HashHeaderName'] = self.hash_header_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k1 in self.zone_mappings:
                result['ZoneMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyGatewayId') is not None:
            self.egress_proxy_gateway_id = m.get('EgressProxyGatewayId')

        if m.get('EgressProxyIpPoolId') is not None:
            self.egress_proxy_ip_pool_id = m.get('EgressProxyIpPoolId')

        if m.get('EgressProxyIpPoolName') is not None:
            self.egress_proxy_ip_pool_name = m.get('EgressProxyIpPoolName')

        if m.get('HashFactor') is not None:
            self.hash_factor = m.get('HashFactor')

        if m.get('HashHeaderName') is not None:
            self.hash_header_name = m.get('HashHeaderName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetEgressProxyIpPoolAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.GetEgressProxyIpPoolAttributeResponseBodyZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class GetEgressProxyIpPoolAttributeResponseBodyZoneMappings(DaraModel):
    def __init__(
        self,
        ip_addresses: List[main_models.GetEgressProxyIpPoolAttributeResponseBodyZoneMappingsIpAddresses] = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.ip_addresses = ip_addresses
        self.v_switch_id = v_switch_id
        self.zone_id = zone_id

    def validate(self):
        if self.ip_addresses:
            for v1 in self.ip_addresses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpAddresses'] = []
        if self.ip_addresses is not None:
            for k1 in self.ip_addresses:
                result['IpAddresses'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_addresses = []
        if m.get('IpAddresses') is not None:
            for k1 in m.get('IpAddresses'):
                temp_model = main_models.GetEgressProxyIpPoolAttributeResponseBodyZoneMappingsIpAddresses()
                self.ip_addresses.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetEgressProxyIpPoolAttributeResponseBodyZoneMappingsIpAddresses(DaraModel):
    def __init__(
        self,
        eip_allocation_id: str = None,
        private_ipv_4address: str = None,
        public_ipv_4address: str = None,
    ):
        self.eip_allocation_id = eip_allocation_id
        self.private_ipv_4address = private_ipv_4address
        self.public_ipv_4address = public_ipv_4address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_allocation_id is not None:
            result['EipAllocationId'] = self.eip_allocation_id

        if self.private_ipv_4address is not None:
            result['PrivateIpv4Address'] = self.private_ipv_4address

        if self.public_ipv_4address is not None:
            result['PublicIpv4Address'] = self.public_ipv_4address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')

        if m.get('PrivateIpv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIpv4Address')

        if m.get('PublicIpv4Address') is not None:
            self.public_ipv_4address = m.get('PublicIpv4Address')

        return self

class GetEgressProxyIpPoolAttributeResponseBodyTags(DaraModel):
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

