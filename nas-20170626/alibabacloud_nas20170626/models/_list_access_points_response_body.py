# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class ListAccessPointsResponseBody(DaraModel):
    def __init__(
        self,
        access_points: List[main_models.ListAccessPointsResponseBodyAccessPoints] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.access_points = access_points
        self.next_token = next_token
        # This parameter is required.
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.access_points:
            for v1 in self.access_points:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessPoints'] = []
        if self.access_points is not None:
            for k1 in self.access_points:
                result['AccessPoints'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_points = []
        if m.get('AccessPoints') is not None:
            for k1 in m.get('AccessPoints'):
                temp_model = main_models.ListAccessPointsResponseBodyAccessPoints()
                self.access_points.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAccessPointsResponseBodyAccessPoints(DaraModel):
    def __init__(
        self,
        arn: str = None,
        access_group: str = None,
        access_point_id: str = None,
        access_point_name: str = None,
        agentic_space_id: str = None,
        create_time: str = None,
        create_time_utc: str = None,
        domain_name: str = None,
        enabled_ram: bool = None,
        file_system_id: str = None,
        modify_time: str = None,
        modify_time_utc: str = None,
        posix_user: main_models.ListAccessPointsResponseBodyAccessPointsPosixUser = None,
        root_path: str = None,
        root_path_permission: main_models.ListAccessPointsResponseBodyAccessPointsRootPathPermission = None,
        root_path_status: str = None,
        status: str = None,
        tags: List[main_models.ListAccessPointsResponseBodyAccessPointsTags] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        self.arn = arn
        self.access_group = access_group
        self.access_point_id = access_point_id
        self.access_point_name = access_point_name
        self.agentic_space_id = agentic_space_id
        self.create_time = create_time
        self.create_time_utc = create_time_utc
        self.domain_name = domain_name
        self.enabled_ram = enabled_ram
        self.file_system_id = file_system_id
        self.modify_time = modify_time
        self.modify_time_utc = modify_time_utc
        self.posix_user = posix_user
        self.root_path = root_path
        self.root_path_permission = root_path_permission
        self.root_path_status = root_path_status
        self.status = status
        self.tags = tags
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id

    def validate(self):
        if self.posix_user:
            self.posix_user.validate()
        if self.root_path_permission:
            self.root_path_permission.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['ARN'] = self.arn

        if self.access_group is not None:
            result['AccessGroup'] = self.access_group

        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.access_point_name is not None:
            result['AccessPointName'] = self.access_point_name

        if self.agentic_space_id is not None:
            result['AgenticSpaceId'] = self.agentic_space_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_time_utc is not None:
            result['CreateTimeUtc'] = self.create_time_utc

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.enabled_ram is not None:
            result['EnabledRam'] = self.enabled_ram

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_time_utc is not None:
            result['ModifyTimeUtc'] = self.modify_time_utc

        if self.posix_user is not None:
            result['PosixUser'] = self.posix_user.to_map()

        if self.root_path is not None:
            result['RootPath'] = self.root_path

        if self.root_path_permission is not None:
            result['RootPathPermission'] = self.root_path_permission.to_map()

        if self.root_path_status is not None:
            result['RootPathStatus'] = self.root_path_status

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ARN') is not None:
            self.arn = m.get('ARN')

        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')

        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AccessPointName') is not None:
            self.access_point_name = m.get('AccessPointName')

        if m.get('AgenticSpaceId') is not None:
            self.agentic_space_id = m.get('AgenticSpaceId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimeUtc') is not None:
            self.create_time_utc = m.get('CreateTimeUtc')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EnabledRam') is not None:
            self.enabled_ram = m.get('EnabledRam')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyTimeUtc') is not None:
            self.modify_time_utc = m.get('ModifyTimeUtc')

        if m.get('PosixUser') is not None:
            temp_model = main_models.ListAccessPointsResponseBodyAccessPointsPosixUser()
            self.posix_user = temp_model.from_map(m.get('PosixUser'))

        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')

        if m.get('RootPathPermission') is not None:
            temp_model = main_models.ListAccessPointsResponseBodyAccessPointsRootPathPermission()
            self.root_path_permission = temp_model.from_map(m.get('RootPathPermission'))

        if m.get('RootPathStatus') is not None:
            self.root_path_status = m.get('RootPathStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListAccessPointsResponseBodyAccessPointsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListAccessPointsResponseBodyAccessPointsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListAccessPointsResponseBodyAccessPointsRootPathPermission(DaraModel):
    def __init__(
        self,
        owner_group_id: int = None,
        owner_user_id: int = None,
        permission: str = None,
    ):
        self.owner_group_id = owner_group_id
        self.owner_user_id = owner_user_id
        self.permission = permission

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_group_id is not None:
            result['OwnerGroupId'] = self.owner_group_id

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.permission is not None:
            result['Permission'] = self.permission

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerGroupId') is not None:
            self.owner_group_id = m.get('OwnerGroupId')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        return self

class ListAccessPointsResponseBodyAccessPointsPosixUser(DaraModel):
    def __init__(
        self,
        posix_group_id: int = None,
        posix_secondary_group_ids: List[int] = None,
        posix_user_id: int = None,
    ):
        self.posix_group_id = posix_group_id
        self.posix_secondary_group_ids = posix_secondary_group_ids
        self.posix_user_id = posix_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.posix_group_id is not None:
            result['PosixGroupId'] = self.posix_group_id

        if self.posix_secondary_group_ids is not None:
            result['PosixSecondaryGroupIds'] = self.posix_secondary_group_ids

        if self.posix_user_id is not None:
            result['PosixUserId'] = self.posix_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PosixGroupId') is not None:
            self.posix_group_id = m.get('PosixGroupId')

        if m.get('PosixSecondaryGroupIds') is not None:
            self.posix_secondary_group_ids = m.get('PosixSecondaryGroupIds')

        if m.get('PosixUserId') is not None:
            self.posix_user_id = m.get('PosixUserId')

        return self

