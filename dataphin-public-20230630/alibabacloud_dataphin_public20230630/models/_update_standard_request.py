# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateStandardRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        update_command: main_models.UpdateStandardRequestUpdateCommand = None,
    ):
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
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
            temp_model = main_models.UpdateStandardRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateStandardRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        description: str = None,
        effective_time_config: main_models.UpdateStandardRequestUpdateCommandEffectiveTimeConfig = None,
        need_generate_standard_code: bool = None,
        owner: str = None,
        standard_general_monitor_config: main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfig = None,
        standard_id: int = None,
        standard_set_reference: main_models.UpdateStandardRequestUpdateCommandStandardSetReference = None,
        standard_status: str = None,
        standard_template_reference: main_models.UpdateStandardRequestUpdateCommandStandardTemplateReference = None,
        version: int = None,
    ):
        self.description = description
        self.effective_time_config = effective_time_config
        self.need_generate_standard_code = need_generate_standard_code
        self.owner = owner
        self.standard_general_monitor_config = standard_general_monitor_config
        # This parameter is required.
        self.standard_id = standard_id
        # This parameter is required.
        self.standard_set_reference = standard_set_reference
        # This parameter is required.
        self.standard_status = standard_status
        # This parameter is required.
        self.standard_template_reference = standard_template_reference
        self.version = version

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

        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        if self.standard_set_reference is not None:
            result['StandardSetReference'] = self.standard_set_reference.to_map()

        if self.standard_status is not None:
            result['StandardStatus'] = self.standard_status

        if self.standard_template_reference is not None:
            result['StandardTemplateReference'] = self.standard_template_reference.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectiveTimeConfig') is not None:
            temp_model = main_models.UpdateStandardRequestUpdateCommandEffectiveTimeConfig()
            self.effective_time_config = temp_model.from_map(m.get('EffectiveTimeConfig'))

        if m.get('NeedGenerateStandardCode') is not None:
            self.need_generate_standard_code = m.get('NeedGenerateStandardCode')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('StandardGeneralMonitorConfig') is not None:
            temp_model = main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfig()
            self.standard_general_monitor_config = temp_model.from_map(m.get('StandardGeneralMonitorConfig'))

        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        if m.get('StandardSetReference') is not None:
            temp_model = main_models.UpdateStandardRequestUpdateCommandStandardSetReference()
            self.standard_set_reference = temp_model.from_map(m.get('StandardSetReference'))

        if m.get('StandardStatus') is not None:
            self.standard_status = m.get('StandardStatus')

        if m.get('StandardTemplateReference') is not None:
            temp_model = main_models.UpdateStandardRequestUpdateCommandStandardTemplateReference()
            self.standard_template_reference = temp_model.from_map(m.get('StandardTemplateReference'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class UpdateStandardRequestUpdateCommandStandardTemplateReference(DaraModel):
    def __init__(
        self,
        attribute_value_list: List[main_models.UpdateStandardRequestUpdateCommandStandardTemplateReferenceAttributeValueList] = None,
        id: int = None,
        version: int = None,
    ):
        self.attribute_value_list = attribute_value_list
        # This parameter is required.
        self.id = id
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
                temp_model = main_models.UpdateStandardRequestUpdateCommandStandardTemplateReferenceAttributeValueList()
                self.attribute_value_list.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class UpdateStandardRequestUpdateCommandStandardTemplateReferenceAttributeValueList(DaraModel):
    def __init__(
        self,
        attribute_id: int = None,
        value: str = None,
    ):
        self.attribute_id = attribute_id
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

class UpdateStandardRequestUpdateCommandStandardSetReference(DaraModel):
    def __init__(
        self,
        id: int = None,
    ):
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

class UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfig(DaraModel):
    def __init__(
        self,
        standard_monitor_config_list: List[main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigList] = None,
    ):
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
                temp_model = main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigList()
                self.standard_monitor_config_list.append(temp_model.from_map(k1))

        return self

class UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigList(DaraModel):
    def __init__(
        self,
        attribute_id: int = None,
        attribute_monitor_config: main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListAttributeMonitorConfig = None,
        attribute_name: str = None,
        description: str = None,
        id: int = None,
        monitor_from: str = None,
        quality_rule_template: main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListQualityRuleTemplate = None,
        rule_config_list: List[main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleConfigList] = None,
        rule_name: str = None,
        rule_sub_type: str = None,
        rule_validate_config_list: List[main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleValidateConfigList] = None,
        type: str = None,
    ):
        self.attribute_id = attribute_id
        self.attribute_monitor_config = attribute_monitor_config
        self.attribute_name = attribute_name
        self.description = description
        self.id = id
        # This parameter is required.
        self.monitor_from = monitor_from
        self.quality_rule_template = quality_rule_template
        self.rule_config_list = rule_config_list
        # This parameter is required.
        self.rule_name = rule_name
        self.rule_sub_type = rule_sub_type
        self.rule_validate_config_list = rule_validate_config_list
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
            temp_model = main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListAttributeMonitorConfig()
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
            temp_model = main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListQualityRuleTemplate()
            self.quality_rule_template = temp_model.from_map(m.get('QualityRuleTemplate'))

        self.rule_config_list = []
        if m.get('RuleConfigList') is not None:
            for k1 in m.get('RuleConfigList'):
                temp_model = main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleConfigList()
                self.rule_config_list.append(temp_model.from_map(k1))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleSubType') is not None:
            self.rule_sub_type = m.get('RuleSubType')

        self.rule_validate_config_list = []
        if m.get('RuleValidateConfigList') is not None:
            for k1 in m.get('RuleValidateConfigList'):
                temp_model = main_models.UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleValidateConfigList()
                self.rule_validate_config_list.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleValidateConfigList(DaraModel):
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
        # This parameter is required.
        self.id = id
        self.metric = metric
        self.metric_name = metric_name
        # This parameter is required.
        self.operator = operator
        self.parent_id = parent_id
        # This parameter is required.
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

class UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListRuleConfigList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
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

class UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListQualityRuleTemplate(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.name = name
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

class UpdateStandardRequestUpdateCommandStandardGeneralMonitorConfigStandardMonitorConfigListAttributeMonitorConfig(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        is_case_sensitive: bool = None,
        type: str = None,
    ):
        self.column_name = column_name
        # This parameter is required.
        self.is_case_sensitive = is_case_sensitive
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

class UpdateStandardRequestUpdateCommandEffectiveTimeConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        type: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
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

