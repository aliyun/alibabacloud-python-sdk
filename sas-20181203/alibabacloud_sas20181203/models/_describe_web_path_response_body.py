# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeWebPathResponseBody(DaraModel):
    def __init__(
        self,
        config_list: List[main_models.DescribeWebPathResponseBodyConfigList] = None,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the paths to the web directories.
        self.config_list = config_list
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.config_list:
            for v1 in self.config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigList'] = []
        if self.config_list is not None:
            for k1 in self.config_list:
                result['ConfigList'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k1 in m.get('ConfigList'):
                temp_model = main_models.DescribeWebPathResponseBodyConfigList()
                self.config_list.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeWebPathResponseBodyConfigList(DaraModel):
    def __init__(
        self,
        target_list: List[main_models.DescribeWebPathResponseBodyConfigListTargetList] = None,
        web_path: str = None,
        web_path_type: str = None,
    ):
        # An array consisting of the servers on which the web directories are scanned.
        self.target_list = target_list
        # The path to the web directory.
        self.web_path = web_path
        # The path type of the web directory. Valid values:
        # 
        # *   **def**: automatically identified
        # *   **customize**: manually added
        self.web_path_type = web_path_type

    def validate(self):
        if self.target_list:
            for v1 in self.target_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TargetList'] = []
        if self.target_list is not None:
            for k1 in self.target_list:
                result['TargetList'].append(k1.to_map() if k1 else None)

        if self.web_path is not None:
            result['WebPath'] = self.web_path

        if self.web_path_type is not None:
            result['WebPathType'] = self.web_path_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.target_list = []
        if m.get('TargetList') is not None:
            for k1 in m.get('TargetList'):
                temp_model = main_models.DescribeWebPathResponseBodyConfigListTargetList()
                self.target_list.append(temp_model.from_map(k1))

        if m.get('WebPath') is not None:
            self.web_path = m.get('WebPath')

        if m.get('WebPathType') is not None:
            self.web_path_type = m.get('WebPathType')

        return self

class DescribeWebPathResponseBodyConfigListTargetList(DaraModel):
    def __init__(
        self,
        target: str = None,
        target_type: str = None,
    ):
        # The object.
        self.target = target
        # The object type. Valid values:
        # 
        # *   **uuid**
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target is not None:
            result['Target'] = self.target

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Target') is not None:
            self.target = m.get('Target')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

