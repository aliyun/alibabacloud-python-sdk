# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTaskFlowTimeVariablesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        time_variables: main_models.ListTaskFlowTimeVariablesResponseBodyTimeVariables = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The time variables for the task flow.
        self.time_variables = time_variables

    def validate(self):
        if self.time_variables:
            self.time_variables.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.time_variables is not None:
            result['TimeVariables'] = self.time_variables.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TimeVariables') is not None:
            temp_model = main_models.ListTaskFlowTimeVariablesResponseBodyTimeVariables()
            self.time_variables = temp_model.from_map(m.get('TimeVariables'))

        return self

class ListTaskFlowTimeVariablesResponseBodyTimeVariables(DaraModel):
    def __init__(
        self,
        time_variable: List[main_models.ListTaskFlowTimeVariablesResponseBodyTimeVariablesTimeVariable] = None,
    ):
        self.time_variable = time_variable

    def validate(self):
        if self.time_variable:
            for v1 in self.time_variable:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TimeVariable'] = []
        if self.time_variable is not None:
            for k1 in self.time_variable:
                result['TimeVariable'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.time_variable = []
        if m.get('TimeVariable') is not None:
            for k1 in m.get('TimeVariable'):
                temp_model = main_models.ListTaskFlowTimeVariablesResponseBodyTimeVariablesTimeVariable()
                self.time_variable.append(temp_model.from_map(k1))

        return self

class ListTaskFlowTimeVariablesResponseBodyTimeVariablesTimeVariable(DaraModel):
    def __init__(
        self,
        name: str = None,
        pattern: str = None,
    ):
        # The name of the time variable.
        self.name = name
        # The format of the time variable.
        self.pattern = pattern

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        return self

