# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMapRunRequest(DaraModel):
    def __init__(
        self,
        execution_name: str = None,
        flow_name: str = None,
        map_run_name: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.execution_name = execution_name
        # This parameter is required.
        self.flow_name = flow_name
        # This parameter is required.
        self.map_run_name = map_run_name
        self.request_id = request_id

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

        if self.map_run_name is not None:
            result['MapRunName'] = self.map_run_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutionName') is not None:
            self.execution_name = m.get('ExecutionName')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('MapRunName') is not None:
            self.map_run_name = m.get('MapRunName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

