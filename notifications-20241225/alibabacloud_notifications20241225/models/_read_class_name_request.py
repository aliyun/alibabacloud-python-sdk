# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReadClassNameRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        client_source: str = None,
        cookies: str = None,
        src_url: str = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        # The language. Default value: Simplified Chinese.
        self.accept_language = accept_language
        # System parameter. You do not need to specify this parameter.
        self.app_name = app_name
        # System parameter. You do not need to specify this parameter.
        self.biz_name = biz_name
        # System parameter. You do not need to specify this parameter.
        self.caller_protocol = caller_protocol
        # System parameter. You do not need to specify this parameter.
        self.client_source = client_source
        # System parameter. You do not need to specify this parameter.
        self.cookies = cookies
        # System parameter. You do not need to specify this parameter.
        self.src_url = src_url
        # System parameter. You do not need to specify this parameter.
        self.tenant_code = tenant_code
        # System parameter. You do not need to specify this parameter.
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

        if self.client_source is not None:
            result['ClientSource'] = self.client_source

        if self.cookies is not None:
            result['Cookies'] = self.cookies

        if self.src_url is not None:
            result['SrcUrl'] = self.src_url

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

        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')

        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')

        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')

        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')

        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')

        return self

