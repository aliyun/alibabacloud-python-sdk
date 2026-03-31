# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableInfoRequest(DaraModel):
    def __init__(
        self,
        schema_name: str = None,
        type: str = None,
    ):
        # The name of the schema to which the table or view belongs.
        self.schema_name = schema_name
        # The type of the table or view that you want to view. Valid values:
        # 
        # *   **internal**: internal table
        # *   **external**: external table
        # *   **view**: view
        # *   **materializedView**: [materialize view](https://www.alibabacloud.com/help/maxcompute/user-guide/materialized-view-operations)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schema_name is not None:
            result['schemaName'] = self.schema_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('schemaName') is not None:
            self.schema_name = m.get('schemaName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

