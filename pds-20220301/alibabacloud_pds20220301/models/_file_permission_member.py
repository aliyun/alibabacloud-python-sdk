# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class FilePermissionMember(DaraModel):
    def __init__(
        self,
        action_list: List[str] = None,
        disinherit_sub_group: bool = None,
        expire_time: int = None,
        identity: main_models.Identity = None,
        role_id: str = None,
    ):
        # The list of permissions to grant. You can grant permissions by assigning roles to identities, or you can customize the permissions. To grant permissions by assigning roles to identities, specify role_id. role_id and action_list are mutually exclusive. If both parameters are specified, the value of role_id prevails. When you specify action_list, the system automatically generates a temporary role_id. You can use this role_id to revoke the permissions.
        self.action_list = action_list
        # Specifies whether the users of subgroups can inherit the permissions. For example, a user named user1 belongs to the group1 group, and a user named user2 belongs to the group2 group. group2 is the subgroup of group1. If you set disinherit_sub_group to true, only user1 is granted the permissions. user2 is not granted the permissions.
        self.disinherit_sub_group = disinherit_sub_group
        # The time when the permissions expire. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC. A value of 4775500800000 indicates that the permissions never expire.
        self.expire_time = expire_time
        # The identity to which the permissions are granted, which is a user or a group.
        self.identity = identity
        # The role ID. You can grant permissions by assigning roles to identities, or you can customize the permissions. To grant permissions by assigning roles to identities, specify role_id. role_id and action_list are mutually exclusive. If both parameters are specified, the value of role_id prevails.
        # 
        # Valid values:
        # 
        # SystemFileOwner: collaborator
        # 
        # SystemFileDownloader: downloader
        # 
        # SystemFileEditor: editor
        # 
        # SystemFileEditorWithoutDelete: editor without permissions to delete the file
        # 
        # SystemFileEditorWithoutShareLink: editor without permissions to share the file
        # 
        # SystemFileMetaViewer: viewer of lists
        # 
        # SystemFileUploader: uploader. SystemFileUploaderAndDownloader: uploader and downloader
        # 
        # SystemFileDownloaderWithShareLink: downloader and sharer
        # 
        # SystemFileUploaderAndDownloaderWithShareLink: uploader, downloader, and sharer
        # 
        # SystemFileUploaderAndViewer: viewer and uploader
        # 
        # SystemFileUploaderWithShareLink: uploader and sharer
        # 
        # SystemFileViewer: viewer
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_list is not None:
            result['action_list'] = self.action_list

        if self.disinherit_sub_group is not None:
            result['disinherit_sub_group'] = self.disinherit_sub_group

        if self.expire_time is not None:
            result['expire_time'] = self.expire_time

        if self.identity is not None:
            result['identity'] = self.identity.to_map()

        if self.role_id is not None:
            result['role_id'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')

        if m.get('disinherit_sub_group') is not None:
            self.disinherit_sub_group = m.get('disinherit_sub_group')

        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')

        if m.get('identity') is not None:
            temp_model = main_models.Identity()
            self.identity = temp_model.from_map(m.get('identity'))

        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        return self

