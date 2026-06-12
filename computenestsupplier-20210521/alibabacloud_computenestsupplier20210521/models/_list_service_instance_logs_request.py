# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceInstanceLogsRequest(DaraModel):
    def __init__(
        self,
        filter: List[main_models.ListServiceInstanceLogsRequestFilter] = None,
        log_source: str = None,
        logstore: str = None,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        service_instance_id: str = None,
        sort_order: str = None,
    ):
        # The filters.
        self.filter = filter
        # The source of the logs. Valid values:
        # 
        # - application: Logs from the application.
        # 
        # - computeNest: Logs from Compute Nest.
        # 
        # - ros: Logs from Resource Orchestration Service (ROS).
        self.log_source = log_source
        # The name of the Simple Log Service Logstore.
        self.logstore = logstore
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The token that specifies the next page of results to return. Set this parameter to the NextToken value from a previous response to retrieve the next page of results.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The service instance ID.
        # 
        # This parameter is required.
        self.service_instance_id = service_instance_id
        # The sort order. Valid values:
        # 
        # - **Ascending**: Ascending order.
        # 
        # - **Descending** (default): Descending order.
        self.sort_order = sort_order

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
        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

        if self.log_source is not None:
            result['LogSource'] = self.log_source

        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_instance_id is not None:
            result['ServiceInstanceId'] = self.service_instance_id

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.ListServiceInstanceLogsRequestFilter()
                self.filter.append(temp_model.from_map(k1))

        if m.get('LogSource') is not None:
            self.log_source = m.get('LogSource')

        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceInstanceId') is not None:
            self.service_instance_id = m.get('ServiceInstanceId')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        return self

class ListServiceInstanceLogsRequestFilter(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: List[str] = None,
    ):
        # The name of the filter condition.
        # 
        # Valid values:
        # 
        # - StartTime
        # 
        # - EndTime
        # 
        # - ApplicationGroupName
        # 
        # - ResourceName
        # 
        # - EventName
        self.name = name
        # The values for the filter condition. You can specify up to 10 values.
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

