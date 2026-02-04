# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListAncestorsResponseBody(DaraModel):
    def __init__(
        self,
        folders: main_models.ListAncestorsResponseBodyFolders = None,
        request_id: str = None,
    ):
        # The information of the folders.
        self.folders = folders
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.folders:
            self.folders.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folders is not None:
            result['Folders'] = self.folders.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folders') is not None:
            temp_model = main_models.ListAncestorsResponseBodyFolders()
            self.folders = temp_model.from_map(m.get('Folders'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAncestorsResponseBodyFolders(DaraModel):
    def __init__(
        self,
        folder: List[main_models.ListAncestorsResponseBodyFoldersFolder] = None,
    ):
        self.folder = folder

    def validate(self):
        if self.folder:
            for v1 in self.folder:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Folder'] = []
        if self.folder is not None:
            for k1 in self.folder:
                result['Folder'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder = []
        if m.get('Folder') is not None:
            for k1 in m.get('Folder'):
                temp_model = main_models.ListAncestorsResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k1))

        return self

class ListAncestorsResponseBodyFoldersFolder(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
    ):
        # The time when the folder was created.
        self.create_time = create_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        return self

