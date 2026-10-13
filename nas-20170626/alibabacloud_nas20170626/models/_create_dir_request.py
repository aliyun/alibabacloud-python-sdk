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
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The user group ID of the directory owner. Valid values: 0 to 4294967295.
        # 
        # This parameter is required.
        self.owner_group_id = owner_group_id
        # The user ID of the directory owner. Valid values: 0 to 4294967295.
        # 
        # This parameter is required.
        self.owner_user_id = owner_user_id
        # The POSIX permissions to apply to the root directory path. The value is a valid octal number, such as 0755.
        # 
        # This parameter is required.
        self.permission = permission
        # Specifies whether to create a multi-level directory. Valid values:
        # 
        # - true (default): If the multi-level directory does not exist, the system creates the directories level by level.
        # - false: Only the last-level directory is created. If the parent directory does not exist, an error message is returned.
        self.recursion = recursion
        # The directory name.
        # 
        # - The name must start with a forward slash (/).
        # - The name can contain digits and uppercase and lowercase letters.
        # - The name can contain underscores (_), hyphens (-), or periods (.).
        # - The path cannot contain symbolic links, such as the current directory (.), the parent directory (..), or other symbolic links.
        # >  - If the root directory does not exist, configure the automatic creation information. The system automatically creates the specified root directory based on the settings.
        #  > - If the root directory already exists, you do not need to configure the automatic creation information. If you configure the information, the automatic creation settings are ignored.
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

