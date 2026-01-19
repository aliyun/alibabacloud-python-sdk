# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSafTagListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeSafTagListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, default value is 10.
        self.page_size = page_size
        # Returned object.
        self.result_object = result_object
        # Total number of items.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeSafTagListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeSafTagListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        tag_desc: str = None,
        tag_mean: str = None,
        tag_name: str = None,
        tag_state: str = None,
        tag_type: str = None,
        tag_uid: str = None,
        update_time: str = None,
    ):
        # Tag description.
        self.tag_desc = tag_desc
        # Tag meaning.
        self.tag_mean = tag_mean
        # Tag name.
        self.tag_name = tag_name
        # Tag identifier.
        self.tag_state = tag_state
        # Tag type.
        self.tag_type = tag_type
        # Unique identifier of the tag key.
        self.tag_uid = tag_uid
        # Update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_desc is not None:
            result['tagDesc'] = self.tag_desc

        if self.tag_mean is not None:
            result['tagMean'] = self.tag_mean

        if self.tag_name is not None:
            result['tagName'] = self.tag_name

        if self.tag_state is not None:
            result['tagState'] = self.tag_state

        if self.tag_type is not None:
            result['tagType'] = self.tag_type

        if self.tag_uid is not None:
            result['tagUid'] = self.tag_uid

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagDesc') is not None:
            self.tag_desc = m.get('tagDesc')

        if m.get('tagMean') is not None:
            self.tag_mean = m.get('tagMean')

        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')

        if m.get('tagState') is not None:
            self.tag_state = m.get('tagState')

        if m.get('tagType') is not None:
            self.tag_type = m.get('tagType')

        if m.get('tagUid') is not None:
            self.tag_uid = m.get('tagUid')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        return self

