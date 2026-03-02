# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetSendTraceByMsgIdResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetSendTraceByMsgIdResponseBodyData = None,
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
            temp_model = main_models.GetSendTraceByMsgIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSendTraceByMsgIdResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: List[main_models.GetSendTraceByMsgIdResponseBodyDataVoList] = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            for v1 in self.vo_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VoList'] = []
        if self.vo_list is not None:
            for k1 in self.vo_list:
                result['VoList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vo_list = []
        if m.get('VoList') is not None:
            for k1 in m.get('VoList'):
                temp_model = main_models.GetSendTraceByMsgIdResponseBodyDataVoList()
                self.vo_list.append(temp_model.from_map(k1))

        return self

class GetSendTraceByMsgIdResponseBodyDataVoList(DaraModel):
    def __init__(
        self,
        code: str = None,
        exchange: str = None,
        instance_id: str = None,
        message_body_length: str = None,
        message_properties_map: Dict[str, Any] = None,
        queue_msg_id_map: Dict[str, Any] = None,
        remote_address: str = None,
        routing_key: str = None,
        send_error_info: str = None,
        time_stamp: str = None,
        user_id: str = None,
        vhost: str = None,
    ):
        self.code = code
        self.exchange = exchange
        self.instance_id = instance_id
        self.message_body_length = message_body_length
        self.message_properties_map = message_properties_map
        self.queue_msg_id_map = queue_msg_id_map
        self.remote_address = remote_address
        self.routing_key = routing_key
        self.send_error_info = send_error_info
        self.time_stamp = time_stamp
        self.user_id = user_id
        self.vhost = vhost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.exchange is not None:
            result['Exchange'] = self.exchange

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message_body_length is not None:
            result['MessageBodyLength'] = self.message_body_length

        if self.message_properties_map is not None:
            result['MessagePropertiesMap'] = self.message_properties_map

        if self.queue_msg_id_map is not None:
            result['QueueMsgIdMap'] = self.queue_msg_id_map

        if self.remote_address is not None:
            result['RemoteAddress'] = self.remote_address

        if self.routing_key is not None:
            result['RoutingKey'] = self.routing_key

        if self.send_error_info is not None:
            result['SendErrorInfo'] = self.send_error_info

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vhost is not None:
            result['Vhost'] = self.vhost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Exchange') is not None:
            self.exchange = m.get('Exchange')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MessageBodyLength') is not None:
            self.message_body_length = m.get('MessageBodyLength')

        if m.get('MessagePropertiesMap') is not None:
            self.message_properties_map = m.get('MessagePropertiesMap')

        if m.get('QueueMsgIdMap') is not None:
            self.queue_msg_id_map = m.get('QueueMsgIdMap')

        if m.get('RemoteAddress') is not None:
            self.remote_address = m.get('RemoteAddress')

        if m.get('RoutingKey') is not None:
            self.routing_key = m.get('RoutingKey')

        if m.get('SendErrorInfo') is not None:
            self.send_error_info = m.get('SendErrorInfo')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Vhost') is not None:
            self.vhost = m.get('Vhost')

        return self

