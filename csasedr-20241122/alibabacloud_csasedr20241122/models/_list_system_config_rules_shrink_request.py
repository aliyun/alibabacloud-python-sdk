# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSystemConfigRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        aggregation_ids_shrink: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        rule_name: str = None,
        rule_types_shrink: str = None,
        selection_key: str = None,
        system_type: int = None,
    ):
        # The list of system rule category IDs.
        self.aggregation_ids_shrink = aggregation_ids_shrink
        # The current page number.
        self.current_page = current_page
        # The language used for the rule name and description. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries to return on each page during paging in a paged query.
        self.page_size = page_size
        # The rule name.
        self.rule_name = rule_name
        # The list of rule types for filtering.
        self.rule_types_shrink = rule_types_shrink
        # The key for the switch configuration of rules associated with a policy. Use the SelectionKey saved for the same policy.
        self.selection_key = selection_key
        # The system platform identifier used for filtering. Valid values:
        # - **1**: Linux.
        # - **2**: Windows.
        # - **3**: Mac.
        self.system_type = system_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregation_ids_shrink is not None:
            result['AggregationIds'] = self.aggregation_ids_shrink

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_types_shrink is not None:
            result['RuleTypes'] = self.rule_types_shrink

        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationIds') is not None:
            self.aggregation_ids_shrink = m.get('AggregationIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleTypes') is not None:
            self.rule_types_shrink = m.get('RuleTypes')

        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        return self

