# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAlertsRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        gmt_end: str = None,
        gmt_start: str = None,
        page_no: int = None,
        page_size: int = None,
        resource_arn: str = None,
        sort_by: str = None,
        sort_by_modified_time: str = None,
    ):
        # The alert type.
        self.category = category
        # The end of the time range to query.
        self.gmt_end = gmt_end
        # The beginning of the time range to query.
        self.gmt_start = gmt_start
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The ARN of the source or program.
        # 
        # This parameter is required.
        self.resource_arn = resource_arn
        # The sorting order. By default, the query results are sorted by creation time in descending order. Valid values: asc and desc.
        self.sort_by = sort_by
        # The sorting order by modification time. Valid values: asc and desc.
        self.sort_by_modified_time = sort_by_modified_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.gmt_end is not None:
            result['GmtEnd'] = self.gmt_end

        if self.gmt_start is not None:
            result['GmtStart'] = self.gmt_start

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.sort_by_modified_time is not None:
            result['SortByModifiedTime'] = self.sort_by_modified_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('GmtEnd') is not None:
            self.gmt_end = m.get('GmtEnd')

        if m.get('GmtStart') is not None:
            self.gmt_start = m.get('GmtStart')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('SortByModifiedTime') is not None:
            self.sort_by_modified_time = m.get('SortByModifiedTime')

        return self

