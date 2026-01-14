# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class ChatFolderItem(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        folder_name: str = None,
        sub_folders: List[main_models.ChatItem] = None,
    ):
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.sub_folders = sub_folders

    def validate(self):
        if self.sub_folders:
            for v1 in self.sub_folders:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.folder_name is not None:
            result['folderName'] = self.folder_name

        result['subFolders'] = []
        if self.sub_folders is not None:
            for k1 in self.sub_folders:
                result['subFolders'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')

        self.sub_folders = []
        if m.get('subFolders') is not None:
            for k1 in m.get('subFolders'):
                temp_model = main_models.ChatItem()
                self.sub_folders.append(temp_model.from_map(k1))

        return self

