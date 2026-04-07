# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListDataServiceFoldersResponseBody(DaraModel):
    def __init__(
        self,
        folder_paging_result: main_models.ListDataServiceFoldersResponseBodyFolderPagingResult = None,
        request_id: str = None,
    ):
        # The paging result for the folders.
        self.folder_paging_result = folder_paging_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.folder_paging_result:
            self.folder_paging_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_paging_result is not None:
            result['FolderPagingResult'] = self.folder_paging_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderPagingResult') is not None:
            temp_model = main_models.ListDataServiceFoldersResponseBodyFolderPagingResult()
            self.folder_paging_result = temp_model.from_map(m.get('FolderPagingResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataServiceFoldersResponseBodyFolderPagingResult(DaraModel):
    def __init__(
        self,
        folders: List[main_models.ListDataServiceFoldersResponseBodyFolderPagingResultFolders] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The folders.
        self.folders = folders
        # The page number. The value of this parameter is the same as that of the PageNumber parameter in the request.
        self.page_number = page_number
        # The number of entries per page. Default value: 10. Maximum value: 100.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.folders:
            for v1 in self.folders:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Folders'] = []
        if self.folders is not None:
            for k1 in self.folders:
                result['Folders'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.folders = []
        if m.get('Folders') is not None:
            for k1 in m.get('Folders'):
                temp_model = main_models.ListDataServiceFoldersResponseBodyFolderPagingResultFolders()
                self.folders.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDataServiceFoldersResponseBodyFolderPagingResultFolders(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        folder_id: int = None,
        folder_name: str = None,
        group_id: str = None,
        modified_time: str = None,
        parent_id: int = None,
        project_id: int = None,
        tenant_id: int = None,
    ):
        # The time when the folder was created.
        self.created_time = created_time
        # The folder ID.
        self.folder_id = folder_id
        # The name of the folder.
        self.folder_name = folder_name
        # The ID of the business process to which the folder belongs.
        self.group_id = group_id
        # The time when the folder was last modified.
        self.modified_time = modified_time
        # The ID of the parent folder. The ID of the root folder in a business process is 0, and the ID of a folder created by a user in a business process is greater than 0.
        self.parent_id = parent_id
        # The workspace ID.
        self.project_id = project_id
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.folder_name is not None:
            result['FolderName'] = self.folder_name

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderName') is not None:
            self.folder_name = m.get('FolderName')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

