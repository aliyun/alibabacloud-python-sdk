# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageBuildRiskListRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        criteria_type: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        risk_level: str = None,
    ):
        # The **rule name** or **type name** of the risk. You can call the [DescribeImageBuildRiskList](~~~~) operation to obtain the name. Optional parameters:
        # 
        # *   If **CriteriaType** is set to **RiskKeyName**, you must specify a **rule name** for this parameter.
        # *   If **CriteriaType** is set to**RiskClassName**, you must specify a **type name** for this parameter.
        self.criteria = criteria
        # The query type.of the risk. Valid values:
        # 
        # *   **RiskKeyName**: the rule name of the risk
        # *   **RiskClassName**: the type name of the risk
        self.criteria_type = criteria_type
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries per page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The risk level. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.criteria_type is not None:
            result['CriteriaType'] = self.criteria_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CriteriaType') is not None:
            self.criteria_type = m.get('CriteriaType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

