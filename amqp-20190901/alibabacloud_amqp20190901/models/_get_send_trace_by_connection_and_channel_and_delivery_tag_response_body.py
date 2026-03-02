# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBodyData = None,
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
            temp_model = main_models.GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSendTraceByConnectionAndChannelAndDeliveryTagResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        delay: str = None,
        exchange: str = None,
        expiration: str = None,
        message_id: str = None,
        queue_msg_id_map: Dict[str, Any] = None,
        remote_address: str = None,
        routing_key: str = None,
        send_error_info: str = None,
        time_stamp: str = None,
        user_id: str = None,
        vhost: str = None,
        xdelay: str = None,
    ):
        self.code = code
        self.delay = delay
        self.exchange = exchange
        self.expiration = expiration
        self.message_id = message_id
        self.queue_msg_id_map = queue_msg_id_map
        self.remote_address = remote_address
        self.routing_key = routing_key
        self.send_error_info = send_error_info
        self.time_stamp = time_stamp
        self.user_id = user_id
        self.vhost = vhost
        self.xdelay = xdelay

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.delay is not None:
            result['Delay'] = self.delay

        if self.exchange is not None:
            result['Exchange'] = self.exchange

        if self.expiration is not None:
            result['Expiration'] = self.expiration

        if self.message_id is not None:
            result['MessageId'] = self.message_id

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

        if self.xdelay is not None:
            result['XDelay'] = self.xdelay

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Delay') is not None:
            self.delay = m.get('Delay')

        if m.get('Exchange') is not None:
            self.exchange = m.get('Exchange')

        if m.get('Expiration') is not None:
            self.expiration = m.get('Expiration')

        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')

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

        if m.get('XDelay') is not None:
            self.xdelay = m.get('XDelay')

        return self

