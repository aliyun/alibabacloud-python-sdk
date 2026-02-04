# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnWafPolicyValidDomainsRequest(DaraModel):
    def __init__(
        self,
        defense_scene: str = None,
        domain_name_like: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The type of the Web Application Firewall (WAF) protection policy. Valid values:
        # 
        # *   waf_group: basic web protection
        # *   custom_acl: custom protection
        # *   whitelist: IP address whitelist
        # *   ip_blacklist: IP address blacklist
        # *   region_block: region blacklist
        # *   bot: bot management
        # 
        # This parameter is required.
        self.defense_scene = defense_scene
        # The protected domain name. Fuzzy search is supported.
        self.domain_name_like = domain_name_like
        # The page number of the returned page. Valid values: **1** to **100000**. Default value: **1**.
        self.page_number = page_number
        # The number of domain names to return on each page. Valid values: an integer from **1** to **500**. Default value: **20**.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.defense_scene is not None:
            result['DefenseScene'] = self.defense_scene

        if self.domain_name_like is not None:
            result['DomainNameLike'] = self.domain_name_like

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefenseScene') is not None:
            self.defense_scene = m.get('DefenseScene')

        if m.get('DomainNameLike') is not None:
            self.domain_name_like = m.get('DomainNameLike')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

