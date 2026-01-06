# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFileRequest(DaraModel):
    def __init__(
        self,
        file_system_id: str = None,
        owner: str = None,
        owner_access_inheritable: bool = None,
        path: str = None,
        type: str = None,
    ):
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the portable account. The ID must be a 16-digit string. The string can contain digits and lowercase letters.
        self.owner = owner
        # Specifies whether to share the directory. Valid values:
        # 
        # *   false (default): does not share the directory.
        # *   true: shares the directory.
        # 
        # > *   This parameter takes effect only if the Type parameter is set to Directory and the Owner parameter is not empty.
        # > *   The permissions on a directory can be inherited by the owner. The owner has read and write permissions on the subdirectories and subfiles created in the directory, even if they are created by others.
        self.owner_access_inheritable = owner_access_inheritable
        # The absolute path of the directory or file. The path must start and end with a forward slash (/) and must be 2 to 1024 characters in length.
        # 
        # This parameter is required.
        self.path = path
        # The type of the object. Valid values:
        # 
        # *   File
        # *   Directory
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_access_inheritable is not None:
            result['OwnerAccessInheritable'] = self.owner_access_inheritable

        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerAccessInheritable') is not None:
            self.owner_access_inheritable = m.get('OwnerAccessInheritable')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

