# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_agentloop20260520 import models as main_models
from darabonba.model import DaraModel

class ExecuteQueryRequest(DaraModel):
    def __init__(
        self,
        annotation_filter: main_models.ExecuteQueryRequestAnnotationFilter = None,
        from_: int = None,
        length: int = None,
        max_output_length: int = None,
        offset: int = None,
        query: str = None,
        to: int = None,
        type: str = None,
        version: str = None,
    ):
        # The annotation filter.
        self.annotation_filter = annotation_filter
        # The start time of the query.
        self.from_ = from_
        # The page size.
        self.length = length
        # The maximum output length.
        self.max_output_length = max_output_length
        # The pagination offset.
        self.offset = offset
        # The query entered by the user.
        # 
        # This parameter is required.
        self.query = query
        # The end time of the query.
        self.to = to
        # The statement type. Currently, only SQL is supported.
        # 
        # This parameter is required.
        self.type = type
        # The dataset version.
        self.version = version

    def validate(self):
        if self.annotation_filter:
            self.annotation_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.annotation_filter is not None:
            result['annotationFilter'] = self.annotation_filter.to_map()

        if self.from_ is not None:
            result['from'] = self.from_

        if self.length is not None:
            result['length'] = self.length

        if self.max_output_length is not None:
            result['maxOutputLength'] = self.max_output_length

        if self.offset is not None:
            result['offset'] = self.offset

        if self.query is not None:
            result['query'] = self.query

        if self.to is not None:
            result['to'] = self.to

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('annotationFilter') is not None:
            temp_model = main_models.ExecuteQueryRequestAnnotationFilter()
            self.annotation_filter = temp_model.from_map(m.get('annotationFilter'))

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('length') is not None:
            self.length = m.get('length')

        if m.get('maxOutputLength') is not None:
            self.max_output_length = m.get('maxOutputLength')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class ExecuteQueryRequestAnnotationFilter(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.ExecuteQueryRequestAnnotationFilterConditions] = None,
    ):
        # The annotation filter conditions.
        self.conditions = conditions

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.ExecuteQueryRequestAnnotationFilterConditions()
                self.conditions.append(temp_model.from_map(k1))

        return self

class ExecuteQueryRequestAnnotationFilterConditions(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: Any = None,
    ):
        # The annotation key.
        self.key = key
        # The operator.
        self.operator = operator
        # The annotation value.
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

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

