# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetModelGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetModelGroupResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response status code.
        self.code = code
        # The response data.
        self.data = data
        # The response message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetModelGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetModelGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        configuration_deployment: main_models.GetModelGroupResponseBodyDataConfigurationDeployment = None,
        description: str = None,
        entitlement_state: main_models.GetModelGroupResponseBodyDataEntitlementState = None,
        gateway_id: str = None,
        model_card_ids: List[str] = None,
        model_group_id: str = None,
        name: str = None,
        update_time: str = None,
        version: int = None,
    ):
        # The summary of the latest group configuration deployment, which is independent of API release and entitlement status. This parameter is not returned when no deployment task exists, and its return does not indicate success. It represents the current version only when the revision matches the current version. List operations do not guarantee that this parameter is populated.
        self.configuration_deployment = configuration_deployment
        # The description of the model group.
        self.description = description
        # The entitlement status information.
        self.entitlement_state = entitlement_state
        # The ID of the gateway instance.
        self.gateway_id = gateway_id
        # The list of model card IDs included in the model group.
        self.model_card_ids = model_card_ids
        # The ID of the model group.
        self.model_group_id = model_group_id
        # The name of the model group.
        self.name = name
        # The last update time in ISO 8601 (RFC 3339) format in the UTC time zone, such as 2026-05-15T10:00:00Z.
        self.update_time = update_time
        # The version number of the model group.
        self.version = version

    def validate(self):
        if self.configuration_deployment:
            self.configuration_deployment.validate()
        if self.entitlement_state:
            self.entitlement_state.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configuration_deployment is not None:
            result['configurationDeployment'] = self.configuration_deployment.to_map()

        if self.description is not None:
            result['description'] = self.description

        if self.entitlement_state is not None:
            result['entitlementState'] = self.entitlement_state.to_map()

        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.model_card_ids is not None:
            result['modelCardIds'] = self.model_card_ids

        if self.model_group_id is not None:
            result['modelGroupId'] = self.model_group_id

        if self.name is not None:
            result['name'] = self.name

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('configurationDeployment') is not None:
            temp_model = main_models.GetModelGroupResponseBodyDataConfigurationDeployment()
            self.configuration_deployment = temp_model.from_map(m.get('configurationDeployment'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('entitlementState') is not None:
            temp_model = main_models.GetModelGroupResponseBodyDataEntitlementState()
            self.entitlement_state = temp_model.from_map(m.get('entitlementState'))

        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('modelCardIds') is not None:
            self.model_card_ids = m.get('modelCardIds')

        if m.get('modelGroupId') is not None:
            self.model_group_id = m.get('modelGroupId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class GetModelGroupResponseBodyDataEntitlementState(DaraModel):
    def __init__(
        self,
        applied_revision: int = None,
        desired_revision: int = None,
        error_message: str = None,
        status: str = None,
    ):
        # The applied entitlement revision.
        self.applied_revision = applied_revision
        # The desired entitlement revision.
        self.desired_revision = desired_revision
        # The error message when entitlement fails. This parameter is not returned when no error occurs.
        self.error_message = error_message
        # The entitlement status. Valid values: Pending, Applying, Committed, and Failed. Committed only indicates that the control plane has successfully submitted and read back the status, and does not mean that all nodes have acknowledged it.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applied_revision is not None:
            result['appliedRevision'] = self.applied_revision

        if self.desired_revision is not None:
            result['desiredRevision'] = self.desired_revision

        if self.error_message is not None:
            result['errorMessage'] = self.error_message

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appliedRevision') is not None:
            self.applied_revision = m.get('appliedRevision')

        if m.get('desiredRevision') is not None:
            self.desired_revision = m.get('desiredRevision')

        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

class GetModelGroupResponseBodyDataConfigurationDeployment(DaraModel):
    def __init__(
        self,
        operation_id: str = None,
        revision: int = None,
        status: str = None,
    ):
        # The operation ID of the group configuration task, which is used for tracking only. It cannot be used in GetLogicalModelDeployment or RetryLogicalModelDeployment.
        self.operation_id = operation_id
        # The model group version corresponding to the task, which may be earlier than the current version.
        self.revision = revision
        # The configuration deployment status. Valid values: Pending, Running, Succeeded, Failed, and PartiallyFailed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation_id is not None:
            result['operationId'] = self.operation_id

        if self.revision is not None:
            result['revision'] = self.revision

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operationId') is not None:
            self.operation_id = m.get('operationId')

        if m.get('revision') is not None:
            self.revision = m.get('revision')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

