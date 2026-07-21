# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class AddFilePermissionRequest(DaraModel):
    def __init__(
        self,
        cds_id: str = None,
        end_user_id: str = None,
        file_id: str = None,
        group_id: str = None,
        member_list: List[main_models.AddFilePermissionRequestMemberList] = None,
        region_id: str = None,
    ):
        # The enterprise cloud disk ID.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The ID of the user who uses the cloud disk.
        self.end_user_id = end_user_id
        # The file ID. You can call [ListCdsFiles](https://help.aliyun.com/document_detail/2247622.html) to query the ID of the file.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The team space ID.
        self.group_id = group_id
        # The list of authorized users.
        # 
        # This parameter is required.
        self.member_list = member_list
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.member_list:
            for v1 in self.member_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_id is not None:
            result['CdsId'] = self.cds_id

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        result['MemberList'] = []
        if self.member_list is not None:
            for k1 in self.member_list:
                result['MemberList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsId') is not None:
            self.cds_id = m.get('CdsId')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        self.member_list = []
        if m.get('MemberList') is not None:
            for k1 in m.get('MemberList'):
                temp_model = main_models.AddFilePermissionRequestMemberList()
                self.member_list.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class AddFilePermissionRequestMemberList(DaraModel):
    def __init__(
        self,
        cds_identity: main_models.AddFilePermissionRequestMemberListCdsIdentity = None,
        disinherit_sub_group: bool = None,
        expire_time: int = None,
        role_id: str = None,
    ):
        # The user object.
        # 
        # This parameter is required.
        self.cds_identity = cds_identity
        # Specifies whether sub-user groups inherit the permissions.
        self.disinherit_sub_group = disinherit_sub_group
        # The time when the authorization expires. The value is the number of milliseconds from January 1, 1970, 00:00:00 to the target time. To set permanent validity, specify a predefined system value, such as 4775500800000.
        self.expire_time = expire_time
        # Two methods are supported for setting permissions: specifying a role or customizing operation permissions. This parameter specifies a role for permission settings and is mutually exclusive with ActionList. If both parameters are specified, this parameter takes precedence.
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        if self.cds_identity:
            self.cds_identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cds_identity is not None:
            result['CdsIdentity'] = self.cds_identity.to_map()

        if self.disinherit_sub_group is not None:
            result['DisinheritSubGroup'] = self.disinherit_sub_group

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdsIdentity') is not None:
            temp_model = main_models.AddFilePermissionRequestMemberListCdsIdentity()
            self.cds_identity = temp_model.from_map(m.get('CdsIdentity'))

        if m.get('DisinheritSubGroup') is not None:
            self.disinherit_sub_group = m.get('DisinheritSubGroup')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        return self

class AddFilePermissionRequestMemberListCdsIdentity(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # The user ID.
        # 
        # This parameter is required.
        self.id = id
        # The user type.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

