# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSampleListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeSampleListResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The current page number.
        self.current_page = current_page
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The returned objects.
        self.result_object = result_object
        # The total number of entries.
        self.total_item = total_item
        # The total number of pages.
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
                temp_model = main_models.DescribeSampleListResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeSampleListResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        id: int = None,
        sample_tags: str = None,
        sample_type: int = None,
        sample_value: str = None,
        update_time: int = None,
        version: int = None,
    ):
        # The database ID.
        self.id = id
        # The sample tags.
        self.sample_tags = sample_tags
        # The sample type.
        self.sample_type = sample_type
        # The sample value.
        self.sample_value = sample_value
        # The update time.
        self.update_time = update_time
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.sample_tags is not None:
            result['sampleTags'] = self.sample_tags

        if self.sample_type is not None:
            result['sampleType'] = self.sample_type

        if self.sample_value is not None:
            result['sampleValue'] = self.sample_value

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('sampleTags') is not None:
            self.sample_tags = m.get('sampleTags')

        if m.get('sampleType') is not None:
            self.sample_type = m.get('sampleType')

        if m.get('sampleValue') is not None:
            self.sample_value = m.get('sampleValue')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

