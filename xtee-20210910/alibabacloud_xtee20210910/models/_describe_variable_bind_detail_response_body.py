# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeVariableBindDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVariableBindDetailResponseBodyResultObject = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Return object
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['resultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('resultObject') is not None:
            temp_model = main_models.DescribeVariableBindDetailResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('resultObject'))

        return self

class DescribeVariableBindDetailResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        allow_modify: bool = None,
        define_id: int = None,
        define_title: str = None,
        description: str = None,
        event_code: str = None,
        id: int = None,
        params: List[main_models.DescribeVariableBindDetailResponseBodyResultObjectParams] = None,
        relation_rules: List[main_models.DescribeVariableBindDetailResponseBodyResultObjectRelationRules] = None,
        title: str = None,
    ):
        # Whether modification is allowed, default is false
        self.allow_modify = allow_modify
        # Variable definition ID
        self.define_id = define_id
        # Variable definition title
        self.define_title = define_title
        # Variable description information
        self.description = description
        # Event code
        self.event_code = event_code
        # Variable ID.
        self.id = id
        # Bound parameters.
        self.params = params
        # List of associated policies
        self.relation_rules = relation_rules
        # Title.
        self.title = title

    def validate(self):
        if self.params:
            for v1 in self.params:
                 if v1:
                    v1.validate()
        if self.relation_rules:
            for v1 in self.relation_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_modify is not None:
            result['allowModify'] = self.allow_modify

        if self.define_id is not None:
            result['defineId'] = self.define_id

        if self.define_title is not None:
            result['defineTitle'] = self.define_title

        if self.description is not None:
            result['description'] = self.description

        if self.event_code is not None:
            result['eventCode'] = self.event_code

        if self.id is not None:
            result['id'] = self.id

        result['params'] = []
        if self.params is not None:
            for k1 in self.params:
                result['params'].append(k1.to_map() if k1 else None)

        result['relationRules'] = []
        if self.relation_rules is not None:
            for k1 in self.relation_rules:
                result['relationRules'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowModify') is not None:
            self.allow_modify = m.get('allowModify')

        if m.get('defineId') is not None:
            self.define_id = m.get('defineId')

        if m.get('defineTitle') is not None:
            self.define_title = m.get('defineTitle')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('eventCode') is not None:
            self.event_code = m.get('eventCode')

        if m.get('id') is not None:
            self.id = m.get('id')

        self.params = []
        if m.get('params') is not None:
            for k1 in m.get('params'):
                temp_model = main_models.DescribeVariableBindDetailResponseBodyResultObjectParams()
                self.params.append(temp_model.from_map(k1))

        self.relation_rules = []
        if m.get('relationRules') is not None:
            for k1 in m.get('relationRules'):
                temp_model = main_models.DescribeVariableBindDetailResponseBodyResultObjectRelationRules()
                self.relation_rules.append(temp_model.from_map(k1))

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class DescribeVariableBindDetailResponseBodyResultObjectRelationRules(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Policy rule ID
        self.key = key
        # Policy name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class DescribeVariableBindDetailResponseBodyResultObjectParams(DaraModel):
    def __init__(
        self,
        event_field_name: str = None,
        required: bool = None,
        variable_name: str = None,
    ):
        # Event field name
        self.event_field_name = event_field_name
        # Whether it is required, default is false
        self.required = required
        # Bound variable name
        self.variable_name = variable_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_field_name is not None:
            result['eventFieldName'] = self.event_field_name

        if self.required is not None:
            result['required'] = self.required

        if self.variable_name is not None:
            result['variableName'] = self.variable_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventFieldName') is not None:
            self.event_field_name = m.get('eventFieldName')

        if m.get('required') is not None:
            self.required = m.get('required')

        if m.get('variableName') is not None:
            self.variable_name = m.get('variableName')

        return self

