# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetMessageCallbackRequest(DaraModel):
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
        owner_account: str = None,
    ):
        # The application ID. If this parameter is not specified, the ID of the default application is used, which is the fixed value: **app-1000000**.
        self.app_id = app_id
        # The authentication key. The key can be up to 32 characters in length and must contain uppercase letters, lowercase letters, and digits. This parameter can be set when the callback method is **HTTP**.
        self.auth_key = auth_key
        # The authentication switch for HTTP callbacks. This parameter takes effect only when the callback method is set to **HTTP**. Valid values:
        # - **on**: enabled.
        # - **off**: disabled.
        self.auth_switch = auth_switch
        # The callback method. Valid values:
        # - **HTTP**
        # - **Simple Message Queue (formerly MNS)**
        self.callback_type = callback_type
        # The callback URL. This parameter is required when the callback method is set to **HTTP**.
        # The callback URL cannot exceed 256 bytes in length. Multiple callback URLs are not supported.
        self.callback_url = callback_url
        # The event types for callbacks. If this parameter is left empty, all notifications are disabled. If this parameter is set to **ALL**, all notifications are enabled. You can also specify specific event types, separated by commas (,). For the valid event types, see [Event types](https://help.aliyun.com/document_detail/55627.html).
        # 
        # <props="china">
        # > All AI-related events such as AIMediaAuditComplete and AIMediaDNAComplete use the value **AIComplete**.
        self.event_type_list = event_type_list
        # The public endpoint of Simple Message Queue (formerly MNS). This parameter is required when the callback method is set to **Simple Message Queue (formerly MNS)**. Log on to the [Simple Message Queue (formerly MNS) console](https://account.aliyun.com/login/login.html) and click the **Get Endpoint** button in the upper-right corner to obtain the endpoint. For more information, see [Endpoint](https://help.aliyun.com/document_detail/27480.html).
        self.mns_endpoint = mns_endpoint
        # The name of the message queue. Log on to the [Simple Message Queue (formerly MNS) console](https://account.aliyun.com/login/login.html) and view the queue in the **Queue List**. This parameter is required when the callback method is set to **Simple Message Queue (formerly MNS)**.
        self.mns_queue_name = mns_queue_name
        self.owner_account = owner_account

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

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

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

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        return self

