# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateVariableRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        instance_id: str = None,
        variable_id: str = None,
    ):
        self.description = description
        self.display_name = display_name
        self.instance_id = instance_id
        self.variable_id = variable_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.variable_id is not None:
            result['VariableId'] = self.variable_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VariableId') is not None:
            self.variable_id = m.get('VariableId')

        return self

