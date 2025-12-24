# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudDiskGroupDrivesResponseBody(DaraModel):
    def __init__(
        self,
        cloud_drive_groups: List[main_models.DescribeCloudDiskGroupDrivesResponseBodyCloudDriveGroups] = None,
        count: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.cloud_drive_groups = cloud_drive_groups
        self.count = count
        self.next_token = next_token
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.cloud_drive_groups:
            for v1 in self.cloud_drive_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudDriveGroups'] = []
        if self.cloud_drive_groups is not None:
            for k1 in self.cloud_drive_groups:
                result['CloudDriveGroups'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_drive_groups = []
        if m.get('CloudDriveGroups') is not None:
            for k1 in m.get('CloudDriveGroups'):
                temp_model = main_models.DescribeCloudDiskGroupDrivesResponseBodyCloudDriveGroups()
                self.cloud_drive_groups.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCloudDiskGroupDrivesResponseBodyCloudDriveGroups(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        directory_id: str = None,
        drive_id: str = None,
        group_id: str = None,
        group_name: str = None,
        org_id: str = None,
        status: str = None,
        total_size: int = None,
        used_size: str = None,
    ):
        self.create_time = create_time
        self.directory_id = directory_id
        self.drive_id = drive_id
        self.group_id = group_id
        self.group_name = group_name
        self.org_id = org_id
        self.status = status
        self.total_size = total_size
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.drive_id is not None:
            result['DriveId'] = self.drive_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.org_id is not None:
            result['OrgId'] = self.org_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        if self.used_size is not None:
            result['UsedSize'] = self.used_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('DriveId') is not None:
            self.drive_id = m.get('DriveId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('OrgId') is not None:
            self.org_id = m.get('OrgId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')

        return self

