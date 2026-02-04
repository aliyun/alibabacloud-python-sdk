# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizedFoldersResponseBody(DaraModel):
    def __init__(
        self,
        folders: main_models.ListAuthorizedFoldersResponseBodyFolders = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The folders.
        self.folders = folders
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Folders') is not None:
            temp_model = main_models.ListAuthorizedFoldersResponseBodyFolders()
            self.folders = temp_model.from_map(m.get('Folders'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAuthorizedFoldersResponseBodyFolders(DaraModel):
    def __init__(
        self,
        folder: List[main_models.ListAuthorizedFoldersResponseBodyFoldersFolder] = None,
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
                temp_model = main_models.ListAuthorizedFoldersResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k1))

        return self

class ListAuthorizedFoldersResponseBodyFoldersFolder(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        folder_name: str = None,
        resource_directory_path: str = None,
    ):
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name
        # The RDPath of the folder.
        self.resource_directory_path = resource_directory_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')

        return self

