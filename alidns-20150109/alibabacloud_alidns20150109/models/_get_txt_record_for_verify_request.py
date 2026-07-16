# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTxtRecordForVerifyRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        lang: str = None,
        type: str = None,
    ):
        # The domain name. The [DescribeDomains](https://www.alibabacloud.com/help/en/dns/api-alidns-2015-01-09-describedomains) operation returns a list of domain names.
        self.domain_name = domain_name
        # The language of the request and response. Default value: **zh**. Valid values:
        # 
        # - **zh**: Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The purpose of the TXT record verification. Valid values:
        # 
        # - ADD_SUB_DOMAIN: Add a subdomain for verification.
        # 
        # - RETRIEVAL: Other verifications.
        # 
        # This parameter is required.
        self.type = type

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

