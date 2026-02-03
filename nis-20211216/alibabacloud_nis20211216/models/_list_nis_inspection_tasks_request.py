# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNisInspectionTasksRequest(DaraModel):
    def __init__(
        self,
        inspection_name: str = None,
        inspection_project: str = None,
        inspection_task_id: str = None,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
    ):
        self.inspection_name = inspection_name
        self.inspection_project = inspection_project
        self.inspection_task_id = inspection_task_id
        self.max_results = max_results
        self.next_token = next_token
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inspection_name is not None:
            result['InspectionName'] = self.inspection_name

        if self.inspection_project is not None:
            result['InspectionProject'] = self.inspection_project

        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionName') is not None:
            self.inspection_name = m.get('InspectionName')

        if m.get('InspectionProject') is not None:
            self.inspection_project = m.get('InspectionProject')

        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

