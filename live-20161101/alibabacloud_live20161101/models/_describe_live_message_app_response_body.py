# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveMessageAppResponseBody(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_key: str = None,
        app_name: str = None,
        app_sign: str = None,
        audit_type: int = None,
        audit_url: str = None,
        create_time: int = None,
        data_center: str = None,
        disable: bool = None,
        event_callback_url: str = None,
        modify_time: int = None,
        msg_life_cycle: int = None,
        request_id: str = None,
    ):
        # The ID of the interactive messaging application.
        self.app_id = app_id
        # The AppKey of the interactive messaging application. It is used to authorize operations related to the application ID.
        self.app_key = app_key
        # The name of the interactive messaging application.
        self.app_name = app_name
        # The signature of the interactive messaging application. It is required by the interactive messaging SDK.
        self.app_sign = app_sign
        # The content moderation method. Valid values:
        # 
        # *   0: Content moderation is disabled.
        # *   1: Built-in content moderation is used.
        # *   2: Custom content moderation is used.
        self.audit_type = audit_type
        # The URL for content moderation. This parameter is returned when the value of AuditType is 2.
        self.audit_url = audit_url
        # The time when the interactive messaging application was created. The value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # The data center.
        self.data_center = data_center
        # Indicates whether the interactive messaging application is disabled.
        self.disable = disable
        # The callback URL for events such as user logon, logoff, joining a group, and leaving a group. An empty value indicates that callbacks are disabled.
        self.event_callback_url = event_callback_url
        # The time when the interactive messaging application was modified. The value is a UNIX timestamp. Unit: seconds.
        self.modify_time = modify_time
        # The retention period of group messages in the application. Valid values:
        # 
        # *   0 (default): 30 days
        # *   1: 90 days
        # *   2: 180 days
        self.msg_life_cycle = msg_life_cycle
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

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_sign is not None:
            result['AppSign'] = self.app_sign

        if self.audit_type is not None:
            result['AuditType'] = self.audit_type

        if self.audit_url is not None:
            result['AuditUrl'] = self.audit_url

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.disable is not None:
            result['Disable'] = self.disable

        if self.event_callback_url is not None:
            result['EventCallbackUrl'] = self.event_callback_url

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.msg_life_cycle is not None:
            result['MsgLifeCycle'] = self.msg_life_cycle

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppSign') is not None:
            self.app_sign = m.get('AppSign')

        if m.get('AuditType') is not None:
            self.audit_type = m.get('AuditType')

        if m.get('AuditUrl') is not None:
            self.audit_url = m.get('AuditUrl')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('Disable') is not None:
            self.disable = m.get('Disable')

        if m.get('EventCallbackUrl') is not None:
            self.event_callback_url = m.get('EventCallbackUrl')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('MsgLifeCycle') is not None:
            self.msg_life_cycle = m.get('MsgLifeCycle')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

