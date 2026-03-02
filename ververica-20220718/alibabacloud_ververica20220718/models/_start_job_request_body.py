# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class StartJobRequestBody(DaraModel):
    def __init__(
        self,
        deployment_id: str = None,
        resource_setting_spec: main_models.BriefResourceSetting = None,
        restore_strategy: main_models.DeploymentRestoreStrategy = None,
    ):
        # The deployment ID.
        self.deployment_id = deployment_id
        # The resource configuration of the deployment.
        self.resource_setting_spec = resource_setting_spec
        # The start offset of the job.
        self.restore_strategy = restore_strategy

    def validate(self):
        if self.resource_setting_spec:
            self.resource_setting_spec.validate()
        if self.restore_strategy:
            self.restore_strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.resource_setting_spec is not None:
            result['resourceSettingSpec'] = self.resource_setting_spec.to_map()

        if self.restore_strategy is not None:
            result['restoreStrategy'] = self.restore_strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('resourceSettingSpec') is not None:
            temp_model = main_models.BriefResourceSetting()
            self.resource_setting_spec = temp_model.from_map(m.get('resourceSettingSpec'))

        if m.get('restoreStrategy') is not None:
            temp_model = main_models.DeploymentRestoreStrategy()
            self.restore_strategy = temp_model.from_map(m.get('restoreStrategy'))

        return self

