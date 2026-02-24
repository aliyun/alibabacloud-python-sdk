# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListManagedRulesRequest(DaraModel):
    def __init__(
        self,
        filter_type: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_types: str = None,
        risk_level: int = None,
    ):
        # The scope of the filter.
        self.filter_type = filter_type
        # The keyword of the rule template.
        self.keyword = keyword
        # The page number.
        # 
        # The value must be greater than or equal to 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100. Default value: 10.
        self.page_size = page_size
        # The resource type that is evaluated by the rule.
        self.resource_types = resource_types
        # The risk level of the rule template. Valid values:
        # 
        # - 1: high
        # 
        # - 2: medium
        # 
        # - 3: low
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_type is not None:
            result['FilterType'] = self.filter_type

        if self.keyword is not None:
            result['Keyword'] = self.keyword

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterType') is not None:
            self.filter_type = m.get('FilterType')

        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

