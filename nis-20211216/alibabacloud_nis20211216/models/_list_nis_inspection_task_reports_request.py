# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNisInspectionTaskReportsRequest(DaraModel):
    def __init__(
        self,
        inspection_task_id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The ID of the inspection task.
        # 
        # This parameter is required.
        self.inspection_task_id = inspection_task_id
        # The number of entries to return on each page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The token that is used to retrieve the next page of results. You do not need to specify this parameter for the first query.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.inspection_task_id is not None:
            result['InspectionTaskId'] = self.inspection_task_id

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InspectionTaskId') is not None:
            self.inspection_task_id = m.get('InspectionTaskId')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

