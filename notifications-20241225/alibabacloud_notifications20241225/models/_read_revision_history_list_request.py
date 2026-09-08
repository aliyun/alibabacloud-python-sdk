# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadRevisionHistoryListRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        biz_name: str = None,
        caller_protocol: str = None,
        category_code: str = None,
        channel_group_code: str = None,
        client_source: str = None,
        cookies: str = None,
        page_info: main_models.ReadRevisionHistoryListRequestPageInfo = None,
        src_url: str = None,
        tenant_code: str = None,
        uid_type: str = None,
    ):
        # The language. Automatically passed through by the browser. You can manually override this value.
        self.accept_language = accept_language
        # Ignored. No need to pass this parameter. The application name of the caller.
        self.app_name = app_name
        # Ignored. No need to pass this parameter. The business line of the caller.
        self.biz_name = biz_name
        # Ignored. No need to pass this parameter. The request protocol type.
        self.caller_protocol = caller_protocol
        # The category code.
        self.category_code = category_code
        # The channel group.
        self.channel_group_code = channel_group_code
        # Ignored. No need to pass this parameter. The source of the operation terminal.
        self.client_source = client_source
        # Ignored. No need to pass this parameter. The user cookies.
        self.cookies = cookies
        # The pagination information.
        self.page_info = page_info
        # Ignored. No need to pass this parameter. The source page URL.
        self.src_url = src_url
        # Ignored. No need to pass this parameter. The tenant information.
        self.tenant_code = tenant_code
        # Ignored. No need to pass this parameter. The user type.
        self.uid_type = uid_type

    def validate(self):
        if self.page_info:
            self.page_info.validate()

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

        if self.category_code is not None:
            result['CategoryCode'] = self.category_code

        if self.channel_group_code is not None:
            result['ChannelGroupCode'] = self.channel_group_code

        if self.client_source is not None:
            result['ClientSource'] = self.client_source

        if self.cookies is not None:
            result['Cookies'] = self.cookies

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

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

        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')

        if m.get('ChannelGroupCode') is not None:
            self.channel_group_code = m.get('ChannelGroupCode')

        if m.get('ClientSource') is not None:
            self.client_source = m.get('ClientSource')

        if m.get('Cookies') is not None:
            self.cookies = m.get('Cookies')

        if m.get('PageInfo') is not None:
            temp_model = main_models.ReadRevisionHistoryListRequestPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('SrcUrl') is not None:
            self.src_url = m.get('SrcUrl')

        if m.get('TenantCode') is not None:
            self.tenant_code = m.get('TenantCode')

        if m.get('UidType') is not None:
            self.uid_type = m.get('UidType')

        return self

class ReadRevisionHistoryListRequestPageInfo(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        return_total_count: bool = None,
    ):
        # The maximum number of entries to return.
        self.max_results = max_results
        # The token for the next page of data.
        self.next_token = next_token
        # Specifies whether to return the total count.
        self.return_total_count = return_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.return_total_count is not None:
            result['ReturnTotalCount'] = self.return_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ReturnTotalCount') is not None:
            self.return_total_count = m.get('ReturnTotalCount')

        return self

