# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeImageEventOperationConditionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeImageEventOperationConditionResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeImageEventOperationConditionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeImageEventOperationConditionResponseBodyData(DaraModel):
    def __init__(
        self,
        event_type: str = None,
        operations: List[main_models.DescribeImageEventOperationConditionResponseBodyDataOperations] = None,
        scenarios: List[str] = None,
    ):
        # The alert type.
        # 
        # *   Only **sensitiveFile** may be returned.
        self.event_type = event_type
        # The operations.
        self.operations = operations
        # The application scopes of the rules.
        self.scenarios = scenarios

    def validate(self):
        if self.operations:
            for v1 in self.operations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_type is not None:
            result['EventType'] = self.event_type

        result['Operations'] = []
        if self.operations is not None:
            for k1 in self.operations:
                result['Operations'].append(k1.to_map() if k1 else None)

        if self.scenarios is not None:
            result['Scenarios'] = self.scenarios

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        self.operations = []
        if m.get('Operations') is not None:
            for k1 in m.get('Operations'):
                temp_model = main_models.DescribeImageEventOperationConditionResponseBodyDataOperations()
                self.operations.append(temp_model.from_map(k1))

        if m.get('Scenarios') is not None:
            self.scenarios = m.get('Scenarios')

        return self

class DescribeImageEventOperationConditionResponseBodyDataOperations(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.DescribeImageEventOperationConditionResponseBodyDataOperationsConditions] = None,
        operation_code: str = None,
        operation_name: str = None,
    ):
        # The rule conditions.
        self.conditions = conditions
        # The operation code.
        # 
        # *   Only **whitelist** may be returned, which indicates that the alert event is added to the whitelist.
        self.operation_code = operation_code
        # The name of the operation.
        self.operation_name = operation_name

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.operation_name is not None:
            result['OperationName'] = self.operation_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.DescribeImageEventOperationConditionResponseBodyDataOperationsConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('OperationName') is not None:
            self.operation_name = m.get('OperationName')

        return self

class DescribeImageEventOperationConditionResponseBodyDataOperationsConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_name: str = None,
        supported_mis_type: List[str] = None,
    ):
        # The keyword of the condition. Valid values:
        # 
        # *   **MD5**
        # *   **PATH**
        self.condition_key = condition_key
        # The name of the condition.
        self.condition_name = condition_name
        # The matching types.
        self.supported_mis_type = supported_mis_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_key is not None:
            result['ConditionKey'] = self.condition_key

        if self.condition_name is not None:
            result['ConditionName'] = self.condition_name

        if self.supported_mis_type is not None:
            result['SupportedMisType'] = self.supported_mis_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionKey') is not None:
            self.condition_key = m.get('ConditionKey')

        if m.get('ConditionName') is not None:
            self.condition_name = m.get('ConditionName')

        if m.get('SupportedMisType') is not None:
            self.supported_mis_type = m.get('SupportedMisType')

        return self

