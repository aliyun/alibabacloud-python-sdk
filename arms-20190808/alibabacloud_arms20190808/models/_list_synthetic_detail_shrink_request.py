# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSyntheticDetailShrinkRequest(DaraModel):
    def __init__(
        self,
        advanced_filters_shrink: str = None,
        category: str = None,
        detail: str = None,
        end_time: int = None,
        exact_filters_shrink: str = None,
        filters_shrink: str = None,
        order: str = None,
        order_by: str = None,
        page: int = None,
        page_size: int = None,
        region_id: str = None,
        start_time: int = None,
        synthetic_type: int = None,
    ):
        # An array of filter conditions. This parameter is required.
        # 
        # *   To query the list of synthetic test results, set this parameter in the following format: [{"Key":"taskType","OpType":"in","Value":[Task type]}].
        # *   To query the result details of a synthetic monitoring task, set this parameter in the following format: [{"Key":"dataId","OpType":"eq","Value":"dataId"}]. dataId is returned when you query the list of synthetic test results.
        self.advanced_filters_shrink = advanced_filters_shrink
        # The type of the results. Set the value to SYNTHETIC.
        self.category = category
        # The type of the list that contains the results. This parameter is required. Valid values:
        # 
        # *   ICMP_LIST
        # *   TCP_LIST
        # *   DNS_LIST
        # *   HTTP_LIST
        # *   WEBSITE_LIST
        # *   DOWNLOAD_LIST
        # *   ALL
        self.detail = detail
        # The timestamp of the end time of the query. Unit: milliseconds.
        self.end_time = end_time
        # A reserved field.
        self.exact_filters_shrink = exact_filters_shrink
        # The filter condition. This parameter is required.
        # 
        # *   To query the result of a synthetic monitoring task, set this parameter in the following format: {"taskId":"${taskId}"}.
        # *   To query the result details of a synthetic monitoring task, set this parameter in the following format: {"taskId":"${taskId}","dataId":"${dataId}"}.
        self.filters_shrink = filters_shrink
        # The order in which results are sorted. Valid values:
        # 
        # - `ASC`: ascending order
        # - `DESC`: descending order
        self.order = order
        # The field based on which results are sorted. Set the value to timestamp.
        self.order_by = order_by
        # The page number. Pages start from page 1.
        self.page = page
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the region. Set the value to cn-hangzhou.
        self.region_id = region_id
        # The timestamp of the start time of the query. Unit: milliseconds.
        self.start_time = start_time
        # The type of the synthetic test. Valid values: 1 and 2. 1 represents an immediate test, and 2 represents a scheduled test.
        self.synthetic_type = synthetic_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_filters_shrink is not None:
            result['AdvancedFilters'] = self.advanced_filters_shrink

        if self.category is not None:
            result['Category'] = self.category

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.exact_filters_shrink is not None:
            result['ExactFilters'] = self.exact_filters_shrink

        if self.filters_shrink is not None:
            result['Filters'] = self.filters_shrink

        if self.order is not None:
            result['Order'] = self.order

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.synthetic_type is not None:
            result['SyntheticType'] = self.synthetic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedFilters') is not None:
            self.advanced_filters_shrink = m.get('AdvancedFilters')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ExactFilters') is not None:
            self.exact_filters_shrink = m.get('ExactFilters')

        if m.get('Filters') is not None:
            self.filters_shrink = m.get('Filters')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SyntheticType') is not None:
            self.synthetic_type = m.get('SyntheticType')

        return self

