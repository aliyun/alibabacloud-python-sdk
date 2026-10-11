# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class CreateEgressProxyIpPoolRequest(DaraModel):
    def __init__(
        self,
        address_type: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        egress_proxy_gateway_id: str = None,
        egress_proxy_ip_pool_name: str = None,
        hash_factor: str = None,
        hash_header_name: str = None,
        scheduler: str = None,
        tag: List[main_models.CreateEgressProxyIpPoolRequestTag] = None,
        zone_mappings: List[main_models.CreateEgressProxyIpPoolRequestZoneMappings] = None,
    ):
        # This parameter is required.
        self.address_type = address_type
        self.client_token = client_token
        self.description = description
        self.dry_run = dry_run
        # This parameter is required.
        self.egress_proxy_gateway_id = egress_proxy_gateway_id
        # This parameter is required.
        self.egress_proxy_ip_pool_name = egress_proxy_ip_pool_name
        self.hash_factor = hash_factor
        self.hash_header_name = hash_header_name
        self.scheduler = scheduler
        self.tag = tag
        # This parameter is required.
        self.zone_mappings = zone_mappings

    def validate(self):
        if self.tag:
            for v1 in self.tag:
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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_gateway_id is not None:
            result['EgressProxyGatewayId'] = self.egress_proxy_gateway_id

        if self.egress_proxy_ip_pool_name is not None:
            result['EgressProxyIpPoolName'] = self.egress_proxy_ip_pool_name

        if self.hash_factor is not None:
            result['HashFactor'] = self.hash_factor

        if self.hash_header_name is not None:
            result['HashHeaderName'] = self.hash_header_name

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        result['ZoneMappings'] = []
        if self.zone_mappings is not None:
            for k1 in self.zone_mappings:
                result['ZoneMappings'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressType') is not None:
            self.address_type = m.get('AddressType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyGatewayId') is not None:
            self.egress_proxy_gateway_id = m.get('EgressProxyGatewayId')

        if m.get('EgressProxyIpPoolName') is not None:
            self.egress_proxy_ip_pool_name = m.get('EgressProxyIpPoolName')

        if m.get('HashFactor') is not None:
            self.hash_factor = m.get('HashFactor')

        if m.get('HashHeaderName') is not None:
            self.hash_header_name = m.get('HashHeaderName')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateEgressProxyIpPoolRequestTag()
                self.tag.append(temp_model.from_map(k1))

        self.zone_mappings = []
        if m.get('ZoneMappings') is not None:
            for k1 in m.get('ZoneMappings'):
                temp_model = main_models.CreateEgressProxyIpPoolRequestZoneMappings()
                self.zone_mappings.append(temp_model.from_map(k1))

        return self

class CreateEgressProxyIpPoolRequestZoneMappings(DaraModel):
    def __init__(
        self,
        ip_addresses: List[main_models.CreateEgressProxyIpPoolRequestZoneMappingsIpAddresses] = None,
        ip_count: int = None,
        v_switch_id: str = None,
        zone_id: str = None,
    ):
        self.ip_addresses = ip_addresses
        self.ip_count = ip_count
        # This parameter is required.
        self.v_switch_id = v_switch_id
        # This parameter is required.
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

        if self.ip_count is not None:
            result['IpCount'] = self.ip_count

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
                temp_model = main_models.CreateEgressProxyIpPoolRequestZoneMappingsIpAddresses()
                self.ip_addresses.append(temp_model.from_map(k1))

        if m.get('IpCount') is not None:
            self.ip_count = m.get('IpCount')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateEgressProxyIpPoolRequestZoneMappingsIpAddresses(DaraModel):
    def __init__(
        self,
        eip_allocation_id: str = None,
        private_ipv_4address: str = None,
    ):
        self.eip_allocation_id = eip_allocation_id
        self.private_ipv_4address = private_ipv_4address

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipAllocationId') is not None:
            self.eip_allocation_id = m.get('EipAllocationId')

        if m.get('PrivateIpv4Address') is not None:
            self.private_ipv_4address = m.get('PrivateIpv4Address')

        return self

class CreateEgressProxyIpPoolRequestTag(DaraModel):
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

