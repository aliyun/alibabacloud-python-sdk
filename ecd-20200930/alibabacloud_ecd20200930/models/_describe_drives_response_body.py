# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeDrivesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        drives: List[main_models.DescribeDrivesResponseBodyDrives] = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. A value of 200 indicates success.
        self.code = code
        # The total number of entries.
        self.count = count
        # The list of user-level storage resources.
        self.drives = drives
        # The response message.
        self.message = message
        # The pagination token for the next query. An empty value indicates that there are no more results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.drives:
            for v1 in self.drives:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['Drives'] = []
        if self.drives is not None:
            for k1 in self.drives:
                result['Drives'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.drives = []
        if m.get('Drives') is not None:
            for k1 in m.get('Drives'):
                temp_model = main_models.DescribeDrivesResponseBodyDrives()
                self.drives.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeDrivesResponseBodyDrives(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        description: str = None,
        desktop_group_count: int = None,
        desktop_groups: List[main_models.DescribeDrivesResponseBodyDrivesDesktopGroups] = None,
        domain_id: str = None,
        drive_id: str = None,
        enable_profile_management: bool = None,
        external_domain_id: str = None,
        external_drive_id: str = None,
        external_user_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        name: str = None,
        profile_roaming: bool = None,
        status: str = None,
        total_size: int = None,
        type: str = None,
        used_size: int = None,
        user_id: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The storage resource description.
        self.description = description
        # The number of associated cloud computer pools.
        # > This parameter is returned only when the storage resource is NAS and the purpose is USER_PROFILE.
        self.desktop_group_count = desktop_group_count
        # The list of associated cloud computer pool details.
        # > This parameter is returned only when the storage resource is NAS and the purpose is USER_PROFILE.
        self.desktop_groups = desktop_groups
        # The storage resource ID.
        self.domain_id = domain_id
        # The user-level storage resource ID.
        self.drive_id = drive_id
        # Indicates whether the User Profile Management (UPM) feature is enabled.
        self.enable_profile_management = enable_profile_management
        # The external storage resource ID.
        # - If the storage resource is NAS, this parameter returns the NAS ID.
        # - If the storage resource is PDS, this parameter returns the PDS ID.
        self.external_domain_id = external_domain_id
        # The external user-level storage resource ID.
        # > This parameter is returned only when the storage resource is PDS.
        self.external_drive_id = external_drive_id
        # The external user ID.
        # > This parameter is returned only when the storage resource is PDS.
        self.external_user_id = external_user_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The ID.
        # > You can ignore this parameter.
        self.id = id
        # The storage resource name.
        self.name = name
        # > This parameter is deprecated.
        self.profile_roaming = profile_roaming
        # The status of the user-level storage resource.
        self.status = status
        # The total capacity of the user-level storage resource.
        self.total_size = total_size
        # The purpose of the storage resource.
        self.type = type
        # The used capacity of the user-level storage resource.
        self.used_size = used_size
        # The user ID.
        self.user_id = user_id

    def validate(self):
        if self.desktop_groups:
            for v1 in self.desktop_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_group_count is not None:
            result['DesktopGroupCount'] = self.desktop_group_count

        result['DesktopGroups'] = []
        if self.desktop_groups is not None:
            for k1 in self.desktop_groups:
                result['DesktopGroups'].append(k1.to_map() if k1 else None)

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.drive_id is not None:
            result['DriveId'] = self.drive_id

        if self.enable_profile_management is not None:
            result['EnableProfileManagement'] = self.enable_profile_management

        if self.external_domain_id is not None:
            result['ExternalDomainId'] = self.external_domain_id

        if self.external_drive_id is not None:
            result['ExternalDriveId'] = self.external_drive_id

        if self.external_user_id is not None:
            result['ExternalUserId'] = self.external_user_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.profile_roaming is not None:
            result['ProfileRoaming'] = self.profile_roaming

        if self.status is not None:
            result['Status'] = self.status

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        if self.type is not None:
            result['Type'] = self.type

        if self.used_size is not None:
            result['UsedSize'] = self.used_size

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopGroupCount') is not None:
            self.desktop_group_count = m.get('DesktopGroupCount')

        self.desktop_groups = []
        if m.get('DesktopGroups') is not None:
            for k1 in m.get('DesktopGroups'):
                temp_model = main_models.DescribeDrivesResponseBodyDrivesDesktopGroups()
                self.desktop_groups.append(temp_model.from_map(k1))

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DriveId') is not None:
            self.drive_id = m.get('DriveId')

        if m.get('EnableProfileManagement') is not None:
            self.enable_profile_management = m.get('EnableProfileManagement')

        if m.get('ExternalDomainId') is not None:
            self.external_domain_id = m.get('ExternalDomainId')

        if m.get('ExternalDriveId') is not None:
            self.external_drive_id = m.get('ExternalDriveId')

        if m.get('ExternalUserId') is not None:
            self.external_user_id = m.get('ExternalUserId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProfileRoaming') is not None:
            self.profile_roaming = m.get('ProfileRoaming')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class DescribeDrivesResponseBodyDrivesDesktopGroups(DaraModel):
    def __init__(
        self,
        desktop_group_id: str = None,
        desktop_group_name: str = None,
    ):
        # The cloud computer pool ID.
        self.desktop_group_id = desktop_group_id
        # The cloud computer pool name.
        self.desktop_group_name = desktop_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_group_id is not None:
            result['DesktopGroupId'] = self.desktop_group_id

        if self.desktop_group_name is not None:
            result['DesktopGroupName'] = self.desktop_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopGroupId') is not None:
            self.desktop_group_id = m.get('DesktopGroupId')

        if m.get('DesktopGroupName') is not None:
            self.desktop_group_name = m.get('DesktopGroupName')

        return self

