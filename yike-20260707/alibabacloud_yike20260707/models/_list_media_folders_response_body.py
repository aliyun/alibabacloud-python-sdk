# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yike20260707 import models as main_models
from darabonba.model import DaraModel

class ListMediaFoldersResponseBody(DaraModel):
    def __init__(
        self,
        folder_list: List[main_models.ListMediaFoldersResponseBodyFolderList] = None,
        request_id: str = None,
    ):
        # The list of folders.
        self.folder_list = folder_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.folder_list:
            for v1 in self.folder_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FolderList'] = []
        if self.folder_list is not None:
            for k1 in self.folder_list:
                result['FolderList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folder_list = []
        if m.get('FolderList') is not None:
            for k1 in m.get('FolderList'):
                temp_model = main_models.ListMediaFoldersResponseBodyFolderList()
                self.folder_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListMediaFoldersResponseBodyFolderList(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        folder_id: str = None,
        folder_name: str = None,
        is_default: bool = None,
        modified_time: str = None,
        production_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The folder ID. The ID of the default folder is fixed to `fd_{ProductionId}_default`.
        self.folder_id = folder_id
        # The folder name.
        self.folder_name = folder_name
        # Indicates whether the folder is the default folder. Each project has one and only one default folder.
        self.is_default = is_default
        # The modification time.
        self.modified_time = modified_time
        # The ID of the project to which the folder belongs.
        self.production_id = production_id

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

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.production_id is not None:
            result['ProductionId'] = self.production_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ProductionId') is not None:
            self.production_id = m.get('ProductionId')

        return self

