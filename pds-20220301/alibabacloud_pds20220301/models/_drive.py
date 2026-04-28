# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Drive(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        drive_type: str = None,
        owner: str = None,
        owner_type: str = None,
        status: str = None,
        total_size: int = None,
        used_size: int = None,
    ):
        # The time when the drive was created.
        self.created_at = created_at
        # The user who created the drive.
        self.creator = creator
        # The description of the drive.
        self.description = description
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The drive name.
        self.drive_name = drive_name
        # The type of the drive.
        self.drive_type = drive_type
        # The owner of the drive.
        self.owner = owner
        # The type of the owner.
        self.owner_type = owner_type
        # The status of the driver.
        self.status = status
        # The total storage space of the drive.
        self.total_size = total_size
        # The occupied storage space of the drive.
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.description is not None:
            result['description'] = self.description

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

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

        if self.used_size is not None:
            result['used_size'] = self.used_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

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

        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')

        return self

