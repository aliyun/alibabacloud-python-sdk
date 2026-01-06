# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class CreateAccessPointRequest(DaraModel):
    def __init__(
        self,
        access_group: str = None,
        access_point_name: str = None,
        enabled_ram: bool = None,
        file_system_id: str = None,
        owner_group_id: int = None,
        owner_user_id: int = None,
        permission: str = None,
        posix_group_id: int = None,
        posix_secondary_group_ids: str = None,
        posix_user_id: int = None,
        root_directory: str = None,
        tag: List[main_models.CreateAccessPointRequestTag] = None,
        vpc_id: str = None,
        vsw_id: str = None,
    ):
        # The name of the permission group.
        # 
        # This parameter is required for a General-purpose File Storage NAS (NAS) file system.
        # 
        # The default permission group for virtual private clouds (VPCs) is named DEFAULT_VPC_GROUP_NAME.
        # 
        # This parameter is required.
        self.access_group = access_group
        # The name of the access point.
        self.access_point_name = access_point_name
        # Specifies whether to enable the RAM policy. Valid values:
        # 
        # *   true: The RAM policy is enabled.
        # *   false (default): The RAM policy is disabled.
        # 
        # >  After the RAM policy is enabled for access points, no RAM user is allowed to use access points to mount and access data by default. To use access points to mount and access data as a RAM user, you must grant the related access permissions to the RAM user. If the RAM policy is disabled, access points can be anonymously mounted. For more information about how to configure permissions on access points, see [Configure a policy for the access point](https://help.aliyun.com/document_detail/2545998.html).
        self.enabled_ram = enabled_ram
        # The ID of the file system.
        # 
        # This parameter is required.
        self.file_system_id = file_system_id
        # The ID of the owner group.
        # 
        # This parameter is required if the RootDirectory directory does not exist.
        self.owner_group_id = owner_group_id
        # The owner ID.
        # 
        # This parameter is required if the RootDirectory directory does not exist.
        self.owner_user_id = owner_user_id
        # The Portable Operating System Interface for UNIX (POSIX) permission. Default value: 0777.
        # 
        # This field takes effect only if you specify the OwnerUserId and OwnerGroupId parameters.
        self.permission = permission
        # The ID of the POSIX user group.
        self.posix_group_id = posix_group_id
        # The secondary user group. Separate multiple user group IDs with commas (,).
        self.posix_secondary_group_ids = posix_secondary_group_ids
        # The ID of the POSIX user.
        self.posix_user_id = posix_user_id
        # The root directory of the access point. The default value is /. If the directory does not exist, you must also specify the OwnerUserId and OwnerGroupId parameters.
        self.root_directory = root_directory
        self.tag = tag
        # The VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The vSwitch ID.
        # 
        # This parameter is required.
        self.vsw_id = vsw_id

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_group is not None:
            result['AccessGroup'] = self.access_group

        if self.access_point_name is not None:
            result['AccessPointName'] = self.access_point_name

        if self.enabled_ram is not None:
            result['EnabledRam'] = self.enabled_ram

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.owner_group_id is not None:
            result['OwnerGroupId'] = self.owner_group_id

        if self.owner_user_id is not None:
            result['OwnerUserId'] = self.owner_user_id

        if self.permission is not None:
            result['Permission'] = self.permission

        if self.posix_group_id is not None:
            result['PosixGroupId'] = self.posix_group_id

        if self.posix_secondary_group_ids is not None:
            result['PosixSecondaryGroupIds'] = self.posix_secondary_group_ids

        if self.posix_user_id is not None:
            result['PosixUserId'] = self.posix_user_id

        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vsw_id is not None:
            result['VswId'] = self.vsw_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessGroup') is not None:
            self.access_group = m.get('AccessGroup')

        if m.get('AccessPointName') is not None:
            self.access_point_name = m.get('AccessPointName')

        if m.get('EnabledRam') is not None:
            self.enabled_ram = m.get('EnabledRam')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('OwnerGroupId') is not None:
            self.owner_group_id = m.get('OwnerGroupId')

        if m.get('OwnerUserId') is not None:
            self.owner_user_id = m.get('OwnerUserId')

        if m.get('Permission') is not None:
            self.permission = m.get('Permission')

        if m.get('PosixGroupId') is not None:
            self.posix_group_id = m.get('PosixGroupId')

        if m.get('PosixSecondaryGroupIds') is not None:
            self.posix_secondary_group_ids = m.get('PosixSecondaryGroupIds')

        if m.get('PosixUserId') is not None:
            self.posix_user_id = m.get('PosixUserId')

        if m.get('RootDirectory') is not None:
            self.root_directory = m.get('RootDirectory')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateAccessPointRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VswId') is not None:
            self.vsw_id = m.get('VswId')

        return self

class CreateAccessPointRequestTag(DaraModel):
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

