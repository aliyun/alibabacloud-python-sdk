# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHttpDDoSIntelligentAclRulesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        rule_type: str = None,
        site_id: int = None,
    ):
        # This parameter is required.
        self.page_number = page_number
        self.page_size = page_size
        self.rule_type = rule_type
        # This parameter is required.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

