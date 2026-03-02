# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class DraftDeployParams(DaraModel):
    def __init__(
        self,
        deployment_draft_id: str = None,
        deployment_target: main_models.BriefDeploymentTarget = None,
        skip_validate: bool = None,
    ):
        # The draft ID.
        self.deployment_draft_id = deployment_draft_id
        # The cluster on which the deployment is deployed.
        self.deployment_target = deployment_target
        # Specifies whether to skip the syntax check.
        self.skip_validate = skip_validate

    def validate(self):
        if self.deployment_target:
            self.deployment_target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_draft_id is not None:
            result['deploymentDraftId'] = self.deployment_draft_id

        if self.deployment_target is not None:
            result['deploymentTarget'] = self.deployment_target.to_map()

        if self.skip_validate is not None:
            result['skipValidate'] = self.skip_validate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentDraftId') is not None:
            self.deployment_draft_id = m.get('deploymentDraftId')

        if m.get('deploymentTarget') is not None:
            temp_model = main_models.BriefDeploymentTarget()
            self.deployment_target = temp_model.from_map(m.get('deploymentTarget'))

        if m.get('skipValidate') is not None:
            self.skip_validate = m.get('skipValidate')

        return self

