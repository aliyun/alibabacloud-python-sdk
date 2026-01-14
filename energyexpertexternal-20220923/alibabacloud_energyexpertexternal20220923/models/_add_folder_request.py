# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddFolderRequest(DaraModel):
    def __init__(
        self,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        # This parameter is required.
        self.folder_name = folder_name
        # This parameter is required.
        self.parent_folder_id = parent_folder_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_name is not None:
            result['folderName'] = self.folder_name

        if self.parent_folder_id is not None:
            result['parentFolderId'] = self.parent_folder_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')

        if m.get('parentFolderId') is not None:
            self.parent_folder_id = m.get('parentFolderId')

        return self

