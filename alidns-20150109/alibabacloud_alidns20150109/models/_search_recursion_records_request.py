# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchRecursionRecordsRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        enable_status: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        page_number: int = None,
        page_size: int = None,
        remark: str = None,
        request_source: str = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        value: str = None,
        weight: int = None,
        zone_id: str = None,
    ):
        # The sort order. Valid values: asc for ascending and dsc for descending.
        self.direction = direction
        # The status of the DNS record. Valid values: enable and **disable**.
        self.enable_status = enable_status
        # The maximum number of records to return for the current request.
        self.max_results = max_results
        # The token used to start the next query.
        self.next_token = next_token
        # The sorting method. Valid values: rr, type, value, requestSource, weight, ttl, and enableStatus.
        self.order_by = order_by
        # The current page number. The value starts from 1. The default value is 1.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries to return on each page for a paged query. The maximum value is 100. The default value is 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The remarks.
        self.remark = remark
        # The DNS resolution line. The default value is **default**. For more information, see [DNS resolution lines](https://www.alibabacloud.com/help/en/doc-detail/29807.htm).
        # 
        # <props="china">
        # 
        # [DNS Line Enumeration](https://help.aliyun.com/document_detail/29807.html)
        # 
        # 
        # 
        # <props="intl">
        # 
        # [Resolution Line Enumeration](https://www.alibabacloud.com/help/zh/doc-detail/29807.htm)
        self.request_source = request_source
        # The host record.
        self.rr = rr
        # The time to live (TTL) in the local cache, in seconds. Valid values are 5, 30, 60, 3600 (1 hour), 43200 (12 hours), and 86400 (1 day). The default value is 60.
        self.ttl = ttl
        # The type of the DNS record. The following types are supported:A: Maps a domain name to an IPv4 address.AAAA: Maps a domain name to an IPv6 address.CNAME: An alias record that points a domain name to another domain name.MX: A mail exchanger record that points a domain name to a mail server.TXT: A text record that contains arbitrary human-readable text.SRV: A service record that identifies a server for a specific service. This is common in directory management for Microsoft systems.
        self.type = type
        # The record value.
        self.value = value
        # The weight of the DNS record. The value ranges from 0 to 100.
        self.weight = weight
        # The zone ID of the DNS record.
        # 
        # This parameter is required.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.request_source is not None:
            result['RequestSource'] = self.request_source

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.weight is not None:
            result['Weight'] = self.weight

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RequestSource') is not None:
            self.request_source = m.get('RequestSource')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

