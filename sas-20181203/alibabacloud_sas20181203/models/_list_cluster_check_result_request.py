# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListClusterCheckResultRequest(DaraModel):
    def __init__(
        self,
        check_key: str = None,
        cluster_id: str = None,
        current_page: int = None,
        lang: str = None,
        page_size: int = None,
        risk_levels: List[str] = None,
        sort_type: str = None,
        statuses: List[str] = None,
    ):
        # Fuzzy search key for check items.
        self.check_key = check_key
        # Cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # Page number for the current page in a paginated query. The default value is **1**.
        self.current_page = current_page
        # Language type for requests and responses. The default value is **zh**. Values:
        # - **zh**: Chinese
        # - **en**: English
        # 
        # This parameter is required.
        self.lang = lang
        # Number of records to display per page when performing a paginated query. The default value is **20**, indicating 20 records per page.
        self.page_size = page_size
        # List of risk levels.
        self.risk_levels = risk_levels
        # Custom sorting type. Values:
        # 
        # - **RISK_LEVEL**: Risk level.
        # - **STATUS**: Check item status.
        self.sort_type = sort_type
        # List of check item statuses.
        self.statuses = statuses

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_key is not None:
            result['CheckKey'] = self.check_key

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels

        if self.sort_type is not None:
            result['SortType'] = self.sort_type

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckKey') is not None:
            self.check_key = m.get('CheckKey')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')

        if m.get('SortType') is not None:
            self.sort_type = m.get('SortType')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        return self

