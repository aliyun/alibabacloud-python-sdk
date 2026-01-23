# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListQualityRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListQualityRulesResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

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

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

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

        if m.get('PageResult') is not None:
            temp_model = main_models.ListQualityRulesResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListQualityRulesResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        quality_rule_list: List[main_models.ListQualityRulesResponseBodyPageResultQualityRuleList] = None,
        total_count: int = None,
    ):
        self.quality_rule_list = quality_rule_list
        self.total_count = total_count

    def validate(self):
        if self.quality_rule_list:
            for v1 in self.quality_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QualityRuleList'] = []
        if self.quality_rule_list is not None:
            for k1 in self.quality_rule_list:
                result['QualityRuleList'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.quality_rule_list = []
        if m.get('QualityRuleList') is not None:
            for k1 in m.get('QualityRuleList'):
                temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleList()
                self.quality_rule_list.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListQualityRulesResponseBodyPageResultQualityRuleList(DaraModel):
    def __init__(
        self,
        attribute_with_value_list: List[main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueList] = None,
        catalog_list: List[str] = None,
        create_time: str = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        enable_error_archive: bool = None,
        form_property_list: List[main_models.ListQualityRulesResponseBodyPageResultQualityRuleListFormPropertyList] = None,
        id: int = None,
        modifier: str = None,
        modifier_name: str = None,
        modify_time: str = None,
        name: str = None,
        schedule_bind_list: List[main_models.ListQualityRulesResponseBodyPageResultQualityRuleListScheduleBindList] = None,
        status: str = None,
        strength: str = None,
        template_id: int = None,
        template_name: str = None,
        template_scope: str = None,
        template_type: str = None,
        test_run_rule_task_id: int = None,
        test_run_rule_task_status: str = None,
        test_run_rule_validate_result: bool = None,
        validate_condition_list: List[main_models.ListQualityRulesResponseBodyPageResultQualityRuleListValidateConditionList] = None,
        validate_object: main_models.ListQualityRulesResponseBodyPageResultQualityRuleListValidateObject = None,
        watch_id: int = None,
    ):
        self.attribute_with_value_list = attribute_with_value_list
        self.catalog_list = catalog_list
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.enable_error_archive = enable_error_archive
        self.form_property_list = form_property_list
        self.id = id
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.modify_time = modify_time
        self.name = name
        self.schedule_bind_list = schedule_bind_list
        self.status = status
        self.strength = strength
        self.template_id = template_id
        self.template_name = template_name
        self.template_scope = template_scope
        self.template_type = template_type
        self.test_run_rule_task_id = test_run_rule_task_id
        self.test_run_rule_task_status = test_run_rule_task_status
        self.test_run_rule_validate_result = test_run_rule_validate_result
        self.validate_condition_list = validate_condition_list
        self.validate_object = validate_object
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
                temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueList()
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
                temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleListFormPropertyList()
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
                temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleListScheduleBindList()
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
                temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleListValidateConditionList()
                self.validate_condition_list.append(temp_model.from_map(k1))

        if m.get('ValidateObject') is not None:
            temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleListValidateObject()
            self.validate_object = temp_model.from_map(m.get('ValidateObject'))

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

class ListQualityRulesResponseBodyPageResultQualityRuleListValidateObject(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        self.name = name
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

class ListQualityRulesResponseBodyPageResultQualityRuleListValidateConditionList(DaraModel):
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
        self.id = id
        self.metric = metric
        self.metric_name = metric_name
        self.operator = operator
        self.operator_name = operator_name
        self.parent_id = parent_id
        self.type = type
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

class ListQualityRulesResponseBodyPageResultQualityRuleListScheduleBindList(DaraModel):
    def __init__(
        self,
        schedule_id: int = None,
        schedule_name: str = None,
    ):
        self.schedule_id = schedule_id
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

class ListQualityRulesResponseBodyPageResultQualityRuleListFormPropertyList(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        name: str = None,
        value: str = None,
    ):
        self.component_type = component_type
        self.name = name
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

class ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueList(DaraModel):
    def __init__(
        self,
        attribute_info: main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeInfo = None,
        attribute_value: main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeValue = None,
    ):
        self.attribute_info = attribute_info
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
            temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeInfo()
            self.attribute_info = temp_model.from_map(m.get('AttributeInfo'))

        if m.get('AttributeValue') is not None:
            temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeValue()
            self.attribute_value = temp_model.from_map(m.get('AttributeValue'))

        return self

class ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeValue(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
        value_list: List[str] = None,
    ):
        self.include_max_value = include_max_value
        self.include_min_value = include_min_value
        self.max_value = max_value
        self.min_value = min_value
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

class ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        enabled: bool = None,
        id: int = None,
        name: str = None,
        required: bool = None,
        searchable: bool = None,
        value_config: main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeInfoValueConfig = None,
    ):
        self.description = description
        self.enabled = enabled
        self.id = id
        self.name = name
        self.required = required
        self.searchable = searchable
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
            temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeInfoValueConfig()
            self.value_config = temp_model.from_map(m.get('ValueConfig'))

        return self

class ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeInfoValueConfig(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        default_value: main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeInfoValueConfigDefaultValue = None,
        length: int = None,
        type: str = None,
        value_enum_list: List[str] = None,
    ):
        self.data_type = data_type
        self.default_value = default_value
        self.length = length
        self.type = type
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
            temp_model = main_models.ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeInfoValueConfigDefaultValue()
            self.default_value = temp_model.from_map(m.get('DefaultValue'))

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueEnumList') is not None:
            self.value_enum_list = m.get('ValueEnumList')

        return self

class ListQualityRulesResponseBodyPageResultQualityRuleListAttributeWithValueListAttributeInfoValueConfigDefaultValue(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
        value_list: List[str] = None,
    ):
        self.include_max_value = include_max_value
        self.include_min_value = include_min_value
        self.max_value = max_value
        self.min_value = min_value
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

