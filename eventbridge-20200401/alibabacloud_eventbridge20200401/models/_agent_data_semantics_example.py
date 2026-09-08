# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AgentDataSemanticsExample(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        parameters: List[main_models.AgentDataSemanticsExampleParameter] = None,
        sqlexpression: str = None,
    ):
        # The example usage description.
        self.description = description
        # The example name.
        # 
        # This parameter is required.
        self.name = name
        # The SQL example parameter list. A maximum of 20 items are supported.
        self.parameters = parameters
        # The standard SQL example.
        # 
        # This parameter is required.
        self.sqlexpression = sqlexpression

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
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

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.sqlexpression is not None:
            result['SQLExpression'] = self.sqlexpression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.AgentDataSemanticsExampleParameter()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('SQLExpression') is not None:
            self.sqlexpression = m.get('SQLExpression')

        return self

