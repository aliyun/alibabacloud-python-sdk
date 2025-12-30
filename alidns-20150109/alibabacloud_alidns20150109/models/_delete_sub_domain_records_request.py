# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSubDomainRecordsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        rr: str = None,
        type: str = None,
        user_client_ip: str = None,
    ):
        # The domain name. You can call the [DescribeDomains](https://www.alibabacloud.com/help/zh/dns/api-alidns-2015-01-09-describedomains?spm=a2c63.p38356.help-menu-search-29697.d_0) operation to obtain the domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The hostname field in the DNS record.
        # 
        # For example, if you want to resolve @.example.com, you must set this parameter to an at sign (@) instead of leaving it empty.
        # 
        # This parameter is required.
        self.rr = rr
        # The type of DNS records. If you do not specify this parameter, all types of DNS records corresponding to the subdomain are returned.
        # 
        # Valid values: **A, MX, CNAME, TXT, REDIRECT_URL, FORWORD_URL, NS, AAAA, and SRV**. The value is not case-sensitive.
        self.type = type
        # The IP address of the client.
        self.user_client_ip = user_client_ip

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

        if self.rr is not None:
            result['RR'] = self.rr

        if self.type is not None:
            result['Type'] = self.type

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RR') is not None:
            self.rr = m.get('RR')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

