# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class BatchGetResourceConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        resources: List[main_models.BatchGetResourceConfigurationsResponseBodyResources] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of resources.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.BatchGetResourceConfigurationsResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class BatchGetResourceConfigurationsResponseBodyResources(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        configuration: Dict[str, Any] = None,
        create_time: str = None,
        expire_time: str = None,
        ip_address_attributes: List[main_models.BatchGetResourceConfigurationsResponseBodyResourcesIpAddressAttributes] = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[main_models.BatchGetResourceConfigurationsResponseBodyResourcesTags] = None,
        zone_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The details of the resource configuration.
        self.configuration = configuration
        # The time when the resource was created.
        self.create_time = create_time
        # The expiration time of the resource.
        self.expire_time = expire_time
        # The properties of the IP addresses.
        self.ip_address_attributes = ip_address_attributes
        # The IP addresses.
        # 
        # > Whether this parameter is returned depends on the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses
        # The region ID of the resource.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type
        # The tags.
        self.tags = tags
        # The zone ID.
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
                temp_model = main_models.BatchGetResourceConfigurationsResponseBodyResourcesIpAddressAttributes()
                self.ip_address_attributes.append(temp_model.from_map(k1))

        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

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
                temp_model = main_models.BatchGetResourceConfigurationsResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class BatchGetResourceConfigurationsResponseBodyResourcesTags(DaraModel):
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

class BatchGetResourceConfigurationsResponseBodyResourcesIpAddressAttributes(DaraModel):
    def __init__(
        self,
        ip_address: str = None,
        network_type: str = None,
        version: str = None,
    ):
        # The IP address.
        self.ip_address = ip_address
        # The network type. Valid values:
        # 
        # - **Public**: Internet.
        # 
        # - **Private**: Private network.
        self.network_type = network_type
        # The version of the IP address.
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

