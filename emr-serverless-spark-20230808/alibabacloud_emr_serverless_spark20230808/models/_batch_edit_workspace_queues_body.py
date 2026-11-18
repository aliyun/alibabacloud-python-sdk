# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class BatchEditWorkspaceQueuesBody(DaraModel):
    def __init__(
        self,
        queues: List[main_models.BatchEditQueueSpec] = None,
        workspace_id: str = None,
    ):
        # The list of queues to update. Each entry independently specifies the absolute target state of a queue. Queue names must be unique within the same request.
        # 
        # This parameter is required.
        self.queues = queues
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.queues:
            for v1 in self.queues:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['queues'] = []
        if self.queues is not None:
            for k1 in self.queues:
                result['queues'].append(k1.to_map() if k1 else None)

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.queues = []
        if m.get('queues') is not None:
            for k1 in m.get('queues'):
                temp_model = main_models.BatchEditQueueSpec()
                self.queues.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

