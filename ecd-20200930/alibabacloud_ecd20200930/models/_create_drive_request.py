# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDriveRequest(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        description: str = None,
        domain_id: str = None,
        drive_name: str = None,
        external_domain_id: str = None,
        profile_roaming: bool = None,
        region_id: str = None,
        resource_type: str = None,
        type: str = None,
        user_id: str = None,
    ):
        # The ID of your Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The description of the user-level storage resource.
        self.description = description
        # The ID of the storage resource.
        # 
        # >  Call the DescribeDrives operation to retrieve the storage resource ID.
        self.domain_id = domain_id
        # The name of the user-level storage resource.
        self.drive_name = drive_name
        # The ID of the external storage resource.
        # 
        # >  Call the DescribeDrives operation to retrieve the external storage resource ID.
        self.external_domain_id = external_domain_id
        # >  This parameter is deprecated.
        self.profile_roaming = profile_roaming
        # The region ID.
        self.region_id = region_id
        # The type of the storage resource.
        # 
        # Valid values:
        # 
        # *   NAS: File Storage NAS
        # *   PDS: Drive and Photo Service
        self.resource_type = resource_type
        # The usage of the storage resource.
        # 
        # Valid values:
        # 
        # *   DESKTOP: data disk space
        # *   USER_PROFILE: space for personal data of the user
        self.type = type
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.drive_name is not None:
            result['DriveName'] = self.drive_name

        if self.external_domain_id is not None:
            result['ExternalDomainId'] = self.external_domain_id

        if self.profile_roaming is not None:
            result['ProfileRoaming'] = self.profile_roaming

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.type is not None:
            result['Type'] = self.type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DriveName') is not None:
            self.drive_name = m.get('DriveName')

        if m.get('ExternalDomainId') is not None:
            self.external_domain_id = m.get('ExternalDomainId')

        if m.get('ProfileRoaming') is not None:
            self.profile_roaming = m.get('ProfileRoaming')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

