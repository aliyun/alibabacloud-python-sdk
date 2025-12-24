# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLiveMessageAppCallbackResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_sign: str = None,
        event_callback_need_authentication: bool = None,
        event_callback_url: str = None,
        request_id: str = None,
    ):
        # The ID of the interactive messaging application.
        self.app_id = app_id
        # The signature of the interactive messaging application. It is required by the interactive messaging SDK.
        self.app_sign = app_sign
        # Indicates whether authentication is required for event callbacks. Default value: true.
        self.event_callback_need_authentication = event_callback_need_authentication
        # The callback URL for events such as user logon, logoff, joining a group, and leaving a group. This parameter is not returned if it has an empty value.
        self.event_callback_url = event_callback_url
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_sign is not None:
            result['AppSign'] = self.app_sign

        if self.event_callback_need_authentication is not None:
            result['EventCallbackNeedAuthentication'] = self.event_callback_need_authentication

        if self.event_callback_url is not None:
            result['EventCallbackUrl'] = self.event_callback_url

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppSign') is not None:
            self.app_sign = m.get('AppSign')

        if m.get('EventCallbackNeedAuthentication') is not None:
            self.event_callback_need_authentication = m.get('EventCallbackNeedAuthentication')

        if m.get('EventCallbackUrl') is not None:
            self.event_callback_url = m.get('EventCallbackUrl')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

