# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCategoryTemplateListRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        feature_type: int = None,
        lang: str = None,
        page_size: int = None,
        usage_scenario: int = None,
    ):
        # Page number for paginated queries. Default value: 1.
        self.current_page = current_page
        # This parameter is deprecated.
        self.feature_type = feature_type
        # Set the language type for the request and response messages, default is **zh_cn**.
        # Values:
        # 
        # - **zh_cn**: Chinese (Simplified)
        # - **en_us**: English (United States)
        self.lang = lang
        # When performing a paginated query, set the number of items per page. Default value is **10**.
        self.page_size = page_size
        # API call scenario, default is **null**.
        # Values:
        # - **null**: Old version
        # - **0**: Old version
        # - **1**: New version
        self.usage_scenario = usage_scenario

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

        if self.usage_scenario is not None:
            result['UsageScenario'] = self.usage_scenario

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

        if m.get('UsageScenario') is not None:
            self.usage_scenario = m.get('UsageScenario')

        return self

