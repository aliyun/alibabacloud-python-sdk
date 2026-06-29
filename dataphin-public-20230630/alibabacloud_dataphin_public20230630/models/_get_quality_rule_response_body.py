# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetQualityRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        quality_rule_info: main_models.GetQualityRuleResponseBodyQualityRuleInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # The quality rule details.
        self.quality_rule_info = quality_rule_info
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.quality_rule_info:
            self.quality_rule_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.quality_rule_info is not None:
            result['QualityRuleInfo'] = self.quality_rule_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('QualityRuleInfo') is not None:
            temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfo()
            self.quality_rule_info = temp_model.from_map(m.get('QualityRuleInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityRuleResponseBodyQualityRuleInfo(DaraModel):
    def __init__(
        self,
        attribute_with_value_list: List[main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueList] = None,
        catalog_list: List[str] = None,
        create_time: str = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        enable_error_archive: bool = None,
        form_property_list: List[main_models.GetQualityRuleResponseBodyQualityRuleInfoFormPropertyList] = None,
        id: int = None,
        modifier: str = None,
        modifier_name: str = None,
        modify_time: str = None,
        name: str = None,
        schedule_bind_list: List[main_models.GetQualityRuleResponseBodyQualityRuleInfoScheduleBindList] = None,
        status: str = None,
        strength: str = None,
        template_id: int = None,
        template_name: str = None,
        template_scope: str = None,
        template_type: str = None,
        test_run_rule_task_id: int = None,
        test_run_rule_task_status: str = None,
        test_run_rule_validate_result: bool = None,
        validate_condition_list: List[main_models.GetQualityRuleResponseBodyQualityRuleInfoValidateConditionList] = None,
        validate_object: main_models.GetQualityRuleResponseBodyQualityRuleInfoValidateObject = None,
        watch_id: int = None,
    ):
        # The rule business attribute configurations.
        self.attribute_with_value_list = attribute_with_value_list
        # The rule categories. Valid values:
        # - CONSISTENT: consistency
        # - EFFECTIVE: validity
        # - TIMELINESE: timeliness
        # - ACCURATE: accuracy
        # - UNIQUENESS: uniqueness
        # - COMPLETENESS: completeness
        # - STABILITY: stability
        # - CUSTOM: custom.
        self.catalog_list = catalog_list
        # The creation time.
        self.create_time = create_time
        # The creator.
        self.creator = creator
        # The creator name.
        self.creator_name = creator_name
        # The description.
        self.description = description
        # Indicates whether exception archiving is enabled.
        self.enable_error_archive = enable_error_archive
        # The rule configuration key-value pairs. These vary by templatetype. Different templatetypes return different form key-value pair configurations.
        self.form_property_list = form_property_list
        # The quality rule ID.
        self.id = id
        # The ID of the user who last modified the rule.
        self.modifier = modifier
        # The name of the user who last modified the rule.
        self.modifier_name = modifier_name
        # The modification time.
        self.modify_time = modify_time
        # The quality rule name.
        self.name = name
        # The list of schedules bound to the rule.
        self.schedule_bind_list = schedule_bind_list
        # The quality rule status. Valid values:
        # - ENABLE
        # - DISABLE.
        self.status = status
        # The rule strength. Valid values:
        # - STRONG
        # - WEAK.
        self.strength = strength
        # The template ID.
        self.template_id = template_id
        # The template name.
        self.template_name = template_name
        # The templatetype group. Valid values:
        # - SYSTEM: system preset
        # - CUSTOM: custom template
        # - TEMPLATE: union of SYSTEM and CUSTOM
        # - CUSTOM_SQL: custom SQL template.
        self.template_scope = template_scope
        # The templatetype. Valid values:
        #   - FIELD_NULL_VALUE_VALIDATE: field null value check
        #   - FIELD_EMPTY_STRING_VALIDATE: field empty character string check
        #   - FIELD_UNIQUE_VALIDATE: field uniqueness check
        #   - FIELD_GROUP_COUNT_VALIDATE: field unique value count check
        #   - FIELD_DUPLICATE_VALUE_COUNT_VALIDATE: field duplicate value count check
        #   - FUNCTION_TIME_COMPARE: time function comparison
        #   - SINGLE_TABLE_TIME_COMPARE: non-partitioned table time field comparison
        #   - DOUBLE_TABLE_TIME_COMPARE: two-table time field comparison
        #   - FIELD_FORMAT_VALIDATE: field format check
        #   - FIELD_LENGTH_VALIDATE: field length check
        #   - FIELD_VALUE_RANGE_VALIDATE: field value range check
        #   - CODE_TABLE_COMPARE: lookup table reference comparison
        #   - STANDARD_CODE_TABLE_COMPARE: data standard lookup table reference comparison
        #   - SINGLE_TABLE_FIELD_VALUE_COMPARE: non-partitioned table field value consistency comparison
        #   - SINGLE_TABLE_FIELD_STATISTICAL_COMPARE: non-partitioned table field statistical value consistency comparison
        #   - SINGLE_TABLE_FIELD_EXP_COMPARE: non-partitioned table field business logic consistency comparison
        #   - DOUBLE_TABLE_FIELD_VALUE_COMPARE: two-table field value consistency comparison
        #   - DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: two-table field statistical value consistency comparison
        #   - CROSS_DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: cross-source two-table field statistical value consistency comparison
        #   - DOUBLE_TABLE_FIELD_EXP_COMPARE: two-table field business logic consistency comparison
        #   - TABLE_STABILITY_VALIDATE: table stability check
        #   - TABLE_FLUCTUATION_VALIDATE: table fluctuation check
        #   - FIELD_STABILITY_VALIDATE: field stability check
        #   - FIELD_FLUCTUATION_VALIDATE: field fluctuation check
        #   - CUSTOM_STATISTICAL_VALIDATE: custom statistical metric check
        #   - CUSTOM_DATA_DETAILS_VALIDATE: custom data details check
        #   - DATASOURCE_AVAILABLE_CHECK: data source connectivity monitoring
        #   - TABLE_SCHEMA_CHECK: table schema change monitoring
        #   - REAL_TIME_OFFLINE_COMPARE: real-time and offline comparison
        #   - REAL_TIME_STATISTICAL_VALIDATE: real-time statistical value monitoring
        #   - REAL_TIME_MULTI_CHAIN_COMPARE: real-time multi-link comparison, and more.
        self.template_type = template_type
        # The ID of the most recent test run task.
        self.test_run_rule_task_id = test_run_rule_task_id
        # The status of the most recent test run task. Valid values: NOT_RUN, WAITING, RUNNING, SUCCESS, FAILED.
        self.test_run_rule_task_status = test_run_rule_task_status
        # Indicates whether the test run validation passed.
        self.test_run_rule_validate_result = test_run_rule_validate_result
        # The list of validation conditions.
        self.validate_condition_list = validate_condition_list
        # The validation object.
        self.validate_object = validate_object
        # The ID of the associated monitoring task.
        self.watch_id = watch_id

    def validate(self):
        if self.attribute_with_value_list:
            for v1 in self.attribute_with_value_list:
                 if v1:
                    v1.validate()
        if self.form_property_list:
            for v1 in self.form_property_list:
                 if v1:
                    v1.validate()
        if self.schedule_bind_list:
            for v1 in self.schedule_bind_list:
                 if v1:
                    v1.validate()
        if self.validate_condition_list:
            for v1 in self.validate_condition_list:
                 if v1:
                    v1.validate()
        if self.validate_object:
            self.validate_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeWithValueList'] = []
        if self.attribute_with_value_list is not None:
            for k1 in self.attribute_with_value_list:
                result['AttributeWithValueList'].append(k1.to_map() if k1 else None)

        if self.catalog_list is not None:
            result['CatalogList'] = self.catalog_list

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_error_archive is not None:
            result['EnableErrorArchive'] = self.enable_error_archive

        result['FormPropertyList'] = []
        if self.form_property_list is not None:
            for k1 in self.form_property_list:
                result['FormPropertyList'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modifier_name is not None:
            result['ModifierName'] = self.modifier_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        result['ScheduleBindList'] = []
        if self.schedule_bind_list is not None:
            for k1 in self.schedule_bind_list:
                result['ScheduleBindList'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        if self.strength is not None:
            result['Strength'] = self.strength

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_scope is not None:
            result['TemplateScope'] = self.template_scope

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.test_run_rule_task_id is not None:
            result['TestRunRuleTaskId'] = self.test_run_rule_task_id

        if self.test_run_rule_task_status is not None:
            result['TestRunRuleTaskStatus'] = self.test_run_rule_task_status

        if self.test_run_rule_validate_result is not None:
            result['TestRunRuleValidateResult'] = self.test_run_rule_validate_result

        result['ValidateConditionList'] = []
        if self.validate_condition_list is not None:
            for k1 in self.validate_condition_list:
                result['ValidateConditionList'].append(k1.to_map() if k1 else None)

        if self.validate_object is not None:
            result['ValidateObject'] = self.validate_object.to_map()

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_with_value_list = []
        if m.get('AttributeWithValueList') is not None:
            for k1 in m.get('AttributeWithValueList'):
                temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueList()
                self.attribute_with_value_list.append(temp_model.from_map(k1))

        if m.get('CatalogList') is not None:
            self.catalog_list = m.get('CatalogList')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableErrorArchive') is not None:
            self.enable_error_archive = m.get('EnableErrorArchive')

        self.form_property_list = []
        if m.get('FormPropertyList') is not None:
            for k1 in m.get('FormPropertyList'):
                temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfoFormPropertyList()
                self.form_property_list.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifierName') is not None:
            self.modifier_name = m.get('ModifierName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.schedule_bind_list = []
        if m.get('ScheduleBindList') is not None:
            for k1 in m.get('ScheduleBindList'):
                temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfoScheduleBindList()
                self.schedule_bind_list.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strength') is not None:
            self.strength = m.get('Strength')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateScope') is not None:
            self.template_scope = m.get('TemplateScope')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TestRunRuleTaskId') is not None:
            self.test_run_rule_task_id = m.get('TestRunRuleTaskId')

        if m.get('TestRunRuleTaskStatus') is not None:
            self.test_run_rule_task_status = m.get('TestRunRuleTaskStatus')

        if m.get('TestRunRuleValidateResult') is not None:
            self.test_run_rule_validate_result = m.get('TestRunRuleValidateResult')

        self.validate_condition_list = []
        if m.get('ValidateConditionList') is not None:
            for k1 in m.get('ValidateConditionList'):
                temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfoValidateConditionList()
                self.validate_condition_list.append(temp_model.from_map(k1))

        if m.get('ValidateObject') is not None:
            temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfoValidateObject()
            self.validate_object = temp_model.from_map(m.get('ValidateObject'))

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

class GetQualityRuleResponseBodyQualityRuleInfoValidateObject(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The validation object name.
        self.name = name
        # The validation object type. Valid values: UNKNOWN, TABLE, COLUMN, DATASOURCE, DATASOURCE_TABLE, REALTIME, INDEX, CHAIN.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetQualityRuleResponseBodyQualityRuleInfoValidateConditionList(DaraModel):
    def __init__(
        self,
        id: str = None,
        metric: str = None,
        metric_name: str = None,
        operator: str = None,
        operator_name: str = None,
        parent_id: str = None,
        type: str = None,
        value: str = None,
    ):
        # The condition node ID.
        self.id = id
        # The metric.
        self.metric = metric
        # The metric name.
        self.metric_name = metric_name
        # The operator. Valid values: EQUAL, NOT_EQUAL, LARGER, SMALLER, LARGE_OR_EQUAL, SMALLER_OR_EQUAL, AND, OR.
        self.operator = operator
        # The operator name.
        self.operator_name = operator_name
        # The parent condition node ID.
        self.parent_id = parent_id
        # The condition type. Valid values:
        # - RELATION: relationship
        # - EXPRESSION: expression.
        self.type = type
        # The value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.metric is not None:
            result['Metric'] = self.metric

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Metric') is not None:
            self.metric = m.get('Metric')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetQualityRuleResponseBodyQualityRuleInfoScheduleBindList(DaraModel):
    def __init__(
        self,
        schedule_id: int = None,
        schedule_name: str = None,
    ):
        # The schedule ID.
        self.schedule_id = schedule_id
        # The schedule name.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id

        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')

        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')

        return self

class GetQualityRuleResponseBodyQualityRuleInfoFormPropertyList(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        name: str = None,
        value: str = None,
    ):
        # The control type.
        self.component_type = component_type
        # The property name.
        self.name = name
        # The property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueList(DaraModel):
    def __init__(
        self,
        attribute_info: main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeInfo = None,
        attribute_value: main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeValue = None,
    ):
        # The attribute details.
        self.attribute_info = attribute_info
        # The property value.
        self.attribute_value = attribute_value

    def validate(self):
        if self.attribute_info:
            self.attribute_info.validate()
        if self.attribute_value:
            self.attribute_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_info is not None:
            result['AttributeInfo'] = self.attribute_info.to_map()

        if self.attribute_value is not None:
            result['AttributeValue'] = self.attribute_value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeInfo') is not None:
            temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeInfo()
            self.attribute_info = temp_model.from_map(m.get('AttributeInfo'))

        if m.get('AttributeValue') is not None:
            temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeValue()
            self.attribute_value = temp_model.from_map(m.get('AttributeValue'))

        return self

class GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeValue(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
        value_list: List[str] = None,
    ):
        # Indicates whether the maximum value is included.
        self.include_max_value = include_max_value
        # Indicates whether the minimum value is included.
        self.include_min_value = include_min_value
        # The maximum value. This applies to range interval attributes.
        self.max_value = max_value
        # The minimum value. This applies to range interval attributes.
        self.min_value = min_value
        # The list of attribute values. This applies to attributes with custom input, single-select dropdown, or multi-select dropdown input methods.
        self.value_list = value_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_max_value is not None:
            result['IncludeMaxValue'] = self.include_max_value

        if self.include_min_value is not None:
            result['IncludeMinValue'] = self.include_min_value

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeMaxValue') is not None:
            self.include_max_value = m.get('IncludeMaxValue')

        if m.get('IncludeMinValue') is not None:
            self.include_min_value = m.get('IncludeMinValue')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

class GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        enabled: bool = None,
        id: int = None,
        name: str = None,
        required: bool = None,
        searchable: bool = None,
        value_config: main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeInfoValueConfig = None,
    ):
        # The description.
        self.description = description
        # Indicates whether the attribute is enabled.
        self.enabled = enabled
        # The attribute ID.
        self.id = id
        # The attribute name.
        self.name = name
        # Indicates whether the attribute is required.
        self.required = required
        # Indicates whether the attribute is searchable.
        self.searchable = searchable
        # The attribute value configuration details.
        self.value_config = value_config

    def validate(self):
        if self.value_config:
            self.value_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.required is not None:
            result['Required'] = self.required

        if self.searchable is not None:
            result['Searchable'] = self.searchable

        if self.value_config is not None:
            result['ValueConfig'] = self.value_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Searchable') is not None:
            self.searchable = m.get('Searchable')

        if m.get('ValueConfig') is not None:
            temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeInfoValueConfig()
            self.value_config = temp_model.from_map(m.get('ValueConfig'))

        return self

class GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeInfoValueConfig(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        default_value: main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeInfoValueConfigDefaultValue = None,
        length: int = None,
        type: str = None,
        value_enum_list: List[str] = None,
    ):
        # The attribute field data type. Valid values:
        # - STRING: text
        # - BIGINT: integer
        # - DOUBLE: floating-point
        # - BOOLEAN: Boolean
        # - DATE: date
        # - DATETIME: datetime.
        self.data_type = data_type
        # The attribute default value.
        self.default_value = default_value
        # The attribute field length. This constrains the maximum length of text-type attribute values.
        self.length = length
        # The attribute value input method. Valid values:
        # - CUSTOMIZED: custom input
        # - SINGLE_ENUM: single-select dropdown
        # - MULTIPLE_ENUMS: multi-select dropdown
        # - RANGE: range interval.
        self.type = type
        # The attribute option values. This applies only to attributes with a single-select dropdown or multi-select dropdown input method.
        self.value_enum_list = value_enum_list

    def validate(self):
        if self.default_value:
            self.default_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value.to_map()

        if self.length is not None:
            result['Length'] = self.length

        if self.type is not None:
            result['Type'] = self.type

        if self.value_enum_list is not None:
            result['ValueEnumList'] = self.value_enum_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DefaultValue') is not None:
            temp_model = main_models.GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeInfoValueConfigDefaultValue()
            self.default_value = temp_model.from_map(m.get('DefaultValue'))

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueEnumList') is not None:
            self.value_enum_list = m.get('ValueEnumList')

        return self

class GetQualityRuleResponseBodyQualityRuleInfoAttributeWithValueListAttributeInfoValueConfigDefaultValue(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
        value_list: List[str] = None,
    ):
        # Indicates whether the maximum value is included.
        self.include_max_value = include_max_value
        # Indicates whether the minimum value is included.
        self.include_min_value = include_min_value
        # The maximum value. This applies to range interval attributes.
        self.max_value = max_value
        # The minimum value. This applies to range interval attributes.
        self.min_value = min_value
        # The list of attribute values. This applies to attributes with custom input, single-select dropdown, or multi-select dropdown input methods.
        self.value_list = value_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.include_max_value is not None:
            result['IncludeMaxValue'] = self.include_max_value

        if self.include_min_value is not None:
            result['IncludeMinValue'] = self.include_min_value

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IncludeMaxValue') is not None:
            self.include_max_value = m.get('IncludeMaxValue')

        if m.get('IncludeMinValue') is not None:
            self.include_min_value = m.get('IncludeMinValue')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

