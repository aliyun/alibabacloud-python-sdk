# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeContainerInstancesRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        current_page: int = None,
        logical_exp: str = None,
        page_size: int = None,
    ):
        # The search conditions that are used to filter containers. The value of this parameter is in the JSON format and is case-sensitive. The value contains the following fields:
        # 
        # *   **name**: the search condition.
        # 
        # *   **name**: the value of the search condition.
        # 
        # *   **logicalExp**: the logical relationship among multiple search conditions. Valid values:
        # 
        #     *   **OR**: Search conditions are evaluated by using a logical **OR**.
        #     *   **AND**: Search conditions are evaluated by using a logical **AND**.
        # 
        # > You can use search conditions such as the container ID, cluster ID, cluster name, cluster type, risk level, and region. You can call the [DescribeContainerCriteria](~~DescribeContainerCriteria~~) operation to query the supported search conditions.
        self.criteria = criteria
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The logical operator that you want to use to evaluate multiple search conditions. Valid values:
        # 
        # *   **OR**: Search conditions are evaluated by using a logical **OR**.
        # *   **AND**: Search conditions are evaluated by using a logical **AND**.
        self.logical_exp = logical_exp
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.logical_exp is not None:
            result['LogicalExp'] = self.logical_exp

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('LogicalExp') is not None:
            self.logical_exp = m.get('LogicalExp')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

