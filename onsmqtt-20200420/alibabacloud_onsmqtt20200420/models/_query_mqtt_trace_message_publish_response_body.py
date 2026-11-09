# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class QueryMqttTraceMessagePublishResponseBody(DaraModel):
    def __init__(
        self,
        message_trace_lists: List[main_models.QueryMqttTraceMessagePublishResponseBodyMessageTraceLists] = None,
        request_id: str = None,
    ):
        # The message traces.
        self.message_trace_lists = message_trace_lists
        # The request ID. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id

    def validate(self):
        if self.message_trace_lists:
            for v1 in self.message_trace_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MessageTraceLists'] = []
        if self.message_trace_lists is not None:
            for k1 in self.message_trace_lists:
                result['MessageTraceLists'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.message_trace_lists = []
        if m.get('MessageTraceLists') is not None:
            for k1 in m.get('MessageTraceLists'):
                temp_model = main_models.QueryMqttTraceMessagePublishResponseBodyMessageTraceLists()
                self.message_trace_lists.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryMqttTraceMessagePublishResponseBodyMessageTraceLists(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_code: str = None,
        action_info: str = None,
        client_id: str = None,
        msg_id: str = None,
        time: str = None,
    ):
        # The action on the message. Valid values:
        # 
        # *   **pub_mqtt**: indicates that the message was sent by an ApsaraMQ for MQTT client.
        # *   **pub_mq**: indicates that the message was sent by an ApsaraMQ for RocketMQ client.
        self.action = action
        # The returned code for the action on the message. Valid values:
        # 
        # *   **mqtt.trace.action.msg.pub.mqtt**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **mqtt.trace.action.msg.pub.mq**: This value is returned if the value of Action is **pub_mq**.
        self.action_code = action_code
        # The returned information for the action on the message. Valid values:
        # 
        # *   **Pub From Mqtt Client**: This value is returned if the value of Action is **pub_mqtt**.
        # *   **Pub From MQ**: This value is returned if the value of Action is **pub_mq**.
        self.action_info = action_info
        # The ID of the client that sends the message.
        self.client_id = client_id
        # The message ID.
        self.msg_id = msg_id
        # The time when the message was sent.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_code is not None:
            result['ActionCode'] = self.action_code

        if self.action_info is not None:
            result['ActionInfo'] = self.action_info

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionCode') is not None:
            self.action_code = m.get('ActionCode')

        if m.get('ActionInfo') is not None:
            self.action_info = m.get('ActionInfo')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

