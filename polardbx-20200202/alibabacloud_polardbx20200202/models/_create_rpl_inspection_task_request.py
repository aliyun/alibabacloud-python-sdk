# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRplInspectionTaskRequest(DaraModel):
    def __init__(
        self,
        dst_db: str = None,
        dst_password: str = None,
        dst_res_id: str = None,
        dst_user_name: str = None,
        region_id: str = None,
        slink_task_id: str = None,
        src_password: str = None,
        src_user_name: str = None,
    ):
        # The ID of the ApsaraDB RDS instance to which the migration object belongs in the target instance. > You can invoke the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation to query the details of all ApsaraDB RDS instances in the specified region, including instance IDs.
        self.dst_db = dst_db
        # The password of the privileged account for the destination ApsaraDB RDS instance. > * The password must be 8 to 32 characters in length. * The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. * Special characters include ! @ # $ & % ^ * ( ) _ + - =.
        self.dst_password = dst_password
        # The destination task ID.
        self.dst_res_id = dst_res_id
        # The username used to connect to the target instance.
        self.dst_user_name = dst_user_name
        # The region ID. > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196841.html) operation to query the regions supported by PolarDB-X, including region IDs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The switchover task ID.
        # 
        # This parameter is required.
        self.slink_task_id = slink_task_id
        # The password of the source ApsaraDB RDS instance. > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation to query the details of all instances in the specified region, including the password.
        self.src_password = src_password
        # The username used to connect to the source instance (source database).
        self.src_user_name = src_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_db is not None:
            result['DstDb'] = self.dst_db

        if self.dst_password is not None:
            result['DstPassword'] = self.dst_password

        if self.dst_res_id is not None:
            result['DstResId'] = self.dst_res_id

        if self.dst_user_name is not None:
            result['DstUserName'] = self.dst_user_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.slink_task_id is not None:
            result['SlinkTaskId'] = self.slink_task_id

        if self.src_password is not None:
            result['SrcPassword'] = self.src_password

        if self.src_user_name is not None:
            result['SrcUserName'] = self.src_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstDb') is not None:
            self.dst_db = m.get('DstDb')

        if m.get('DstPassword') is not None:
            self.dst_password = m.get('DstPassword')

        if m.get('DstResId') is not None:
            self.dst_res_id = m.get('DstResId')

        if m.get('DstUserName') is not None:
            self.dst_user_name = m.get('DstUserName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SlinkTaskId') is not None:
            self.slink_task_id = m.get('SlinkTaskId')

        if m.get('SrcPassword') is not None:
            self.src_password = m.get('SrcPassword')

        if m.get('SrcUserName') is not None:
            self.src_user_name = m.get('SrcUserName')

        return self

