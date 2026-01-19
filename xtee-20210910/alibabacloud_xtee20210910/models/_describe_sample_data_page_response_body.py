# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSampleDataPageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeSampleDataPageResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # ID of the request
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Number of items per page, default is 10.
        self.page_size = page_size
        # Returned object
        self.result_object = result_object
        # Total number of items
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
                temp_model = main_models.DescribeSampleDataPageResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeSampleDataPageResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        creator: str = None,
        data_tag_type: str = None,
        data_value: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        last_source_type: str = None,
        updator: str = None,
        uuid: str = None,
        version: int = None,
    ):
        # Creator
        self.creator = creator
        # Sample type
        self.data_tag_type = data_tag_type
        # Content of the list entered in the text box
        self.data_value = data_value
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time
        self.gmt_modified = gmt_modified
        # Last source
        self.last_source_type = last_source_type
        # Modifier
        self.updator = updator
        # UUID of the sample batch
        self.uuid = uuid
        # Version number
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['creator'] = self.creator

        if self.data_tag_type is not None:
            result['dataTagType'] = self.data_tag_type

        if self.data_value is not None:
            result['dataValue'] = self.data_value

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.last_source_type is not None:
            result['lastSourceType'] = self.last_source_type

        if self.updator is not None:
            result['updator'] = self.updator

        if self.uuid is not None:
            result['uuid'] = self.uuid

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('dataTagType') is not None:
            self.data_tag_type = m.get('dataTagType')

        if m.get('dataValue') is not None:
            self.data_value = m.get('dataValue')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('lastSourceType') is not None:
            self.last_source_type = m.get('lastSourceType')

        if m.get('updator') is not None:
            self.updator = m.get('updator')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

