# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelDirQuotaRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        path: str = None,
        user_id: str = None,
        user_type: str = None,
    ):
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of the directory in the file system.
        # 
        # This parameter is required.
        self.path = path
        # The UID or GID to cancel.
        # 
        # This parameter is required and valid only when UserType is set to Uid or Gid.
        # 
        # Examples:
        # 
        # - To cancel the quota for the user whose UID is 500, set UserType to Uid and UserId to 500.
        # - To cancel the quota for the user group whose GID is 100, set UserType to Gid and UserId to 100.
        self.user_id = user_id
        # The user type.
        # 
        # Valid values:
        # 
        # - Uid: user ID
        # - Gid: user group ID
        # - AllUsers: all users.
        # 
        # This parameter is required.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.path is not None:
            result['Path'] = self.path

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

