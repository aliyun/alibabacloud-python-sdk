# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class CreateFolderRequest(DaraModel):
    def __init__(
        self,
        folder_name: str = None,
        parent_folder_id: str = None,
        tag: List[main_models.CreateFolderRequestTag] = None,
    ):
        # The name of the folder.
        # 
        # The name must be 1 to 24 characters in length and can contain letters, digits, underscores (_), periods (.),and hyphens (-).
        # 
        # This parameter is required.
        self.folder_name = folder_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id
        # The tag to add to the folder.
        self.tag = tag

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
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateFolderRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateFolderRequestTag(DaraModel):
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

