# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class VerifyWorkspaceAcrRamAuthorizationResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.VerifyWorkspaceAcrRamAuthorizationResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The business status code.
        self.code = code
        # The response data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.VerifyWorkspaceAcrRamAuthorizationResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class VerifyWorkspaceAcrRamAuthorizationResponseBodyData(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        authorization_status: str = None,
        eligibility_status: str = None,
        reason_code: str = None,
        reason_message: str = None,
        role_name: str = None,
        role_source: str = None,
        workspace_id: str = None,
    ):
        # The ACR Enterprise instance ID.
        self.acr_instance_id = acr_instance_id
        # The policy attachment status for the target repository.
        self.authorization_status = authorization_status
        # The prerequisite status for access. This is not the Secret Ready status.
        self.eligibility_status = eligibility_status
        # The stable reason code for unauthorized or unmet conditions. This field is omitted when no reason exists.
        self.reason_code = reason_code
        # The human-readable reason. This field is omitted when no reason exists.
        self.reason_message = reason_message
        # The shared role name selected by the backend. This value is not editable on the frontend.
        self.role_name = role_name
        # The source of the shared role. This does not indicate that authorization is complete.
        self.role_source = role_source
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.authorization_status is not None:
            result['authorizationStatus'] = self.authorization_status

        if self.eligibility_status is not None:
            result['eligibilityStatus'] = self.eligibility_status

        if self.reason_code is not None:
            result['reasonCode'] = self.reason_code

        if self.reason_message is not None:
            result['reasonMessage'] = self.reason_message

        if self.role_name is not None:
            result['roleName'] = self.role_name

        if self.role_source is not None:
            result['roleSource'] = self.role_source

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('authorizationStatus') is not None:
            self.authorization_status = m.get('authorizationStatus')

        if m.get('eligibilityStatus') is not None:
            self.eligibility_status = m.get('eligibilityStatus')

        if m.get('reasonCode') is not None:
            self.reason_code = m.get('reasonCode')

        if m.get('reasonMessage') is not None:
            self.reason_message = m.get('reasonMessage')

        if m.get('roleName') is not None:
            self.role_name = m.get('roleName')

        if m.get('roleSource') is not None:
            self.role_source = m.get('roleSource')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

