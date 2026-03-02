# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLineageInfoParams(DaraModel):
    def __init__(
        self,
        depth: int = None,
        direction: str = None,
        id: str = None,
        id_type: str = None,
        is_column_level: bool = None,
        is_temporary: bool = None,
        namespace: str = None,
        workspace: str = None,
    ):
        # The depth of the data lineage.
        self.depth = depth
        # The direction of the lineage. Valid values:
        # 
        # *   UPSTREAM: searches for upstream operators.
        # *   DOWNSTREAM: searches for downstream operators.
        # *   BOTH: searches for both upstream and downstream operators.
        self.direction = direction
        # The job ID or the table ID. You can call the ListJobs operation to obtain the job ID or call the ListTables operation to obtain the table ID.
        self.id = id
        # The data type of the job or table. If the id parameter is set to the job ID, the value of this parameter is the data type of the job. If the id parameter is set to the table ID, the value of this parameter is the data type of the table.
        self.id_type = id_type
        # The lineage type. The value true indicates a field-level lineage. The value false indicates a table-level lineage.
        self.is_column_level = is_column_level
        # Indicates whether the table was a temporary table.
        self.is_temporary = is_temporary
        # The name of the namespace.
        self.namespace = namespace
        # The workspace ID.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.depth is not None:
            result['depth'] = self.depth

        if self.direction is not None:
            result['direction'] = self.direction

        if self.id is not None:
            result['id'] = self.id

        if self.id_type is not None:
            result['idType'] = self.id_type

        if self.is_column_level is not None:
            result['isColumnLevel'] = self.is_column_level

        if self.is_temporary is not None:
            result['isTemporary'] = self.is_temporary

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('depth') is not None:
            self.depth = m.get('depth')

        if m.get('direction') is not None:
            self.direction = m.get('direction')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('idType') is not None:
            self.id_type = m.get('idType')

        if m.get('isColumnLevel') is not None:
            self.is_column_level = m.get('isColumnLevel')

        if m.get('isTemporary') is not None:
            self.is_temporary = m.get('isTemporary')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

