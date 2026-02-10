# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupFilesResponseBody(DaraModel):
    def __init__(
        self,
        backup_files: List[main_models.DescribeBackupFilesResponseBodyBackupFiles] = None,
        page_info: main_models.DescribeBackupFilesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array that consists of the backup files returned.
        self.backup_files = backup_files
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.backup_files:
            for v1 in self.backup_files:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupFiles'] = []
        if self.backup_files is not None:
            for k1 in self.backup_files:
                result['BackupFiles'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_files = []
        if m.get('BackupFiles') is not None:
            for k1 in m.get('BackupFiles'):
                temp_model = main_models.DescribeBackupFilesResponseBodyBackupFiles()
                self.backup_files.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeBackupFilesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBackupFilesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of backup files returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **10**.
        self.page_size = page_size
        # The total number of backup files returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBackupFilesResponseBodyBackupFiles(DaraModel):
    def __init__(
        self,
        name: str = None,
        size: int = None,
        subtree: str = None,
        type: str = None,
    ):
        # The name of the anti-ransomware policy.
        self.name = name
        # The size of the backup file. Unit: bytes.
        self.size = size
        # The path to the subdirectory of the backup file.
        self.subtree = subtree
        # The type of the protected file. Valid values:
        # 
        # *   **file**: files
        # *   **dir**: folders
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.subtree is not None:
            result['Subtree'] = self.subtree

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Subtree') is not None:
            self.subtree = m.get('Subtree')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

