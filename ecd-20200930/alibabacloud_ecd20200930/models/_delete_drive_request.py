# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDriveRequest(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        drive_id: str = None,
        end_user_id: str = None,
        office_site_id: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        self.domain_id = domain_id
        # The ID of the user-level storage resource.
        self.drive_id = drive_id
        # The ID of the end user. This parameter is used when locating the UPM drive by using DomainId or OfficeSiteId.
        self.end_user_id = end_user_id
        # The ID of the workspace.
        self.office_site_id = office_site_id
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.drive_id is not None:
            result['DriveId'] = self.drive_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DriveId') is not None:
            self.drive_id = m.get('DriveId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

