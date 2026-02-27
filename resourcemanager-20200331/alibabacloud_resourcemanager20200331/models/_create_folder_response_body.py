# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class CreateFolderResponseBody(DaraModel):
    def __init__(
        self,
        folder: main_models.CreateFolderResponseBodyFolder = None,
        request_id: str = None,
    ):
        # The information of the folder.
        self.folder = folder
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.folder:
            self.folder.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder is not None:
            result['Folder'] = self.folder.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folder') is not None:
            temp_model = main_models.CreateFolderResponseBodyFolder()
            self.folder = temp_model.from_map(m.get('Folder'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateFolderResponseBodyFolder(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        parent_folder_id: str = None,
    ):
        # The time when the folder was created.
        self.create_time = create_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        if self.parent_folder_id is not None:
            result['ParentFolderId'] = self.parent_folder_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('ParentFolderId') is not None:
            self.parent_folder_id = m.get('ParentFolderId')

        return self

