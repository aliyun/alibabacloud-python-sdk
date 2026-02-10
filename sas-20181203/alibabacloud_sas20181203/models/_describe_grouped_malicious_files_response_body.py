# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupedMaliciousFilesResponseBody(DaraModel):
    def __init__(
        self,
        grouped_malicious_file_response: List[main_models.DescribeGroupedMaliciousFilesResponseBodyGroupedMaliciousFileResponse] = None,
        page_info: main_models.DescribeGroupedMaliciousFilesResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The details of the malicious image sample.
        self.grouped_malicious_file_response = grouped_malicious_file_response
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.grouped_malicious_file_response:
            for v1 in self.grouped_malicious_file_response:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GroupedMaliciousFileResponse'] = []
        if self.grouped_malicious_file_response is not None:
            for k1 in self.grouped_malicious_file_response:
                result['GroupedMaliciousFileResponse'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.grouped_malicious_file_response = []
        if m.get('GroupedMaliciousFileResponse') is not None:
            for k1 in m.get('GroupedMaliciousFileResponse'):
                temp_model = main_models.DescribeGroupedMaliciousFilesResponseBodyGroupedMaliciousFileResponse()
                self.grouped_malicious_file_response.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeGroupedMaliciousFilesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeGroupedMaliciousFilesResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The total number of entries returned.
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

class DescribeGroupedMaliciousFilesResponseBodyGroupedMaliciousFileResponse(DaraModel):
    def __init__(
        self,
        first_scan_timestamp: int = None,
        image_count: int = None,
        latest_scan_timestamp: int = None,
        level: str = None,
        malicious_key: str = None,
        malicious_md_5: str = None,
        malicious_name: str = None,
        status: int = None,
    ):
        # The timestamp generated when the first scan was performed. Unit: milliseconds.
        self.first_scan_timestamp = first_scan_timestamp
        # The number of affected images.
        self.image_count = image_count
        # The timestamp generated when the last scan was performed. Unit: milliseconds.
        self.latest_scan_timestamp = latest_scan_timestamp
        # The severity of the malicious image sample. Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.level = level
        # The keyword of the malicious image sample.
        self.malicious_key = malicious_key
        # The MD5 hash value of the malicious image sample.
        self.malicious_md_5 = malicious_md_5
        # The name of the malicious image sample.
        self.malicious_name = malicious_name
        # The handling status of the malicious image sample. Valid values:
        # 
        # *   **0**: unhandled
        # *   **1**: handled
        # *   **2**: verifying
        # *   **3**: whitelisted
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_scan_timestamp is not None:
            result['FirstScanTimestamp'] = self.first_scan_timestamp

        if self.image_count is not None:
            result['ImageCount'] = self.image_count

        if self.latest_scan_timestamp is not None:
            result['LatestScanTimestamp'] = self.latest_scan_timestamp

        if self.level is not None:
            result['Level'] = self.level

        if self.malicious_key is not None:
            result['MaliciousKey'] = self.malicious_key

        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5

        if self.malicious_name is not None:
            result['MaliciousName'] = self.malicious_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstScanTimestamp') is not None:
            self.first_scan_timestamp = m.get('FirstScanTimestamp')

        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')

        if m.get('LatestScanTimestamp') is not None:
            self.latest_scan_timestamp = m.get('LatestScanTimestamp')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MaliciousKey') is not None:
            self.malicious_key = m.get('MaliciousKey')

        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')

        if m.get('MaliciousName') is not None:
            self.malicious_name = m.get('MaliciousName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

