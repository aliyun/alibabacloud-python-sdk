# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class FileRemovePermissionRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        member_list: List[main_models.FileRemovePermissionRequestMemberList] = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The identities with whom the file is shared.
        # 
        # This parameter is required.
        self.member_list = member_list

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
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.file_id is not None:
            result['file_id'] = self.file_id

        result['member_list'] = []
        if self.member_list is not None:
            for k1 in self.member_list:
                result['member_list'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')

        self.member_list = []
        if m.get('member_list') is not None:
            for k1 in m.get('member_list'):
                temp_model = main_models.FileRemovePermissionRequestMemberList()
                self.member_list.append(temp_model.from_map(k1))

        return self

class FileRemovePermissionRequestMemberList(DaraModel):
    def __init__(
        self,
        identity: main_models.Identity = None,
        role_id: str = None,
    ):
        # The identity to whom the permissions are granted, which is a user or a group.
        # 
        # This parameter is required.
        self.identity = identity
        # The role ID. You can grant permissions by assigning roles to identities, or you can customize the permissions. To grant permissions by assigning roles to identities, specify role_id. role_id and action_list are mutually exclusive. If both parameters are specified, role_id has a higher priority.
        # 
        # Valid values:
        # 
        # SystemFileOwner: collaborator.
        # 
        # SystemFileDownloader: downloader.
        # 
        # SystemFileEditor: editor.
        # 
        # SystemFileEditorWithoutDelete: editor without permissions to delete the file.
        # 
        # SystemFileEditorWithoutShareLink: editor without permissions to share the file.
        # 
        # SystemFileMetaViewer: viewer of lists.
        # 
        # SystemFileUploader: uploader. SystemFileUploaderAndDownloader: uploader and downloader.
        # 
        # SystemFileDownloaderWithShareLink: downloader and sharer.
        # 
        # SystemFileUploaderAndDownloaderWithShareLink: uploader, downloader, and sharer.
        # 
        # SystemFileUploaderAndViewer: viewer and uploader.
        # 
        # SystemFileUploaderWithShareLink: uploader and sharer.
        # 
        # SystemFileViewer: viewer.
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identity is not None:
            result['identity'] = self.identity.to_map()

        if self.role_id is not None:
            result['role_id'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity') is not None:
            temp_model = main_models.Identity()
            self.identity = temp_model.from_map(m.get('identity'))

        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        return self

