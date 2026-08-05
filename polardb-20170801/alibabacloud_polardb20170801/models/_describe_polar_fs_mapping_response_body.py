# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarFsMappingResponseBody(DaraModel):
    def __init__(
        self,
        default_access_key_id: str = None,
        page_number: str = None,
        page_record_count: str = None,
        page_size: str = None,
        path_mapping_items: List[main_models.DescribePolarFsMappingResponseBodyPathMappingItems] = None,
        request_id: str = None,
        total_record_count: str = None,
    ):
        # The default AccessKey ID at the instance level.
        self.default_access_key_id = default_access_key_id
        # The page number.
        self.page_number = page_number
        # The number of records on the current page.
        self.page_record_count = page_record_count
        # The number of entries per page. Valid values:
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        self.page_size = page_size
        # The list of path mappings.
        self.path_mapping_items = path_mapping_items
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

    def validate(self):
        if self.path_mapping_items:
            for v1 in self.path_mapping_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_access_key_id is not None:
            result['DefaultAccessKeyId'] = self.default_access_key_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PathMappingItems'] = []
        if self.path_mapping_items is not None:
            for k1 in self.path_mapping_items:
                result['PathMappingItems'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultAccessKeyId') is not None:
            self.default_access_key_id = m.get('DefaultAccessKeyId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.path_mapping_items = []
        if m.get('PathMappingItems') is not None:
            for k1 in m.get('PathMappingItems'):
                temp_model = main_models.DescribePolarFsMappingResponseBodyPathMappingItems()
                self.path_mapping_items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribePolarFsMappingResponseBodyPathMappingItems(DaraModel):
    def __init__(
        self,
        bucket: str = None,
        bucket_access_key_id: str = None,
        path: str = None,
    ):
        # The storage bucket.
        self.bucket = bucket
        # The AccessKey ID of the storage bucket.
        self.bucket_access_key_id = bucket_access_key_id
        # The mapping path.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.bucket_access_key_id is not None:
            result['BucketAccessKeyId'] = self.bucket_access_key_id

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('BucketAccessKeyId') is not None:
            self.bucket_access_key_id = m.get('BucketAccessKeyId')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

