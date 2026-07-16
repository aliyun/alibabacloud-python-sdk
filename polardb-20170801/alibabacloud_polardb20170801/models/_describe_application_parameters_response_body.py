# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationParametersResponseBody(DaraModel):
    def __init__(
        self,
        parameter_templates: main_models.DescribeApplicationParametersResponseBodyParameterTemplates = None,
        parameters: main_models.DescribeApplicationParametersResponseBodyParameters = None,
        request_id: str = None,
    ):
        # The details of the parameter template.
        self.parameter_templates = parameter_templates
        # The parameter details.
        self.parameters = parameters
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.parameter_templates:
            self.parameter_templates.validate()
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_templates is not None:
            result['ParameterTemplates'] = self.parameter_templates.to_map()

        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterTemplates') is not None:
            temp_model = main_models.DescribeApplicationParametersResponseBodyParameterTemplates()
            self.parameter_templates = temp_model.from_map(m.get('ParameterTemplates'))

        if m.get('Parameters') is not None:
            temp_model = main_models.DescribeApplicationParametersResponseBodyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApplicationParametersResponseBodyParameters(DaraModel):
    def __init__(
        self,
        component_parameters: List[main_models.DescribeApplicationParametersResponseBodyParametersComponentParameters] = None,
    ):
        # A list of subcomponents that contain lists of parameter details.
        self.component_parameters = component_parameters

    def validate(self):
        if self.component_parameters:
            for v1 in self.component_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComponentParameters'] = []
        if self.component_parameters is not None:
            for k1 in self.component_parameters:
                result['ComponentParameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_parameters = []
        if m.get('ComponentParameters') is not None:
            for k1 in m.get('ComponentParameters'):
                temp_model = main_models.DescribeApplicationParametersResponseBodyParametersComponentParameters()
                self.component_parameters.append(temp_model.from_map(k1))

        return self

class DescribeApplicationParametersResponseBodyParametersComponentParameters(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        component_type: str = None,
        parameters: List[main_models.DescribeApplicationParametersResponseBodyParametersComponentParametersParameters] = None,
    ):
        # The subcomponent ID or application ID.
        self.component_id = component_id
        # The type of the subcomponent.
        self.component_type = component_type
        # A list of parameter details.
        self.parameters = parameters

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
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.DescribeApplicationParametersResponseBodyParametersComponentParametersParameters()
                self.parameters.append(temp_model.from_map(k1))

        return self

class DescribeApplicationParametersResponseBodyParametersComponentParametersParameters(DaraModel):
    def __init__(
        self,
        default: str = None,
        description: str = None,
        name: str = None,
        need_restart: bool = None,
        pattern: str = None,
        read_only: bool = None,
        status: str = None,
        type: str = None,
        value: str = None,
    ):
        # The default value of the parameter.
        self.default = default
        # The parameter description.
        self.description = description
        # The parameter name.
        self.name = name
        # Indicates whether the application needs to be restarted after you modify the parameter.
        self.need_restart = need_restart
        # The regular expression for the parameter.
        self.pattern = pattern
        # Indicates whether the parameter is read-only.
        self.read_only = read_only
        # The status.
        self.status = status
        # The parameter type.
        self.type = type
        # The current value of the parameter.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['Default'] = self.default

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.need_restart is not None:
            result['NeedRestart'] = self.need_restart

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedRestart') is not None:
            self.need_restart = m.get('NeedRestart')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeApplicationParametersResponseBodyParameterTemplates(DaraModel):
    def __init__(
        self,
        component_parameter_templates: List[main_models.DescribeApplicationParametersResponseBodyParameterTemplatesComponentParameterTemplates] = None,
    ):
        # A list of subcomponents that contain lists of parameter template details.
        self.component_parameter_templates = component_parameter_templates

    def validate(self):
        if self.component_parameter_templates:
            for v1 in self.component_parameter_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComponentParameterTemplates'] = []
        if self.component_parameter_templates is not None:
            for k1 in self.component_parameter_templates:
                result['ComponentParameterTemplates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_parameter_templates = []
        if m.get('ComponentParameterTemplates') is not None:
            for k1 in m.get('ComponentParameterTemplates'):
                temp_model = main_models.DescribeApplicationParametersResponseBodyParameterTemplatesComponentParameterTemplates()
                self.component_parameter_templates.append(temp_model.from_map(k1))

        return self

class DescribeApplicationParametersResponseBodyParameterTemplatesComponentParameterTemplates(DaraModel):
    def __init__(
        self,
        component_id: str = None,
        component_type: str = None,
        parameters: List[main_models.DescribeApplicationParametersResponseBodyParameterTemplatesComponentParameterTemplatesParameters] = None,
    ):
        # The subcomponent ID or application ID.
        self.component_id = component_id
        # The type of the subcomponent.
        self.component_type = component_type
        # A list of parameter template details.
        self.parameters = parameters

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
        if self.component_id is not None:
            result['ComponentId'] = self.component_id

        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        result['Parameters'] = []
        if self.parameters is not None:
            for k1 in self.parameters:
                result['Parameters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentId') is not None:
            self.component_id = m.get('ComponentId')

        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        self.parameters = []
        if m.get('Parameters') is not None:
            for k1 in m.get('Parameters'):
                temp_model = main_models.DescribeApplicationParametersResponseBodyParameterTemplatesComponentParameterTemplatesParameters()
                self.parameters.append(temp_model.from_map(k1))

        return self

class DescribeApplicationParametersResponseBodyParameterTemplatesComponentParameterTemplatesParameters(DaraModel):
    def __init__(
        self,
        default: str = None,
        description: str = None,
        name: str = None,
        need_restart: bool = None,
        pattern: str = None,
        read_only: bool = None,
        type: str = None,
    ):
        # The default value of the parameter.
        self.default = default
        # The parameter description.
        self.description = description
        # The parameter name.
        self.name = name
        # Indicates whether the application needs to be restarted after you modify the parameter.
        self.need_restart = need_restart
        # The regular expression for the parameter.
        self.pattern = pattern
        # Indicates whether the parameter is read-only.
        self.read_only = read_only
        # The parameter type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default is not None:
            result['Default'] = self.default

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.need_restart is not None:
            result['NeedRestart'] = self.need_restart

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NeedRestart') is not None:
            self.need_restart = m.get('NeedRestart')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

