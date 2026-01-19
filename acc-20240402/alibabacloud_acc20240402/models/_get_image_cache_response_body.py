# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_acc20240402 import models as main_models
from darabonba.model import DaraModel

class GetImageCacheResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        events: List[main_models.GetImageCacheResponseBodyEvents] = None,
        image_cache_id: str = None,
        image_cache_name: str = None,
        images: List[str] = None,
        network_config: main_models.GetImageCacheResponseBodyNetworkConfig = None,
        payment_type: str = None,
        ready_time: str = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        size: int = None,
        status: str = None,
        tags: List[main_models.GetImageCacheResponseBodyTags] = None,
    ):
        self.create_time = create_time
        self.events = events
        self.image_cache_id = image_cache_id
        self.image_cache_name = image_cache_name
        self.images = images
        self.network_config = network_config
        self.payment_type = payment_type
        self.ready_time = ready_time
        self.region_id = region_id
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.size = size
        self.status = status
        self.tags = tags

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()
        if self.network_config:
            self.network_config.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.image_cache_id is not None:
            result['ImageCacheId'] = self.image_cache_id

        if self.image_cache_name is not None:
            result['ImageCacheName'] = self.image_cache_name

        if self.images is not None:
            result['Images'] = self.images

        if self.network_config is not None:
            result['NetworkConfig'] = self.network_config.to_map()

        if self.payment_type is not None:
            result['PaymentType'] = self.payment_type

        if self.ready_time is not None:
            result['ReadyTime'] = self.ready_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.GetImageCacheResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('ImageCacheId') is not None:
            self.image_cache_id = m.get('ImageCacheId')

        if m.get('ImageCacheName') is not None:
            self.image_cache_name = m.get('ImageCacheName')

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('NetworkConfig') is not None:
            temp_model = main_models.GetImageCacheResponseBodyNetworkConfig()
            self.network_config = temp_model.from_map(m.get('NetworkConfig'))

        if m.get('PaymentType') is not None:
            self.payment_type = m.get('PaymentType')

        if m.get('ReadyTime') is not None:
            self.ready_time = m.get('ReadyTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetImageCacheResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetImageCacheResponseBodyTags(DaraModel):
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

class GetImageCacheResponseBodyNetworkConfig(DaraModel):
    def __init__(
        self,
        eip_instance: main_models.GetImageCacheResponseBodyNetworkConfigEipInstance = None,
        security_group_id: str = None,
        v_switch_ids: List[str] = None,
    ):
        self.eip_instance = eip_instance
        self.security_group_id = security_group_id
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.eip_instance:
            self.eip_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_instance is not None:
            result['EipInstance'] = self.eip_instance.to_map()

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipInstance') is not None:
            temp_model = main_models.GetImageCacheResponseBodyNetworkConfigEipInstance()
            self.eip_instance = temp_model.from_map(m.get('EipInstance'))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class GetImageCacheResponseBodyNetworkConfigEipInstance(DaraModel):
    def __init__(
        self,
        auto_create: bool = None,
        bandwidth: int = None,
        instance_id: str = None,
    ):
        self.auto_create = auto_create
        self.bandwidth = bandwidth
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_create is not None:
            result['AutoCreate'] = self.auto_create

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreate') is not None:
            self.auto_create = m.get('AutoCreate')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

class GetImageCacheResponseBodyEvents(DaraModel):
    def __init__(
        self,
        count: int = None,
        first_timestamp: str = None,
        last_timestamp: str = None,
        message: str = None,
        name: str = None,
        reason: str = None,
        type: str = None,
    ):
        self.count = count
        self.first_timestamp = first_timestamp
        self.last_timestamp = last_timestamp
        self.message = message
        self.name = name
        self.reason = reason
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp

        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp

        if self.message is not None:
            result['Message'] = self.message

        if self.name is not None:
            result['Name'] = self.name

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')

        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

