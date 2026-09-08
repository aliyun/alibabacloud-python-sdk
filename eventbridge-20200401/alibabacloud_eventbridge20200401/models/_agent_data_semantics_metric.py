# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AgentDataSemanticsMetric(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        sqlexpression: str = None,
        synonyms: List[str] = None,
        type: str = None,
    ):
        # The usage description.
        self.description = description
        # The name of the SQL expression.
        # 
        # This parameter is required.
        self.name = name
        # The SQL expression.
        # 
        # This parameter is required.
        self.sqlexpression = sqlexpression
        # The list of synonyms. A maximum of 10 items are supported. Each item can contain up to 64 characters.
        self.synonyms = synonyms
        # The type of the SQL expression.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.sqlexpression is not None:
            result['SQLExpression'] = self.sqlexpression

        if self.synonyms is not None:
            result['Synonyms'] = self.synonyms

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SQLExpression') is not None:
            self.sqlexpression = m.get('SQLExpression')

        if m.get('Synonyms') is not None:
            self.synonyms = m.get('Synonyms')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

