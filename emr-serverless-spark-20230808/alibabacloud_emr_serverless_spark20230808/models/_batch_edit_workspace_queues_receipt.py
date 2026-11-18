# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchEditWorkspaceQueuesReceipt(DaraModel):
    def __init__(
        self,
        accepted_queues: List[str] = None,
        skipped_queues: List[str] = None,
        workflow_instance_id: int = None,
        workspace_id: str = None,
    ):
        # The target states of these queues are progressively written during the workflow.
        self.accepted_queues = accepted_queues
        # The current values are already equal to the target values, so no write operations are required.
        self.skipped_queues = skipped_queues
        # A null value indicates that all queues in this request are already in the target state and no workflow is started (idempotent no-op).
        self.workflow_instance_id = workflow_instance_id
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accepted_queues is not None:
            result['acceptedQueues'] = self.accepted_queues

        if self.skipped_queues is not None:
            result['skippedQueues'] = self.skipped_queues

        if self.workflow_instance_id is not None:
            result['workflowInstanceId'] = self.workflow_instance_id

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptedQueues') is not None:
            self.accepted_queues = m.get('acceptedQueues')

        if m.get('skippedQueues') is not None:
            self.skipped_queues = m.get('skippedQueues')

        if m.get('workflowInstanceId') is not None:
            self.workflow_instance_id = m.get('workflowInstanceId')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

