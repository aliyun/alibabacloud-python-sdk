# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddDomainRecordRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        line: str = None,
        priority: int = None,
        rr: str = None,
        ttl: int = None,
        type: str = None,
        user_client_ip: str = None,
        value: str = None,
    ):
        # The domain name. Call the [DescribeDomains](https://www.alibabacloud.com/help/dns/api-alidns-2015-01-09-describedomains?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to query the domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language of the request and response. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        #   The default value is **zh**.
        self.lang = lang
        # The DNS resolution line. The default value is **default**. For more information, see [DNS resolution lines](https://www.alibabacloud.com/help/doc-detail/29807.htm).
        # 
        # <props="china">
        # 
        # [Resolution line enumeration](https://help.aliyun.com/document_detail/29807.html)
        # 
        # 
        # 
        # <props="intl">
        # 
        # [Resolution Line Enumeration](https://www.alibabacloud.com/help/zh/doc-detail/29807.htm)
        self.line = line
        # The priority of the MX record. Valid values: `[1,50]`.
        # 
        # This parameter is required if the record type is MX. A smaller value indicates a higher priority.
        self.priority = priority
        # The host record.
        # 
        # To resolve example.com, set the host record to "@" instead of leaving it empty.
        # 
        # This parameter is required.
        self.rr = rr
        # The time to live (TTL) value of the Domain Name System (DNS) record. Default value: 600. Unit: seconds. For more information, see the following topic:
        # 
        # <props="china">
        # 
        # [TTL overview](https://help.aliyun.com/document_detail/29806.html)
        # 
        # 
        # 
        # <props="intl">
        # 
        # The time to live (TTL) of the DNS record. The default value is 600 seconds. For more information, see [TTL](https://www.alibabacloud.com/help/doc-detail/29806.htm).
        self.ttl = ttl
        # The type of the DNS record. For more information, see
        # 
        # <props="china">
        # 
        # [DNS record type format](https://help.aliyun.com/document_detail/29805.html)
        # 
        # 
        # 
        # <props="intl">
        # 
        # The type of the DNS record. For more information, see [DNS record types](https://www.alibabacloud.com/help/doc-detail/29805.htm).
        # 
        # This parameter is required.
        self.type = type
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The record value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.line is not None:
            result['Line'] = self.line

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.rr is not None:
            result['RR'] = self.rr

        if self.ttl is not None:
            result['TTL'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('TTL') is not None:
            self.ttl = m.get('TTL')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

