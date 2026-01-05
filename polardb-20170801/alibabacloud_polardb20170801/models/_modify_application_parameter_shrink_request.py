# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyApplicationParameterShrinkRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        parameter_name: str = None,
        parameter_value: str = None,
        parameters_shrink: str = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.parameters_shrink = parameters_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')

        return self

