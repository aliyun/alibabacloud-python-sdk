# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkflowExecutionsRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        cluster_id: str = None,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        page_num: int = None,
        page_size: int = None,
        start_time: str = None,
        status: int = None,
        workflow_execution_id: int = None,
        workflow_id: int = None,
        workflow_name: str = None,
    ):
        self.app_name = app_name
        # This parameter is required.
        self.cluster_id = cluster_id
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.page_num = page_num
        self.page_size = page_size
        self.start_time = start_time
        self.status = status
        self.workflow_execution_id = workflow_execution_id
        self.workflow_id = workflow_id
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.workflow_execution_id is not None:
            result['WorkflowExecutionId'] = self.workflow_execution_id

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkflowExecutionId') is not None:
            self.workflow_execution_id = m.get('WorkflowExecutionId')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        return self

