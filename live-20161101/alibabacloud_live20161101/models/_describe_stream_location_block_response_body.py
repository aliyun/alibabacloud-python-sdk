# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeStreamLocationBlockResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        stream_block_list: main_models.DescribeStreamLocationBlockResponseBodyStreamBlockList = None,
        total_page: int = None,
    ):
        # The total number of entries that meet the specified conditions.
        self.count = count
        # The page number.
        self.page_num = page_num
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The configurations.
        self.stream_block_list = stream_block_list
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.stream_block_list:
            self.stream_block_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.stream_block_list is not None:
            result['StreamBlockList'] = self.stream_block_list.to_map()

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StreamBlockList') is not None:
            temp_model = main_models.DescribeStreamLocationBlockResponseBodyStreamBlockList()
            self.stream_block_list = temp_model.from_map(m.get('StreamBlockList'))

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class DescribeStreamLocationBlockResponseBodyStreamBlockList(DaraModel):
    def __init__(
        self,
        stream_block: List[main_models.DescribeStreamLocationBlockResponseBodyStreamBlockListStreamBlock] = None,
    ):
        self.stream_block = stream_block

    def validate(self):
        if self.stream_block:
            for v1 in self.stream_block:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StreamBlock'] = []
        if self.stream_block is not None:
            for k1 in self.stream_block:
                result['StreamBlock'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.stream_block = []
        if m.get('StreamBlock') is not None:
            for k1 in m.get('StreamBlock'):
                temp_model = main_models.DescribeStreamLocationBlockResponseBodyStreamBlockListStreamBlock()
                self.stream_block.append(temp_model.from_map(k1))

        return self

class DescribeStreamLocationBlockResponseBodyStreamBlockListStreamBlock(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        block_type: str = None,
        domain_name: str = None,
        location_list: str = None,
        release_time: str = None,
        status: int = None,
        stream_name: str = None,
        update_time: str = None,
    ):
        # The name of the application in which the blocking applies.
        self.app_name = app_name
        # The blocking type. Valid values:
        # 
        # *   blacklist
        # *   whitelist
        self.block_type = block_type
        # The accelerated domain name.
        self.domain_name = domain_name
        # The blocked region. If multiple regions are specified, such as CN and AS, they are separated by commas (,).
        self.location_list = location_list
        # The time when the blocking ends. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.release_time = release_time
        # The blocking status. Valid values: 0 (not started), 1 (blocking), 2 (successful), 3 (failed), 4 (expired), and 5 (deleting).
        self.status = status
        # The name of the stream.
        self.stream_name = stream_name
        # The time when the configuration was last modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.block_type is not None:
            result['BlockType'] = self.block_type

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.location_list is not None:
            result['LocationList'] = self.location_list

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.status is not None:
            result['Status'] = self.status

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('BlockType') is not None:
            self.block_type = m.get('BlockType')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('LocationList') is not None:
            self.location_list = m.get('LocationList')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

