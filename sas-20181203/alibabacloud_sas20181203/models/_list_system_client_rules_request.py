# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSystemClientRulesRequest(DaraModel):
    def __init__(
        self,
        aggregation_ids: List[int] = None,
        current_page: int = None,
        is_container: int = None,
        lang: str = None,
        page_size: int = None,
        rule_name: str = None,
        rule_types: List[int] = None,
        system_type: int = None,
    ):
        # The IDs of the aggregation types for rules.
        self.aggregation_ids = aggregation_ids
        # The number of the page to return.
        # 
        # This parameter is required.
        self.current_page = current_page
        # Specifies whether to query only container images. Valid values:
        # 
        # *   **0**: no
        # *   **1**: yes
        self.is_container = is_container
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The name of the system defense rule.
        self.rule_name = rule_name
        # The types of the system defense rules.
        self.rule_types = rule_types
        # The type of the OS. Valid values:
        # 
        # *   **2**: Windows
        # *   **1**: Linux
        # *   **0**: all types
        self.system_type = system_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aggregation_ids is not None:
            result['AggregationIds'] = self.aggregation_ids

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.is_container is not None:
            result['IsContainer'] = self.is_container

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_types is not None:
            result['RuleTypes'] = self.rule_types

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregationIds') is not None:
            self.aggregation_ids = m.get('AggregationIds')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IsContainer') is not None:
            self.is_container = m.get('IsContainer')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleTypes') is not None:
            self.rule_types = m.get('RuleTypes')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        return self

