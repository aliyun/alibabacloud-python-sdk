# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCustomMetricListRequest(DaraModel):
    def __init__(
        self,
        dimension: str = None,
        group_id: str = None,
        md_5: str = None,
        metric_name: str = None,
        page_number: str = None,
        page_size: str = None,
        region_id: str = None,
    ):
        # The dimensions based on which the resources are queried.
        self.dimension = dimension
        # The ID of the application group.
        # 
        # For information about how to query the IDs of application groups, see [DescribeMonitorGroups](https://help.aliyun.com/document_detail/115032.html).
        self.group_id = group_id
        # The MD5 value of the HTTP request body. The MD5 value is a 128-bit hash value used to verify the uniqueness of the reported monitoring data.
        self.md_5 = md_5
        # The name of the custom metric.
        self.metric_name = metric_name
        # The page number.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Pages start from page 1. Default value: 10.
        self.page_size = page_size
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

