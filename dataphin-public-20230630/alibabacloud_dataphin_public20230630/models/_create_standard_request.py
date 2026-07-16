# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateStandardRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateStandardRequestCreateCommand = None,
        op_tenant_id: int = None,
    ):
        # The create command.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateStandardRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateStandardRequestCreateCommand(DaraModel):
    def __init__(
        self,
        description: str = None,
        effective_time_config: main_models.CreateStandardRequestCreateCommandEffectiveTimeConfig = None,
        need_generate_standard_code: bool = None,
        owner: str = None,
        standard_general_monitor_config: main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfig = None,
        standard_set_reference: main_models.CreateStandardRequestCreateCommandStandardSetReference = None,
        standard_template_reference: main_models.CreateStandardRequestCreateCommandStandardTemplateReference = None,
    ):
        # The description.
        self.description = description
        # The effective period configuration.
        self.effective_time_config = effective_time_config
        # Specifies whether to generate a standard code based on rules. If this parameter is set to true, the standard code specified in the attribute values is ignored and a new standard code is generated.
        self.need_generate_standard_code = need_generate_standard_code
        # The owner. If this parameter is not specified, the current user is used.
        self.owner = owner
        # The standard monitoring configuration.
        self.standard_general_monitor_config = standard_general_monitor_config
        # The reference to the standard set.
        # 
        # This parameter is required.
        self.standard_set_reference = standard_set_reference
        # The standard template to which the standard belongs.
        # 
        # This parameter is required.
        self.standard_template_reference = standard_template_reference

    def validate(self):
        if self.effective_time_config:
            self.effective_time_config.validate()
        if self.standard_general_monitor_config:
            self.standard_general_monitor_config.validate()
        if self.standard_set_reference:
            self.standard_set_reference.validate()
        if self.standard_template_reference:
            self.standard_template_reference.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.effective_time_config is not None:
            result['EffectiveTimeConfig'] = self.effective_time_config.to_map()

        if self.need_generate_standard_code is not None:
            result['NeedGenerateStandardCode'] = self.need_generate_standard_code

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.standard_general_monitor_config is not None:
            result['StandardGeneralMonitorConfig'] = self.standard_general_monitor_config.to_map()

        if self.standard_set_reference is not None:
            result['StandardSetReference'] = self.standard_set_reference.to_map()

        if self.standard_template_reference is not None:
            result['StandardTemplateReference'] = self.standard_template_reference.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectiveTimeConfig') is not None:
            temp_model = main_models.CreateStandardRequestCreateCommandEffectiveTimeConfig()
            self.effective_time_config = temp_model.from_map(m.get('EffectiveTimeConfig'))

        if m.get('NeedGenerateStandardCode') is not None:
            self.need_generate_standard_code = m.get('NeedGenerateStandardCode')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('StandardGeneralMonitorConfig') is not None:
            temp_model = main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfig()
            self.standard_general_monitor_config = temp_model.from_map(m.get('StandardGeneralMonitorConfig'))

        if m.get('StandardSetReference') is not None:
            temp_model = main_models.CreateStandardRequestCreateCommandStandardSetReference()
            self.standard_set_reference = temp_model.from_map(m.get('StandardSetReference'))

        if m.get('StandardTemplateReference') is not None:
            temp_model = main_models.CreateStandardRequestCreateCommandStandardTemplateReference()
            self.standard_template_reference = temp_model.from_map(m.get('StandardTemplateReference'))

        return self

class CreateStandardRequestCreateCommandStandardTemplateReference(DaraModel):
    def __init__(
        self,
        attribute_value_list: List[main_models.CreateStandardRequestCreateCommandStandardTemplateReferenceAttributeValueList] = None,
        id: int = None,
        version: int = None,
    ):
        # The attribute values corresponding to the attributes in the referenced template. If this parameter is left empty, default values are used.
        self.attribute_value_list = attribute_value_list
        # The standard template ID.
        # 
        # This parameter is required.
        self.id = id
        # The standard template version number. The latest version is used by default.
        self.version = version

    def validate(self):
        if self.attribute_value_list:
            for v1 in self.attribute_value_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeValueList'] = []
        if self.attribute_value_list is not None:
            for k1 in self.attribute_value_list:
                result['AttributeValueList'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_value_list = []
        if m.get('AttributeValueList') is not None:
            for k1 in m.get('AttributeValueList'):
                temp_model = main_models.CreateStandardRequestCreateCommandStandardTemplateReferenceAttributeValueList()
                self.attribute_value_list.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class CreateStandardRequestCreateCommandStandardTemplateReferenceAttributeValueList(DaraModel):
    def __init__(
        self,
        attribute_id: int = None,
        value: str = None,
    ):
        # The attribute ID.
        self.attribute_id = attribute_id
        # The attribute value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_id is not None:
            result['AttributeId'] = self.attribute_id

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeId') is not None:
            self.attribute_id = m.get('AttributeId')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateStandardRequestCreateCommandStandardSetReference(DaraModel):
    def __init__(
        self,
        id: int = None,
    ):
        # The standard set ID.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

class CreateStandardRequestCreateCommandStandardGeneralMonitorConfig(DaraModel):
    def __init__(
        self,
        standard_monitor_config_list: List[main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigList] = None,
    ):
        # The list of standard monitoring configurations.
        # 
        # This parameter is required.
        self.standard_monitor_config_list = standard_monitor_config_list

    def validate(self):
        if self.standard_monitor_config_list:
            for v1 in self.standard_monitor_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['StandardMonitorConfigList'] = []
        if self.standard_monitor_config_list is not None:
            for k1 in self.standard_monitor_config_list:
                result['StandardMonitorConfigList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.standard_monitor_config_list = []
        if m.get('StandardMonitorConfigList') is not None:
            for k1 in m.get('StandardMonitorConfigList'):
                temp_model = main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigList()
                self.standard_monitor_config_list.append(temp_model.from_map(k1))

        return self

class CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigList(DaraModel):
    def __init__(
        self,
        attribute_id: int = None,
        attribute_monitor_config: main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListAttributeMonitorConfig = None,
        attribute_name: str = None,
        description: str = None,
        id: int = None,
        monitor_from: str = None,
        quality_rule_template: main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListQualityRuleTemplate = None,
        rule_config_list: List[main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleConfigList] = None,
        rule_name: str = None,
        rule_sub_type: str = None,
        rule_validate_config_list: List[main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleValidateConfigList] = None,
        type: str = None,
    ):
        # The associated attribute ID.
        self.attribute_id = attribute_id
        # The monitoring configuration for the associated attribute.
        self.attribute_monitor_config = attribute_monitor_config
        # The attribute name.
        self.attribute_name = attribute_name
        # The rule description.
        self.description = description
        # The monitoring configuration ID. If this parameter is left empty, a new monitoring configuration is created. If an existing monitoring configuration ID is specified, the corresponding monitoring configuration is updated.
        self.id = id
        # The method used to add the monitoring configuration. Valid values:
        # - BY_USER: manually added.
        # - BY_SYSTEM_ATTRIBUTE: preset by system attribute.
        # 
        # This parameter is required.
        self.monitor_from = monitor_from
        # The rule template. This parameter is required when the monitoring type is QUALITY.
        self.quality_rule_template = quality_rule_template
        # The rule configurations. This parameter is required when the monitoring type is QUALITY.
        self.rule_config_list = rule_config_list
        # The rule name.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The rule subtype. This parameter is required when the monitoring type is QUALITY. Valid values:
        # - BY_ATTRIBUTE: configured based on attributes.
        # - CUSTOMIZED: custom configuration.
        self.rule_sub_type = rule_sub_type
        # The rule validation configurations. This parameter is required when the monitoring type is QUALITY.
        self.rule_validate_config_list = rule_validate_config_list
        # The monitoring type. Valid values:
        # - METADATA: metadata monitoring.
        # - QUALITY: data quality monitoring.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.attribute_monitor_config:
            self.attribute_monitor_config.validate()
        if self.quality_rule_template:
            self.quality_rule_template.validate()
        if self.rule_config_list:
            for v1 in self.rule_config_list:
                 if v1:
                    v1.validate()
        if self.rule_validate_config_list:
            for v1 in self.rule_validate_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_id is not None:
            result['AttributeId'] = self.attribute_id

        if self.attribute_monitor_config is not None:
            result['AttributeMonitorConfig'] = self.attribute_monitor_config.to_map()

        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.monitor_from is not None:
            result['MonitorFrom'] = self.monitor_from

        if self.quality_rule_template is not None:
            result['QualityRuleTemplate'] = self.quality_rule_template.to_map()

        result['RuleConfigList'] = []
        if self.rule_config_list is not None:
            for k1 in self.rule_config_list:
                result['RuleConfigList'].append(k1.to_map() if k1 else None)

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_sub_type is not None:
            result['RuleSubType'] = self.rule_sub_type

        result['RuleValidateConfigList'] = []
        if self.rule_validate_config_list is not None:
            for k1 in self.rule_validate_config_list:
                result['RuleValidateConfigList'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeId') is not None:
            self.attribute_id = m.get('AttributeId')

        if m.get('AttributeMonitorConfig') is not None:
            temp_model = main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListAttributeMonitorConfig()
            self.attribute_monitor_config = temp_model.from_map(m.get('AttributeMonitorConfig'))

        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MonitorFrom') is not None:
            self.monitor_from = m.get('MonitorFrom')

        if m.get('QualityRuleTemplate') is not None:
            temp_model = main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListQualityRuleTemplate()
            self.quality_rule_template = temp_model.from_map(m.get('QualityRuleTemplate'))

        self.rule_config_list = []
        if m.get('RuleConfigList') is not None:
            for k1 in m.get('RuleConfigList'):
                temp_model = main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleConfigList()
                self.rule_config_list.append(temp_model.from_map(k1))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleSubType') is not None:
            self.rule_sub_type = m.get('RuleSubType')

        self.rule_validate_config_list = []
        if m.get('RuleValidateConfigList') is not None:
            for k1 in m.get('RuleValidateConfigList'):
                temp_model = main_models.CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleValidateConfigList()
                self.rule_validate_config_list.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleValidateConfigList(DaraModel):
    def __init__(
        self,
        id: str = None,
        metric: str = None,
        metric_name: str = None,
        operator: str = None,
        parent_id: str = None,
        type: str = None,
        value: str = None,
    ):
        # The validation configuration ID. This ID is randomly generated by the business and must be unique.
        # 
        # This parameter is required.
        self.id = id
        # The metric. This parameter is required when the validation type is EXPRESSION.
        self.metric = metric
        # The metric name. This parameter is required when the validation type is EXPRESSION.
        self.metric_name = metric_name
        # If the validation type is EXPRESSION, valid values:
        # - EQUAL: equal to.
        # - NOT_EQUAL: not equal to.
        # - LARGER: greater than.
        # - LARGE_OR_EQUAL: greater than or equal to.
        # - SMALLER: less than.
        # - SMALLER_OR_EQUAL: less than or equal to.
        # 
        # If the validation type is RELATION, valid values:
        # - AND: and.
        # - OR: or.
        # 
        # This parameter is required.
        self.operator = operator
        # The parent validation configuration ID. The parent rule validation type can only be RELATION.
        self.parent_id = parent_id
        # The rule validation type. Valid values:
        # - RELATION: relation.
        # - EXPRESSION: expression.
        # 
        # This parameter is required.
        self.type = type
        # The value to compare.
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

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleConfigList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The configuration item.
        # 
        # This parameter is required.
        self.key = key
        # The configuration item value.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListQualityRuleTemplate(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        # The template ID.
        # 
        # This parameter is required.
        self.id = id
        # The template name.
        # 
        # This parameter is required.
        self.name = name
        # The template source. Valid values:
        # - FROM_SYSTEM: system template.
        # - CUSTOMIZED: custom template.
        # 
        # This parameter is required.
        self.type = type

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

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateStandardRequestCreateCommandStandardGeneralMonitorConfigStandardMonitorConfigListAttributeMonitorConfig(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        is_case_sensitive: bool = None,
        type: str = None,
    ):
        # The field to check.
        self.column_name = column_name
        # Specifies whether the check is case-sensitive.
        # 
        # This parameter is required.
        self.is_case_sensitive = is_case_sensitive
        # The monitoring method. Valid values:
        # - METADATA: metadata monitoring.
        # - QUALITY: data quality monitoring.
        # 
        # This parameter is required.
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

class CreateStandardRequestCreateCommandEffectiveTimeConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The end of the effective period.
        self.end_time = end_time
        # The start of the effective period.
        self.start_time = start_time
        # The effective period type. Valid values:
        # - FOREVER: permanent.
        # - TIME_PERIOD: time period.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

