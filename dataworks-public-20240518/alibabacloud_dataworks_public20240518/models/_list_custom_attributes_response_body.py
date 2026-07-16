# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListCustomAttributesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListCustomAttributesResponseBodyPagingInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The paging information.
        self.paging_info = paging_info
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request succeeded.
        self.success = success

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListCustomAttributesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCustomAttributesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        custom_attributes: List[main_models.CustomAttribute] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # A list of custom attribute objects.
        self.custom_attributes = custom_attributes
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.custom_attributes:
            for v1 in self.custom_attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomAttributes'] = []
        if self.custom_attributes is not None:
            for k1 in self.custom_attributes:
                result['CustomAttributes'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_attributes = []
        if m.get('CustomAttributes') is not None:
            for k1 in m.get('CustomAttributes'):
                temp_model = main_models.CustomAttribute()
                self.custom_attributes.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

