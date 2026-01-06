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
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of a directory.
        # 
        # This parameter is required.
        self.path = path
        # The UID or GID of a user for whom you want to cancel the directory quota.
        # 
        # This parameter is required and valid only if the UserType parameter is set to Uid or Gid.
        # 
        # Examples:
        # 
        # *   If you want to cancel a quota for a user whose UID is 500, set the UserType parameter to Uid and set the UserId parameter to 500.
        # *   If you want to cancel a quota for a group whose GID is 100, set the UserType parameter to Gid and set the UserId parameter to 100.
        self.user_id = user_id
        # The type of the user.
        # 
        # Valid values:
        # 
        # *   Uid: user ID
        # *   Gid: user group ID
        # *   AllUsers: all users
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

