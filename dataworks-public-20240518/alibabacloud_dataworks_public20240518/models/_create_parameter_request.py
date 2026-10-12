# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CreateParameterRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        owner: str = None,
        project_id: int = None,
        properties: List[main_models.CreateParameterRequestProperties] = None,
        scope: str = None,
        type: str = None,
    ):
        # The description.
        self.description = description
        # The name of the parameter. It must be unique within the workspace. It must start with "workspace.". The subsequent content must start with a letter and can contain only letters, underscores, and digits. The total length of the name cannot exceed 255 characters.
        # 
        # This parameter is required.
        self.name = name
        # The account ID of the owner.
        # 
        # This parameter is required.
        self.owner = owner
        # The workspace ID. This parameter is required when Scope is set to Project.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The parameter value configurations. This parameter is required for the production environment. If duplicate environment configurations exist in the array, the subsequent configurations do not take effect.
        # 
        # This parameter is required.
        self.properties = properties
        # The scope of the parameter. Default value: Project. Other types are currently not supported.
        self.scope = scope
        # The type. Valid values:
        # - PlainConstant: plaintext constant.
        # - SecretConstant: ciphertext constant.
        # - Variable: variable.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        result['Properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['Properties'].append(k1.to_map() if k1 else None)

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        self.properties = []
        if m.get('Properties') is not None:
            for k1 in m.get('Properties'):
                temp_model = main_models.CreateParameterRequestProperties()
                self.properties.append(temp_model.from_map(k1))

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateParameterRequestProperties(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        value: str = None,
    ):
        # The project environment. Valid values:
        # - Prod: production.
        # - Dev: development.
        self.env_type = env_type
        # The parameter value. Only Chinese characters, letters, digits, and specific special characters are allowed, such as /, :, ., [, ], ,, \\, \\", ", _, =, ?, space, carriage return, line feed, +, -, *, %, &, @, !, $, #, {, and }.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

