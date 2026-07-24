# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDeploymentByNameRequest(DaraModel):
    def __init__(
        self,
        deployment_name: str = None,
    ):
        # The name of the deployed job, which is typically specified by the user when submitting the job.
        # 
        # This parameter is required.
        self.deployment_name = deployment_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_name is not None:
            result['deploymentName'] = self.deployment_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentName') is not None:
            self.deployment_name = m.get('deploymentName')

        return self

