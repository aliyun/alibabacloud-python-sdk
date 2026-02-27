# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateFolderRequest(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        new_folder_name: str = None,
    ):
        # The ID of the folder.
        # 
        # This parameter is required.
        self.folder_id = folder_id
        # The new name of the folder.
        # 
        # The name must be 1 to 24 characters in length and can contain letters, digits, underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.new_folder_name = new_folder_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.new_folder_name is not None:
            result['NewFolderName'] = self.new_folder_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('NewFolderName') is not None:
            self.new_folder_name = m.get('NewFolderName')

        return self

