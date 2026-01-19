# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeSamplebatchPageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeSamplebatchPageResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # ID of the request
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Page size, with a default value of 10
        self.page_size = page_size
        # Returned object
        self.result_object = result_object
        # Total number of items
        self.total_item = total_item
        # Total number of pages
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
                temp_model = main_models.DescribeSamplebatchPageResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeSamplebatchPageResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        batch_name: str = None,
        creator: str = None,
        data_type: str = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        init_valid_file_row: int = None,
        sample_batch_type: str = None,
        services: str = None,
        updator: str = None,
        uuid: str = None,
    ):
        # Sample batch name
        self.batch_name = batch_name
        # Creator.
        self.creator = creator
        # Data type
        self.data_type = data_type
        # Description.
        self.description = description
        # Creation time.
        self.gmt_create = gmt_create
        # Modification time
        self.gmt_modified = gmt_modified
        # Valid sample content data
        self.init_valid_file_row = init_valid_file_row
        # Specific type of the sample list
        self.sample_batch_type = sample_batch_type
        # Service ID
        self.services = services
        # Modifier
        self.updator = updator
        # Sample batch UUID
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_name is not None:
            result['batchName'] = self.batch_name

        if self.creator is not None:
            result['creator'] = self.creator

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.description is not None:
            result['description'] = self.description

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.init_valid_file_row is not None:
            result['initValidFileRow'] = self.init_valid_file_row

        if self.sample_batch_type is not None:
            result['sampleBatchType'] = self.sample_batch_type

        if self.services is not None:
            result['services'] = self.services

        if self.updator is not None:
            result['updator'] = self.updator

        if self.uuid is not None:
            result['uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchName') is not None:
            self.batch_name = m.get('batchName')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('initValidFileRow') is not None:
            self.init_valid_file_row = m.get('initValidFileRow')

        if m.get('sampleBatchType') is not None:
            self.sample_batch_type = m.get('sampleBatchType')

        if m.get('services') is not None:
            self.services = m.get('services')

        if m.get('updator') is not None:
            self.updator = m.get('updator')

        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')

        return self

