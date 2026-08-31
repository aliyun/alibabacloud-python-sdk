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
        # The file system ID.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The portable account ID.
        # Limit: The value is a 16-character string that supports digits and lowercase letters.
        self.owner = owner
        # Specifies whether to share directory permissions. Valid values:
        # - false (default): does not share directory permissions.
        # - true: shares directory permissions.
        # > - This parameter takes effect only when Type is set to Directory and Owner is not empty.
        # > - The directory has inheritable Owner permissions. The Owner has read and write permissions on subdirectories and files created under this directory, even if they are created by other users.
        self.owner_access_inheritable = owner_access_inheritable
        # The absolute path of the directory or file.
        # - The path must start and end with a forward slash (/).
        # - The path must be 1 to 1,023 characters in length.
        # - The path must be encoded in UTF-8.
        # 
        # This parameter is required.
        self.path = path
        # The object type. Valid values:
        # 
        # - File: file.
        # - Directory: directory.
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

