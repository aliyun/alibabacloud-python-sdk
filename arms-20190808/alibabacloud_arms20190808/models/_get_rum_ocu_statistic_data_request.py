# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class GetRumOcuStatisticDataRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        filter: List[main_models.GetRumOcuStatisticDataRequestFilter] = None,
        group: List[str] = None,
        page: int = None,
        page_size: int = None,
        query_type: str = None,
        region_id: str = None,
        start_time: int = None,
    ):
        # The end of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The filter condition. Three types of filter conditions are provided:
        # 
        # *   Application name: pid (Note that the application name is displayed, but the application ID is actually specified)
        # *   Application type: siteType
        # *   Data type: dataType
        self.filter = filter
        # The grouping fields. Valid values:
        # 
        # *   siteType: The total number of OCUs is grouped by application type.
        # *   dataType: The total number of OCUs is grouped by data type.
        # *   pid: The total number of OCUs is grouped by application ID.
        # *   appName: The total number of OCUs is grouped by application name.
        # *   startTime: The total number of OCUs is grouped by start time.
        self.group = group
        # The page number.
        # 
        # This parameter is required.
        self.page = page
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The type of the query. To query non-time series data, set the value to INSTANT. To query time series data, set the value to TIME_SERIES.
        self.query_type = query_type
        # The region ID.
        self.region_id = region_id
        # The beginning of the time range to query. Unit: milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.group is not None:
            result['Group'] = self.group

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.GetRumOcuStatisticDataRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetRumOcuStatisticDataRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        op_type: str = None,
        value: Any = None,
    ):
        # The key of the filter condition. Three types of filter conditions are provided:
        # 
        # *   Application name: pid (Note that the application name is displayed, but the application ID is actually specified)
        # *   Application type: siteType
        # *   Data type: dataType
        self.key = key
        # The type of the operator. Valid value: in.
        self.op_type = op_type
        # The value of the filter condition. The value is a JSON array of strings.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

