# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetStandardResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        standard_info: main_models.GetStandardResponseBodyStandardInfo = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # The standard details.
        self.standard_info = standard_info
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.standard_info:
            self.standard_info.validate()

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

        if self.standard_info is not None:
            result['StandardInfo'] = self.standard_info.to_map()

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StandardInfo') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfo()
            self.standard_info = temp_model.from_map(m.get('StandardInfo'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStandardResponseBodyStandardInfo(DaraModel):
    def __init__(
        self,
        attribute_with_value_list: List[main_models.GetStandardResponseBodyStandardInfoAttributeWithValueList] = None,
        code: str = None,
        creator: main_models.GetStandardResponseBodyStandardInfoCreator = None,
        description: str = None,
        effective_time_config: main_models.GetStandardResponseBodyStandardInfoEffectiveTimeConfig = None,
        english_name: str = None,
        id: int = None,
        last_modifier: main_models.GetStandardResponseBodyStandardInfoLastModifier = None,
        lookup_table_relations: List[main_models.GetStandardResponseBodyStandardInfoLookupTableRelations] = None,
        modify_time: str = None,
        name: str = None,
        owner: main_models.GetStandardResponseBodyStandardInfoOwner = None,
        stage: str = None,
        standard_general_monitor_config: main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfig = None,
        standard_relations: List[main_models.GetStandardResponseBodyStandardInfoStandardRelations] = None,
        standard_set: main_models.GetStandardResponseBodyStandardInfoStandardSet = None,
        standard_template: main_models.GetStandardResponseBodyStandardInfoStandardTemplate = None,
        status: str = None,
        type: str = None,
        version: int = None,
    ):
        # The attribute value configurations.
        self.attribute_with_value_list = attribute_with_value_list
        # The standard code.
        self.code = code
        # The creator.
        self.creator = creator
        # The description.
        self.description = description
        # The effective period configuration.
        self.effective_time_config = effective_time_config
        # The English name of the standard.
        self.english_name = english_name
        # The lookup table.
        self.id = id
        # The last modifier.
        self.last_modifier = last_modifier
        # The list of associated lookup tables.
        self.lookup_table_relations = lookup_table_relations
        # The last modification time.
        self.modify_time = modify_time
        # The standard name.
        self.name = name
        # The owner.
        self.owner = owner
        # The stage to which the standard belongs.
        self.stage = stage
        # The standard monitoring configuration.
        self.standard_general_monitor_config = standard_general_monitor_config
        # The list of associated standards.
        self.standard_relations = standard_relations
        # The standard set on which the current standard depends.
        self.standard_set = standard_set
        # The standard template on which the current standard depends.
        self.standard_template = standard_template
        # The status of the standard.
        self.status = status
        # The standard type.
        self.type = type
        # The version number.
        self.version = version

    def validate(self):
        if self.attribute_with_value_list:
            for v1 in self.attribute_with_value_list:
                 if v1:
                    v1.validate()
        if self.creator:
            self.creator.validate()
        if self.effective_time_config:
            self.effective_time_config.validate()
        if self.last_modifier:
            self.last_modifier.validate()
        if self.lookup_table_relations:
            for v1 in self.lookup_table_relations:
                 if v1:
                    v1.validate()
        if self.owner:
            self.owner.validate()
        if self.standard_general_monitor_config:
            self.standard_general_monitor_config.validate()
        if self.standard_relations:
            for v1 in self.standard_relations:
                 if v1:
                    v1.validate()
        if self.standard_set:
            self.standard_set.validate()
        if self.standard_template:
            self.standard_template.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AttributeWithValueList'] = []
        if self.attribute_with_value_list is not None:
            for k1 in self.attribute_with_value_list:
                result['AttributeWithValueList'].append(k1.to_map() if k1 else None)

        if self.code is not None:
            result['Code'] = self.code

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.effective_time_config is not None:
            result['EffectiveTimeConfig'] = self.effective_time_config.to_map()

        if self.english_name is not None:
            result['EnglishName'] = self.english_name

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modifier is not None:
            result['LastModifier'] = self.last_modifier.to_map()

        result['LookupTableRelations'] = []
        if self.lookup_table_relations is not None:
            for k1 in self.lookup_table_relations:
                result['LookupTableRelations'].append(k1.to_map() if k1 else None)

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner.to_map()

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.standard_general_monitor_config is not None:
            result['StandardGeneralMonitorConfig'] = self.standard_general_monitor_config.to_map()

        result['StandardRelations'] = []
        if self.standard_relations is not None:
            for k1 in self.standard_relations:
                result['StandardRelations'].append(k1.to_map() if k1 else None)

        if self.standard_set is not None:
            result['StandardSet'] = self.standard_set.to_map()

        if self.standard_template is not None:
            result['StandardTemplate'] = self.standard_template.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attribute_with_value_list = []
        if m.get('AttributeWithValueList') is not None:
            for k1 in m.get('AttributeWithValueList'):
                temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueList()
                self.attribute_with_value_list.append(temp_model.from_map(k1))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Creator') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EffectiveTimeConfig') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoEffectiveTimeConfig()
            self.effective_time_config = temp_model.from_map(m.get('EffectiveTimeConfig'))

        if m.get('EnglishName') is not None:
            self.english_name = m.get('EnglishName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifier') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoLastModifier()
            self.last_modifier = temp_model.from_map(m.get('LastModifier'))

        self.lookup_table_relations = []
        if m.get('LookupTableRelations') is not None:
            for k1 in m.get('LookupTableRelations'):
                temp_model = main_models.GetStandardResponseBodyStandardInfoLookupTableRelations()
                self.lookup_table_relations.append(temp_model.from_map(k1))

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoOwner()
            self.owner = temp_model.from_map(m.get('Owner'))

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('StandardGeneralMonitorConfig') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfig()
            self.standard_general_monitor_config = temp_model.from_map(m.get('StandardGeneralMonitorConfig'))

        self.standard_relations = []
        if m.get('StandardRelations') is not None:
            for k1 in m.get('StandardRelations'):
                temp_model = main_models.GetStandardResponseBodyStandardInfoStandardRelations()
                self.standard_relations.append(temp_model.from_map(k1))

        if m.get('StandardSet') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoStandardSet()
            self.standard_set = temp_model.from_map(m.get('StandardSet'))

        if m.get('StandardTemplate') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoStandardTemplate()
            self.standard_template = temp_model.from_map(m.get('StandardTemplate'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetStandardResponseBodyStandardInfoStandardTemplate(DaraModel):
    def __init__(
        self,
        code: str = None,
        id: int = None,
        name: str = None,
        template_from: str = None,
        version: int = None,
    ):
        # The standard template code.
        self.code = code
        # The standard template ID.
        self.id = id
        # The standard template name.
        self.name = name
        # The source of the standard template. Valid values:
        # - CUSTOM: Custom standard template.
        # - SYSTEM: System built-in standard template.
        self.template_from = template_from
        # The version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.template_from is not None:
            result['TemplateFrom'] = self.template_from

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateFrom') is not None:
            self.template_from = m.get('TemplateFrom')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetStandardResponseBodyStandardInfoStandardSet(DaraModel):
    def __init__(
        self,
        code: str = None,
        directory: str = None,
        id: int = None,
        name: str = None,
    ):
        # The standard set code.
        self.code = code
        # The folder to which the standard set belongs.
        self.directory = directory
        # The standard set ID.
        self.id = id
        # The standard set name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetStandardResponseBodyStandardInfoStandardRelations(DaraModel):
    def __init__(
        self,
        relation_type: str = None,
        standard_id: int = None,
        standard_stage: str = None,
        standard_status: str = None,
        version: int = None,
    ):
        # The association type. Valid values:
        # - RELATIVE.
        self.relation_type = relation_type
        # The standard ID.
        self.standard_id = standard_id
        # The stage of the standard.
        self.standard_stage = standard_stage
        # The standard status.
        self.standard_status = standard_status
        # The standard version number.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.relation_type is not None:
            result['RelationType'] = self.relation_type

        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        if self.standard_stage is not None:
            result['StandardStage'] = self.standard_stage

        if self.standard_status is not None:
            result['StandardStatus'] = self.standard_status

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelationType') is not None:
            self.relation_type = m.get('RelationType')

        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        if m.get('StandardStage') is not None:
            self.standard_stage = m.get('StandardStage')

        if m.get('StandardStatus') is not None:
            self.standard_status = m.get('StandardStatus')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfig(DaraModel):
    def __init__(
        self,
        standard_monitor_config_list: List[main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigList] = None,
    ):
        # The list of standard monitoring configurations.
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
                temp_model = main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigList()
                self.standard_monitor_config_list.append(temp_model.from_map(k1))

        return self

class GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigList(DaraModel):
    def __init__(
        self,
        attribute_id: int = None,
        attribute_monitor_config: main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListAttributeMonitorConfig = None,
        attribute_name: str = None,
        description: str = None,
        id: int = None,
        monitor_from: str = None,
        quality_rule_template: main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListQualityRuleTemplate = None,
        rule_config_list: List[main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListRuleConfigList] = None,
        rule_name: str = None,
        rule_sub_type: str = None,
        rule_validate_config_list: List[main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListRuleValidateConfigList] = None,
        type: str = None,
    ):
        # The associated attribute ID.
        self.attribute_id = attribute_id
        # The monitoring configuration of the associated attribute.
        self.attribute_monitor_config = attribute_monitor_config
        # The attribute name.
        self.attribute_name = attribute_name
        # The rule description.
        self.description = description
        # The monitoring configuration ID. If empty, a new monitoring configuration is created. If an existing monitoring configuration ID is specified, the corresponding monitoring configuration is updated.
        self.id = id
        # The method by which the monitoring configuration is added. Valid values:
        # - BY_USER: manually added.
        # - BY_SYSTEM_ATTRIBUTE: preset by system attribute.
        self.monitor_from = monitor_from
        # The rule template. This parameter is required when the monitoring type is QUALITY.
        self.quality_rule_template = quality_rule_template
        # The rule configurations. This parameter is required when the monitoring type is QUALITY.
        self.rule_config_list = rule_config_list
        # The rule name.
        self.rule_name = rule_name
        # The rule subtype. Valid values:
        # - BY_ATTRIBUTE: configured based on attributes.
        # - CUSTOMIZED: custom configuration.
        # 
        # This parameter is required when the monitoring type is QUALITY.
        self.rule_sub_type = rule_sub_type
        # The rule validation configurations. This parameter is required when the monitoring type is QUALITY.
        self.rule_validate_config_list = rule_validate_config_list
        # The monitoring type. Valid values:
        # - METADATA: metadata monitoring.
        # - QUALITY: data quality monitoring.
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
            temp_model = main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListAttributeMonitorConfig()
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
            temp_model = main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListQualityRuleTemplate()
            self.quality_rule_template = temp_model.from_map(m.get('QualityRuleTemplate'))

        self.rule_config_list = []
        if m.get('RuleConfigList') is not None:
            for k1 in m.get('RuleConfigList'):
                temp_model = main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListRuleConfigList()
                self.rule_config_list.append(temp_model.from_map(k1))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleSubType') is not None:
            self.rule_sub_type = m.get('RuleSubType')

        self.rule_validate_config_list = []
        if m.get('RuleValidateConfigList') is not None:
            for k1 in m.get('RuleValidateConfigList'):
                temp_model = main_models.GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListRuleValidateConfigList()
                self.rule_validate_config_list.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListRuleValidateConfigList(DaraModel):
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
        self.id = id
        # The metric. This parameter is required when the validation type is EXPRESSION.
        self.metric = metric
        # The metric name. This parameter is required when the validation type is EXPRESSION.
        self.metric_name = metric_name
        # The operator. If the validation type is EXPRESSION, valid values:
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
        self.operator = operator
        # The parent validation configuration ID. The parent rule validation type can only be RELATION.
        self.parent_id = parent_id
        # The rule validation type. Valid values:
        # - RELATION: relation.
        # - EXPRESSION: expression.
        self.type = type
        # The comparison value.
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

class GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListRuleConfigList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The configuration item.
        self.key = key
        # The configuration item value.
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

class GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListQualityRuleTemplate(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
        type: str = None,
    ):
        # The template ID.
        self.id = id
        # The template name.
        self.name = name
        # The template source. Valid values:
        # - FROM_SYSTEM: system template.
        # - CUSTOMIZED: custom template.
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

class GetStandardResponseBodyStandardInfoStandardGeneralMonitorConfigStandardMonitorConfigListAttributeMonitorConfig(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        is_case_sensitive: bool = None,
        type: str = None,
    ):
        # The field to check.
        self.column_name = column_name
        # Indicates whether the check is case-sensitive.
        self.is_case_sensitive = is_case_sensitive
        # The monitoring method. Valid values:
        # - METADATA: metadata monitoring.
        # - QUALITY: data quality monitoring.
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

class GetStandardResponseBodyStandardInfoOwner(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The user ID.
        self.id = id
        # The username.
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

class GetStandardResponseBodyStandardInfoLookupTableRelations(DaraModel):
    def __init__(
        self,
        attribute_code: str = None,
        attribute_id: int = None,
        attribute_name: str = None,
        lookup_table_code: str = None,
        lookup_table_id: int = None,
    ):
        # The attribute name.
        self.attribute_code = attribute_code
        # The attribute ID.
        self.attribute_id = attribute_id
        # The attribute name.
        self.attribute_name = attribute_name
        # The lookup table code.
        self.lookup_table_code = lookup_table_code
        # The lookup table ID.
        self.lookup_table_id = lookup_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_code is not None:
            result['AttributeCode'] = self.attribute_code

        if self.attribute_id is not None:
            result['AttributeId'] = self.attribute_id

        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

        if self.lookup_table_code is not None:
            result['LookupTableCode'] = self.lookup_table_code

        if self.lookup_table_id is not None:
            result['LookupTableId'] = self.lookup_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeCode') is not None:
            self.attribute_code = m.get('AttributeCode')

        if m.get('AttributeId') is not None:
            self.attribute_id = m.get('AttributeId')

        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

        if m.get('LookupTableCode') is not None:
            self.lookup_table_code = m.get('LookupTableCode')

        if m.get('LookupTableId') is not None:
            self.lookup_table_id = m.get('LookupTableId')

        return self

class GetStandardResponseBodyStandardInfoLastModifier(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The user ID.
        self.id = id
        # The username.
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

class GetStandardResponseBodyStandardInfoEffectiveTimeConfig(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The end time of the effective period.
        self.end_time = end_time
        # The start time of the effective period.
        self.start_time = start_time
        # The effective period type. Valid values:
        # - FOREVER: permanent.
        # - TIME_PERIOD: time period.
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

class GetStandardResponseBodyStandardInfoCreator(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # The user ID.
        self.id = id
        # The username.
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

class GetStandardResponseBodyStandardInfoAttributeWithValueList(DaraModel):
    def __init__(
        self,
        attribute: main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttribute = None,
        value: str = None,
    ):
        # The attribute details.
        self.attribute = attribute
        # The attribute value.
        self.value = value

    def validate(self):
        if self.attribute:
            self.attribute.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['Attribute'] = self.attribute.to_map()

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attribute') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttribute()
            self.attribute = temp_model.from_map(m.get('Attribute'))

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class GetStandardResponseBodyStandardInfoAttributeWithValueListAttribute(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        enable_monitor_config: bool = None,
        id: int = None,
        monitor_config: main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeMonitorConfig = None,
        name: str = None,
        ref_attribute: main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeRefAttribute = None,
        required: bool = None,
        type: str = None,
        value_config: main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfig = None,
    ):
        # The attribute code.
        self.code = code
        # The description.
        self.description = description
        # Indicates whether the monitoring configuration is enabled.
        self.enable_monitor_config = enable_monitor_config
        # The attribute ID.
        self.id = id
        # The monitoring configuration.
        self.monitor_config = monitor_config
        # The attribute name.
        self.name = name
        # The referenced attribute information.
        self.ref_attribute = ref_attribute
        # Indicates whether the attribute is required.
        self.required = required
        # The attribute type. Valid values:
        # - BIZ_ATTRIBUTE: business attribute.
        # - TECH_ATTRIBUTE: technical attribute.
        # - MANAGEMENT_ATTRIBUTE: management attribute.
        # - QUALITY_ATTRIBUTE: quality attribute.
        # - MASTER_DATA_ATTRIBUTE: master data attribute.
        # - LIFECYCLE_ATTRIBUTE: lifecycle attribute.
        # - SECURITY_ATTRIBUTE: security attribute.
        self.type = type
        # The value configuration.
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
            temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeMonitorConfig()
            self.monitor_config = temp_model.from_map(m.get('MonitorConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RefAttribute') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeRefAttribute()
            self.ref_attribute = temp_model.from_map(m.get('RefAttribute'))

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('ValueConfig') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfig()
            self.value_config = temp_model.from_map(m.get('ValueConfig'))

        return self

class GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfig(DaraModel):
    def __init__(
        self,
        data_type: str = None,
        default_value: str = None,
        length: int = None,
        type: str = None,
        value_range: main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfigValueRange = None,
    ):
        # The data type of the attribute value. Valid values:
        # - STRING: string.
        # - BIGINT: numeric type.
        # - DOUBLE: floating-point type.
        # - DATE: date, accurate to the day.
        # - DATETIME: date, accurate to milliseconds.
        # - BOOLEAN: Boolean.
        self.data_type = data_type
        # The default value.
        self.default_value = default_value
        # The length of the attribute value. If empty or -1, the length is not limited. Typically, only string types have a length limit for attribute values.
        self.length = length
        # The attribute value type. Valid values:
        # - CUSTOMIZED: custom input.
        # - SINGLE_ENUM: single enumeration value.
        # - MULTIPLE_ENUMS: multiple enumeration values.
        # - RANGE: range value.
        self.type = type
        # The value range.
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
            temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfigValueRange()
            self.value_range = temp_model.from_map(m.get('ValueRange'))

        return self

class GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfigValueRange(DaraModel):
    def __init__(
        self,
        dataphin_attribute_type: str = None,
        lookup_table_reference: main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfigValueRangeLookupTableReference = None,
        min_max_value_config: main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfigValueRangeMinMaxValueConfig = None,
        value_constraint: str = None,
        value_list: List[str] = None,
    ):
        # The value range. This parameter takes effect when the value source is set to DATAPHIN_ATTRIBUTE. Valid values:
        # - BIZ_UNIT: business unit.
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
            temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfigValueRangeLookupTableReference()
            self.lookup_table_reference = temp_model.from_map(m.get('LookupTableReference'))

        if m.get('MinMaxValueConfig') is not None:
            temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfigValueRangeMinMaxValueConfig()
            self.min_max_value_config = temp_model.from_map(m.get('MinMaxValueConfig'))

        if m.get('ValueConstraint') is not None:
            self.value_constraint = m.get('ValueConstraint')

        if m.get('ValueList') is not None:
            self.value_list = m.get('ValueList')

        return self

class GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfigValueRangeMinMaxValueConfig(DaraModel):
    def __init__(
        self,
        include_max_value: bool = None,
        include_min_value: bool = None,
        max_value: str = None,
        min_value: str = None,
    ):
        # Indicates whether the maximum value is included.
        self.include_max_value = include_max_value
        # Indicates whether the minimum value is included.
        self.include_min_value = include_min_value
        # The maximum value.
        self.max_value = max_value
        # The minimum value.
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

class GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeValueConfigValueRangeLookupTableReference(DaraModel):
    def __init__(
        self,
        column: str = None,
        lookup_table_id: int = None,
    ):
        # The referenced lookup table field.
        self.column = column
        # The lookup table ID.
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

class GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeRefAttribute(DaraModel):
    def __init__(
        self,
        attribute_from_info: main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeRefAttributeAttributeFromInfo = None,
        attribute_id: int = None,
    ):
        # The attribute source.
        self.attribute_from_info = attribute_from_info
        # The attribute ID.
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
            temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeRefAttributeAttributeFromInfo()
            self.attribute_from_info = temp_model.from_map(m.get('AttributeFromInfo'))

        if m.get('AttributeId') is not None:
            self.attribute_id = m.get('AttributeId')

        return self

class GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeRefAttributeAttributeFromInfo(DaraModel):
    def __init__(
        self,
        attribute_from: str = None,
        standard_reference: main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeRefAttributeAttributeFromInfoStandardReference = None,
    ):
        # The attribute source. Valid values:
        # - SYSTEM: system attribute.
        # - CUSTOM: custom attribute.
        # - STANDARD: standard.
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
            temp_model = main_models.GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeRefAttributeAttributeFromInfoStandardReference()
            self.standard_reference = temp_model.from_map(m.get('StandardReference'))

        return self

class GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeRefAttributeAttributeFromInfoStandardReference(DaraModel):
    def __init__(
        self,
        standard_id: int = None,
        version: int = None,
    ):
        # The standard ID.
        self.standard_id = standard_id
        # The version number.
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

class GetStandardResponseBodyStandardInfoAttributeWithValueListAttributeMonitorConfig(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        is_case_sensitive: bool = None,
        type: str = None,
    ):
        # The field to check.
        self.column_name = column_name
        # Indicates whether the check is case-sensitive.
        self.is_case_sensitive = is_case_sensitive
        # The monitoring method. Valid values:
        # - METADATA: metadata monitoring.
        # - QUALITY: data quality monitoring.
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

