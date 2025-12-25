# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class FieldContentValue(DaraModel):
    def __init__(
        self,
        sort_order: int = None,
        field_list: List[main_models.FieldContentValueFieldList] = None,
    ):
        # The sequence number of the fields.
        self.sort_order = sort_order
        # The fields.
        self.field_list = field_list

    def validate(self):
        if self.field_list:
            for v1 in self.field_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        result['FieldList'] = []
        if self.field_list is not None:
            for k1 in self.field_list:
                result['FieldList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        self.field_list = []
        if m.get('FieldList') is not None:
            for k1 in m.get('FieldList'):
                temp_model = main_models.FieldContentValueFieldList()
                self.field_list.append(temp_model.from_map(k1))

        return self

class FieldContentValueFieldList(DaraModel):
    def __init__(
        self,
        field_name: str = None,
        description: str = None,
        description_cn: str = None,
        category: str = None,
        data_type: str = None,
        sort_order: int = None,
        is_default: bool = None,
    ):
        # The field name.
        self.field_name = field_name
        # The description of the field in English.
        self.description = description
        # The description of the field in Chinese.
        self.description_cn = description_cn
        # The category of the field.
        self.category = category
        # The data type of the field.
        self.data_type = data_type
        # The sequence number of the field.
        self.sort_order = sort_order
        # Indicates whether the field is available by default.
        self.is_default = is_default

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_name is not None:
            result['FieldName'] = self.field_name

        if self.description is not None:
            result['Description'] = self.description

        if self.description_cn is not None:
            result['DescriptionCn'] = self.description_cn

        if self.category is not None:
            result['Category'] = self.category

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldName') is not None:
            self.field_name = m.get('FieldName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DescriptionCn') is not None:
            self.description_cn = m.get('DescriptionCn')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        return self

