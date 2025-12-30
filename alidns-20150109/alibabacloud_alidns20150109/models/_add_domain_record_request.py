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
        # The domain name. You can call the [DescribeDomains](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomains?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to obtain the domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English Default: **zh**
        self.lang = lang
        # The resolution line. Default value: **default**. For more information, see
        # 
        # [DNS resolution lines](https://www.alibabacloud.com/help/zh/doc-detail/29807.htm).
        self.line = line
        # The priority of the mail exchanger (MX) record. Valid values: `1 to 50`.
        # 
        # This parameter is required if the type of the DNS record is MX. A smaller value indicates a higher priority.
        self.priority = priority
        # The hostname.
        # 
        # For example, to resolve @.example.com, you must set this parameter to an at sign (@). You cannot leave this parameter empty.
        # 
        # This parameter is required.
        self.rr = rr
        # The time to live (TTL) period of the Alibaba Cloud DNS (DNS) record. Default value: 600. Unit: seconds. For more information, see
        # 
        # [TTL definition](https://www.alibabacloud.com/help/zh/doc-detail/29806.htm).
        self.ttl = ttl
        # The type of the DNS record. For more information, see
        # 
        # [DNS record types](https://www.alibabacloud.com/help/zh/doc-detail/29805.htm).
        # 
        # This parameter is required.
        self.type = type
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The value of the DNS record.
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

