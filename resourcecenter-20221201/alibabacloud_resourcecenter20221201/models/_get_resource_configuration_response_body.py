# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class GetResourceConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        configuration: Dict[str, Any] = None,
        create_time: str = None,
        expire_time: str = None,
        ip_address_attributes: List[main_models.GetResourceConfigurationResponseBodyIpAddressAttributes] = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[main_models.GetResourceConfigurationResponseBodyTags] = None,
        zone_id: str = None,
    ):
        self.account_id = account_id
        self.configuration = configuration
        self.create_time = create_time
        self.expire_time = expire_time
        self.ip_address_attributes = ip_address_attributes
        self.ip_addresses = ip_addresses
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.resource_type = resource_type
        self.tags = tags
        self.zone_id = zone_id

    def validate(self):
        if self.ip_address_attributes:
            for v1 in self.ip_address_attributes:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.configuration is not None:
            result['Configuration'] = self.configuration

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        result['IpAddressAttributes'] = []
        if self.ip_address_attributes is not None:
            for k1 in self.ip_address_attributes:
                result['IpAddressAttributes'].append(k1.to_map() if k1 else None)

        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        self.ip_address_attributes = []
        if m.get('IpAddressAttributes') is not None:
            for k1 in m.get('IpAddressAttributes'):
                temp_model = main_models.GetResourceConfigurationResponseBodyIpAddressAttributes()
                self.ip_address_attributes.append(temp_model.from_map(k1))

        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetResourceConfigurationResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class GetResourceConfigurationResponseBodyTags(DaraModel):
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

class GetResourceConfigurationResponseBodyIpAddressAttributes(DaraModel):
    def __init__(
        self,
        ip_address: str = None,
        network_type: str = None,
        version: str = None,
    ):
        self.ip_address = ip_address
        self.network_type = network_type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

