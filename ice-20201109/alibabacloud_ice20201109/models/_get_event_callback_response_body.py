# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetEventCallbackResponseBody(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        auth_switch: str = None,
        callback_queue_name: str = None,
        callback_type: str = None,
        callback_url: str = None,
        event_type_list: str = None,
        request_id: str = None,
    ):
        # The authentication key. This parameter is returned only for HTTP callbacks.
        self.auth_key = auth_key
        # Specifies whether callback authentication is enabled. This parameter is returned only for **HTTP** callbacks. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.auth_switch = auth_switch
        # The name of the Simple Message Queue (SMQ) queue to which callback messages are sent.
        self.callback_queue_name = callback_queue_name
        # The callback method. Valid values:
        # 
        # *   **HTTP**
        # *   **MNS**
        self.callback_type = callback_type
        # The callback URL to which event notifications are sent.
        self.callback_url = callback_url
        # The type of the callback event. Multiple values are separated with commas (,). For more information about callback event types, see [Event notification content](https://help.aliyun.com/document_detail/610204.html).
        self.event_type_list = event_type_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.auth_switch is not None:
            result['AuthSwitch'] = self.auth_switch

        if self.callback_queue_name is not None:
            result['CallbackQueueName'] = self.callback_queue_name

        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type

        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url

        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('AuthSwitch') is not None:
            self.auth_switch = m.get('AuthSwitch')

        if m.get('CallbackQueueName') is not None:
            self.callback_queue_name = m.get('CallbackQueueName')

        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')

        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')

        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

