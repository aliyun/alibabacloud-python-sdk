# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudDriveUsersResponseBody(DaraModel):
    def __init__(
        self,
        cloud_drive_users: List[main_models.DescribeCloudDriveUsersResponseBodyCloudDriveUsers] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.cloud_drive_users = cloud_drive_users
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.cloud_drive_users:
            for v1 in self.cloud_drive_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudDriveUsers'] = []
        if self.cloud_drive_users is not None:
            for k1 in self.cloud_drive_users:
                result['CloudDriveUsers'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_drive_users = []
        if m.get('CloudDriveUsers') is not None:
            for k1 in m.get('CloudDriveUsers'):
                temp_model = main_models.DescribeCloudDriveUsersResponseBodyCloudDriveUsers()
                self.cloud_drive_users.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCloudDriveUsersResponseBodyCloudDriveUsers(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        end_user_id: str = None,
        status: str = None,
        total_size: int = None,
        used_size: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.drive_id = drive_id
        self.end_user_id = end_user_id
        self.status = status
        self.total_size = total_size
        self.used_size = used_size
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['DriveId'] = self.drive_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.status is not None:
            result['Status'] = self.status

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        if self.used_size is not None:
            result['UsedSize'] = self.used_size

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DriveId') is not None:
            self.drive_id = m.get('DriveId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        if m.get('UsedSize') is not None:
            self.used_size = m.get('UsedSize')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

