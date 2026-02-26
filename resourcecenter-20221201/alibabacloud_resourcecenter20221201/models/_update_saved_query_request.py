# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSavedQueryRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        expression: str = None,
        name: str = None,
        query_id: str = None,
    ):
        # The description of the template.
        # 
        # The description must be 1 to 256 characters in length.
        self.description = description
        # The expression of the template.
        self.expression = expression
        # The name of the template.
        # 
        # - The name must be 1 to 64 characters in length.
        # 
        # - It can contain letters, digits, underscores (_), and hyphens (-).
        # 
        # - It must be globally unique.
        self.name = name
        # The ID of the template.
        # 
        # This parameter is required.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.expression is not None:
            result['Expression'] = self.expression

        if self.name is not None:
            result['Name'] = self.name

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Expression') is not None:
            self.expression = m.get('Expression')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        return self

