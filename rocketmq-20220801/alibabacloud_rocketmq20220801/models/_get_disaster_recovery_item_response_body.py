# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class GetDisasterRecoveryItemResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetDisasterRecoveryItemResponseBodyData = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial. This parameter is returned only if the access is denied because the Resource Access Management (RAM) user does not have the required permissions.
        self.access_denied_detail = access_denied_detail
        # The error code.
        self.code = code
        # The data returned.
        self.data = data
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # Request ID
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['accessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.dynamic_code is not None:
            result['dynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['dynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessDeniedDetail') is not None:
            self.access_denied_detail = m.get('accessDeniedDetail')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetDisasterRecoveryItemResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dynamicCode') is not None:
            self.dynamic_code = m.get('dynamicCode')

        if m.get('dynamicMessage') is not None:
            self.dynamic_message = m.get('dynamicMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetDisasterRecoveryItemResponseBodyData(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        ext_info: Dict[str, str] = None,
        item_id: int = None,
        item_status: str = None,
        plan_id: int = None,
        topics: List[main_models.GetDisasterRecoveryItemResponseBodyDataTopics] = None,
        update_time: str = None,
    ):
        # The time when the topic mapping task was created.
        self.create_time = create_time
        # Additional Information
        self.ext_info = ext_info
        # The ID of the topic mapping
        self.item_id = item_id
        # The topic mapping task status.
        self.item_status = item_status
        # The ID of the global message backup plan.
        self.plan_id = plan_id
        # Topics included in the backup mapping
        self.topics = topics
        # The time when the topic mapping task was last updated.
        self.update_time = update_time

    def validate(self):
        if self.topics:
            for v1 in self.topics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.ext_info is not None:
            result['extInfo'] = self.ext_info

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.item_status is not None:
            result['itemStatus'] = self.item_status

        if self.plan_id is not None:
            result['planId'] = self.plan_id

        result['topics'] = []
        if self.topics is not None:
            for k1 in self.topics:
                result['topics'].append(k1.to_map() if k1 else None)

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('extInfo') is not None:
            self.ext_info = m.get('extInfo')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('itemStatus') is not None:
            self.item_status = m.get('itemStatus')

        if m.get('planId') is not None:
            self.plan_id = m.get('planId')

        self.topics = []
        if m.get('topics') is not None:
            for k1 in m.get('topics'):
                temp_model = main_models.GetDisasterRecoveryItemResponseBodyDataTopics()
                self.topics.append(temp_model.from_map(k1))

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

class GetDisasterRecoveryItemResponseBodyDataTopics(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        delivery_order_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The order in which messages are delivered to the target instance. The parameter values ​​are as follows:
        #   - Concurrently: concurrent delivery
        #   - Orderly: sequential delivery
        self.delivery_order_type = delivery_order_type
        # The instance ID.
        self.instance_id = instance_id
        # Instance type
        #   - ALIYUN_ROCKETMQ: Alibaba Cloud instance
        #   - EXTERNAL_ROCKETMQ: External instance, open-source instance, open-source cluster
        self.instance_type = instance_type
        # regionId
        self.region_id = region_id
        # The topic name.
        self.topic_name = topic_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer_group_id is not None:
            result['consumerGroupId'] = self.consumer_group_id

        if self.delivery_order_type is not None:
            result['deliveryOrderType'] = self.delivery_order_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_type is not None:
            result['instanceType'] = self.instance_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('consumerGroupId') is not None:
            self.consumer_group_id = m.get('consumerGroupId')

        if m.get('deliveryOrderType') is not None:
            self.delivery_order_type = m.get('deliveryOrderType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        return self

