# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class ShareResource(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        created_by: str = None,
        database_name: str = None,
        share_type: str = None,
        table_name: str = None,
        updated_at: int = None,
        updated_by: str = None,
    ):
        self.created_at = created_at
        self.created_by = created_by
        self.database_name = database_name
        self.share_type = share_type
        self.table_name = table_name
        self.updated_at = updated_at
        self.updated_by = updated_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.created_by is not None:
            result['createdBy'] = self.created_by

        if self.database_name is not None:
            result['databaseName'] = self.database_name

        if self.share_type is not None:
            result['shareType'] = self.share_type

        if self.table_name is not None:
            result['tableName'] = self.table_name

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        if self.updated_by is not None:
            result['updatedBy'] = self.updated_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('createdBy') is not None:
            self.created_by = m.get('createdBy')

        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')

        if m.get('shareType') is not None:
            self.share_type = m.get('shareType')

        if m.get('tableName') is not None:
            self.table_name = m.get('tableName')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        if m.get('updatedBy') is not None:
            self.updated_by = m.get('updatedBy')

        return self

