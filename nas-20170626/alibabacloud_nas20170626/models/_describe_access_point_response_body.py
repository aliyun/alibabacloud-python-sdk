# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessPointResponseBody(DaraModel):
    def __init__(
        self,
        access_point: main_models.DescribeAccessPointResponseBodyAccessPoint = None,
        request_id: str = None,
    ):
        # The access point information.
        self.access_point = access_point
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.access_point:
            self.access_point.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point is not None:
            result['AccessPoint'] = self.access_point.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPoint') is not None:
            temp_model = main_models.DescribeAccessPointResponseBodyAccessPoint()
            self.access_point = temp_model.from_map(m.get('AccessPoint'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccessPointResponseBodyAccessPoint(DaraModel):
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
        posix_user: main_models.DescribeAccessPointResponseBodyAccessPointPosixUser = None,
        region_id: str = None,
        root_path: str = None,
        root_path_permission: main_models.DescribeAccessPointResponseBodyAccessPointRootPathPermission = None,
        root_path_status: str = None,
        status: str = None,
        tags: List[main_models.DescribeAccessPointResponseBodyAccessPointTags] = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The access point ARN.
        self.arn = arn
        # The permission group name.
        self.access_group = access_group
        # The access point ID.
        self.access_point_id = access_point_id
        # The access point name.
        self.access_point_name = access_point_name
        # AgenticSpace Id。
        self.agentic_space_id = agentic_space_id
        # The time when the access point was created.
        self.create_time = create_time
        # The time when the AgenticSpace was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.create_time_utc = create_time_utc
        # The access point domain name.
        self.domain_name = domain_name
        # Indicates whether the RAM policy is enabled.
        self.enabled_ram = enabled_ram
        # The file system ID.
        self.file_system_id = file_system_id
        # The time when the access point was last modified.
        self.modify_time = modify_time
        # The time when the AgenticSpace was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
        self.modify_time_utc = modify_time_utc
        # The POSIX user.
        self.posix_user = posix_user
        # The region ID.
        self.region_id = region_id
        # The root directory.
        self.root_path = root_path
        # The permissions for creating the root directory.
        self.root_path_permission = root_path_permission
        # The current root directory status.
        # 
        # Valid values:
        # 
        # - 0: The root path status is unknown.
        # - 1: The root path does not exist. It may have been deleted by the user.
        # - 2: The root path status is normal.
        self.root_path_status = root_path_status
        # The current access point status.
        # 
        # Valid values:
        # 
        # - Active: active
        # - Inactive: inactive
        # - Pending: being created
        # - Deleting: being deleted
        self.status = status
        # The list of access point tags.
        self.tags = tags
        # The vSwitch ID.
        self.v_switch_id = v_switch_id
        # The VPC ID.
        # 
        # The VPC must be the same as the VPC of the Elastic Computing Service (ECS) server to which you want to mount the file system.
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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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
            temp_model = main_models.DescribeAccessPointResponseBodyAccessPointPosixUser()
            self.posix_user = temp_model.from_map(m.get('PosixUser'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RootPath') is not None:
            self.root_path = m.get('RootPath')

        if m.get('RootPathPermission') is not None:
            temp_model = main_models.DescribeAccessPointResponseBodyAccessPointRootPathPermission()
            self.root_path_permission = temp_model.from_map(m.get('RootPathPermission'))

        if m.get('RootPathStatus') is not None:
            self.root_path_status = m.get('RootPathStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeAccessPointResponseBodyAccessPointTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeAccessPointResponseBodyAccessPointTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class DescribeAccessPointResponseBodyAccessPointRootPathPermission(DaraModel):
    def __init__(
        self,
        owner_group_id: int = None,
        owner_user_id: int = None,
        permission: str = None,
    ):
        # The file group ID.
        self.owner_group_id = owner_group_id
        # The file owner ID.
        self.owner_user_id = owner_user_id
        # The POSIX permissions.
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

class DescribeAccessPointResponseBodyAccessPointPosixUser(DaraModel):
    def __init__(
        self,
        posix_group_id: int = None,
        posix_secondary_group_ids: List[int] = None,
        posix_user_id: int = None,
    ):
        # The POSIX user group ID.
        self.posix_group_id = posix_group_id
        # The secondary user group ID.
        self.posix_secondary_group_ids = posix_secondary_group_ids
        # The POSIX user ID.
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

