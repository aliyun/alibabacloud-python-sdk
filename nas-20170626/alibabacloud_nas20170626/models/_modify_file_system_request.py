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
        # - The description must be 2 to 128 characters.
        # 
        # - It must start with an uppercase or lowercase letter or a Chinese character, and cannot start with `http://` or `https://`.
        # 
        # - It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The ID of the file system.
        # 
        # - General-purpose NAS: For example, `31a8e4****`.
        # 
        # - Extreme NAS: The ID must start with `extreme-`. For example, `extreme-0015****`.
        # 
        # - CPFS: The ID must start with `cpfs-`. For example, `cpfs-125487****`.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # Additional options for the file system.
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
        enable_abe: bool = None,
        enable_oplock: bool = None,
        vsc_access_point_access_only: bool = None,
    ):
        self.enable_abe = enable_abe
        # Specifies whether to enable OpLock. Valid values:
        # 
        # - true: Enables OpLock.
        # 
        # - false: Disables OpLock.
        # 
        # > This feature is available only for file systems that use the SMB protocol.
        self.enable_oplock = enable_oplock
        self.vsc_access_point_access_only = vsc_access_point_access_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_abe is not None:
            result['EnableABE'] = self.enable_abe

        if self.enable_oplock is not None:
            result['EnableOplock'] = self.enable_oplock

        if self.vsc_access_point_access_only is not None:
            result['VscAccessPointAccessOnly'] = self.vsc_access_point_access_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableABE') is not None:
            self.enable_abe = m.get('EnableABE')

        if m.get('EnableOplock') is not None:
            self.enable_oplock = m.get('EnableOplock')

        if m.get('VscAccessPointAccessOnly') is not None:
            self.vsc_access_point_access_only = m.get('VscAccessPointAccessOnly')

        return self

