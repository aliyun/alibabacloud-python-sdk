# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeployTrafficControlTaskCodeRequest(DaraModel):
    def __init__(
        self,
        environment: str = None,
        instance_id: str = None,
        retry_deploy: bool = None,
    ):
        self.environment = environment
        self.instance_id = instance_id
        self.retry_deploy = retry_deploy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.environment is not None:
            result['Environment'] = self.environment

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.retry_deploy is not None:
            result['RetryDeploy'] = self.retry_deploy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Environment') is not None:
            self.environment = m.get('Environment')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RetryDeploy') is not None:
            self.retry_deploy = m.get('RetryDeploy')

        return self

