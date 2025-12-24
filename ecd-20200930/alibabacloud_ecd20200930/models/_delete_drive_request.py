# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDriveRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        region_id: str = None,
    ):
        # The ID of the user-level storage resource.
        self.drive_id = drive_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['DriveId'] = self.drive_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriveId') is not None:
            self.drive_id = m.get('DriveId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

