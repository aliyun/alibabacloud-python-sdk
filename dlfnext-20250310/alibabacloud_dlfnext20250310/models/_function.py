# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class Function(DaraModel):
    def __init__(
        self,
        comment: str = None,
        created_at: int = None,
        created_by: str = None,
        definitions: Dict[str, main_models.FunctionDefinition] = None,
        deterministic: bool = None,
        id: str = None,
        input_params: List[main_models.DataField] = None,
        name: str = None,
        options: Dict[str, str] = None,
        owner: str = None,
        return_params: List[main_models.DataField] = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.comment = comment
        self.created_at = created_at
        self.created_by = created_by
        self.definitions = definitions
        self.deterministic = deterministic
        self.id = id
        self.input_params = input_params
        self.name = name
        self.options = options
        self.owner = owner
        self.return_params = return_params
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        if self.definitions:
            for v1 in self.definitions.values():
                 if v1:
                    v1.validate()
        if self.input_params:
            for v1 in self.input_params:
                 if v1:
                    v1.validate()
        if self.return_params:
            for v1 in self.return_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        result['definitions'] = {}
        if self.definitions is not None:
            for k1, v1 in self.definitions.items():
                result['definitions'][k1] = v1.to_map() if v1 else None

        if self.deterministic is not None:
            result['deterministic'] = self.deterministic

        if self.id is not None:
            result['id'] = self.id

        result['inputParams'] = []
        if self.input_params is not None:
            for k1 in self.input_params:
                result['inputParams'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.options is not None:
            result['options'] = self.options

        if self.owner is not None:
            result['owner'] = self.owner

        result['returnParams'] = []
        if self.return_params is not None:
            for k1 in self.return_params:
                result['returnParams'].append(k1.to_map() if k1 else None)

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        self.definitions = {}
        if m.get('definitions') is not None:
            for k1, v1 in m.get('definitions').items():
                temp_model = main_models.FunctionDefinition()
                self.definitions[k1] = temp_model.from_map(v1)

        if m.get('deterministic') is not None:
            self.deterministic = m.get('deterministic')

        if m.get('id') is not None:
            self.id = m.get('id')

        self.input_params = []
        if m.get('inputParams') is not None:
            for k1 in m.get('inputParams'):
                temp_model = main_models.DataField()
                self.input_params.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('options') is not None:
            self.options = m.get('options')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        self.return_params = []
        if m.get('returnParams') is not None:
            for k1 in m.get('returnParams'):
                temp_model = main_models.DataField()
                self.return_params.append(temp_model.from_map(k1))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

