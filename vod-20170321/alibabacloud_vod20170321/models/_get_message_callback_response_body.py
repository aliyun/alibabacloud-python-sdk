# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class GetMessageCallbackResponseBody(DaraModel):
    def __init__(
        self,
        message_callback: main_models.GetMessageCallbackResponseBodyMessageCallback = None,
        request_id: str = None,
    ):
        # The configuration of the event notification.
        self.message_callback = message_callback
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.message_callback:
            self.message_callback.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message_callback is not None:
            result['MessageCallback'] = self.message_callback.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageCallback') is not None:
            temp_model = main_models.GetMessageCallbackResponseBodyMessageCallback()
            self.message_callback = temp_model.from_map(m.get('MessageCallback'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMessageCallbackResponseBodyMessageCallback(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        auth_key: str = None,
        auth_switch: str = None,
        callback_type: str = None,
        callback_url: str = None,
        event_type_list: str = None,
        mns_endpoint: str = None,
        mns_queue_name: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The cryptographic key. This parameter is returned only for HTTP callbacks.
        self.auth_key = auth_key
        # Indicates whether callback authentication is enabled. This parameter is returned only for HTTP callbacks. Valid values:
        # 
        # *   **on**
        # *   **off**
        self.auth_switch = auth_switch
        # The callback method. Valid values:
        # 
        # *   **HTTP**
        # *   **MNS**
        self.callback_type = callback_type
        # The callback URL. This parameter is returned only for HTTP callbacks.
        self.callback_url = callback_url
        # The type of the callback event.
        self.event_type_list = event_type_list
        # The public endpoint of MNS. This parameter is returned only for MNS callbacks.
        self.mns_endpoint = mns_endpoint
        # The name of the Message Service (MNS) queue. This parameter is returned only for MNS callbacks.
        self.mns_queue_name = mns_queue_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.auth_switch is not None:
            result['AuthSwitch'] = self.auth_switch

        if self.callback_type is not None:
            result['CallbackType'] = self.callback_type

        if self.callback_url is not None:
            result['CallbackURL'] = self.callback_url

        if self.event_type_list is not None:
            result['EventTypeList'] = self.event_type_list

        if self.mns_endpoint is not None:
            result['MnsEndpoint'] = self.mns_endpoint

        if self.mns_queue_name is not None:
            result['MnsQueueName'] = self.mns_queue_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('AuthSwitch') is not None:
            self.auth_switch = m.get('AuthSwitch')

        if m.get('CallbackType') is not None:
            self.callback_type = m.get('CallbackType')

        if m.get('CallbackURL') is not None:
            self.callback_url = m.get('CallbackURL')

        if m.get('EventTypeList') is not None:
            self.event_type_list = m.get('EventTypeList')

        if m.get('MnsEndpoint') is not None:
            self.mns_endpoint = m.get('MnsEndpoint')

        if m.get('MnsQueueName') is not None:
            self.mns_queue_name = m.get('MnsQueueName')

        return self

