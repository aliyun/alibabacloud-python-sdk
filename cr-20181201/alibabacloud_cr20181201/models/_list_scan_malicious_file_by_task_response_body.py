# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ListScanMaliciousFileByTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        scan_malicious_files: List[main_models.ListScanMaliciousFileByTaskResponseBodyScanMaliciousFiles] = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried malicious files.
        self.scan_malicious_files = scan_malicious_files
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.scan_malicious_files:
            for v1 in self.scan_malicious_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.is_success is not None:
            result['IsSuccess'] = self.is_success

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScanMaliciousFiles'] = []
        if self.scan_malicious_files is not None:
            for k1 in self.scan_malicious_files:
                result['ScanMaliciousFiles'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scan_malicious_files = []
        if m.get('ScanMaliciousFiles') is not None:
            for k1 in m.get('ScanMaliciousFiles'):
                temp_model = main_models.ListScanMaliciousFileByTaskResponseBodyScanMaliciousFiles()
                self.scan_malicious_files.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListScanMaliciousFileByTaskResponseBodyScanMaliciousFiles(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        file_path: str = None,
        first_scan_time: int = None,
        level: str = None,
        malicious_md_5: str = None,
        malicious_name: str = None,
        scan_task_id: str = None,
        update_time: int = None,
    ):
        # The time when the image was created.
        self.create_time = create_time
        # The path of the file.
        self.file_path = file_path
        # The time when the image was first scanned.
        self.first_scan_time = first_scan_time
        # The severity of the malicious file.
        self.level = level
        # The MD5 hash value of the malicious file.
        self.malicious_md_5 = malicious_md_5
        # The type of the malicious file.
        self.malicious_name = malicious_name
        # The ID of the image scan task.
        self.scan_task_id = scan_task_id
        # The time when the image was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time

        if self.level is not None:
            result['Level'] = self.level

        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5

        if self.malicious_name is not None:
            result['MaliciousName'] = self.malicious_name

        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')

        if m.get('MaliciousName') is not None:
            self.malicious_name = m.get('MaliciousName')

        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

