# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomLinesResponseBody(DaraModel):
    def __init__(
        self,
        custom_lines: List[main_models.DescribeCustomLinesResponseBodyCustomLines] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The custom lines.
        self.custom_lines = custom_lines
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of custom lines.
        self.total_items = total_items
        # The total number of pages returned.
        self.total_pages = total_pages

    def validate(self):
        if self.custom_lines:
            for v1 in self.custom_lines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomLines'] = []
        if self.custom_lines is not None:
            for k1 in self.custom_lines:
                result['CustomLines'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_items is not None:
            result['TotalItems'] = self.total_items

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_lines = []
        if m.get('CustomLines') is not None:
            for k1 in m.get('CustomLines'):
                temp_model = main_models.DescribeCustomLinesResponseBodyCustomLines()
                self.custom_lines.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalItems') is not None:
            self.total_items = m.get('TotalItems')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeCustomLinesResponseBodyCustomLines(DaraModel):
    def __init__(
        self,
        code: str = None,
        id: int = None,
        ip_segment_list: List[main_models.DescribeCustomLinesResponseBodyCustomLinesIpSegmentList] = None,
        name: str = None,
    ):
        # The code of the custom line.
        self.code = code
        # The unique ID of the custom line.
        self.id = id
        self.ip_segment_list = ip_segment_list
        # The name of the custom line.
        self.name = name

    def validate(self):
        if self.ip_segment_list:
            for v1 in self.ip_segment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        result['IpSegmentList'] = []
        if self.ip_segment_list is not None:
            for k1 in self.ip_segment_list:
                result['IpSegmentList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.ip_segment_list = []
        if m.get('IpSegmentList') is not None:
            for k1 in m.get('IpSegmentList'):
                temp_model = main_models.DescribeCustomLinesResponseBodyCustomLinesIpSegmentList()
                self.ip_segment_list.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeCustomLinesResponseBodyCustomLinesIpSegmentList(DaraModel):
    def __init__(
        self,
        end_ip: str = None,
        start_ip: str = None,
    ):
        self.end_ip = end_ip
        self.start_ip = start_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_ip is not None:
            result['EndIp'] = self.end_ip

        if self.start_ip is not None:
            result['StartIp'] = self.start_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndIp') is not None:
            self.end_ip = m.get('EndIp')

        if m.get('StartIp') is not None:
            self.start_ip = m.get('StartIp')

        return self

