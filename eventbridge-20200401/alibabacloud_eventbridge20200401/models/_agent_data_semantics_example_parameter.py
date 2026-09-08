# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentDataSemanticsExampleParameter(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        description: str = None,
        name: str = None,
        value: str = None,
    ):
        # The data type of the parameter.
        # 
        # This parameter is required.
        self.data_type = data_type
        # The parameter description.
        self.description = description
        # The parameter name.
        # 
        # This parameter is required.
        self.name = name
        # The example value of the parameter.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

