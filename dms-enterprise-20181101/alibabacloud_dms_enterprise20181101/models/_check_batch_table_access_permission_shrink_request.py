# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckBatchTableAccessPermissionShrinkRequest(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
        permission_type: str = None,
        table_name_list_shrink: str = None,
        tid: int = None,
    ):
        # This parameter is required.
        self.db_id = db_id
        self.logic = logic
        # This parameter is required.
        self.permission_type = permission_type
        # This parameter is required.
        self.table_name_list_shrink = table_name_list_shrink
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.permission_type is not None:
            result['PermissionType'] = self.permission_type

        if self.table_name_list_shrink is not None:
            result['TableNameList'] = self.table_name_list_shrink

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('PermissionType') is not None:
            self.permission_type = m.get('PermissionType')

        if m.get('TableNameList') is not None:
            self.table_name_list_shrink = m.get('TableNameList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

