# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DraftValidateParams(DaraModel):
    def __init__(
        self,
        deployment_draft_id: str = None,
        deployment_target_name: str = None,
    ):
        self.deployment_draft_id = deployment_draft_id
        self.deployment_target_name = deployment_target_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_draft_id is not None:
            result['deploymentDraftId'] = self.deployment_draft_id

        if self.deployment_target_name is not None:
            result['deploymentTargetName'] = self.deployment_target_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deploymentDraftId') is not None:
            self.deployment_draft_id = m.get('deploymentDraftId')

        if m.get('deploymentTargetName') is not None:
            self.deployment_target_name = m.get('deploymentTargetName')

        return self

