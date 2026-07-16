# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainDnssecInfoRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
    ):
        # The domain name. To obtain the domain name, call [DescribeDomains](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describedomains).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The language of the request and response. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        # 
        # The default value is **zh**.
        self.lang = lang

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self

