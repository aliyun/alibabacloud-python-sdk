# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class BatchEditQueueSpec(DaraModel):
    def __init__(
        self,
        description: str = None,
        environments: List[str] = None,
        gpu_spec: List[str] = None,
        resource_spec: main_models.ResourceSpec = None,
        workspace_queue_name: str = None,
    ):
        # The description of the queue. If this parameter is not specified, the description is not modified.
        self.description = description
        # The runtime environments. If this parameter is not specified, the runtime environments are not modified.
        self.environments = environments
        # The list of GPU instance types. If this parameter is not specified, the GPU specifications are not modified.
        self.gpu_spec = gpu_spec
        # The resource specifications, which represent the absolute target value. If this parameter is not specified, only the description, environments, or GPU specifications are modified, and the quota is not recalculated.
        self.resource_spec = resource_spec
        # The name of the queue.
        # 
        # This parameter is required.
        self.workspace_queue_name = workspace_queue_name

    def validate(self):
        if self.resource_spec:
            self.resource_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.environments is not None:
            result['environments'] = self.environments

        if self.gpu_spec is not None:
            result['gpuSpec'] = self.gpu_spec

        if self.resource_spec is not None:
            result['resourceSpec'] = self.resource_spec.to_map()

        if self.workspace_queue_name is not None:
            result['workspaceQueueName'] = self.workspace_queue_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('environments') is not None:
            self.environments = m.get('environments')

        if m.get('gpuSpec') is not None:
            self.gpu_spec = m.get('gpuSpec')

        if m.get('resourceSpec') is not None:
            temp_model = main_models.ResourceSpec()
            self.resource_spec = temp_model.from_map(m.get('resourceSpec'))

        if m.get('workspaceQueueName') is not None:
            self.workspace_queue_name = m.get('workspaceQueueName')

        return self

