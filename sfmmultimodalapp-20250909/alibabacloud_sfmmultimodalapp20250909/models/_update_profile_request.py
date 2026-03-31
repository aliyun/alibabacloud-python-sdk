# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class UpdateProfileRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        attributes_operations: List[main_models.UpdateProfileRequestAttributesOperations] = None,
        description: str = None,
        name: str = None,
        user_defined_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.app_id = app_id
        self.attributes_operations = attributes_operations
        self.description = description
        self.name = name
        self.user_defined_id = user_defined_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.attributes_operations:
            for v1 in self.attributes_operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        result['AttributesOperations'] = []
        if self.attributes_operations is not None:
            for k1 in self.attributes_operations:
                result['AttributesOperations'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.user_defined_id is not None:
            result['UserDefinedId'] = self.user_defined_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        self.attributes_operations = []
        if m.get('AttributesOperations') is not None:
            for k1 in m.get('AttributesOperations'):
                temp_model = main_models.UpdateProfileRequestAttributesOperations()
                self.attributes_operations.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserDefinedId') is not None:
            self.user_defined_id = m.get('UserDefinedId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class UpdateProfileRequestAttributesOperations(DaraModel):
    def __init__(
        self,
        attribute_id: str = None,
        default_value: str = None,
        description: str = None,
        name: str = None,
        op: str = None,
    ):
        self.attribute_id = attribute_id
        self.default_value = default_value
        self.description = description
        self.name = name
        self.op = op

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_id is not None:
            result['AttributeId'] = self.attribute_id

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.op is not None:
            result['Op'] = self.op

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeId') is not None:
            self.attribute_id = m.get('AttributeId')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Op') is not None:
            self.op = m.get('Op')

        return self

