# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_onsmqtt20200420 import models as main_models
from darabonba.model import DaraModel

class QueryMqttTraceMessageSubscribeResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        message_trace_lists: List[main_models.QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists] = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The delivery trace of the queried message.
        self.message_trace_lists = message_trace_lists
        # The number of entries returned per page.
        self.page_size = page_size
        # The unique ID that the system generates for the request. You can use the ID to troubleshoot issues. This parameter is a common parameter.
        self.request_id = request_id
        # The returned delivery traces.
        self.total = total

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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['MessageTraceLists'] = []
        if self.message_trace_lists is not None:
            for k1 in self.message_trace_lists:
                result['MessageTraceLists'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.message_trace_lists = []
        if m.get('MessageTraceLists') is not None:
            for k1 in m.get('MessageTraceLists'):
                temp_model = main_models.QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists()
                self.message_trace_lists.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryMqttTraceMessageSubscribeResponseBodyMessageTraceLists(DaraModel):
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
        # - **sub**: The ApsaraMQ for MQTT client subscribes to the message.
        # 
        # - **push_offline**: The ApsaraMQ for MQTT broker pushes the offline message to the ApsaraMQ for MQTT client.
        self.action = action
        # The code returned for the action on the message. Valid values:
        # 
        # - **mqtt.trace.action.msg.sub**: The value that is returned if the value of Action is **sub**.
        # 
        # - **mqtt.trace.action.msg.push.offline**: The value that is returned if the value of Action is **push_offline**.
        self.action_code = action_code
        # The returned information for the action on the message. Valid values:
        # 
        # - **Push To Mqtt Client**: The value that is returned if the value of Action is **sub**.
        # 
        # - **Push Offline Msg To Mqtt Client**: The value that is returned if the value of Action is **push_offline**.
        self.action_info = action_info
        # The ID of the client that subscribes to the message.
        self.client_id = client_id
        # The message ID.
        self.msg_id = msg_id
        # The time when the message was delivered.
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

