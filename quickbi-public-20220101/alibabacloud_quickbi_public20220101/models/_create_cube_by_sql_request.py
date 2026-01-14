# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCubeBySqlRequest(DaraModel):
    def __init__(
        self,
        caption: str = None,
        custom_sql: str = None,
        ds_id: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.caption = caption
        # This parameter is required.
        self.custom_sql = custom_sql
        # This parameter is required.
        self.ds_id = ds_id
        # This parameter is required.
        self.user_id = user_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caption is not None:
            result['Caption'] = self.caption

        if self.custom_sql is not None:
            result['CustomSql'] = self.custom_sql

        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Caption') is not None:
            self.caption = m.get('Caption')

        if m.get('CustomSql') is not None:
            self.custom_sql = m.get('CustomSql')

        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

