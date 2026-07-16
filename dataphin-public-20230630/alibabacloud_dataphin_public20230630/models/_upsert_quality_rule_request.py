# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpsertQualityRuleRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        upsert_command: main_models.UpsertQualityRuleRequestUpsertCommand = None,
    ):
        # Tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The upsert command.
        # 
        # This parameter is required.
        self.upsert_command = upsert_command

    def validate(self):
        if self.upsert_command:
            self.upsert_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.upsert_command is not None:
            result['UpsertCommand'] = self.upsert_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpsertCommand') is not None:
            temp_model = main_models.UpsertQualityRuleRequestUpsertCommand()
            self.upsert_command = temp_model.from_map(m.get('UpsertCommand'))

        return self

class UpsertQualityRuleRequestUpsertCommand(DaraModel):
    def __init__(
        self,
        attribute_with_value_list: List[main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueList] = None,
        catalog_list: List[str] = None,
        description: str = None,
        enable_error_archive: bool = None,
        form_property_list: List[main_models.UpsertQualityRuleRequestUpsertCommandFormPropertyList] = None,
        id: int = None,
        name: str = None,
        strength: str = None,
        template_id: int = None,
        template_type: str = None,
        validate_condition_list: List[main_models.UpsertQualityRuleRequestUpsertCommandValidateConditionList] = None,
        watch_id: int = None,
    ):
        # The rule business attribute configuration.
        self.attribute_with_value_list = attribute_with_value_list
        # The rule category. Valid values: CONSISTENT (Consistency), EFFECTIVE (Effectiveness), TIMELINESE (Timeliness), ACCURATE (Accuracy), UNIQUENESS (Uniqueness), COMPLETENESS (Completeness), STABILITY (Stability), CUSTOM (Custom).
        # 
        # This parameter is required.
        self.catalog_list = catalog_list
        # The description of the quality rule.
        self.description = description
        # Specifies whether to enable error archiving.
        self.enable_error_archive = enable_error_archive
        # The rule configuration key-value pairs. The configuration varies based on the template type. Different template types return different form key-value pair configurations.
        self.form_property_list = form_property_list
        # Rule ID. A non-empty value indicates a modification, and an empty value indicates a creation.
        self.id = id
        # The name of the quality rule.
        # 
        # This parameter is required.
        self.name = name
        # The rule strength. Valid values: STRONG, WEAK.
        # 
        # This parameter is required.
        self.strength = strength
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The template type. Valid values:
        #   - FIELD_NULL_VALUE_VALIDATE: Field null value validation
        #   - FIELD_EMPTY_STRING_VALIDATE: Field empty string validation
        #   - FIELD_UNIQUE_VALIDATE: Field uniqueness validation
        #   - FIELD_GROUP_COUNT_VALIDATE: Field unique value count validation
        #   - FIELD_DUPLICATE_VALUE_COUNT_VALIDATE: Field duplicate value count validation
        #   - FUNCTION_TIME_COMPARE: Time function comparison
        #   - SINGLE_TABLE_TIME_COMPARE: Single-table time field comparison
        #   - DOUBLE_TABLE_TIME_COMPARE: Cross-table time field comparison
        #   - FIELD_FORMAT_VALIDATE: Field format validation
        #   - FIELD_LENGTH_VALIDATE: Field length validation
        #   - FIELD_VALUE_RANGE_VALIDATE: Field value range validation
        #   - CODE_TABLE_COMPARE: Code table reference comparison
        #   - STANDARD_CODE_TABLE_COMPARE: Data standard code table reference comparison
        #   - SINGLE_TABLE_FIELD_VALUE_COMPARE: Single-table field value consistency comparison
        #   - SINGLE_TABLE_FIELD_STATISTICAL_COMPARE: Single-table field statistical value consistency comparison
        #   - SINGLE_TABLE_FIELD_EXP_COMPARE: Single-table field business logic consistency comparison
        #   - DOUBLE_TABLE_FIELD_VALUE_COMPARE: Cross-table field value consistency comparison
        #   - DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: Cross-table field statistical value consistency comparison
        #   - CROSS_DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: Cross-source cross-table field statistical value consistency comparison
        #   - DOUBLE_TABLE_FIELD_EXP_COMPARE: Cross-table field business logic consistency comparison
        #   - TABLE_STABILITY_VALIDATE: Table stability validation
        #   - TABLE_FLUCTUATION_VALIDATE: Table fluctuation validation
        #   - FIELD_STABILITY_VALIDATE: Field stability validation
        #   - FIELD_FLUCTUATION_VALIDATE: Field fluctuation validation
        #   - CUSTOM_STATISTICAL_VALIDATE: Custom statistical metric validation
        #   - CUSTOM_DATA_DETAILS_VALIDATE: Custom data details validation
        #   - DATASOURCE_AVAILABLE_CHECK: Data source connectivity check
        #   - TABLE_SCHEMA_CHECK: Table schema change monitoring
        #   - REAL_TIME_OFFLINE_COMPARE: Real-time offline comparison
        #   - REAL_TIME_STATISTICAL_VALIDATE: Real-time statistical value monitoring
        #   - REAL_TIME_MULTI_CHAIN_COMPARE: Real-time multi-chain comparison, etc.
        # 
        # This parameter is required.
        self.template_type = template_type
        # The validation conditions.
        self.validate_condition_list = validate_condition_list
        # The ID of the associated monitor.
        # 
        # This parameter is required.
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
        if self.validate_condition_list:
            for v1 in self.validate_condition_list:
                 if v1:
                    v1.validate()

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

        if self.name is not None:
            result['Name'] = self.name

        if self.strength is not None:
            result['Strength'] = self.strength

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        result['ValidateConditionList'] = []
        if self.validate_condition_list is not None:
            for k1 in self.validate_condition_list:
                result['ValidateConditionList'].append(k1.to_map() if k1 else None)

        if self.watch_id is not None:
            result['WatchId'] = self.watch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_with_value_list = []
        if m.get('AttributeWithValueList') is not None:
            for k1 in m.get('AttributeWithValueList'):
                temp_model = main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueList()
                self.attribute_with_value_list.append(temp_model.from_map(k1))

        if m.get('CatalogList') is not None:
            self.catalog_list = m.get('CatalogList')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableErrorArchive') is not None:
            self.enable_error_archive = m.get('EnableErrorArchive')

        self.form_property_list = []
        if m.get('FormPropertyList') is not None:
            for k1 in m.get('FormPropertyList'):
                temp_model = main_models.UpsertQualityRuleRequestUpsertCommandFormPropertyList()
                self.form_property_list.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Strength') is not None:
            self.strength = m.get('Strength')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        self.validate_condition_list = []
        if m.get('ValidateConditionList') is not None:
            for k1 in m.get('ValidateConditionList'):
                temp_model = main_models.UpsertQualityRuleRequestUpsertCommandValidateConditionList()
                self.validate_condition_list.append(temp_model.from_map(k1))

        if m.get('WatchId') is not None:
            self.watch_id = m.get('WatchId')

        return self

class UpsertQualityRuleRequestUpsertCommandValidateConditionList(DaraModel):
    def __init__(
        self,
        id: str = None,
        metric: str = None,
        operator: str = None,
        parent_id: str = None,
        type: str = None,
        value: str = None,
    ):
        # The ID of the condition node.
        self.id = id
        # The metric.
        self.metric = metric
        # The operator. Valid values: EQUAL, NOT_EQUAL, LARGER, SMALLER, LARGE_OR_EQUAL, SMALLER_OR_EQUAL, AND, OR.
        self.operator = operator
        # The ID of the parent condition node.
        self.parent_id = parent_id
        # The condition type. Valid values: RELATION, EXPRESSION.
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

        if self.operator is not None:
            result['Operator'] = self.operator

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

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpsertQualityRuleRequestUpsertCommandFormPropertyList(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        name: str = None,
        value: str = None,
    ):
        # The component type.
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

class UpsertQualityRuleRequestUpsertCommandAttributeWithValueList(DaraModel):
    def __init__(
        self,
        attribute_info: main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeInfo = None,
        attribute_value: main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeValue = None,
    ):
        # The attribute details.
        self.attribute_info = attribute_info
        # The attribute value.
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
            temp_model = main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeInfo()
            self.attribute_info = temp_model.from_map(m.get('AttributeInfo'))

        if m.get('AttributeValue') is not None:
            temp_model = main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeValue()
            self.attribute_value = temp_model.from_map(m.get('AttributeValue'))

        return self

class UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeValue(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
        value_list: List[str] = None,
    ):
        # Specifies whether to include the maximum value.
        self.include_max_value = include_max_value
        # Specifies whether to include the minimum value.
        self.include_min_value = include_min_value
        # The maximum value. Applicable to range interval attributes.
        self.max_value = max_value
        # The minimum value. Applicable to range interval attributes.
        self.min_value = min_value
        # The attribute value list. Applicable to attributes with the custom input, single-select dropdown, or multi-select dropdown input method.
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

class UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeInfo(DaraModel):
    def __init__(
        self,
        description: str = None,
        enabled: bool = None,
        id: int = None,
        name: str = None,
        required: bool = None,
        searchable: bool = None,
        value_config: main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeInfoValueConfig = None,
    ):
        # The description.
        self.description = description
        # Specifies whether to enable the attribute.
        self.enabled = enabled
        # The attribute ID.
        self.id = id
        # The attribute name.
        self.name = name
        # Specifies whether the attribute is required.
        self.required = required
        # Specifies whether the attribute is searchable.
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
            temp_model = main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeInfoValueConfig()
            self.value_config = temp_model.from_map(m.get('ValueConfig'))

        return self

class UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeInfoValueConfig(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        default_value: main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeInfoValueConfigDefaultValue = None,
        length: int = None,
        type: str = None,
        value_enum_list: List[str] = None,
    ):
        # The attribute field type. Valid values: STRING (Text), BIGINT (Integer), DOUBLE (Floating-point), BOOLEAN (Boolean), DATE (Date), DATETIME (Datetime).
        self.data_type = data_type
        # The attribute default value.
        self.default_value = default_value
        # The attribute field length. Used to constrain the maximum length of text-type attribute values.
        self.length = length
        # The attribute value input method. Valid values: CUSTOMIZED (Custom input), SINGLE_ENUM (Single-select dropdown), MULTIPLE_ENUMS (Multi-select dropdown), RANGE (Range interval).
        self.type = type
        # The attribute option values. Only applicable to attributes with the single-select dropdown or multi-select dropdown input method.
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
            temp_model = main_models.UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeInfoValueConfigDefaultValue()
            self.default_value = temp_model.from_map(m.get('DefaultValue'))

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueEnumList') is not None:
            self.value_enum_list = m.get('ValueEnumList')

        return self

class UpsertQualityRuleRequestUpsertCommandAttributeWithValueListAttributeInfoValueConfigDefaultValue(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
        value_list: List[str] = None,
    ):
        # Specifies whether to include the maximum value.
        self.include_max_value = include_max_value
        # Specifies whether to include the minimum value.
        self.include_min_value = include_min_value
        # The maximum value. Applicable to range interval attributes.
        self.max_value = max_value
        # The minimum value. Applicable to range interval attributes.
        self.min_value = min_value
        # The attribute value list. Applicable to attributes with the custom input, single-select dropdown, or multi-select dropdown input method.
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

