# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeExcludeSystemPathResponseBody(DaraModel):
    def __init__(
        self,
        exclude_paths: List[main_models.DescribeExcludeSystemPathResponseBodyExcludePaths] = None,
        page_info: main_models.DescribeExcludeSystemPathResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # An array consisting of the directories that are excluded.
        self.exclude_paths = exclude_paths
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.exclude_paths:
            for v1 in self.exclude_paths:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExcludePaths'] = []
        if self.exclude_paths is not None:
            for k1 in self.exclude_paths:
                result['ExcludePaths'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exclude_paths = []
        if m.get('ExcludePaths') is not None:
            for k1 in m.get('ExcludePaths'):
                temp_model = main_models.DescribeExcludeSystemPathResponseBodyExcludePaths()
                self.exclude_paths.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeExcludeSystemPathResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeExcludeSystemPathResponseBodyPageInfo(DaraModel):
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
        # The number of entries returned per page.
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

class DescribeExcludeSystemPathResponseBodyExcludePaths(DaraModel):
    def __init__(
        self,
        os: str = None,
        path: str = None,
    ):
        # The operating system of the server. Valid values:
        # 
        # *   **linux**: Linux
        # *   **windows**: Windows
        self.os = os
        # The absolute path to the directory.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.os is not None:
            result['Os'] = self.os

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

