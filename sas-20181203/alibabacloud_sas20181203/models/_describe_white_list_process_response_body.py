# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWhiteListProcessResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        processes: List[main_models.DescribeWhiteListProcessResponseBodyProcesses] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The information about the processes.
        self.processes = processes
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.processes:
            for v1 in self.processes:
                 if v1:
                    v1.validate()

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

        result['Processes'] = []
        if self.processes is not None:
            for k1 in self.processes:
                result['Processes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        self.processes = []
        if m.get('Processes') is not None:
            for k1 in m.get('Processes'):
                temp_model = main_models.DescribeWhiteListProcessResponseBodyProcesses()
                self.processes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWhiteListProcessResponseBodyProcesses(DaraModel):
    def __init__(
        self,
        file_path: str = None,
        id: int = None,
        level: int = None,
        md_5: str = None,
        process_id: int = None,
        process_name: str = None,
        process_type: int = None,
        status: int = None,
    ):
        # The path to the process startup file.
        self.file_path = file_path
        # The primary key of the process information.
        self.id = id
        # The trust score of the process.
        self.level = level
        # The MD5 hash value of the process startup file.
        self.md_5 = md_5
        # The ID of the process.
        self.process_id = process_id
        # The name of the process.
        self.process_name = process_name
        # The type of the process. Valid values:
        # 
        # *   **1**: trusted
        # *   **2**: suspicious
        # *   **3**: malicious
        self.process_type = process_type
        # Indicates whether the process is trusted. Valid values:
        # 
        # *   **1**: no
        # *   **2**: yes
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.id is not None:
            result['Id'] = self.id

        if self.level is not None:
            result['Level'] = self.level

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        if self.process_name is not None:
            result['ProcessName'] = self.process_name

        if self.process_type is not None:
            result['ProcessType'] = self.process_type

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        if m.get('ProcessName') is not None:
            self.process_name = m.get('ProcessName')

        if m.get('ProcessType') is not None:
            self.process_type = m.get('ProcessType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

