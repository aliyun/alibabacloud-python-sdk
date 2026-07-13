# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRecordLogsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        key_word: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        start_date: str = None,
        user_client_ip: str = None,
        end_date: str = None,
    ):
        # The domain name.<props="china">You can call the [DescribeDomains](https://help.aliyun.com/document_detail/29751.html) operation to obtain the domain name.<props="intl">You can call the [DescribeDomains](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describedomains) operation to obtain the domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The keyword. The system searches for the keyword in the "%KeyWord%" pattern. The search is not case-sensitive.
        self.key_word = key_word
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The page number. The value starts from **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is **100**. Default value: **20**.
        self.page_size = page_size
        # The start of the time range to query. The format is **YYYY-MM-DD**.
        self.start_date = start_date
        # The client IP address.
        self.user_client_ip = user_client_ip
        # The end of the time range to query. The format is **YYYY-MM-DD**.
        self.end_date = end_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.end_date is not None:
            result['endDate'] = self.end_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')

        return self

