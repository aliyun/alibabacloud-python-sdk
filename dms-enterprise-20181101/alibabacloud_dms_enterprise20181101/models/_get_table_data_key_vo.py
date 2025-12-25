# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableDataKeyVO(DaraModel):
    def __init__(
        self,
        col_name: str = None,
        db_name: str = None,
        mek_id: int = None,
        schema_name: str = None,
        tbl_name: str = None,
        user_name: str = None,
    ):
        self.col_name = col_name
        self.db_name = db_name
        self.mek_id = mek_id
        self.schema_name = schema_name
        self.tbl_name = tbl_name
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.col_name is not None:
            result['ColName'] = self.col_name

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.mek_id is not None:
            result['MekId'] = self.mek_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.tbl_name is not None:
            result['TblName'] = self.tbl_name

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColName') is not None:
            self.col_name = m.get('ColName')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('MekId') is not None:
            self.mek_id = m.get('MekId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TblName') is not None:
            self.tbl_name = m.get('TblName')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

