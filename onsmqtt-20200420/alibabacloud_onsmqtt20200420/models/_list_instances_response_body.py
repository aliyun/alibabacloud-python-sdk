# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class ListInstancesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        instances: List[main_models.ListInstancesResponseBodyInstances] = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The response code.
        self.code = code
        # The list of instances.
        self.instances = instances
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.instances:
            for v1 in self.instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Instances'] = []
        if self.instances is not None:
            for k1 in self.instances:
                result['Instances'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.instances = []
        if m.get('Instances') is not None:
            for k1 in m.get('Instances'):
                temp_model = main_models.ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListInstancesResponseBodyInstances(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        expire_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: int = None,
        instance_type: int = None,
        kernel_version: str = None,
        mqtt_tags: List[main_models.ListInstancesResponseBodyInstancesMqttTags] = None,
        order_id: str = None,
        region_id: str = None,
        specific: str = None,
    ):
        # The time when the instance was created.
        self.create_time = create_time
        # The expiration time of the instance.
        self.expire_time = expire_time
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name
        # The instance status.
        # 
        # - 0: Preparing
        # 
        # - 5: In Service
        # 
        # - 7: Upgrading
        # 
        # - 15: Frozen
        # 
        # - 10: Released
        # 
        # - 1: Not Activated
        # 
        # - 2: Overdue
        # 
        # - 3: Expired
        self.instance_status = instance_status
        # The instance type:
        # 
        # - 0: Basic Edition
        # 
        # - 1: Platinum Edition
        # 
        # - 2: Pay-as-you-go
        # 
        # - 3: Subscription Lightweight
        # 
        # - 4: Professional Edition
        # 
        # - 5: Serverless Edition
        self.instance_type = instance_type
        # The Milvus version.
        self.kernel_version = kernel_version
        # The list of tags.
        self.mqtt_tags = mqtt_tags
        # The order ID.
        self.order_id = order_id
        # The region ID.
        self.region_id = region_id
        # The instance type of the Professional Edition instance.
        self.specific = specific

    def validate(self):
        if self.mqtt_tags:
            for v1 in self.mqtt_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.kernel_version is not None:
            result['KernelVersion'] = self.kernel_version

        result['MqttTags'] = []
        if self.mqtt_tags is not None:
            for k1 in self.mqtt_tags:
                result['MqttTags'].append(k1.to_map() if k1 else None)

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.specific is not None:
            result['Specific'] = self.specific

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('KernelVersion') is not None:
            self.kernel_version = m.get('KernelVersion')

        self.mqtt_tags = []
        if m.get('MqttTags') is not None:
            for k1 in m.get('MqttTags'):
                temp_model = main_models.ListInstancesResponseBodyInstancesMqttTags()
                self.mqtt_tags.append(temp_model.from_map(k1))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Specific') is not None:
            self.specific = m.get('Specific')

        return self

class ListInstancesResponseBodyInstancesMqttTags(DaraModel):
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

