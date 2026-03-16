# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetExecutionHistoryRequest(DaraModel):
    def __init__(
        self,
        execution_name: str = None,
        flow_name: str = None,
        limit: int = None,
        next_token: str = None,
    ):
        # The name of the execution.
        # 
        # This parameter is required.
        self.execution_name = execution_name
        # The name of the workflow.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The number of workflows that you want to query. Valid values: 1-999. Default value: 60.
        self.limit = limit
        # The name of the event to start the query. You can obtain the value from the response data.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.execution_name is not None:
            result['ExecutionName'] = self.execution_name

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

