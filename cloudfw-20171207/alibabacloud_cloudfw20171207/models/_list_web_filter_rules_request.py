# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWebFilterRulesRequest(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        rule_action: str = None,
        web_filter_rule_id: str = None,
        web_filter_template_id: str = None,
    ):
        # The page number. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. The value must be greater than or equal to 1. Default value: 10.
        self.page_size = page_size
        # The rule action for exact matching. Valid values:
        # - **Allow**: Allows the request.
        # - **Alert**: Monitors the request.
        # - **Deny**: Blocks the request.
        self.rule_action = rule_action
        # The ID of the web filtering rule for exact matching.
        self.web_filter_rule_id = web_filter_rule_id
        # The ID of the web filtering template for exact matching.
        self.web_filter_template_id = web_filter_template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.web_filter_rule_id is not None:
            result['WebFilterRuleId'] = self.web_filter_rule_id

        if self.web_filter_template_id is not None:
            result['WebFilterTemplateId'] = self.web_filter_template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('WebFilterRuleId') is not None:
            self.web_filter_rule_id = m.get('WebFilterRuleId')

        if m.get('WebFilterTemplateId') is not None:
            self.web_filter_template_id = m.get('WebFilterTemplateId')

        return self

