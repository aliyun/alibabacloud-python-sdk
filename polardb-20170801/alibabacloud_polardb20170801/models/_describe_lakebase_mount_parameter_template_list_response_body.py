# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeLakebaseMountParameterTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        parameters: List[main_models.DescribeLakebaseMountParameterTemplateListResponseBodyParameters] = None,
        request_id: str = None,
    ):
        # The list of parameter templates.
        self.parameters = parameters
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parameters:
            for v1 in self.parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.DescribeLakebaseMountParameterTemplateListResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLakebaseMountParameterTemplateListResponseBodyParameters(DaraModel):
    def __init__(
        self,
        comment: str = None,
        default_value: str = None,
        is_dynamic: str = None,
        is_user_changeable: str = None,
        optional: str = None,
        parameter_name: str = None,
        unit: str = None,
    ):
        # The parameter description.
        self.comment = comment
        # The default value.
        self.default_value = default_value
        # Indicates whether the parameter takes effect dynamically. Valid values: 1 and 0.
        self.is_dynamic = is_dynamic
        # Indicates whether the parameter can be modified by users. Valid values: 1 and 0.
        self.is_user_changeable = is_user_changeable
        # The value range or valid values. Example: [0-3600].
        self.optional = optional
        # The parameter name.
        self.parameter_name = parameter_name
        # The unit.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.is_dynamic is not None:
            result['IsDynamic'] = self.is_dynamic

        if self.is_user_changeable is not None:
            result['IsUserChangeable'] = self.is_user_changeable

        if self.optional is not None:
            result['Optional'] = self.optional

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('IsDynamic') is not None:
            self.is_dynamic = m.get('IsDynamic')

        if m.get('IsUserChangeable') is not None:
            self.is_user_changeable = m.get('IsUserChangeable')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

