# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteComfyWorkflowRequest(DaraModel):
    def __init__(
        self,
        workflow_id: str = None,
    ):
        # This parameter is required.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

