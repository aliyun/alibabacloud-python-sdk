# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDriveRequest(DaraModel):
    def __init__(
        self,
        default: bool = None,
        description: str = None,
        drive_name: str = None,
        drive_type: str = None,
        owner: str = None,
        owner_type: str = None,
        status: str = None,
        total_size: int = None,
    ):
        # Specifies whether the drive is the default drive. Default value: false.
        self.default = default
        # The description of the drive. The description can be up to 1,024 characters in length.
        self.description = description
        # The name of the drive. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.drive_name = drive_name
        # The type of the drive. Set the value to normal.
        self.drive_type = drive_type
        # The owner of the drive.
        # 
        # This parameter is required.
        self.owner = owner
        # The type of the owner. Valid values:
        # 
        # user and group.
        # 
        # This parameter is required.
        self.owner_type = owner_type
        # The state of the drive. Valid values:
        # 
        # enabled and disabled.
        # 
        # Default value: enabled.
        self.status = status
        # The total size of the drive. Unit: bytes. By default, the size is unlimited.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['default'] = self.default

        if self.description is not None:
            result['description'] = self.description

        if self.drive_name is not None:
            result['drive_name'] = self.drive_name

        if self.drive_type is not None:
            result['drive_type'] = self.drive_type

        if self.owner is not None:
            result['owner'] = self.owner

        if self.owner_type is not None:
            result['owner_type'] = self.owner_type

        if self.status is not None:
            result['status'] = self.status

        if self.total_size is not None:
            result['total_size'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')

        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        return self

