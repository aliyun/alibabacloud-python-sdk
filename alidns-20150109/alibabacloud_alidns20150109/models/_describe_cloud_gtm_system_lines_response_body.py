# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCloudGtmSystemLinesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        system_lines: main_models.DescribeCloudGtmSystemLinesResponseBodySystemLines = None,
        system_lines_tree: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The system lines.
        self.system_lines = system_lines
        # The system lines, which are in a tree structure. Only a system line is listed in this example.
        self.system_lines_tree = system_lines_tree

    def validate(self):
        if self.system_lines:
            self.system_lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.system_lines is not None:
            result['SystemLines'] = self.system_lines.to_map()

        if self.system_lines_tree is not None:
            result['SystemLinesTree'] = self.system_lines_tree

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SystemLines') is not None:
            temp_model = main_models.DescribeCloudGtmSystemLinesResponseBodySystemLines()
            self.system_lines = temp_model.from_map(m.get('SystemLines'))

        if m.get('SystemLinesTree') is not None:
            self.system_lines_tree = m.get('SystemLinesTree')

        return self

class DescribeCloudGtmSystemLinesResponseBodySystemLines(DaraModel):
    def __init__(
        self,
        system_line: List[main_models.DescribeCloudGtmSystemLinesResponseBodySystemLinesSystemLine] = None,
    ):
        self.system_line = system_line

    def validate(self):
        if self.system_line:
            for v1 in self.system_line:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SystemLine'] = []
        if self.system_line is not None:
            for k1 in self.system_line:
                result['SystemLine'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.system_line = []
        if m.get('SystemLine') is not None:
            for k1 in m.get('SystemLine'):
                temp_model = main_models.DescribeCloudGtmSystemLinesResponseBodySystemLinesSystemLine()
                self.system_line.append(temp_model.from_map(k1))

        return self

class DescribeCloudGtmSystemLinesResponseBodySystemLinesSystemLine(DaraModel):
    def __init__(
        self,
        code: str = None,
        display_name: str = None,
        is_available: bool = None,
        name: str = None,
        parent_code: str = None,
    ):
        # The line code.
        self.code = code
        # The display name of the line.
        self.display_name = display_name
        # Indicates whether the line can be selected as the source of a Domain Name System (DNS) request. Valid values:
        # 
        # *   true
        # *   false
        self.is_available = is_available
        # The name of the line.
        self.name = name
        # The code of the parent line.
        self.parent_code = parent_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.is_available is not None:
            result['IsAvailable'] = self.is_available

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_code is not None:
            result['ParentCode'] = self.parent_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('IsAvailable') is not None:
            self.is_available = m.get('IsAvailable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentCode') is not None:
            self.parent_code = m.get('ParentCode')

        return self

