# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class EditWorkspaceQueueRequest(DaraModel):
    def __init__(
        self,
        environments: List[str] = None,
        resource_spec: main_models.EditWorkspaceQueueRequestResourceSpec = None,
        workspace_id: str = None,
        workspace_queue_name: str = None,
        region_id: str = None,
    ):
        self.environments = environments
        self.resource_spec = resource_spec
        self.workspace_id = workspace_id
        self.workspace_queue_name = workspace_queue_name
        self.region_id = region_id

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environments is not None:
            result['environments'] = self.environments

        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec.to_map()

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        if self.workspace_queue_name is not None:
            result['workspaceQueueName'] = self.workspace_queue_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('environments') is not None:
            self.environments = m.get('environments')

        if m.get('resourceSpec') is not None:
            temp_model = main_models.EditWorkspaceQueueRequestResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('resourceSpec'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        if m.get('workspaceQueueName') is not None:
            self.workspace_queue_name = m.get('workspaceQueueName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class EditWorkspaceQueueRequestResourceSpec(DaraModel):
    def __init__(
        self,
        cu: int = None,
        max_cu: int = None,
    ):
        self.cu = cu
        self.max_cu = max_cu

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['cu'] = self.cu

        if self.max_cu is not None:
            result['maxCu'] = self.max_cu

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cu') is not None:
            self.cu = m.get('cu')

        if m.get('maxCu') is not None:
            self.max_cu = m.get('maxCu')

        return self

