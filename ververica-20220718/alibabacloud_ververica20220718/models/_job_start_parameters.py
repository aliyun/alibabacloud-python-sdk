# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class JobStartParameters(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        job_id: str = None,
        local_variables: List[main_models.LocalVariable] = None,
        resource_queue_name: str = None,
        restore_strategy: main_models.DeploymentRestoreStrategy = None,
    ):
        # The deployment ID.
        self.deployment_id = deployment_id
        self.job_id = job_id
        # The variables.
        self.local_variables = local_variables
        # The queue in which the deployment is running.
        self.resource_queue_name = resource_queue_name
        # The configuration of the start offset of the deployment.
        self.restore_strategy = restore_strategy

    def validate(self):
        if self.local_variables:
            for v1 in self.local_variables:
                 if v1:
                    v1.validate()
        if self.restore_strategy:
            self.restore_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.job_id is not None:
            result['jobId'] = self.job_id

        result['localVariables'] = []
        if self.local_variables is not None:
            for k1 in self.local_variables:
                result['localVariables'].append(k1.to_map() if k1 else None)

        if self.resource_queue_name is not None:
            result['resourceQueueName'] = self.resource_queue_name

        if self.restore_strategy is not None:
            result['restoreStrategy'] = self.restore_strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')

        self.local_variables = []
        if m.get('localVariables') is not None:
            for k1 in m.get('localVariables'):
                temp_model = main_models.LocalVariable()
                self.local_variables.append(temp_model.from_map(k1))

        if m.get('resourceQueueName') is not None:
            self.resource_queue_name = m.get('resourceQueueName')

        if m.get('restoreStrategy') is not None:
            temp_model = main_models.DeploymentRestoreStrategy()
            self.restore_strategy = temp_model.from_map(m.get('restoreStrategy'))

        return self

