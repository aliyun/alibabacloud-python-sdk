# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateComfyTaskRequest(DaraModel):
    def __init__(
        self,
        hive_id: str = None,
        user_parameters: str = None,
        workflow_id: str = None,
    ):
        # This parameter is required.
        self.hive_id = hive_id
        # This parameter is required.
        self.user_parameters = user_parameters
        # This parameter is required.
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hive_id is not None:
            result['HiveId'] = self.hive_id

        if self.user_parameters is not None:
            result['UserParameters'] = self.user_parameters

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HiveId') is not None:
            self.hive_id = m.get('HiveId')

        if m.get('UserParameters') is not None:
            self.user_parameters = m.get('UserParameters')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        return self

