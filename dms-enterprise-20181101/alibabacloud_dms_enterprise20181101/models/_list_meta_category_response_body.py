# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListMetaCategoryResponseBody(DaraModel):
    def __init__(
        self,
        category_list: main_models.ListMetaCategoryResponseBodyCategoryList = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The list of categories.
        self.category_list = category_list
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.category_list:
            self.category_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_list is not None:
            result['CategoryList'] = self.category_list.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryList') is not None:
            temp_model = main_models.ListMetaCategoryResponseBodyCategoryList()
            self.category_list = temp_model.from_map(m.get('CategoryList'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListMetaCategoryResponseBodyCategoryList(DaraModel):
    def __init__(
        self,
        meta_category: List[main_models.MetaCategory] = None,
    ):
        self.meta_category = meta_category

    def validate(self):
        if self.meta_category:
            for v1 in self.meta_category:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MetaCategory'] = []
        if self.meta_category is not None:
            for k1 in self.meta_category:
                result['MetaCategory'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.meta_category = []
        if m.get('MetaCategory') is not None:
            for k1 in m.get('MetaCategory'):
                temp_model = main_models.MetaCategory()
                self.meta_category.append(temp_model.from_map(k1))

        return self

