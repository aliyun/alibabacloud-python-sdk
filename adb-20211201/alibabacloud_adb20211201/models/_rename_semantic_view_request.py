# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RenameSemanticViewRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        new_schema_name: str = None,
        new_view_name: str = None,
        old_schema_name: str = None,
        old_view_name: str = None,
    ):
        # The ID of the AnalyticDB for MySQL cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The new schema name in which the semantic view resides.
        # 
        # This parameter is required.
        self.new_schema_name = new_schema_name
        # The new name of the semantic view.
        # 
        # This parameter is required.
        self.new_view_name = new_view_name
        # The original schema name in which the semantic view resides.
        # 
        # This parameter is required.
        self.old_schema_name = old_schema_name
        # The original name of the semantic view.
        # 
        # This parameter is required.
        self.old_view_name = old_view_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.new_schema_name is not None:
            result['NewSchemaName'] = self.new_schema_name

        if self.new_view_name is not None:
            result['NewViewName'] = self.new_view_name

        if self.old_schema_name is not None:
            result['OldSchemaName'] = self.old_schema_name

        if self.old_view_name is not None:
            result['OldViewName'] = self.old_view_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('NewSchemaName') is not None:
            self.new_schema_name = m.get('NewSchemaName')

        if m.get('NewViewName') is not None:
            self.new_view_name = m.get('NewViewName')

        if m.get('OldSchemaName') is not None:
            self.old_schema_name = m.get('OldSchemaName')

        if m.get('OldViewName') is not None:
            self.old_view_name = m.get('OldViewName')

        return self

