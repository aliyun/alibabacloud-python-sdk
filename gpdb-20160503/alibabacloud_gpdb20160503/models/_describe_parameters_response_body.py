# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeParametersResponseBody(DaraModel):
    def __init__(
        self,
        parameters: List[main_models.DescribeParametersResponseBodyParameters] = None,
        request_id: str = None,
    ):
        # The queried configuration parameters.
        self.parameters = parameters
        # The ID of the request.
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
                temp_model = main_models.DescribeParametersResponseBodyParameters()
                self.parameters.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParametersResponseBodyParameters(DaraModel):
    def __init__(
        self,
        current_value: str = None,
        force_restart_instance: str = None,
        is_changeable_config: str = None,
        optional_range: str = None,
        parameter_description: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # The current value of the configuration parameter.
        self.current_value = current_value
        # Indicates whether a restart is required for parameter modifications to take effect. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.force_restart_instance = force_restart_instance
        # Indicates whether the configuration parameter can be modified. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.is_changeable_config = is_changeable_config
        # The valid values of the configuration parameter.
        self.optional_range = optional_range
        # The description of the configuration parameter.
        self.parameter_description = parameter_description
        # The name of the configuration parameter.
        self.parameter_name = parameter_name
        # The default value of the configuration parameter.
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_value is not None:
            result['CurrentValue'] = self.current_value

        if self.force_restart_instance is not None:
            result['ForceRestartInstance'] = self.force_restart_instance

        if self.is_changeable_config is not None:
            result['IsChangeableConfig'] = self.is_changeable_config

        if self.optional_range is not None:
            result['OptionalRange'] = self.optional_range

        if self.parameter_description is not None:
            result['ParameterDescription'] = self.parameter_description

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')

        if m.get('ForceRestartInstance') is not None:
            self.force_restart_instance = m.get('ForceRestartInstance')

        if m.get('IsChangeableConfig') is not None:
            self.is_changeable_config = m.get('IsChangeableConfig')

        if m.get('OptionalRange') is not None:
            self.optional_range = m.get('OptionalRange')

        if m.get('ParameterDescription') is not None:
            self.parameter_description = m.get('ParameterDescription')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

