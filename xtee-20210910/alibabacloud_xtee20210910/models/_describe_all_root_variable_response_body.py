# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeAllRootVariableResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: List[main_models.DescribeAllRootVariableResponseBodyResultObject] = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

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

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeAllRootVariableResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        return self

class DescribeAllRootVariableResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        display_type: str = None,
        favorite_flag: bool = None,
        field_rank: int = None,
        field_type: str = None,
        id: int = None,
        input_field_type: str = None,
        inputs: str = None,
        name: str = None,
        output_threshold: main_models.DescribeAllRootVariableResponseBodyResultObjectOutputThreshold = None,
        source_type: str = None,
        title: str = None,
        type: str = None,
    ):
        # Variable code
        self.code = code
        # Variable description.
        self.description = description
        # Display type and group label
        self.display_type = display_type
        # Favorite flag
        self.favorite_flag = favorite_flag
        # Field ranking
        self.field_rank = field_rank
        # Field type.
        self.field_type = field_type
        # Variable ID.
        self.id = id
        # Input field type.
        self.input_field_type = input_field_type
        # Variable input.
        self.inputs = inputs
        # Variable name.
        self.name = name
        # Maximum cross-sectional area of the checkbox.
        self.output_threshold = output_threshold
        # Data source
        self.source_type = source_type
        # Title.
        self.title = title
        # Variable type.
        self.type = type

    def validate(self):
        if self.output_threshold:
            self.output_threshold.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.description is not None:
            result['description'] = self.description

        if self.display_type is not None:
            result['displayType'] = self.display_type

        if self.favorite_flag is not None:
            result['favoriteFlag'] = self.favorite_flag

        if self.field_rank is not None:
            result['fieldRank'] = self.field_rank

        if self.field_type is not None:
            result['fieldType'] = self.field_type

        if self.id is not None:
            result['id'] = self.id

        if self.input_field_type is not None:
            result['inputFieldType'] = self.input_field_type

        if self.inputs is not None:
            result['inputs'] = self.inputs

        if self.name is not None:
            result['name'] = self.name

        if self.output_threshold is not None:
            result['outputThreshold'] = self.output_threshold.to_map()

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayType') is not None:
            self.display_type = m.get('displayType')

        if m.get('favoriteFlag') is not None:
            self.favorite_flag = m.get('favoriteFlag')

        if m.get('fieldRank') is not None:
            self.field_rank = m.get('fieldRank')

        if m.get('fieldType') is not None:
            self.field_type = m.get('fieldType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('inputFieldType') is not None:
            self.input_field_type = m.get('inputFieldType')

        if m.get('inputs') is not None:
            self.inputs = m.get('inputs')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('outputThreshold') is not None:
            temp_model = main_models.DescribeAllRootVariableResponseBodyResultObjectOutputThreshold()
            self.output_threshold = temp_model.from_map(m.get('outputThreshold'))

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class DescribeAllRootVariableResponseBodyResultObjectOutputThreshold(DaraModel):
    def __init__(
        self,
        max_value: float = None,
        min_value: float = None,
    ):
        # Maximum value
        self.max_value = max_value
        # Minimum value.
        self.min_value = min_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_value is not None:
            result['maxValue'] = self.max_value

        if self.min_value is not None:
            result['minValue'] = self.min_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxValue') is not None:
            self.max_value = m.get('maxValue')

        if m.get('minValue') is not None:
            self.min_value = m.get('minValue')

        return self

