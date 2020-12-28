# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ListTagResourcesRequestTag(TeaModel):
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


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_type: str = None,
        next_token: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
        resource_id: List[str] = None,
    ):
        self.instance_id = instance_id
        self.resource_type = resource_type
        self.next_token = next_token
        self.tag = tag
        self.resource_id = resource_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        resource_type: str = None,
        instance_id: str = None,
        tag_value: str = None,
        resource_id: str = None,
        tag_key: str = None,
    ):
        self.resource_type = resource_type
        self.instance_id = instance_id
        self.tag_value = tag_value
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsConsumerAccumulateRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        detail: bool = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.detail = detail
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsConsumerAccumulateResponseBodyDataDetailInTopicList(TeaModel):
    def __init__(
        self,
        delay_time: int = None,
        total_diff: int = None,
        last_timestamp: int = None,
        topic: str = None,
    ):
        self.delay_time = delay_time
        self.total_diff = total_diff
        self.last_timestamp = last_timestamp
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsConsumerAccumulateResponseBodyData(TeaModel):
    def __init__(
        self,
        consume_tps: float = None,
        delay_time: int = None,
        last_timestamp: int = None,
        total_diff: int = None,
        online: bool = None,
        detail_in_topic_list: List[OnsConsumerAccumulateResponseBodyDataDetailInTopicList] = None,
    ):
        self.consume_tps = consume_tps
        self.delay_time = delay_time
        self.last_timestamp = last_timestamp
        self.total_diff = total_diff
        self.online = online
        self.detail_in_topic_list = detail_in_topic_list

    def validate(self):
        if self.detail_in_topic_list:
            for k in self.detail_in_topic_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.consume_tps is not None:
            result['ConsumeTps'] = self.consume_tps
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        if self.online is not None:
            result['Online'] = self.online
        result['DetailInTopicList'] = []
        if self.detail_in_topic_list is not None:
            for k in self.detail_in_topic_list:
                result['DetailInTopicList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeTps') is not None:
            self.consume_tps = m.get('ConsumeTps')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        self.detail_in_topic_list = []
        if m.get('DetailInTopicList') is not None:
            for k in m.get('DetailInTopicList'):
                temp_model = OnsConsumerAccumulateResponseBodyDataDetailInTopicList()
                self.detail_in_topic_list.append(temp_model.from_map(k))
        return self


class OnsConsumerAccumulateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsConsumerAccumulateResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsConsumerAccumulateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsConsumerAccumulateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsConsumerAccumulateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsConsumerAccumulateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsConsumerGetConnectionRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsConsumerGetConnectionResponseBodyDataConnectionList(TeaModel):
    def __init__(
        self,
        version: str = None,
        client_addr: str = None,
        language: str = None,
        client_id: str = None,
    ):
        self.version = version
        self.client_addr = client_addr
        self.language = language
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.version is not None:
            result['Version'] = self.version
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr
        if self.language is not None:
            result['Language'] = self.language
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class OnsConsumerGetConnectionResponseBodyData(TeaModel):
    def __init__(
        self,
        connection_list: List[OnsConsumerGetConnectionResponseBodyDataConnectionList] = None,
    ):
        self.connection_list = connection_list

    def validate(self):
        if self.connection_list:
            for k in self.connection_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ConnectionList'] = []
        if self.connection_list is not None:
            for k in self.connection_list:
                result['ConnectionList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_list = []
        if m.get('ConnectionList') is not None:
            for k in m.get('ConnectionList'):
                temp_model = OnsConsumerGetConnectionResponseBodyDataConnectionList()
                self.connection_list.append(temp_model.from_map(k))
        return self


class OnsConsumerGetConnectionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsConsumerGetConnectionResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsConsumerGetConnectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsConsumerGetConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsConsumerGetConnectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsConsumerGetConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsConsumerResetOffsetRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        topic: str = None,
        type: int = None,
        reset_timestamp: int = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.topic = topic
        self.type = type
        self.reset_timestamp = reset_timestamp
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.type is not None:
            result['Type'] = self.type
        if self.reset_timestamp is not None:
            result['ResetTimestamp'] = self.reset_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ResetTimestamp') is not None:
            self.reset_timestamp = m.get('ResetTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsConsumerResetOffsetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsConsumerResetOffsetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsConsumerResetOffsetResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsConsumerResetOffsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsConsumerStatusRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        detail: bool = None,
        need_jstack: bool = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.detail = detail
        self.need_jstack = need_jstack
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.need_jstack is not None:
            result['NeedJstack'] = self.need_jstack
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('NeedJstack') is not None:
            self.need_jstack = m.get('NeedJstack')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsConsumerStatusResponseBodyDataConnectionSet(TeaModel):
    def __init__(
        self,
        remote_ip: str = None,
        version: str = None,
        client_addr: str = None,
        language: str = None,
        client_id: str = None,
    ):
        self.remote_ip = remote_ip
        self.version = version
        self.client_addr = client_addr
        self.language = language
        self.client_id = client_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remote_ip is not None:
            result['RemoteIP'] = self.remote_ip
        if self.version is not None:
            result['Version'] = self.version
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr
        if self.language is not None:
            result['Language'] = self.language
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RemoteIP') is not None:
            self.remote_ip = m.get('RemoteIP')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListRunningDataList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        rt: float = None,
        topic: str = None,
        failed_count_per_hour: int = None,
        ok_tps: float = None,
        failed_tps: float = None,
    ):
        self.group_id = group_id
        self.rt = rt
        self.topic = topic
        self.failed_count_per_hour = failed_count_per_hour
        self.ok_tps = ok_tps
        self.failed_tps = failed_tps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.rt is not None:
            result['Rt'] = self.rt
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.failed_count_per_hour is not None:
            result['FailedCountPerHour'] = self.failed_count_per_hour
        if self.ok_tps is not None:
            result['OkTps'] = self.ok_tps
        if self.failed_tps is not None:
            result['FailedTps'] = self.failed_tps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Rt') is not None:
            self.rt = m.get('Rt')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('FailedCountPerHour') is not None:
            self.failed_count_per_hour = m.get('FailedCountPerHour')
        if m.get('OkTps') is not None:
            self.ok_tps = m.get('OkTps')
        if m.get('FailedTps') is not None:
            self.failed_tps = m.get('FailedTps')
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListSubscriptionSet(TeaModel):
    def __init__(
        self,
        sub_string: str = None,
        sub_version: int = None,
        topic: str = None,
        tags_set: List[str] = None,
    ):
        self.sub_string = sub_string
        self.sub_version = sub_version
        self.topic = topic
        self.tags_set = tags_set

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sub_string is not None:
            result['SubString'] = self.sub_string
        if self.sub_version is not None:
            result['SubVersion'] = self.sub_version
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.tags_set is not None:
            result['TagsSet'] = self.tags_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubString') is not None:
            self.sub_string = m.get('SubString')
        if m.get('SubVersion') is not None:
            self.sub_version = m.get('SubVersion')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TagsSet') is not None:
            self.tags_set = m.get('TagsSet')
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListJstack(TeaModel):
    def __init__(
        self,
        track_list: List[str] = None,
        thread: str = None,
    ):
        self.track_list = track_list
        self.thread = thread

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.track_list is not None:
            result['TrackList'] = self.track_list
        if self.thread is not None:
            result['Thread'] = self.thread
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrackList') is not None:
            self.track_list = m.get('TrackList')
        if m.get('Thread') is not None:
            self.thread = m.get('Thread')
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoList(TeaModel):
    def __init__(
        self,
        consume_model: str = None,
        running_data_list: List[OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListRunningDataList] = None,
        subscription_set: List[OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListSubscriptionSet] = None,
        jstack: List[OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListJstack] = None,
        last_time_stamp: int = None,
        start_time_stamp: int = None,
        language: str = None,
        client_id: str = None,
        connection: str = None,
        version: str = None,
        consume_type: str = None,
        thread_count: int = None,
    ):
        self.consume_model = consume_model
        self.running_data_list = running_data_list
        self.subscription_set = subscription_set
        self.jstack = jstack
        self.last_time_stamp = last_time_stamp
        self.start_time_stamp = start_time_stamp
        self.language = language
        self.client_id = client_id
        self.connection = connection
        self.version = version
        self.consume_type = consume_type
        self.thread_count = thread_count

    def validate(self):
        if self.running_data_list:
            for k in self.running_data_list:
                if k:
                    k.validate()
        if self.subscription_set:
            for k in self.subscription_set:
                if k:
                    k.validate()
        if self.jstack:
            for k in self.jstack:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.consume_model is not None:
            result['ConsumeModel'] = self.consume_model
        result['RunningDataList'] = []
        if self.running_data_list is not None:
            for k in self.running_data_list:
                result['RunningDataList'].append(k.to_map() if k else None)
        result['SubscriptionSet'] = []
        if self.subscription_set is not None:
            for k in self.subscription_set:
                result['SubscriptionSet'].append(k.to_map() if k else None)
        result['Jstack'] = []
        if self.jstack is not None:
            for k in self.jstack:
                result['Jstack'].append(k.to_map() if k else None)
        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp
        if self.start_time_stamp is not None:
            result['StartTimeStamp'] = self.start_time_stamp
        if self.language is not None:
            result['Language'] = self.language
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.connection is not None:
            result['Connection'] = self.connection
        if self.version is not None:
            result['Version'] = self.version
        if self.consume_type is not None:
            result['ConsumeType'] = self.consume_type
        if self.thread_count is not None:
            result['ThreadCount'] = self.thread_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeModel') is not None:
            self.consume_model = m.get('ConsumeModel')
        self.running_data_list = []
        if m.get('RunningDataList') is not None:
            for k in m.get('RunningDataList'):
                temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListRunningDataList()
                self.running_data_list.append(temp_model.from_map(k))
        self.subscription_set = []
        if m.get('SubscriptionSet') is not None:
            for k in m.get('SubscriptionSet'):
                temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListSubscriptionSet()
                self.subscription_set.append(temp_model.from_map(k))
        self.jstack = []
        if m.get('Jstack') is not None:
            for k in m.get('Jstack'):
                temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListJstack()
                self.jstack.append(temp_model.from_map(k))
        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')
        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Connection') is not None:
            self.connection = m.get('Connection')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ConsumeType') is not None:
            self.consume_type = m.get('ConsumeType')
        if m.get('ThreadCount') is not None:
            self.thread_count = m.get('ThreadCount')
        return self


class OnsConsumerStatusResponseBodyDataDetailInTopicList(TeaModel):
    def __init__(
        self,
        delay_time: int = None,
        total_diff: int = None,
        last_timestamp: int = None,
        topic: str = None,
    ):
        self.delay_time = delay_time
        self.total_diff = total_diff
        self.last_timestamp = last_timestamp
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsConsumerStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        consume_tps: float = None,
        consume_model: str = None,
        connection_set: List[OnsConsumerStatusResponseBodyDataConnectionSet] = None,
        total_diff: int = None,
        consumer_connection_info_list: List[OnsConsumerStatusResponseBodyDataConsumerConnectionInfoList] = None,
        instance_id: str = None,
        detail_in_topic_list: List[OnsConsumerStatusResponseBodyDataDetailInTopicList] = None,
        subscription_same: bool = None,
        delay_time: int = None,
        last_timestamp: int = None,
        online: bool = None,
        rebalance_ok: bool = None,
    ):
        self.consume_tps = consume_tps
        self.consume_model = consume_model
        self.connection_set = connection_set
        self.total_diff = total_diff
        self.consumer_connection_info_list = consumer_connection_info_list
        self.instance_id = instance_id
        self.detail_in_topic_list = detail_in_topic_list
        self.subscription_same = subscription_same
        self.delay_time = delay_time
        self.last_timestamp = last_timestamp
        self.online = online
        self.rebalance_ok = rebalance_ok

    def validate(self):
        if self.connection_set:
            for k in self.connection_set:
                if k:
                    k.validate()
        if self.consumer_connection_info_list:
            for k in self.consumer_connection_info_list:
                if k:
                    k.validate()
        if self.detail_in_topic_list:
            for k in self.detail_in_topic_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.consume_tps is not None:
            result['ConsumeTps'] = self.consume_tps
        if self.consume_model is not None:
            result['ConsumeModel'] = self.consume_model
        result['ConnectionSet'] = []
        if self.connection_set is not None:
            for k in self.connection_set:
                result['ConnectionSet'].append(k.to_map() if k else None)
        if self.total_diff is not None:
            result['TotalDiff'] = self.total_diff
        result['ConsumerConnectionInfoList'] = []
        if self.consumer_connection_info_list is not None:
            for k in self.consumer_connection_info_list:
                result['ConsumerConnectionInfoList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['DetailInTopicList'] = []
        if self.detail_in_topic_list is not None:
            for k in self.detail_in_topic_list:
                result['DetailInTopicList'].append(k.to_map() if k else None)
        if self.subscription_same is not None:
            result['SubscriptionSame'] = self.subscription_same
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp
        if self.online is not None:
            result['Online'] = self.online
        if self.rebalance_ok is not None:
            result['RebalanceOK'] = self.rebalance_ok
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeTps') is not None:
            self.consume_tps = m.get('ConsumeTps')
        if m.get('ConsumeModel') is not None:
            self.consume_model = m.get('ConsumeModel')
        self.connection_set = []
        if m.get('ConnectionSet') is not None:
            for k in m.get('ConnectionSet'):
                temp_model = OnsConsumerStatusResponseBodyDataConnectionSet()
                self.connection_set.append(temp_model.from_map(k))
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        self.consumer_connection_info_list = []
        if m.get('ConsumerConnectionInfoList') is not None:
            for k in m.get('ConsumerConnectionInfoList'):
                temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoList()
                self.consumer_connection_info_list.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.detail_in_topic_list = []
        if m.get('DetailInTopicList') is not None:
            for k in m.get('DetailInTopicList'):
                temp_model = OnsConsumerStatusResponseBodyDataDetailInTopicList()
                self.detail_in_topic_list.append(temp_model.from_map(k))
        if m.get('SubscriptionSame') is not None:
            self.subscription_same = m.get('SubscriptionSame')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('RebalanceOK') is not None:
            self.rebalance_ok = m.get('RebalanceOK')
        return self


class OnsConsumerStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsConsumerStatusResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsConsumerStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsConsumerStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsConsumerStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsConsumerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsConsumerTimeSpanRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        topic: str = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.topic = topic
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsConsumerTimeSpanResponseBodyData(TeaModel):
    def __init__(
        self,
        max_time_stamp: int = None,
        consume_time_stamp: int = None,
        topic: str = None,
        min_time_stamp: int = None,
        instance_id: str = None,
    ):
        self.max_time_stamp = max_time_stamp
        self.consume_time_stamp = consume_time_stamp
        self.topic = topic
        self.min_time_stamp = min_time_stamp
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.max_time_stamp is not None:
            result['MaxTimeStamp'] = self.max_time_stamp
        if self.consume_time_stamp is not None:
            result['ConsumeTimeStamp'] = self.consume_time_stamp
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.min_time_stamp is not None:
            result['MinTimeStamp'] = self.min_time_stamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTimeStamp') is not None:
            self.max_time_stamp = m.get('MaxTimeStamp')
        if m.get('ConsumeTimeStamp') is not None:
            self.consume_time_stamp = m.get('ConsumeTimeStamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('MinTimeStamp') is not None:
            self.min_time_stamp = m.get('MinTimeStamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsConsumerTimeSpanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsConsumerTimeSpanResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsConsumerTimeSpanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsConsumerTimeSpanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsConsumerTimeSpanResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsConsumerTimeSpanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsDLQMessageGetByIdRequest(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
        group_id: str = None,
        instance_id: str = None,
    ):
        self.msg_id = msg_id
        self.group_id = group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsDLQMessageGetByIdResponseBodyDataPropertyList(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class OnsDLQMessageGetByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        store_size: int = None,
        reconsume_times: int = None,
        store_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        store_host: str = None,
        topic: str = None,
        property_list: List[OnsDLQMessageGetByIdResponseBodyDataPropertyList] = None,
        born_timestamp: int = None,
        body_crc: int = None,
        born_host: str = None,
    ):
        self.store_size = store_size
        self.reconsume_times = reconsume_times
        self.store_timestamp = store_timestamp
        self.instance_id = instance_id
        self.msg_id = msg_id
        self.store_host = store_host
        self.topic = topic
        self.property_list = property_list
        self.born_timestamp = born_timestamp
        self.body_crc = body_crc
        self.born_host = born_host

    def validate(self):
        if self.property_list:
            for k in self.property_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.topic is not None:
            result['Topic'] = self.topic
        result['PropertyList'] = []
        if self.property_list is not None:
            for k in self.property_list:
                result['PropertyList'].append(k.to_map() if k else None)
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        self.property_list = []
        if m.get('PropertyList') is not None:
            for k in m.get('PropertyList'):
                temp_model = OnsDLQMessageGetByIdResponseBodyDataPropertyList()
                self.property_list.append(temp_model.from_map(k))
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        return self


class OnsDLQMessageGetByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsDLQMessageGetByIdResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsDLQMessageGetByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsDLQMessageGetByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsDLQMessageGetByIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsDLQMessageGetByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsDLQMessagePageQueryByGroupIdRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        begin_time: int = None,
        end_time: int = None,
        task_id: str = None,
        current_page: int = None,
        page_size: int = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.task_id = task_id
        self.current_page = current_page
        self.page_size = page_size
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListPropertyList(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundList(TeaModel):
    def __init__(
        self,
        store_size: int = None,
        reconsume_times: int = None,
        store_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        store_host: str = None,
        topic: str = None,
        property_list: List[OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListPropertyList] = None,
        born_timestamp: int = None,
        body_crc: int = None,
        born_host: str = None,
    ):
        self.store_size = store_size
        self.reconsume_times = reconsume_times
        self.store_timestamp = store_timestamp
        self.instance_id = instance_id
        self.msg_id = msg_id
        self.store_host = store_host
        self.topic = topic
        self.property_list = property_list
        self.born_timestamp = born_timestamp
        self.body_crc = body_crc
        self.born_host = born_host

    def validate(self):
        if self.property_list:
            for k in self.property_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.topic is not None:
            result['Topic'] = self.topic
        result['PropertyList'] = []
        if self.property_list is not None:
            for k in self.property_list:
                result['PropertyList'].append(k.to_map() if k else None)
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        self.property_list = []
        if m.get('PropertyList') is not None:
            for k in m.get('PropertyList'):
                temp_model = OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListPropertyList()
                self.property_list.append(temp_model.from_map(k))
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        msg_found_list: List[OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundList] = None,
        max_page_count: int = None,
        task_id: str = None,
    ):
        self.current_page = current_page
        self.msg_found_list = msg_found_list
        self.max_page_count = max_page_count
        self.task_id = task_id

    def validate(self):
        if self.msg_found_list:
            for k in self.msg_found_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['MsgFoundList'] = []
        if self.msg_found_list is not None:
            for k in self.msg_found_list:
                result['MsgFoundList'].append(k.to_map() if k else None)
        if self.max_page_count is not None:
            result['MaxPageCount'] = self.max_page_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.msg_found_list = []
        if m.get('MsgFoundList') is not None:
            for k in m.get('MsgFoundList'):
                temp_model = OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundList()
                self.msg_found_list.append(temp_model.from_map(k))
        if m.get('MaxPageCount') is not None:
            self.max_page_count = m.get('MaxPageCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        msg_found_do: OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDo = None,
    ):
        self.request_id = request_id
        self.msg_found_do = msg_found_do

    def validate(self):
        if self.msg_found_do:
            self.msg_found_do.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.msg_found_do is not None:
            result['MsgFoundDo'] = self.msg_found_do.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MsgFoundDo') is not None:
            temp_model = OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDo()
            self.msg_found_do = temp_model.from_map(m['MsgFoundDo'])
        return self


class OnsDLQMessagePageQueryByGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsDLQMessagePageQueryByGroupIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsDLQMessagePageQueryByGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsDLQMessageResendByIdRequest(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
        group_id: str = None,
        instance_id: str = None,
    ):
        self.msg_id = msg_id
        self.group_id = group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsDLQMessageResendByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[str] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class OnsDLQMessageResendByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsDLQMessageResendByIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsDLQMessageResendByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsGroupConsumerUpdateRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        read_enable: bool = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.read_enable = read_enable
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.read_enable is not None:
            result['ReadEnable'] = self.read_enable
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ReadEnable') is not None:
            self.read_enable = m.get('ReadEnable')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsGroupConsumerUpdateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsGroupConsumerUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsGroupConsumerUpdateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsGroupConsumerUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsGroupCreateRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        remark: str = None,
        instance_id: str = None,
        group_type: str = None,
    ):
        self.group_id = group_id
        self.remark = remark
        self.instance_id = instance_id
        self.group_type = group_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        return self


class OnsGroupCreateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsGroupCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsGroupCreateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsGroupCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsGroupDeleteRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsGroupDeleteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsGroupDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsGroupDeleteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsGroupDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsGroupListRequestTag(TeaModel):
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


class OnsGroupListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        group_id: str = None,
        group_type: str = None,
        tag: List[OnsGroupListRequestTag] = None,
    ):
        self.instance_id = instance_id
        self.group_id = group_id
        self.group_type = group_type
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = OnsGroupListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class OnsGroupListResponseBodyDataTags(TeaModel):
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


class OnsGroupListResponseBodyData(TeaModel):
    def __init__(
        self,
        owner: str = None,
        update_time: int = None,
        independent_naming: bool = None,
        group_id: str = None,
        remark: str = None,
        create_time: int = None,
        tags: List[OnsGroupListResponseBodyDataTags] = None,
        instance_id: str = None,
        group_type: str = None,
    ):
        self.owner = owner
        self.update_time = update_time
        self.independent_naming = independent_naming
        self.group_id = group_id
        self.remark = remark
        self.create_time = create_time
        self.tags = tags
        self.instance_id = instance_id
        self.group_type = group_type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = OnsGroupListResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        return self


class OnsGroupListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[OnsGroupListResponseBodyData] = None,
        help_url: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.help_url = help_url

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.help_url is not None:
            result['HelpUrl'] = self.help_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OnsGroupListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HelpUrl') is not None:
            self.help_url = m.get('HelpUrl')
        return self


class OnsGroupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsGroupListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsGroupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsGroupSubDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        group_id: str = None,
    ):
        self.instance_id = instance_id
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        return self


class OnsGroupSubDetailResponseBodyDataSubscriptionDataList(TeaModel):
    def __init__(
        self,
        sub_string: str = None,
        topic: str = None,
    ):
        self.sub_string = sub_string
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sub_string is not None:
            result['SubString'] = self.sub_string
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubString') is not None:
            self.sub_string = m.get('SubString')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsGroupSubDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        subscription_data_list: List[OnsGroupSubDetailResponseBodyDataSubscriptionDataList] = None,
        group_id: str = None,
        message_model: str = None,
        online: bool = None,
    ):
        self.subscription_data_list = subscription_data_list
        self.group_id = group_id
        self.message_model = message_model
        self.online = online

    def validate(self):
        if self.subscription_data_list:
            for k in self.subscription_data_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SubscriptionDataList'] = []
        if self.subscription_data_list is not None:
            for k in self.subscription_data_list:
                result['SubscriptionDataList'].append(k.to_map() if k else None)
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.message_model is not None:
            result['MessageModel'] = self.message_model
        if self.online is not None:
            result['Online'] = self.online
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_data_list = []
        if m.get('SubscriptionDataList') is not None:
            for k in m.get('SubscriptionDataList'):
                temp_model = OnsGroupSubDetailResponseBodyDataSubscriptionDataList()
                self.subscription_data_list.append(temp_model.from_map(k))
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MessageModel') is not None:
            self.message_model = m.get('MessageModel')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        return self


class OnsGroupSubDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsGroupSubDetailResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsGroupSubDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsGroupSubDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsGroupSubDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsGroupSubDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsInstanceBaseInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsInstanceBaseInfoResponseBodyInstanceBaseInfoEndpoints(TeaModel):
    def __init__(
        self,
        tcp_endpoint: str = None,
        http_internet_endpoint: str = None,
        http_internal_endpoint: str = None,
        http_internet_secure_endpoint: str = None,
    ):
        self.tcp_endpoint = tcp_endpoint
        self.http_internet_endpoint = http_internet_endpoint
        self.http_internal_endpoint = http_internal_endpoint
        self.http_internet_secure_endpoint = http_internet_secure_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tcp_endpoint is not None:
            result['TcpEndpoint'] = self.tcp_endpoint
        if self.http_internet_endpoint is not None:
            result['HttpInternetEndpoint'] = self.http_internet_endpoint
        if self.http_internal_endpoint is not None:
            result['HttpInternalEndpoint'] = self.http_internal_endpoint
        if self.http_internet_secure_endpoint is not None:
            result['HttpInternetSecureEndpoint'] = self.http_internet_secure_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TcpEndpoint') is not None:
            self.tcp_endpoint = m.get('TcpEndpoint')
        if m.get('HttpInternetEndpoint') is not None:
            self.http_internet_endpoint = m.get('HttpInternetEndpoint')
        if m.get('HttpInternalEndpoint') is not None:
            self.http_internal_endpoint = m.get('HttpInternalEndpoint')
        if m.get('HttpInternetSecureEndpoint') is not None:
            self.http_internet_secure_endpoint = m.get('HttpInternetSecureEndpoint')
        return self


class OnsInstanceBaseInfoResponseBodyInstanceBaseInfo(TeaModel):
    def __init__(
        self,
        endpoints: OnsInstanceBaseInfoResponseBodyInstanceBaseInfoEndpoints = None,
        independent_naming: bool = None,
        max_tps: int = None,
        remark: str = None,
        instance_name: str = None,
        release_time: int = None,
        topic_capacity: int = None,
        instance_status: int = None,
        instance_id: str = None,
        instance_type: int = None,
    ):
        self.endpoints = endpoints
        self.independent_naming = independent_naming
        self.max_tps = max_tps
        self.remark = remark
        self.instance_name = instance_name
        self.release_time = release_time
        self.topic_capacity = topic_capacity
        self.instance_status = instance_status
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()

    def to_map(self):
        result = dict()
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.topic_capacity is not None:
            result['TopicCapacity'] = self.topic_capacity
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoints') is not None:
            temp_model = OnsInstanceBaseInfoResponseBodyInstanceBaseInfoEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('TopicCapacity') is not None:
            self.topic_capacity = m.get('TopicCapacity')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class OnsInstanceBaseInfoResponseBody(TeaModel):
    def __init__(
        self,
        instance_base_info: OnsInstanceBaseInfoResponseBodyInstanceBaseInfo = None,
        request_id: str = None,
    ):
        self.instance_base_info = instance_base_info
        self.request_id = request_id

    def validate(self):
        if self.instance_base_info:
            self.instance_base_info.validate()

    def to_map(self):
        result = dict()
        if self.instance_base_info is not None:
            result['InstanceBaseInfo'] = self.instance_base_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceBaseInfo') is not None:
            temp_model = OnsInstanceBaseInfoResponseBodyInstanceBaseInfo()
            self.instance_base_info = temp_model.from_map(m['InstanceBaseInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsInstanceBaseInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsInstanceBaseInfoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsInstanceBaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsInstanceCreateRequest(TeaModel):
    def __init__(
        self,
        remark: str = None,
        instance_name: str = None,
    ):
        self.remark = remark
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        return self


class OnsInstanceCreateResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: int = None,
    ):
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class OnsInstanceCreateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsInstanceCreateResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsInstanceCreateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsInstanceCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsInstanceCreateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsInstanceCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsInstanceDeleteRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsInstanceDeleteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsInstanceDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsInstanceDeleteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsInstanceDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsInstanceInServiceListRequestTag(TeaModel):
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


class OnsInstanceInServiceListRequest(TeaModel):
    def __init__(
        self,
        tag: List[OnsInstanceInServiceListRequestTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = OnsInstanceInServiceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class OnsInstanceInServiceListResponseBodyDataTags(TeaModel):
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


class OnsInstanceInServiceListResponseBodyData(TeaModel):
    def __init__(
        self,
        independent_naming: bool = None,
        instance_name: str = None,
        release_time: int = None,
        instance_status: int = None,
        tags: List[OnsInstanceInServiceListResponseBodyDataTags] = None,
        instance_id: str = None,
        instance_type: int = None,
    ):
        self.independent_naming = independent_naming
        self.instance_name = instance_name
        self.release_time = release_time
        self.instance_status = instance_status
        self.tags = tags
        self.instance_id = instance_id
        self.instance_type = instance_type

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = OnsInstanceInServiceListResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        return self


class OnsInstanceInServiceListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[OnsInstanceInServiceListResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OnsInstanceInServiceListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class OnsInstanceInServiceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsInstanceInServiceListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsInstanceInServiceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsInstanceUpdateRequest(TeaModel):
    def __init__(
        self,
        remark: str = None,
        instance_name: str = None,
        instance_id: str = None,
    ):
        self.remark = remark
        self.instance_name = instance_name
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsInstanceUpdateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsInstanceUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsInstanceUpdateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsInstanceUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessageGetByKeyRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        key: str = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.key = key
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.key is not None:
            result['Key'] = self.key
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMessageGetByKeyResponseBodyDataPropertyList(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class OnsMessageGetByKeyResponseBodyData(TeaModel):
    def __init__(
        self,
        store_size: int = None,
        reconsume_times: int = None,
        store_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        store_host: str = None,
        topic: str = None,
        property_list: List[OnsMessageGetByKeyResponseBodyDataPropertyList] = None,
        born_timestamp: int = None,
        body_crc: int = None,
        born_host: str = None,
    ):
        self.store_size = store_size
        self.reconsume_times = reconsume_times
        self.store_timestamp = store_timestamp
        self.instance_id = instance_id
        self.msg_id = msg_id
        self.store_host = store_host
        self.topic = topic
        self.property_list = property_list
        self.born_timestamp = born_timestamp
        self.body_crc = body_crc
        self.born_host = born_host

    def validate(self):
        if self.property_list:
            for k in self.property_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.topic is not None:
            result['Topic'] = self.topic
        result['PropertyList'] = []
        if self.property_list is not None:
            for k in self.property_list:
                result['PropertyList'].append(k.to_map() if k else None)
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        self.property_list = []
        if m.get('PropertyList') is not None:
            for k in m.get('PropertyList'):
                temp_model = OnsMessageGetByKeyResponseBodyDataPropertyList()
                self.property_list.append(temp_model.from_map(k))
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        return self


class OnsMessageGetByKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[OnsMessageGetByKeyResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OnsMessageGetByKeyResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class OnsMessageGetByKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMessageGetByKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMessageGetByKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessageGetByMsgIdRequest(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
        topic: str = None,
        instance_id: str = None,
    ):
        self.msg_id = msg_id
        self.topic = topic
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMessageGetByMsgIdResponseBodyDataPropertyList(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class OnsMessageGetByMsgIdResponseBodyData(TeaModel):
    def __init__(
        self,
        store_size: int = None,
        reconsume_times: int = None,
        store_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        store_host: str = None,
        topic: str = None,
        property_list: List[OnsMessageGetByMsgIdResponseBodyDataPropertyList] = None,
        born_timestamp: int = None,
        body_crc: int = None,
        born_host: str = None,
    ):
        self.store_size = store_size
        self.reconsume_times = reconsume_times
        self.store_timestamp = store_timestamp
        self.instance_id = instance_id
        self.msg_id = msg_id
        self.store_host = store_host
        self.topic = topic
        self.property_list = property_list
        self.born_timestamp = born_timestamp
        self.body_crc = body_crc
        self.born_host = born_host

    def validate(self):
        if self.property_list:
            for k in self.property_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.topic is not None:
            result['Topic'] = self.topic
        result['PropertyList'] = []
        if self.property_list is not None:
            for k in self.property_list:
                result['PropertyList'].append(k.to_map() if k else None)
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        self.property_list = []
        if m.get('PropertyList') is not None:
            for k in m.get('PropertyList'):
                temp_model = OnsMessageGetByMsgIdResponseBodyDataPropertyList()
                self.property_list.append(temp_model.from_map(k))
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        return self


class OnsMessageGetByMsgIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsMessageGetByMsgIdResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsMessageGetByMsgIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsMessageGetByMsgIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMessageGetByMsgIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMessageGetByMsgIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessagePageQueryByTopicRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        begin_time: int = None,
        end_time: int = None,
        task_id: str = None,
        current_page: int = None,
        page_size: int = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.begin_time = begin_time
        self.end_time = end_time
        self.task_id = task_id
        self.current_page = current_page
        self.page_size = page_size
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListPropertyList(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundList(TeaModel):
    def __init__(
        self,
        store_size: int = None,
        reconsume_times: int = None,
        store_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        store_host: str = None,
        topic: str = None,
        property_list: List[OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListPropertyList] = None,
        born_timestamp: int = None,
        body_crc: int = None,
        born_host: str = None,
    ):
        self.store_size = store_size
        self.reconsume_times = reconsume_times
        self.store_timestamp = store_timestamp
        self.instance_id = instance_id
        self.msg_id = msg_id
        self.store_host = store_host
        self.topic = topic
        self.property_list = property_list
        self.born_timestamp = born_timestamp
        self.body_crc = body_crc
        self.born_host = born_host

    def validate(self):
        if self.property_list:
            for k in self.property_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.topic is not None:
            result['Topic'] = self.topic
        result['PropertyList'] = []
        if self.property_list is not None:
            for k in self.property_list:
                result['PropertyList'].append(k.to_map() if k else None)
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        self.property_list = []
        if m.get('PropertyList') is not None:
            for k in m.get('PropertyList'):
                temp_model = OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListPropertyList()
                self.property_list.append(temp_model.from_map(k))
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        return self


class OnsMessagePageQueryByTopicResponseBodyMsgFoundDo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        msg_found_list: List[OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundList] = None,
        max_page_count: int = None,
        task_id: str = None,
    ):
        self.current_page = current_page
        self.msg_found_list = msg_found_list
        self.max_page_count = max_page_count
        self.task_id = task_id

    def validate(self):
        if self.msg_found_list:
            for k in self.msg_found_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['MsgFoundList'] = []
        if self.msg_found_list is not None:
            for k in self.msg_found_list:
                result['MsgFoundList'].append(k.to_map() if k else None)
        if self.max_page_count is not None:
            result['MaxPageCount'] = self.max_page_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.msg_found_list = []
        if m.get('MsgFoundList') is not None:
            for k in m.get('MsgFoundList'):
                temp_model = OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundList()
                self.msg_found_list.append(temp_model.from_map(k))
        if m.get('MaxPageCount') is not None:
            self.max_page_count = m.get('MaxPageCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OnsMessagePageQueryByTopicResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        msg_found_do: OnsMessagePageQueryByTopicResponseBodyMsgFoundDo = None,
    ):
        self.request_id = request_id
        self.msg_found_do = msg_found_do

    def validate(self):
        if self.msg_found_do:
            self.msg_found_do.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.msg_found_do is not None:
            result['MsgFoundDo'] = self.msg_found_do.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MsgFoundDo') is not None:
            temp_model = OnsMessagePageQueryByTopicResponseBodyMsgFoundDo()
            self.msg_found_do = temp_model.from_map(m['MsgFoundDo'])
        return self


class OnsMessagePageQueryByTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMessagePageQueryByTopicResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMessagePageQueryByTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessagePushRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        client_id: str = None,
        msg_id: str = None,
        topic: str = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.client_id = client_id
        self.msg_id = msg_id
        self.topic = topic
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMessagePushResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsMessagePushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMessagePushResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMessagePushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessageSendRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        tag: str = None,
        key: str = None,
        message: str = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.tag = tag
        self.key = key
        self.message = message
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.key is not None:
            result['Key'] = self.key
        if self.message is not None:
            result['Message'] = self.message
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMessageSendResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class OnsMessageSendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMessageSendResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMessageSendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessageTraceRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        msg_id: str = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.msg_id = msg_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMessageTraceResponseBodyData(TeaModel):
    def __init__(
        self,
        track_type: str = None,
        consumer_group: str = None,
        instance_id: str = None,
    ):
        self.track_type = track_type
        self.consumer_group = consumer_group
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.track_type is not None:
            result['TrackType'] = self.track_type
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrackType') is not None:
            self.track_type = m.get('TrackType')
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMessageTraceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[OnsMessageTraceResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OnsMessageTraceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class OnsMessageTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMessageTraceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMessageTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMqttGroupIdCreateRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        group_id: str = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.group_id = group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMqttGroupIdCreateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsMqttGroupIdCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMqttGroupIdCreateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMqttGroupIdCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMqttGroupIdDeleteRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMqttGroupIdDeleteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsMqttGroupIdDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMqttGroupIdDeleteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMqttGroupIdDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMqttGroupIdListRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMqttGroupIdListResponseBodyData(TeaModel):
    def __init__(
        self,
        update_time: int = None,
        independent_naming: bool = None,
        group_id: str = None,
        create_time: int = None,
        instance_id: str = None,
    ):
        self.update_time = update_time
        self.independent_naming = independent_naming
        self.group_id = group_id
        self.create_time = create_time
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMqttGroupIdListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[OnsMqttGroupIdListResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OnsMqttGroupIdListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class OnsMqttGroupIdListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMqttGroupIdListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMqttGroupIdListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMqttQueryClientByClientIdRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        instance_id: str = None,
    ):
        self.client_id = client_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMqttQueryClientByClientIdResponseBodyMqttClientInfoDoSubScriptonData(TeaModel):
    def __init__(
        self,
        sub_topic: str = None,
        parent_topic: str = None,
        qos: int = None,
    ):
        self.sub_topic = sub_topic
        self.parent_topic = parent_topic
        self.qos = qos

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.sub_topic is not None:
            result['SubTopic'] = self.sub_topic
        if self.parent_topic is not None:
            result['ParentTopic'] = self.parent_topic
        if self.qos is not None:
            result['Qos'] = self.qos
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubTopic') is not None:
            self.sub_topic = m.get('SubTopic')
        if m.get('ParentTopic') is not None:
            self.parent_topic = m.get('ParentTopic')
        if m.get('Qos') is not None:
            self.qos = m.get('Qos')
        return self


class OnsMqttQueryClientByClientIdResponseBodyMqttClientInfoDo(TeaModel):
    def __init__(
        self,
        online: bool = None,
        last_touch: int = None,
        socket_channel: str = None,
        client_id: str = None,
        sub_scripton_data: List[OnsMqttQueryClientByClientIdResponseBodyMqttClientInfoDoSubScriptonData] = None,
    ):
        self.online = online
        self.last_touch = last_touch
        self.socket_channel = socket_channel
        self.client_id = client_id
        self.sub_scripton_data = sub_scripton_data

    def validate(self):
        if self.sub_scripton_data:
            for k in self.sub_scripton_data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.online is not None:
            result['Online'] = self.online
        if self.last_touch is not None:
            result['LastTouch'] = self.last_touch
        if self.socket_channel is not None:
            result['SocketChannel'] = self.socket_channel
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        result['SubScriptonData'] = []
        if self.sub_scripton_data is not None:
            for k in self.sub_scripton_data:
                result['SubScriptonData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('LastTouch') is not None:
            self.last_touch = m.get('LastTouch')
        if m.get('SocketChannel') is not None:
            self.socket_channel = m.get('SocketChannel')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        self.sub_scripton_data = []
        if m.get('SubScriptonData') is not None:
            for k in m.get('SubScriptonData'):
                temp_model = OnsMqttQueryClientByClientIdResponseBodyMqttClientInfoDoSubScriptonData()
                self.sub_scripton_data.append(temp_model.from_map(k))
        return self


class OnsMqttQueryClientByClientIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        mqtt_client_info_do: OnsMqttQueryClientByClientIdResponseBodyMqttClientInfoDo = None,
    ):
        self.request_id = request_id
        self.mqtt_client_info_do = mqtt_client_info_do

    def validate(self):
        if self.mqtt_client_info_do:
            self.mqtt_client_info_do.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mqtt_client_info_do is not None:
            result['MqttClientInfoDo'] = self.mqtt_client_info_do.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MqttClientInfoDo') is not None:
            temp_model = OnsMqttQueryClientByClientIdResponseBodyMqttClientInfoDo()
            self.mqtt_client_info_do = temp_model.from_map(m['MqttClientInfoDo'])
        return self


class OnsMqttQueryClientByClientIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMqttQueryClientByClientIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMqttQueryClientByClientIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMqttQueryClientByGroupIdRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMqttQueryClientByGroupIdResponseBodyMqttClientSetDo(TeaModel):
    def __init__(
        self,
        online_count: int = None,
    ):
        self.online_count = online_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        return self


class OnsMqttQueryClientByGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        mqtt_client_set_do: OnsMqttQueryClientByGroupIdResponseBodyMqttClientSetDo = None,
    ):
        self.request_id = request_id
        self.mqtt_client_set_do = mqtt_client_set_do

    def validate(self):
        if self.mqtt_client_set_do:
            self.mqtt_client_set_do.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mqtt_client_set_do is not None:
            result['MqttClientSetDo'] = self.mqtt_client_set_do.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MqttClientSetDo') is not None:
            temp_model = OnsMqttQueryClientByGroupIdResponseBodyMqttClientSetDo()
            self.mqtt_client_set_do = temp_model.from_map(m['MqttClientSetDo'])
        return self


class OnsMqttQueryClientByGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMqttQueryClientByGroupIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMqttQueryClientByGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMqttQueryClientByTopicRequest(TeaModel):
    def __init__(
        self,
        parent_topic: str = None,
        sub_topic: str = None,
        instance_id: str = None,
    ):
        self.parent_topic = parent_topic
        self.sub_topic = sub_topic
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.parent_topic is not None:
            result['ParentTopic'] = self.parent_topic
        if self.sub_topic is not None:
            result['SubTopic'] = self.sub_topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentTopic') is not None:
            self.parent_topic = m.get('ParentTopic')
        if m.get('SubTopic') is not None:
            self.sub_topic = m.get('SubTopic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMqttQueryClientByTopicResponseBodyMqttClientSetDo(TeaModel):
    def __init__(
        self,
        online_count: int = None,
    ):
        self.online_count = online_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        return self


class OnsMqttQueryClientByTopicResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        mqtt_client_set_do: OnsMqttQueryClientByTopicResponseBodyMqttClientSetDo = None,
    ):
        self.request_id = request_id
        self.mqtt_client_set_do = mqtt_client_set_do

    def validate(self):
        if self.mqtt_client_set_do:
            self.mqtt_client_set_do.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.mqtt_client_set_do is not None:
            result['MqttClientSetDo'] = self.mqtt_client_set_do.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('MqttClientSetDo') is not None:
            temp_model = OnsMqttQueryClientByTopicResponseBodyMqttClientSetDo()
            self.mqtt_client_set_do = temp_model.from_map(m['MqttClientSetDo'])
        return self


class OnsMqttQueryClientByTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMqttQueryClientByTopicResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMqttQueryClientByTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMqttQueryHistoryOnlineRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMqttQueryHistoryOnlineResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        y: float = None,
        x: int = None,
    ):
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class OnsMqttQueryHistoryOnlineResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[OnsMqttQueryHistoryOnlineResponseBodyDataRecords] = None,
        xunit: str = None,
        yunit: str = None,
        title: str = None,
    ):
        self.records = records
        self.xunit = xunit
        self.yunit = yunit
        self.title = title

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.xunit is not None:
            result['XUnit'] = self.xunit
        if self.yunit is not None:
            result['YUnit'] = self.yunit
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = OnsMqttQueryHistoryOnlineResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('XUnit') is not None:
            self.xunit = m.get('XUnit')
        if m.get('YUnit') is not None:
            self.yunit = m.get('YUnit')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class OnsMqttQueryHistoryOnlineResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsMqttQueryHistoryOnlineResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsMqttQueryHistoryOnlineResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsMqttQueryHistoryOnlineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMqttQueryHistoryOnlineResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMqttQueryHistoryOnlineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMqttQueryMsgTransTrendRequest(TeaModel):
    def __init__(
        self,
        tps_type: str = None,
        trans_type: str = None,
        parent_topic: str = None,
        sub_topic: str = None,
        msg_type: str = None,
        qos: int = None,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
    ):
        self.tps_type = tps_type
        self.trans_type = trans_type
        self.parent_topic = parent_topic
        self.sub_topic = sub_topic
        self.msg_type = msg_type
        self.qos = qos
        self.begin_time = begin_time
        self.end_time = end_time
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.tps_type is not None:
            result['TpsType'] = self.tps_type
        if self.trans_type is not None:
            result['TransType'] = self.trans_type
        if self.parent_topic is not None:
            result['ParentTopic'] = self.parent_topic
        if self.sub_topic is not None:
            result['SubTopic'] = self.sub_topic
        if self.msg_type is not None:
            result['MsgType'] = self.msg_type
        if self.qos is not None:
            result['Qos'] = self.qos
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TpsType') is not None:
            self.tps_type = m.get('TpsType')
        if m.get('TransType') is not None:
            self.trans_type = m.get('TransType')
        if m.get('ParentTopic') is not None:
            self.parent_topic = m.get('ParentTopic')
        if m.get('SubTopic') is not None:
            self.sub_topic = m.get('SubTopic')
        if m.get('MsgType') is not None:
            self.msg_type = m.get('MsgType')
        if m.get('Qos') is not None:
            self.qos = m.get('Qos')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsMqttQueryMsgTransTrendResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        y: float = None,
        x: int = None,
    ):
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class OnsMqttQueryMsgTransTrendResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[OnsMqttQueryMsgTransTrendResponseBodyDataRecords] = None,
        xunit: str = None,
        yunit: str = None,
        title: str = None,
    ):
        self.records = records
        self.xunit = xunit
        self.yunit = yunit
        self.title = title

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.xunit is not None:
            result['XUnit'] = self.xunit
        if self.yunit is not None:
            result['YUnit'] = self.yunit
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = OnsMqttQueryMsgTransTrendResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('XUnit') is not None:
            self.xunit = m.get('XUnit')
        if m.get('YUnit') is not None:
            self.yunit = m.get('YUnit')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class OnsMqttQueryMsgTransTrendResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsMqttQueryMsgTransTrendResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsMqttQueryMsgTransTrendResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsMqttQueryMsgTransTrendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsMqttQueryMsgTransTrendResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsMqttQueryMsgTransTrendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsRegionListResponseBodyData(TeaModel):
    def __init__(
        self,
        region_name: str = None,
        ons_region_id: str = None,
    ):
        self.region_name = region_name
        self.ons_region_id = ons_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.ons_region_id is not None:
            result['OnsRegionId'] = self.ons_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('OnsRegionId') is not None:
            self.ons_region_id = m.get('OnsRegionId')
        return self


class OnsRegionListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[OnsRegionListResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OnsRegionListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class OnsRegionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsRegionListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsRegionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicCreateRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        message_type: int = None,
        remark: str = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.message_type = message_type
        self.remark = remark
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsTopicCreateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTopicCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTopicCreateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTopicCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicDeleteRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsTopicDeleteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTopicDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTopicDeleteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTopicDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicListRequestTag(TeaModel):
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


class OnsTopicListRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        instance_id: str = None,
        tag: List[OnsTopicListRequestTag] = None,
    ):
        self.topic = topic
        self.instance_id = instance_id
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = OnsTopicListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class OnsTopicListResponseBodyDataTags(TeaModel):
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


class OnsTopicListResponseBodyData(TeaModel):
    def __init__(
        self,
        message_type: int = None,
        relation_name: str = None,
        owner: str = None,
        independent_naming: bool = None,
        remark: str = None,
        relation: int = None,
        create_time: int = None,
        topic: str = None,
        tags: List[OnsTopicListResponseBodyDataTags] = None,
        instance_id: str = None,
    ):
        self.message_type = message_type
        self.relation_name = relation_name
        self.owner = owner
        self.independent_naming = independent_naming
        self.remark = remark
        self.relation = relation
        self.create_time = create_time
        self.topic = topic
        self.tags = tags
        self.instance_id = instance_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.relation_name is not None:
            result['RelationName'] = self.relation_name
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.topic is not None:
            result['Topic'] = self.topic
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('RelationName') is not None:
            self.relation_name = m.get('RelationName')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = OnsTopicListResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsTopicListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[OnsTopicListResponseBodyData] = None,
        help_url: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.help_url = help_url

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.help_url is not None:
            result['HelpUrl'] = self.help_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = OnsTopicListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HelpUrl') is not None:
            self.help_url = m.get('HelpUrl')
        return self


class OnsTopicListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTopicListResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTopicListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicStatusRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsTopicStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        perm: int = None,
        last_time_stamp: int = None,
        total_count: int = None,
    ):
        self.perm = perm
        self.last_time_stamp = last_time_stamp
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.perm is not None:
            result['Perm'] = self.perm
        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Perm') is not None:
            self.perm = m.get('Perm')
        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class OnsTopicStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsTopicStatusResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsTopicStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsTopicStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTopicStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTopicStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicSubDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        topic: str = None,
    ):
        self.instance_id = instance_id
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTopicSubDetailResponseBodyDataSubscriptionDataList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        message_model: str = None,
        sub_string: str = None,
    ):
        self.group_id = group_id
        self.message_model = message_model
        self.sub_string = sub_string

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.message_model is not None:
            result['MessageModel'] = self.message_model
        if self.sub_string is not None:
            result['SubString'] = self.sub_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MessageModel') is not None:
            self.message_model = m.get('MessageModel')
        if m.get('SubString') is not None:
            self.sub_string = m.get('SubString')
        return self


class OnsTopicSubDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        subscription_data_list: List[OnsTopicSubDetailResponseBodyDataSubscriptionDataList] = None,
        topic: str = None,
    ):
        self.subscription_data_list = subscription_data_list
        self.topic = topic

    def validate(self):
        if self.subscription_data_list:
            for k in self.subscription_data_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['SubscriptionDataList'] = []
        if self.subscription_data_list is not None:
            for k in self.subscription_data_list:
                result['SubscriptionDataList'].append(k.to_map() if k else None)
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_data_list = []
        if m.get('SubscriptionDataList') is not None:
            for k in m.get('SubscriptionDataList'):
                temp_model = OnsTopicSubDetailResponseBodyDataSubscriptionDataList()
                self.subscription_data_list.append(temp_model.from_map(k))
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTopicSubDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsTopicSubDetailResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsTopicSubDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsTopicSubDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTopicSubDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTopicSubDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicUpdateRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        perm: int = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.perm = perm
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.perm is not None:
            result['Perm'] = self.perm
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Perm') is not None:
            self.perm = m.get('Perm')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsTopicUpdateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTopicUpdateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTopicUpdateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTopicUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTraceGetResultRequest(TeaModel):
    def __init__(
        self,
        query_id: str = None,
    ):
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class OnsTraceGetResultResponseBodyTraceDataTraceListSubListClientList(TeaModel):
    def __init__(
        self,
        status: str = None,
        sub_time: int = None,
        reconsume_times: int = None,
        sub_group_name: str = None,
        client_host: str = None,
        cost_time: int = None,
    ):
        self.status = status
        self.sub_time = sub_time
        self.reconsume_times = reconsume_times
        self.sub_group_name = sub_group_name
        self.client_host = client_host
        self.cost_time = cost_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_time is not None:
            result['SubTime'] = self.sub_time
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.sub_group_name is not None:
            result['SubGroupName'] = self.sub_group_name
        if self.client_host is not None:
            result['ClientHost'] = self.client_host
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubTime') is not None:
            self.sub_time = m.get('SubTime')
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('SubGroupName') is not None:
            self.sub_group_name = m.get('SubGroupName')
        if m.get('ClientHost') is not None:
            self.client_host = m.get('ClientHost')
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        return self


class OnsTraceGetResultResponseBodyTraceDataTraceListSubList(TeaModel):
    def __init__(
        self,
        client_list: List[OnsTraceGetResultResponseBodyTraceDataTraceListSubListClientList] = None,
        fail_count: int = None,
        sub_group_name: str = None,
        success_count: int = None,
    ):
        self.client_list = client_list
        self.fail_count = fail_count
        self.sub_group_name = sub_group_name
        self.success_count = success_count

    def validate(self):
        if self.client_list:
            for k in self.client_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['ClientList'] = []
        if self.client_list is not None:
            for k in self.client_list:
                result['ClientList'].append(k.to_map() if k else None)
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.sub_group_name is not None:
            result['SubGroupName'] = self.sub_group_name
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.client_list = []
        if m.get('ClientList') is not None:
            for k in m.get('ClientList'):
                temp_model = OnsTraceGetResultResponseBodyTraceDataTraceListSubListClientList()
                self.client_list.append(temp_model.from_map(k))
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('SubGroupName') is not None:
            self.sub_group_name = m.get('SubGroupName')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class OnsTraceGetResultResponseBodyTraceDataTraceList(TeaModel):
    def __init__(
        self,
        status: str = None,
        msg_key: str = None,
        pub_time: int = None,
        sub_list: List[OnsTraceGetResultResponseBodyTraceDataTraceListSubList] = None,
        topic: str = None,
        cost_time: int = None,
        tag: str = None,
        msg_id: str = None,
        pub_group_name: str = None,
        born_host: str = None,
    ):
        self.status = status
        self.msg_key = msg_key
        self.pub_time = pub_time
        self.sub_list = sub_list
        self.topic = topic
        self.cost_time = cost_time
        self.tag = tag
        self.msg_id = msg_id
        self.pub_group_name = pub_group_name
        self.born_host = born_host

    def validate(self):
        if self.sub_list:
            for k in self.sub_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        result['SubList'] = []
        if self.sub_list is not None:
            for k in self.sub_list:
                result['SubList'].append(k.to_map() if k else None)
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.pub_group_name is not None:
            result['PubGroupName'] = self.pub_group_name
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        self.sub_list = []
        if m.get('SubList') is not None:
            for k in m.get('SubList'):
                temp_model = OnsTraceGetResultResponseBodyTraceDataTraceListSubList()
                self.sub_list.append(temp_model.from_map(k))
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('PubGroupName') is not None:
            self.pub_group_name = m.get('PubGroupName')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        return self


class OnsTraceGetResultResponseBodyTraceData(TeaModel):
    def __init__(
        self,
        status: str = None,
        msg_key: str = None,
        update_time: int = None,
        create_time: int = None,
        topic: str = None,
        user_id: str = None,
        instance_id: str = None,
        msg_id: str = None,
        trace_list: List[OnsTraceGetResultResponseBodyTraceDataTraceList] = None,
        query_id: str = None,
    ):
        self.status = status
        self.msg_key = msg_key
        self.update_time = update_time
        self.create_time = create_time
        self.topic = topic
        self.user_id = user_id
        self.instance_id = instance_id
        self.msg_id = msg_id
        self.trace_list = trace_list
        self.query_id = query_id

    def validate(self):
        if self.trace_list:
            for k in self.trace_list:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        result['TraceList'] = []
        if self.trace_list is not None:
            for k in self.trace_list:
                result['TraceList'].append(k.to_map() if k else None)
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        self.trace_list = []
        if m.get('TraceList') is not None:
            for k in m.get('TraceList'):
                temp_model = OnsTraceGetResultResponseBodyTraceDataTraceList()
                self.trace_list.append(temp_model.from_map(k))
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class OnsTraceGetResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_data: OnsTraceGetResultResponseBodyTraceData = None,
    ):
        self.request_id = request_id
        self.trace_data = trace_data

    def validate(self):
        if self.trace_data:
            self.trace_data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trace_data is not None:
            result['TraceData'] = self.trace_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TraceData') is not None:
            temp_model = OnsTraceGetResultResponseBodyTraceData()
            self.trace_data = temp_model.from_map(m['TraceData'])
        return self


class OnsTraceGetResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTraceGetResultResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTraceGetResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTraceQueryByMsgIdRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        msg_id: str = None,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.msg_id = msg_id
        self.begin_time = begin_time
        self.end_time = end_time
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsTraceQueryByMsgIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        query_id: str = None,
    ):
        self.request_id = request_id
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class OnsTraceQueryByMsgIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTraceQueryByMsgIdResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTraceQueryByMsgIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTraceQueryByMsgKeyRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        msg_key: str = None,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
    ):
        self.topic = topic
        self.msg_key = msg_key
        self.begin_time = begin_time
        self.end_time = end_time
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsTraceQueryByMsgKeyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        query_id: str = None,
    ):
        self.request_id = request_id
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class OnsTraceQueryByMsgKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTraceQueryByMsgKeyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTraceQueryByMsgKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTrendGroupOutputTpsRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        topic: str = None,
        begin_time: int = None,
        end_time: int = None,
        type: int = None,
        instance_id: str = None,
        period: int = None,
    ):
        self.group_id = group_id
        self.topic = topic
        self.begin_time = begin_time
        self.end_time = end_time
        self.type = type
        self.instance_id = instance_id
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.type is not None:
            result['Type'] = self.type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period is not None:
            result['Period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        return self


class OnsTrendGroupOutputTpsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        y: float = None,
        x: int = None,
    ):
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class OnsTrendGroupOutputTpsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[OnsTrendGroupOutputTpsResponseBodyDataRecords] = None,
        xunit: str = None,
        yunit: str = None,
        title: str = None,
    ):
        self.records = records
        self.xunit = xunit
        self.yunit = yunit
        self.title = title

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.xunit is not None:
            result['XUnit'] = self.xunit
        if self.yunit is not None:
            result['YUnit'] = self.yunit
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = OnsTrendGroupOutputTpsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('XUnit') is not None:
            self.xunit = m.get('XUnit')
        if m.get('YUnit') is not None:
            self.yunit = m.get('YUnit')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class OnsTrendGroupOutputTpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsTrendGroupOutputTpsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsTrendGroupOutputTpsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsTrendGroupOutputTpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTrendGroupOutputTpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTrendGroupOutputTpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTrendTopicInputTpsRequest(TeaModel):
    def __init__(
        self,
        topic: str = None,
        begin_time: int = None,
        end_time: int = None,
        type: int = None,
        instance_id: str = None,
        period: int = None,
    ):
        self.topic = topic
        self.begin_time = begin_time
        self.end_time = end_time
        self.type = type
        self.instance_id = instance_id
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.type is not None:
            result['Type'] = self.type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period is not None:
            result['Period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        return self


class OnsTrendTopicInputTpsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        y: float = None,
        x: int = None,
    ):
        self.y = y
        self.x = x

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.y is not None:
            result['Y'] = self.y
        if self.x is not None:
            result['X'] = self.x
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Y') is not None:
            self.y = m.get('Y')
        if m.get('X') is not None:
            self.x = m.get('X')
        return self


class OnsTrendTopicInputTpsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: List[OnsTrendTopicInputTpsResponseBodyDataRecords] = None,
        xunit: str = None,
        yunit: str = None,
        title: str = None,
    ):
        self.records = records
        self.xunit = xunit
        self.yunit = yunit
        self.title = title

    def validate(self):
        if self.records:
            for k in self.records:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.xunit is not None:
            result['XUnit'] = self.xunit
        if self.yunit is not None:
            result['YUnit'] = self.yunit
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = OnsTrendTopicInputTpsResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('XUnit') is not None:
            self.xunit = m.get('XUnit')
        if m.get('YUnit') is not None:
            self.yunit = m.get('YUnit')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class OnsTrendTopicInputTpsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: OnsTrendTopicInputTpsResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = OnsTrendTopicInputTpsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class OnsTrendTopicInputTpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsTrendTopicInputTpsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsTrendTopicInputTpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsWarnCreateRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        topic: str = None,
        threshold: str = None,
        contacts: str = None,
        delay_time: str = None,
        block_time: str = None,
        alert_time: str = None,
        level: str = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.topic = topic
        self.threshold = threshold
        self.contacts = contacts
        self.delay_time = delay_time
        self.block_time = block_time
        self.alert_time = alert_time
        self.level = level
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.threshold is not None:
            result['Threshold'] = self.threshold
        if self.contacts is not None:
            result['Contacts'] = self.contacts
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.block_time is not None:
            result['BlockTime'] = self.block_time
        if self.alert_time is not None:
            result['AlertTime'] = self.alert_time
        if self.level is not None:
            result['Level'] = self.level
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')
        if m.get('Contacts') is not None:
            self.contacts = m.get('Contacts')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('BlockTime') is not None:
            self.block_time = m.get('BlockTime')
        if m.get('AlertTime') is not None:
            self.alert_time = m.get('AlertTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsWarnCreateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsWarnCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsWarnCreateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsWarnCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsWarnDeleteRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        topic: str = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.topic = topic
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsWarnDeleteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsWarnDeleteResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OnsWarnDeleteResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OnsWarnDeleteResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenOnsServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        order_id: str = None,
    ):
        self.request_id = request_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        return self


class OpenOnsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenOnsServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenOnsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
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


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
        resource_id: List[str] = None,
    ):
        self.instance_id = instance_id
        self.resource_type = resource_type
        self.tag = tag
        self.resource_id = resource_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_type: str = None,
        all: bool = None,
        resource_id: List[str] = None,
        tag_key: List[str] = None,
    ):
        self.instance_id = instance_id
        self.resource_type = resource_type
        self.all = all
        self.resource_id = resource_id
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.all is not None:
            result['All'] = self.all
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


