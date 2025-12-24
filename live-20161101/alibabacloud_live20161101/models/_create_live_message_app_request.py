# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLiveMessageAppRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        audit_type: int = None,
        audit_url: str = None,
        data_center: str = None,
        event_callback_url: str = None,
        msg_life_cycle: int = None,
    ):
        # The name of the application. The name must be 2 to 16 characters in length.
        self.app_name = app_name
        # The content moderation method. Valid values:
        # 
        # *   0 (default): disables content moderation.
        # *   1: uses built-in content moderation.
        # *   2: uses custom content moderation.
        self.audit_type = audit_type
        # The URL for content moderation. If you set AuditType to 2, you must specify this parameter. The URL must start with http:// or https:// and cannot contain a private IP address or a port number. For more information about custom content moderation, see the "Custom content moderation" section of this topic.
        self.audit_url = audit_url
        # The data center. Valid values:
        # 
        # *   cn-shanghai (default)
        # *   ap-southeast-1: Singapore
        # 
        # >  When you call other operations to manage the interactive messaging application, you must specify the same data center in which the application is created.
        self.data_center = data_center
        # The callback URL for events, such as logon, logoff, and joining and leaving a group. If you leave this parameter empty, event callbacks are disabled. [](~~2672836~~)The callback URL must start with http:// or https:// and cannot contain a private IP address or a port number. For information about the callback message format and authentication logic, see the "Event callbacks" and "Callback authentication" sections of this topic.
        self.event_callback_url = event_callback_url
        # The retention period of group messages in the application. Valid values:
        # 
        # *   0 (default): 30 days.
        # *   1: 90 days.
        # *   2: 180 days.
        self.msg_life_cycle = msg_life_cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.audit_type is not None:
            result['AuditType'] = self.audit_type

        if self.audit_url is not None:
            result['AuditUrl'] = self.audit_url

        if self.data_center is not None:
            result['DataCenter'] = self.data_center

        if self.event_callback_url is not None:
            result['EventCallbackUrl'] = self.event_callback_url

        if self.msg_life_cycle is not None:
            result['MsgLifeCycle'] = self.msg_life_cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AuditType') is not None:
            self.audit_type = m.get('AuditType')

        if m.get('AuditUrl') is not None:
            self.audit_url = m.get('AuditUrl')

        if m.get('DataCenter') is not None:
            self.data_center = m.get('DataCenter')

        if m.get('EventCallbackUrl') is not None:
            self.event_callback_url = m.get('EventCallbackUrl')

        if m.get('MsgLifeCycle') is not None:
            self.msg_life_cycle = m.get('MsgLifeCycle')

        return self

