# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListDoctorComputeSummaryRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        component_types: List[str] = None,
        date_time: str = None,
        max_results: int = None,
        next_token: str = None,
        order_by: str = None,
        order_type: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The resource types, which are used to filter query results. Valid values:
        # 
        # *   engine: filters results by engine.
        # *   queue: filters results by queue.
        # *   cluster: displays the results at the cluster level.
        # 
        # If you do not specify this parameter, the information at the cluster level is displayed by default. Currently, only one resource type is supported. If you specify multiple resource types, the first resource type is used by default.
        self.component_types = component_types
        # Specify the date in the ISO 8601 standard. For example, 2023-01-01 represents January 1, 2023.
        # 
        # This parameter is required.
        self.date_time = date_time
        # The maximum number of entries to return on each page.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results.
        self.next_token = next_token
        # The basis on which you want to sort the query results. Valid values:
        # 
        # 1.  vcoreSeconds: the total CPU consumption over time in seconds.
        # 2.  memSeconds: the total memory consumption over time in seconds.
        # 3.  vcoreUtilization: the average CPU utilization. The meaning is the same as the %CPU parameter in the output of the top command in Linux.
        # 4.  memUtilization: the average memory usage.
        # 5.  vcoreSecondsDayGrowthRatio: the day-to-day growth rate of the total CPU consumption over time in seconds.
        # 6.  memSecondsDayGrowthRatio: the day-to-day growth rate of the total memory consumption over time in seconds.
        # 7.  readSize: the total amount of data read from the file system.
        # 8.  writeSize: the total amount of data written to the file system.
        # 9.  healthyJobCount: the total number of healthy jobs.
        # 10. subHealthyJobCount: the total number of sub-healthy jobs.
        # 11. unhealthyJobCount: the total number of unhealthy jobs.
        # 12. needAttentionJobCount: the total number of jobs that require attention.
        # 13. score: the score for jobs.
        # 14. scoreDayGrowthRatio: the day-to-day growth rate of the score for jobs.
        self.order_by = order_by
        # The order in which you want to sort the query results. Valid values:
        # 
        # *   ASC: in ascending order.
        # *   DESC: in descending order.
        self.order_type = order_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.component_types is not None:
            result['ComponentTypes'] = self.component_types

        if self.date_time is not None:
            result['DateTime'] = self.date_time

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComponentTypes') is not None:
            self.component_types = m.get('ComponentTypes')

        if m.get('DateTime') is not None:
            self.date_time = m.get('DateTime')

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

        return self

