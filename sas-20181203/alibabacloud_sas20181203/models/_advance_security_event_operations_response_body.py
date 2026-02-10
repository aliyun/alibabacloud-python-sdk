# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AdvanceSecurityEventOperationsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_operations_response: List[main_models.AdvanceSecurityEventOperationsResponseBodySecurityEventOperationsResponse] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The operation performed on the alert event.
        self.security_event_operations_response = security_event_operations_response

    def validate(self):
        if self.security_event_operations_response:
            for v1 in self.security_event_operations_response:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecurityEventOperationsResponse'] = []
        if self.security_event_operations_response is not None:
            for k1 in self.security_event_operations_response:
                result['SecurityEventOperationsResponse'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_event_operations_response = []
        if m.get('SecurityEventOperationsResponse') is not None:
            for k1 in m.get('SecurityEventOperationsResponse'):
                temp_model = main_models.AdvanceSecurityEventOperationsResponseBodySecurityEventOperationsResponse()
                self.security_event_operations_response.append(temp_model.from_map(k1))

        return self

class AdvanceSecurityEventOperationsResponseBodySecurityEventOperationsResponse(DaraModel):
    def __init__(
        self,
        mark_field: List[main_models.AdvanceSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkField] = None,
        mark_fields_source: List[main_models.AdvanceSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkFieldsSource] = None,
        operation_code: str = None,
        operation_params: str = None,
        user_can_operate: bool = None,
    ):
        # The object on which the operation is performed. This parameter is required when you set the OperationCode parameter to **advance_mark_mis_info**.
        self.mark_field = mark_field
        # The metadata configuration returned by the advanced whitelist rule.
        self.mark_fields_source = mark_fields_source
        # The operation performed to handle the alert. Valid values:
        # 
        # *   **block_ip**: blocks the alert.
        # *   **advance_mark_mis_info**: adds the alert to the whitelist.
        # *   **ignore**: ignores the alert.
        # *   **manual_handled**: marks the alert as manually handled.
        # *   **kill_process**: terminates the malicious process.
        # *   **cleanup**: performs in-depth virus detection and removal.
        # *   **kill_and_quara**: performs virus detection and removal.
        # *   **disable_malicious_defense**: turns off malicious defense behavior.
        # *   **client_problem_check**: performs troubleshooting.
        # *   **quara**: performs quarantine operations.
        self.operation_code = operation_code
        # The configuration of the operation performed to handle the alert event.
        self.operation_params = operation_params
        # Indicates whether the operation can be performed.
        # 
        # *   **true**: The operation can be performed.
        # *   **false**: The operation cannot be performed.
        self.user_can_operate = user_can_operate

    def validate(self):
        if self.mark_field:
            for v1 in self.mark_field:
                 if v1:
                    v1.validate()
        if self.mark_fields_source:
            for v1 in self.mark_fields_source:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MarkField'] = []
        if self.mark_field is not None:
            for k1 in self.mark_field:
                result['MarkField'].append(k1.to_map() if k1 else None)

        result['MarkFieldsSource'] = []
        if self.mark_fields_source is not None:
            for k1 in self.mark_fields_source:
                result['MarkFieldsSource'].append(k1.to_map() if k1 else None)

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params

        if self.user_can_operate is not None:
            result['UserCanOperate'] = self.user_can_operate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mark_field = []
        if m.get('MarkField') is not None:
            for k1 in m.get('MarkField'):
                temp_model = main_models.AdvanceSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkField()
                self.mark_field.append(temp_model.from_map(k1))

        self.mark_fields_source = []
        if m.get('MarkFieldsSource') is not None:
            for k1 in m.get('MarkFieldsSource'):
                temp_model = main_models.AdvanceSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkFieldsSource()
                self.mark_fields_source.append(temp_model.from_map(k1))

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')

        if m.get('UserCanOperate') is not None:
            self.user_can_operate = m.get('UserCanOperate')

        return self

class AdvanceSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkFieldsSource(DaraModel):
    def __init__(
        self,
        filed_alias_name: str = None,
        filed_name: str = None,
        mark_mis_value: str = None,
        supported_mis_type: List[str] = None,
    ):
        # The alias of the field that can be used in the whitelist rule.
        self.filed_alias_name = filed_alias_name
        # The field that can be used in the whitelist rule.
        self.filed_name = filed_name
        # The value of the field that can be used in the whitelist rule.
        self.mark_mis_value = mark_mis_value
        # The operation that is supported in the whitelist rule. Valid values:
        # 
        # *   **contains**: contains
        # *   **notContains**: does not contain
        # *   **regex**: regular expression
        # *   **strEqual**: equals
        # *   **strNotEqual**: does not equal
        self.supported_mis_type = supported_mis_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filed_alias_name is not None:
            result['FiledAliasName'] = self.filed_alias_name

        if self.filed_name is not None:
            result['FiledName'] = self.filed_name

        if self.mark_mis_value is not None:
            result['MarkMisValue'] = self.mark_mis_value

        if self.supported_mis_type is not None:
            result['SupportedMisType'] = self.supported_mis_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FiledAliasName') is not None:
            self.filed_alias_name = m.get('FiledAliasName')

        if m.get('FiledName') is not None:
            self.filed_name = m.get('FiledName')

        if m.get('MarkMisValue') is not None:
            self.mark_mis_value = m.get('MarkMisValue')

        if m.get('SupportedMisType') is not None:
            self.supported_mis_type = m.get('SupportedMisType')

        return self

class AdvanceSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkField(DaraModel):
    def __init__(
        self,
        filed_alias_name: str = None,
        filed_name: str = None,
        mark_mis_type: str = None,
        mark_mis_value: str = None,
        supported_mis_type: List[str] = None,
    ):
        # The alias of the field that is used in the whitelist rule.
        self.filed_alias_name = filed_alias_name
        # The field that is used in the whitelist rule.
        self.filed_name = filed_name
        # The operation that is used in the whitelist rule. Valid values:
        # 
        # *   **contains**: contains
        # *   **notContains**: does not contain
        # *   **regex**: regular expression
        # *   **strEqual**: equals
        # *   **strNotEqual**: does not equal
        self.mark_mis_type = mark_mis_type
        # The value of the field that is used in the whitelist rule.
        self.mark_mis_value = mark_mis_value
        # The operation that is used and can be modified in the whitelist rule. Valid values:
        # 
        # *   **contains**: contains
        # *   **notContains**: does not contain
        # *   **regex**: regular expression
        # *   **strEqual**: equals
        # *   **strNotEqual**: does not equal
        self.supported_mis_type = supported_mis_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filed_alias_name is not None:
            result['FiledAliasName'] = self.filed_alias_name

        if self.filed_name is not None:
            result['FiledName'] = self.filed_name

        if self.mark_mis_type is not None:
            result['MarkMisType'] = self.mark_mis_type

        if self.mark_mis_value is not None:
            result['MarkMisValue'] = self.mark_mis_value

        if self.supported_mis_type is not None:
            result['SupportedMisType'] = self.supported_mis_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FiledAliasName') is not None:
            self.filed_alias_name = m.get('FiledAliasName')

        if m.get('FiledName') is not None:
            self.filed_name = m.get('FiledName')

        if m.get('MarkMisType') is not None:
            self.mark_mis_type = m.get('MarkMisType')

        if m.get('MarkMisValue') is not None:
            self.mark_mis_value = m.get('MarkMisValue')

        if m.get('SupportedMisType') is not None:
            self.supported_mis_type = m.get('SupportedMisType')

        return self

