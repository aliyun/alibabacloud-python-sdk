# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class ListTasksRequest(DaraModel):
    def __init__(
        self,
        end_time_range: main_models.TimeRange = None,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        request_definition: bool = None,
        sort: str = None,
        start_time_range: main_models.TimeRange = None,
        status: str = None,
        tag_selector: str = None,
        task_types: List[str] = None,
    ):
        # The task end time range. You can specify this parameter to filter tasks that end within the specified range.
        self.end_time_range = end_time_range
        # The maximum number of results to return. Valid value range: (0, 100]. Default value: 100.
        self.max_results = max_results
        # The pagination token.
        # 
        # The pagination token is used in the next request to retrieve a new page of results if the total number of results exceeds the value of the MaxResults parameter. The next call to the operation returns results lexicographically after the NextToken parameter value.
        # 
        # >  Leave this parameter empty in your first call to the operation.
        self.next_token = next_token
        # The sort order. Valid values:
        # 
        # *   asc: in ascending order. This is the default value.
        # *   desc: in descending order.
        self.order = order
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # Specifies whether to return request parameters in the initial request to create the task. Default value: False.
        self.request_definition = request_definition
        # The field used to sort the results by. Valid values:
        # 
        # *   TaskId: sorts the results by task ID. This is the default sort field.
        # *   StartTime: sorts the results by task start time.
        # *   StartTime: sorts the results by task end time.
        self.sort = sort
        # The task start time range. You can specify this parameter to filter tasks that start within the specified range.
        self.start_time_range = start_time_range
        # The task status. Valid values:
        # 
        # *   Running: The task is running.
        # *   Succeeded: The task is successful.
        # *   Failed: The task failed.
        self.status = status
        # The custom tags of tasks.
        self.tag_selector = tag_selector
        # The task types.
        self.task_types = task_types

    def validate(self):
        if self.end_time_range:
            self.end_time_range.validate()
        if self.start_time_range:
            self.start_time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time_range is not None:
            result['EndTimeRange'] = self.end_time_range.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_definition is not None:
            result['RequestDefinition'] = self.request_definition

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.start_time_range is not None:
            result['StartTimeRange'] = self.start_time_range.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector

        if self.task_types is not None:
            result['TaskTypes'] = self.task_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTimeRange') is not None:
            temp_model = main_models.TimeRange()
            self.end_time_range = temp_model.from_map(m.get('EndTimeRange'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestDefinition') is not None:
            self.request_definition = m.get('RequestDefinition')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('StartTimeRange') is not None:
            temp_model = main_models.TimeRange()
            self.start_time_range = temp_model.from_map(m.get('StartTimeRange'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')

        if m.get('TaskTypes') is not None:
            self.task_types = m.get('TaskTypes')

        return self

