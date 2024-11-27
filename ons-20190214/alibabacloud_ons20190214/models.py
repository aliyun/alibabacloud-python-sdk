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
        # The key of the tag that you want to detach from the resource.
        # 
        # *   If you include this parameter in a request, the value of this parameter cannot be an empty string.
        # *   The tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag that you want to query.
        # 
        # *   The value of this parameter can be an empty string.
        # *   The tag key must be 1 to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        next_token: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The ID of the ApsaraMQ for RocketMQ instance to which the resource whose tags you want to query belongs.
        # 
        # > This parameter is required when you query the tags of a topic or a group.
        self.instance_id = instance_id
        # The token that determines the start point of the next query.
        self.next_token = next_token
        # The list of resource IDs.
        self.resource_id = resource_id
        # The type of the resource whose tags you want to query. Valid values:
        # 
        # *   **INSTANCE**\
        # *   **TOPIC**\
        # *   **GROUP**\
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to query. A maximum of 20 tags can be included in the list.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The ID of the instance
        self.instance_id = instance_id
        # Indicates the ID of the resource.
        self.resource_id = resource_id
        # The type of the resource whose tags you want to query.
        # 
        # *   ALIYUN::MQ::INSTANCE: indicates that the resource is a ApsaraMQ for RocketMQ instance.
        # *   ALIYUN::MQ::TOPIC: indicates that the resource is a topic.
        # *   ALIYUN::MQ::GROUP: indicates that the resource is a group.
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: List[ListTagResourcesResponseBodyTagResources] = None,
    ):
        # The token that determines the start point of the next query.
        self.next_token = next_token
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Details of the resource and tags, including the resource ID, the resource type, tag keys, and tag values.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsConsumerAccumulateRequest(TeaModel):
    def __init__(
        self,
        detail: bool = None,
        group_id: str = None,
        instance_id: str = None,
    ):
        # Specifies whether to query the details of each topic to which the consumer group subscribes. Valid values:
        # 
        # *   **true**: The details of each topic are queried. You can obtain the details from the **DetailInTopicList** response parameter.
        # *   **false**: The details of each topic are not queried. This is the default value. If you use this value, the value of the **DetailInTopicList** response parameter is empty.
        self.detail = detail
        # The ID of the consumer group.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class OnsConsumerAccumulateResponseBodyDataDetailInTopicListDetailInTopicDo(TeaModel):
    def __init__(
        self,
        delay_time: int = None,
        last_timestamp: int = None,
        topic: str = None,
        total_diff: int = None,
    ):
        # The maximum latency of message consumption in the topic.
        self.delay_time = delay_time
        # The point in time when the latest consumed message in the topic was produced.
        self.last_timestamp = last_timestamp
        # The topic name.
        self.topic = topic
        # The number of accumulated messages in the topic.
        self.total_diff = total_diff

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class OnsConsumerAccumulateResponseBodyDataDetailInTopicList(TeaModel):
    def __init__(
        self,
        detail_in_topic_do: List[OnsConsumerAccumulateResponseBodyDataDetailInTopicListDetailInTopicDo] = None,
    ):
        self.detail_in_topic_do = detail_in_topic_do

    def validate(self):
        if self.detail_in_topic_do:
            for k in self.detail_in_topic_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailInTopicDo'] = []
        if self.detail_in_topic_do is not None:
            for k in self.detail_in_topic_do:
                result['DetailInTopicDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_in_topic_do = []
        if m.get('DetailInTopicDo') is not None:
            for k in m.get('DetailInTopicDo'):
                temp_model = OnsConsumerAccumulateResponseBodyDataDetailInTopicListDetailInTopicDo()
                self.detail_in_topic_do.append(temp_model.from_map(k))
        return self


class OnsConsumerAccumulateResponseBodyData(TeaModel):
    def __init__(
        self,
        consume_tps: float = None,
        delay_time: int = None,
        detail_in_topic_list: OnsConsumerAccumulateResponseBodyDataDetailInTopicList = None,
        last_timestamp: int = None,
        online: bool = None,
        total_diff: int = None,
    ):
        # The transactions per second (TPS) for message consumption performed by consumers in the group.
        self.consume_tps = consume_tps
        # The consumption latency.
        self.delay_time = delay_time
        # The information about each topic to which the consumer group subscribes. If the **Detail** parameter in the request is set to **false**, the value of this parameter is empty.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = OnsConsumerAccumulateResponseBodyDataDetailInTopicList()
            self.detail_in_topic_list = temp_model.from_map(m['DetailInTopicList'])
        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('TotalDiff') is not None:
            self.total_diff = m.get('TotalDiff')
        return self


class OnsConsumerAccumulateResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsConsumerAccumulateResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsConsumerAccumulateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsConsumerAccumulateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsConsumerAccumulateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The ID of the consumer group whose client connection status you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsConsumerGetConnectionResponseBodyDataConnectionListConnectionDo(TeaModel):
    def __init__(
        self,
        client_addr: str = None,
        client_id: str = None,
        language: str = None,
        version: str = None,
    ):
        # The IP address and port number of the consumer client.
        self.client_addr = client_addr
        # The ID of the consumer client.
        self.client_id = client_id
        # The programming language in which the consumer application was developed.
        self.language = language
        # The version of the consumer client.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.language is not None:
            result['Language'] = self.language
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientAddr') is not None:
            self.client_addr = m.get('ClientAddr')
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class OnsConsumerGetConnectionResponseBodyDataConnectionList(TeaModel):
    def __init__(
        self,
        connection_do: List[OnsConsumerGetConnectionResponseBodyDataConnectionListConnectionDo] = None,
    ):
        self.connection_do = connection_do

    def validate(self):
        if self.connection_do:
            for k in self.connection_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionDo'] = []
        if self.connection_do is not None:
            for k in self.connection_do:
                result['ConnectionDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_do = []
        if m.get('ConnectionDo') is not None:
            for k in m.get('ConnectionDo'):
                temp_model = OnsConsumerGetConnectionResponseBodyDataConnectionListConnectionDo()
                self.connection_do.append(temp_model.from_map(k))
        return self


class OnsConsumerGetConnectionResponseBodyData(TeaModel):
    def __init__(
        self,
        connection_list: OnsConsumerGetConnectionResponseBodyDataConnectionList = None,
    ):
        # The client connection information of the consumer group.
        self.connection_list = connection_list

    def validate(self):
        if self.connection_list:
            self.connection_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.connection_list is not None:
            result['ConnectionList'] = self.connection_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionList') is not None:
            temp_model = OnsConsumerGetConnectionResponseBodyDataConnectionList()
            self.connection_list = temp_model.from_map(m['ConnectionList'])
        return self


class OnsConsumerGetConnectionResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsConsumerGetConnectionResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsConsumerGetConnectionResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsConsumerGetConnectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsConsumerGetConnectionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsConsumerGetConnectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsConsumerResetOffsetRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        reset_timestamp: int = None,
        topic: str = None,
        type: int = None,
    ):
        # The ID of the consumer group whose dead-letter message you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id
        # The timestamp to which you want to reset the consumer offset. This parameter takes effect only when the **Type** parameter is set to **1**. Unit: milliseconds.
        self.reset_timestamp = reset_timestamp
        # The name of the topic for which you want to reset the consumer offset.
        # 
        # This parameter is required.
        self.topic = topic
        # The method that you want to use to clear accumulated messages. Valid values:
        # 
        # *   **0:** All accumulated messages are cleared. Messages that are not consumed are ignored. Consumers in the specified consumer group consume only messages that are published to the topic after the specified point in time.
        # 
        # If "reconsumeLater" is returned, the accumulated messages are not cleared because the system is retrying to resend the messages to consumers.
        # 
        # *   **1:** The messages that were published to the topic before the specified point in time are cleared. You must specify a point in time. Consumers in the specified consumer group consume only the messages that are published to the topic after the specified point in time.
        # 
        # You can specify a point in time from the earliest point in time when a message was published to the topic to the most recent point in time when a message was published to the topic. Points in time that are not within the allowed time range are invalid.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.reset_timestamp is not None:
            result['ResetTimestamp'] = self.reset_timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResetTimestamp') is not None:
            self.reset_timestamp = m.get('ResetTimestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OnsConsumerResetOffsetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsConsumerResetOffsetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsConsumerResetOffsetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsConsumerStatusRequest(TeaModel):
    def __init__(
        self,
        detail: bool = None,
        group_id: str = None,
        instance_id: str = None,
        need_jstack: bool = None,
    ):
        # Specifies whether to query the details of the consumer group. Valid values:
        # 
        # *   **true**: The details of the consumer group are queried. You can obtain details from the **ConsumerConnectionInfoList** and **DetailInTopicList** response parameters.
        # *   **false**: The details of the consumer group are not queried. The values of the **ConsumerConnectionInfoList** and **DetailInTopicList** response parameters are empty. This value is the default value of the Detail parameter.
        self.detail = detail
        # The ID of the consumer group whose details you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id
        # Specifies whether to query the information about thread stack traces. Valid values:
        # 
        # *   **true**: The information about thread stack traces is queried. You can obtain the information from the **Jstack** response parameter.
        # 
        # > If you want to obtain the information about thread stack traces, make sure that the **Detail** parameter in the request is set to **true**.
        # 
        # *   **false**: The information about thread stack traces is not queried. The value of the **Jstack** response parameter is empty. This value is the default value of the NeedJstack parameter.
        self.need_jstack = need_jstack

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.need_jstack is not None:
            result['NeedJstack'] = self.need_jstack
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NeedJstack') is not None:
            self.need_jstack = m.get('NeedJstack')
        return self


class OnsConsumerStatusResponseBodyDataConnectionSetConnectionDo(TeaModel):
    def __init__(
        self,
        client_addr: str = None,
        client_id: str = None,
        language: str = None,
        remote_ip: str = None,
        version: str = None,
    ):
        # The IP address and port number of the consumer instance.
        self.client_addr = client_addr
        # The ID of the consumer instance.
        self.client_id = client_id
        # The programming language in which the consumer is developed.
        self.language = language
        # The private or public IP address of the host.
        self.remote_ip = remote_ip
        # The version of the consumer client.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_addr is not None:
            result['ClientAddr'] = self.client_addr
        if self.client_id is not None:
            result['ClientId'] = self.client_id
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
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('RemoteIP') is not None:
            self.remote_ip = m.get('RemoteIP')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class OnsConsumerStatusResponseBodyDataConnectionSet(TeaModel):
    def __init__(
        self,
        connection_do: List[OnsConsumerStatusResponseBodyDataConnectionSetConnectionDo] = None,
    ):
        self.connection_do = connection_do

    def validate(self):
        if self.connection_do:
            for k in self.connection_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConnectionDo'] = []
        if self.connection_do is not None:
            for k in self.connection_do:
                result['ConnectionDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connection_do = []
        if m.get('ConnectionDo') is not None:
            for k in m.get('ConnectionDo'):
                temp_model = OnsConsumerStatusResponseBodyDataConnectionSetConnectionDo()
                self.connection_do.append(temp_model.from_map(k))
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDoTrackList(TeaModel):
    def __init__(
        self,
        track: List[str] = None,
    ):
        self.track = track

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.track is not None:
            result['Track'] = self.track
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Track') is not None:
            self.track = m.get('Track')
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDo(TeaModel):
    def __init__(
        self,
        thread: str = None,
        track_list: OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDoTrackList = None,
    ):
        # The name of the thread.
        self.thread = thread
        # The details of thread stack traces.
        self.track_list = track_list

    def validate(self):
        if self.track_list:
            self.track_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDoTrackList()
            self.track_list = temp_model.from_map(m['TrackList'])
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstack(TeaModel):
    def __init__(
        self,
        thread_track_do: List[OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDo] = None,
    ):
        self.thread_track_do = thread_track_do

    def validate(self):
        if self.thread_track_do:
            for k in self.thread_track_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ThreadTrackDo'] = []
        if self.thread_track_do is not None:
            for k in self.thread_track_do:
                result['ThreadTrackDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.thread_track_do = []
        if m.get('ThreadTrackDo') is not None:
            for k in m.get('ThreadTrackDo'):
                temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstackThreadTrackDo()
                self.thread_track_do.append(temp_model.from_map(k))
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataListConsumerRunningDataDo(TeaModel):
    def __init__(
        self,
        failed_count_per_hour: int = None,
        failed_tps: float = None,
        ok_tps: float = None,
        rt: float = None,
        topic: str = None,
    ):
        # The number of messages that failed to be consumed each hour.
        self.failed_count_per_hour = failed_count_per_hour
        # The TPS for failed message consumption.
        self.failed_tps = failed_tps
        # The TPS for successful message consumption.
        self.ok_tps = ok_tps
        # The consumption RT. Unit: milliseconds.
        self.rt = rt
        # The name of the topic to which the consumer subscribes.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataList(TeaModel):
    def __init__(
        self,
        consumer_running_data_do: List[OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataListConsumerRunningDataDo] = None,
    ):
        self.consumer_running_data_do = consumer_running_data_do

    def validate(self):
        if self.consumer_running_data_do:
            for k in self.consumer_running_data_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConsumerRunningDataDo'] = []
        if self.consumer_running_data_do is not None:
            for k in self.consumer_running_data_do:
                result['ConsumerRunningDataDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumer_running_data_do = []
        if m.get('ConsumerRunningDataDo') is not None:
            for k in m.get('ConsumerRunningDataDo'):
                temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataListConsumerRunningDataDo()
                self.consumer_running_data_do.append(temp_model.from_map(k))
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionDataTagsSet(TeaModel):
    def __init__(
        self,
        tag: List[str] = None,
    ):
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionData(TeaModel):
    def __init__(
        self,
        sub_string: str = None,
        sub_version: int = None,
        tags_set: OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionDataTagsSet = None,
        topic: str = None,
    ):
        # The expression that is used to specify the tags of messages in the subscribed topic.
        self.sub_string = sub_string
        # The subscription version. The value is of the LONG type and is automatically incremented.
        self.sub_version = sub_version
        # The information about the tags of the topic to which the consumer subscribes.
        self.tags_set = tags_set
        # The name of the topic to which the consumer subscribes.
        self.topic = topic

    def validate(self):
        if self.tags_set:
            self.tags_set.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionDataTagsSet()
            self.tags_set = temp_model.from_map(m['TagsSet'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSet(TeaModel):
    def __init__(
        self,
        subscription_data: List[OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionData] = None,
    ):
        self.subscription_data = subscription_data

    def validate(self):
        if self.subscription_data:
            for k in self.subscription_data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubscriptionData'] = []
        if self.subscription_data is not None:
            for k in self.subscription_data:
                result['SubscriptionData'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_data = []
        if m.get('SubscriptionData') is not None:
            for k in m.get('SubscriptionData'):
                temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSetSubscriptionData()
                self.subscription_data.append(temp_model.from_map(k))
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDo(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        connection: str = None,
        consume_model: str = None,
        consume_type: str = None,
        jstack: OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstack = None,
        language: str = None,
        last_time_stamp: int = None,
        running_data_list: OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataList = None,
        start_time_stamp: int = None,
        subscription_set: OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSet = None,
        thread_count: int = None,
        version: str = None,
    ):
        # The ID of the consumer instance.
        self.client_id = client_id
        # The connection information.
        self.connection = connection
        # The consumption mode. Valid values:
        # 
        # *   **CLUSTERING**: the clustering consumption mode
        # *   **BROADCASTING**: the broadcasting consumption mode
        # 
        # For more information about consumption modes, see [Clustering consumption and broadcasting consumption](https://help.aliyun.com/document_detail/43163.html).
        self.consume_model = consume_model
        # The mode in which the consumer consumes messages. Valid values:
        # 
        # *   **PUSH**: The ApsaraMQ for RocketMQ broker pushes messages to the consumer.
        # *   **PULL**: The consumer pulls messages from the ApsaraMQ for RocketMQ broker.
        self.consume_type = consume_type
        # The information about thread stack traces. If you want to obtain the information about thread stack traces, make sure that the **NeedJstack** parameter in the request is set to **true**. If the NeedJstack parameter is not set to true, the value of this parameter is empty.
        self.jstack = jstack
        # The programming language that the consumer supports.
        self.language = language
        # The most recent point in time when a message was consumed.
        # 
        # The value of this parameter is a UNIX timestamp in milliseconds.
        self.last_time_stamp = last_time_stamp
        # The real-time statistics.
        self.running_data_list = running_data_list
        # The earliest point in time when a message was consumed.
        # 
        # The value of this parameter is a UNIX timestamp in milliseconds.
        self.start_time_stamp = start_time_stamp
        # The information about subscriptions.
        self.subscription_set = subscription_set
        # The number of consumer threads.
        self.thread_count = thread_count
        # The version of the consumer client.
        self.version = version

    def validate(self):
        if self.jstack:
            self.jstack.validate()
        if self.running_data_list:
            self.running_data_list.validate()
        if self.subscription_set:
            self.subscription_set.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoJstack()
            self.jstack = temp_model.from_map(m['Jstack'])
        if m.get('Language') is not None:
            self.language = m.get('Language')
        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')
        if m.get('RunningDataList') is not None:
            temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoRunningDataList()
            self.running_data_list = temp_model.from_map(m['RunningDataList'])
        if m.get('StartTimeStamp') is not None:
            self.start_time_stamp = m.get('StartTimeStamp')
        if m.get('SubscriptionSet') is not None:
            temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDoSubscriptionSet()
            self.subscription_set = temp_model.from_map(m['SubscriptionSet'])
        if m.get('ThreadCount') is not None:
            self.thread_count = m.get('ThreadCount')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class OnsConsumerStatusResponseBodyDataConsumerConnectionInfoList(TeaModel):
    def __init__(
        self,
        consumer_connection_info_do: List[OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDo] = None,
    ):
        self.consumer_connection_info_do = consumer_connection_info_do

    def validate(self):
        if self.consumer_connection_info_do:
            for k in self.consumer_connection_info_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConsumerConnectionInfoDo'] = []
        if self.consumer_connection_info_do is not None:
            for k in self.consumer_connection_info_do:
                result['ConsumerConnectionInfoDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.consumer_connection_info_do = []
        if m.get('ConsumerConnectionInfoDo') is not None:
            for k in m.get('ConsumerConnectionInfoDo'):
                temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoListConsumerConnectionInfoDo()
                self.consumer_connection_info_do.append(temp_model.from_map(k))
        return self


class OnsConsumerStatusResponseBodyDataDetailInTopicListDetailInTopicDo(TeaModel):
    def __init__(
        self,
        delay_time: int = None,
        last_timestamp: int = None,
        topic: str = None,
        total_diff: int = None,
    ):
        # The latency of message consumption in the topic. Unit: milliseconds.
        self.delay_time = delay_time
        # The most recent point in time when a message was consumed.
        # 
        # The value of this parameter is a UNIX timestamp in milliseconds.
        self.last_timestamp = last_timestamp
        # The topic name.
        self.topic = topic
        # The number of accumulated messages in the topic.
        self.total_diff = total_diff

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class OnsConsumerStatusResponseBodyDataDetailInTopicList(TeaModel):
    def __init__(
        self,
        detail_in_topic_do: List[OnsConsumerStatusResponseBodyDataDetailInTopicListDetailInTopicDo] = None,
    ):
        self.detail_in_topic_do = detail_in_topic_do

    def validate(self):
        if self.detail_in_topic_do:
            for k in self.detail_in_topic_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DetailInTopicDo'] = []
        if self.detail_in_topic_do is not None:
            for k in self.detail_in_topic_do:
                result['DetailInTopicDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.detail_in_topic_do = []
        if m.get('DetailInTopicDo') is not None:
            for k in m.get('DetailInTopicDo'):
                temp_model = OnsConsumerStatusResponseBodyDataDetailInTopicListDetailInTopicDo()
                self.detail_in_topic_do.append(temp_model.from_map(k))
        return self


class OnsConsumerStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        connection_set: OnsConsumerStatusResponseBodyDataConnectionSet = None,
        consume_model: str = None,
        consume_tps: float = None,
        consumer_connection_info_list: OnsConsumerStatusResponseBodyDataConsumerConnectionInfoList = None,
        delay_time: int = None,
        detail_in_topic_list: OnsConsumerStatusResponseBodyDataDetailInTopicList = None,
        instance_id: str = None,
        last_timestamp: int = None,
        online: bool = None,
        rebalance_ok: bool = None,
        subscription_same: bool = None,
        total_diff: int = None,
    ):
        # The information about online consumers in the consumer group.
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
        # The details of online consumers in the consumer group, including the information about the thread stack traces and the consumption response time (RT). If you want to obtain the details of online consumers in the consumer group, make sure that the **Detail** parameter in the request is set to **true**. If the Detail parameter is not set to true, the value of this parameter is empty.
        self.consumer_connection_info_list = consumer_connection_info_list
        # The maximum latency of message consumption in all topics to which the consumer group subscribes. Unit: milliseconds.
        self.delay_time = delay_time
        # The information about message consumption by topic. If you want to obtain the information about the consumption status of each topic, make sure that the **Detail** parameter in the request is set to **true**. If the Detail parameter is not set to true, the value of this parameter is empty.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = OnsConsumerStatusResponseBodyDataConnectionSet()
            self.connection_set = temp_model.from_map(m['ConnectionSet'])
        if m.get('ConsumeModel') is not None:
            self.consume_model = m.get('ConsumeModel')
        if m.get('ConsumeTps') is not None:
            self.consume_tps = m.get('ConsumeTps')
        if m.get('ConsumerConnectionInfoList') is not None:
            temp_model = OnsConsumerStatusResponseBodyDataConsumerConnectionInfoList()
            self.consumer_connection_info_list = temp_model.from_map(m['ConsumerConnectionInfoList'])
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('DetailInTopicList') is not None:
            temp_model = OnsConsumerStatusResponseBodyDataDetailInTopicList()
            self.detail_in_topic_list = temp_model.from_map(m['DetailInTopicList'])
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


class OnsConsumerStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsConsumerStatusResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsConsumerStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsConsumerStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsConsumerStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsConsumerStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsConsumerTimeSpanRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        topic: str = None,
    ):
        # The ID of the consumer group whose reset time range you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id
        # The topic to which the consumer group subscribes.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsConsumerTimeSpanResponseBodyData(TeaModel):
    def __init__(
        self,
        consume_time_stamp: int = None,
        instance_id: str = None,
        max_time_stamp: int = None,
        min_time_stamp: int = None,
        topic: str = None,
    ):
        # The most recent point in time when a message in the topic was consumed by the customer group.
        self.consume_time_stamp = consume_time_stamp
        # The ID of the instance to which the consumer group belongs.
        self.instance_id = instance_id
        # The point in time when the earliest stored message was published to the topic.
        self.max_time_stamp = max_time_stamp
        # The point in time when the most recently stored message was published to the topic.
        self.min_time_stamp = min_time_stamp
        # The name of the topic that you want to query.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consume_time_stamp is not None:
            result['ConsumeTimeStamp'] = self.consume_time_stamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.max_time_stamp is not None:
            result['MaxTimeStamp'] = self.max_time_stamp
        if self.min_time_stamp is not None:
            result['MinTimeStamp'] = self.min_time_stamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumeTimeStamp') is not None:
            self.consume_time_stamp = m.get('ConsumeTimeStamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MaxTimeStamp') is not None:
            self.max_time_stamp = m.get('MaxTimeStamp')
        if m.get('MinTimeStamp') is not None:
            self.min_time_stamp = m.get('MinTimeStamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsConsumerTimeSpanResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsConsumerTimeSpanResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsConsumerTimeSpanResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsConsumerTimeSpanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsConsumerTimeSpanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsConsumerTimeSpanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsDLQMessageGetByIdRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        msg_id: str = None,
    ):
        # The ID of the consumer group whose dead-letter message you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the message you want to query belongs.
        self.instance_id = instance_id
        # The ID of the dead-letter message that you want to query.
        # 
        # This parameter is required.
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class OnsDLQMessageGetByIdResponseBodyDataPropertyListMessageProperty(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the attribute. Valid values:
        # 
        # *   **TRACE_ON**: indicates whether the message trace exists.
        # *   **KEYS**: indicates the key of the message.
        # *   **TAGS**: indicates the tag that is attached to the message.
        # *   **INSTANCE_ID**: indicates the ID of the instance that contains the message.
        # 
        # For information about the terms that are used in ApsaraMQ for RocketMQ, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        self.name = name
        # The value of the attribute.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class OnsDLQMessageGetByIdResponseBodyDataPropertyList(TeaModel):
    def __init__(
        self,
        message_property: List[OnsDLQMessageGetByIdResponseBodyDataPropertyListMessageProperty] = None,
    ):
        self.message_property = message_property

    def validate(self):
        if self.message_property:
            for k in self.message_property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MessageProperty'] = []
        if self.message_property is not None:
            for k in self.message_property:
                result['MessageProperty'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_property = []
        if m.get('MessageProperty') is not None:
            for k in m.get('MessageProperty'):
                temp_model = OnsDLQMessageGetByIdResponseBodyDataPropertyListMessageProperty()
                self.message_property.append(temp_model.from_map(k))
        return self


class OnsDLQMessageGetByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        body_crc: int = None,
        born_host: str = None,
        born_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        property_list: OnsDLQMessageGetByIdResponseBodyDataPropertyList = None,
        reconsume_times: int = None,
        store_host: str = None,
        store_size: int = None,
        store_timestamp: int = None,
        topic: str = None,
    ):
        # The cyclic redundancy check (CRC) value of the message body.
        self.body_crc = body_crc
        # The producer instance that generated the message.
        self.born_host = born_host
        # The timestamp that indicates the point in time when the message was generated. Unit: milliseconds.
        self.born_timestamp = born_timestamp
        # The ID of the instance
        self.instance_id = instance_id
        # The ID of the dead-letter message.
        self.msg_id = msg_id
        # The attributes of the message.
        self.property_list = property_list
        # The number of retries that were performed to send the message to consumers.
        self.reconsume_times = reconsume_times
        # The ApsaraMQ for RocketMQ broker that stores the message.
        self.store_host = store_host
        # The size of the message. Unit: KB.
        self.store_size = store_size
        # The timestamp that indicates the point in time when the ApsaraMQ for RocketMQ broker stored the message. Unit: milliseconds.
        self.store_timestamp = store_timestamp
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        if self.property_list:
            self.property_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.property_list is not None:
            result['PropertyList'] = self.property_list.to_map()
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('PropertyList') is not None:
            temp_model = OnsDLQMessageGetByIdResponseBodyDataPropertyList()
            self.property_list = temp_model.from_map(m['PropertyList'])
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsDLQMessageGetByIdResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsDLQMessageGetByIdResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsDLQMessageGetByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsDLQMessageGetByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsDLQMessageGetByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsDLQMessageGetByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsDLQMessagePageQueryByGroupIdRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        current_page: int = None,
        end_time: int = None,
        group_id: str = None,
        instance_id: str = None,
        page_size: int = None,
        task_id: str = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds. If you specify a valid value for the **TaskId** parameter in the request, this parameter does not take effect. The system uses the value of the BeginTime parameter that you specified in the request when you created the specified query task.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The number of the page to return. Pages start from page 1. Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds. If you specify a valid value for the **TaskId** parameter in the request, this parameter does not take effect. The system uses the value of the EndTime parameter that you specified in the request when you created the specified query task.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the consumer group whose dead-letter messages you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the dead-letter messages you want to query belong.
        self.instance_id = instance_id
        # The number of dead-letter messages to return on each page. Valid values: 5 to 50. Default value: 20. If you specify a valid value for the **TaskId** parameter in the request, this parameter does not take effect. The system uses the value of the PageSize parameter that you specified in the request when you created the specified query task.
        self.page_size = page_size
        # The ID of the query task. The first time you call this operation to query dead-letter messages that are sent to a specified consumer group within a specified time range, this parameter is not required. This parameter is required in subsequent queries for dead-letter messages on a specified page. You can obtain the task ID from the returned result of the first query.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyListMessageProperty(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the attribute. Valid values:
        # 
        # *   **TRACE_ON**: indicates whether a trace of the message exists.
        # *   **KEYS**: indicates the key of the message.
        # *   **TAGS**: indicates the tag that is attached to the message.
        # *   **INSTANCE_ID**: indicates the ID of the instance that contains the message.
        # 
        # For information about the terms that are used in ApsaraMQ for RocketMQ, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        self.name = name
        # The value of the attribute.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyList(TeaModel):
    def __init__(
        self,
        message_property: List[OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyListMessageProperty] = None,
    ):
        self.message_property = message_property

    def validate(self):
        if self.message_property:
            for k in self.message_property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MessageProperty'] = []
        if self.message_property is not None:
            for k in self.message_property:
                result['MessageProperty'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_property = []
        if m.get('MessageProperty') is not None:
            for k in m.get('MessageProperty'):
                temp_model = OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyListMessageProperty()
                self.message_property.append(temp_model.from_map(k))
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDo(TeaModel):
    def __init__(
        self,
        body_crc: int = None,
        born_host: str = None,
        born_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        property_list: OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyList = None,
        reconsume_times: int = None,
        store_host: str = None,
        store_size: int = None,
        store_timestamp: int = None,
        topic: str = None,
    ):
        # The cyclic redundancy check (CRC) value of the message body.
        self.body_crc = body_crc
        # The producer instance that generated the message.
        self.born_host = born_host
        # The timestamp that indicates when the message was produced.
        self.born_timestamp = born_timestamp
        # The ID of the instance
        self.instance_id = instance_id
        # The ID of the message.
        self.msg_id = msg_id
        # The attributes of the message.
        self.property_list = property_list
        # The number of retries that were performed to send the message to consumers.
        self.reconsume_times = reconsume_times
        # The ApsaraMQ for RocketMQ broker that stores the message.
        self.store_host = store_host
        # The size of the message. Unit: KB.
        self.store_size = store_size
        # The timestamp that indicates the point in time when the ApsaraMQ for RocketMQ broker stored the message.
        self.store_timestamp = store_timestamp
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        if self.property_list:
            self.property_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.property_list is not None:
            result['PropertyList'] = self.property_list.to_map()
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('PropertyList') is not None:
            temp_model = OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyList()
            self.property_list = temp_model.from_map(m['PropertyList'])
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundList(TeaModel):
    def __init__(
        self,
        ons_rest_message_do: List[OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDo] = None,
    ):
        self.ons_rest_message_do = ons_rest_message_do

    def validate(self):
        if self.ons_rest_message_do:
            for k in self.ons_rest_message_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OnsRestMessageDo'] = []
        if self.ons_rest_message_do is not None:
            for k in self.ons_rest_message_do:
                result['OnsRestMessageDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ons_rest_message_do = []
        if m.get('OnsRestMessageDo') is not None:
            for k in m.get('OnsRestMessageDo'):
                temp_model = OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDo()
                self.ons_rest_message_do.append(temp_model.from_map(k))
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        max_page_count: int = None,
        msg_found_list: OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundList = None,
        task_id: str = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The total number of returned pages.
        self.max_page_count = max_page_count
        # The information about dead-letter messages that are returned on the current page. The information that is contained in this parameter is the same as the information that is returned by the [OnsDLQMessageGetById](https://help.aliyun.com/document_detail/112667.html) operation.
        self.msg_found_list = msg_found_list
        # The ID of the query task. The first time you call this operation to query the dead-letter messages that are sent to a specified consumer group within a specified time range, this parameter is returned. You can use the task ID to query the details of dead-letter messages on other returned pages.
        self.task_id = task_id

    def validate(self):
        if self.msg_found_list:
            self.msg_found_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.max_page_count is not None:
            result['MaxPageCount'] = self.max_page_count
        if self.msg_found_list is not None:
            result['MsgFoundList'] = self.msg_found_list.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('MaxPageCount') is not None:
            self.max_page_count = m.get('MaxPageCount')
        if m.get('MsgFoundList') is not None:
            temp_model = OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDoMsgFoundList()
            self.msg_found_list = temp_model.from_map(m['MsgFoundList'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OnsDLQMessagePageQueryByGroupIdResponseBody(TeaModel):
    def __init__(
        self,
        msg_found_do: OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDo = None,
        request_id: str = None,
    ):
        # The information about dead-letter messages that are queried.
        self.msg_found_do = msg_found_do
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.msg_found_do:
            self.msg_found_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_found_do is not None:
            result['MsgFoundDo'] = self.msg_found_do.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgFoundDo') is not None:
            temp_model = OnsDLQMessagePageQueryByGroupIdResponseBodyMsgFoundDo()
            self.msg_found_do = temp_model.from_map(m['MsgFoundDo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsDLQMessagePageQueryByGroupIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsDLQMessagePageQueryByGroupIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsDLQMessagePageQueryByGroupIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsDLQMessageResendByIdRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        msg_id: str = None,
    ):
        # The ID of the consumer group in which you want to query dead-letter messages.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance in which the dead-letter message you want to query resides.
        self.instance_id = instance_id
        # The ID of the dead-letter message that you want to send to a consumer group for consumption.
        # 
        # This parameter is required.
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class OnsDLQMessageResendByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        msg_id: List[str] = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class OnsDLQMessageResendByIdResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsDLQMessageResendByIdResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned messages.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsDLQMessageResendByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsDLQMessageResendByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsDLQMessageResendByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsDLQMessageResendByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsGroupConsumerUpdateRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
        read_enable: bool = None,
    ):
        # The ID of the consumer group for which you want to configure read permissions.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group you want to configure belongs.
        self.instance_id = instance_id
        # Specifies whether to authorize the consumer group to read messages. Valid values:
        # 
        # *   **true**: The consumer group can read messages.
        # *   **false**: The consumer group cannot read messages.
        # 
        # Default value: **true**.
        # 
        # This parameter is required.
        self.read_enable = read_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.read_enable is not None:
            result['ReadEnable'] = self.read_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ReadEnable') is not None:
            self.read_enable = m.get('ReadEnable')
        return self


class OnsGroupConsumerUpdateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsGroupConsumerUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsGroupConsumerUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsGroupCreateRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_type: str = None,
        instance_id: str = None,
        remark: str = None,
    ):
        # The ID of the consumer group that you want to create. The group ID must meet the following rules:
        # 
        # *   The group ID must be 2 to 64 characters in length and can contain only letters, digits, hyphens (-), and underscores (_).
        # *   If the ApsaraMQ for RocketMQ instance in which you want to create the consumer group uses a namespace, the group ID must be unique in the instance. The group ID cannot be the same as an existing group ID or a topic name in the instance. The group ID can be the same as a group ID or a topic name in another instance that uses a different namespace. For example, if Instance A and Instance B use different namespaces, a group ID in Instance A can be the same as a group ID or a topic name in Instance B.
        # *   If the instance does not use a namespace, the group ID must be globally unique across instances and regions. The group ID cannot be the same as an existing group ID or topic name in ApsaraMQ for RocketMQ instances that belong to your Alibaba Cloud account.
        # 
        # > 
        # 
        # *   After the consumer group is created, the group ID cannot be changed.
        # 
        # *   To check whether an instance uses a namespace, log on to the ApsaraMQ for RocketMQ console, go to the **Instance Details** page, and then view the value of the Namespace field in the **Basic Information** section.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The protocol over which clients in the consumer group communicate with the ApsaraMQ for RocketMQ broker. All clients in a consumer group communicate with the ApsaraMQ for RocketMQ broker over the same protocol. You must create different groups for TCP clients and HTTP clients. Valid values:
        # 
        # *   **tcp**: Clients in the consumer group consume messages over TCP. This is the default value.
        # *   **http**: Clients in the consumer group consume messages over HTTP.
        self.group_type = group_type
        # The ID of the instance in which you want to create the consumer group.
        self.instance_id = instance_id
        # The description of the consumer group.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class OnsGroupCreateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsGroupCreateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The ID of the consumer group that you want to delete.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the ApsaraMQ for RocketMQ instance to which the specified consumer group belongs.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsGroupDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The key of the tag that is attached to the consumer group. This parameter is not required. If you configure this parameter, you must configure the **Key** parameter.**** If you configure both the Key and Value parameters, the consumer groups are filtered based on the specified tag. If you do not configure these parameters, all consumer groups are queried.
        # 
        # *   The value of this parameter cannot be an empty string.
        # *   The tag value must be 1 to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag that is attached to the group. This parameter is not required. If you configure this parameter, you must configure the **Key** parameter.**** If you configure both the Key and Value parameters, the consumer groups are filtered based on the specified tag. If you do not configure these parameters, all consumer groups are queried.
        # 
        # *   The value of this parameter can be an empty string.
        # *   The tag key must be 1 to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        group_id: str = None,
        group_type: str = None,
        instance_id: str = None,
        tag: List[OnsGroupListRequestTag] = None,
    ):
        # This parameter is required only when you query specific consumer groups by using the fuzzy search method. If this parameter is not configured, the system queries all consumer groups that can be accessed by the current account.
        # 
        # If you set this parameter to GID_ABC, the information about the consumer groups whose IDs contain GID_ABC is returned. For example, the information about the GID_test_GID_ABC_123 and GID_ABC_356 consumer groups is returned.
        self.group_id = group_id
        # The protocol over which the queried consumer group publishes and subscribes to messages. All clients in a consumer group communicate with the ApsaraMQ for RocketMQ broker over the same protocol. You must create different consumer groups for TCP clients and HTTP clients. Valid values:
        # 
        # *   **tcp**: specifies that the consumer group publishes or subscribes to messages over TCP. This value is the default value.
        # *   **http**: specifies that the consumer group publishes or subscribes to messages over HTTP.
        self.group_type = group_type
        # The ID of the instance to which the consumer group you want to query belongs.
        self.instance_id = instance_id
        # The list of tags that are attached to the consumer group. A maximum of 20 tags can be included in the list.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = OnsGroupListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class OnsGroupListResponseBodyDataSubscribeInfoDoTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that is attached to the consumer group.
        self.key = key
        # The value of the tag that is attached to the consumer group.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsGroupListResponseBodyDataSubscribeInfoDoTags(TeaModel):
    def __init__(
        self,
        tag: List[OnsGroupListResponseBodyDataSubscribeInfoDoTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = OnsGroupListResponseBodyDataSubscribeInfoDoTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class OnsGroupListResponseBodyDataSubscribeInfoDo(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        group_id: str = None,
        group_type: str = None,
        independent_naming: bool = None,
        instance_id: str = None,
        owner: str = None,
        remark: str = None,
        tags: OnsGroupListResponseBodyDataSubscribeInfoDoTags = None,
        update_time: int = None,
    ):
        # The point in time when the consumer group was created.
        self.create_time = create_time
        # The ID of the consumer group.
        self.group_id = group_id
        # The protocol over which the queried consumer group publishes and subscribes to messages. All clients in a consumer group communicate with the ApsaraMQ for RocketMQ broker over the same protocol. You must create different consumer groups for TCP clients and HTTP clients. Valid values:
        # 
        # *   **tcp**: indicates that the consumer group publishes and subscribes to messages over TCP.
        # *   **http**: indicates that the consumer group publishes and subscribes to messages over HTTP.
        self.group_type = group_type
        # Indicates whether the instance uses a namespace. Valid values:
        # 
        # *   **true**: The instance uses a separate namespace. The name of each resource must be unique in the instance. The names of resources in different instances can be the same.
        # *   **false**: The instance does not use a separate namespace. The name of each resource must be globally unique within the instance and across all instances.
        self.independent_naming = independent_naming
        # The ID of the instance
        self.instance_id = instance_id
        # The Alibaba Cloud account ID of the user who created the consumer group.
        self.owner = owner
        # The description of the consumer group.
        self.remark = remark
        # The tags that are attached to the consumer group.
        self.tags = tags
        # The most recent point in time when the consumer group was updated.
        self.update_time = update_time

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.group_type is not None:
            result['GroupType'] = self.group_type
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Tags') is not None:
            temp_model = OnsGroupListResponseBodyDataSubscribeInfoDoTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class OnsGroupListResponseBodyData(TeaModel):
    def __init__(
        self,
        subscribe_info_do: List[OnsGroupListResponseBodyDataSubscribeInfoDo] = None,
    ):
        self.subscribe_info_do = subscribe_info_do

    def validate(self):
        if self.subscribe_info_do:
            for k in self.subscribe_info_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubscribeInfoDo'] = []
        if self.subscribe_info_do is not None:
            for k in self.subscribe_info_do:
                result['SubscribeInfoDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscribe_info_do = []
        if m.get('SubscribeInfoDo') is not None:
            for k in m.get('SubscribeInfoDo'):
                temp_model = OnsGroupListResponseBodyDataSubscribeInfoDo()
                self.subscribe_info_do.append(temp_model.from_map(k))
        return self


class OnsGroupListResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsGroupListResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned list of subscriptions.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsGroupListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsGroupListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsGroupListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsGroupListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsGroupSubDetailRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the consumer group that you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group you want to query belongs.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsGroupSubDetailResponseBodyDataSubscriptionDataListSubscriptionDataList(TeaModel):
    def __init__(
        self,
        sub_string: str = None,
        topic: str = None,
    ):
        # The expression based on which consumers in the consumer group subscribe to the topic.
        self.sub_string = sub_string
        # The name of the topic to which consumers in the consumer group subscribe.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsGroupSubDetailResponseBodyDataSubscriptionDataList(TeaModel):
    def __init__(
        self,
        subscription_data_list: List[OnsGroupSubDetailResponseBodyDataSubscriptionDataListSubscriptionDataList] = None,
    ):
        self.subscription_data_list = subscription_data_list

    def validate(self):
        if self.subscription_data_list:
            for k in self.subscription_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubscriptionDataList'] = []
        if self.subscription_data_list is not None:
            for k in self.subscription_data_list:
                result['SubscriptionDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_data_list = []
        if m.get('SubscriptionDataList') is not None:
            for k in m.get('SubscriptionDataList'):
                temp_model = OnsGroupSubDetailResponseBodyDataSubscriptionDataListSubscriptionDataList()
                self.subscription_data_list.append(temp_model.from_map(k))
        return self


class OnsGroupSubDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        message_model: str = None,
        online: bool = None,
        subscription_data_list: OnsGroupSubDetailResponseBodyDataSubscriptionDataList = None,
    ):
        # The ID of the consumer group that you want to query.
        self.group_id = group_id
        # The consumption mode. Valid values:
        # 
        # *   **CLUSTERING**: the clustering consumption mode
        # *   **BROADCASTING**: the broadcasting consumption mode
        # 
        # For more information about consumption modes, see [Clustering consumption and broadcasting consumption](https://help.aliyun.com/document_detail/43163.html).
        self.message_model = message_model
        # Indicates whether consumers in the group are online.
        self.online = online
        # The topics to which consumers in the consumer group subscribe. If all consumers in the specified group are offline, no topics are returned.
        self.subscription_data_list = subscription_data_list

    def validate(self):
        if self.subscription_data_list:
            self.subscription_data_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.message_model is not None:
            result['MessageModel'] = self.message_model
        if self.online is not None:
            result['Online'] = self.online
        if self.subscription_data_list is not None:
            result['SubscriptionDataList'] = self.subscription_data_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('MessageModel') is not None:
            self.message_model = m.get('MessageModel')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('SubscriptionDataList') is not None:
            temp_model = OnsGroupSubDetailResponseBodyDataSubscriptionDataList()
            self.subscription_data_list = temp_model.from_map(m['SubscriptionDataList'])
        return self


class OnsGroupSubDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsGroupSubDetailResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsGroupSubDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsGroupSubDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsGroupSubDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsGroupSubDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsInstanceBaseInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the instance that you want to query.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        http_internal_endpoint: str = None,
        http_internet_endpoint: str = None,
        http_internet_secure_endpoint: str = None,
        tcp_endpoint: str = None,
        tcp_internet_endpoint: str = None,
    ):
        # The private HTTP endpoint of the instance.
        self.http_internal_endpoint = http_internal_endpoint
        # The public HTTP endpoint of the instance.
        self.http_internet_endpoint = http_internet_endpoint
        # The public HTTPS endpoint of the instance.
        self.http_internet_secure_endpoint = http_internet_secure_endpoint
        # The private TCP endpoint of the instance.
        self.tcp_endpoint = tcp_endpoint
        # The public TCP endpoint of the instance.
        # 
        # *   Only instances that are deployed in the China (Chengdu), China (Qingdao), or China (Shenzhen) region can be accessed by using public TCP endpoints.
        # 
        # *   Before you use a public TCP endpoint, make sure that your client SDK meets the following requirements:
        # 
        #     *   TCP client SDK for Java: V2.0.0.Final or later For more information, see [Release notes for the SDK for Java](https://help.aliyun.com/document_detail/325569.html).
        #     *   TCP client SDK for C++: V3.0.0 or later For more information, see [Release notes for the SDK for C++](https://help.aliyun.com/document_detail/325570.html).
        # 
        # *   You are charged for Internet traffic when you use a public TCP endpoint. For more information, see [Internet traffic fee](https://help.aliyun.com/document_detail/325571.html).
        self.tcp_internet_endpoint = tcp_internet_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http_internal_endpoint is not None:
            result['HttpInternalEndpoint'] = self.http_internal_endpoint
        if self.http_internet_endpoint is not None:
            result['HttpInternetEndpoint'] = self.http_internet_endpoint
        if self.http_internet_secure_endpoint is not None:
            result['HttpInternetSecureEndpoint'] = self.http_internet_secure_endpoint
        if self.tcp_endpoint is not None:
            result['TcpEndpoint'] = self.tcp_endpoint
        if self.tcp_internet_endpoint is not None:
            result['TcpInternetEndpoint'] = self.tcp_internet_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpInternalEndpoint') is not None:
            self.http_internal_endpoint = m.get('HttpInternalEndpoint')
        if m.get('HttpInternetEndpoint') is not None:
            self.http_internet_endpoint = m.get('HttpInternetEndpoint')
        if m.get('HttpInternetSecureEndpoint') is not None:
            self.http_internet_secure_endpoint = m.get('HttpInternetSecureEndpoint')
        if m.get('TcpEndpoint') is not None:
            self.tcp_endpoint = m.get('TcpEndpoint')
        if m.get('TcpInternetEndpoint') is not None:
            self.tcp_internet_endpoint = m.get('TcpInternetEndpoint')
        return self


class OnsInstanceBaseInfoResponseBodyInstanceBaseInfo(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        endpoints: OnsInstanceBaseInfoResponseBodyInstanceBaseInfoEndpoints = None,
        independent_naming: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: int = None,
        instance_type: int = None,
        max_tps: int = None,
        release_time: int = None,
        remark: str = None,
        topic_capacity: int = None,
        sp_instance_id: str = None,
        sp_instance_type: int = None,
    ):
        # The time when the instance was created. The value of this parameter is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The endpoints used to access ApsaraMQ for RocketMQ over different protocols.
        self.endpoints = endpoints
        # Indicates whether the instance uses a namespace. Valid values:
        # 
        # *   **true**: The instance uses a separate namespace. The name of each resource must be unique in the instance. The names of resources in different instances can be the same.
        # *   **false**: The instance does not use a separate namespace. The name of each resource must be globally unique within the instance and across all instances.
        self.independent_naming = independent_naming
        # The ID of the instance
        self.instance_id = instance_id
        # The name of the instance.
        # 
        # The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.instance_name = instance_name
        # The status of the instance. Valid values:
        # 
        # *   **0**: The instance is being deployed. This value is valid only for Enterprise Platinum Edition instances.
        # *   **2**: The instance has overdue payments. This value is valid only for Standard Edition instances.
        # *   **5**: The instance is running. This value is valid for Standard Edition instances and Enterprise Platinum Edition instances.
        # *   **7**: The instance is being upgraded and is running. This value is valid only for Enterprise Platinum Edition instances.
        self.instance_status = instance_status
        # The instance type. Valid values:
        # 
        # *   **1**: Standard Edition instances that use the pay-as-you-go billing method.
        # *   **2**: Enterprise Platinum Edition instances that use the subscription billing method.
        # 
        # For information about the editions and specifications of ApsaraMQ for RocketMQ instances, see [Instance editions](https://help.aliyun.com/document_detail/185261.html).
        self.instance_type = instance_type
        # The maximum messaging transactions per second (TPS). Valid values: 5000, 10000, 20000, 50000, 100000, 200000, 300000, 500000, 800000, and 1000000.
        # 
        # You can view the details about messaging TPS on the buy page of ApsaraMQ for RocketMQ.
        # 
        # > This parameter is available only to the ApsaraMQ for RocketMQ Enterprise Platinum Edition instances.
        self.max_tps = max_tps
        # The time when the Enterprise Platinum Edition instance expires.
        self.release_time = release_time
        # The description of the instance.
        self.remark = remark
        # The maximum number of topics that can be created on the instance. Valid values: 25, 50, 100, 300, and 500.
        # 
        # > This parameter is available only to the ApsaraMQ for RocketMQ Enterprise Platinum Edition instances.
        self.topic_capacity = topic_capacity
        # The commodity ID of the instance.
        self.sp_instance_id = sp_instance_id
        # The commodity type of the instance.
        self.sp_instance_type = sp_instance_type

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.topic_capacity is not None:
            result['TopicCapacity'] = self.topic_capacity
        if self.sp_instance_id is not None:
            result['spInstanceId'] = self.sp_instance_id
        if self.sp_instance_type is not None:
            result['spInstanceType'] = self.sp_instance_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Endpoints') is not None:
            temp_model = OnsInstanceBaseInfoResponseBodyInstanceBaseInfoEndpoints()
            self.endpoints = temp_model.from_map(m['Endpoints'])
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TopicCapacity') is not None:
            self.topic_capacity = m.get('TopicCapacity')
        if m.get('spInstanceId') is not None:
            self.sp_instance_id = m.get('spInstanceId')
        if m.get('spInstanceType') is not None:
            self.sp_instance_type = m.get('spInstanceType')
        return self


class OnsInstanceBaseInfoResponseBody(TeaModel):
    def __init__(
        self,
        instance_base_info: OnsInstanceBaseInfoResponseBodyInstanceBaseInfo = None,
        request_id: str = None,
    ):
        # The information about the instance.
        self.instance_base_info = instance_base_info
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instance_base_info:
            self.instance_base_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsInstanceBaseInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsInstanceBaseInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsInstanceCreateRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        remark: str = None,
    ):
        # The name of the instance. The name must meet the following rules:
        # 
        # *   The name of the instance must be unique in the region where the instance is deployed.
        # *   The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The description of the instance.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class OnsInstanceCreateResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: int = None,
    ):
        # The ID of the instance that you created.
        self.instance_id = instance_id
        # The edition of the instance that you created. Valid value:
        # 
        # *   **1**: Standard Edition instances
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        data: OnsInstanceCreateResponseBodyData = None,
        request_id: str = None,
    ):
        # The result returned.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsInstanceCreateResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsInstanceCreateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsInstanceCreateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsInstanceCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsInstanceDeleteRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsInstanceDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The tag key. This parameter is not required. If you configure this parameter, you must also configure **Value**.**** If you configure Key and Value in a request, this operation queries only the instances that use the specified tags. If you do not configure these parameters in a request, this operation queries all instances that you can access.
        # 
        # *   The value of this parameter cannot be an empty string.
        # *   The tag key can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. This parameter is not required. If you configure this parameter, you must also configure **Key**.**** If you configure Key and Value in a request, this operation queries only the instances that use the specified tags. If you do not configure these parameters in a request, this operation queries all instances that you can access.
        # 
        # *   The value of this parameter can be an empty string.
        # *   The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:` or `aliyun`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        need_resource_info: bool = None,
        tag: List[OnsInstanceInServiceListRequestTag] = None,
    ):
        # Specifies whether you want the resource information to be returned.
        self.need_resource_info = need_resource_info
        # The tags that you want to attach to the instance. You can attach up to 20 tags to the instance.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.need_resource_info is not None:
            result['NeedResourceInfo'] = self.need_resource_info
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NeedResourceInfo') is not None:
            self.need_resource_info = m.get('NeedResourceInfo')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = OnsInstanceInServiceListRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class OnsInstanceInServiceListResponseBodyDataInstanceVOTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsInstanceInServiceListResponseBodyDataInstanceVOTags(TeaModel):
    def __init__(
        self,
        tag: List[OnsInstanceInServiceListResponseBodyDataInstanceVOTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = OnsInstanceInServiceListResponseBodyDataInstanceVOTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class OnsInstanceInServiceListResponseBodyDataInstanceVO(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        group_count: int = None,
        independent_naming: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: int = None,
        instance_type: int = None,
        release_time: int = None,
        tags: OnsInstanceInServiceListResponseBodyDataInstanceVOTags = None,
        topic_count: int = None,
    ):
        # The time when the instance was created. The value of this parameter is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The number of consumer groups.
        self.group_count = group_count
        # Indicates whether a namespace is used for the instance. Valid values:
        # 
        # *   **true**: A separate namespace is used for the instance. The identifier of each resource in the instance must be unique within the instance. However, the identifier of a resource in the instance can be the same as the identifier of a resource in another instance that uses a different namespace.
        # *   **false**: A separate namespace is not used for the instance. The name of each resource must be globally unique within the instance and across all instances.
        self.independent_naming = independent_naming
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        # 
        # The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.instance_name = instance_name
        # The instance status. Valid values:
        # 
        # *   **0**: The instance is being deployed. This value is valid only for Enterprise Platinum Edition instances.
        # *   **2**: The instance has overdue payments. This value is valid only for Standard Edition instances.
        # *   **5**: The instance is running. This value is valid only for Standard Edition instances and Enterprise Platinum Edition instances.
        # *   **7**: The instance is being upgraded and is running. This value is valid only for Enterprise Platinum Edition instances.
        self.instance_status = instance_status
        # The instance type. Valid values:
        # 
        # *   **1**: Standard Edition
        # *   **2**: Enterprise Platinum Edition
        # 
        # For information about the instance editions and the differences between the editions, see [Instance editions](https://help.aliyun.com/document_detail/185261.html).
        self.instance_type = instance_type
        # The time when the instance expires. If the instance is of Enterprise Platinum Edition, this parameter is returned.
        self.release_time = release_time
        # The tags that are attached to the instance.
        self.tags = tags
        # The number of topics.
        self.topic_count = topic_count

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.group_count is not None:
            result['GroupCount'] = self.group_count
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type
        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic_count is not None:
            result['TopicCount'] = self.topic_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')
        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')
        if m.get('Tags') is not None:
            temp_model = OnsInstanceInServiceListResponseBodyDataInstanceVOTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('TopicCount') is not None:
            self.topic_count = m.get('TopicCount')
        return self


class OnsInstanceInServiceListResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_vo: List[OnsInstanceInServiceListResponseBodyDataInstanceVO] = None,
    ):
        self.instance_vo = instance_vo

    def validate(self):
        if self.instance_vo:
            for k in self.instance_vo:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InstanceVO'] = []
        if self.instance_vo is not None:
            for k in self.instance_vo:
                result['InstanceVO'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_vo = []
        if m.get('InstanceVO') is not None:
            for k in m.get('InstanceVO'):
                temp_model = OnsInstanceInServiceListResponseBodyDataInstanceVO()
                self.instance_vo.append(temp_model.from_map(k))
        return self


class OnsInstanceInServiceListResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsInstanceInServiceListResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned information about the queried instances.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsInstanceInServiceListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsInstanceInServiceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsInstanceInServiceListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsInstanceInServiceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsInstanceUpdateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        remark: str = None,
    ):
        # The ID of the instance whose name or description you want to update.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new name of the instance. The name must meet the following rules:
        # 
        # *   The name of the instance must be unique in the region where the instance is deployed.
        # *   The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), underscores (_), and Chinese characters.
        # *   If you do not configure this parameter, the instance name remains unchanged.
        self.instance_name = instance_name
        # The updated description of the instance. If you do not configure this parameter, the instance description remains unchanged.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class OnsInstanceUpdateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsInstanceUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsInstanceUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessageDetailRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        msg_id: str = None,
        topic: str = None,
    ):
        # The ID of the ApsaraMQ for RocketMQ Instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the message that you want to query.
        # 
        # This parameter is required.
        self.msg_id = msg_id
        # The name of the topic in which the message you want to query is stored.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessageDetailResponseBodyDataPropertyList(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the attribute. Valid values:
        # 
        # *   **TRACE_ON**: indicates whether the trace of the message exists.
        # *   **MSG_REGION**: The region ID of the instance to which the topic belongs.
        # *   **__MESSAGE_DECODED_TIME**: The time when the message was decoded.
        # *   **__BORNHOST**: The IP address of the producer client.
        # *   **UNIQ_KEY**: The ID of the message.
        # 
        # For information about the terms that are used in ApsaraMQ for RocketMQ, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        self.name = name
        # The value of the attribute.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class OnsMessageDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        body: str = None,
        body_crc: int = None,
        body_str: str = None,
        born_host: str = None,
        born_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        property_list: List[OnsMessageDetailResponseBodyDataPropertyList] = None,
        reconsume_times: int = None,
        store_host: str = None,
        store_size: int = None,
        store_timestamp: int = None,
        topic: str = None,
    ):
        # The string that is obtained after the message body is encrypted by using the Base 64 algorithm.
        self.body = body
        # The cyclic redundancy check (CRC) value of the message body.
        self.body_crc = body_crc
        # The information about the message body.
        self.body_str = body_str
        # The producer instance that generated the message.
        self.born_host = born_host
        # The timestamp that indicates the point in time when the message was generated. Unit: milliseconds.
        self.born_timestamp = born_timestamp
        # The ID of the ApsaraMQ for RocketMQ Instance.
        self.instance_id = instance_id
        # The ID of the message.
        self.msg_id = msg_id
        # The attributes of the message.
        self.property_list = property_list
        # The number of retries that ApsaraMQ for RocketMQ performed to send the message to consumers.
        self.reconsume_times = reconsume_times
        # The ApsaraMQ for RocketMQ broker that stores the message.
        self.store_host = store_host
        # The size of the message. Unit: KB.
        self.store_size = store_size
        # The timestamp that indicates the point in time when the ApsaraMQ for RocketMQ broker stored the message. Unit: milliseconds.
        self.store_timestamp = store_timestamp
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        if self.property_list:
            for k in self.property_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.body_str is not None:
            result['BodyStr'] = self.body_str
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        result['PropertyList'] = []
        if self.property_list is not None:
            for k in self.property_list:
                result['PropertyList'].append(k.to_map() if k else None)
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BodyStr') is not None:
            self.body_str = m.get('BodyStr')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        self.property_list = []
        if m.get('PropertyList') is not None:
            for k in m.get('PropertyList'):
                temp_model = OnsMessageDetailResponseBodyDataPropertyList()
                self.property_list.append(temp_model.from_map(k))
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessageDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsMessageDetailResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsMessageDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsMessageDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsMessageDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsMessageDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessageGetByKeyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        key: str = None,
        topic: str = None,
    ):
        # The ID of the instance to which the messages that you want to query belong.
        self.instance_id = instance_id
        # The key of the messages that you want to query.
        # 
        # This parameter is required.
        self.key = key
        # The topic that contains the messages that you want to query.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.key is not None:
            result['Key'] = self.key
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessageGetByKeyResponseBodyDataOnsRestMessageDoPropertyListMessageProperty(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the attribute. Valid values:
        # 
        # -  **TRACE_ON**: indicates whether the message trace exists.
        # 
        # -   **KEYS**: indicates the key of the message.
        # 
        # - **TAGS**: indicates the tag that is attached to the message.
        # 
        # - **INSTANCE_ID**: indicates the ID of the instance that contains the message.
        # 
        # For information about the terms that are used in ApsaraMQ for RocketMQ, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        self.name = name
        # The value of the attribute.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class OnsMessageGetByKeyResponseBodyDataOnsRestMessageDoPropertyList(TeaModel):
    def __init__(
        self,
        message_property: List[OnsMessageGetByKeyResponseBodyDataOnsRestMessageDoPropertyListMessageProperty] = None,
    ):
        self.message_property = message_property

    def validate(self):
        if self.message_property:
            for k in self.message_property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MessageProperty'] = []
        if self.message_property is not None:
            for k in self.message_property:
                result['MessageProperty'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_property = []
        if m.get('MessageProperty') is not None:
            for k in m.get('MessageProperty'):
                temp_model = OnsMessageGetByKeyResponseBodyDataOnsRestMessageDoPropertyListMessageProperty()
                self.message_property.append(temp_model.from_map(k))
        return self


class OnsMessageGetByKeyResponseBodyDataOnsRestMessageDo(TeaModel):
    def __init__(
        self,
        body_crc: int = None,
        born_host: str = None,
        born_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        property_list: OnsMessageGetByKeyResponseBodyDataOnsRestMessageDoPropertyList = None,
        reconsume_times: int = None,
        store_host: str = None,
        store_size: int = None,
        store_timestamp: int = None,
        topic: str = None,
    ):
        # The cyclic redundancy check (CRC) value of the message body.
        self.body_crc = body_crc
        # The producer client that generated the message.
        self.born_host = born_host
        # The timestamp that indicates when the message was produced.
        self.born_timestamp = born_timestamp
        # The ID of the instance
        self.instance_id = instance_id
        # The ID of the message.
        self.msg_id = msg_id
        # The attributes of the message.
        self.property_list = property_list
        # The number of retries that were performed to send the message to consumers.
        self.reconsume_times = reconsume_times
        # The ApsaraMQ for RocketMQ broker that stores the message.
        self.store_host = store_host
        # The size of the message.
        self.store_size = store_size
        # The timestamp that indicates when the ApsaraMQ for RocketMQ broker stored the message.
        self.store_timestamp = store_timestamp
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        if self.property_list:
            self.property_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.property_list is not None:
            result['PropertyList'] = self.property_list.to_map()
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('PropertyList') is not None:
            temp_model = OnsMessageGetByKeyResponseBodyDataOnsRestMessageDoPropertyList()
            self.property_list = temp_model.from_map(m['PropertyList'])
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessageGetByKeyResponseBodyData(TeaModel):
    def __init__(
        self,
        ons_rest_message_do: List[OnsMessageGetByKeyResponseBodyDataOnsRestMessageDo] = None,
    ):
        self.ons_rest_message_do = ons_rest_message_do

    def validate(self):
        if self.ons_rest_message_do:
            for k in self.ons_rest_message_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OnsRestMessageDo'] = []
        if self.ons_rest_message_do is not None:
            for k in self.ons_rest_message_do:
                result['OnsRestMessageDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ons_rest_message_do = []
        if m.get('OnsRestMessageDo') is not None:
            for k in m.get('OnsRestMessageDo'):
                temp_model = OnsMessageGetByKeyResponseBodyDataOnsRestMessageDo()
                self.ons_rest_message_do.append(temp_model.from_map(k))
        return self


class OnsMessageGetByKeyResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsMessageGetByKeyResponseBodyData = None,
        request_id: str = None,
    ):
        # The list of returned results.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsMessageGetByKeyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsMessageGetByKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsMessageGetByKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsMessageGetByKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessageGetByMsgIdRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        msg_id: str = None,
        topic: str = None,
    ):
        # The ID of the instance to which the message you want to query belongs.
        self.instance_id = instance_id
        # The ID of the message that you want to query.
        # 
        # This parameter is required.
        self.msg_id = msg_id
        # The topic that contains the message you want to query.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessageGetByMsgIdResponseBodyDataPropertyListMessageProperty(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the attribute. Valid values:
        # 
        # *   **TRACE_ON**: indicates whether a trace of the message exists.
        # *   **KEYS**: indicates the key of the message.
        # *   **TAGS**: indicates the tag that is attached to the message.
        # *   **INSTANCE_ID**: indicates the ID of the instance which contains the message.
        # 
        # For information about the terms that are used in Message Queue for Apache RocketMQ, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        self.name = name
        # The value of the attribute.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class OnsMessageGetByMsgIdResponseBodyDataPropertyList(TeaModel):
    def __init__(
        self,
        message_property: List[OnsMessageGetByMsgIdResponseBodyDataPropertyListMessageProperty] = None,
    ):
        self.message_property = message_property

    def validate(self):
        if self.message_property:
            for k in self.message_property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MessageProperty'] = []
        if self.message_property is not None:
            for k in self.message_property:
                result['MessageProperty'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_property = []
        if m.get('MessageProperty') is not None:
            for k in m.get('MessageProperty'):
                temp_model = OnsMessageGetByMsgIdResponseBodyDataPropertyListMessageProperty()
                self.message_property.append(temp_model.from_map(k))
        return self


class OnsMessageGetByMsgIdResponseBodyData(TeaModel):
    def __init__(
        self,
        body_crc: int = None,
        born_host: str = None,
        born_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        property_list: OnsMessageGetByMsgIdResponseBodyDataPropertyList = None,
        reconsume_times: int = None,
        store_host: str = None,
        store_size: int = None,
        store_timestamp: int = None,
        topic: str = None,
    ):
        # The cyclic redundancy check (CRC) value of the message body.
        self.body_crc = body_crc
        # The producer instance that generated the message.
        self.born_host = born_host
        # The timestamp that indicates when the message was produced.
        self.born_timestamp = born_timestamp
        # The ID of the instance
        self.instance_id = instance_id
        # The ID of the message.
        self.msg_id = msg_id
        # The attributes of the message.
        self.property_list = property_list
        # The number of retries that were performed to send the message to consumers.
        self.reconsume_times = reconsume_times
        # The ApsaraMQ for RocketMQ broker that stores the message.
        self.store_host = store_host
        # The size of the message.
        self.store_size = store_size
        # The timestamp that indicates when the ApsaraMQ for RocketMQ broker stored the message.
        self.store_timestamp = store_timestamp
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        if self.property_list:
            self.property_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.property_list is not None:
            result['PropertyList'] = self.property_list.to_map()
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('PropertyList') is not None:
            temp_model = OnsMessageGetByMsgIdResponseBodyDataPropertyList()
            self.property_list = temp_model.from_map(m['PropertyList'])
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessageGetByMsgIdResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsMessageGetByMsgIdResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsMessageGetByMsgIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsMessageGetByMsgIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsMessageGetByMsgIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsMessageGetByMsgIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessagePageQueryByTopicRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        current_page: int = None,
        end_time: int = None,
        instance_id: str = None,
        page_size: int = None,
        task_id: str = None,
        topic: str = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds. If you specify a valid value for the **TaskId** parameter in the request, this parameter does not take effect. The system uses the value of the BeginTime parameter that you specified in the request when you created the specified query task.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The number of the page to return. Pages start from page 1. Valid values: 1 to 50.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds. If you specify a valid value for the **TaskId** parameter in the request, this parameter does not take effect. The system uses the value of the EndTime parameter that you specified in the request when you created the specified query task.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the instance to which the message you want to query belongs.
        self.instance_id = instance_id
        # The number of entries to return on each page. Valid values: 5 to 50. Default value: 20. If you specify a valid value for the **TaskId** parameter in the request, this parameter does not take effect. The system uses the value of the PageSize parameter that you specified in the request for creating the query task.
        self.page_size = page_size
        # The ID of the query task. The first time you call this operation to query the information about messages in a specified topic within a specified time range, this parameter is not required. This parameter is required in subsequent queries for messages on a specified page. You can obtain the task ID from the returned result of the first query.
        self.task_id = task_id
        # The name of the topic whose messages you want to query.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyListMessageProperty(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the attribute. Valid values:
        # 
        # *   **TRACE_ON**: indicates whether a trace of the message exists.
        # *   **KEYS**: indicates the key of the message.
        # *   **TAGS**: indicates the tag of the message.
        # *   **INSTANCE_ID**: indicates the ID of the instance that contains the message.
        # 
        # For information about the terms that are used in ApsaraMQ for RocketMQ see [Terms](https://help.aliyun.com/document_detail/29533.html).
        self.name = name
        # The value of the attribute.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyList(TeaModel):
    def __init__(
        self,
        message_property: List[OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyListMessageProperty] = None,
    ):
        self.message_property = message_property

    def validate(self):
        if self.message_property:
            for k in self.message_property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MessageProperty'] = []
        if self.message_property is not None:
            for k in self.message_property:
                result['MessageProperty'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_property = []
        if m.get('MessageProperty') is not None:
            for k in m.get('MessageProperty'):
                temp_model = OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyListMessageProperty()
                self.message_property.append(temp_model.from_map(k))
        return self


class OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDo(TeaModel):
    def __init__(
        self,
        body_crc: int = None,
        born_host: str = None,
        born_timestamp: int = None,
        instance_id: str = None,
        msg_id: str = None,
        property_list: OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyList = None,
        reconsume_times: int = None,
        store_host: str = None,
        store_size: int = None,
        store_timestamp: int = None,
        topic: str = None,
    ):
        # The cyclic redundancy check (CRC) value of the message body.
        self.body_crc = body_crc
        # The producer client that generated the message.
        self.born_host = born_host
        # The time when the message was generated. The value is a UNIX timestamp that represents the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.born_timestamp = born_timestamp
        # The ID of the instance
        self.instance_id = instance_id
        # The ID of the message.
        self.msg_id = msg_id
        # The attributes of the message.
        self.property_list = property_list
        # The number of retries that were performed to send the message to consumers.
        self.reconsume_times = reconsume_times
        # The ApsaraMQ for RocketMQ broker that stores the message.
        self.store_host = store_host
        # The size of the message. Unit: KB.
        self.store_size = store_size
        # The time when the ApsaraMQ for RocketMQ broker stored the message. The value is a UNIX timestamp that represents the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        self.store_timestamp = store_timestamp
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        if self.property_list:
            self.property_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body_crc is not None:
            result['BodyCRC'] = self.body_crc
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        if self.born_timestamp is not None:
            result['BornTimestamp'] = self.born_timestamp
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.property_list is not None:
            result['PropertyList'] = self.property_list.to_map()
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.store_host is not None:
            result['StoreHost'] = self.store_host
        if self.store_size is not None:
            result['StoreSize'] = self.store_size
        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyCRC') is not None:
            self.body_crc = m.get('BodyCRC')
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        if m.get('BornTimestamp') is not None:
            self.born_timestamp = m.get('BornTimestamp')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('PropertyList') is not None:
            temp_model = OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDoPropertyList()
            self.property_list = temp_model.from_map(m['PropertyList'])
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('StoreHost') is not None:
            self.store_host = m.get('StoreHost')
        if m.get('StoreSize') is not None:
            self.store_size = m.get('StoreSize')
        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundList(TeaModel):
    def __init__(
        self,
        ons_rest_message_do: List[OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDo] = None,
    ):
        self.ons_rest_message_do = ons_rest_message_do

    def validate(self):
        if self.ons_rest_message_do:
            for k in self.ons_rest_message_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OnsRestMessageDo'] = []
        if self.ons_rest_message_do is not None:
            for k in self.ons_rest_message_do:
                result['OnsRestMessageDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ons_rest_message_do = []
        if m.get('OnsRestMessageDo') is not None:
            for k in m.get('OnsRestMessageDo'):
                temp_model = OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundListOnsRestMessageDo()
                self.ons_rest_message_do.append(temp_model.from_map(k))
        return self


class OnsMessagePageQueryByTopicResponseBodyMsgFoundDo(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        max_page_count: int = None,
        msg_found_list: OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundList = None,
        task_id: str = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The total number of returned pages.
        self.max_page_count = max_page_count
        # The information about messages on the returned page. The information that is contained in this parameter is the same as the information that is returned by the [OnsMessageGetByMsgId](https://help.aliyun.com/document_detail/29607.html) operation.
        self.msg_found_list = msg_found_list
        # The ID of the query task. The first time you call this operation to query the messages that are sent to a specified consumer group within a specified time range, this parameter is returned. You can use the task ID to query the details of messages on other returned pages.
        self.task_id = task_id

    def validate(self):
        if self.msg_found_list:
            self.msg_found_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.max_page_count is not None:
            result['MaxPageCount'] = self.max_page_count
        if self.msg_found_list is not None:
            result['MsgFoundList'] = self.msg_found_list.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('MaxPageCount') is not None:
            self.max_page_count = m.get('MaxPageCount')
        if m.get('MsgFoundList') is not None:
            temp_model = OnsMessagePageQueryByTopicResponseBodyMsgFoundDoMsgFoundList()
            self.msg_found_list = temp_model.from_map(m['MsgFoundList'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OnsMessagePageQueryByTopicResponseBody(TeaModel):
    def __init__(
        self,
        msg_found_do: OnsMessagePageQueryByTopicResponseBodyMsgFoundDo = None,
        request_id: str = None,
    ):
        # The information about the message that is queried.
        self.msg_found_do = msg_found_do
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.msg_found_do:
            self.msg_found_do.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_found_do is not None:
            result['MsgFoundDo'] = self.msg_found_do.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgFoundDo') is not None:
            temp_model = OnsMessagePageQueryByTopicResponseBodyMsgFoundDo()
            self.msg_found_do = temp_model.from_map(m['MsgFoundDo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsMessagePageQueryByTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsMessagePageQueryByTopicResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsMessagePageQueryByTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessagePushRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        group_id: str = None,
        instance_id: str = None,
        msg_id: str = None,
        topic: str = None,
    ):
        # The ID of the consumer client. You can call the [OnsConsumerGetConnection](https://help.aliyun.com/document_detail/29598.html) operation to query client IDs.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The ID of the consumer group. For information about what a consumer group is, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the ApsaraMQ for RocketMQ instance to which the specified consumer group belongs.
        self.instance_id = instance_id
        # The ID of the message.
        # 
        # This parameter is required.
        self.msg_id = msg_id
        # The topic to which the message is pushed.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessagePushResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsMessagePushResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsMessagePushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsMessageTraceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        msg_id: str = None,
        topic: str = None,
    ):
        # The ID of the instance to which the message you want to query belongs.
        self.instance_id = instance_id
        # The ID of the message that you want to query.
        # 
        # This parameter is required.
        self.msg_id = msg_id
        # The topic to which the message belongs.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsMessageTraceResponseBodyDataMessageTrack(TeaModel):
    def __init__(
        self,
        consumer_group: str = None,
        instance_id: str = None,
        track_type: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.consumer_group = consumer_group
        # The ID of the instance to which the message you want to query belongs.
        self.instance_id = instance_id
        # The status of the message. Valid values:
        # 
        # *   **CONSUMED**: The message is consumed.
        # *   **CONSUMED_BUT_FILTERED**: No consumer group subscribes to the message. The message is filtered out and not consumed.
        # *   **NOT_CONSUME_YET**: The message is not consumed.
        # *   **NOT_ONLINE**: The consumer group is offline.
        # *   **UNKNOWN**: The message is not consumed due to unknown reasons.
        self.track_type = track_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.consumer_group is not None:
            result['ConsumerGroup'] = self.consumer_group
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.track_type is not None:
            result['TrackType'] = self.track_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConsumerGroup') is not None:
            self.consumer_group = m.get('ConsumerGroup')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TrackType') is not None:
            self.track_type = m.get('TrackType')
        return self


class OnsMessageTraceResponseBodyData(TeaModel):
    def __init__(
        self,
        message_track: List[OnsMessageTraceResponseBodyDataMessageTrack] = None,
    ):
        self.message_track = message_track

    def validate(self):
        if self.message_track:
            for k in self.message_track:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MessageTrack'] = []
        if self.message_track is not None:
            for k in self.message_track:
                result['MessageTrack'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_track = []
        if m.get('MessageTrack') is not None:
            for k in m.get('MessageTrack'):
                temp_model = OnsMessageTraceResponseBodyDataMessageTrack()
                self.message_track.append(temp_model.from_map(k))
        return self


class OnsMessageTraceResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsMessageTraceResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the message that is queried.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsMessageTraceResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsMessageTraceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsMessageTraceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsMessageTraceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsRegionListResponseBodyDataRegionDo(TeaModel):
    def __init__(
        self,
        channel_name: str = None,
        create_time: int = None,
        id: int = None,
        ons_region_id: str = None,
        region_name: str = None,
        update_time: int = None,
    ):
        # The channel name.
        self.channel_name = channel_name
        # The time when the instance was created.
        self.create_time = create_time
        # The instance ID.
        self.id = id
        # The region ID.
        self.ons_region_id = ons_region_id
        # The region name.
        self.region_name = region_name
        # The time when the instance was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_name is not None:
            result['ChannelName'] = self.channel_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.ons_region_id is not None:
            result['OnsRegionId'] = self.ons_region_id
        if self.region_name is not None:
            result['RegionName'] = self.region_name
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelName') is not None:
            self.channel_name = m.get('ChannelName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OnsRegionId') is not None:
            self.ons_region_id = m.get('OnsRegionId')
        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class OnsRegionListResponseBodyData(TeaModel):
    def __init__(
        self,
        region_do: List[OnsRegionListResponseBodyDataRegionDo] = None,
    ):
        self.region_do = region_do

    def validate(self):
        if self.region_do:
            for k in self.region_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['RegionDo'] = []
        if self.region_do is not None:
            for k in self.region_do:
                result['RegionDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_do = []
        if m.get('RegionDo') is not None:
            for k in m.get('RegionDo'):
                temp_model = OnsRegionListResponseBodyDataRegionDo()
                self.region_do.append(temp_model.from_map(k))
        return self


class OnsRegionListResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsRegionListResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsRegionListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsRegionListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsRegionListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsRegionListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicCreateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        message_type: int = None,
        remark: str = None,
        topic: str = None,
    ):
        # The ID of the instance in which you want to create the topic.
        self.instance_id = instance_id
        # The type of messages that you want to publish to the topic. Valid values:
        # 
        # *   **0**: normal messages
        # *   **1**: partitionally ordered messages
        # *   **2**: globally ordered messages
        # *   **4**: transactional messages
        # *   **5**: scheduled or delayed messages
        # 
        # For more information about message types, see [Message types](https://help.aliyun.com/document_detail/155952.html).
        # 
        # This parameter is required.
        self.message_type = message_type
        # The description of the topic that you want to create.
        self.remark = remark
        # The name of the topic that you want to create. The name must meet the following rules:
        # 
        # *   The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # *   The topic name cannot start with CID or GID because CID and GID are reserved prefixes for group IDs.
        # *   If the ApsaraMQ for RocketMQ instance in which you want to create the topic uses a namespace, the topic name must be unique in the instance. The topic name cannot be the same as an existing topic name or a group ID in the instance. The topic name can be the same as a topic name or a group ID in another instance that uses a different namespace. For example, if Instance A and Instance B use different namespaces, a topic name in Instance A can be the same as a topic name or a group ID in Instance B.
        # *   If the instance in which you want to create the topic does not use a namespace, the topic name must be globally unique across instances and regions. The topic name cannot be the same as an existing topic name or group ID in all ApsaraMQ for RocketMQ instances that belong to your Alibaba Cloud account.
        # 
        # > To check whether an instance uses a namespace, log on to the ApsaraMQ for RocketMQ console, go to the **Instance Details** page, and then view the value of the Namespace field in the **Basic Information** section.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTopicCreateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsTopicCreateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsTopicCreateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicDeleteRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        topic: str = None,
    ):
        # The ID of the instance to which the topic you want to delete belongs.
        self.instance_id = instance_id
        # The name of the topic that you want to delete.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsTopicDeleteResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsTopicDeleteResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The key of the tag that is attached to the topics you want to query. This parameter is not required. If you configure this parameter, you must also configure the **Value** parameter.**** If you include the Key and Value parameters in a request, this operation queries only the topics that use the specified tag. If you do not include these parameters in a request, this operation queries all topics that you can access.
        # 
        # *   The value of this parameter cannot be an empty string.
        # *   A tag value can be up to 128 characters in length and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag that is attached to the topics you want to query. This parameter is not required. If you configure this parameter, you must also configure the **Key** parameter.**** If you include the Key and Value parameters in a request, this operation queries only the topics that use the specified tag. If you do not include these parameters in a request, this operation queries all topics that you can access.
        # 
        # *   The value of this parameter can be an empty string.
        # *   A tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `acs:` or `aliyun`.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        instance_id: str = None,
        tag: List[OnsTopicListRequestTag] = None,
        topic: str = None,
        user_id: str = None,
    ):
        # The ID of the instance that contains the topics you want to query.
        self.instance_id = instance_id
        # The list of tags that are attached to the topic. A maximum of 20 tags can be included in the list.
        self.tag = tag
        # The name of the topic that you want to query. This parameter is required if you want to query a specific topic. If you do not include this parameter in a request, all topics that you can access are queried.
        self.topic = topic
        # The user ID of the topic owner. Set this parameter to an Alibaba Cloud account ID.
        self.user_id = user_id

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = OnsTopicListRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class OnsTopicListResponseBodyDataPublishInfoDoTagsTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsTopicListResponseBodyDataPublishInfoDoTags(TeaModel):
    def __init__(
        self,
        tag: List[OnsTopicListResponseBodyDataPublishInfoDoTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = OnsTopicListResponseBodyDataPublishInfoDoTagsTag()
                self.tag.append(temp_model.from_map(k))
        return self


class OnsTopicListResponseBodyDataPublishInfoDo(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        independent_naming: bool = None,
        instance_id: str = None,
        message_type: int = None,
        owner: str = None,
        relation: int = None,
        relation_name: str = None,
        remark: str = None,
        service_status: int = None,
        tags: OnsTopicListResponseBodyDataPublishInfoDoTags = None,
        topic: str = None,
    ):
        # The time when the topic was created.
        self.create_time = create_time
        # Indicates whether the instance that contains the topic uses a namespace. Valid values:
        # 
        # *   **true**: The instance uses a separate namespace. The name of each resource must be unique in the instance. The names of resources in different instances can be the same.
        # *   **false**: The instance does not use a separate namespace. The name of each resource must be globally unique within an instance and across all instances.
        self.independent_naming = independent_naming
        # The ID of the instance that contains the topic.
        self.instance_id = instance_id
        # The message type. Valid values:
        # 
        # *   **0**: normal messages
        # *   **1**: partitionally ordered messages
        # *   **2**: globally ordered messages
        # *   **4**: transactional messages
        # *   **5**: scheduled or delayed messages
        self.message_type = message_type
        # The user ID of the topic owner. The value of this parameter is an Alibaba account ID.
        self.owner = owner
        # Indicates the relationship between the current account and the topic. Valid values:
        # 
        # *   **1**: The current account is the owner of the topic.
        # *   **2**: The current account can publish messages to the topic.
        # *   **4**: The current account can subscribe to the topic.
        # *   **6**: The current account can publish messages to and subscribe to the topic.
        self.relation = relation
        # The relationship between the current account and the topic. The value of this parameter indicates whether the current account is the owner of the topic, and whether the current account can subscribe or publish messages to the topic. the topic.
        self.relation_name = relation_name
        # The description of the topic.
        self.remark = remark
        # The status of the topic that is asynchronously created. Valid values:
        # 
        # *   **0**: The topic is being created.
        # *   **1**: The topic is being used.
        self.service_status = service_status
        # The tags that are attached to the topic.
        self.tags = tags
        # The topic name.
        self.topic = topic

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_type is not None:
            result['MessageType'] = self.message_type
        if self.owner is not None:
            result['Owner'] = self.owner
        if self.relation is not None:
            result['Relation'] = self.relation
        if self.relation_name is not None:
            result['RelationName'] = self.relation_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.tags is not None:
            result['Tags'] = self.tags.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')
        if m.get('Owner') is not None:
            self.owner = m.get('Owner')
        if m.get('Relation') is not None:
            self.relation = m.get('Relation')
        if m.get('RelationName') is not None:
            self.relation_name = m.get('RelationName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('Tags') is not None:
            temp_model = OnsTopicListResponseBodyDataPublishInfoDoTags()
            self.tags = temp_model.from_map(m['Tags'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTopicListResponseBodyData(TeaModel):
    def __init__(
        self,
        publish_info_do: List[OnsTopicListResponseBodyDataPublishInfoDo] = None,
    ):
        self.publish_info_do = publish_info_do

    def validate(self):
        if self.publish_info_do:
            for k in self.publish_info_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PublishInfoDo'] = []
        if self.publish_info_do is not None:
            for k in self.publish_info_do:
                result['PublishInfoDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.publish_info_do = []
        if m.get('PublishInfoDo') is not None:
            for k in m.get('PublishInfoDo'):
                temp_model = OnsTopicListResponseBodyDataPublishInfoDo()
                self.publish_info_do.append(temp_model.from_map(k))
        return self


class OnsTopicListResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsTopicListResponseBodyData = None,
        request_id: str = None,
    ):
        # The information about the topics.
        self.data = data
        # The ID of the request. This is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsTopicListResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTopicListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsTopicListResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsTopicListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        topic: str = None,
    ):
        # The ID of the instance that contains the topic you want to query.
        self.instance_id = instance_id
        # The name of the topic that you want to query.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsTopicStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        last_time_stamp: int = None,
        perm: int = None,
        total_count: int = None,
    ):
        # The point in time when the latest message is ready in the topic. If no message exists in the topic, the return value of this parameter is 0.
        # 
        # The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # For information about the definition of ready messages and ready time, see [Terms](https://help.aliyun.com/document_detail/29533.html).
        self.last_time_stamp = last_time_stamp
        # Indicates the operations that you can perform on the topic. Valid values:
        # 
        # *   **2**: You can publish messages to the topic.
        # *   **4**: You can subscribe to the topic.
        # *   **6**: You can publish messages to and subscribe to the topic.
        self.perm = perm
        # The total number of messages in all partitions of the topic.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_time_stamp is not None:
            result['LastTimeStamp'] = self.last_time_stamp
        if self.perm is not None:
            result['Perm'] = self.perm
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastTimeStamp') is not None:
            self.last_time_stamp = m.get('LastTimeStamp')
        if m.get('Perm') is not None:
            self.perm = m.get('Perm')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class OnsTopicStatusResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsTopicStatusResponseBodyData = None,
        request_id: str = None,
    ):
        # The data structure of the queried topic.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsTopicStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTopicStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsTopicStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The ID of the instance that contains the topic you want to query.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the topic that you want to query.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsTopicSubDetailResponseBodyDataSubscriptionDataListSubscriptionDataList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        message_model: str = None,
        sub_string: str = None,
    ):
        # The ID of the consumer group that subscribes to the topic.
        self.group_id = group_id
        # The consumption mode. Valid values:
        # 
        # *   **CLUSTERING**: the clustering consumption mode
        # *   **BROADCASTING**: the broadcasting consumption mode
        # 
        # For more information about consumption modes, see [Clustering consumption and broadcasting consumption](https://help.aliyun.com/document_detail/43163.html).
        self.message_model = message_model
        # The expression based on which consumers in the consumer group subscribe to the topic.
        self.sub_string = sub_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class OnsTopicSubDetailResponseBodyDataSubscriptionDataList(TeaModel):
    def __init__(
        self,
        subscription_data_list: List[OnsTopicSubDetailResponseBodyDataSubscriptionDataListSubscriptionDataList] = None,
    ):
        self.subscription_data_list = subscription_data_list

    def validate(self):
        if self.subscription_data_list:
            for k in self.subscription_data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubscriptionDataList'] = []
        if self.subscription_data_list is not None:
            for k in self.subscription_data_list:
                result['SubscriptionDataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_data_list = []
        if m.get('SubscriptionDataList') is not None:
            for k in m.get('SubscriptionDataList'):
                temp_model = OnsTopicSubDetailResponseBodyDataSubscriptionDataListSubscriptionDataList()
                self.subscription_data_list.append(temp_model.from_map(k))
        return self


class OnsTopicSubDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        subscription_data_list: OnsTopicSubDetailResponseBodyDataSubscriptionDataList = None,
        topic: str = None,
    ):
        # The information about the online consumer groups that subscribe to the topic.
        self.subscription_data_list = subscription_data_list
        # The topic name.
        self.topic = topic

    def validate(self):
        if self.subscription_data_list:
            self.subscription_data_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subscription_data_list is not None:
            result['SubscriptionDataList'] = self.subscription_data_list.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubscriptionDataList') is not None:
            temp_model = OnsTopicSubDetailResponseBodyDataSubscriptionDataList()
            self.subscription_data_list = temp_model.from_map(m['SubscriptionDataList'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTopicSubDetailResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsTopicSubDetailResponseBodyData = None,
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsTopicSubDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTopicSubDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsTopicSubDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsTopicSubDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTopicUpdateRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        perm: int = None,
        topic: str = None,
    ):
        # The ID of the instance to which the topic belongs.
        self.instance_id = instance_id
        # The read/write mode that you want to configure for the topic. Valid values:
        # 
        # *   **6**: Both read and write operations are allowed.
        # *   **4**: Write operations are forbidden.
        # *   **2**: Read operations are forbidden.
        # 
        # This parameter is required.
        self.perm = perm
        # The name of the topic that you want to manage.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.perm is not None:
            result['Perm'] = self.perm
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Perm') is not None:
            self.perm = m.get('Perm')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTopicUpdateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsTopicUpdateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsTopicUpdateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTraceGetResultRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        query_id: str = None,
        topic: str = None,
    ):
        # The ID of the instance to which the message you want to query belongs.
        self.instance_id = instance_id
        # The ID of the task that was created to query the trace of the message.
        # 
        # This parameter is required.
        self.query_id = query_id
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientListSubClientInfoDo(TeaModel):
    def __init__(
        self,
        client_host: str = None,
        cost_time: int = None,
        reconsume_times: int = None,
        status: str = None,
        sub_group_name: str = None,
        sub_time: int = None,
    ):
        # The address of the consumer.
        self.client_host = client_host
        # The period of time that the system took to consume the message. Unit: milliseconds.
        self.cost_time = cost_time
        # The number of attempts that the ApsaraMQ for RocketMQ broker tried to send the message to the consumer.
        self.reconsume_times = reconsume_times
        # Indicates whether the message is consumed. Valid values:
        # 
        # *   **CONSUME_FAILED**: The message failed to be consumed.
        # *   **CONSUME_SUCCESS**: The message is consumed.
        # *   **CONSUME_NOT_RETURN:** No responses are returned.
        # *   **SEND_UNKNOWN:** The message is a transactional message and is not committed.
        # *   **SEND_DELAY:** The message is a scheduled or delayed message and is waiting to be consumed at the specified point in time.
        self.status = status
        # The ID of the group that contains the consumer.
        self.sub_group_name = sub_group_name
        # The earliest point in time when the message was consumed.
        self.sub_time = sub_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_host is not None:
            result['ClientHost'] = self.client_host
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_group_name is not None:
            result['SubGroupName'] = self.sub_group_name
        if self.sub_time is not None:
            result['SubTime'] = self.sub_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientHost') is not None:
            self.client_host = m.get('ClientHost')
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubGroupName') is not None:
            self.sub_group_name = m.get('SubGroupName')
        if m.get('SubTime') is not None:
            self.sub_time = m.get('SubTime')
        return self


class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientList(TeaModel):
    def __init__(
        self,
        sub_client_info_do: List[OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientListSubClientInfoDo] = None,
    ):
        self.sub_client_info_do = sub_client_info_do

    def validate(self):
        if self.sub_client_info_do:
            for k in self.sub_client_info_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubClientInfoDo'] = []
        if self.sub_client_info_do is not None:
            for k in self.sub_client_info_do:
                result['SubClientInfoDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_client_info_do = []
        if m.get('SubClientInfoDo') is not None:
            for k in m.get('SubClientInfoDo'):
                temp_model = OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientListSubClientInfoDo()
                self.sub_client_info_do.append(temp_model.from_map(k))
        return self


class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDo(TeaModel):
    def __init__(
        self,
        client_list: OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientList = None,
        fail_count: int = None,
        sub_group_name: str = None,
        success_count: int = None,
    ):
        # The information about message consumption by consumers in the group.
        self.client_list = client_list
        # The number of consumption failures.
        self.fail_count = fail_count
        # The ID of the consumer group.
        self.sub_group_name = sub_group_name
        # The number of successful consumptions.
        self.success_count = success_count

    def validate(self):
        if self.client_list:
            self.client_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_list is not None:
            result['ClientList'] = self.client_list.to_map()
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count
        if self.sub_group_name is not None:
            result['SubGroupName'] = self.sub_group_name
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientList') is not None:
            temp_model = OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDoClientList()
            self.client_list = temp_model.from_map(m['ClientList'])
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')
        if m.get('SubGroupName') is not None:
            self.sub_group_name = m.get('SubGroupName')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubList(TeaModel):
    def __init__(
        self,
        sub_map_do: List[OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDo] = None,
    ):
        self.sub_map_do = sub_map_do

    def validate(self):
        if self.sub_map_do:
            for k in self.sub_map_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SubMapDo'] = []
        if self.sub_map_do is not None:
            for k in self.sub_map_do:
                result['SubMapDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sub_map_do = []
        if m.get('SubMapDo') is not None:
            for k in m.get('SubMapDo'):
                temp_model = OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubListSubMapDo()
                self.sub_map_do.append(temp_model.from_map(k))
        return self


class OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDo(TeaModel):
    def __init__(
        self,
        born_host: str = None,
        cost_time: int = None,
        msg_id: str = None,
        msg_key: str = None,
        pub_group_name: str = None,
        pub_time: int = None,
        status: str = None,
        sub_list: OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubList = None,
        tag: str = None,
        topic: str = None,
    ):
        # The address of the producer that generated the message.
        self.born_host = born_host
        # The period of time that the system took to send the message. Unit: milliseconds.
        self.cost_time = cost_time
        # The ID of the message.
        self.msg_id = msg_id
        # The key of the message.
        self.msg_key = msg_key
        # The ID of the group that contains the producer.
        self.pub_group_name = pub_group_name
        # The point in time when the message was sent.
        self.pub_time = pub_time
        # Indicates whether the message is sent. Valid values:
        # 
        # *   **SEND_SUCCESS**: The message is sent.
        # *   **SEND_FAILED**: The message failed to be sent.
        # *   **SEND_ROLLBACK:** The message is a transactional message and is rolled back.
        # *   **SEND_UNKNOWN:** The message is a transactional message and is not committed.
        # *   **SEND_DELAY:** The message is a scheduled or delayed message and is waiting to be consumed at the specified point in time.
        self.status = status
        # The consumption traces of the message.
        self.sub_list = sub_list
        # The tag of the message.
        self.tag = tag
        # The topic to which the message belongs.
        self.topic = topic

    def validate(self):
        if self.sub_list:
            self.sub_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.born_host is not None:
            result['BornHost'] = self.born_host
        if self.cost_time is not None:
            result['CostTime'] = self.cost_time
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key
        if self.pub_group_name is not None:
            result['PubGroupName'] = self.pub_group_name
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_list is not None:
            result['SubList'] = self.sub_list.to_map()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BornHost') is not None:
            self.born_host = m.get('BornHost')
        if m.get('CostTime') is not None:
            self.cost_time = m.get('CostTime')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')
        if m.get('PubGroupName') is not None:
            self.pub_group_name = m.get('PubGroupName')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubList') is not None:
            temp_model = OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDoSubList()
            self.sub_list = temp_model.from_map(m['SubList'])
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTraceGetResultResponseBodyTraceDataTraceList(TeaModel):
    def __init__(
        self,
        trace_map_do: List[OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDo] = None,
    ):
        self.trace_map_do = trace_map_do

    def validate(self):
        if self.trace_map_do:
            for k in self.trace_map_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TraceMapDo'] = []
        if self.trace_map_do is not None:
            for k in self.trace_map_do:
                result['TraceMapDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.trace_map_do = []
        if m.get('TraceMapDo') is not None:
            for k in m.get('TraceMapDo'):
                temp_model = OnsTraceGetResultResponseBodyTraceDataTraceListTraceMapDo()
                self.trace_map_do.append(temp_model.from_map(k))
        return self


class OnsTraceGetResultResponseBodyTraceData(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        msg_id: str = None,
        msg_key: str = None,
        query_id: str = None,
        status: str = None,
        topic: str = None,
        trace_list: OnsTraceGetResultResponseBodyTraceDataTraceList = None,
        update_time: int = None,
        user_id: str = None,
    ):
        # The point in time when the task was created.
        self.create_time = create_time
        # The ID of the instance
        self.instance_id = instance_id
        # The ID of the message that is queried.
        self.msg_id = msg_id
        # The key of the message that is queried.
        self.msg_key = msg_key
        # The ID of the task.
        self.query_id = query_id
        # The status of the task. Valid values:
        # 
        # *   **finish**: The task is complete.
        # *   **working**: The task is in progress.
        # *   **removed**: The task is deleted.
        self.status = status
        # The topic in which the message is stored.
        self.topic = topic
        # The details of the message trace.
        self.trace_list = trace_list
        # The most recent point in time when the task was updated.
        self.update_time = update_time
        # The ID of the user who created the task.
        self.user_id = user_id

    def validate(self):
        if self.trace_list:
            self.trace_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.status is not None:
            result['Status'] = self.status
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.trace_list is not None:
            result['TraceList'] = self.trace_list.to_map()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TraceList') is not None:
            temp_model = OnsTraceGetResultResponseBodyTraceDataTraceList()
            self.trace_list = temp_model.from_map(m['TraceList'])
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class OnsTraceGetResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        trace_data: OnsTraceGetResultResponseBodyTraceData = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The details of the message trace.
        self.trace_data = trace_data

    def validate(self):
        if self.trace_data:
            self.trace_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: OnsTraceGetResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsTraceGetResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTraceQueryByMsgIdRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
        msg_id: str = None,
        topic: str = None,
    ):
        # The beginning of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraMQ for RocketMQ instance that contains the specified topic.
        self.instance_id = instance_id
        # The ID of the message that you want to query.
        # 
        # This parameter is required.
        self.msg_id = msg_id
        # The topic that contains the message you want to query.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTraceQueryByMsgIdResponseBody(TeaModel):
    def __init__(
        self,
        query_id: str = None,
        request_id: str = None,
    ):
        # The ID of the query task. You can call the [OnsTraceGetResult](https://help.aliyun.com/document_detail/59832.html) operation to query the details of the message trace based on the task ID.
        self.query_id = query_id
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTraceQueryByMsgIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsTraceQueryByMsgIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsTraceQueryByMsgIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTraceQueryByMsgKeyRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
        msg_key: str = None,
        topic: str = None,
    ):
        # The start of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The end of the time range to query. The value of this parameter is a UNIX timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ApsaraMQ for RocketMQ instance that contains the specified topic.
        self.instance_id = instance_id
        # The key of the message that you want to query.
        # 
        # This parameter is required.
        self.msg_key = msg_key
        # The topic that contains the message you want to query.
        # 
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.msg_key is not None:
            result['MsgKey'] = self.msg_key
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MsgKey') is not None:
            self.msg_key = m.get('MsgKey')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class OnsTraceQueryByMsgKeyResponseBody(TeaModel):
    def __init__(
        self,
        query_id: str = None,
        request_id: str = None,
    ):
        # The ID of the query task. You can call the [OnsTraceGetResult](https://help.aliyun.com/document_detail/59832.html) operation to query the details of the message trace based on the task ID.
        self.query_id = query_id
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTraceQueryByMsgKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsTraceQueryByMsgKeyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsTraceQueryByMsgKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTrendGroupOutputTpsRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        group_id: str = None,
        instance_id: str = None,
        period: int = None,
        topic: str = None,
        type: int = None,
    ):
        # The timestamp that indicates the beginning of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The timestamp that indicates the end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the consumer group that you want to query.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the instance to which the consumer group you want to query belongs.
        self.instance_id = instance_id
        # The sampling period. Unit: minutes. Valid values: 1, 5, and 10.
        self.period = period
        # The name of the topic that you want to query.
        # 
        # This parameter is required.
        self.topic = topic
        # The type of information that you want to query. Valid values:
        # 
        # *   **0**: the number of messages that are consumed during each sampling period.
        # *   **1**: the TPS for message consumption during each sampling period.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period is not None:
            result['Period'] = self.period
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OnsTrendGroupOutputTpsResponseBodyDataRecordsStatsDataDo(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: float = None,
    ):
        # The X axis. The value of this parameter is a UNIX timestamp in milliseconds.
        self.x = x
        # The Y axis. This parameter indicates the TPS for message consumption or the number of messages that are consumed.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class OnsTrendGroupOutputTpsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        stats_data_do: List[OnsTrendGroupOutputTpsResponseBodyDataRecordsStatsDataDo] = None,
    ):
        self.stats_data_do = stats_data_do

    def validate(self):
        if self.stats_data_do:
            for k in self.stats_data_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StatsDataDo'] = []
        if self.stats_data_do is not None:
            for k in self.stats_data_do:
                result['StatsDataDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stats_data_do = []
        if m.get('StatsDataDo') is not None:
            for k in m.get('StatsDataDo'):
                temp_model = OnsTrendGroupOutputTpsResponseBodyDataRecordsStatsDataDo()
                self.stats_data_do.append(temp_model.from_map(k))
        return self


class OnsTrendGroupOutputTpsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: OnsTrendGroupOutputTpsResponseBodyDataRecords = None,
        title: str = None,
        xunit: str = None,
        yunit: str = None,
    ):
        # The data set returned based on sampling period.
        self.records = records
        # The name of the table.
        self.title = title
        # The unit of the timestamp.
        self.xunit = xunit
        # The total number of messages.
        self.yunit = yunit

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.records is not None:
            result['Records'] = self.records.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.xunit is not None:
            result['XUnit'] = self.xunit
        if self.yunit is not None:
            result['YUnit'] = self.yunit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Records') is not None:
            temp_model = OnsTrendGroupOutputTpsResponseBodyDataRecords()
            self.records = temp_model.from_map(m['Records'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('XUnit') is not None:
            self.xunit = m.get('XUnit')
        if m.get('YUnit') is not None:
            self.yunit = m.get('YUnit')
        return self


class OnsTrendGroupOutputTpsResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsTrendGroupOutputTpsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsTrendGroupOutputTpsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTrendGroupOutputTpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsTrendGroupOutputTpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsTrendGroupOutputTpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OnsTrendTopicInputTpsRequest(TeaModel):
    def __init__(
        self,
        begin_time: int = None,
        end_time: int = None,
        instance_id: str = None,
        period: int = None,
        topic: str = None,
        type: int = None,
    ):
        # The timestamp that indicates the beginning of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.begin_time = begin_time
        # The timestamp that indicates the end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the instance to which the topic you want to query belongs.
        self.instance_id = instance_id
        # The sampling period. Unit: minutes. Valid values: 1, 5, and 10.
        self.period = period
        # The name of the topic that you want to query.
        # 
        # This parameter is required.
        self.topic = topic
        # The type of information that you want to query. Valid values:
        # 
        # *   **0**: the number of messages that are published to the topic during each sampling period.
        # *   **1**: the TPS for message publishing in the topic during each sampling period.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.period is not None:
            result['Period'] = self.period
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Period') is not None:
            self.period = m.get('Period')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class OnsTrendTopicInputTpsResponseBodyDataRecordsStatsDataDo(TeaModel):
    def __init__(
        self,
        x: int = None,
        y: float = None,
    ):
        # The X axis. The value of this parameter is a UNIX timestamp in milliseconds.
        self.x = x
        # The Y axis. This parameter indicates the TPS for message publishing or the number of messages that are published.
        self.y = y

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.x is not None:
            result['X'] = self.x
        if self.y is not None:
            result['Y'] = self.y
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')
        if m.get('Y') is not None:
            self.y = m.get('Y')
        return self


class OnsTrendTopicInputTpsResponseBodyDataRecords(TeaModel):
    def __init__(
        self,
        stats_data_do: List[OnsTrendTopicInputTpsResponseBodyDataRecordsStatsDataDo] = None,
    ):
        self.stats_data_do = stats_data_do

    def validate(self):
        if self.stats_data_do:
            for k in self.stats_data_do:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['StatsDataDo'] = []
        if self.stats_data_do is not None:
            for k in self.stats_data_do:
                result['StatsDataDo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stats_data_do = []
        if m.get('StatsDataDo') is not None:
            for k in m.get('StatsDataDo'):
                temp_model = OnsTrendTopicInputTpsResponseBodyDataRecordsStatsDataDo()
                self.stats_data_do.append(temp_model.from_map(k))
        return self


class OnsTrendTopicInputTpsResponseBodyData(TeaModel):
    def __init__(
        self,
        records: OnsTrendTopicInputTpsResponseBodyDataRecords = None,
        title: str = None,
        xunit: str = None,
        yunit: str = None,
    ):
        # The data set returned based on sampling period.
        self.records = records
        # The name of the table.
        self.title = title
        # The unit of the timestamp.
        self.xunit = xunit
        # The unit of the Y axis.
        self.yunit = yunit

    def validate(self):
        if self.records:
            self.records.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.records is not None:
            result['Records'] = self.records.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.xunit is not None:
            result['XUnit'] = self.xunit
        if self.yunit is not None:
            result['YUnit'] = self.yunit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Records') is not None:
            temp_model = OnsTrendTopicInputTpsResponseBodyDataRecords()
            self.records = temp_model.from_map(m['Records'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('XUnit') is not None:
            self.xunit = m.get('XUnit')
        if m.get('YUnit') is not None:
            self.yunit = m.get('YUnit')
        return self


class OnsTrendTopicInputTpsResponseBody(TeaModel):
    def __init__(
        self,
        data: OnsTrendTopicInputTpsResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = OnsTrendTopicInputTpsResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OnsTrendTopicInputTpsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OnsTrendTopicInputTpsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OnsTrendTopicInputTpsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenOnsServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        # The ID of the order.
        self.order_id = order_id
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenOnsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenOnsServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
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
        # The tag key. If you configure this parameter, you must also configure the **Value** parameter.****\
        # *   The value of this parameter cannot be an empty string.
        # *   A tag key must be 1 to 128 characters in length and cannot contain `http://` or `https://`. A tag key cannot start with `acs:` or `aliyun`.
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag that you want to attach to the resource. If you configure this parameter, you must also configure the **Key** parameter.****\
        # *   The value of this parameter can be an empty string.
        # *   A tag value must be 1 to 128 characters in length and cannot contain `http://` or `https://`. A tag value cannot start with `acs:` or `aliyun`.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The ID of the ApsaraMQ for RocketMQ instance that contains the resource to which you want to attach tags.
        # 
        # > This parameter is required when you attach tags to a topic or a group.
        self.instance_id = instance_id
        # The resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource to which you want to attach tags. Valid values:
        # 
        # *   **INSTANCE**\
        # *   **TOPIC**\
        # *   **GROUP**\
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to attach to the resource.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        instance_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags that are attached to the specified resource. This parameter takes effect only if the **TagKey** parameter is empty. Default value: **false**.
        self.all = all
        # This parameter is required when you detach tags from a topic or a group.
        self.instance_id = instance_id
        # The resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource from which you want to detach tags. Valid values:
        # 
        # *   **INSTANCE**\
        # *   **TOPIC**\
        # *   **GROUP**\
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys of the resource.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use the ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


