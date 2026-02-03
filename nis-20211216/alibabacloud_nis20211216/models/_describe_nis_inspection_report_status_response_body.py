# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeNisInspectionReportStatusResponseBody(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        inspection_project: str = None,
        inspection_report_id: str = None,
        inspection_task_id: str = None,
        inspection_task_name: str = None,
        request_id: str = None,
        start_time: str = None,
        status: str = None,
    ):
        self.end_time = end_time
        self.inspection_project = inspection_project
        self.inspection_report_id = inspection_report_id
        self.inspection_task_id = inspection_task_id
        self.inspection_task_name = inspection_task_name
        self.request_id = request_id
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.inspection_project is not None:
            result['InspectionProject'] = self.inspection_project

        if self.inspection_report_id is not None:
            result['InspectionReportId'] = self.inspection_report_id

        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id

        if self.inspection_task_name is not None:
            result['InspectionTaskName'] = self.inspection_task_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InspectionProject') is not None:
            self.inspection_project = m.get('InspectionProject')

        if m.get('InspectionReportId') is not None:
            self.inspection_report_id = m.get('InspectionReportId')

        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')

        if m.get('InspectionTaskName') is not None:
            self.inspection_task_name = m.get('InspectionTaskName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

