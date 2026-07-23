# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class ExecutionResult(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        row_count: int = None,
        rows: str = None,
        schema: List[main_models.SchemaColumn] = None,
        total_rows: int = None,
    ):
        # Whether truncated due to the maxRows limit
        self.is_truncated = is_truncated
        # Number of rows returned this time
        self.row_count = row_count
        # Two-dimensional array, one array per row
        self.rows = rows
        # Schema information
        self.schema = schema
        # Total number of rows that meet the criteria. Different from RowCount when IsTruncated=true
        self.total_rows = total_rows

    def validate(self):
        if self.schema:
            for v1 in self.schema:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.row_count is not None:
            result['RowCount'] = self.row_count

        if self.rows is not None:
            result['Rows'] = self.rows

        result['Schema'] = []
        if self.schema is not None:
            for k1 in self.schema:
                result['Schema'].append(k1.to_map() if k1 else None)

        if self.total_rows is not None:
            result['TotalRows'] = self.total_rows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('RowCount') is not None:
            self.row_count = m.get('RowCount')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        self.schema = []
        if m.get('Schema') is not None:
            for k1 in m.get('Schema'):
                temp_model = main_models.SchemaColumn()
                self.schema.append(temp_model.from_map(k1))

        if m.get('TotalRows') is not None:
            self.total_rows = m.get('TotalRows')

        return self

