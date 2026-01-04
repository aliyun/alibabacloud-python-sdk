# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDomainResourceRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        instance_ids: List[str] = None,
        page_number: int = None,
        page_size: int = None,
        query_domain_pattern: str = None,
    ):
        # The domain name of the website that you want to query.
        self.domain = domain
        # An array that consists of the IDs of instances to query.
        self.instance_ids = instance_ids
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The match mode. Valid values:
        # 
        # *   **fuzzy**: fuzzy match. This is the default value.
        # *   **exact**: exact match.
        self.query_domain_pattern = query_domain_pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_domain_pattern is not None:
            result['QueryDomainPattern'] = self.query_domain_pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryDomainPattern') is not None:
            self.query_domain_pattern = m.get('QueryDomainPattern')

        return self

