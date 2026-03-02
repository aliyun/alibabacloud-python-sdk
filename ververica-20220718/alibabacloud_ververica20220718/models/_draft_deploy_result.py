# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class DraftDeployResult(DaraModel):
    def __init__(
        self,
        artifact_validation_detail: main_models.ValidateStatementResult = None,
        deployment_id: str = None,
        message: str = None,
        success: bool = None,
    ):
        # The verification result of the SQL syntax.
        self.artifact_validation_detail = artifact_validation_detail
        # The deployment ID.
        self.deployment_id = deployment_id
        # The deployment information.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.artifact_validation_detail:
            self.artifact_validation_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.artifact_validation_detail is not None:
            result['artifactValidationDetail'] = self.artifact_validation_detail.to_map()

        if self.deployment_id is not None:
            result['deploymentId'] = self.deployment_id

        if self.message is not None:
            result['message'] = self.message

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('artifactValidationDetail') is not None:
            temp_model = main_models.ValidateStatementResult()
            self.artifact_validation_detail = temp_model.from_map(m.get('artifactValidationDetail'))

        if m.get('deploymentId') is not None:
            self.deployment_id = m.get('deploymentId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

