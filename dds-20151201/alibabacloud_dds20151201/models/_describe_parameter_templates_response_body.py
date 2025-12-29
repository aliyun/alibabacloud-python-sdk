# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        engine: str = None,
        engine_version: str = None,
        parameter_count: str = None,
        parameters: main_models.DescribeParameterTemplatesResponseBodyParameters = None,
        request_id: str = None,
    ):
        # The database engine of the instance.
        self.engine = engine
        # The database engine version of the instance.
        self.engine_version = engine_version
        # The number of parameters that are supported by the instance.
        self.parameter_count = parameter_count
        # Details about the parameter templates.
        self.parameters = parameters
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.engine_version is not None:
            result['EngineVersion'] = self.engine_version

        if self.parameter_count is not None:
            result['ParameterCount'] = self.parameter_count

        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EngineVersion') is not None:
            self.engine_version = m.get('EngineVersion')

        if m.get('ParameterCount') is not None:
            self.parameter_count = m.get('ParameterCount')

        if m.get('Parameters') is not None:
            temp_model = main_models.DescribeParameterTemplatesResponseBodyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParameterTemplatesResponseBodyParameters(DaraModel):
    def __init__(
        self,
        template_record: List[main_models.DescribeParameterTemplatesResponseBodyParametersTemplateRecord] = None,
    ):
        self.template_record = template_record

    def validate(self):
        if self.template_record:
            for v1 in self.template_record:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TemplateRecord'] = []
        if self.template_record is not None:
            for k1 in self.template_record:
                result['TemplateRecord'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.template_record = []
        if m.get('TemplateRecord') is not None:
            for k1 in m.get('TemplateRecord'):
                temp_model = main_models.DescribeParameterTemplatesResponseBodyParametersTemplateRecord()
                self.template_record.append(temp_model.from_map(k1))

        return self

class DescribeParameterTemplatesResponseBodyParametersTemplateRecord(DaraModel):
    def __init__(
        self,
        checking_code: str = None,
        force_modify: bool = None,
        force_restart: bool = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # The value range of modifiable parameters.
        self.checking_code = checking_code
        # Indicates whether the parameter is modifiable.
        # 
        # *   **false**: The parameter cannot be modified.
        # *   **true**: The parameter can be modified.
        self.force_modify = force_modify
        # Indicates whether a restart is required for parameter modifications to take effect.
        # 
        # *   **false**: A restart is not required. Parameter modifications immediately take effect.
        # *   **true**: A restart is required for parameter modifications to take effect.
        self.force_restart = force_restart
        # The description of the parameter.
        self.parameter_description = parameter_description
        # The name of the parameter.
        self.parameter_name = parameter_name
        # The default value of the parameter.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checking_code is not None:
            result['CheckingCode'] = self.checking_code

        if self.force_modify is not None:
            result['ForceModify'] = self.force_modify

        if self.force_restart is not None:
            result['ForceRestart'] = self.force_restart

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckingCode') is not None:
            self.checking_code = m.get('CheckingCode')

        if m.get('ForceModify') is not None:
            self.force_modify = m.get('ForceModify')

        if m.get('ForceRestart') is not None:
            self.force_restart = m.get('ForceRestart')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

