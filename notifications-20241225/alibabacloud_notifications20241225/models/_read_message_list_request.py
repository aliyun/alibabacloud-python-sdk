# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReadMessageListRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        class_id: int = None,
        client_source: str = None,
        content: str = None,
        cookies: str = None,
        group_code: str = None,
        history: str = None,
        loc: str = None,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        src_url: str = None,
        status: int = None,
        tenant_code: str = None,
        title: str = None,
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
        # The message content. This parameter is used for fuzzy match.
        self.content = content
        # A system parameter. You do not need to specify this parameter.
        self.cookies = cookies
        # The group code.
        self.group_code = group_code
        # Specifies whether the messages are historical messages.
        self.history = history
        # The location.
        self.loc = loc
        # A system parameter. You do not need to specify this parameter.
        self.max_results = max_results
        # A system parameter. You do not need to specify this parameter.
        self.next_token = next_token
        # The page number for the paged query.
        self.page = page
        # The page size for the paged query.
        self.page_size = page_size
        # A system parameter. You do not need to specify this parameter.
        self.src_url = src_url
        # The message status. A value of 1 indicates read. A value of 0 indicates unread. A value of -1 indicates all. Default value: -1.
        self.status = status
        # A system parameter. You do not need to specify this parameter.
        self.tenant_code = tenant_code
        # The message title. This parameter is used for fuzzy match.
        self.title = title
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

        if self.content is not None:
            result['Content'] = self.content

        if self.cookies is not None:
            result['Cookies'] = self.cookies

        if self.group_code is not None:
            result['GroupCode'] = self.group_code

        if self.history is not None:
            result['History'] = self.history

        if self.loc is not None:
            result['Loc'] = self.loc

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.src_url is not None:
            result['SrcUrl'] = self.src_url

        if self.status is not None:
            result['Status'] = self.status

        if self.tenant_code is not None:
            result['TenantCode'] = self.tenant_code

        if self.title is not None:
            result['Title'] = self.title

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

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')

        if m.get('GroupCode') is not None:
            self.group_code = m.get('GroupCode')

        if m.get('History') is not None:
            self.history = m.get('History')

        if m.get('Loc') is not None:
            self.loc = m.get('Loc')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')

        return self

