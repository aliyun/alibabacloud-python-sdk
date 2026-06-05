# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateComfyWorkflowResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        missing_nodes: List[str] = None,
        request_id: str = None,
        status: str = None,
        workflow_id: str = None,
    ):
        self.code = code
        self.message = message
        self.missing_nodes = missing_nodes
        self.request_id = request_id
        self.status = status
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.missing_nodes is not None:
            result['MissingNodes'] = self.missing_nodes

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('MissingNodes') is not None:
            self.missing_nodes = m.get('MissingNodes')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

