# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDriveRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        drive_id: str = None,
        drive_name: str = None,
        owner: str = None,
        status: str = None,
        total_size: int = None,
    ):
        # The description of the drive. The description can be up to 1,024 characters in length.
        self.description = description
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The name of the drive. The name can be up to 128 characters in length.
        self.drive_name = drive_name
        # The owner of the drive. Note: You can modify the owner of a personal drive only by using an AccessKey pair.
        self.owner = owner
        # The state of the drive. Valid values:
        # 
        # enabled and disabled.
        self.status = status
        # The total size of the drive. Unit: bytes. A value of -1 specifies that the size is unlimited.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.drive_name is not None:
            result['drive_name'] = self.drive_name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.status is not None:
            result['status'] = self.status

        if self.total_size is not None:
            result['total_size'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')

        return self

