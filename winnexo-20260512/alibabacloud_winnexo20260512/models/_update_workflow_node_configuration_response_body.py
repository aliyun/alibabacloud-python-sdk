# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class UpdateWorkflowNodeConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        can_edit: bool = None,
        code: str = None,
        config_version: int = None,
        default_executor: main_models.UpdateWorkflowNodeConfigurationResponseBodyDefaultExecutor = None,
        default_model: str = None,
        default_responsible_user_ids: List[str] = None,
        effective_executor: main_models.UpdateWorkflowNodeConfigurationResponseBodyEffectiveExecutor = None,
        effective_model: str = None,
        effective_responsible_user_ids: List[str] = None,
        instance_id: str = None,
        message: str = None,
        node_id: str = None,
        overrides: main_models.UpdateWorkflowNodeConfigurationResponseBodyOverrides = None,
        request_id: str = None,
        state_version: int = None,
        updated_at: str = None,
        updated_by: int = None,
    ):
        # Indicates whether the current user can edit this node.
        self.can_edit = can_edit
        # The common business status code.
        self.code = code
        # The configuration version. Use this value as the expectedVersion when updating or restoring.
        self.config_version = config_version
        # The default executor defined in the template.
        self.default_executor = default_executor
        # The default model profile defined in the template.
        self.default_model = default_model
        # The list of user IDs for the default owners defined in the template.
        self.default_responsible_user_ids = default_responsible_user_ids
        # The currently effective executor.
        self.effective_executor = effective_executor
        # The currently effective model profile.
        self.effective_model = effective_model
        # The list of user IDs for the currently effective owners.
        self.effective_responsible_user_ids = effective_responsible_user_ids
        # The ID of the current physical plan.
        self.instance_id = instance_id
        # The common error description.
        self.message = message
        # The key of the business node.
        self.node_id = node_id
        # The instance override values. If a field is null, the default value defined in the template is used.
        self.overrides = overrides
        # The request tracking ID.
        self.request_id = request_id
        # The state refresh cursor. This value cannot be used as the configuration version.
        self.state_version = state_version
        # The time when the configuration was last updated, in ISO 8601 format. This field is empty if the configuration has never been updated.
        self.updated_at = updated_at
        # The platform user ID of the user who last updated the configuration. This field is empty if the configuration has never been updated.
        self.updated_by = updated_by

    def validate(self):
        if self.default_executor:
            self.default_executor.validate()
        if self.effective_executor:
            self.effective_executor.validate()
        if self.overrides:
            self.overrides.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_edit is not None:
            result['canEdit'] = self.can_edit

        if self.code is not None:
            result['code'] = self.code

        if self.config_version is not None:
            result['configVersion'] = self.config_version

        if self.default_executor is not None:
            result['defaultExecutor'] = self.default_executor.to_map()

        if self.default_model is not None:
            result['defaultModel'] = self.default_model

        if self.default_responsible_user_ids is not None:
            result['defaultResponsibleUserIds'] = self.default_responsible_user_ids

        if self.effective_executor is not None:
            result['effectiveExecutor'] = self.effective_executor.to_map()

        if self.effective_model is not None:
            result['effectiveModel'] = self.effective_model

        if self.effective_responsible_user_ids is not None:
            result['effectiveResponsibleUserIds'] = self.effective_responsible_user_ids

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.message is not None:
            result['message'] = self.message

        if self.node_id is not None:
            result['nodeId'] = self.node_id

        if self.overrides is not None:
            result['overrides'] = self.overrides.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.state_version is not None:
            result['stateVersion'] = self.state_version

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('canEdit') is not None:
            self.can_edit = m.get('canEdit')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('configVersion') is not None:
            self.config_version = m.get('configVersion')

        if m.get('defaultExecutor') is not None:
            temp_model = main_models.UpdateWorkflowNodeConfigurationResponseBodyDefaultExecutor()
            self.default_executor = temp_model.from_map(m.get('defaultExecutor'))

        if m.get('defaultModel') is not None:
            self.default_model = m.get('defaultModel')

        if m.get('defaultResponsibleUserIds') is not None:
            self.default_responsible_user_ids = m.get('defaultResponsibleUserIds')

        if m.get('effectiveExecutor') is not None:
            temp_model = main_models.UpdateWorkflowNodeConfigurationResponseBodyEffectiveExecutor()
            self.effective_executor = temp_model.from_map(m.get('effectiveExecutor'))

        if m.get('effectiveModel') is not None:
            self.effective_model = m.get('effectiveModel')

        if m.get('effectiveResponsibleUserIds') is not None:
            self.effective_responsible_user_ids = m.get('effectiveResponsibleUserIds')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')

        if m.get('overrides') is not None:
            temp_model = main_models.UpdateWorkflowNodeConfigurationResponseBodyOverrides()
            self.overrides = temp_model.from_map(m.get('overrides'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('stateVersion') is not None:
            self.state_version = m.get('stateVersion')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

class UpdateWorkflowNodeConfigurationResponseBodyOverrides(DaraModel):
    def __init__(
        self,
        executor: main_models.UpdateWorkflowNodeConfigurationResponseBodyOverridesExecutor = None,
        model: str = None,
        responsible_user_ids: List[int] = None,
    ):
        # The overridden executor. A value of null indicates that the default value is used.
        self.executor = executor
        # The overridden model profile. A value of null indicates that the default value is used.
        self.model = model
        # The list of overridden owner IDs. A value of null indicates that the default value is used.
        self.responsible_user_ids = responsible_user_ids

    def validate(self):
        if self.executor:
            self.executor.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor is not None:
            result['executor'] = self.executor.to_map()

        if self.model is not None:
            result['model'] = self.model

        if self.responsible_user_ids is not None:
            result['responsibleUserIds'] = self.responsible_user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('executor') is not None:
            temp_model = main_models.UpdateWorkflowNodeConfigurationResponseBodyOverridesExecutor()
            self.executor = temp_model.from_map(m.get('executor'))

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('responsibleUserIds') is not None:
            self.responsible_user_ids = m.get('responsibleUserIds')

        return self

class UpdateWorkflowNodeConfigurationResponseBodyOverridesExecutor(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # The executor ID. If the type is USER, the value is a string representing a positive integer platform user ID. If the type is AGENT, the value is the technical name of the digital worker in the workspace.
        self.id = id
        # The executor type. Valid values: USER (a human user), AGENT (a digital worker), and SYSTEM (a legacy system executor). The SYSTEM value is used only in responses.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateWorkflowNodeConfigurationResponseBodyEffectiveExecutor(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # The executor ID. If the type is USER, the value is a string representing a positive integer platform user ID. If the type is AGENT, the value is the technical name of the digital worker in the workspace.
        self.id = id
        # The executor type. Valid values: USER (a human user), AGENT (a digital worker), and SYSTEM (a legacy system executor). The SYSTEM value is used only in responses.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class UpdateWorkflowNodeConfigurationResponseBodyDefaultExecutor(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # The executor ID. If the type is USER, the value is a string representing a positive integer platform user ID. If the type is AGENT, the value is the technical name of the digital worker in the workspace.
        self.id = id
        # The executor type. Valid values: USER (a human user), AGENT (a digital worker), and SYSTEM (a legacy system executor). The SYSTEM value is used only in responses.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

