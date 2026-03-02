# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class QueryMessageByQueueNameResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.QueryMessageByQueueNameResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.QueryMessageByQueueNameResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMessageByQueueNameResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        task_id: str = None,
        total_count: int = None,
        vo_list: main_models.QueryMessageByQueueNameResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.task_id = task_id
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VoList') is not None:
            temp_model = main_models.QueryMessageByQueueNameResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m.get('VoList'))

        return self

class QueryMessageByQueueNameResponseBodyDataVoList(DaraModel):
    def __init__(
        self,
        amqp_message_vo: List[main_models.QueryMessageByQueueNameResponseBodyDataVoListAmqpMessageVO] = None,
    ):
        self.amqp_message_vo = amqp_message_vo

    def validate(self):
        if self.amqp_message_vo:
            for v1 in self.amqp_message_vo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AmqpMessageVO'] = []
        if self.amqp_message_vo is not None:
            for k1 in self.amqp_message_vo:
                result['AmqpMessageVO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.amqp_message_vo = []
        if m.get('AmqpMessageVO') is not None:
            for k1 in m.get('AmqpMessageVO'):
                temp_model = main_models.QueryMessageByQueueNameResponseBodyDataVoListAmqpMessageVO()
                self.amqp_message_vo.append(temp_model.from_map(k1))

        return self

class QueryMessageByQueueNameResponseBodyDataVoListAmqpMessageVO(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        body: str = None,
        cluster_id: str = None,
        content_encoding: str = None,
        content_type: str = None,
        correlation_id: str = None,
        delivery_mode: int = None,
        exchange_name: str = None,
        expiration: str = None,
        headers: str = None,
        immediate: bool = None,
        mandatory: bool = None,
        message_id: str = None,
        priority: int = None,
        process_token: str = None,
        reconsume_times: int = None,
        reply_to: str = None,
        routing_key: str = None,
        store_timestamp: int = None,
        timestamp: int = None,
        type: str = None,
        user_id: str = None,
    ):
        self.app_id = app_id
        self.body = body
        self.cluster_id = cluster_id
        self.content_encoding = content_encoding
        self.content_type = content_type
        self.correlation_id = correlation_id
        self.delivery_mode = delivery_mode
        self.exchange_name = exchange_name
        self.expiration = expiration
        self.headers = headers
        self.immediate = immediate
        self.mandatory = mandatory
        self.message_id = message_id
        self.priority = priority
        self.process_token = process_token
        self.reconsume_times = reconsume_times
        self.reply_to = reply_to
        self.routing_key = routing_key
        self.store_timestamp = store_timestamp
        self.timestamp = timestamp
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.body is not None:
            result['Body'] = self.body

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.correlation_id is not None:
            result['CorrelationId'] = self.correlation_id

        if self.delivery_mode is not None:
            result['DeliveryMode'] = self.delivery_mode

        if self.exchange_name is not None:
            result['ExchangeName'] = self.exchange_name

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.headers is not None:
            result['Headers'] = self.headers

        if self.immediate is not None:
            result['Immediate'] = self.immediate

        if self.mandatory is not None:
            result['Mandatory'] = self.mandatory

        if self.message_id is not None:
            result['MessageId'] = self.message_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.process_token is not None:
            result['ProcessToken'] = self.process_token

        if self.reconsume_times is not None:
            result['ReconsumeTimes'] = self.reconsume_times

        if self.reply_to is not None:
            result['ReplyTo'] = self.reply_to

        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key

        if self.store_timestamp is not None:
            result['StoreTimestamp'] = self.store_timestamp

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Body') is not None:
            self.body = m.get('Body')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('CorrelationId') is not None:
            self.correlation_id = m.get('CorrelationId')

        if m.get('DeliveryMode') is not None:
            self.delivery_mode = m.get('DeliveryMode')

        if m.get('ExchangeName') is not None:
            self.exchange_name = m.get('ExchangeName')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('Headers') is not None:
            self.headers = m.get('Headers')

        if m.get('Immediate') is not None:
            self.immediate = m.get('Immediate')

        if m.get('Mandatory') is not None:
            self.mandatory = m.get('Mandatory')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProcessToken') is not None:
            self.process_token = m.get('ProcessToken')

        if m.get('ReconsumeTimes') is not None:
            self.reconsume_times = m.get('ReconsumeTimes')

        if m.get('ReplyTo') is not None:
            self.reply_to = m.get('ReplyTo')

        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')

        if m.get('StoreTimestamp') is not None:
            self.store_timestamp = m.get('StoreTimestamp')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

