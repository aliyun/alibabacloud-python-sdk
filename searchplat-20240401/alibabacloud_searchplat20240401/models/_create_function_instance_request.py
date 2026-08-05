# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_searchplat20240401 import models as main_models
from darabonba.model import DaraModel

class CreateFunctionInstanceRequest(DaraModel):
    def __init__(
        self,
        create_parameters: List[main_models.CreateFunctionInstanceRequestCreateParameters] = None,
        description: str = None,
        function_type: str = None,
        instance_name: str = None,
        model_type: str = None,
    ):
        # The creation parameters.
        self.create_parameters = create_parameters
        # The instance description.
        self.description = description
        # The configuration type. Valid values:
        # - PAAS
        # - SAAS.
        self.function_type = function_type
        # The configuration or model name.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The service ID. Valid values:
        # - ops-query-analyze-nl2sql-001
        # - ops-embedding-dim-reduction-001: vector dimension reduction.
        # 
        # This parameter is required.
        self.model_type = model_type

    def validate(self):
        if self.create_parameters:
            for v1 in self.create_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['createParameters'] = []
        if self.create_parameters is not None:
            for k1 in self.create_parameters:
                result['createParameters'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.function_type is not None:
            result['functionType'] = self.function_type

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.model_type is not None:
            result['modelType'] = self.model_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_parameters = []
        if m.get('createParameters') is not None:
            for k1 in m.get('createParameters'):
                temp_model = main_models.CreateFunctionInstanceRequestCreateParameters()
                self.create_parameters.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('functionType') is not None:
            self.function_type = m.get('functionType')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('modelType') is not None:
            self.model_type = m.get('modelType')

        return self

class CreateFunctionInstanceRequestCreateParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The parameter name.
        self.name = name
        # The parameter value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

