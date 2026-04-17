# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alikafka20190916 import models as main_models
from darabonba.model import DaraModel

class GetConsumerProgressResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        consumer_progress: main_models.GetConsumerProgressResponseBodyConsumerProgress = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned HTTP status code. If the request is successful, 200 is returned.
        self.code = code
        # The consumer progress of the consumer group.
        self.consumer_progress = consumer_progress
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success

    def validate(self):
        if self.consumer_progress:
            self.consumer_progress.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.consumer_progress is not None:
            result['ConsumerProgress'] = self.consumer_progress.to_map()

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

        if m.get('ConsumerProgress') is not None:
            temp_model = main_models.GetConsumerProgressResponseBodyConsumerProgress()
            self.consumer_progress = temp_model.from_map(m.get('ConsumerProgress'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetConsumerProgressResponseBodyConsumerProgress(DaraModel):
    def __init__(
        self,
        last_timestamp: int = None,
        rebalance_info_list: main_models.GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoList = None,
        topic_list: main_models.GetConsumerProgressResponseBodyConsumerProgressTopicList = None,
        total_diff: int = None,
        state: str = None,
    ):
        # The time when the last message consumed by the consumer group was generated.
        self.last_timestamp = last_timestamp
        self.rebalance_info_list = rebalance_info_list
        self.topic_list = topic_list
        # The total number of unconsumed messages in all topics to which the consumer group subscribes.
        self.total_diff = total_diff
        self.state = state

    def validate(self):
        if self.rebalance_info_list:
            self.rebalance_info_list.validate()
        if self.topic_list:
            self.topic_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp

        if self.rebalance_info_list is not None:
            result['RebalanceInfoList'] = self.rebalance_info_list.to_map()

        if self.topic_list is not None:
            result['TopicList'] = self.topic_list.to_map()

        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')

        if m.get('RebalanceInfoList') is not None:
            temp_model = main_models.GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoList()
            self.rebalance_info_list = temp_model.from_map(m.get('RebalanceInfoList'))

        if m.get('TopicList') is not None:
            temp_model = main_models.GetConsumerProgressResponseBodyConsumerProgressTopicList()
            self.topic_list = temp_model.from_map(m.get('TopicList'))

        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self

class GetConsumerProgressResponseBodyConsumerProgressTopicList(DaraModel):
    def __init__(
        self,
        topic_list: List[main_models.GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList] = None,
    ):
        self.topic_list = topic_list

    def validate(self):
        if self.topic_list:
            for v1 in self.topic_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TopicList'] = []
        if self.topic_list is not None:
            for k1 in self.topic_list:
                result['TopicList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topic_list = []
        if m.get('TopicList') is not None:
            for k1 in m.get('TopicList'):
                temp_model = main_models.GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList()
                self.topic_list.append(temp_model.from_map(k1))

        return self

class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicList(DaraModel):
    def __init__(
        self,
        last_timestamp: int = None,
        offset_list: main_models.GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList = None,
        topic: str = None,
        total_diff: int = None,
    ):
        self.last_timestamp = last_timestamp
        self.offset_list = offset_list
        self.topic = topic
        self.total_diff = total_diff

    def validate(self):
        if self.offset_list:
            self.offset_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp

        if self.offset_list is not None:
            result['OffsetList'] = self.offset_list.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')

        if m.get('OffsetList') is not None:
            temp_model = main_models.GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList()
            self.offset_list = temp_model.from_map(m.get('OffsetList'))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')

        return self

class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetList(DaraModel):
    def __init__(
        self,
        offset_list: List[main_models.GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList] = None,
    ):
        self.offset_list = offset_list

    def validate(self):
        if self.offset_list:
            for v1 in self.offset_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['OffsetList'] = []
        if self.offset_list is not None:
            for k1 in self.offset_list:
                result['OffsetList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.offset_list = []
        if m.get('OffsetList') is not None:
            for k1 in m.get('OffsetList'):
                temp_model = main_models.GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList()
                self.offset_list.append(temp_model.from_map(k1))

        return self

class GetConsumerProgressResponseBodyConsumerProgressTopicListTopicListOffsetListOffsetList(DaraModel):
    def __init__(
        self,
        accumulate: int = None,
        broker_offset: int = None,
        client_id: str = None,
        client_ip: str = None,
        consumer_offset: int = None,
        last_timestamp: int = None,
        member_id: str = None,
        partition: int = None,
    ):
        self.accumulate = accumulate
        self.broker_offset = broker_offset
        self.client_id = client_id
        self.client_ip = client_ip
        self.consumer_offset = consumer_offset
        self.last_timestamp = last_timestamp
        self.member_id = member_id
        self.partition = partition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accumulate is not None:
            result['Accumulate'] = self.accumulate

        if self.broker_offset is not None:
            result['BrokerOffset'] = self.broker_offset

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.consumer_offset is not None:
            result['ConsumerOffset'] = self.consumer_offset

        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp

        if self.member_id is not None:
            result['MemberId'] = self.member_id

        if self.partition is not None:
            result['Partition'] = self.partition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accumulate') is not None:
            self.accumulate = m.get('Accumulate')

        if m.get('BrokerOffset') is not None:
            self.broker_offset = m.get('BrokerOffset')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('ConsumerOffset') is not None:
            self.consumer_offset = m.get('ConsumerOffset')

        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')

        if m.get('MemberId') is not None:
            self.member_id = m.get('MemberId')

        if m.get('Partition') is not None:
            self.partition = m.get('Partition')

        return self

class GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoList(DaraModel):
    def __init__(
        self,
        rebalance_info_list: List[main_models.GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoListRebalanceInfoList] = None,
    ):
        self.rebalance_info_list = rebalance_info_list

    def validate(self):
        if self.rebalance_info_list:
            for v1 in self.rebalance_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RebalanceInfoList'] = []
        if self.rebalance_info_list is not None:
            for k1 in self.rebalance_info_list:
                result['RebalanceInfoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rebalance_info_list = []
        if m.get('RebalanceInfoList') is not None:
            for k1 in m.get('RebalanceInfoList'):
                temp_model = main_models.GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoListRebalanceInfoList()
                self.rebalance_info_list.append(temp_model.from_map(k1))

        return self

class GetConsumerProgressResponseBodyConsumerProgressRebalanceInfoListRebalanceInfoList(DaraModel):
    def __init__(
        self,
        generation: int = None,
        group_id: str = None,
        last_rebalance_timestamp: int = None,
        reason: str = None,
        rebalance_success: bool = None,
        rebalance_time_consuming: int = None,
    ):
        self.generation = generation
        self.group_id = group_id
        self.last_rebalance_timestamp = last_rebalance_timestamp
        self.reason = reason
        self.rebalance_success = rebalance_success
        self.rebalance_time_consuming = rebalance_time_consuming

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generation is not None:
            result['Generation'] = self.generation

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.last_rebalance_timestamp is not None:
            result['LastRebalanceTimestamp'] = self.last_rebalance_timestamp

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.rebalance_success is not None:
            result['RebalanceSuccess'] = self.rebalance_success

        if self.rebalance_time_consuming is not None:
            result['RebalanceTimeConsuming'] = self.rebalance_time_consuming

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Generation') is not None:
            self.generation = m.get('Generation')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LastRebalanceTimestamp') is not None:
            self.last_rebalance_timestamp = m.get('LastRebalanceTimestamp')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RebalanceSuccess') is not None:
            self.rebalance_success = m.get('RebalanceSuccess')

        if m.get('RebalanceTimeConsuming') is not None:
            self.rebalance_time_consuming = m.get('RebalanceTimeConsuming')

        return self

