# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDirRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        owner_group_id: int = None,
        owner_user_id: int = None,
        permission: str = None,
        recursion: bool = None,
        root_directory: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the owner group for the directory. Valid values: 0 to 4294967295.
        # 
        # This parameter is required.
        self.owner_group_id = owner_group_id
        # The owner ID for the directory. Valid values: 0 to 4294967295.
        # 
        # This parameter is required.
        self.owner_user_id = owner_user_id
        # The Portable Operating System Interface (POSIX) permissions applied to the root directory. The value is a valid octal number, such as 0755.
        # 
        # This parameter is required.
        self.permission = permission
        # Specifies whether to create a multi-level directory. Valid values:
        # 
        # *   true (default): If no multi-level directory exists, directories are created level by level.
        # *   false: Only the last level of directory is created. An error message is returned because the parent directory does not exist.
        self.recursion = recursion
        # The directory name.
        # 
        # *   The directory must start with a forward slash (/).
        # *   The directory can contain digits and letters.
        # *   The directory can contain underscores (_), hyphens (-), and periods (.).
        # *   The directory cannot contain symbolic links, such as the current directory (.), the upper-level directory (..), and other symbolic links.
        # 
        # > *   If the root directory does not exist, configure the information for directory creation. The system then automatically creates the specified root directory based on your settings.
        # > *  If the root directory exists, you do not need to configure the information for directory creation. The configurations for directory creation are ignored even if you configure the information.
        # 
        # This parameter is required.
        self.root_directory = root_directory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.owner_group_id is not None:
            result['OwnerGroupId'] = self.owner_group_id

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.permission is not None:
            result['Permission'] = self.permission

        if self.recursion is not None:
            result['Recursion'] = self.recursion

        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('OwnerGroupId') is not None:
            self.owner_group_id = m.get('OwnerGroupId')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        if m.get('Recursion') is not None:
            self.recursion = m.get('Recursion')

        if m.get('RootDirectory') is not None:
            self.root_directory = m.get('RootDirectory')

        return self

