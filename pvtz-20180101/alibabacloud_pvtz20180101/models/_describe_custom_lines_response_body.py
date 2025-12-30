# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomLinesResponseBody(DaraModel):
    def __init__(
        self,
        custom_lines: main_models.DescribeCustomLinesResponseBodyCustomLines = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_items: int = None,
        total_pages: int = None,
    ):
        # The custom lines.
        self.custom_lines = custom_lines
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **1 to 100**. Default value: **10**.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_items = total_items
        # The total number of returned pages.
        self.total_pages = total_pages

    def validate(self):
        if self.custom_lines:
            self.custom_lines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_lines is not None:
            result['CustomLines'] = self.custom_lines.to_map()

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
        if m.get('CustomLines') is not None:
            temp_model = main_models.DescribeCustomLinesResponseBodyCustomLines()
            self.custom_lines = temp_model.from_map(m.get('CustomLines'))

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
        custom_line: List[main_models.DescribeCustomLinesResponseBodyCustomLinesCustomLine] = None,
    ):
        self.custom_line = custom_line

    def validate(self):
        if self.custom_line:
            for v1 in self.custom_line:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomLine'] = []
        if self.custom_line is not None:
            for k1 in self.custom_line:
                result['CustomLine'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_line = []
        if m.get('CustomLine') is not None:
            for k1 in m.get('CustomLine'):
                temp_model = main_models.DescribeCustomLinesResponseBodyCustomLinesCustomLine()
                self.custom_line.append(temp_model.from_map(k1))

        return self

class DescribeCustomLinesResponseBodyCustomLinesCustomLine(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        create_timestamp: int = None,
        creator: str = None,
        creator_sub_type: str = None,
        creator_type: str = None,
        dns_category: str = None,
        ipv_4s: main_models.DescribeCustomLinesResponseBodyCustomLinesCustomLineIpv4s = None,
        line_id: str = None,
        name: str = None,
        update_time: str = None,
        update_timestamp: int = None,
    ):
        # The time when the custom line was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the custom line was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.create_timestamp = create_timestamp
        # The creator of the custom line.
        self.creator = creator
        # The type of the creator for the custom line. Valid values:
        # 
        # *   CUSTOM: Alibaba Cloud account
        # *   SUB: RAM user
        # *   STS: assumed role that obtains the Security Token Service (STS) token of a RAM role
        # *   OTHER: other roles
        self.creator_sub_type = creator_sub_type
        # The role of the creator for the custom line. Valid values:
        # 
        # *   USER: user
        # *   SYSTEM: system
        self.creator_type = creator_type
        self.dns_category = dns_category
        # The IPv4 CIDR blocks.
        self.ipv_4s = ipv_4s
        # The unique ID of the custom line.
        self.line_id = line_id
        # The name of the custom line.
        self.name = name
        # The time when the custom line was updated. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time
        # The time when the custom line was updated. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.update_timestamp = update_timestamp

    def validate(self):
        if self.ipv_4s:
            self.ipv_4s.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_sub_type is not None:
            result['CreatorSubType'] = self.creator_sub_type

        if self.creator_type is not None:
            result['CreatorType'] = self.creator_type

        if self.dns_category is not None:
            result['DnsCategory'] = self.dns_category

        if self.ipv_4s is not None:
            result['Ipv4s'] = self.ipv_4s.to_map()

        if self.line_id is not None:
            result['LineId'] = self.line_id

        if self.name is not None:
            result['Name'] = self.name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_timestamp is not None:
            result['UpdateTimestamp'] = self.update_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorSubType') is not None:
            self.creator_sub_type = m.get('CreatorSubType')

        if m.get('CreatorType') is not None:
            self.creator_type = m.get('CreatorType')

        if m.get('DnsCategory') is not None:
            self.dns_category = m.get('DnsCategory')

        if m.get('Ipv4s') is not None:
            temp_model = main_models.DescribeCustomLinesResponseBodyCustomLinesCustomLineIpv4s()
            self.ipv_4s = temp_model.from_map(m.get('Ipv4s'))

        if m.get('LineId') is not None:
            self.line_id = m.get('LineId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateTimestamp') is not None:
            self.update_timestamp = m.get('UpdateTimestamp')

        return self

class DescribeCustomLinesResponseBodyCustomLinesCustomLineIpv4s(DaraModel):
    def __init__(
        self,
        ipv_4: List[str] = None,
    ):
        self.ipv_4 = ipv_4

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ipv_4 is not None:
            result['Ipv4'] = self.ipv_4

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ipv4') is not None:
            self.ipv_4 = m.get('Ipv4')

        return self

