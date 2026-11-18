# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportDriveRequest(DaraModel):
    def __init__(
        self,
        domain_id: str = None,
        end_user_id: str = None,
        force_update: bool = None,
        mount_url: str = None,
        platform: str = None,
        region_id: str = None,
    ):
        # The target UPM domain ID. For workspace scenarios, use the UpmDomainId instead of the NAS file system ID.
        # 
        # This parameter is required.
        self.domain_id = domain_id
        # The target ECD end user ID. The caller account is obtained from the authentication context.
        # 
        # This parameter is required.
        self.end_user_id = end_user_id
        # Specifies whether to force an update. Default value: false. If the file already exists and this parameter is set to false, the request fails. If this parameter is set to true, the original DriveId is reused for the update.
        self.force_update = force_update
        # The relative path of the cloud application UPM. It must be the same as the path specified during upload authorization. For cloud desktops, do not pass this parameter or pass an empty value.
        self.mount_url = mount_url
        # The target platform. Valid values: WINDOWS_10, WINDOWS_11, WINDOWS_SERVER_2019, WINDOWS_SERVER_2022, and WINDOWS_SERVER_2025.
        # 
        # This parameter is required.
        self.platform = platform
        # The region of the target UPM.
        # 
        # This parameter is required.
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

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.force_update is not None:
            result['ForceUpdate'] = self.force_update

        if self.mount_url is not None:
            result['MountUrl'] = self.mount_url

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ForceUpdate') is not None:
            self.force_update = m.get('ForceUpdate')

        if m.get('MountUrl') is not None:
            self.mount_url = m.get('MountUrl')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

