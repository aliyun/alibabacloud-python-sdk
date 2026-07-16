# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDataAssetsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        lang: str = None,
        name: str = None,
        page_size: int = None,
        range_id: int = None,
        risk_levels: str = None,
        rule_id: int = None,
    ):
        # The page number to return.
        self.current_page = current_page
        # The language of the request and response. The default value is **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Chinese (Simplified)
        # 
        # - **en_us**: English (US)
        self.lang = lang
        # The keyword for a fuzzy search of data assets.
        self.name = name
        # The number of entries to return on each page. The default value is **20**.
        self.page_size = page_size
        # The type of data asset to query. Valid values:
        # 
        # - **1**: MaxCompute project
        # 
        # - **2**: MaxCompute table
        # 
        # - **3**: MaxCompute package
        # 
        # - **11**: AnalyticDB for MySQL database
        # 
        # - **12**: AnalyticDB for MySQL table
        # 
        # - **21**: OSS bucket
        # 
        # - **22**: OSS object
        # 
        # - **31**: Tablestore instance
        # 
        # - **32**: Tablestore table
        # 
        # - **51**: RDS database
        # 
        # - **52**: RDS table
        # 
        # - **61**: Self-managed database on an ECS instance
        # 
        # - **62**: Self-managed table on an ECS instance
        # 
        # - **71**: DRDS database
        # 
        # - **72**: DRDS table
        # 
        # - **81**: PolarDB database
        # 
        # - **82**: PolarDB table
        # 
        # - **91**: GPDB database
        # 
        # - **92**: GPDB table
        self.range_id = range_id
        # The risk levels of the data assets to query. Separate multiple risk levels with commas (,).
        # 
        # - **2**: S1, low risk level
        # 
        # - **3**: S2, medium risk level
        # 
        # - **4**: S3, high risk level
        # 
        # - **5**: S4, highest risk level
        self.risk_levels = risk_levels
        # The ID of the sensitive data detection rule that the data asset matches.
        # 
        # > To find data assets based on the sensitive data detection rules they match, call the [DescribeRules](~~DescribeRules~~) operation to get the rule IDs.
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.name is not None:
            result['Name'] = self.name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.range_id is not None:
            result['RangeId'] = self.range_id

        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RangeId') is not None:
            self.range_id = m.get('RangeId')

        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        return self

