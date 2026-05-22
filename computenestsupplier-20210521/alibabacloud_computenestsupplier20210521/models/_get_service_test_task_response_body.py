# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class GetServiceTestTaskResponseBody(DaraModel):
    def __init__(
        self,
        execution_details: List[main_models.GetServiceTestTaskResponseBodyExecutionDetails] = None,
        request_id: str = None,
        status: str = None,
        task_name: str = None,
        task_region_id: str = None,
    ):
        # The execution details.
        self.execution_details = execution_details
        # Id of the request
        self.request_id = request_id
        # The status of the service test task. Valid values:
        # 
        # *   Running
        # *   Success
        # *    Failure
        self.status = status
        # The task name.
        self.task_name = task_name
        # The task execution region.
        self.task_region_id = task_region_id

    def validate(self):
        if self.execution_details:
            for v1 in self.execution_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExecutionDetails'] = []
        if self.execution_details is not None:
            for k1 in self.execution_details:
                result['ExecutionDetails'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_region_id is not None:
            result['TaskRegionId'] = self.task_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.execution_details = []
        if m.get('ExecutionDetails') is not None:
            for k1 in m.get('ExecutionDetails'):
                temp_model = main_models.GetServiceTestTaskResponseBodyExecutionDetails()
                self.execution_details.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskRegionId') is not None:
            self.task_region_id = m.get('TaskRegionId')

        return self

class GetServiceTestTaskResponseBodyExecutionDetails(DaraModel):
    def __init__(
        self,
        case_name: str = None,
        execution_report: str = None,
        status: str = None,
        sub_task_id: str = None,
    ):
        # The service test case name.
        self.case_name = case_name
        # The execution report
        self.execution_report = execution_report
        # The sub task status.
        self.status = status
        # The sub task id.
        self.sub_task_id = sub_task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.case_name is not None:
            result['CaseName'] = self.case_name

        if self.execution_report is not None:
            result['ExecutionReport'] = self.execution_report

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_task_id is not None:
            result['SubTaskId'] = self.sub_task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CaseName') is not None:
            self.case_name = m.get('CaseName')

        if m.get('ExecutionReport') is not None:
            self.execution_report = m.get('ExecutionReport')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubTaskId') is not None:
            self.sub_task_id = m.get('SubTaskId')

        return self

