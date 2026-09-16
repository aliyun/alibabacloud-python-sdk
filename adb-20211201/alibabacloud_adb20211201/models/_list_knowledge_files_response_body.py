# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ListKnowledgeFilesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListKnowledgeFilesResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListKnowledgeFilesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListKnowledgeFilesResponseBodyData(DaraModel):
    def __init__(
        self,
        files: List[main_models.ListKnowledgeFilesResponseBodyDataFiles] = None,
        message: str = None,
        page: int = None,
        page_size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.files = files
        self.message = message
        self.page = page
        self.page_size = page_size
        self.success = success
        self.total = total

    def validate(self):
        if self.files:
            for v1 in self.files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Files'] = []
        if self.files is not None:
            for k1 in self.files:
                result['Files'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.success is not None:
            result['Success'] = self.success

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('Files') is not None:
            for k1 in m.get('Files'):
                temp_model = main_models.ListKnowledgeFilesResponseBodyDataFiles()
                self.files.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListKnowledgeFilesResponseBodyDataFiles(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        file_id: int = None,
        file_size_bytes: int = None,
        file_url: str = None,
        format: str = None,
        is_directory: bool = None,
        owner_file_id: int = None,
        page_count: int = None,
        process_message: str = None,
        process_status: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.file_id = file_id
        self.file_size_bytes = file_size_bytes
        self.file_url = file_url
        self.format = format
        self.is_directory = is_directory
        self.owner_file_id = owner_file_id
        self.page_count = page_count
        self.process_message = process_message
        self.process_status = process_status
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_size_bytes is not None:
            result['FileSizeBytes'] = self.file_size_bytes

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.format is not None:
            result['Format'] = self.format

        if self.is_directory is not None:
            result['IsDirectory'] = self.is_directory

        if self.owner_file_id is not None:
            result['OwnerFileId'] = self.owner_file_id

        if self.page_count is not None:
            result['PageCount'] = self.page_count

        if self.process_message is not None:
            result['ProcessMessage'] = self.process_message

        if self.process_status is not None:
            result['ProcessStatus'] = self.process_status

        if self.updated_at is not None:
            result['UpdatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileSizeBytes') is not None:
            self.file_size_bytes = m.get('FileSizeBytes')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('IsDirectory') is not None:
            self.is_directory = m.get('IsDirectory')

        if m.get('OwnerFileId') is not None:
            self.owner_file_id = m.get('OwnerFileId')

        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')

        if m.get('ProcessMessage') is not None:
            self.process_message = m.get('ProcessMessage')

        if m.get('ProcessStatus') is not None:
            self.process_status = m.get('ProcessStatus')

        if m.get('UpdatedAt') is not None:
            self.updated_at = m.get('UpdatedAt')

        return self

