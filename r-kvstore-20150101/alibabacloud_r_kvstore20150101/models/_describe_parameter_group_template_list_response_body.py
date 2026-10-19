# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_r_kvstore20150101 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterGroupTemplateListResponseBody(DaraModel):
    def __init__(
        self,
        engine_version: str = None,
        parameters: List[main_models.DescribeParameterGroupTemplateListResponseBodyParameters] = None,
        request_id: str = None,
    ):
        # The compatible version.
        self.engine_version = engine_version
        # The list of parameter details.
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
        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.DescribeParameterGroupTemplateListResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParameterGroupTemplateListResponseBodyParameters(DaraModel):
    def __init__(
        self,
        checking_code: str = None,
        effective: int = None,
        factor: int = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
        revisable: int = None,
        support_modify_for_minor_version: bool = None,
        unit: str = None,
    ):
        # The value range of the parameter.
        self.checking_code = checking_code
        # Indicates whether the parameter has taken effect. Valid values:
        # * **0**: No.
        # * **1**: Yes.
        self.effective = effective
        # The divisor factor. For integer and byte type parameters, the parameter value must not only fall within the valid range but also be a multiple of Factor (when Factor is not 0).
        self.factor = factor
        # The parameter description.
        self.parameter_description = parameter_description
        # The parameter name.
        self.parameter_name = parameter_name
        # The default value of the parameter.
        self.parameter_value = parameter_value
        # Indicates whether the parameter can be modified. Valid values:
        # 
        # - **0**: The parameter cannot be modified.
        # - **1**: The parameter can be modified.
        self.revisable = revisable
        # Indicates whether modification for minor versions is supported. Valid values:
        # * **true**: Supported.
        # * **false**: Not supported.
        self.support_modify_for_minor_version = support_modify_for_minor_version
        # The unit of the parameter value. Valid values:
        # * **INT**: a common integer.
        # * **STRING**: a fixed string.
        # * **B**: bytes.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code

        if self.effective is not None:
            result['Effective'] = self.effective

        if self.factor is not None:
            result['Factor'] = self.factor

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        if self.revisable is not None:
            result['Revisable'] = self.revisable

        if self.support_modify_for_minor_version is not None:
            result['SupportModifyForMinorVersion'] = self.support_modify_for_minor_version

        if self.unit is not None:
            result['Unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')

        if m.get('Effective') is not None:
            self.effective = m.get('Effective')

        if m.get('Factor') is not None:
            self.factor = m.get('Factor')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        if m.get('Revisable') is not None:
            self.revisable = m.get('Revisable')

        if m.get('SupportModifyForMinorVersion') is not None:
            self.support_modify_for_minor_version = m.get('SupportModifyForMinorVersion')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        return self

