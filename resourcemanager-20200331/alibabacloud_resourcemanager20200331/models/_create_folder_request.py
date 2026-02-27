# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateFolderRequest(DaraModel):
    def __init__(
        self,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        # The name of the folder.
        # 
        # The name must be 1 to 24 characters in length and can contain letters, digits, underscores (_), periods (.),and hyphens (-).
        # 
        # This parameter is required.
        self.folder_name = folder_name
        # The ID of the parent folder.
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')

        return self

