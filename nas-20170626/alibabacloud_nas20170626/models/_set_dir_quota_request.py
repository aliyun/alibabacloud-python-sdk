# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetDirQuotaRequest(DaraModel):
    def __init__(
        self,
        file_count_limit: int = None,
        file_system_id: str = None,
        path: str = None,
        quota_type: str = None,
        size_limit: int = None,
        user_id: str = None,
        user_type: str = None,
    ):
        # The number of files that a user can create in the directory.
        # 
        # This number includes the number of files, subdirectories, and special files.
        # 
        # If you set the QuotaType parameter to Enforcement, you must specify at least one of the SizeLimit and FileCountLimit parameters.
        self.file_count_limit = file_count_limit
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of the directory in the file system.
        # 
        # > *   You can set quotas only for the directories that have been created in a NAS file system. The path of the directory that you specify for a quota is the absolute path of the directory in the NAS file system, but not the local path of the compute node, such as an Elastic Compute Service (ECS) instance or a container.
        # > *   Directories whose names contain Chinese characters are not supported.
        # 
        # This parameter is required.
        self.path = path
        # The type of the quota.
        # 
        # Valid values:
        # 
        # *   Accounting: a statistical quota. If you set this parameter to Accounting, NAS calculates only the storage usage of the directory.
        # *   Enforcement: a restricted quota. If you set this parameter to Enforcement and the storage usage exceeds the quota, you can no longer create files or subdirectories for the directory, or write data to the directory.
        # 
        # This parameter is required.
        self.quota_type = quota_type
        # The size of files that a user can create in the directory.
        # 
        # Unit: GiB.
        # 
        # If you set the QuotaType parameter to Enforcement, you must specify at least one of the SizeLimit and FileCountLimit parameters.
        self.size_limit = size_limit
        # The UID or GID of the user for whom you want to set a directory quota.
        # 
        # This parameter is required and valid only if the UserType parameter is set to Uid or Gid.
        # 
        # Examples:
        # 
        # *   If you want to set a directory quota for a user whose UID is 500, set the UserType parameter to Uid and set the UserId parameter to 500.
        # *   If you want to set a directory quota for a user group whose GID is 100, set the UserType parameter to Gid and set the UserId parameter to 100.
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
        if self.file_count_limit is not None:
            result['FileCountLimit'] = self.file_count_limit

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.path is not None:
            result['Path'] = self.path

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileCountLimit') is not None:
            self.file_count_limit = m.get('FileCountLimit')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

