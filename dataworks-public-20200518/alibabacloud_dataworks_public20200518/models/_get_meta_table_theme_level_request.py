# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaTableThemeLevelRequest(DaraModel):
    def __init__(
        self,
        data_source_type: str = None,
        table_guid: str = None,
    ):
        # The type of the data source. Set the value to odps.
        # 
        # This parameter is required.
        self.data_source_type = data_source_type
        # The GUID of the metatable. Specify the GUID in the format of odps.${projectName}.${tableName}.
        # 
        # This parameter is required.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

