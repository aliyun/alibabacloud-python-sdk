# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AgentDataSemanticsJoinCondition(DaraModel):
    def __init__(
        self,
        left_column: str = None,
        mode: str = None,
        right_column: str = None,
        sqlexpression: str = None,
    ):
        # The left table field name in form mode.
        self.left_column = left_column
        # The conditional expression method.
        # 
        # This parameter is required.
        self.mode = mode
        # The right table field name in form mode.
        self.right_column = right_column
        # The join SQL expression in SQL mode.
        self.sqlexpression = sqlexpression

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.left_column is not None:
            result['LeftColumn'] = self.left_column

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.right_column is not None:
            result['RightColumn'] = self.right_column

        if self.sqlexpression is not None:
            result['SQLExpression'] = self.sqlexpression

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LeftColumn') is not None:
            self.left_column = m.get('LeftColumn')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RightColumn') is not None:
            self.right_column = m.get('RightColumn')

        if m.get('SQLExpression') is not None:
            self.sqlexpression = m.get('SQLExpression')

        return self

