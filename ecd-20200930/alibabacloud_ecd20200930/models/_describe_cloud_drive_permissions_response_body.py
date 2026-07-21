# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudDrivePermissionsResponseBody(DaraModel):
    def __init__(
        self,
        cloud_drive_permission_models: List[main_models.DescribeCloudDrivePermissionsResponseBodyCloudDrivePermissionModels] = None,
        request_id: str = None,
    ):
        # The list of permission settings for the enterprise cloud drive.
        self.cloud_drive_permission_models = cloud_drive_permission_models
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.cloud_drive_permission_models:
            for v1 in self.cloud_drive_permission_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudDrivePermissionModels'] = []
        if self.cloud_drive_permission_models is not None:
            for k1 in self.cloud_drive_permission_models:
                result['CloudDrivePermissionModels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_drive_permission_models = []
        if m.get('CloudDrivePermissionModels') is not None:
            for k1 in m.get('CloudDrivePermissionModels'):
                temp_model = main_models.DescribeCloudDrivePermissionsResponseBodyCloudDrivePermissionModels()
                self.cloud_drive_permission_models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCloudDrivePermissionsResponseBodyCloudDrivePermissionModels(DaraModel):
    def __init__(
        self,
        end_users: List[str] = None,
        permission: str = None,
    ):
        # The list of end user IDs.
        self.end_users = end_users
        # The file transfer permission between the enterprise cloud drive and the on-premises device for the user. Valid values:
        # 
        # - CDS_CREATE_DOWNLOAD: has both upload and download permissions.
        # - CDS_DOWNLOAD: has only download permission.
        # - CDS_CREATE: has only upload permission.
        self.permission = permission

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_users is not None:
            result['EndUsers'] = self.end_users

        if self.permission is not None:
            result['Permission'] = self.permission

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUsers') is not None:
            self.end_users = m.get('EndUsers')

        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        return self

