# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class CreateConnectionRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        configs: Dict[str, str] = None,
        connection_name: str = None,
        connection_type: str = None,
        description: str = None,
        models: List[main_models.CreateConnectionRequestModels] = None,
        resource_meta: main_models.CreateConnectionRequestResourceMeta = None,
        secrets: Dict[str, str] = None,
        workspace_id: str = None,
    ):
        # The visibility of the workspace. The default value is `PRIVATE`.
        self.accessibility = accessibility
        # Configuration properties for the connection, provided as key-value pairs. The required keys depend on the connection type. For details, see the supplementary parameter information.
        # 
        # This parameter is required.
        self.configs = configs
        # The name of the connection.
        # 
        # This parameter is required.
        self.connection_name = connection_name
        # The type of the connection.
        self.connection_type = connection_type
        # The description of the connection.
        self.description = description
        # A list of models. This parameter applies to model service connections.
        self.models = models
        # Resource metadata for the connection. This parameter is typically used for database connection types.
        self.resource_meta = resource_meta
        # Sensitive connection properties that require encryption, such as database credentials or an API key for a model service.
        self.secrets = secrets
        # The ID of the workspace. To get this ID, call the [`ListWorkspaces`](https://help.aliyun.com/document_detail/449124.html) operation.
        self.workspace_id = workspace_id

    def validate(self):
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()
        if self.resource_meta:
            self.resource_meta.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.configs is not None:
            result['Configs'] = self.configs

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.description is not None:
            result['Description'] = self.description

        result['Models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['Models'].append(k1.to_map() if k1 else None)

        if self.resource_meta is not None:
            result['ResourceMeta'] = self.resource_meta.to_map()

        if self.secrets is not None:
            result['Secrets'] = self.secrets

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('Configs') is not None:
            self.configs = m.get('Configs')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.models = []
        if m.get('Models') is not None:
            for k1 in m.get('Models'):
                temp_model = main_models.CreateConnectionRequestModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('ResourceMeta') is not None:
            temp_model = main_models.CreateConnectionRequestResourceMeta()
            self.resource_meta = temp_model.from_map(m.get('ResourceMeta'))

        if m.get('Secrets') is not None:
            self.secrets = m.get('Secrets')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateConnectionRequestResourceMeta(DaraModel):
    def __init__(
        self,
        extra: str = None,
        instance_id: str = None,
        instance_name: str = None,
    ):
        # Additional configuration information.
        self.extra = extra
        # The instance ID.
        self.instance_id = instance_id
        # The instance name.
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        return self

class CreateConnectionRequestModels(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        max_model_length: int = None,
        model: str = None,
        model_type: str = None,
        support_reasoning: bool = None,
        support_response_schema: bool = None,
        support_vision: bool = None,
        tool_call: bool = None,
    ):
        # The display name of the model.
        self.display_name = display_name
        # The context length.
        self.max_model_length = max_model_length
        # The model identifier. This value corresponds to the `model` parameter in an OpenAI API request.
        self.model = model
        # The model type.
        self.model_type = model_type
        # Specifies whether the model supports deep reasoning and can output the reasoning process as `reasoning_content`.
        self.support_reasoning = support_reasoning
        # Specifies whether the model supports structured output in the OpenAI API\\"s JSON Schema format.
        self.support_response_schema = support_response_schema
        # Specifies whether the model supports visual understanding.
        self.support_vision = support_vision
        # Specifies whether the model supports tool calling.
        self.tool_call = tool_call

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.max_model_length is not None:
            result['MaxModelLength'] = self.max_model_length

        if self.model is not None:
            result['Model'] = self.model

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.support_reasoning is not None:
            result['SupportReasoning'] = self.support_reasoning

        if self.support_response_schema is not None:
            result['SupportResponseSchema'] = self.support_response_schema

        if self.support_vision is not None:
            result['SupportVision'] = self.support_vision

        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('MaxModelLength') is not None:
            self.max_model_length = m.get('MaxModelLength')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('SupportReasoning') is not None:
            self.support_reasoning = m.get('SupportReasoning')

        if m.get('SupportResponseSchema') is not None:
            self.support_response_schema = m.get('SupportResponseSchema')

        if m.get('SupportVision') is not None:
            self.support_vision = m.get('SupportVision')

        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')

        return self

