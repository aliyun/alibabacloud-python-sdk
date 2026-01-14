# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class FolderItem(DaraModel):
    def __init__(
        self,
        current_level: int = None,
        doc_count: int = None,
        folder_default: int = None,
        folder_id: str = None,
        folder_name: str = None,
        folder_num: int = None,
        oss_domain: str = None,
        oss_path: str = None,
        oss_update_by: str = None,
        parent_folder_id: str = None,
        resource_path: str = None,
        storage_type: int = None,
        sub_folder_list: List[main_models.FolderItem] = None,
        sync_parsing_status: int = None,
        sync_status: int = None,
        task_id: int = None,
    ):
        self.current_level = current_level
        self.doc_count = doc_count
        self.folder_default = folder_default
        self.folder_id = folder_id
        self.folder_name = folder_name
        self.folder_num = folder_num
        self.oss_domain = oss_domain
        self.oss_path = oss_path
        self.oss_update_by = oss_update_by
        self.parent_folder_id = parent_folder_id
        self.resource_path = resource_path
        self.storage_type = storage_type
        self.sub_folder_list = sub_folder_list
        self.sync_parsing_status = sync_parsing_status
        self.sync_status = sync_status
        self.task_id = task_id

    def validate(self):
        if self.sub_folder_list:
            for v1 in self.sub_folder_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_level is not None:
            result['currentLevel'] = self.current_level

        if self.doc_count is not None:
            result['docCount'] = self.doc_count

        if self.folder_default is not None:
            result['folderDefault'] = self.folder_default

        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.folder_name is not None:
            result['folderName'] = self.folder_name

        if self.folder_num is not None:
            result['folderNum'] = self.folder_num

        if self.oss_domain is not None:
            result['ossDomain'] = self.oss_domain

        if self.oss_path is not None:
            result['ossPath'] = self.oss_path

        if self.oss_update_by is not None:
            result['ossUpdateBy'] = self.oss_update_by

        if self.parent_folder_id is not None:
            result['parentFolderId'] = self.parent_folder_id

        if self.resource_path is not None:
            result['resourcePath'] = self.resource_path

        if self.storage_type is not None:
            result['storageType'] = self.storage_type

        result['subFolderList'] = []
        if self.sub_folder_list is not None:
            for k1 in self.sub_folder_list:
                result['subFolderList'].append(k1.to_map() if k1 else None)

        if self.sync_parsing_status is not None:
            result['syncParsingStatus'] = self.sync_parsing_status

        if self.sync_status is not None:
            result['syncStatus'] = self.sync_status

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentLevel') is not None:
            self.current_level = m.get('currentLevel')

        if m.get('docCount') is not None:
            self.doc_count = m.get('docCount')

        if m.get('folderDefault') is not None:
            self.folder_default = m.get('folderDefault')

        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('folderName') is not None:
            self.folder_name = m.get('folderName')

        if m.get('folderNum') is not None:
            self.folder_num = m.get('folderNum')

        if m.get('ossDomain') is not None:
            self.oss_domain = m.get('ossDomain')

        if m.get('ossPath') is not None:
            self.oss_path = m.get('ossPath')

        if m.get('ossUpdateBy') is not None:
            self.oss_update_by = m.get('ossUpdateBy')

        if m.get('parentFolderId') is not None:
            self.parent_folder_id = m.get('parentFolderId')

        if m.get('resourcePath') is not None:
            self.resource_path = m.get('resourcePath')

        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')

        self.sub_folder_list = []
        if m.get('subFolderList') is not None:
            for k1 in m.get('subFolderList'):
                temp_model = main_models.FolderItem()
                self.sub_folder_list.append(temp_model.from_map(k1))

        if m.get('syncParsingStatus') is not None:
            self.sync_parsing_status = m.get('syncParsingStatus')

        if m.get('syncStatus') is not None:
            self.sync_status = m.get('syncStatus')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

