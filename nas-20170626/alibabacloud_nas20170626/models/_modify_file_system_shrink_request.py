# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFileSystemShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        file_system_id: str = None,
        options_shrink: str = None,
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
        self.options_shrink = options_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.options_shrink is not None:
            result['Options'] = self.options_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('Options') is not None:
            self.options_shrink = m.get('Options')

        return self

