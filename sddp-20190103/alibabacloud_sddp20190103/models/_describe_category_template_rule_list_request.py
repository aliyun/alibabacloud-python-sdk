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
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # This parameter is deprecated.
        self.feature_type = feature_type
        # The language of the content within the request and response. Default value: **zh_cn**. Valid values:
        # 
        # *   **zh_cn**: Simplified Chinese
        # *   **en_us**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size
        # The sensitivity level of the data that is not compliant with the rule. Valid values: **1** to **11**. Default value: **null**.
        # 
        # *   **1**: No sensitive data is detected.
        # *   **2**: specifies the S1 sensitivity level.
        # *   **3**: specifies the S2 sensitivity level.
        # *   **4**: specifies the S3 sensitivity level.
        # *   **5**: specifies the S4 sensitivity level.
        # *   **6**: specifies the S5 sensitivity level.
        # *   **7**: specifies the S6 sensitivity level.
        # *   **8**: specifies the S7 sensitivity level.
        # *   **9**: specifies the S8 sensitivity level.
        # *   **10**: specifies the S9 sensitivity level.
        # *   **11**: specifies the S10 sensitivity level.
        # *   **null**: specifies all preceding sensitivity levels.
        self.risk_level_id = risk_level_id
        # The status of the rule. Default value: **null**. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        # *   **null**: all states
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

