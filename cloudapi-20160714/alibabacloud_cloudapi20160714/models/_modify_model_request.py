# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyModelRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        model_name: str = None,
        new_model_name: str = None,
        schema: str = None,
    ):
        # The description of the new model definition.
        self.description = description
        # The ID of the API group to which the model belongs.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the model.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The new name of the model.
        self.new_model_name = new_model_name
        # The new definition of the model.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.new_model_name is not None:
            result['NewModelName'] = self.new_model_name

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('NewModelName') is not None:
            self.new_model_name = m.get('NewModelName')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self

