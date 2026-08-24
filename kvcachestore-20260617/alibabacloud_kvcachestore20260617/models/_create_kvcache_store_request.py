# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_kvcachestore20260617 import models as main_models
from darabonba.model import DaraModel

class CreateKVCacheStoreRequest(DaraModel):
    def __init__(
        self,
        capacity: int = None,
        client_token: str = None,
        description: str = None,
        hpn_zone: str = None,
        name: str = None,
        payment_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tag: List[main_models.CreateKVCacheStoreRequestTag] = None,
        zone_id: str = None,
    ):
        # The storage capacity in GiB. The minimum capacity is 300 TiB (307200 GiB), and the capacity is scaled in increments of 300 TiB.
        # 
        # This parameter is required.
        self.capacity = capacity
        # The client token used to ensure idempotence of the request. The token can be up to 64 characters in length. Use a UUID.
        self.client_token = client_token
        # The KVCacheStore description. The description must be 2 to 256 characters in length and cannot start with http:// or https://. Default value: empty.
        self.description = description
        # The HPN cluster ID, which is used to create an affinity scheduling relationship between the KVCacheStore and the specified HPN cluster. After creation, the KVCacheStore may have affinity relationships with multiple HPN clusters based on network topology. You can call GetKVCacheStore to query the available HPN clusters.
        # 
        # This parameter is required.
        self.hpn_zone = hpn_zone
        # The KVCacheStore name. The name must be 2 to 128 characters in length and can contain characters from the Unicode letter category (including English and Chinese characters) and digits. The name can contain colons (:), underscores (_), periods (.), and hyphens (-). If this parameter is not specified, the default value is the KVCacheStore ID.
        self.name = name
        # The billing method. Valid values: POSTPAY (pay-as-you-go). Default value: POSTPAY.
        self.payment_type = payment_type
        # The region ID in which to create the KVCacheStore. You can call DescribeRegions to query the list of available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The list of resource tag key-value pairs. A maximum of 20 tags are supported. This overrides the parent TagDTO type and uses the same Tag type as the Get/List response.
        self.tag = tag
        # The zone ID. You can call DescribeZones to query the list of zones in the specified region.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.hpn_zone is not None:
            result['HpnZone'] = self.hpn_zone

        if self.name is not None:
            result['Name'] = self.name

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HpnZone') is not None:
            self.hpn_zone = m.get('HpnZone')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateKVCacheStoreRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateKVCacheStoreRequestTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the resource.
        self.tag_key = tag_key
        # The tag value of the resource.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

