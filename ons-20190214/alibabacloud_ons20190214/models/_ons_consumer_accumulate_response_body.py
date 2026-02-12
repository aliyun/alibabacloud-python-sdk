# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsConsumerAccumulateResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsConsumerAccumulateResponseBodyData = None,
        request_id: str = None,
    ):
        # The message accumulation information about topics to which the specified consumer subscribes.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.OnsConsumerAccumulateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsConsumerAccumulateResponseBodyData(DaraModel):
    def __init__(
        self,
        consume_tps: float = None,
        delay_time: int = None,
        detail_in_topic_list: main_models.OnsConsumerAccumulateResponseBodyDataDetailInTopicList = None,
        last_timestamp: int = None,
        online: bool = None,
        total_diff: int = None,
    ):
        # The transactions per second (TPS) for message consumption performed by consumers in the group.
        self.consume_tps = consume_tps
        # The consumption latency.
        self.delay_time = delay_time
        self.detail_in_topic_list = detail_in_topic_list
        # The point in time when the latest message consumed by a consumer in the consumer group was produced.
        self.last_timestamp = last_timestamp
        # Indicates whether the consumer group is online. The consumer group is online if one of the consumers in the group is online. Valid values:
        # 
        # *   **true**: The consumer group is online.
        # *   **false**: The consumer group is offline.
        self.online = online
        # The total number of accumulated messages in all topics to which the consumer group subscribes.
        self.total_diff = total_diff

    def validate(self):
        if self.detail_in_topic_list:
            self.detail_in_topic_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consume_tps is not None:
            result['ConsumeTps'] = self.consume_tps

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.detail_in_topic_list is not None:
            result['DetailInTopicList'] = self.detail_in_topic_list.to_map()

        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp

        if self.online is not None:
            result['Online'] = self.online

        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeTps') is not None:
            self.consume_tps = m.get('ConsumeTps')

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('DetailInTopicList') is not None:
            temp_model = main_models.OnsConsumerAccumulateResponseBodyDataDetailInTopicList()
            self.detail_in_topic_list = temp_model.from_map(m.get('DetailInTopicList'))

        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')

        return self

class OnsConsumerAccumulateResponseBodyDataDetailInTopicList(DaraModel):
    def __init__(
        self,
        detail_in_topic_do: List[main_models.OnsConsumerAccumulateResponseBodyDataDetailInTopicListDetailInTopicDo] = None,
    ):
        self.detail_in_topic_do = detail_in_topic_do

    def validate(self):
        if self.detail_in_topic_do:
            for v1 in self.detail_in_topic_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DetailInTopicDo'] = []
        if self.detail_in_topic_do is not None:
            for k1 in self.detail_in_topic_do:
                result['DetailInTopicDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_in_topic_do = []
        if m.get('DetailInTopicDo') is not None:
            for k1 in m.get('DetailInTopicDo'):
                temp_model = main_models.OnsConsumerAccumulateResponseBodyDataDetailInTopicListDetailInTopicDo()
                self.detail_in_topic_do.append(temp_model.from_map(k1))

        return self

class OnsConsumerAccumulateResponseBodyDataDetailInTopicListDetailInTopicDo(DaraModel):
    def __init__(
        self,
        delay_time: int = None,
        last_timestamp: int = None,
        topic: str = None,
        total_diff: int = None,
    ):
        self.delay_time = delay_time
        self.last_timestamp = last_timestamp
        self.topic = topic
        self.total_diff = total_diff

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')

        return self

