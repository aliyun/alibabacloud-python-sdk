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
        query_condition: str = None,
        recursion_protocol_type: str = None,
        start_timestamp: int = None,
    ):
        # The account ID displayed on the Recursive Resolution (Public DNS) page after you activate Alibaba Cloud Public DNS.
        self.account_id = account_id
        # The domain name.
        self.domain_name = domain_name
        # The end time of the query (timestamp, unit: milliseconds). >Warning: If the query time span is too large and the amount of resolution logs for the queried domain is excessive, it may lead to a query timeout or inaccurate query results.
        self.end_timestamp = end_timestamp
        # Return value language, options: 
        # - zh: Chinese 
        # - en: English
        # 
        # Default: en
        self.lang = lang
        # Module type 
        # - AUTHORITY (default): Public Authoritative DNS 
        # - RECURSION: Public Recursive DNS
        self.module = module
        # Page number, default value is 1.
        self.page_number = page_number
        # Page size for query.
        self.page_size = page_size
        # Query parameters 
        # - sourceIp: Source IP address 
        # - queryNameFuzzy: Domain name (fuzzy value) 
        # - queryType: Record type 
        # - value: Resolution result 
        # - status: Status 
        # - serverIp: Resolution server IP
        self.query_condition = query_condition
        self.recursion_protocol_type = recursion_protocol_type
        # The start time of the query (timestamp, unit: milliseconds).
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

        if m.get('QueryCondition') is not None:
            self.query_condition = m.get('QueryCondition')

        if m.get('RecursionProtocolType') is not None:
            self.recursion_protocol_type = m.get('RecursionProtocolType')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

