# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nis20211216 import models as main_models
from darabonba.model import DaraModel

class ListNisInspectionTasksResponseBody(DaraModel):
    def __init__(
        self,
        inspection_task_list: List[main_models.ListNisInspectionTasksResponseBodyInspectionTaskList] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of network inspection tasks.
        self.inspection_task_list = inspection_task_list
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The token to retrieve the next page of results. If the value of this parameter is not empty, it indicates that there are more results to retrieve. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.inspection_task_list:
            for v1 in self.inspection_task_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InspectionTaskList'] = []
        if self.inspection_task_list is not None:
            for k1 in self.inspection_task_list:
                result['InspectionTaskList'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_task_list = []
        if m.get('InspectionTaskList') is not None:
            for k1 in m.get('InspectionTaskList'):
                temp_model = main_models.ListNisInspectionTasksResponseBodyInspectionTaskList()
                self.inspection_task_list.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNisInspectionTasksResponseBodyInspectionTaskList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        inspection_name: str = None,
        inspection_project: str = None,
        inspection_task_id: str = None,
        last_update_report_id: str = None,
        status: str = None,
    ):
        # The time when the task was created.
        self.create_time = create_time
        # The name of the network inspection task.
        self.inspection_name = inspection_name
        # The type of inspection solution that the network inspection task uses. Valid values: basic and customized.
        self.inspection_project = inspection_project
        # The ID of the network inspection task.
        self.inspection_task_id = inspection_task_id
        # The ID of the latest report.
        self.last_update_report_id = last_update_report_id
        # The running status of the task. Valid values:
        # 
        # Creating: The task is being created.
        # 
        # - Active
        # 
        # - Running
        # 
        # - Inactive
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.inspection_name is not None:
            result['InspectionName'] = self.inspection_name

        if self.inspection_project is not None:
            result['InspectionProject'] = self.inspection_project

        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id

        if self.last_update_report_id is not None:
            result['LastUpdateReportId'] = self.last_update_report_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('InspectionName') is not None:
            self.inspection_name = m.get('InspectionName')

        if m.get('InspectionProject') is not None:
            self.inspection_project = m.get('InspectionProject')

        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')

        if m.get('LastUpdateReportId') is not None:
            self.last_update_report_id = m.get('LastUpdateReportId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

