# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class InviteAccountToResourceDirectoryRequest(DaraModel):
    def __init__(
        self,
        note: str = None,
        parent_folder_id: str = None,
        tag: List[main_models.InviteAccountToResourceDirectoryRequestTag] = None,
        target_entity: str = None,
        target_type: str = None,
    ):
        # The description of the invitation.
        # 
        # The description can be up to 1,024 characters in length.
        self.note = note
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The tags.
        self.tag = tag
        # The ID or logon email address of the account that you want to invite.
        # 
        # This parameter is required.
        self.target_entity = target_entity
        # The type of the invited account. Valid values:
        # 
        # *   Account: indicates the ID of the account.
        # *   Email: indicates the logon email address of the account.
        # 
        # This parameter is required.
        self.target_type = target_type

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
        if self.note is not None:
            result['Note'] = self.note

        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.target_entity is not None:
            result['TargetEntity'] = self.target_entity

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.InviteAccountToResourceDirectoryRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TargetEntity') is not None:
            self.target_entity = m.get('TargetEntity')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class InviteAccountToResourceDirectoryRequestTag(DaraModel):
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

