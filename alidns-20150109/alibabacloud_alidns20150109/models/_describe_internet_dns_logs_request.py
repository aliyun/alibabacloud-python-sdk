# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeInternetDnsLogsRequest(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        domain_name: str = None,
        end_timestamp: int = None,
        lang: str = None,
        module: str = None,
        page_number: int = None,
        page_size: int = None,
        precise_sort: bool = None,
        query_condition: str = None,
        recursion_protocol_type: str = None,
        start_timestamp: int = None,
    ):
        # The ID of the Public DNS configuration.
        self.account_id = account_id
        # The domain name.
        self.domain_name = domain_name
        # The end of the time range to query. This is a UNIX timestamp in milliseconds.
        # >Warning: If you specify a wide time range, many logs may be returned. This can cause a query timeout or inaccurate results.
        self.end_timestamp = end_timestamp
        # The language of the response. Valid values:
        # 
        # - zh: Chinese
        # 
        # - en: English
        # 
        # Default value: en.
        self.lang = lang
        # The module type.
        # 
        # - AUTHORITY (default): public authoritative DNS
        # 
        # - RECURSION: public recursive DNS
        self.module = module
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        self.page_size = page_size
        self.precise_sort = precise_sort
        # The query parameters.
        # 
        # - sourceIp: the source IP address
        # 
        # - queryNameFuzzy: the domain name (fuzzy match)
        # 
        # - queryType: the record type
        # 
        # - value: the resolution result
        # 
        # - status: the status
        # 
        # - serverIp: the IP address of the resolution server
        self.query_condition = query_condition
        self.recursion_protocol_type = recursion_protocol_type
        # The start of the time range to query. This is a UNIX timestamp in milliseconds.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.module is not None:
            result['Module'] = self.module

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.precise_sort is not None:
            result['PreciseSort'] = self.precise_sort

        if self.query_condition is not None:
            result['QueryCondition'] = self.query_condition

        if self.recursion_protocol_type is not None:
            result['RecursionProtocolType'] = self.recursion_protocol_type

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PreciseSort') is not None:
            self.precise_sort = m.get('PreciseSort')

        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')

        if m.get('RecursionProtocolType') is not None:
            self.recursion_protocol_type = m.get('RecursionProtocolType')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

