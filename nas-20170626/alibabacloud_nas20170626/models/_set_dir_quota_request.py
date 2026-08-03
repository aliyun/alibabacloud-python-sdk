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
        # The maximum number of files in the directory.
        # 
        # This includes files, directories, and special files.
        # 
        # 
        # When QuotaType is set to Enforcement, you must specify at least one of SizeLimit and FileCountLimit.
        self.file_count_limit = file_count_limit
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The absolute path of the directory in the file system.
        #  > - You can set a quota only for a directory that has been created in the NAS file system. The directory path for the quota is the absolute path in the NAS file system, not the local path on a compute node (for example, an ECS instance or container).
        #  > - Directories whose path names contain Chinese characters are not supported.
        # 
        # This parameter is required.
        self.path = path
        # The quota type.
        # 
        # Valid values:
        # - Accounting: statistical quota. Only tracks usage.
        # - Enforcement: restrictive quota. When usage exceeds the limit, operations such as creating files or directories and appending data fail.
        # 
        # This parameter is required.
        self.quota_type = quota_type
        # The total capacity limit for files in the directory.
        # 
        # Unit: GiB.
        # 
        # 
        # When QuotaType is set to Enforcement, you must specify at least one of SizeLimit and FileCountLimit.
        self.size_limit = size_limit
        # The UID or GID to restrict.
        # 
        # This parameter is required and valid only when UserType is set to Uid or Gid.
        # 
        # Examples:
        # 
        # - To restrict the user whose UID is 500, set UserType to Uid and UserId to 500.
        # - To restrict the user group whose GID is 100, set UserType to Gid and UserId to 100.
        self.user_id = user_id
        # The user type.
        # 
        # Valid values:
        # 
        # - Uid: user ID
        # - Gid: user group ID
        # - AllUsers: all users
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

