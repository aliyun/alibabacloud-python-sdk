# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkflowTasksRequest(DaraModel):
    def __init__(
        self,
        end_of_create_time: str = None,
        key_text: str = None,
        max_results: int = None,
        next_token: str = None,
        start_of_create_time: str = None,
        workflow_id: str = None,
        workflow_name: str = None,
    ):
        # The end of the time range for filtering tasks by their creation time. Supports querying data from the last 90 days only.
        self.end_of_create_time = end_of_create_time
        # A keyword for fuzzy matching against the TaskInput, such as a file name or Media ID. Max length: 32 characters.
        self.key_text = key_text
        # The maximum number of media workflow instances to return. Valid values: 1 to 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The start of the time range for filtering tasks by their creation time. Supports querying data from the last 90 days only.
        self.start_of_create_time = start_of_create_time
        # The ID of the workflow template.[](https://ims.console.aliyun.com/settings/workflow/list)
        self.workflow_id = workflow_id
        # The name of the workflow template.
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_of_create_time is not None:
            result['EndOfCreateTime'] = self.end_of_create_time

        if self.key_text is not None:
            result['KeyText'] = self.key_text

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.start_of_create_time is not None:
            result['StartOfCreateTime'] = self.start_of_create_time

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndOfCreateTime') is not None:
            self.end_of_create_time = m.get('EndOfCreateTime')

        if m.get('KeyText') is not None:
            self.key_text = m.get('KeyText')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('StartOfCreateTime') is not None:
            self.start_of_create_time = m.get('StartOfCreateTime')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        return self

