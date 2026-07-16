# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeImageBaselineCheckSummaryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        criteria: str = None,
        criteria_type: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        risk_level: str = None,
        scan_range: List[str] = None,
    ):
        # The ID of the container cluster to query.
        # > You can call the [DescribeGroupedContainerInstances](~~DescribeGroupedContainerInstances~~) operation to obtain this parameter.
        self.cluster_id = cluster_id
        # The query condition of the baseline.
        self.criteria = criteria
        # The query type of the baselines to query. Valid values:
        # 
        # - **BaselineNameAlias**: baseline name
        # 
        # - **BaselineClassAlias**: baseline category.
        self.criteria_type = criteria_type
        # The page number to display from the returned results. Minimum value: **1**. Default value: **1**, which indicates that the first page is displayed.
        self.current_page = current_page
        # The language type for requests and responses. Default value: **zh**. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries per page in a paged query. Default value: **20**.
        self.page_size = page_size
        # The risk level of the baselines to query. Separate multiple levels with commas (,). Valid values:
        # 
        # - **high**: high risk
        # 
        # - **medium**: medium risk
        # 
        # - **low**: low risk.
        self.risk_level = risk_level
        # The collection of scan ranges.
        self.scan_range = scan_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

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

        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

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

        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        return self

