# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListParameterSetRelationResponseBody(DaraModel):
    def __init__(
        self,
        parameter_sets: List[main_models.ListParameterSetRelationResponseBodyParameterSets] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.parameter_sets = parameter_sets
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.parameter_sets:
            for v1 in self.parameter_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['parameterSets'] = []
        if self.parameter_sets is not None:
            for k1 in self.parameter_sets:
                result['parameterSets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameter_sets = []
        if m.get('parameterSets') is not None:
            for k1 in m.get('parameterSets'):
                temp_model = main_models.ListParameterSetRelationResponseBodyParameterSets()
                self.parameter_sets.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListParameterSetRelationResponseBodyParameterSets(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        parameter_set_id: str = None,
        parameters: Dict[str, str] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.parameter_set_id = parameter_set_id
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.parameter_set_id is not None:
            result['parameterSetId'] = self.parameter_set_id

        if self.parameters is not None:
            result['parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('parameterSetId') is not None:
            self.parameter_set_id = m.get('parameterSetId')

        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')

        return self

