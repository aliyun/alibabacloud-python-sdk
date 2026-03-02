# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class AsyncDraftDeployResult(DaraModel):
    def __init__(
        self,
        artifact_validation_detail: main_models.ValidateStatementResult = None,
        deployment_id: str = None,
        message: str = None,
        success: bool = None,
        ticket_status: str = None,
    ):
        # The verification result of the SQL syntax.
        self.artifact_validation_detail = artifact_validation_detail
        # The deployment ID.
        self.deployment_id = deployment_id
        # The information about the deployment result.
        self.message = message
        # Indicates whether the request was successful.
        self.success = success
        # The state of the execution.
        self.ticket_status = ticket_status

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

        if self.ticket_status is not None:
            result['ticketStatus'] = self.ticket_status

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

        if m.get('ticketStatus') is not None:
            self.ticket_status = m.get('ticketStatus')

        return self

