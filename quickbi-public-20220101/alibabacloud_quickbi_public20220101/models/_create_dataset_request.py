# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatasetRequest(DaraModel):
    def __init__(
        self,
        ds_id: str = None,
        table_name: str = None,
        target_directory_id: str = None,
        user_define_cube_name: str = None,
        user_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.ds_id = ds_id
        # This parameter is required.
        self.table_name = table_name
        self.target_directory_id = target_directory_id
        # This parameter is required.
        self.user_define_cube_name = user_define_cube_name
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
        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.target_directory_id is not None:
            result['TargetDirectoryId'] = self.target_directory_id

        if self.user_define_cube_name is not None:
            result['UserDefineCubeName'] = self.user_define_cube_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TargetDirectoryId') is not None:
            self.target_directory_id = m.get('TargetDirectoryId')

        if m.get('UserDefineCubeName') is not None:
            self.user_define_cube_name = m.get('UserDefineCubeName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

