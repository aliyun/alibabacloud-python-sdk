# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDirectoryRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        new_directory_name: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The new name of the directory. The name must be globally unique.
        # 
        # The name can contain lowercase letters, digits, and hyphens (-). The name cannot start or end with a hyphen (-) and cannot contain two consecutive hyphens (-). If you want the new name of the directory to start with `d-`, you must set this parameter to the ID of the directory.
        # 
        # The name must be 2 to 64 characters in length.
        self.new_directory_name = new_directory_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.new_directory_name is not None:
            result['NewDirectoryName'] = self.new_directory_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('NewDirectoryName') is not None:
            self.new_directory_name = m.get('NewDirectoryName')

        return self

