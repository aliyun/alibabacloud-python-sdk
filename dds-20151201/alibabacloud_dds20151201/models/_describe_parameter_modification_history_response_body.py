# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeParameterModificationHistoryResponseBody(DaraModel):
    def __init__(
        self,
        historical_parameters: main_models.DescribeParameterModificationHistoryResponseBodyHistoricalParameters = None,
        request_id: str = None,
    ):
        # Details about the parameter modification records.
        self.historical_parameters = historical_parameters
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.historical_parameters:
            self.historical_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.historical_parameters is not None:
            result['HistoricalParameters'] = self.historical_parameters.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HistoricalParameters') is not None:
            temp_model = main_models.DescribeParameterModificationHistoryResponseBodyHistoricalParameters()
            self.historical_parameters = temp_model.from_map(m.get('HistoricalParameters'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeParameterModificationHistoryResponseBodyHistoricalParameters(DaraModel):
    def __init__(
        self,
        historical_parameter: List[main_models.DescribeParameterModificationHistoryResponseBodyHistoricalParametersHistoricalParameter] = None,
    ):
        self.historical_parameter = historical_parameter

    def validate(self):
        if self.historical_parameter:
            for v1 in self.historical_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HistoricalParameter'] = []
        if self.historical_parameter is not None:
            for k1 in self.historical_parameter:
                result['HistoricalParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.historical_parameter = []
        if m.get('HistoricalParameter') is not None:
            for k1 in m.get('HistoricalParameter'):
                temp_model = main_models.DescribeParameterModificationHistoryResponseBodyHistoricalParametersHistoricalParameter()
                self.historical_parameter.append(temp_model.from_map(k1))

        return self

class DescribeParameterModificationHistoryResponseBodyHistoricalParametersHistoricalParameter(DaraModel):
    def __init__(
        self,
        modify_time: str = None,
        new_parameter_value: str = None,
        old_parameter_value: str = None,
        parameter_name: str = None,
    ):
        # The time when the parameter was modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modify_time = modify_time
        # The parameter value after modification.
        self.new_parameter_value = new_parameter_value
        # The parameter value before modification.
        self.old_parameter_value = old_parameter_value
        # The name of the modified parameter.
        self.parameter_name = parameter_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.new_parameter_value is not None:
            result['NewParameterValue'] = self.new_parameter_value

        if self.old_parameter_value is not None:
            result['OldParameterValue'] = self.old_parameter_value

        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('NewParameterValue') is not None:
            self.new_parameter_value = m.get('NewParameterValue')

        if m.get('OldParameterValue') is not None:
            self.old_parameter_value = m.get('OldParameterValue')

        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        return self

