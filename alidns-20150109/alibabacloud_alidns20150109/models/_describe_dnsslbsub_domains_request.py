# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDNSSLBSubDomainsRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        page_number: int = None,
        page_size: int = None,
        rr: str = None,
        user_client_ip: str = None,
    ):
        # The domain name. Call the [DescribeDomains](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describedomains) operation to obtain the domain name.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language of the response. Valid values are:
        # 
        # - **zh**: Chinese. This is the default value.
        # 
        # - **en**: English.
        self.lang = lang
        # The page number. The value starts from **1**. The default value is **1**.
        self.page_number = page_number
        # The number of entries to return on each page. The maximum value is **100**. The default value is **20**.
        self.page_size = page_size
        # The host record.
        self.rr = rr
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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        return self

