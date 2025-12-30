# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatBISchemaIndexCreateRequest(DaraModel):
    def __init__(
        self,
        columns_excluded: str = None,
        db_name: str = None,
        instance_name: str = None,
        table_name_suffix: str = None,
        tables_included: str = None,
        to_sample: int = None,
    ):
        self.columns_excluded = columns_excluded
        # This parameter is required.
        self.db_name = db_name
        # This parameter is required.
        self.instance_name = instance_name
        self.table_name_suffix = table_name_suffix
        self.tables_included = tables_included
        self.to_sample = to_sample

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns_excluded is not None:
            result['ColumnsExcluded'] = self.columns_excluded

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.table_name_suffix is not None:
            result['TableNameSuffix'] = self.table_name_suffix

        if self.tables_included is not None:
            result['TablesIncluded'] = self.tables_included

        if self.to_sample is not None:
            result['ToSample'] = self.to_sample

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnsExcluded') is not None:
            self.columns_excluded = m.get('ColumnsExcluded')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('TableNameSuffix') is not None:
            self.table_name_suffix = m.get('TableNameSuffix')

        if m.get('TablesIncluded') is not None:
            self.tables_included = m.get('TablesIncluded')

        if m.get('ToSample') is not None:
            self.to_sample = m.get('ToSample')

        return self

