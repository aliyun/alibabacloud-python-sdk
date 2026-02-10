# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class FilePermissionMember(DaraModel):
    def __init__(
        self,
        cds_identity: main_models.FilePermissionMemberCdsIdentity = None,
        disinherit_sub_group: bool = None,
        expire_time: int = None,
        role_id: str = None,
    ):
        # The object that you want to grant permissions. The object can be a user or a group.
        # 
        # This parameter is required.
        self.cds_identity = cds_identity
        # Indicates whether to disable the permission from users in the subgroup.
        self.disinherit_sub_group = disinherit_sub_group
        # The expiration time. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC
        self.expire_time = expire_time
        # The role.
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
            temp_model = main_models.FilePermissionMemberCdsIdentity()
            self.cds_identity = temp_model.from_map(m.get('CdsIdentity'))

        if m.get('DisinheritSubGroup') is not None:
            self.disinherit_sub_group = m.get('DisinheritSubGroup')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        return self



class FilePermissionMemberCdsIdentity(DaraModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        # The user ID or a team ID.
        # 
        # This parameter is required.
        self.id = id
        # The object type.
        # 
        # Valid values:
        # 
        # *   IT_Group: team
        # *   IT_User: user
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

