# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCategoryTemplateRuleListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        feature_type: int = None,
        lang: str = None,
        page_size: int = None,
        risk_level_id: int = None,
        status: int = None,
    ):
        # The page number. The default value is **1**.
        self.current_page = current_page
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the request and response. The default value is **zh_cn**. Valid values:
        # 
        # - **zh_cn**: Simplified Chinese.
        # 
        # - **en_us**: US English.
        self.lang = lang
        # The number of template rules to return on each page. The default value is **10**.
        self.page_size = page_size
        # The risk level of the template rule. The value ranges from **1** to **11**. The default value is **null**. Valid values:
        # 
        # - **1**: No risk.
        # 
        # - **2**: S1.
        # 
        # - **3**: S2.
        # 
        # - **4**: S3.
        # 
        # - **5**: S4.
        # 
        # - **6**: S5.
        # 
        # - **7**: S6.
        # 
        # - **8**: S7.
        # 
        # - **9**: S8.
        # 
        # - **10**: S9.
        # 
        # - **11**: S10.
        # 
        # - **null**: All risk levels, including No risk, S1, S2, S3, S4, S5, S6, S7, S8, S9, and S10.
        self.risk_level_id = risk_level_id
        # The status of the template rule. The default value is **null**. Valid values:
        # 
        # - **0**: The rule is disabled.
        # 
        # - **1**: The rule is enabled.
        # 
        # - **null**: All rules are returned, regardless of their status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.feature_type is not None:
            result['FeatureType'] = self.feature_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('FeatureType') is not None:
            self.feature_type = m.get('FeatureType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

