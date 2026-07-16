# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainRecordsRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        domain_name: str = None,
        group_id: int = None,
        key_word: str = None,
        lang: str = None,
        line: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        rrkey_word: str = None,
        search_mode: str = None,
        status: str = None,
        type: str = None,
        type_key_word: str = None,
        value_key_word: str = None,
    ):
        # The sorting direction. Valid values: DESC, ASC. Default value: DESC.
        self.direction = direction
        # The domain name.<props="china"> For more information, see [DescribeDomains](https://help.aliyun.com/zh/dns/api-alidns-2015-01-09-describedomains?spm=a2c4g.11186623.help-menu-search-29697.d_0).
        # <props="intl">For more information, see [DescribeDomains](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomains?spm=a2c63.p38356.help-menu-search-29697.d_0).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The ID of the domain group.
        # 
        # - If you do not specify GroupId, the query is performed on all domain names.
        # 
        # - If you set GroupId to 0, an empty result is returned.
        # 
        # - If you set GroupId to -1, the query is performed on the default group. The default group includes domain names that are not assigned to a group.
        # 
        # - If you set GroupId to -2, the query is performed on all domain names.
        # 
        # - If you specify another value for GroupId, the query is performed on the specified group.
        #   <props="china">For more information, see [DescribeDomainGroups](https://help.aliyun.com/zh/dns/api-alidns-2015-01-09-describedomaingroups?spm=a2c4g.11186623.help-menu-search-29697.d_0).
        #   <props="intl">For more information, see [DescribeDomainGroups](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomaingroups?spm=a2c63.p38356.help-menu-search-29697.d_0).
        self.group_id = group_id
        # The keyword.
        self.key_word = key_word
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The DNS resolution line. Default value: **default**.
        # 
        # For more information, see:
        # <props="china">[Enumeration of DNS resolution lines](https://help.aliyun.com/document_detail/29807.html).
        # 
        # <props="intl">
        # 
        # [Enumeration of DNS resolution lines](https://www.alibabacloud.com/help/zh/doc-detail/29807.htm)
        self.line = line
        # The sorting method. Records are sorted in descending order based on the time they were added.
        self.order_by = order_by
        # The page number. The value starts from **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. Maximum value: **500**. Default value: **20**.
        self.page_size = page_size
        # The keyword for the host record. The search uses a fuzzy match pattern and is not case-sensitive.
        self.rrkey_word = rrkey_word
        # The search mode. Valid values: LIKE, EXACT, ADVANCED, and **COMBINATION**.
        # 
        # - If you set this parameter to LIKE or EXACT, use the KeyWord parameter. The RRKeyWord, TypeKeyWord, ValueKeyWord, Type, Line, and Status parameters are invalid.
        # 
        # - If you set this parameter to ADVANCED, use the RRKeyWord, TypeKeyWord, ValueKeyWord, Type, Line, and Status parameters. The RRKeyWord and ValueKeyWord parameters support fuzzy matching.
        # 
        # - If you set this parameter to COMBINATION, use the RRKeyWord, TypeKeyWord, ValueKeyWord, Type, Line, and Status parameters. All these parameters support only exact matching.
        # 
        # - If you do not specify this parameter:
        # 
        #   - If you specify the keyWord parameter, the search mode is set to LIKE.
        # 
        #   - If you do not specify the keyWord parameter, RRKeyWord and ValueKeyWord support fuzzy matching, and TypeKeyWord, Type, Line, and Status support exact matching.
        self.search_mode = search_mode
        # The status of the DNS record. Valid values:
        # 
        # Enable: The DNS record is enabled.
        # 
        # Disable: The DNS record is paused.
        self.status = status
        # The type of the DNS record. For more information, see:
        # 
        # <props="china">[DNS record types](https://help.aliyun.com/document_detail/29805.html)
        # <props="intl">[DNS record types](https://www.alibabacloud.com/help/zh/doc-detail/29805.htm)
        self.type = type
        # The keyword for the record type. The search uses an exact match and is not case-sensitive.
        self.type_key_word = type_key_word
        # The keyword for the record value. The search uses a fuzzy match pattern and is not case-sensitive.
        self.value_key_word = value_key_word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.key_word is not None:
            result['KeyWord'] = self.key_word

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.line is not None:
            result['Line'] = self.line

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rrkey_word is not None:
            result['RRKeyWord'] = self.rrkey_word

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.type_key_word is not None:
            result['TypeKeyWord'] = self.type_key_word

        if self.value_key_word is not None:
            result['ValueKeyWord'] = self.value_key_word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('KeyWord') is not None:
            self.key_word = m.get('KeyWord')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RRKeyWord') is not None:
            self.rrkey_word = m.get('RRKeyWord')

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeKeyWord') is not None:
            self.type_key_word = m.get('TypeKeyWord')

        if m.get('ValueKeyWord') is not None:
            self.value_key_word = m.get('ValueKeyWord')

        return self

