# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class AgentDataSemanticsJoin(DaraModel):
    def __init__(
        self,
        condition: main_models.AgentDataSemanticsJoinCondition = None,
        description: str = None,
        left_table: str = None,
        relationship_type: str = None,
        right_table: str = None,
    ):
        # The join condition.
        # 
        # This parameter is required.
        self.condition = condition
        # The join usage description.
        self.description = description
        # The full name of the left table.
        # 
        # This parameter is required.
        self.left_table = left_table
        # The table relationship type.
        self.relationship_type = relationship_type
        # The full name of the right table.
        # 
        # This parameter is required.
        self.right_table = right_table

    def validate(self):
        if self.condition:
            self.condition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.left_table is not None:
            result['LeftTable'] = self.left_table

        if self.relationship_type is not None:
            result['RelationshipType'] = self.relationship_type

        if self.right_table is not None:
            result['RightTable'] = self.right_table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            temp_model = main_models.AgentDataSemanticsJoinCondition()
            self.condition = temp_model.from_map(m.get('Condition'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LeftTable') is not None:
            self.left_table = m.get('LeftTable')

        if m.get('RelationshipType') is not None:
            self.relationship_type = m.get('RelationshipType')

        if m.get('RightTable') is not None:
            self.right_table = m.get('RightTable')

        return self

