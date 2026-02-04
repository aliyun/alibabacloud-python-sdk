# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListFoldersForParentResponseBody(DaraModel):
    def __init__(
        self,
        folders: main_models.ListFoldersForParentResponseBodyFolders = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The folders.
        self.folders = folders
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
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
            temp_model = main_models.ListFoldersForParentResponseBodyFolders()
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

class ListFoldersForParentResponseBodyFolders(DaraModel):
    def __init__(
        self,
        folder: List[main_models.ListFoldersForParentResponseBodyFoldersFolder] = None,
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
                temp_model = main_models.ListFoldersForParentResponseBodyFoldersFolder()
                self.folder.append(temp_model.from_map(k1))

        return self

class ListFoldersForParentResponseBodyFoldersFolder(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        tags: main_models.ListFoldersForParentResponseBodyFoldersFolderTags = None,
    ):
        # The time when the folder was created.
        self.create_time = create_time
        # The ID of the folder.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name
        # The tags added to the folder.
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

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

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('Tags') is not None:
            temp_model = main_models.ListFoldersForParentResponseBodyFoldersFolderTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class ListFoldersForParentResponseBodyFoldersFolderTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.ListFoldersForParentResponseBodyFoldersFolderTagsTag] = None,
    ):
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
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListFoldersForParentResponseBodyFoldersFolderTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListFoldersForParentResponseBodyFoldersFolderTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
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

