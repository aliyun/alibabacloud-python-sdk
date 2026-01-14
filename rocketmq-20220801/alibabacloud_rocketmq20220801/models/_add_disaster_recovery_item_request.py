# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rocketmq20220801 import models as main_models
from darabonba.model import DaraModel

class AddDisasterRecoveryItemRequest(DaraModel):
    def __init__(
        self,
        topics: List[main_models.AddDisasterRecoveryItemRequestTopics] = None,
    ):
        # Topics included in the backup mapping. Required.
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
                temp_model = main_models.AddDisasterRecoveryItemRequestTopics()
                self.topics.append(temp_model.from_map(k1))

        return self



class AddDisasterRecoveryItemRequestTopics(DaraModel):
    def __init__(
        self,
        consumer_group_id: str = None,
        delivery_order_type: str = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        topic_name: str = None,
    ):
        # Consumer group ID, required for ACTIVE_ACTIVE bidirectional backup
        self.consumer_group_id = consumer_group_id
        # The order in which messages are delivered to the target instance. The parameter values ​​are as follows:
        #   - Concurrently: concurrent delivery
        #   - Orderly: sequential delivery
        self.delivery_order_type = delivery_order_type
        # Instance ID, an instance ID will be automatically generated when `instanceType` is `EXTERNAL_ROCKETMQ`, and it can be obtained by querying the backup plan.
        self.instance_id = instance_id
        # Instance type
        #   - ALIYUN_ROCKETMQ: Alibaba Cloud instance
        #   - EXTERNAL_ROCKETMQ: External instance, open-source instance, open-source cluster
        self.instance_type = instance_type
        # Region ID
        self.region_id = region_id
        # Disaster recovery topic name, required
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

