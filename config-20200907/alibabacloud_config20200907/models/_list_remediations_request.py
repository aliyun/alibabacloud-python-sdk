# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRemediationsRequest(DaraModel):
    def __init__(
        self,
        config_rule_ids: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The rule IDs. Separate multiple rule IDs with commas (,).
        # 
        # For more information about how to obtain the ID of a rule, see [ListConfigRules](https://help.aliyun.com/document_detail/169607.html).
        self.config_rule_ids = config_rule_ids
        # The page number. Pages start from page 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule_ids is not None:
            result['ConfigRuleIds'] = self.config_rule_ids

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleIds') is not None:
            self.config_rule_ids = m.get('ConfigRuleIds')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

