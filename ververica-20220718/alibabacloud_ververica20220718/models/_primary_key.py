# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PrimaryKey(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        constraint_name: str = None,
        constraint_type: str = None,
        enforced: bool = None,
    ):
        # This parameter is required.
        self.columns = columns
        # This parameter is required.
        self.constraint_name = constraint_name
        # This parameter is required.
        self.constraint_type = constraint_type
        # This parameter is required.
        self.enforced = enforced

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['columns'] = self.columns

        if self.constraint_name is not None:
            result['constraintName'] = self.constraint_name

        if self.constraint_type is not None:
            result['constraintType'] = self.constraint_type

        if self.enforced is not None:
            result['enforced'] = self.enforced

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')

        if m.get('constraintName') is not None:
            self.constraint_name = m.get('constraintName')

        if m.get('constraintType') is not None:
            self.constraint_type = m.get('constraintType')

        if m.get('enforced') is not None:
            self.enforced = m.get('enforced')

        return self

