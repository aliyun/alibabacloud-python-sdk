# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListFoldersResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListFoldersResponseBodyData = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of folders that meet the conditions.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. Used to troubleshoot errors.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: success.
        # *   false: failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListFoldersResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListFoldersResponseBodyData(DaraModel):
    def __init__(
        self,
        folders: List[main_models.ListFoldersResponseBodyDataFolders] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of folders.
        self.folders = folders
        # The current page number.
        self.page_number = page_number
        # The number of records on the current page.
        self.page_size = page_size
        # The total number of records that meet the query conditions.
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
                temp_model = main_models.ListFoldersResponseBodyDataFolders()
                self.folders.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFoldersResponseBodyDataFolders(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        folder_path: str = None,
    ):
        # The folder ID.
        self.folder_id = folder_id
        # The folder path.
        self.folder_path = folder_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['FolderId'] = self.folder_id

        if self.folder_path is not None:
            result['FolderPath'] = self.folder_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FolderId') is not None:
            self.folder_id = m.get('FolderId')

        if m.get('FolderPath') is not None:
            self.folder_path = m.get('FolderPath')

        return self

