# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ModifyFileSystemRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        options: main_models.ModifyFileSystemRequestOptions = None,
    ):
        # The description of the file system.
        # 
        # Limits:
        # 
        # *   The description must be 2 to 128 characters in length.
        # *   It must start with a letter but cannot start with `http://` or `https://`.
        # *   The description can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The ID of the file system.
        # 
        # *   Sample ID of a General-purpose NAS file system: `31a8e4****`.
        # *   The IDs of Extreme NAS file systems must start with `extreme-`. Example: `extreme-0015****`.
        # *   The IDs of Cloud Paralleled File System (CPFS) file systems must start with `cpfs-`. Example: `cpfs-125487****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The options.
        self.options = options

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.options is not None:
            result['Options'] = self.options.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Options') is not None:
            temp_model = main_models.ModifyFileSystemRequestOptions()
            self.options = temp_model.from_map(m.get('Options'))

        return self

class ModifyFileSystemRequestOptions(DaraModel):
    def __init__(
        self,
        enable_oplock: bool = None,
    ):
        # Specifies whether to enable the oplock feature. Valid values:
        # 
        # *   true: enables the feature.
        # *   false: disables the feature.
        # 
        # >  Only Server Message Block (SMB) file systems support this feature.
        self.enable_oplock = enable_oplock

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_oplock is not None:
            result['EnableOplock'] = self.enable_oplock

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableOplock') is not None:
            self.enable_oplock = m.get('EnableOplock')

        return self

