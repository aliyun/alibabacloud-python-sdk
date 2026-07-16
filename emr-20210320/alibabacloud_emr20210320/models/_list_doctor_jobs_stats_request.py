# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorJobsStatsRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        end_range: main_models.ListDoctorJobsStatsRequestEndRange = None,
        group_by: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        order_type: str = None,
        region_id: str = None,
        start_range: main_models.ListDoctorJobsStatsRequestStartRange = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The range of end time. You can filter jobs whose end time falls within the specified time range.
        self.end_range = end_range
        # The fields that are used for grouping data.
        # 
        # Currently, only the first value is used for grouping data. Combinations of multiple values will be supported in the future.
        self.group_by = group_by
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The field that you use to sort the query results. Valid values:
        # 
        # *   vcoreSeconds: the aggregated number of vCPUs that are allocated to the job multiplied by the number of seconds the job has been running
        # *   memSeconds: the aggregated amount of memory that is allocated to the job multiplied by the number of seconds the job has been running
        self.order_by = order_by
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   ASC: in ascending order
        # *   DESC: in descending order
        self.order_type = order_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The range of start time. You can filter jobs whose start time falls within the specified time range.
        self.start_range = start_range

    def validate(self):
        if self.end_range:
            self.end_range.validate()
        if self.start_range:
            self.start_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_range is not None:
            result['EndRange'] = self.end_range.to_map()

        if self.group_by is not None:
            result['GroupBy'] = self.group_by

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_range is not None:
            result['StartRange'] = self.start_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndRange') is not None:
            temp_model = main_models.ListDoctorJobsStatsRequestEndRange()
            self.end_range = temp_model.from_map(m.get('EndRange'))

        if m.get('GroupBy') is not None:
            self.group_by = m.get('GroupBy')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartRange') is not None:
            temp_model = main_models.ListDoctorJobsStatsRequestStartRange()
            self.start_range = temp_model.from_map(m.get('StartRange'))

        return self

class ListDoctorJobsStatsRequestStartRange(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end of the time range during which jobs were submitted. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: milliseconds.
        self.end_time = end_time
        # The beginning of the time range during which jobs were submitted. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. Unit: milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListDoctorJobsStatsRequestEndRange(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # The end of the time range during which jobs ended. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.end_time = end_time
        # The beginning of the time range during which jobs ended. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

