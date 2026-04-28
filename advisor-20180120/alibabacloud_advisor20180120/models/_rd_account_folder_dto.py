# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class RdAccountFolderDTO(DaraModel):
    def __init__(
        self,
        account_count: int = None,
        account_list: List[main_models.RdAccountDTO] = None,
        folder_id: str = None,
        folder_list: List[main_models.RdAccountFolderDTO] = None,
        folder_name: str = None,
        resource_directory_id: str = None,
        resource_directory_path: str = None,
        resource_directory_path_name: str = None,
        selected_count: int = None,
    ):
        self.account_count = account_count
        self.account_list = account_list
        self.folder_id = folder_id
        self.folder_list = folder_list
        self.folder_name = folder_name
        self.resource_directory_id = resource_directory_id
        self.resource_directory_path = resource_directory_path
        self.resource_directory_path_name = resource_directory_path_name
        self.selected_count = selected_count

    def validate(self):
        if self.account_list:
            for v1 in self.account_list:
                 if v1:
                    v1.validate()
        if self.folder_list:
            for v1 in self.folder_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_count is not None:
            result['AccountCount'] = self.account_count

        result['AccountList'] = []
        if self.account_list is not None:
            for k1 in self.account_list:
                result['AccountList'].append(k1.to_map() if k1 else None)

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        result['FolderList'] = []
        if self.folder_list is not None:
            for k1 in self.folder_list:
                result['FolderList'].append(k1.to_map() if k1 else None)

        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        if self.resource_directory_id is not None:
            result['ResourceDirectoryId'] = self.resource_directory_id

        if self.resource_directory_path is not None:
            result['ResourceDirectoryPath'] = self.resource_directory_path

        if self.resource_directory_path_name is not None:
            result['ResourceDirectoryPathName'] = self.resource_directory_path_name

        if self.selected_count is not None:
            result['SelectedCount'] = self.selected_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountCount') is not None:
            self.account_count = m.get('AccountCount')

        self.account_list = []
        if m.get('AccountList') is not None:
            for k1 in m.get('AccountList'):
                temp_model = main_models.RdAccountDTO()
                self.account_list.append(temp_model.from_map(k1))

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        self.folder_list = []
        if m.get('FolderList') is not None:
            for k1 in m.get('FolderList'):
                temp_model = main_models.RdAccountFolderDTO()
                self.folder_list.append(temp_model.from_map(k1))

        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('ResourceDirectoryId') is not None:
            self.resource_directory_id = m.get('ResourceDirectoryId')

        if m.get('ResourceDirectoryPath') is not None:
            self.resource_directory_path = m.get('ResourceDirectoryPath')

        if m.get('ResourceDirectoryPathName') is not None:
            self.resource_directory_path_name = m.get('ResourceDirectoryPathName')

        if m.get('SelectedCount') is not None:
            self.selected_count = m.get('SelectedCount')

        return self

