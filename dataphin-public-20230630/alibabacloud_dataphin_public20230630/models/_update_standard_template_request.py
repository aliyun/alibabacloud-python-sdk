# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateStandardTemplateRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateStandardTemplateRequestUpdateCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The update command.
        # 
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateStandardTemplateRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        attributes_config: main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfig = None,
        code: str = None,
        code_rule_config: main_models.UpdateStandardTemplateRequestUpdateCommandCodeRuleConfig = None,
        description: str = None,
        id: int = None,
        maintainer_list: List[str] = None,
        name: str = None,
        publish_info: main_models.UpdateStandardTemplateRequestUpdateCommandPublishInfo = None,
        version: int = None,
    ):
        # The attribute configuration.
        # 
        # This parameter is required.
        self.attributes_config = attributes_config
        # The code of the standard template. The code must be globally unique. The code cannot be modified if the template is referenced.
        # 
        # This parameter is required.
        self.code = code
        # The configuration for automatic generation of standard codes.
        self.code_rule_config = code_rule_config
        # The description of the standard template.
        self.description = description
        # The ID of the standard template.
        # 
        # This parameter is required.
        self.id = id
        # The list of maintainers.
        self.maintainer_list = maintainer_list
        # The name of the standard template.
        # 
        # This parameter is required.
        self.name = name
        # The publish information of the standard template.
        self.publish_info = publish_info
        # The version number. If this parameter is left empty or set to -1, the latest version is used.
        self.version = version

    def validate(self):
        if self.attributes_config:
            self.attributes_config.validate()
        if self.code_rule_config:
            self.code_rule_config.validate()
        if self.publish_info:
            self.publish_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attributes_config is not None:
            result['AttributesConfig'] = self.attributes_config.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.code_rule_config is not None:
            result['CodeRuleConfig'] = self.code_rule_config.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.maintainer_list is not None:
            result['MaintainerList'] = self.maintainer_list

        if self.name is not None:
            result['Name'] = self.name

        if self.publish_info is not None:
            result['PublishInfo'] = self.publish_info.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributesConfig') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfig()
            self.attributes_config = temp_model.from_map(m.get('AttributesConfig'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeRuleConfig') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandCodeRuleConfig()
            self.code_rule_config = temp_model.from_map(m.get('CodeRuleConfig'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MaintainerList') is not None:
            self.maintainer_list = m.get('MaintainerList')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishInfo') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandPublishInfo()
            self.publish_info = temp_model.from_map(m.get('PublishInfo'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class UpdateStandardTemplateRequestUpdateCommandPublishInfo(DaraModel):
    def __init__(
        self,
        comment: str = None,
    ):
        # The publish comment.
        self.comment = comment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        return self

class UpdateStandardTemplateRequestUpdateCommandCodeRuleConfig(DaraModel):
    def __init__(
        self,
        auto_config: main_models.UpdateStandardTemplateRequestUpdateCommandCodeRuleConfigAutoConfig = None,
        generate_type: str = None,
    ):
        # The automatic generation configuration for standard code rules. This parameter takes effect when the generation method is set to AUTO_GENERATE.
        self.auto_config = auto_config
        # The standard code generation method. Valid values:
        # - CUSTOMIZED: custom.
        # - AUTO_GENERATE: automatically generated based on standard code rules.
        # 
        # This parameter is required.
        self.generate_type = generate_type

    def validate(self):
        if self.auto_config:
            self.auto_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config.to_map()

        if self.generate_type is not None:
            result['GenerateType'] = self.generate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoConfig') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandCodeRuleConfigAutoConfig()
            self.auto_config = temp_model.from_map(m.get('AutoConfig'))

        if m.get('GenerateType') is not None:
            self.generate_type = m.get('GenerateType')

        return self

class UpdateStandardTemplateRequestUpdateCommandCodeRuleConfigAutoConfig(DaraModel):
    def __init__(
        self,
        code_rule_list: List[main_models.UpdateStandardTemplateRequestUpdateCommandCodeRuleConfigAutoConfigCodeRuleList] = None,
        need_strong_validate: bool = None,
    ):
        # The standard code rules.
        # 
        # This parameter is required.
        self.code_rule_list = code_rule_list
        # Specifies whether strict validation is required.
        # 
        # This parameter is required.
        self.need_strong_validate = need_strong_validate

    def validate(self):
        if self.code_rule_list:
            for v1 in self.code_rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CodeRuleList'] = []
        if self.code_rule_list is not None:
            for k1 in self.code_rule_list:
                result['CodeRuleList'].append(k1.to_map() if k1 else None)

        if self.need_strong_validate is not None:
            result['NeedStrongValidate'] = self.need_strong_validate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.code_rule_list = []
        if m.get('CodeRuleList') is not None:
            for k1 in m.get('CodeRuleList'):
                temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandCodeRuleConfigAutoConfigCodeRuleList()
                self.code_rule_list.append(temp_model.from_map(k1))

        if m.get('NeedStrongValidate') is not None:
            self.need_strong_validate = m.get('NeedStrongValidate')

        return self

class UpdateStandardTemplateRequestUpdateCommandCodeRuleConfigAutoConfigCodeRuleList(DaraModel):
    def __init__(
        self,
        auto_increment_sequence_config: main_models.UpdateStandardTemplateRequestUpdateCommandCodeRuleConfigAutoConfigCodeRuleListAutoIncrementSequenceConfig = None,
        index: int = None,
        type: str = None,
        value: str = None,
    ):
        # The auto-increment sequence configuration.
        self.auto_increment_sequence_config = auto_increment_sequence_config
        # The position index of the code rule.
        # 
        # This parameter is required.
        self.index = index
        # The type of the code rule. Valid values:
        # - FIXED_STRING: fixed string.
        # - AUTO_INCREMENT: auto-increment sequence.
        # - STANDARD_SET_CODE: standard set code.
        # 
        # This parameter is required.
        self.type = type
        # The format or value of the code rule.
        self.value = value

    def validate(self):
        if self.auto_increment_sequence_config:
            self.auto_increment_sequence_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_increment_sequence_config is not None:
            result['AutoIncrementSequenceConfig'] = self.auto_increment_sequence_config.to_map()

        if self.index is not None:
            result['Index'] = self.index

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncrementSequenceConfig') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandCodeRuleConfigAutoConfigCodeRuleListAutoIncrementSequenceConfig()
            self.auto_increment_sequence_config = temp_model.from_map(m.get('AutoIncrementSequenceConfig'))

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateStandardTemplateRequestUpdateCommandCodeRuleConfigAutoConfigCodeRuleListAutoIncrementSequenceConfig(DaraModel):
    def __init__(
        self,
        digit: int = None,
        need_padding_zero: bool = None,
        start_value: int = None,
        step: int = None,
    ):
        # The number of digits.
        # 
        # This parameter is required.
        self.digit = digit
        # Specifies whether to pad with zeros.
        # 
        # This parameter is required.
        self.need_padding_zero = need_padding_zero
        # The start value.
        # 
        # This parameter is required.
        self.start_value = start_value
        # The step size.
        # 
        # This parameter is required.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.digit is not None:
            result['Digit'] = self.digit

        if self.need_padding_zero is not None:
            result['NeedPaddingZero'] = self.need_padding_zero

        if self.start_value is not None:
            result['StartValue'] = self.start_value

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digit') is not None:
            self.digit = m.get('Digit')

        if m.get('NeedPaddingZero') is not None:
            self.need_padding_zero = m.get('NeedPaddingZero')

        if m.get('StartValue') is not None:
            self.start_value = m.get('StartValue')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class UpdateStandardTemplateRequestUpdateCommandAttributesConfig(DaraModel):
    def __init__(
        self,
        attribute_list: List[main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeList] = None,
    ):
        # The list of attributes.
        # 
        # This parameter is required.
        self.attribute_list = attribute_list

    def validate(self):
        if self.attribute_list:
            for v1 in self.attribute_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeList'] = []
        if self.attribute_list is not None:
            for k1 in self.attribute_list:
                result['AttributeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_list = []
        if m.get('AttributeList') is not None:
            for k1 in m.get('AttributeList'):
                temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeList()
                self.attribute_list.append(temp_model.from_map(k1))

        return self

class UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeList(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        name: str = None,
        ref_attribute: main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListRefAttribute = None,
        required: bool = None,
        type: str = None,
        value_config: main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfig = None,
    ):
        # The attribute code. This parameter is optional when a common attribute is referenced.
        self.code = code
        # The description.
        self.description = description
        # The attribute name. This parameter is optional when a common attribute is referenced.
        self.name = name
        # The referenced attribute information.
        self.ref_attribute = ref_attribute
        # Specifies whether the attribute is required. This parameter is optional when a common attribute is referenced.
        self.required = required
        # The attribute type. This parameter is optional when a common attribute is referenced. Valid values:
        # - BIZ_ATTRIBUTE: business attribute.
        # - TECH_ATTRIBUTE: technical attribute.
        # - MANAGEMENT_ATTRIBUTE: management attribute.
        # - QUALITY_ATTRIBUTE: quality attribute.
        # - MASTER_DATA_ATTRIBUTE: master data attribute.
        # - LIFECYCLE_ATTRIBUTE: lifecycle attribute.
        # - SECURITY_ATTRIBUTE: security attribute.
        self.type = type
        # The value configuration. This parameter is optional when a common attribute is referenced.
        self.value_config = value_config

    def validate(self):
        if self.ref_attribute:
            self.ref_attribute.validate()
        if self.value_config:
            self.value_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.ref_attribute is not None:
            result['RefAttribute'] = self.ref_attribute.to_map()

        if self.required is not None:
            result['Required'] = self.required

        if self.type is not None:
            result['Type'] = self.type

        if self.value_config is not None:
            result['ValueConfig'] = self.value_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RefAttribute') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListRefAttribute()
            self.ref_attribute = temp_model.from_map(m.get('RefAttribute'))

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueConfig') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfig()
            self.value_config = temp_model.from_map(m.get('ValueConfig'))

        return self

class UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfig(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        default_value: str = None,
        length: int = None,
        type: str = None,
        value_range: main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfigValueRange = None,
    ):
        # The data type of the attribute value. Valid values:
        # - STRING: string.
        # - BIGINT: numeric.
        # - DOUBLE: floating-point.
        # - DATE: date, accurate to the day.
        # - DATETIME: date, accurate to milliseconds.
        # - BOOLEAN: Boolean.
        # 
        # This parameter is required.
        self.data_type = data_type
        # The default value.
        self.default_value = default_value
        # The length of the attribute value. If this parameter is left empty or set to -1, the length is not limited. Typically, only string types have a length limit for attribute values.
        self.length = length
        # The attribute value type. Valid values:
        # - CUSTOMIZED: custom input.
        # - SINGLE_ENUM: single enumeration value.
        # - MULTIPLE_ENUMS: multiple enumeration values.
        # - RANGE: range value.
        # 
        # This parameter is required.
        self.type = type
        # The value range.
        # 
        # This parameter is required.
        self.value_range = value_range

    def validate(self):
        if self.value_range:
            self.value_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.length is not None:
            result['Length'] = self.length

        if self.type is not None:
            result['Type'] = self.type

        if self.value_range is not None:
            result['ValueRange'] = self.value_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Length') is not None:
            self.length = m.get('Length')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueRange') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfigValueRange()
            self.value_range = temp_model.from_map(m.get('ValueRange'))

        return self

class UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfigValueRange(DaraModel):
    def __init__(
        self,
        dataphin_attribute_type: str = None,
        lookup_table_reference: main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfigValueRangeLookupTableReference = None,
        min_max_value_config: main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfigValueRangeMinMaxValueConfig = None,
        value_constraint: str = None,
        value_list: List[str] = None,
    ):
        # The value range. This parameter takes effect when the value source is set to DATAPHIN_ATTRIBUTE. Valid values:
        # - BIZ_UNIT: data board.
        # - PROJECT: project.
        # - USER: user.
        # - USER_GROUP: user group.
        self.dataphin_attribute_type = dataphin_attribute_type
        # The value range. This parameter takes effect when the value source is set to LOOKUP_TABLE.
        self.lookup_table_reference = lookup_table_reference
        # The value range. This parameter takes effect when the value source is set to MIN_MAX.
        self.min_max_value_config = min_max_value_config
        # The value source. Valid values:
        # - NONE: no constraint.
        # - LIST: obtained from a list.
        # - LOOKUP_TABLE: lookup table.
        # - MIN_MAX: value between the minimum and maximum.
        # - DATAPHIN_ATTRIBUTE: Dataphin system property.
        # - BUILT_IN_DATA_TYPES: built-in data types.
        # - BUILT_IN_DATA_CLASSIFICATION: built-in data categorization.
        # - BUILT_IN_DATA_LEVEL: built-in data security classification.
        # 
        # This parameter is required.
        self.value_constraint = value_constraint
        # The value range. This parameter takes effect when the value source is set to LIST.
        self.value_list = value_list

    def validate(self):
        if self.lookup_table_reference:
            self.lookup_table_reference.validate()
        if self.min_max_value_config:
            self.min_max_value_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataphin_attribute_type is not None:
            result['DataphinAttributeType'] = self.dataphin_attribute_type

        if self.lookup_table_reference is not None:
            result['LookupTableReference'] = self.lookup_table_reference.to_map()

        if self.min_max_value_config is not None:
            result['MinMaxValueConfig'] = self.min_max_value_config.to_map()

        if self.value_constraint is not None:
            result['ValueConstraint'] = self.value_constraint

        if self.value_list is not None:
            result['ValueList'] = self.value_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataphinAttributeType') is not None:
            self.dataphin_attribute_type = m.get('DataphinAttributeType')

        if m.get('LookupTableReference') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfigValueRangeLookupTableReference()
            self.lookup_table_reference = temp_model.from_map(m.get('LookupTableReference'))

        if m.get('MinMaxValueConfig') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfigValueRangeMinMaxValueConfig()
            self.min_max_value_config = temp_model.from_map(m.get('MinMaxValueConfig'))

        if m.get('ValueConstraint') is not None:
            self.value_constraint = m.get('ValueConstraint')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

class UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfigValueRangeMinMaxValueConfig(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
    ):
        # Specifies whether the maximum value is included.
        # 
        # This parameter is required.
        self.include_max_value = include_max_value
        # Specifies whether the minimum value is included.
        # 
        # This parameter is required.
        self.include_min_value = include_min_value
        # The maximum value.
        # 
        # This parameter is required.
        self.max_value = max_value
        # The minimum value.
        # 
        # This parameter is required.
        self.min_value = min_value

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

        return self

class UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListValueConfigValueRangeLookupTableReference(DaraModel):
    def __init__(
        self,
        column: str = None,
        lookup_table_id: int = None,
    ):
        # The referenced lookup table field.
        self.column = column
        # The ID of the lookup table.
        # 
        # This parameter is required.
        self.lookup_table_id = lookup_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.lookup_table_id is not None:
            result['LookupTableId'] = self.lookup_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('LookupTableId') is not None:
            self.lookup_table_id = m.get('LookupTableId')

        return self

class UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListRefAttribute(DaraModel):
    def __init__(
        self,
        attribute_from_info: main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListRefAttributeAttributeFromInfo = None,
        attribute_id: int = None,
    ):
        # The attribute source.
        # 
        # This parameter is required.
        self.attribute_from_info = attribute_from_info
        # The attribute ID.
        # 
        # This parameter is required.
        self.attribute_id = attribute_id

    def validate(self):
        if self.attribute_from_info:
            self.attribute_from_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_from_info is not None:
            result['AttributeFromInfo'] = self.attribute_from_info.to_map()

        if self.attribute_id is not None:
            result['AttributeId'] = self.attribute_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeFromInfo') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListRefAttributeAttributeFromInfo()
            self.attribute_from_info = temp_model.from_map(m.get('AttributeFromInfo'))

        if m.get('AttributeId') is not None:
            self.attribute_id = m.get('AttributeId')

        return self

class UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListRefAttributeAttributeFromInfo(DaraModel):
    def __init__(
        self,
        attribute_from: str = None,
        standard_reference: main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListRefAttributeAttributeFromInfoStandardReference = None,
    ):
        # The attribute source. Valid values:
        # - SYSTEM: system attribute.
        # - CUSTOM: custom attribute.
        # - STANDARD: standard.
        # 
        # This parameter is required.
        self.attribute_from = attribute_from
        # The corresponding standard. This parameter takes effect when the attribute source is set to STANDARD.
        self.standard_reference = standard_reference

    def validate(self):
        if self.standard_reference:
            self.standard_reference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_from is not None:
            result['AttributeFrom'] = self.attribute_from

        if self.standard_reference is not None:
            result['StandardReference'] = self.standard_reference.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeFrom') is not None:
            self.attribute_from = m.get('AttributeFrom')

        if m.get('StandardReference') is not None:
            temp_model = main_models.UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListRefAttributeAttributeFromInfoStandardReference()
            self.standard_reference = temp_model.from_map(m.get('StandardReference'))

        return self

class UpdateStandardTemplateRequestUpdateCommandAttributesConfigAttributeListRefAttributeAttributeFromInfoStandardReference(DaraModel):
    def __init__(
        self,
        standard_id: int = None,
        version: int = None,
    ):
        # The standard ID.
        # 
        # This parameter is required.
        self.standard_id = standard_id
        # The version number.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

