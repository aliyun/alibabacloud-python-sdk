# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListSensitiveColumnInfoResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        sensitive_column_list: main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnList = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The request ID. You can use the request ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # The details of the sensitive field.
        self.sensitive_column_list = sensitive_column_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The total number of entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.sensitive_column_list:
            self.sensitive_column_list.validate()

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

        if self.sensitive_column_list is not None:
            result['SensitiveColumnList'] = self.sensitive_column_list.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SensitiveColumnList') is not None:
            temp_model = main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnList()
            self.sensitive_column_list = temp_model.from_map(m.get('SensitiveColumnList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSensitiveColumnInfoResponseBodySensitiveColumnList(DaraModel):
    def __init__(
        self,
        sensitive_column: List[main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumn] = None,
    ):
        self.sensitive_column = sensitive_column

    def validate(self):
        if self.sensitive_column:
            for v1 in self.sensitive_column:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SensitiveColumn'] = []
        if self.sensitive_column is not None:
            for k1 in self.sensitive_column:
                result['SensitiveColumn'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sensitive_column = []
        if m.get('SensitiveColumn') is not None:
            for k1 in m.get('SensitiveColumn'):
                temp_model = main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumn()
                self.sensitive_column.append(temp_model.from_map(k1))

        return self

class ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumn(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        column_name: str = None,
        default_desensitization_rule: main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumnDefaultDesensitizationRule = None,
        instance_id: int = None,
        is_plain: bool = None,
        sample_data: str = None,
        schema_name: str = None,
        security_level: str = None,
        semi_desensitization_rule_list: main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumnSemiDesensitizationRuleList = None,
        table_name: str = None,
        user_sensitivity_level: str = None,
    ):
        # The name of the category.
        self.category_name = category_name
        # The name of the sensitive field.
        self.column_name = column_name
        # The information about the default masking algorithm.
        self.default_desensitization_rule = default_desensitization_rule
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the sensitive field is displayed in plaintext.
        self.is_plain = is_plain
        # The sample data.
        self.sample_data = sample_data
        # The name of the database.
        self.schema_name = schema_name
        # The sensitivity level of the field. Valid values:
        # 
        # *   Low
        # *   Medium
        # *   High
        self.security_level = security_level
        # The list of partial masking algorithms.
        self.semi_desensitization_rule_list = semi_desensitization_rule_list
        # The name of the table.
        self.table_name = table_name
        # The user-defined sensitivity level.
        self.user_sensitivity_level = user_sensitivity_level

    def validate(self):
        if self.default_desensitization_rule:
            self.default_desensitization_rule.validate()
        if self.semi_desensitization_rule_list:
            self.semi_desensitization_rule_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.default_desensitization_rule is not None:
            result['DefaultDesensitizationRule'] = self.default_desensitization_rule.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_plain is not None:
            result['IsPlain'] = self.is_plain

        if self.sample_data is not None:
            result['SampleData'] = self.sample_data

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.semi_desensitization_rule_list is not None:
            result['SemiDesensitizationRuleList'] = self.semi_desensitization_rule_list.to_map()

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.user_sensitivity_level is not None:
            result['UserSensitivityLevel'] = self.user_sensitivity_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DefaultDesensitizationRule') is not None:
            temp_model = main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumnDefaultDesensitizationRule()
            self.default_desensitization_rule = temp_model.from_map(m.get('DefaultDesensitizationRule'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsPlain') is not None:
            self.is_plain = m.get('IsPlain')

        if m.get('SampleData') is not None:
            self.sample_data = m.get('SampleData')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('SemiDesensitizationRuleList') is not None:
            temp_model = main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumnSemiDesensitizationRuleList()
            self.semi_desensitization_rule_list = temp_model.from_map(m.get('SemiDesensitizationRuleList'))

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('UserSensitivityLevel') is not None:
            self.user_sensitivity_level = m.get('UserSensitivityLevel')

        return self

class ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumnSemiDesensitizationRuleList(DaraModel):
    def __init__(
        self,
        semi_desensitization_rule: List[main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumnSemiDesensitizationRuleListSemiDesensitizationRule] = None,
    ):
        self.semi_desensitization_rule = semi_desensitization_rule

    def validate(self):
        if self.semi_desensitization_rule:
            for v1 in self.semi_desensitization_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SemiDesensitizationRule'] = []
        if self.semi_desensitization_rule is not None:
            for k1 in self.semi_desensitization_rule:
                result['SemiDesensitizationRule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.semi_desensitization_rule = []
        if m.get('SemiDesensitizationRule') is not None:
            for k1 in m.get('SemiDesensitizationRule'):
                temp_model = main_models.ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumnSemiDesensitizationRuleListSemiDesensitizationRule()
                self.semi_desensitization_rule.append(temp_model.from_map(k1))

        return self

class ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumnSemiDesensitizationRuleListSemiDesensitizationRule(DaraModel):
    def __init__(
        self,
        rule_id: int = None,
        rule_name: str = None,
    ):
        # The ID of the partial masking algorithm.
        self.rule_id = rule_id
        # The partial masking algorithm name.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class ListSensitiveColumnInfoResponseBodySensitiveColumnListSensitiveColumnDefaultDesensitizationRule(DaraModel):
    def __init__(
        self,
        rule_id: int = None,
        rule_name: str = None,
    ):
        # The masking algorithm ID.
        self.rule_id = rule_id
        # The masking algorithm name.
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

