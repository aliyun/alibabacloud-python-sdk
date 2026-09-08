# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReadMessageContentRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        class_id: int = None,
        client_source: str = None,
        cookies: str = None,
        group_code: str = None,
        history: bool = None,
        msg_id: str = None,
        src_url: str = None,
        status: int = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        # The language. Default value: Simplified Chinese.
        self.accept_language = accept_language
        # A system parameter. You do not need to specify this parameter.
        self.app_name = app_name
        # A system parameter. You do not need to specify this parameter.
        self.biz_name = biz_name
        # A system parameter. You do not need to specify this parameter.
        self.caller_protocol = caller_protocol
        # Deprecated.
        self.class_id = class_id
        # A system parameter. You do not need to specify this parameter.
        self.client_source = client_source
        # A system parameter. You do not need to specify this parameter.
        self.cookies = cookies
        # The group code.
        self.group_code = group_code
        # Specifies whether the message is a historical message.
        self.history = history
        # The message ID.
        self.msg_id = msg_id
        # A system parameter. You do not need to specify this parameter.
        self.src_url = src_url
        # The read status. Valid values:
        # - 0: unread
        # - 1: read.
        self.status = status
        # A system parameter. You do not need to specify this parameter.
        self.tenant_code = tenant_code
        # A system parameter. You do not need to specify this parameter.
        self.uid_type = uid_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.biz_name is not None:
            result['BizName'] = self.biz_name

        if self.caller_protocol is not None:
            result['CallerProtocol'] = self.caller_protocol

        if self.class_id is not None:
            result['ClassId'] = self.class_id

        if self.client_source is not None:
            result['ClientSource'] = self.client_source

        if self.cookies is not None:
            result['Cookies'] = self.cookies

        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.history is not None:
            result['History'] = self.history

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.src_url is not None:
            result['SrcUrl'] = self.src_url

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code

        if self.uid_type is not None:
            result['UidType'] = self.uid_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BizName') is not None:
            self.biz_name = m.get('BizName')

        if m.get('CallerProtocol') is not None:
            self.caller_protocol = m.get('CallerProtocol')

        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')

        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')

        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')

        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('History') is not None:
            self.history = m.get('History')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')

        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')

        return self

