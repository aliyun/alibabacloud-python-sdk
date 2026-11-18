# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConsumerQuotaRulesRequest(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        rule_status: str = None,
    ):
        # The gateway ID. This parameter is optional.
        self.gateway_id = gateway_id
        # The keyword used to perform a fuzzy match on the rule name.
        self.keyword = keyword
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The rule status. This parameter is optional. Valid values: enabled and disabled. If this parameter is not specified, all rules are queried.
        self.rule_status = rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.keyword is not None:
            result['keyword'] = self.keyword

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.rule_status is not None:
            result['ruleStatus'] = self.rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('ruleStatus') is not None:
            self.rule_status = m.get('ruleStatus')

        return self

