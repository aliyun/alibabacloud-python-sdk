# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteVariableRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        variable_id: str = None,
    ):
        self.instance_id = instance_id
        self.variable_id = variable_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.variable_id is not None:
            result['VariableId'] = self.variable_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VariableId') is not None:
            self.variable_id = m.get('VariableId')

        return self

