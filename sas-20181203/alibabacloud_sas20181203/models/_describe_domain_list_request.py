# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        domain_type: str = None,
        fuzzy_domain: str = None,
        page_size: int = None,
        source_ip: str = None,
    ):
        # The page number of the page to return in a paged query. Default value: **1**, which indicates that the first page is returned.
        self.current_page = current_page
        # The type of the domain name to query. Valid values:
        # 
        # - **root**: root domain name
        # - **sub**: subdomain name.
        self.domain_type = domain_type
        # The search keyword for the domain name to query. Fuzzy match is supported.
        self.fuzzy_domain = fuzzy_domain
        # The number of domain names to display on each page in a paged query. Default value: **10**, which indicates that 10 domain names are displayed on each page.
        self.page_size = page_size
        # The IP address of the access source.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.domain_type is not None:
            result['DomainType'] = self.domain_type

        if self.fuzzy_domain is not None:
            result['FuzzyDomain'] = self.fuzzy_domain

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DomainType') is not None:
            self.domain_type = m.get('DomainType')

        if m.get('FuzzyDomain') is not None:
            self.fuzzy_domain = m.get('FuzzyDomain')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

