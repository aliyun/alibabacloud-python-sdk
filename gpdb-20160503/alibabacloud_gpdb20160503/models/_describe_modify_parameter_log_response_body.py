# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeModifyParameterLogResponseBody(DaraModel):
    def __init__(
        self,
        changelogs: List[main_models.DescribeModifyParameterLogResponseBodyChangelogs] = None,
        request_id: str = None,
    ):
        # The queried parameter modification logs.
        self.changelogs = changelogs
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.changelogs:
            for v1 in self.changelogs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Changelogs'] = []
        if self.changelogs is not None:
            for k1 in self.changelogs:
                result['Changelogs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.changelogs = []
        if m.get('Changelogs') is not None:
            for k1 in m.get('Changelogs'):
                temp_model = main_models.DescribeModifyParameterLogResponseBodyChangelogs()
                self.changelogs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeModifyParameterLogResponseBodyChangelogs(DaraModel):
    def __init__(
        self,
        effect_time: str = None,
        parameter_name: str = None,
        parameter_valid: str = None,
        parameter_value_after: str = None,
        parameter_value_before: str = None,
    ):
        # The effective time.
        self.effect_time = effect_time
        # The name of the parameter.
        self.parameter_name = parameter_name
        # Indicates whether the modification takes effect.
        self.parameter_valid = parameter_valid
        # The original value of the parameter.
        self.parameter_value_after = parameter_value_after
        # The new value of the parameter.
        self.parameter_value_before = parameter_value_before

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_valid is not None:
            result['ParameterValid'] = self.parameter_valid

        if self.parameter_value_after is not None:
            result['ParameterValueAfter'] = self.parameter_value_after

        if self.parameter_value_before is not None:
            result['ParameterValueBefore'] = self.parameter_value_before

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValid') is not None:
            self.parameter_valid = m.get('ParameterValid')

        if m.get('ParameterValueAfter') is not None:
            self.parameter_value_after = m.get('ParameterValueAfter')

        if m.get('ParameterValueBefore') is not None:
            self.parameter_value_before = m.get('ParameterValueBefore')

        return self

