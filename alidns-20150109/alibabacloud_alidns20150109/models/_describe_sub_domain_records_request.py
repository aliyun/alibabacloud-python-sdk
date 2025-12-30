# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSubDomainRecordsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        line: str = None,
        page_number: int = None,
        page_size: int = None,
        sub_domain: str = None,
        type: str = None,
        user_client_ip: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The DNS resolution line.
        self.line = line
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **20**.
        self.page_size = page_size
        # If you set SubDomain to `a.www.example.com` and leave
        # 
        # DomainName empty, the system returns the DNS records that contain the hostname `a.www` for the domain name example.com. If you set SubDomain to a.www.example.com and set DomainName to www.example.com, the system returns the DNS records that contain the hostname `a` for the domain name www.example.com. If you set SubDomain to a.www.example.com and set DomainName to a.www.example.com, the system returns the DNS records that contain the hostname `@` for the domain name a.www.example.com.
        # 
        # This parameter is required.
        self.sub_domain = sub_domain
        # The type of DNS records. If you do not specify this parameter, all types of DNS records for the subdomain name are returned.
        # 
        # Valid values: **A, MX, CNAME, TXT, REDIRECT_URL, FORWORD_URL, NS, AAAA, and SRV**.
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

        if self.line is not None:
            result['Line'] = self.line

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

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

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

