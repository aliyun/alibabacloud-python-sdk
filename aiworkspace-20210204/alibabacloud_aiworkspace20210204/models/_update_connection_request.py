# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class UpdateConnectionRequest(DaraModel):
    def __init__(
        self,
        configs: Dict[str, str] = None,
        description: str = None,
        models: List[main_models.UpdateConnectionRequestModels] = None,
        secrets: Dict[str, str] = None,
    ):
        # The configuration of the connection, specified as key-value pairs. The keys in the Configs parameter vary based on the connection type. For more information, see the request parameters in the CreateConnection topic.
        self.configs = configs
        # The description of the connection.
        self.description = description
        # A list of model information.
        self.models = models
        # Key-value pairs that require encryption, such as database logon passwords and keys for model connections.
        self.secrets = secrets

    def validate(self):
        if self.models:
            for v1 in self.models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.configs is not None:
            result['Configs'] = self.configs

        if self.description is not None:
            result['Description'] = self.description

        result['Models'] = []
        if self.models is not None:
            for k1 in self.models:
                result['Models'].append(k1.to_map() if k1 else None)

        if self.secrets is not None:
            result['Secrets'] = self.secrets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Configs') is not None:
            self.configs = m.get('Configs')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.models = []
        if m.get('Models') is not None:
            for k1 in m.get('Models'):
                temp_model = main_models.UpdateConnectionRequestModels()
                self.models.append(temp_model.from_map(k1))

        if m.get('Secrets') is not None:
            self.secrets = m.get('Secrets')

        return self

class UpdateConnectionRequestModels(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        model: str = None,
        model_type: str = None,
        tool_call: bool = None,
    ):
        # The display name of the model.
        self.display_name = display_name
        # The model identifier.
        self.model = model
        # The model type. Valid values:
        # 
        # - LLM
        # 
        # - Embedding
        # 
        # - ReRank
        self.model_type = model_type
        # Indicates whether tool calling is supported. Valid values:
        # 
        # - true: Tool calling is supported.
        # 
        # - false: Tool calling is not supported.
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

        if self.model is not None:
            result['Model'] = self.model

        if self.model_type is not None:
            result['ModelType'] = self.model_type

        if self.tool_call is not None:
            result['ToolCall'] = self.tool_call

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('ModelType') is not None:
            self.model_type = m.get('ModelType')

        if m.get('ToolCall') is not None:
            self.tool_call = m.get('ToolCall')

        return self

