# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyComfyWorkflowRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        workflow_id: str = None,
        workflow_name: str = None,
    ):
        self.description = description
        # This parameter is required.
        self.workflow_id = workflow_id
        self.workflow_name = workflow_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        return self

