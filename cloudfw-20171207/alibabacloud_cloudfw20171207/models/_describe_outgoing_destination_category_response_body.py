# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeOutgoingDestinationCategoryResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        type_list: List[main_models.DescribeOutgoingDestinationCategoryResponseBodyTypeList] = None,
    ):
        self.request_id = request_id
        self.total_count = total_count
        self.type_list = type_list

    def validate(self):
        if self.type_list:
            for v1 in self.type_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TypeList'] = []
        if self.type_list is not None:
            for k1 in self.type_list:
                result['TypeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.type_list = []
        if m.get('TypeList') is not None:
            for k1 in m.get('TypeList'):
                temp_model = main_models.DescribeOutgoingDestinationCategoryResponseBodyTypeList()
                self.type_list.append(temp_model.from_map(k1))

        return self

class DescribeOutgoingDestinationCategoryResponseBodyTypeList(DaraModel):
    def __init__(
        self,
        category_list: List[main_models.DescribeOutgoingDestinationCategoryResponseBodyTypeListCategoryList] = None,
        type_describe: str = None,
        type_id: str = None,
        type_name: str = None,
    ):
        self.category_list = category_list
        self.type_describe = type_describe
        self.type_id = type_id
        self.type_name = type_name

    def validate(self):
        if self.category_list:
            for v1 in self.category_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CategoryList'] = []
        if self.category_list is not None:
            for k1 in self.category_list:
                result['CategoryList'].append(k1.to_map() if k1 else None)

        if self.type_describe is not None:
            result['TypeDescribe'] = self.type_describe

        if self.type_id is not None:
            result['TypeId'] = self.type_id

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_list = []
        if m.get('CategoryList') is not None:
            for k1 in m.get('CategoryList'):
                temp_model = main_models.DescribeOutgoingDestinationCategoryResponseBodyTypeListCategoryList()
                self.category_list.append(temp_model.from_map(k1))

        if m.get('TypeDescribe') is not None:
            self.type_describe = m.get('TypeDescribe')

        if m.get('TypeId') is not None:
            self.type_id = m.get('TypeId')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

class DescribeOutgoingDestinationCategoryResponseBodyTypeListCategoryList(DaraModel):
    def __init__(
        self,
        category_describe: str = None,
        category_id: str = None,
        category_name: str = None,
        class_id: str = None,
    ):
        self.category_describe = category_describe
        self.category_id = category_id
        self.category_name = category_name
        self.class_id = class_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_describe is not None:
            result['CategoryDescribe'] = self.category_describe

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.class_id is not None:
            result['ClassId'] = self.class_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryDescribe') is not None:
            self.category_describe = m.get('CategoryDescribe')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')

        return self

