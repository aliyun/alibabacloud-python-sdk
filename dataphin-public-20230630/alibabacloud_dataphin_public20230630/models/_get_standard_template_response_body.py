# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetStandardTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        template_info: main_models.GetStandardTemplateResponseBodyTemplateInfo = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.template_info = template_info

    def validate(self):
        if self.template_info:
            self.template_info.validate()

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.template_info is not None:
            result['TemplateInfo'] = self.template_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TemplateInfo') is not None:
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfo()
            self.template_info = temp_model.from_map(m.get('TemplateInfo'))

        return self

class GetStandardTemplateResponseBodyTemplateInfo(DaraModel):
    def __init__(
        self,
        attributes_config: main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfig = None,
        code: str = None,
        code_rule_config: main_models.GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfig = None,
        create_time: str = None,
        creator: main_models.GetStandardTemplateResponseBodyTemplateInfoCreator = None,
        description: str = None,
        id: int = None,
        last_modifier: main_models.GetStandardTemplateResponseBodyTemplateInfoLastModifier = None,
        maintainer_list: List[main_models.GetStandardTemplateResponseBodyTemplateInfoMaintainerList] = None,
        modify_time: str = None,
        name: str = None,
        template_from: str = None,
        unique_id: str = None,
        version: int = None,
    ):
        self.attributes_config = attributes_config
        self.code = code
        self.code_rule_config = code_rule_config
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.id = id
        self.last_modifier = last_modifier
        self.maintainer_list = maintainer_list
        self.modify_time = modify_time
        self.name = name
        self.template_from = template_from
        # uniqueId
        self.unique_id = unique_id
        self.version = version

    def validate(self):
        if self.attributes_config:
            self.attributes_config.validate()
        if self.code_rule_config:
            self.code_rule_config.validate()
        if self.creator:
            self.creator.validate()
        if self.last_modifier:
            self.last_modifier.validate()
        if self.maintainer_list:
            for v1 in self.maintainer_list:
                 if v1:
                    v1.validate()

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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier.to_map()

        result['MaintainerList'] = []
        if self.maintainer_list is not None:
            for k1 in self.maintainer_list:
                result['MaintainerList'].append(k1.to_map() if k1 else None)

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.template_from is not None:
            result['TemplateFrom'] = self.template_from

        if self.unique_id is not None:
            result['UniqueId'] = self.unique_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributesConfig') is not None:
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfig()
            self.attributes_config = temp_model.from_map(m.get('AttributesConfig'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CodeRuleConfig') is not None:
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfig()
            self.code_rule_config = temp_model.from_map(m.get('CodeRuleConfig'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoLastModifier()
            self.last_modifier = temp_model.from_map(m.get('LastModifier'))

        self.maintainer_list = []
        if m.get('MaintainerList') is not None:
            for k1 in m.get('MaintainerList'):
                temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoMaintainerList()
                self.maintainer_list.append(temp_model.from_map(k1))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateFrom') is not None:
            self.template_from = m.get('TemplateFrom')

        if m.get('UniqueId') is not None:
            self.unique_id = m.get('UniqueId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetStandardTemplateResponseBodyTemplateInfoMaintainerList(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardTemplateResponseBodyTemplateInfoLastModifier(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardTemplateResponseBodyTemplateInfoCreator(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfig(DaraModel):
    def __init__(
        self,
        auto_config: main_models.GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfigAutoConfig = None,
        generate_type: str = None,
    ):
        self.auto_config = auto_config
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
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfigAutoConfig()
            self.auto_config = temp_model.from_map(m.get('AutoConfig'))

        if m.get('GenerateType') is not None:
            self.generate_type = m.get('GenerateType')

        return self

class GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfigAutoConfig(DaraModel):
    def __init__(
        self,
        code_rule_list: List[main_models.GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfigAutoConfigCodeRuleList] = None,
        need_strong_validate: bool = None,
    ):
        self.code_rule_list = code_rule_list
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
                temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfigAutoConfigCodeRuleList()
                self.code_rule_list.append(temp_model.from_map(k1))

        if m.get('NeedStrongValidate') is not None:
            self.need_strong_validate = m.get('NeedStrongValidate')

        return self

class GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfigAutoConfigCodeRuleList(DaraModel):
    def __init__(
        self,
        auto_increment_sequence_config: main_models.GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfigAutoConfigCodeRuleListAutoIncrementSequenceConfig = None,
        index: int = None,
        type: str = None,
        value: str = None,
    ):
        self.auto_increment_sequence_config = auto_increment_sequence_config
        self.index = index
        self.type = type
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
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfigAutoConfigCodeRuleListAutoIncrementSequenceConfig()
            self.auto_increment_sequence_config = temp_model.from_map(m.get('AutoIncrementSequenceConfig'))

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetStandardTemplateResponseBodyTemplateInfoCodeRuleConfigAutoConfigCodeRuleListAutoIncrementSequenceConfig(DaraModel):
    def __init__(
        self,
        digit: int = None,
        need_padding_zero: bool = None,
        start_value: int = None,
        step: int = None,
    ):
        self.digit = digit
        self.need_padding_zero = need_padding_zero
        self.start_value = start_value
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

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfig(DaraModel):
    def __init__(
        self,
        attribute_list: List[main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeList] = None,
    ):
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
                temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeList()
                self.attribute_list.append(temp_model.from_map(k1))

        return self

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeList(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        enable_monitor_config: bool = None,
        id: int = None,
        monitor_config: main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListMonitorConfig = None,
        name: str = None,
        ref_attribute: main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListRefAttribute = None,
        required: bool = None,
        type: str = None,
        value_config: main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfig = None,
    ):
        self.code = code
        self.description = description
        self.enable_monitor_config = enable_monitor_config
        self.id = id
        self.monitor_config = monitor_config
        self.name = name
        self.ref_attribute = ref_attribute
        self.required = required
        self.type = type
        self.value_config = value_config

    def validate(self):
        if self.monitor_config:
            self.monitor_config.validate()
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

        if self.enable_monitor_config is not None:
            result['EnableMonitorConfig'] = self.enable_monitor_config

        if self.id is not None:
            result['Id'] = self.id

        if self.monitor_config is not None:
            result['MonitorConfig'] = self.monitor_config.to_map()

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

        if m.get('EnableMonitorConfig') is not None:
            self.enable_monitor_config = m.get('EnableMonitorConfig')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MonitorConfig') is not None:
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListMonitorConfig()
            self.monitor_config = temp_model.from_map(m.get('MonitorConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RefAttribute') is not None:
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListRefAttribute()
            self.ref_attribute = temp_model.from_map(m.get('RefAttribute'))

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueConfig') is not None:
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfig()
            self.value_config = temp_model.from_map(m.get('ValueConfig'))

        return self

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfig(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        default_value: str = None,
        length: int = None,
        type: str = None,
        value_range: main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfigValueRange = None,
    ):
        self.data_type = data_type
        self.default_value = default_value
        self.length = length
        self.type = type
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
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfigValueRange()
            self.value_range = temp_model.from_map(m.get('ValueRange'))

        return self

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfigValueRange(DaraModel):
    def __init__(
        self,
        dataphin_attribute_type: str = None,
        lookup_table_reference: main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfigValueRangeLookupTableReference = None,
        min_max_value_config: main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfigValueRangeMinMaxValueConfig = None,
        value_constraint: str = None,
        value_list: List[str] = None,
    ):
        self.dataphin_attribute_type = dataphin_attribute_type
        self.lookup_table_reference = lookup_table_reference
        self.min_max_value_config = min_max_value_config
        self.value_constraint = value_constraint
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
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfigValueRangeLookupTableReference()
            self.lookup_table_reference = temp_model.from_map(m.get('LookupTableReference'))

        if m.get('MinMaxValueConfig') is not None:
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfigValueRangeMinMaxValueConfig()
            self.min_max_value_config = temp_model.from_map(m.get('MinMaxValueConfig'))

        if m.get('ValueConstraint') is not None:
            self.value_constraint = m.get('ValueConstraint')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfigValueRangeMinMaxValueConfig(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
    ):
        self.include_max_value = include_max_value
        self.include_min_value = include_min_value
        self.max_value = max_value
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

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListValueConfigValueRangeLookupTableReference(DaraModel):
    def __init__(
        self,
        column: str = None,
        lookup_table_id: int = None,
    ):
        self.column = column
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

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListRefAttribute(DaraModel):
    def __init__(
        self,
        attribute_from_info: main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListRefAttributeAttributeFromInfo = None,
        attribute_id: int = None,
    ):
        self.attribute_from_info = attribute_from_info
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
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListRefAttributeAttributeFromInfo()
            self.attribute_from_info = temp_model.from_map(m.get('AttributeFromInfo'))

        if m.get('AttributeId') is not None:
            self.attribute_id = m.get('AttributeId')

        return self

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListRefAttributeAttributeFromInfo(DaraModel):
    def __init__(
        self,
        attribute_from: str = None,
        standard_reference: main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListRefAttributeAttributeFromInfoStandardReference = None,
    ):
        self.attribute_from = attribute_from
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
            temp_model = main_models.GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListRefAttributeAttributeFromInfoStandardReference()
            self.standard_reference = temp_model.from_map(m.get('StandardReference'))

        return self

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListRefAttributeAttributeFromInfoStandardReference(DaraModel):
    def __init__(
        self,
        standard_id: int = None,
        version: int = None,
    ):
        self.standard_id = standard_id
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

class GetStandardTemplateResponseBodyTemplateInfoAttributesConfigAttributeListMonitorConfig(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        is_case_sensitive: bool = None,
        type: str = None,
    ):
        self.column_name = column_name
        self.is_case_sensitive = is_case_sensitive
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.is_case_sensitive is not None:
            result['IsCaseSensitive'] = self.is_case_sensitive

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('IsCaseSensitive') is not None:
            self.is_case_sensitive = m.get('IsCaseSensitive')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

