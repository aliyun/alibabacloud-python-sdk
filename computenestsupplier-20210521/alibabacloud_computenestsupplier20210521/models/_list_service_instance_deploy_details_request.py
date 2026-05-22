# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceDeployDetailsRequest(DaraModel):
    def __init__(
        self,
        cycle_time_zone: str = None,
        cycle_type: str = None,
        dimension: List[str] = None,
        end_time: str = None,
        filter: List[main_models.ListServiceInstanceDeployDetailsRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The time zone.
        # 
        # Reference Format: "+08:00"
        # 
        # Valid Range: "-12:59" to "+13:00"
        self.cycle_time_zone = cycle_time_zone
        # Determines the time period over which data is aggregated. If no aggregation dimension is specified, the query defaults to providing detailed, unaggregated results.
        # 
        # Optional Values:
        # 
        # - Year
        # - Month
        # - Day
        # - All
        self.cycle_type = cycle_type
        # The dimension names. (Equivalent to SQL\\"s GROUP BY Clause)
        # Optional Values:
        # 
        # - UserId
        # - ServiceId
        # - ServiceVersion
        # - ServiceInstanceId
        # - DeploySucceeded
        # - ErrorType
        # - ErrorCode
        self.dimension = dimension
        # The end of the time range to query. The end time must be later than the start time. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. The time must be in UTC.
        self.end_time = end_time
        # The filter.
        self.filter = filter
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm*Z format. The time must be in UTC.
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
        if self.cycle_time_zone is not None:
            result['CycleTimeZone'] = self.cycle_time_zone

        if self.cycle_type is not None:
            result['CycleType'] = self.cycle_type

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleTimeZone') is not None:
            self.cycle_time_zone = m.get('CycleTimeZone')

        if m.get('CycleType') is not None:
            self.cycle_type = m.get('CycleType')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListServiceInstanceDeployDetailsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListServiceInstanceDeployDetailsRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # Filter Value Names (Equivalent to SQL\\"s WHERE Clause)
        # 
        # Available Options:
        # 
        # - UserId
        # - ServiceId
        # - ServiceVersion
        # - ServiceInstanceId
        # - DeploySucceeded (Accepts True or False and case-insensitive)
        # - ErrorType
        # - ErrorCode
        self.name = name
        # A value of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

