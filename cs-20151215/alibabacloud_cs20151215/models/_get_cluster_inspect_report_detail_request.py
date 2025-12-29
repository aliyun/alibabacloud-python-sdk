# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetClusterInspectReportDetailRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        enable_filter: bool = None,
        language: str = None,
        level: str = None,
        max_results: int = None,
        next_token: str = None,
        target_type: str = None,
    ):
        # The category of the inspection item. Valid values:
        # 
        # *   security: Security compliance
        # *   performance: Performance efficiency
        # *   stability: Business stability
        # *   limitation: Service limits
        # *   cost: Cost optimization
        self.category = category
        # Inspection results filtering. If this parameter is set to true, only abnormal inspection items are returned.
        self.enable_filter = enable_filter
        # The query language.
        # 
        # *   zh_CN
        # *   en_US
        self.language = language
        # The level of the inspection item. Valid values:
        # 
        # *   advice: Suggestions
        # *   warning: Low severity
        # *   error: Medium severity
        # *   critical: High severity
        self.level = level
        # The maximum number of entries per page. Maximum value: 50.
        self.max_results = max_results
        # The token that is used to display the returned tags on multiple pages.
        self.next_token = next_token
        # The type of the inspection object. Only items that meet the targetType parameter are returned.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.enable_filter is not None:
            result['enableFilter'] = self.enable_filter

        if self.language is not None:
            result['language'] = self.language

        if self.level is not None:
            result['level'] = self.level

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.target_type is not None:
            result['targetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('enableFilter') is not None:
            self.enable_filter = m.get('enableFilter')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')

        return self

