# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListSynchronizationJobsRequest(DaraModel):
    def __init__(
        self,
        direction: str = None,
        end_time: int = None,
        filters: List[main_models.ListSynchronizationJobsRequestFilters] = None,
        instance_id: str = None,
        max_results: int = None,
        next_token: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
        status: str = None,
        target_ids: List[str] = None,
        target_type: str = None,
    ):
        # The direction of the sync task. Valid values:
        # 
        # - ingress: Inbound.
        # 
        # - egress: Outbound.
        self.direction = direction
        # The synchronization end time. The value is a UNIX timestamp. Unit: milliseconds.
        self.end_time = end_time
        # The filter parameters.
        self.filters = filters
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of entries to return on each page. The maximum value is 100.
        self.max_results = max_results
        # The token to retrieve the next page of results. If no more pages exist, this parameter is not returned.
        self.next_token = next_token
        # The page number. The value starts from 1.
        self.page_number = page_number
        # The number of entries per page. The maximum value is 100.
        self.page_size = page_size
        # The synchronization start time. The value is a UNIX timestamp. Unit: milliseconds.
        self.start_time = start_time
        # The status of the sync task. Valid values:
        # 
        # - pending: The task is pending.
        # 
        # - running: The task is running.
        # 
        # - failed: The task failed.
        # 
        # - partial_success: The task is partially successful.
        # 
        # - success: The task is successful.
        self.status = status
        # A list of synchronization target IDs. For example, \\`[idp_111XXXX,idp_222XXXX]\\`.
        self.target_ids = target_ids
        # The type of the synchronization target. Valid values:
        # 
        # - identity_provider: Identity provider.
        # 
        # - application: Application.
        self.target_type = target_type

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.direction is not None:
            result['Direction'] = self.direction

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_ids is not None:
            result['TargetIds'] = self.target_ids

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ListSynchronizationJobsRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetIds') is not None:
            self.target_ids = m.get('TargetIds')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class ListSynchronizationJobsRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The name of the dynamic parameter.
        self.key = key
        # The values of the dynamic parameter.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

