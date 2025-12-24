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
        # The ID of the enterprise drive.
        # 
        # This parameter is required.
        self.cds_id = cds_id
        # The ID of the user who uses the network disk.
        self.end_user_id = end_user_id
        # The file ID. You can call the [ListCdsFiles](https://help.aliyun.com/document_detail/2247622.html) operation to query the ID of the file.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the team space.
        self.group_id = group_id
        # The users that you want to authorize to use the cloud disk.
        # 
        # This parameter is required.
        self.member_list = member_list
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
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
        # The user of the cloud disk.
        # 
        # This parameter is required.
        self.cds_identity = cds_identity
        # Specifies whether the users of the child group can inherit the folder permissions.
        self.disinherit_sub_group = disinherit_sub_group
        # The time when the authorization expires. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. The value never expires. You can specify a value that is predefined by the system for this parameter. Example: 4775500800000.
        self.expire_time = expire_time
        # You can set permissions by specifying roles or by customizing operation permissions. This field is used to set permissions by specifying roles. This field is mutually exclusive with `ActionList`.
        # 
        # Valid values:
        # 
        # *   SystemFileEditorWithoutShareLink: The role that can edit but cannot share files.
        # *   SystemFileUploaderAndDownloaderWithShareLink: The role that can upload, download, and share files.
        # *   SystemFileDownloader: The role that can download files.
        # *   SystemFileEditorWithoutDelete: The role that can edit but cannot edit files.
        # *   SystemFileOwner: The role that can collaborate with others on files.
        # *   SystemFileDownloaderWithShareLink: The role that can download and share files.
        # *   SystemFileUploaderAndViewer: The role that can preview and upload files.
        # *   SystemFileViewer: The role that can preview files.
        # *   SystemFileEditor: The role that can edit files.
        # *   SystemFileUploaderWithShareLink: The role that can upload and share files.
        # *   SystemFileUploader: The role that can upload files.
        # *   SystemFileUploaderAndDownloader: The role that can upload and download files.
        # *   SystemFileMetaViewer: The role that can view file list.
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
        # The ID of the convenience user.
        # 
        # This parameter is required.
        self.id = id
        # The user type.
        # 
        # Set the value to TENANT_ADMIN.
        # 
        # *   IT_Group: group.
        # *   IT_User: user.
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

