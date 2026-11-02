# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDirectoryRequest(DaraModel):
    def __init__(
        self,
        directory_name: str = None,
    ):
        # The name of the directory. The name must be globally unique.
        # 
        # Format: The name can contain lowercase letters, digits, and hyphens (-). It cannot start or end with a hyphen (-) and cannot contain two consecutive hyphens (-). It cannot start with `d-`.
        # 
        # Length: 2 to 64 characters.
        # 
        # > If you do not specify this parameter, the system automatically generates a name.
        self.directory_name = directory_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_name is not None:
            result['DirectoryName'] = self.directory_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryName') is not None:
            self.directory_name = m.get('DirectoryName')

        return self

