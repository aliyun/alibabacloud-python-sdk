# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeImageInstancesRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        current_page: int = None,
        logical_exp: str = None,
        page_size: int = None,
        scanned: bool = None,
    ):
        # Sets the conditions for searching assets. This parameter is in JSON format and contains the following fields:
        # - **name**: The search item.
        # - **value**: The value of the search item.
        # - **logicalExp**: The logical relationship between multiple search item values. Valid values:
        #     - **OR**: The multiple search item values are in an **OR** relationship.
        #     - **AND**: The multiple search item values are in an **AND** relationship.
        # > You can call the [DescribeImageRepoCriteria](~~DescribeImageRepoCriteria~~) operation to query supported search conditions.
        self.criteria = criteria
        # The page number of the returned results to start displaying. The starting value is **1**. Default value: **1**, which indicates that page 1 is displayed.
        self.current_page = current_page
        # Sets the logical relationship between multiple search conditions. Valid values:
        # 
        # - **OR**: The multiple search conditions are in an **OR** relationship.
        # - **AND**: The multiple search conditions are in an **AND** relationship.
        self.logical_exp = logical_exp
        # The maximum number of entries to return on each page during a paged query. The default number of entries per page is 20. If the PageSize parameter is left empty, 20 entries are returned by default.
        # > We recommend that you do not leave the PageSize parameter empty.
        self.page_size = page_size
        # Indicates whether the image has been scanned. Valid values:
        # - **true**: processed.
        # - **false**: not processed.
        self.scanned = scanned

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

        if self.scanned is not None:
            result['Scanned'] = self.scanned

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

        if m.get('Scanned') is not None:
            self.scanned = m.get('Scanned')

        return self

