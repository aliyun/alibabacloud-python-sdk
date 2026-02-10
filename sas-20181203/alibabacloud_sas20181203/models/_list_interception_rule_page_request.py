# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInterceptionRulePageRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        criteria: str = None,
        criteria_type: str = None,
        current_page: int = None,
        page_size: int = None,
    ):
        # The ID of the container cluster.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The query condition.
        self.criteria = criteria
        # The type of the query condition. Valid values:
        # 
        # *   **ID**
        # *   **RULE_NAME**
        # *   **SRC_TARGET**
        # *   **DST_TARGET**
        # *   **DST_PORT**
        # *   **RULE_SWITCH**
        # *   **INTERCEPTOR_TYPE**
        self.criteria_type = criteria_type
        # The number of the page to return.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The number of entries to return on each page.
        # 
        # This parameter is required.
        self.page_size = page_size

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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

