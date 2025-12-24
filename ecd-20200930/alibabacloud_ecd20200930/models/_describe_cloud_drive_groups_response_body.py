# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudDriveGroupsResponseBody(DaraModel):
    def __init__(
        self,
        cloud_drive_groups: List[main_models.DescribeCloudDriveGroupsResponseBodyCloudDriveGroups] = None,
        count: int = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of team spaces.
        self.cloud_drive_groups = cloud_drive_groups
        # The total number of entries returned.
        self.count = count
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
                temp_model = main_models.DescribeCloudDriveGroupsResponseBodyCloudDriveGroups()
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

class DescribeCloudDriveGroupsResponseBodyCloudDriveGroups(DaraModel):
    def __init__(
        self,
        admin_user_ids: str = None,
        admin_user_infos: List[main_models.DescribeCloudDriveGroupsResponseBodyCloudDriveGroupsAdminUserInfos] = None,
        create_time: str = None,
        directory_id: str = None,
        drive_id: str = None,
        group_id: str = None,
        group_name: str = None,
        org_id: str = None,
        recycle_bin_size: str = None,
        status: str = None,
        total_size: int = None,
        used_size: str = None,
    ):
        self.admin_user_ids = admin_user_ids
        self.admin_user_infos = admin_user_infos
        # The time when the team space was created.
        self.create_time = create_time
        # The workspace ID.
        self.directory_id = directory_id
        # The team space ID.
        self.drive_id = drive_id
        # The team ID.
        self.group_id = group_id
        # The name of the team space.
        self.group_name = group_name
        self.org_id = org_id
        self.recycle_bin_size = recycle_bin_size
        # The team space status. Valid values:
        # 
        # *   enabled
        # *   disabled
        # 
        # Default value: enabled.
        self.status = status
        # The total capacity of the team space.
        self.total_size = total_size
        # The capacity of the used space. Unit: bytes.
        self.used_size = used_size

    def validate(self):
        if self.admin_user_infos:
            for v1 in self.admin_user_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.admin_user_ids is not None:
            result['AdminUserIds'] = self.admin_user_ids

        result['AdminUserInfos'] = []
        if self.admin_user_infos is not None:
            for k1 in self.admin_user_infos:
                result['AdminUserInfos'].append(k1.to_map() if k1 else None)

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

        if self.recycle_bin_size is not None:
            result['RecycleBinSize'] = self.recycle_bin_size

        if self.status is not None:
            result['Status'] = self.status

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        if self.used_size is not None:
            result['UsedSize'] = self.used_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdminUserIds') is not None:
            self.admin_user_ids = m.get('AdminUserIds')

        self.admin_user_infos = []
        if m.get('AdminUserInfos') is not None:
            for k1 in m.get('AdminUserInfos'):
                temp_model = main_models.DescribeCloudDriveGroupsResponseBodyCloudDriveGroupsAdminUserInfos()
                self.admin_user_infos.append(temp_model.from_map(k1))

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

        if m.get('RecycleBinSize') is not None:
            self.recycle_bin_size = m.get('RecycleBinSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')

        return self

class DescribeCloudDriveGroupsResponseBodyCloudDriveGroupsAdminUserInfos(DaraModel):
    def __init__(
        self,
        email: str = None,
        end_user_id: str = None,
        job_number: str = None,
        nick_name: str = None,
        phone: str = None,
        real_nick_name: str = None,
        remark: str = None,
    ):
        self.email = email
        self.end_user_id = end_user_id
        self.job_number = job_number
        self.nick_name = nick_name
        self.phone = phone
        self.real_nick_name = real_nick_name
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email is not None:
            result['Email'] = self.email

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.job_number is not None:
            result['JobNumber'] = self.job_number

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.phone is not None:
            result['Phone'] = self.phone

        if self.real_nick_name is not None:
            result['RealNickName'] = self.real_nick_name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('JobNumber') is not None:
            self.job_number = m.get('JobNumber')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('Phone') is not None:
            self.phone = m.get('Phone')

        if m.get('RealNickName') is not None:
            self.real_nick_name = m.get('RealNickName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

