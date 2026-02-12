# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsConsumerStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.OnsConsumerStatusResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
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
            temp_model = main_models.OnsConsumerStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsConsumerStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        connection_set: main_models.OnsConsumerStatusResponseBodyDataConnectionSet = None,
        consume_model: str = None,
        consume_tps: float = None,
        consumer_connection_info_list: main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoList = None,
        delay_time: int = None,
        detail_in_topic_list: main_models.OnsConsumerStatusResponseBodyDataDetailInTopicList = None,
        instance_id: str = None,
        last_timestamp: int = None,
        online: bool = None,
        rebalance_ok: bool = None,
        subscription_same: bool = None,
        total_diff: int = None,
    ):
        self.connection_set = connection_set
        # The consumption mode. Valid values:
        # 
        # *   **CLUSTERING**: the clustering consumption mode
        # *   **BROADCASTING**: the broadcasting consumption mode
        # 
        # For more information about consumption modes, see [Clustering consumption and broadcasting consumption](https://help.aliyun.com/document_detail/43163.html).
        self.consume_model = consume_model
        # The TPS for message consumption.
        self.consume_tps = consume_tps
        self.consumer_connection_info_list = consumer_connection_info_list
        # The maximum latency of message consumption in all topics to which the consumer group subscribes. Unit: milliseconds.
        self.delay_time = delay_time
        self.detail_in_topic_list = detail_in_topic_list
        # The ID of the instance
        self.instance_id = instance_id
        # The most recent point in time when a message was consumed.
        # 
        # The value of this parameter is a UNIX timestamp in milliseconds.
        self.last_timestamp = last_timestamp
        # Indicates whether the consumer group is online.
        self.online = online
        # Indicates whether load balancing is performed as expected. Valid values:
        # 
        # *   **true**: Load balancing is performed as expected.
        # *   **false**: Load balancing is not performed as expected.
        self.rebalance_ok = rebalance_ok
        # Indicates whether all consumers in the consumer group subscribe to the same topics and tags.
        self.subscription_same = subscription_same
        # The total number of accumulated messages.
        self.total_diff = total_diff

    def validate(self):
        if self.connection_set:
            self.connection_set.validate()
        if self.consumer_connection_info_list:
            self.consumer_connection_info_list.validate()
        if self.detail_in_topic_list:
            self.detail_in_topic_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_set is not None:
            result['ConnectionSet'] = self.connection_set.to_map()

        if self.consume_model is not None:
            result['ConsumeModel'] = self.consume_model

        if self.consume_tps is not None:
            result['ConsumeTps'] = self.consume_tps

        if self.consumer_connection_info_list is not None:
            result['ConsumerConnectionInfoList'] = self.consumer_connection_info_list.to_map()

        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time

        if self.detail_in_topic_list is not None:
            result['DetailInTopicList'] = self.detail_in_topic_list.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp

        if self.online is not None:
            result['Online'] = self.online

        if self.rebalance_ok is not None:
            result['RebalanceOK'] = self.rebalance_ok

        if self.subscription_same is not None:
            result['SubscriptionSame'] = self.subscription_same

        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionSet') is not None:
            temp_model = main_models.OnsConsumerStatusResponseBodyDataConnectionSet()
            self.connection_set = temp_model.from_map(m.get('ConnectionSet'))

        if m.get('ConsumeModel') is not None:
            self.consume_model = m.get('ConsumeModel')

        if m.get('ConsumeTps') is not None:
            self.consume_tps = m.get('ConsumeTps')

        if m.get('ConsumerConnectionInfoList') is not None:
            temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoList()
            self.consumer_connection_info_list = temp_model.from_map(m.get('ConsumerConnectionInfoList'))

        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')

        if m.get('DetailInTopicList') is not None:
            temp_model = main_models.OnsConsumerStatusResponseBodyDataDetailInTopicList()
            self.detail_in_topic_list = temp_model.from_map(m.get('DetailInTopicList'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')

        if m.get('Online') is not None:
            self.online = m.get('Online')

        if m.get('RebalanceOK') is not None:
            self.rebalance_ok = m.get('RebalanceOK')

        if m.get('SubscriptionSame') is not None:
            self.subscription_same = m.get('SubscriptionSame')

        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')

        return self

class OnsConsumerStatusResponseBodyDataDetailInTopicList(DaraModel):
    def __init__(
        self,
        detail_in_topic_do: List[main_models.OnsConsumerStatusResponseBodyDataDetailInTopicListDetailInTopicDo] = None,
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
                temp_model = main_models.OnsConsumerStatusResponseBodyDataDetailInTopicListDetailInTopicDo()
                self.detail_in_topic_do.append(temp_model.from_map(k1))

        return self

class OnsConsumerStatusResponseBodyDataDetailInTopicListDetailInTopicDo(DaraModel):
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

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoList(DaraModel):
    def __init__(
        self,
        consumer_connection_info_do: List[main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDo] = None,
    ):
        self.consumer_connection_info_do = consumer_connection_info_do

    def validate(self):
        if self.consumer_connection_info_do:
            for v1 in self.consumer_connection_info_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConsumerConnectionInfoDo'] = []
        if self.consumer_connection_info_do is not None:
            for k1 in self.consumer_connection_info_do:
                result['ConsumerConnectionInfoDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumer_connection_info_do = []
        if m.get('ConsumerConnectionInfoDo') is not None:
            for k1 in m.get('ConsumerConnectionInfoDo'):
                temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDo()
                self.consumer_connection_info_do.append(temp_model.from_map(k1))

        return self

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDo(DaraModel):
    def __init__(
        self,
        client_id: str = None,
        connection: str = None,
        consume_model: str = None,
        consume_type: str = None,
        jstack: main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstack = None,
        language: str = None,
        last_time_stamp: int = None,
        running_data_list: main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataList = None,
        start_time_stamp: int = None,
        subscription_set: main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSet = None,
        thread_count: int = None,
        version: str = None,
    ):
        self.client_id = client_id
        self.connection = connection
        self.consume_model = consume_model
        self.consume_type = consume_type
        self.jstack = jstack
        self.language = language
        self.last_time_stamp = last_time_stamp
        self.running_data_list = running_data_list
        self.start_time_stamp = start_time_stamp
        self.subscription_set = subscription_set
        self.thread_count = thread_count
        self.version = version

    def validate(self):
        if self.jstack:
            self.jstack.validate()
        if self.running_data_list:
            self.running_data_list.validate()
        if self.subscription_set:
            self.subscription_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.connection is not None:
            result['Connection'] = self.connection

        if self.consume_model is not None:
            result['ConsumeModel'] = self.consume_model

        if self.consume_type is not None:
            result['ConsumeType'] = self.consume_type

        if self.jstack is not None:
            result['Jstack'] = self.jstack.to_map()

        if self.language is not None:
            result['Language'] = self.language

        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp

        if self.running_data_list is not None:
            result['RunningDataList'] = self.running_data_list.to_map()

        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp

        if self.subscription_set is not None:
            result['SubscriptionSet'] = self.subscription_set.to_map()

        if self.thread_count is not None:
            result['ThreadCount'] = self.thread_count

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Connection') is not None:
            self.connection = m.get('Connection')

        if m.get('ConsumeModel') is not None:
            self.consume_model = m.get('ConsumeModel')

        if m.get('ConsumeType') is not None:
            self.consume_type = m.get('ConsumeType')

        if m.get('Jstack') is not None:
            temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstack()
            self.jstack = temp_model.from_map(m.get('Jstack'))

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')

        if m.get('RunningDataList') is not None:
            temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataList()
            self.running_data_list = temp_model.from_map(m.get('RunningDataList'))

        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')

        if m.get('SubscriptionSet') is not None:
            temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSet()
            self.subscription_set = temp_model.from_map(m.get('SubscriptionSet'))

        if m.get('ThreadCount') is not None:
            self.thread_count = m.get('ThreadCount')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSet(DaraModel):
    def __init__(
        self,
        subscription_data: List[main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionData] = None,
    ):
        self.subscription_data = subscription_data

    def validate(self):
        if self.subscription_data:
            for v1 in self.subscription_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubscriptionData'] = []
        if self.subscription_data is not None:
            for k1 in self.subscription_data:
                result['SubscriptionData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_data = []
        if m.get('SubscriptionData') is not None:
            for k1 in m.get('SubscriptionData'):
                temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionData()
                self.subscription_data.append(temp_model.from_map(k1))

        return self

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionData(DaraModel):
    def __init__(
        self,
        sub_string: str = None,
        sub_version: int = None,
        tags_set: main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionDataTagsSet = None,
        topic: str = None,
    ):
        self.sub_string = sub_string
        self.sub_version = sub_version
        self.tags_set = tags_set
        self.topic = topic

    def validate(self):
        if self.tags_set:
            self.tags_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sub_string is not None:
            result['SubString'] = self.sub_string

        if self.sub_version is not None:
            result['SubVersion'] = self.sub_version

        if self.tags_set is not None:
            result['TagsSet'] = self.tags_set.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubString') is not None:
            self.sub_string = m.get('SubString')

        if m.get('SubVersion') is not None:
            self.sub_version = m.get('SubVersion')

        if m.get('TagsSet') is not None:
            temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionDataTagsSet()
            self.tags_set = temp_model.from_map(m.get('TagsSet'))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionDataTagsSet(DaraModel):
    def __init__(
        self,
        tag: List[str] = None,
    ):
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataList(DaraModel):
    def __init__(
        self,
        consumer_running_data_do: List[main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataListConsumerRunningDataDo] = None,
    ):
        self.consumer_running_data_do = consumer_running_data_do

    def validate(self):
        if self.consumer_running_data_do:
            for v1 in self.consumer_running_data_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConsumerRunningDataDo'] = []
        if self.consumer_running_data_do is not None:
            for k1 in self.consumer_running_data_do:
                result['ConsumerRunningDataDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumer_running_data_do = []
        if m.get('ConsumerRunningDataDo') is not None:
            for k1 in m.get('ConsumerRunningDataDo'):
                temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataListConsumerRunningDataDo()
                self.consumer_running_data_do.append(temp_model.from_map(k1))

        return self

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataListConsumerRunningDataDo(DaraModel):
    def __init__(
        self,
        failed_count_per_hour: int = None,
        failed_tps: float = None,
        ok_tps: float = None,
        rt: float = None,
        topic: str = None,
    ):
        self.failed_count_per_hour = failed_count_per_hour
        self.failed_tps = failed_tps
        self.ok_tps = ok_tps
        self.rt = rt
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_count_per_hour is not None:
            result['FailedCountPerHour'] = self.failed_count_per_hour

        if self.failed_tps is not None:
            result['FailedTps'] = self.failed_tps

        if self.ok_tps is not None:
            result['OkTps'] = self.ok_tps

        if self.rt is not None:
            result['Rt'] = self.rt

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailedCountPerHour') is not None:
            self.failed_count_per_hour = m.get('FailedCountPerHour')

        if m.get('FailedTps') is not None:
            self.failed_tps = m.get('FailedTps')

        if m.get('OkTps') is not None:
            self.ok_tps = m.get('OkTps')

        if m.get('Rt') is not None:
            self.rt = m.get('Rt')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstack(DaraModel):
    def __init__(
        self,
        thread_track_do: List[main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDo] = None,
    ):
        self.thread_track_do = thread_track_do

    def validate(self):
        if self.thread_track_do:
            for v1 in self.thread_track_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ThreadTrackDo'] = []
        if self.thread_track_do is not None:
            for k1 in self.thread_track_do:
                result['ThreadTrackDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.thread_track_do = []
        if m.get('ThreadTrackDo') is not None:
            for k1 in m.get('ThreadTrackDo'):
                temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDo()
                self.thread_track_do.append(temp_model.from_map(k1))

        return self

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDo(DaraModel):
    def __init__(
        self,
        thread: str = None,
        track_list: main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDoTrackList = None,
    ):
        self.thread = thread
        self.track_list = track_list

    def validate(self):
        if self.track_list:
            self.track_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.thread is not None:
            result['Thread'] = self.thread

        if self.track_list is not None:
            result['TrackList'] = self.track_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')

        if m.get('TrackList') is not None:
            temp_model = main_models.OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDoTrackList()
            self.track_list = temp_model.from_map(m.get('TrackList'))

        return self

class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDoTrackList(DaraModel):
    def __init__(
        self,
        track: List[str] = None,
    ):
        self.track = track

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.track is not None:
            result['Track'] = self.track

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Track') is not None:
            self.track = m.get('Track')

        return self

class OnsConsumerStatusResponseBodyDataConnectionSet(DaraModel):
    def __init__(
        self,
        connection_do: List[main_models.OnsConsumerStatusResponseBodyDataConnectionSetConnectionDo] = None,
    ):
        self.connection_do = connection_do

    def validate(self):
        if self.connection_do:
            for v1 in self.connection_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConnectionDo'] = []
        if self.connection_do is not None:
            for k1 in self.connection_do:
                result['ConnectionDo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_do = []
        if m.get('ConnectionDo') is not None:
            for k1 in m.get('ConnectionDo'):
                temp_model = main_models.OnsConsumerStatusResponseBodyDataConnectionSetConnectionDo()
                self.connection_do.append(temp_model.from_map(k1))

        return self

class OnsConsumerStatusResponseBodyDataConnectionSetConnectionDo(DaraModel):
    def __init__(
        self,
        client_addr: str = None,
        client_id: str = None,
        diff: int = None,
        language: str = None,
        remote_ip: str = None,
        version: str = None,
    ):
        self.client_addr = client_addr
        self.client_id = client_id
        self.diff = diff
        self.language = language
        self.remote_ip = remote_ip
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.diff is not None:
            result['Diff'] = self.diff

        if self.language is not None:
            result['Language'] = self.language

        if self.remote_ip is not None:
            result['RemoteIP'] = self.remote_ip

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('Diff') is not None:
            self.diff = m.get('Diff')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('RemoteIP') is not None:
            self.remote_ip = m.get('RemoteIP')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

