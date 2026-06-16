# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aidge20260428 import models as main_models
from darabonba.model import DaraModel

class CategoryAttributeMatchResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.CategoryAttributeMatchResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. This parameter is not returned if the call is successful.
        self.code = code
        # The returned result.
        self.data = data
        # The error message. This parameter is not returned if the call is successful.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the call is successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CategoryAttributeMatchResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CategoryAttributeMatchResponseBodyData(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.CategoryAttributeMatchResponseBodyDataAttributes] = None,
        category_id: int = None,
        category_name: str = None,
        category_path: str = None,
        filled_count: int = None,
        matched: bool = None,
        total_attributes: int = None,
        usage_map: main_models.CategoryAttributeMatchResponseBodyDataUsageMap = None,
    ):
        # The list of attribute filling results.
        self.attributes = attributes
        # The category ID.
        self.category_id = category_id
        # The category name.
        self.category_name = category_name
        # The full path of the category, separated by "/".
        self.category_path = category_path
        # The number of attributes that are successfully filled.
        self.filled_count = filled_count
        # Indicates whether the attribute is successfully matched. Valid values: true and false.
        self.matched = matched
        # The total number of attributes under the category.
        self.total_attributes = total_attributes
        # The usage fields.
        self.usage_map = usage_map

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()
        if self.usage_map:
            self.usage_map.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['Attributes'].append(k1.to_map() if k1 else None)

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.category_path is not None:
            result['CategoryPath'] = self.category_path

        if self.filled_count is not None:
            result['FilledCount'] = self.filled_count

        if self.matched is not None:
            result['Matched'] = self.matched

        if self.total_attributes is not None:
            result['TotalAttributes'] = self.total_attributes

        if self.usage_map is not None:
            result['UsageMap'] = self.usage_map.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.CategoryAttributeMatchResponseBodyDataAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('CategoryPath') is not None:
            self.category_path = m.get('CategoryPath')

        if m.get('FilledCount') is not None:
            self.filled_count = m.get('FilledCount')

        if m.get('Matched') is not None:
            self.matched = m.get('Matched')

        if m.get('TotalAttributes') is not None:
            self.total_attributes = m.get('TotalAttributes')

        if m.get('UsageMap') is not None:
            temp_model = main_models.CategoryAttributeMatchResponseBodyDataUsageMap()
            self.usage_map = temp_model.from_map(m.get('UsageMap'))

        return self

class CategoryAttributeMatchResponseBodyDataUsageMap(DaraModel):
    def __init__(
        self,
        processing_count: int = None,
    ):
        # The number of processing times.
        self.processing_count = processing_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.processing_count is not None:
            result['ProcessingCount'] = self.processing_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProcessingCount') is not None:
            self.processing_count = m.get('ProcessingCount')

        return self

class CategoryAttributeMatchResponseBodyDataAttributes(DaraModel):
    def __init__(
        self,
        attr_id: int = None,
        confidence: int = None,
        input_type: str = None,
        matched: bool = None,
        name: str = None,
        name_en: str = None,
        reason: str = None,
        selected_values: List[str] = None,
        selected_vids: List[int] = None,
    ):
        # The attribute ID.
        self.attr_id = attr_id
        # The matching confidence score. Valid values: 0 to 100.
        self.confidence = confidence
        # The input type of the attribute.
        self.input_type = input_type
        # Indicates whether the attribute is successfully matched. Valid values: true and false.
        self.matched = matched
        # The Chinese name of the attribute.
        self.name = name
        # The English name of the attribute.
        self.name_en = name_en
        # The reason for the matching result.
        self.reason = reason
        # The list of selected attribute value texts, such as ["iOS","Android"\\].
        self.selected_values = selected_values
        # The list of selected attribute value IDs, such as [30127,30128\\].
        self.selected_vids = selected_vids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attr_id is not None:
            result['AttrId'] = self.attr_id

        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.input_type is not None:
            result['InputType'] = self.input_type

        if self.matched is not None:
            result['Matched'] = self.matched

        if self.name is not None:
            result['Name'] = self.name

        if self.name_en is not None:
            result['NameEn'] = self.name_en

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.selected_values is not None:
            result['SelectedValues'] = self.selected_values

        if self.selected_vids is not None:
            result['SelectedVids'] = self.selected_vids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttrId') is not None:
            self.attr_id = m.get('AttrId')

        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('InputType') is not None:
            self.input_type = m.get('InputType')

        if m.get('Matched') is not None:
            self.matched = m.get('Matched')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('SelectedValues') is not None:
            self.selected_values = m.get('SelectedValues')

        if m.get('SelectedVids') is not None:
            self.selected_vids = m.get('SelectedVids')

        return self

