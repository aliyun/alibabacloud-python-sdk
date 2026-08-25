# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        directory_id: str = None,
        group_name: str = None,
    ):
        # The description of the group.
        # 
        # The description can be up to 1,024 characters in length.
        self.description = description
        # The ID of the directory.
        self.directory_id = directory_id
        # The name of the group.
        # 
        # The name can contain letters, digits, underscores (_), hyphens (-), and periods (.).\\`\\`
        # 
        # The name can be up to 128 characters in length.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

