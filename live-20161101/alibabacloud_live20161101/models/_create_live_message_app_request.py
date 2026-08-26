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
        # The application name. The name must be 2 to 16 characters in length.
        self.app_name = app_name
        # The security audit mode. Valid values:
        # - 0: default value. Security audit is disabled.
        # - 1: built-in security audit.
        # - 2: custom security audit.
        self.audit_type = audit_type
        # The URL for custom security audit. This parameter is required when custom security audit is selected (AuditType=2). The URL must start with http:// or https://, must not contain private IP addresses, and must not include port numbers. For the format of custom security audit content, see the following section.
        self.audit_url = audit_url
        # The data center. Valid values:
        # - cn-shanghai: default value. Shanghai.
        # - ap-southeast-1: Singapore.
        # 
        # > When calling other interactive messaging API operations, the data center must be the same as the one specified when creating the interactive messaging application.
        self.data_center = data_center
        # The event callback URL for client logon, logout, join group, and leave group events. If this parameter is empty, event callbacks are disabled. For the callback API operations that are triggered, see [Client access](https://help.aliyun.com/document_detail/2672836.html). The event callback URL must start with http:// or https://, must not contain private IP addresses, and must not include port numbers. For the event callback format and callback authentication logic, see the following section.
        self.event_callback_url = event_callback_url
        # The storage duration tier for group messages within the application. Valid values:
        # - 0: default value. Messages are stored for 30 days.
        # - 1: messages are stored for 90 days.
        # - 2: messages are stored for 180 days.
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

