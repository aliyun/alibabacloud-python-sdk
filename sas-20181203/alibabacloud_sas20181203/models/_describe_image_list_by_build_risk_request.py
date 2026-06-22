# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageListByBuildRiskRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        criteria_type: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        risk_key: str = None,
        risk_level: str = None,
        status: int = None,
    ):
        # The value of the condition parameter.
        self.criteria = criteria
        # The name of the condition parameter. Valid values:
        # - **RepoNamespace**: namespace.
        # - **RepoName**: repository name.
        self.criteria_type = criteria_type
        # The page number of the current page in paging query. Default value: **1**.
        self.current_page = current_page
        # The language of the content within the request and response. Valid values:
        # - **zh**: Chinese
        # - **en**: English.
        self.lang = lang
        # The maximum number of entries per page in paging query. Default value: 20. If you leave this parameter empty, 20 entries are returned.
        # > Do not leave PageSize empty.
        self.page_size = page_size
        # The key of the build risk rule. You can call the [DescribeImageBuildRiskList](~~~~) operation to obtain the RiskKey.
        self.risk_key = risk_key
        # The risk level. Valid values:
        # - **high**
        # - **medium**
        # - **low**.
        self.risk_level = risk_level
        # The status of the alert event to query. Valid values:
        # - **0**: Unhandled.
        # - **1**: Ignored.
        # - **2**: False positive.
        self.status = status

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

        if self.risk_key is not None:
            result['RiskKey'] = self.risk_key

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.status is not None:
            result['Status'] = self.status

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

        if m.get('RiskKey') is not None:
            self.risk_key = m.get('RiskKey')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

