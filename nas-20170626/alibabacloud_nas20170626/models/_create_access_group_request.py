# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateAccessGroupRequest(DaraModel):
    def __init__(
        self,
        access_group_name: str = None,
        access_group_type: str = None,
        description: str = None,
        file_system_type: str = None,
    ):
        # The name of the permission group.
        # 
        # Limits:
        # 
        # *   The name must be 3 to 64 characters in length.
        # *   The name must start with a letter and can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be different from the name of the default permission group.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        # 
        # This parameter is required.
        self.access_group_name = access_group_name
        # The network type of the permission group. Valid value: **Vpc**.
        # 
        # This parameter is required.
        self.access_group_type = access_group_type
        # The description of the permission group.
        # 
        # Limits:
        # 
        # *   By default, the description of a permission group is the same as the name of the permission group. The description must be 2 to 128 characters in length.
        # *   The name must start with a letter and cannot start with `http://` or `https://`.
        # *   The description can contain digits, colons (:), underscores (_), and hyphens (-).
        self.description = description
        # The type of the file system.
        # 
        # Valid values:
        # 
        # *   standard (default): General-purpose NAS file system.
        # *   extreme: Extreme NAS file system.
        self.file_system_type = file_system_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group_name is not None:
            result['AccessGroupName'] = self.access_group_name

        if self.access_group_type is not None:
            result['AccessGroupType'] = self.access_group_type

        if self.description is not None:
            result['Description'] = self.description

        if self.file_system_type is not None:
            result['FileSystemType'] = self.file_system_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroupName') is not None:
            self.access_group_name = m.get('AccessGroupName')

        if m.get('AccessGroupType') is not None:
            self.access_group_type = m.get('AccessGroupType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileSystemType') is not None:
            self.file_system_type = m.get('FileSystemType')

        return self

