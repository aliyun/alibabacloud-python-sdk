# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class RowUpdate(DaraModel):
    def __init__(
        self,
        row: main_models.Row = None,
        row_kind: str = None,
    ):
        self.row = row
        self.row_kind = row_kind

    def validate(self):
        if self.row:
            self.row.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.row is not None:
            result['row'] = self.row.to_map()

        if self.row_kind is not None:
            result['rowKind'] = self.row_kind

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('row') is not None:
            temp_model = main_models.Row()
            self.row = temp_model.from_map(m.get('row'))

        if m.get('rowKind') is not None:
            self.row_kind = m.get('rowKind')

        return self

