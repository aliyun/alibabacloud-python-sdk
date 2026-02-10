# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityEventOperationsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        security_event_operations_response: List[main_models.DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponse] = None,
    ):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The operations that are performed to handle the alert.
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
                temp_model = main_models.DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponse()
                self.security_event_operations_response.append(temp_model.from_map(k1))

        return self

class DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponse(DaraModel):
    def __init__(
        self,
        mapping_mark_fields: List[main_models.DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMappingMarkFields] = None,
        mark_field: List[main_models.DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkField] = None,
        mark_fields_source: List[main_models.DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkFieldsSource] = None,
        operation_code: str = None,
        operation_params: str = None,
        user_can_operate: bool = None,
    ):
        # The objects on which the operations are performed. This parameter is required when you add the alert to the whitelist by configuring precise defense rules.
        self.mapping_mark_fields = mapping_mark_fields
        # The configurations that are used when the value of the OperationCode parameter is **advance_mark_mis_info**.
        self.mark_field = mark_field
        # The configuration items that can be used when the value of the OperationCode parameter is advance_mark_mis_info.
        self.mark_fields_source = mark_fields_source
        # The operation that is performed to handle the alert. Valid values:
        # 
        # *   **block_ip**: blocks the source IP address.
        # *   **advance_mark_mis_info**: adds the alert to the whitelist.
        # *   **ignore**: ignores the alert.
        # *   **manual_handled**: marks the alert as manually handled.
        # *   **kill_process**: terminates the malicious process.
        # *   **cleanup**: performs in-depth virus detection and removal.
        # *   **kill_and_quara**: terminates the malicious process and quarantines the source file.
        # *   **disable_malicious_defense**: disables the malicious behavior defense feature.
        # *   **client_problem_check**: performs troubleshooting.
        # *   **quara**: quarantines the source file of the malicious process.
        # *   **defense_mark_mis_info**: enables the precise defense feature but disables the notification feature.
        # *   **rm_defense_mark_mis_info**: enables the notification feature.
        # *   **rm_mark_mis_info**: removes the alert from the whitelist.
        # *   **cancle_manual**: cancels marking the alert as manually handled.
        self.operation_code = operation_code
        # The configuration of the operation that is performed to handle the alert.
        # 
        # >  If the value of the **OperationCode** parameter is **kill_and_quara** or **block_ip**, the OperationParams parameter is required. If the value of the **OperationCode** parameter is a different value, the OperationParams parameter can be left empty.
        self.operation_params = operation_params
        # Indicates whether you can handle the alert in the current edition of Security Center. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.user_can_operate = user_can_operate

    def validate(self):
        if self.mapping_mark_fields:
            for v1 in self.mapping_mark_fields:
                 if v1:
                    v1.validate()
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
        result['MappingMarkFields'] = []
        if self.mapping_mark_fields is not None:
            for k1 in self.mapping_mark_fields:
                result['MappingMarkFields'].append(k1.to_map() if k1 else None)

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
        self.mapping_mark_fields = []
        if m.get('MappingMarkFields') is not None:
            for k1 in m.get('MappingMarkFields'):
                temp_model = main_models.DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMappingMarkFields()
                self.mapping_mark_fields.append(temp_model.from_map(k1))

        self.mark_field = []
        if m.get('MarkField') is not None:
            for k1 in m.get('MarkField'):
                temp_model = main_models.DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkField()
                self.mark_field.append(temp_model.from_map(k1))

        self.mark_fields_source = []
        if m.get('MarkFieldsSource') is not None:
            for k1 in m.get('MarkFieldsSource'):
                temp_model = main_models.DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkFieldsSource()
                self.mark_fields_source.append(temp_model.from_map(k1))

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')

        if m.get('UserCanOperate') is not None:
            self.user_can_operate = m.get('UserCanOperate')

        return self

class DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkFieldsSource(DaraModel):
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
        # An array consisting of the operations that are supported by the method to add the alert event to the whitelist.
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

class DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMarkField(DaraModel):
    def __init__(
        self,
        filed_alias_name: str = None,
        filed_name: str = None,
        mark_mis_type: str = None,
        mark_mis_value: str = None,
        supported_mis_type: List[str] = None,
        uuid: str = None,
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
        # An array consisting of the operations that are supported by the method to add the alert event to the whitelist.
        self.supported_mis_type = supported_mis_type
        # The UUID of the server on which the alert event is detected.
        self.uuid = uuid

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

        if self.uuid is not None:
            result['Uuid'] = self.uuid

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

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeSecurityEventOperationsResponseBodySecurityEventOperationsResponseMappingMarkFields(DaraModel):
    def __init__(
        self,
        description: str = None,
        fill_type: str = None,
        max_length: int = None,
        min_length: int = None,
        name: str = None,
        required: bool = None,
        show_name: str = None,
        show_value: str = None,
        value: str = None,
    ):
        # The description of the field that is added to the whitelist.
        self.description = description
        # Indicates whether the value of the field can be changed.
        # 
        # *   **CUSTOM**: The value of the field can be changed.
        # *   **SYSTEM**: The value of the field cannot be changed.
        self.fill_type = fill_type
        # The maximum length of the field that is added to the whitelist.
        self.max_length = max_length
        # The minimum length of the field that is added to the whitelist.
        self.min_length = min_length
        # The name of the field that is added to the whitelist.
        self.name = name
        # Indicates whether the parameter is required. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.required = required
        # The display name of the field that can be used in the whitelist rule.
        self.show_name = show_name
        # The display name of the field that is added to the whitelist.
        self.show_value = show_value
        # The value of the field that is added to the whitelist.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.fill_type is not None:
            result['FillType'] = self.fill_type

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        if self.name is not None:
            result['Name'] = self.name

        if self.required is not None:
            result['Required'] = self.required

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.show_value is not None:
            result['ShowValue'] = self.show_value

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FillType') is not None:
            self.fill_type = m.get('FillType')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('ShowValue') is not None:
            self.show_value = m.get('ShowValue')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

