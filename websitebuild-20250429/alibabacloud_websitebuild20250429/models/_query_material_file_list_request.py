# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryMaterialFileListRequest(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        directory_id: str = None,
        max_file_size: int = None,
        max_results: int = None,
        min_file_size: int = None,
        name: str = None,
        next_token: str = None,
        order_column: str = None,
        order_type: str = None,
        page_num: int = None,
        page_size: int = None,
        status_list: List[str] = None,
        suffix_list: List[str] = None,
        type_list: List[str] = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        # This parameter is required.
        self.directory_id = directory_id
        self.max_file_size = max_file_size
        self.max_results = max_results
        self.min_file_size = min_file_size
        self.name = name
        self.next_token = next_token
        self.order_column = order_column
        self.order_type = order_type
        self.page_num = page_num
        self.page_size = page_size
        self.status_list = status_list
        self.suffix_list = suffix_list
        self.type_list = type_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.max_file_size is not None:
            result['MaxFileSize'] = self.max_file_size

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.min_file_size is not None:
            result['MinFileSize'] = self.min_file_size

        if self.name is not None:
            result['Name'] = self.name

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status_list is not None:
            result['StatusList'] = self.status_list

        if self.suffix_list is not None:
            result['SuffixList'] = self.suffix_list

        if self.type_list is not None:
            result['TypeList'] = self.type_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('MaxFileSize') is not None:
            self.max_file_size = m.get('MaxFileSize')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MinFileSize') is not None:
            self.min_file_size = m.get('MinFileSize')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('SuffixList') is not None:
            self.suffix_list = m.get('SuffixList')

        if m.get('TypeList') is not None:
            self.type_list = m.get('TypeList')

        return self

