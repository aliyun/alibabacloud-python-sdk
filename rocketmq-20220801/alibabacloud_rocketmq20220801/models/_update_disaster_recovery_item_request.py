# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class UpdateDisasterRecoveryItemRequest(DaraModel):
    def __init__(
        self,
        topics: List[main_models.UpdateDisasterRecoveryItemRequestTopics] = None,
    ):
        # The topics involved in the topic mapping.
        self.topics = topics

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
        result['topics'] = []
        if self.topics is not None:
            for k1 in self.topics:
                result['topics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topics = []
        if m.get('topics') is not None:
            for k1 in m.get('topics'):
                temp_model = main_models.UpdateDisasterRecoveryItemRequestTopics()
                self.topics.append(temp_model.from_map(k1))

        return self

class UpdateDisasterRecoveryItemRequestTopics(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        delivery_order_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # The ID of the consumer group. If you use the two-way backup mode, you must specify this parameter.
        self.consumer_group_id = consumer_group_id
        # The method used to deliver messages to the destination instance.
        # 
        # Valid values:
        # 
        # *   Concurrently: concurrent delivery
        # *   Orderly: ordered delivery
        self.delivery_order_type = delivery_order_type
        # The instance ID. If you set instanceType to EXTERNAL_ROCKETMQ, the system automatically generates an ID for the instance. You can obtain the ID by querying the global message backup plan.
        self.instance_id = instance_id
        # The instance type. Valid values:
        # 
        # *   ALIYUN_ROCKETMQ: ApsaraMQ for RocketMQ instance
        # *   EXTERNAL_ROCKETMQ: open source RocketMQ cluster
        self.instance_type = instance_type
        # The region ID.
        self.region_id = region_id
        # The topic name. You must specify this parameter.
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

