# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImageBaselineCheckResultRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        criteria_type: str = None,
        current_page: int = None,
        image_uuid: str = None,
        lang: str = None,
        page_size: int = None,
        risk_level: str = None,
        scan_range: List[str] = None,
    ):
        # The search condition for the image baseline.
        self.criteria = criteria
        # The type of the search condition. Valid values:
        # 
        # *   **BaselineNameAlias**: baseline name
        # *   **BaselineClassAlias**: baseline category
        self.criteria_type = criteria_type
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The UUID of the image.
        # 
        # This parameter is required.
        self.image_uuid = image_uuid
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size
        # The severity of the image baseline that you want to query. Separate multiple severities with commas (,). By default, all valid values are used. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.risk_level = risk_level
        # The types of the assets that you want to scan.
        self.scan_range = scan_range

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

        if self.image_uuid is not None:
            result['ImageUuid'] = self.image_uuid

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CriteriaType') is not None:
            self.criteria_type = m.get('CriteriaType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageUuid') is not None:
            self.image_uuid = m.get('ImageUuid')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        return self

