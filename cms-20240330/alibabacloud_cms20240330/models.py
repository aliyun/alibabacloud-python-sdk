# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class FilterSettingConditions(TeaModel):
    def __init__(
        self,
        field: str = None,
        op: str = None,
        value: str = None,
    ):
        self.field = field
        self.op = op
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['field'] = self.field
        if self.op is not None:
            result['op'] = self.op
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('op') is not None:
            self.op = m.get('op')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class FilterSetting(TeaModel):
    def __init__(
        self,
        conditions: List[FilterSettingConditions] = None,
        expression: str = None,
        relation: str = None,
    ):
        self.conditions = conditions
        self.expression = expression
        self.relation = relation

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        if self.expression is not None:
            result['expression'] = self.expression
        if self.relation is not None:
            result['relation'] = self.relation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = FilterSettingConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('expression') is not None:
            self.expression = m.get('expression')
        if m.get('relation') is not None:
            self.relation = m.get('relation')
        return self


class TransformAction(TeaModel):
    def __init__(
        self,
        filter_setting: FilterSetting = None,
        label_key: str = None,
        mapping: Dict[str, str] = None,
        reg_exp: str = None,
        source: str = None,
        target: str = None,
        type: str = None,
        value: str = None,
        variable: str = None,
    ):
        self.filter_setting = filter_setting
        self.label_key = label_key
        self.mapping = mapping
        self.reg_exp = reg_exp
        self.source = source
        self.target = target
        self.type = type
        self.value = value
        self.variable = variable

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.label_key is not None:
            result['labelKey'] = self.label_key
        if self.mapping is not None:
            result['mapping'] = self.mapping
        if self.reg_exp is not None:
            result['regExp'] = self.reg_exp
        if self.source is not None:
            result['source'] = self.source
        if self.target is not None:
            result['target'] = self.target
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.variable is not None:
            result['variable'] = self.variable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('labelKey') is not None:
            self.label_key = m.get('labelKey')
        if m.get('mapping') is not None:
            self.mapping = m.get('mapping')
        if m.get('regExp') is not None:
            self.reg_exp = m.get('regExp')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('variable') is not None:
            self.variable = m.get('variable')
        return self


class AlertEventIntegrationPolicyForModify(TeaModel):
    def __init__(
        self,
        alert_event_integration_policy_name: str = None,
        description: str = None,
        filter_setting: FilterSetting = None,
        integration_setting: str = None,
        transformer_setting: List[TransformAction] = None,
        type: str = None,
    ):
        # This parameter is required.
        self.alert_event_integration_policy_name = alert_event_integration_policy_name
        self.description = description
        self.filter_setting = filter_setting
        self.integration_setting = integration_setting
        self.transformer_setting = transformer_setting
        self.type = type

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()
        if self.transformer_setting:
            for k in self.transformer_setting:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_event_integration_policy_name is not None:
            result['alertEventIntegrationPolicyName'] = self.alert_event_integration_policy_name
        if self.description is not None:
            result['description'] = self.description
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.integration_setting is not None:
            result['integrationSetting'] = self.integration_setting
        result['transformerSetting'] = []
        if self.transformer_setting is not None:
            for k in self.transformer_setting:
                result['transformerSetting'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEventIntegrationPolicyName') is not None:
            self.alert_event_integration_policy_name = m.get('alertEventIntegrationPolicyName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('integrationSetting') is not None:
            self.integration_setting = m.get('integrationSetting')
        self.transformer_setting = []
        if m.get('transformerSetting') is not None:
            for k in m.get('transformerSetting'):
                temp_model = TransformAction()
                self.transformer_setting.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AlertEventIntegrationPolicyForView(TeaModel):
    def __init__(
        self,
        alert_event_integration_policy_id: str = None,
        alert_event_integration_policy_name: str = None,
        create_time: str = None,
        description: str = None,
        enable: bool = None,
        filter_setting: FilterSetting = None,
        integration_setting: str = None,
        transformer_setting: List[TransformAction] = None,
        type: str = None,
        update_time: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.alert_event_integration_policy_id = alert_event_integration_policy_id
        # This parameter is required.
        self.alert_event_integration_policy_name = alert_event_integration_policy_name
        self.create_time = create_time
        self.description = description
        self.enable = enable
        self.filter_setting = filter_setting
        self.integration_setting = integration_setting
        self.transformer_setting = transformer_setting
        self.type = type
        self.update_time = update_time
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()
        if self.transformer_setting:
            for k in self.transformer_setting:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_event_integration_policy_id is not None:
            result['alertEventIntegrationPolicyId'] = self.alert_event_integration_policy_id
        if self.alert_event_integration_policy_name is not None:
            result['alertEventIntegrationPolicyName'] = self.alert_event_integration_policy_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.enable is not None:
            result['enable'] = self.enable
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.integration_setting is not None:
            result['integrationSetting'] = self.integration_setting
        result['transformerSetting'] = []
        if self.transformer_setting is not None:
            for k in self.transformer_setting:
                result['transformerSetting'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEventIntegrationPolicyId') is not None:
            self.alert_event_integration_policy_id = m.get('alertEventIntegrationPolicyId')
        if m.get('alertEventIntegrationPolicyName') is not None:
            self.alert_event_integration_policy_name = m.get('alertEventIntegrationPolicyName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('integrationSetting') is not None:
            self.integration_setting = m.get('integrationSetting')
        self.transformer_setting = []
        if m.get('transformerSetting') is not None:
            for k in m.get('transformerSetting'):
                temp_model = TransformAction()
                self.transformer_setting.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class AlertRuleAction(TeaModel):
    def __init__(
        self,
        actions: List[str] = None,
    ):
        self.actions = actions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.actions is not None:
            result['actions'] = self.actions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('actions') is not None:
            self.actions = m.get('actions')
        return self


class AlertRuleAlertMetricFilterDefSupportedOpts(TeaModel):
    def __init__(
        self,
        display_name_cn: str = None,
        display_name_en: str = None,
        value: str = None,
    ):
        self.display_name_cn = display_name_cn
        self.display_name_en = display_name_en
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name_cn is not None:
            result['displayNameCn'] = self.display_name_cn
        if self.display_name_en is not None:
            result['displayNameEn'] = self.display_name_en
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayNameCn') is not None:
            self.display_name_cn = m.get('displayNameCn')
        if m.get('displayNameEn') is not None:
            self.display_name_en = m.get('displayNameEn')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AlertRuleAlertMetricFilterDef(TeaModel):
    def __init__(
        self,
        dim: str = None,
        display_name_cn: str = None,
        display_name_en: str = None,
        hidden: bool = None,
        opt: str = None,
        supported_opts: List[AlertRuleAlertMetricFilterDefSupportedOpts] = None,
    ):
        self.dim = dim
        self.display_name_cn = display_name_cn
        self.display_name_en = display_name_en
        self.hidden = hidden
        self.opt = opt
        self.supported_opts = supported_opts

    def validate(self):
        if self.supported_opts:
            for k in self.supported_opts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dim is not None:
            result['dim'] = self.dim
        if self.display_name_cn is not None:
            result['displayNameCn'] = self.display_name_cn
        if self.display_name_en is not None:
            result['displayNameEn'] = self.display_name_en
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.opt is not None:
            result['opt'] = self.opt
        result['supportedOpts'] = []
        if self.supported_opts is not None:
            for k in self.supported_opts:
                result['supportedOpts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dim') is not None:
            self.dim = m.get('dim')
        if m.get('displayNameCn') is not None:
            self.display_name_cn = m.get('displayNameCn')
        if m.get('displayNameEn') is not None:
            self.display_name_en = m.get('displayNameEn')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('opt') is not None:
            self.opt = m.get('opt')
        self.supported_opts = []
        if m.get('supportedOpts') is not None:
            for k in m.get('supportedOpts'):
                temp_model = AlertRuleAlertMetricFilterDefSupportedOpts()
                self.supported_opts.append(temp_model.from_map(k))
        return self


class AlertRuleAlertMetricInputFilterValue(TeaModel):
    def __init__(
        self,
        dim: str = None,
        opt: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.dim = dim
        # This parameter is required.
        self.opt = opt
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dim is not None:
            result['dim'] = self.dim
        if self.opt is not None:
            result['opt'] = self.opt
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dim') is not None:
            self.dim = m.get('dim')
        if m.get('opt') is not None:
            self.opt = m.get('opt')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AlertRuleAlertMetricInputParamValue(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AlertRuleAlertMetricInput(TeaModel):
    def __init__(
        self,
        filter_values: List[AlertRuleAlertMetricInputFilterValue] = None,
        group_id: str = None,
        metric_id: str = None,
        param_values: List[AlertRuleAlertMetricInputParamValue] = None,
    ):
        self.filter_values = filter_values
        self.group_id = group_id
        self.metric_id = metric_id
        self.param_values = param_values

    def validate(self):
        if self.filter_values:
            for k in self.filter_values:
                if k:
                    k.validate()
        if self.param_values:
            for k in self.param_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['filterValues'] = []
        if self.filter_values is not None:
            for k in self.filter_values:
                result['filterValues'].append(k.to_map() if k else None)
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.metric_id is not None:
            result['metricId'] = self.metric_id
        result['paramValues'] = []
        if self.param_values is not None:
            for k in self.param_values:
                result['paramValues'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_values = []
        if m.get('filterValues') is not None:
            for k in m.get('filterValues'):
                temp_model = AlertRuleAlertMetricInputFilterValue()
                self.filter_values.append(temp_model.from_map(k))
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('metricId') is not None:
            self.metric_id = m.get('metricId')
        self.param_values = []
        if m.get('paramValues') is not None:
            for k in m.get('paramValues'):
                temp_model = AlertRuleAlertMetricInputParamValue()
                self.param_values.append(temp_model.from_map(k))
        return self


class AlertRuleAlertMetricParamDefValues(TeaModel):
    def __init__(
        self,
        label_cn: str = None,
        label_en: str = None,
        value: str = None,
    ):
        self.label_cn = label_cn
        self.label_en = label_en
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_cn is not None:
            result['labelCn'] = self.label_cn
        if self.label_en is not None:
            result['labelEn'] = self.label_en
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelCn') is not None:
            self.label_cn = m.get('labelCn')
        if m.get('labelEn') is not None:
            self.label_en = m.get('labelEn')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AlertRuleAlertMetricParamDef(TeaModel):
    def __init__(
        self,
        max_width: int = None,
        min_width: int = None,
        name: str = None,
        placeholder_cn: str = None,
        placeholder_en: str = None,
        type: str = None,
        value: str = None,
        values: List[AlertRuleAlertMetricParamDefValues] = None,
    ):
        self.max_width = max_width
        self.min_width = min_width
        self.name = name
        self.placeholder_cn = placeholder_cn
        self.placeholder_en = placeholder_en
        self.type = type
        self.value = value
        self.values = values

    def validate(self):
        if self.values:
            for k in self.values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_width is not None:
            result['maxWidth'] = self.max_width
        if self.min_width is not None:
            result['minWidth'] = self.min_width
        if self.name is not None:
            result['name'] = self.name
        if self.placeholder_cn is not None:
            result['placeholderCn'] = self.placeholder_cn
        if self.placeholder_en is not None:
            result['placeholderEn'] = self.placeholder_en
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        result['values'] = []
        if self.values is not None:
            for k in self.values:
                result['values'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxWidth') is not None:
            self.max_width = m.get('maxWidth')
        if m.get('minWidth') is not None:
            self.min_width = m.get('minWidth')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('placeholderCn') is not None:
            self.placeholder_cn = m.get('placeholderCn')
        if m.get('placeholderEn') is not None:
            self.placeholder_en = m.get('placeholderEn')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        self.values = []
        if m.get('values') is not None:
            for k in m.get('values'):
                temp_model = AlertRuleAlertMetricParamDefValues()
                self.values.append(temp_model.from_map(k))
        return self


class AlertRuleConditionCaseList(TeaModel):
    def __init__(
        self,
        condition: str = None,
        count_condition: str = None,
        level: str = None,
        type: str = None,
    ):
        self.condition = condition
        self.count_condition = count_condition
        self.level = level
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['condition'] = self.condition
        if self.count_condition is not None:
            result['countCondition'] = self.count_condition
        if self.level is not None:
            result['level'] = self.level
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('countCondition') is not None:
            self.count_condition = m.get('countCondition')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AlertRuleConditionCompareListValueLevelList(TeaModel):
    def __init__(
        self,
        level: str = None,
        value: float = None,
    ):
        self.level = level
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['level'] = self.level
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AlertRuleConditionCompareList(TeaModel):
    def __init__(
        self,
        aggregate: str = None,
        oper: str = None,
        value: float = None,
        value_level_list: List[AlertRuleConditionCompareListValueLevelList] = None,
        yoy_time_unit: str = None,
        yoy_time_value: int = None,
    ):
        self.aggregate = aggregate
        self.oper = oper
        self.value = value
        self.value_level_list = value_level_list
        self.yoy_time_unit = yoy_time_unit
        self.yoy_time_value = yoy_time_value

    def validate(self):
        if self.value_level_list:
            for k in self.value_level_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aggregate is not None:
            result['aggregate'] = self.aggregate
        if self.oper is not None:
            result['oper'] = self.oper
        if self.value is not None:
            result['value'] = self.value
        result['valueLevelList'] = []
        if self.value_level_list is not None:
            for k in self.value_level_list:
                result['valueLevelList'].append(k.to_map() if k else None)
        if self.yoy_time_unit is not None:
            result['yoyTimeUnit'] = self.yoy_time_unit
        if self.yoy_time_value is not None:
            result['yoyTimeValue'] = self.yoy_time_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aggregate') is not None:
            self.aggregate = m.get('aggregate')
        if m.get('oper') is not None:
            self.oper = m.get('oper')
        if m.get('value') is not None:
            self.value = m.get('value')
        self.value_level_list = []
        if m.get('valueLevelList') is not None:
            for k in m.get('valueLevelList'):
                temp_model = AlertRuleConditionCompareListValueLevelList()
                self.value_level_list.append(temp_model.from_map(k))
        if m.get('yoyTimeUnit') is not None:
            self.yoy_time_unit = m.get('yoyTimeUnit')
        if m.get('yoyTimeValue') is not None:
            self.yoy_time_value = m.get('yoyTimeValue')
        return self


class AlertRuleCondition(TeaModel):
    def __init__(
        self,
        alert_count: int = None,
        case_list: List[AlertRuleConditionCaseList] = None,
        compare_list: List[AlertRuleConditionCompareList] = None,
        no_data_append_value: str = None,
        nodata_alert_level: str = None,
        type: str = None,
    ):
        # type=SLS_CONDITION时指定，满足条件几次后告警，默认为1
        self.alert_count = alert_count
        # type=SLS_CONDITION时指定
        self.case_list = case_list
        self.compare_list = compare_list
        self.no_data_append_value = no_data_append_value
        # 无数据时按什么级别告警，不指定则不对无数据报警
        self.nodata_alert_level = nodata_alert_level
        # 规则条件类型，可选值：SLS_CONDITION
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.case_list:
            for k in self.case_list:
                if k:
                    k.validate()
        if self.compare_list:
            for k in self.compare_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_count is not None:
            result['alertCount'] = self.alert_count
        result['caseList'] = []
        if self.case_list is not None:
            for k in self.case_list:
                result['caseList'].append(k.to_map() if k else None)
        result['compareList'] = []
        if self.compare_list is not None:
            for k in self.compare_list:
                result['compareList'].append(k.to_map() if k else None)
        if self.no_data_append_value is not None:
            result['noDataAppendValue'] = self.no_data_append_value
        if self.nodata_alert_level is not None:
            result['nodataAlertLevel'] = self.nodata_alert_level
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertCount') is not None:
            self.alert_count = m.get('alertCount')
        self.case_list = []
        if m.get('caseList') is not None:
            for k in m.get('caseList'):
                temp_model = AlertRuleConditionCaseList()
                self.case_list.append(temp_model.from_map(k))
        self.compare_list = []
        if m.get('compareList') is not None:
            for k in m.get('compareList'):
                temp_model = AlertRuleConditionCompareList()
                self.compare_list.append(temp_model.from_map(k))
        if m.get('noDataAppendValue') is not None:
            self.no_data_append_value = m.get('noDataAppendValue')
        if m.get('nodataAlertLevel') is not None:
            self.nodata_alert_level = m.get('nodataAlertLevel')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AlertRuleDataSourceDsList(TeaModel):
    def __init__(
        self,
        project: str = None,
        region_id: str = None,
        store: str = None,
        type: str = None,
    ):
        self.project = project
        self.region_id = region_id
        self.store = store
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.store is not None:
            result['store'] = self.store
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('store') is not None:
            self.store = m.get('store')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AlertRuleDataSource(TeaModel):
    def __init__(
        self,
        ds_list: List[AlertRuleDataSourceDsList] = None,
        instance_id: str = None,
        namespace: str = None,
        type: str = None,
    ):
        self.ds_list = ds_list
        # 实例id，当type=PROMETHEUS_DS/ENTERPRISE_DS时必填，为prometheus实例的clusterId或指标仓库名称
        self.instance_id = instance_id
        self.namespace = namespace
        # 数据源类型
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.ds_list:
            for k in self.ds_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['dsList'] = []
        if self.ds_list is not None:
            for k in self.ds_list:
                result['dsList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ds_list = []
        if m.get('dsList') is not None:
            for k in m.get('dsList'):
                temp_model = AlertRuleDataSourceDsList()
                self.ds_list.append(temp_model.from_map(k))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AlertRuleLabelFilter(TeaModel):
    def __init__(
        self,
        labels: Dict[str, str] = None,
        opt: str = None,
    ):
        self.labels = labels
        self.opt = opt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.opt is not None:
            result['opt'] = self.opt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('opt') is not None:
            self.opt = m.get('opt')
        return self


class AlertRuleTimeSpan(TeaModel):
    def __init__(
        self,
        day_of_week: List[int] = None,
        end_time: str = None,
        gmt_offset: str = None,
        start_time: str = None,
    ):
        self.day_of_week = day_of_week
        self.end_time = end_time
        self.gmt_offset = gmt_offset
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_of_week is not None:
            result['dayOfWeek'] = self.day_of_week
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.gmt_offset is not None:
            result['gmtOffset'] = self.gmt_offset
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayOfWeek') is not None:
            self.day_of_week = m.get('dayOfWeek')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('gmtOffset') is not None:
            self.gmt_offset = m.get('gmtOffset')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class AlertRuleNotification(TeaModel):
    def __init__(
        self,
        contacts: List[str] = None,
        custom_webhooks: List[str] = None,
        ding_webhooks: List[str] = None,
        fs_webhooks: List[str] = None,
        groups: List[str] = None,
        notify_time: AlertRuleTimeSpan = None,
        silence_time: int = None,
        slack_webhooks: List[str] = None,
        wx_webhooks: List[str] = None,
    ):
        self.contacts = contacts
        self.custom_webhooks = custom_webhooks
        self.ding_webhooks = ding_webhooks
        self.fs_webhooks = fs_webhooks
        self.groups = groups
        self.notify_time = notify_time
        self.silence_time = silence_time
        self.slack_webhooks = slack_webhooks
        self.wx_webhooks = wx_webhooks

    def validate(self):
        if self.notify_time:
            self.notify_time.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contacts is not None:
            result['contacts'] = self.contacts
        if self.custom_webhooks is not None:
            result['customWebhooks'] = self.custom_webhooks
        if self.ding_webhooks is not None:
            result['dingWebhooks'] = self.ding_webhooks
        if self.fs_webhooks is not None:
            result['fsWebhooks'] = self.fs_webhooks
        if self.groups is not None:
            result['groups'] = self.groups
        if self.notify_time is not None:
            result['notifyTime'] = self.notify_time.to_map()
        if self.silence_time is not None:
            result['silenceTime'] = self.silence_time
        if self.slack_webhooks is not None:
            result['slackWebhooks'] = self.slack_webhooks
        if self.wx_webhooks is not None:
            result['wxWebhooks'] = self.wx_webhooks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')
        if m.get('customWebhooks') is not None:
            self.custom_webhooks = m.get('customWebhooks')
        if m.get('dingWebhooks') is not None:
            self.ding_webhooks = m.get('dingWebhooks')
        if m.get('fsWebhooks') is not None:
            self.fs_webhooks = m.get('fsWebhooks')
        if m.get('groups') is not None:
            self.groups = m.get('groups')
        if m.get('notifyTime') is not None:
            temp_model = AlertRuleTimeSpan()
            self.notify_time = temp_model.from_map(m['notifyTime'])
        if m.get('silenceTime') is not None:
            self.silence_time = m.get('silenceTime')
        if m.get('slackWebhooks') is not None:
            self.slack_webhooks = m.get('slackWebhooks')
        if m.get('wxWebhooks') is not None:
            self.wx_webhooks = m.get('wxWebhooks')
        return self


class AlertRuleNotificationFilter(TeaModel):
    def __init__(
        self,
        contacts: List[str] = None,
        custom_webhooks: List[str] = None,
        ding_webhooks: List[str] = None,
        fs_webhooks: List[str] = None,
        groups: List[str] = None,
        slack_webhooks: List[str] = None,
        wx_webhooks: List[str] = None,
    ):
        self.contacts = contacts
        self.custom_webhooks = custom_webhooks
        self.ding_webhooks = ding_webhooks
        self.fs_webhooks = fs_webhooks
        self.groups = groups
        self.slack_webhooks = slack_webhooks
        self.wx_webhooks = wx_webhooks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contacts is not None:
            result['contacts'] = self.contacts
        if self.custom_webhooks is not None:
            result['customWebhooks'] = self.custom_webhooks
        if self.ding_webhooks is not None:
            result['dingWebhooks'] = self.ding_webhooks
        if self.fs_webhooks is not None:
            result['fsWebhooks'] = self.fs_webhooks
        if self.groups is not None:
            result['groups'] = self.groups
        if self.slack_webhooks is not None:
            result['slackWebhooks'] = self.slack_webhooks
        if self.wx_webhooks is not None:
            result['wxWebhooks'] = self.wx_webhooks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')
        if m.get('customWebhooks') is not None:
            self.custom_webhooks = m.get('customWebhooks')
        if m.get('dingWebhooks') is not None:
            self.ding_webhooks = m.get('dingWebhooks')
        if m.get('fsWebhooks') is not None:
            self.fs_webhooks = m.get('fsWebhooks')
        if m.get('groups') is not None:
            self.groups = m.get('groups')
        if m.get('slackWebhooks') is not None:
            self.slack_webhooks = m.get('slackWebhooks')
        if m.get('wxWebhooks') is not None:
            self.wx_webhooks = m.get('wxWebhooks')
        return self


class AlertRuleQueryQueries(TeaModel):
    def __init__(
        self,
        duration: int = None,
        end: int = None,
        expr: str = None,
        start: int = None,
        time_unit: str = None,
        window: str = None,
    ):
        self.duration = duration
        # 时间偏移结束时间(相对)，如果指定了start、end，则不指定window。
        self.end = end
        # 查询表达式
        # 
        # This parameter is required.
        self.expr = expr
        # sls查询的时间偏移开始时间(相对)，如果指定了start、end，则不指定window。  例如：start=15， timeUnit=minute，表示15分钟前
        self.start = start
        # start和end、window的时间单位： day/hour/minute/second
        self.time_unit = time_unit
        # 整点时间查询区间。  如果指定了window则不指定start、end
        self.window = window

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.end is not None:
            result['end'] = self.end
        if self.expr is not None:
            result['expr'] = self.expr
        if self.start is not None:
            result['start'] = self.start
        if self.time_unit is not None:
            result['timeUnit'] = self.time_unit
        if self.window is not None:
            result['window'] = self.window
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('timeUnit') is not None:
            self.time_unit = m.get('timeUnit')
        if m.get('window') is not None:
            self.window = m.get('window')
        return self


class AlertRuleSlsQueryJoinConditions(TeaModel):
    def __init__(
        self,
        first_field: str = None,
        oper: str = None,
        second_field: str = None,
    ):
        # 条件的左操作参数，格式为$<query_idx>.<结果集字段名>
        self.first_field = first_field
        # <, >, ==, !=, <=, >=\
        self.oper = oper
        # 条件的右操作参数，格式为$<query_idx>.<结果集字段名>
        self.second_field = second_field

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_field is not None:
            result['firstField'] = self.first_field
        if self.oper is not None:
            result['oper'] = self.oper
        if self.second_field is not None:
            result['secondField'] = self.second_field
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstField') is not None:
            self.first_field = m.get('firstField')
        if m.get('oper') is not None:
            self.oper = m.get('oper')
        if m.get('secondField') is not None:
            self.second_field = m.get('secondField')
        return self


class AlertRuleSlsQueryJoin(TeaModel):
    def __init__(
        self,
        conditions: List[AlertRuleSlsQueryJoinConditions] = None,
        type: str = None,
    ):
        self.conditions = conditions
        # 集合操作类型。
        #   ● CrossJoin： 笛卡尔积
        #   ● FullJoin：全联
        #   ● InnerJoin：内联
        #   ● LeftExclude： 左斥
        #   ● RightExclude：右斥
        #   ● LeftJoin：左联
        #   ● RightJoin：右联
        #   ● NoJoin：不合并
        #   ● Concat： 拼接
        #   https://help.aliyun.com/zh/sls/user-guide/set-query-statistics-statement
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['conditions'] = []
        if self.conditions is not None:
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k in m.get('conditions'):
                temp_model = AlertRuleSlsQueryJoinConditions()
                self.conditions.append(temp_model.from_map(k))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AlertRuleQuery(TeaModel):
    def __init__(
        self,
        duration: int = None,
        expr: str = None,
        first_join: AlertRuleSlsQueryJoin = None,
        group_field_list: List[str] = None,
        group_type: str = None,
        queries: List[AlertRuleQueryQueries] = None,
        second_join: AlertRuleSlsQueryJoin = None,
        type: str = None,
    ):
        self.duration = duration
        self.expr = expr
        self.first_join = first_join
        self.group_field_list = group_field_list
        self.group_type = group_type
        self.queries = queries
        self.second_join = second_join
        # 查询类型
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.first_join:
            self.first_join.validate()
        if self.queries:
            for k in self.queries:
                if k:
                    k.validate()
        if self.second_join:
            self.second_join.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.expr is not None:
            result['expr'] = self.expr
        if self.first_join is not None:
            result['firstJoin'] = self.first_join.to_map()
        if self.group_field_list is not None:
            result['groupFieldList'] = self.group_field_list
        if self.group_type is not None:
            result['groupType'] = self.group_type
        result['queries'] = []
        if self.queries is not None:
            for k in self.queries:
                result['queries'].append(k.to_map() if k else None)
        if self.second_join is not None:
            result['secondJoin'] = self.second_join.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('firstJoin') is not None:
            temp_model = AlertRuleSlsQueryJoin()
            self.first_join = temp_model.from_map(m['firstJoin'])
        if m.get('groupFieldList') is not None:
            self.group_field_list = m.get('groupFieldList')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        self.queries = []
        if m.get('queries') is not None:
            for k in m.get('queries'):
                temp_model = AlertRuleQueryQueries()
                self.queries.append(temp_model.from_map(k))
        if m.get('secondJoin') is not None:
            temp_model = AlertRuleSlsQueryJoin()
            self.second_join = temp_model.from_map(m['secondJoin'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AlertRuleSend(TeaModel):
    def __init__(
        self,
        action: AlertRuleAction = None,
        notification: AlertRuleNotification = None,
    ):
        self.action = action
        self.notification = notification

    def validate(self):
        if self.action:
            self.action.validate()
        if self.notification:
            self.notification.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action.to_map()
        if self.notification is not None:
            result['notification'] = self.notification.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            temp_model = AlertRuleAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('notification') is not None:
            temp_model = AlertRuleNotification()
            self.notification = temp_model.from_map(m['notification'])
        return self


class MaintainWindowForModify(TeaModel):
    def __init__(
        self,
        description: str = None,
        effective: str = None,
        end_time: str = None,
        filter_setting: FilterSetting = None,
        maintain_window_name: str = None,
        start_time: str = None,
    ):
        self.description = description
        self.effective = effective
        self.end_time = end_time
        self.filter_setting = filter_setting
        # This parameter is required.
        self.maintain_window_name = maintain_window_name
        self.start_time = start_time

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.effective is not None:
            result['effective'] = self.effective
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.maintain_window_name is not None:
            result['maintainWindowName'] = self.maintain_window_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('effective') is not None:
            self.effective = m.get('effective')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('maintainWindowName') is not None:
            self.maintain_window_name = m.get('maintainWindowName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        return self


class MaintainWindowForView(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        effective: str = None,
        enable: bool = None,
        end_time: str = None,
        filter_setting: FilterSetting = None,
        maintain_window_id: str = None,
        maintain_window_name: str = None,
        start_time: str = None,
        update_time: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.effective = effective
        self.enable = enable
        self.end_time = end_time
        self.filter_setting = filter_setting
        self.maintain_window_id = maintain_window_id
        # This parameter is required.
        self.maintain_window_name = maintain_window_name
        self.start_time = start_time
        self.update_time = update_time
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.effective is not None:
            result['effective'] = self.effective
        if self.enable is not None:
            result['enable'] = self.enable
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.maintain_window_id is not None:
            result['maintainWindowId'] = self.maintain_window_id
        if self.maintain_window_name is not None:
            result['maintainWindowName'] = self.maintain_window_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('effective') is not None:
            self.effective = m.get('effective')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('maintainWindowId') is not None:
            self.maintain_window_id = m.get('maintainWindowId')
        if m.get('maintainWindowName') is not None:
            self.maintain_window_name = m.get('maintainWindowName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class NotifyStrategyForModifyCustomTemplateEntries(TeaModel):
    def __init__(
        self,
        target_type: str = None,
        template_uuid: str = None,
    ):
        # This parameter is required.
        self.target_type = target_type
        # This parameter is required.
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_type is not None:
            result['targetType'] = self.target_type
        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')
        return self


class NotifyStrategyForModifyGroupingSetting(TeaModel):
    def __init__(
        self,
        grouping_keys: List[str] = None,
        period_min: int = None,
        silence_sec: int = None,
        times: int = None,
    ):
        self.grouping_keys = grouping_keys
        self.period_min = period_min
        self.silence_sec = silence_sec
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grouping_keys is not None:
            result['groupingKeys'] = self.grouping_keys
        if self.period_min is not None:
            result['periodMin'] = self.period_min
        if self.silence_sec is not None:
            result['silenceSec'] = self.silence_sec
        if self.times is not None:
            result['times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupingKeys') is not None:
            self.grouping_keys = m.get('groupingKeys')
        if m.get('periodMin') is not None:
            self.period_min = m.get('periodMin')
        if m.get('silenceSec') is not None:
            self.silence_sec = m.get('silenceSec')
        if m.get('times') is not None:
            self.times = m.get('times')
        return self


class NotifyStrategyForModifyRoutesChannels(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        enabled_sub_channels: List[str] = None,
        receivers: List[str] = None,
    ):
        # This parameter is required.
        self.channel_type = channel_type
        self.enabled_sub_channels = enabled_sub_channels
        # This parameter is required.
        self.receivers = receivers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['channelType'] = self.channel_type
        if self.enabled_sub_channels is not None:
            result['enabledSubChannels'] = self.enabled_sub_channels
        if self.receivers is not None:
            result['receivers'] = self.receivers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')
        if m.get('enabledSubChannels') is not None:
            self.enabled_sub_channels = m.get('enabledSubChannels')
        if m.get('receivers') is not None:
            self.receivers = m.get('receivers')
        return self


class NotifyStrategyForModifyRoutesEffectTimeRange(TeaModel):
    def __init__(
        self,
        day_in_week: List[int] = None,
        end_time_in_minute: int = None,
        start_time_in_minute: int = None,
        time_zone: str = None,
    ):
        self.day_in_week = day_in_week
        self.end_time_in_minute = end_time_in_minute
        self.start_time_in_minute = start_time_in_minute
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_in_week is not None:
            result['dayInWeek'] = self.day_in_week
        if self.end_time_in_minute is not None:
            result['endTimeInMinute'] = self.end_time_in_minute
        if self.start_time_in_minute is not None:
            result['startTimeInMinute'] = self.start_time_in_minute
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayInWeek') is not None:
            self.day_in_week = m.get('dayInWeek')
        if m.get('endTimeInMinute') is not None:
            self.end_time_in_minute = m.get('endTimeInMinute')
        if m.get('startTimeInMinute') is not None:
            self.start_time_in_minute = m.get('startTimeInMinute')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class NotifyStrategyForModifyRoutes(TeaModel):
    def __init__(
        self,
        channels: List[NotifyStrategyForModifyRoutesChannels] = None,
        effect_time_range: NotifyStrategyForModifyRoutesEffectTimeRange = None,
        filter_setting: FilterSetting = None,
        severities: List[str] = None,
    ):
        self.channels = channels
        self.effect_time_range = effect_time_range
        self.filter_setting = filter_setting
        self.severities = severities

    def validate(self):
        if self.channels:
            for k in self.channels:
                if k:
                    k.validate()
        if self.effect_time_range:
            self.effect_time_range.validate()
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['channels'].append(k.to_map() if k else None)
        if self.effect_time_range is not None:
            result['effectTimeRange'] = self.effect_time_range.to_map()
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.severities is not None:
            result['severities'] = self.severities
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('channels') is not None:
            for k in m.get('channels'):
                temp_model = NotifyStrategyForModifyRoutesChannels()
                self.channels.append(temp_model.from_map(k))
        if m.get('effectTimeRange') is not None:
            temp_model = NotifyStrategyForModifyRoutesEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m['effectTimeRange'])
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('severities') is not None:
            self.severities = m.get('severities')
        return self


class NotifyStrategyForModify(TeaModel):
    def __init__(
        self,
        custom_template_entries: List[NotifyStrategyForModifyCustomTemplateEntries] = None,
        description: str = None,
        grouping_setting: NotifyStrategyForModifyGroupingSetting = None,
        ignore_restored_notification: bool = None,
        notify_strategy_name: str = None,
        routes: List[NotifyStrategyForModifyRoutes] = None,
    ):
        self.custom_template_entries = custom_template_entries
        self.description = description
        # This parameter is required.
        self.grouping_setting = grouping_setting
        self.ignore_restored_notification = ignore_restored_notification
        # This parameter is required.
        self.notify_strategy_name = notify_strategy_name
        # This parameter is required.
        self.routes = routes

    def validate(self):
        if self.custom_template_entries:
            for k in self.custom_template_entries:
                if k:
                    k.validate()
        if self.grouping_setting:
            self.grouping_setting.validate()
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['customTemplateEntries'] = []
        if self.custom_template_entries is not None:
            for k in self.custom_template_entries:
                result['customTemplateEntries'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.grouping_setting is not None:
            result['groupingSetting'] = self.grouping_setting.to_map()
        if self.ignore_restored_notification is not None:
            result['ignoreRestoredNotification'] = self.ignore_restored_notification
        if self.notify_strategy_name is not None:
            result['notifyStrategyName'] = self.notify_strategy_name
        result['routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['routes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_template_entries = []
        if m.get('customTemplateEntries') is not None:
            for k in m.get('customTemplateEntries'):
                temp_model = NotifyStrategyForModifyCustomTemplateEntries()
                self.custom_template_entries.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupingSetting') is not None:
            temp_model = NotifyStrategyForModifyGroupingSetting()
            self.grouping_setting = temp_model.from_map(m['groupingSetting'])
        if m.get('ignoreRestoredNotification') is not None:
            self.ignore_restored_notification = m.get('ignoreRestoredNotification')
        if m.get('notifyStrategyName') is not None:
            self.notify_strategy_name = m.get('notifyStrategyName')
        self.routes = []
        if m.get('routes') is not None:
            for k in m.get('routes'):
                temp_model = NotifyStrategyForModifyRoutes()
                self.routes.append(temp_model.from_map(k))
        return self


class NotifyStrategyForViewCustomTemplateEntries(TeaModel):
    def __init__(
        self,
        target_type: str = None,
        template_uuid: str = None,
    ):
        # This parameter is required.
        self.target_type = target_type
        # This parameter is required.
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_type is not None:
            result['targetType'] = self.target_type
        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetType') is not None:
            self.target_type = m.get('targetType')
        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')
        return self


class NotifyStrategyForViewGroupingSetting(TeaModel):
    def __init__(
        self,
        grouping_keys: List[str] = None,
        period_min: int = None,
        silence_sec: int = None,
        times: int = None,
    ):
        self.grouping_keys = grouping_keys
        self.period_min = period_min
        self.silence_sec = silence_sec
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grouping_keys is not None:
            result['groupingKeys'] = self.grouping_keys
        if self.period_min is not None:
            result['periodMin'] = self.period_min
        if self.silence_sec is not None:
            result['silenceSec'] = self.silence_sec
        if self.times is not None:
            result['times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupingKeys') is not None:
            self.grouping_keys = m.get('groupingKeys')
        if m.get('periodMin') is not None:
            self.period_min = m.get('periodMin')
        if m.get('silenceSec') is not None:
            self.silence_sec = m.get('silenceSec')
        if m.get('times') is not None:
            self.times = m.get('times')
        return self


class NotifyStrategyForViewRoutesChannels(TeaModel):
    def __init__(
        self,
        channel_type: str = None,
        enabled_sub_channels: List[str] = None,
        receivers: List[str] = None,
    ):
        # This parameter is required.
        self.channel_type = channel_type
        self.enabled_sub_channels = enabled_sub_channels
        # This parameter is required.
        self.receivers = receivers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_type is not None:
            result['channelType'] = self.channel_type
        if self.enabled_sub_channels is not None:
            result['enabledSubChannels'] = self.enabled_sub_channels
        if self.receivers is not None:
            result['receivers'] = self.receivers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channelType') is not None:
            self.channel_type = m.get('channelType')
        if m.get('enabledSubChannels') is not None:
            self.enabled_sub_channels = m.get('enabledSubChannels')
        if m.get('receivers') is not None:
            self.receivers = m.get('receivers')
        return self


class NotifyStrategyForViewRoutesEffectTimeRange(TeaModel):
    def __init__(
        self,
        day_in_week: List[int] = None,
        end_time_in_minute: int = None,
        start_time_in_minute: int = None,
        time_zone: str = None,
    ):
        self.day_in_week = day_in_week
        self.end_time_in_minute = end_time_in_minute
        self.start_time_in_minute = start_time_in_minute
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day_in_week is not None:
            result['dayInWeek'] = self.day_in_week
        if self.end_time_in_minute is not None:
            result['endTimeInMinute'] = self.end_time_in_minute
        if self.start_time_in_minute is not None:
            result['startTimeInMinute'] = self.start_time_in_minute
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dayInWeek') is not None:
            self.day_in_week = m.get('dayInWeek')
        if m.get('endTimeInMinute') is not None:
            self.end_time_in_minute = m.get('endTimeInMinute')
        if m.get('startTimeInMinute') is not None:
            self.start_time_in_minute = m.get('startTimeInMinute')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        return self


class NotifyStrategyForViewRoutes(TeaModel):
    def __init__(
        self,
        channels: List[NotifyStrategyForViewRoutesChannels] = None,
        effect_time_range: NotifyStrategyForViewRoutesEffectTimeRange = None,
        filter_setting: FilterSetting = None,
        severities: List[str] = None,
    ):
        self.channels = channels
        self.effect_time_range = effect_time_range
        self.filter_setting = filter_setting
        self.severities = severities

    def validate(self):
        if self.channels:
            for k in self.channels:
                if k:
                    k.validate()
        if self.effect_time_range:
            self.effect_time_range.validate()
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['channels'] = []
        if self.channels is not None:
            for k in self.channels:
                result['channels'].append(k.to_map() if k else None)
        if self.effect_time_range is not None:
            result['effectTimeRange'] = self.effect_time_range.to_map()
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.severities is not None:
            result['severities'] = self.severities
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.channels = []
        if m.get('channels') is not None:
            for k in m.get('channels'):
                temp_model = NotifyStrategyForViewRoutesChannels()
                self.channels.append(temp_model.from_map(k))
        if m.get('effectTimeRange') is not None:
            temp_model = NotifyStrategyForViewRoutesEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m['effectTimeRange'])
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('severities') is not None:
            self.severities = m.get('severities')
        return self


class NotifyStrategyForView(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        custom_template_entries: List[NotifyStrategyForViewCustomTemplateEntries] = None,
        description: str = None,
        enable: bool = None,
        grouping_setting: NotifyStrategyForViewGroupingSetting = None,
        ignore_restored_notification: bool = None,
        notify_strategy_id: str = None,
        notify_strategy_name: str = None,
        routes: List[NotifyStrategyForViewRoutes] = None,
        update_time: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.custom_template_entries = custom_template_entries
        self.description = description
        self.enable = enable
        # This parameter is required.
        self.grouping_setting = grouping_setting
        self.ignore_restored_notification = ignore_restored_notification
        self.notify_strategy_id = notify_strategy_id
        # This parameter is required.
        self.notify_strategy_name = notify_strategy_name
        # This parameter is required.
        self.routes = routes
        self.update_time = update_time
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.custom_template_entries:
            for k in self.custom_template_entries:
                if k:
                    k.validate()
        if self.grouping_setting:
            self.grouping_setting.validate()
        if self.routes:
            for k in self.routes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        result['customTemplateEntries'] = []
        if self.custom_template_entries is not None:
            for k in self.custom_template_entries:
                result['customTemplateEntries'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.enable is not None:
            result['enable'] = self.enable
        if self.grouping_setting is not None:
            result['groupingSetting'] = self.grouping_setting.to_map()
        if self.ignore_restored_notification is not None:
            result['ignoreRestoredNotification'] = self.ignore_restored_notification
        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id
        if self.notify_strategy_name is not None:
            result['notifyStrategyName'] = self.notify_strategy_name
        result['routes'] = []
        if self.routes is not None:
            for k in self.routes:
                result['routes'].append(k.to_map() if k else None)
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        self.custom_template_entries = []
        if m.get('customTemplateEntries') is not None:
            for k in m.get('customTemplateEntries'):
                temp_model = NotifyStrategyForViewCustomTemplateEntries()
                self.custom_template_entries.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('groupingSetting') is not None:
            temp_model = NotifyStrategyForViewGroupingSetting()
            self.grouping_setting = temp_model.from_map(m['groupingSetting'])
        if m.get('ignoreRestoredNotification') is not None:
            self.ignore_restored_notification = m.get('ignoreRestoredNotification')
        if m.get('notifyStrategyId') is not None:
            self.notify_strategy_id = m.get('notifyStrategyId')
        if m.get('notifyStrategyName') is not None:
            self.notify_strategy_name = m.get('notifyStrategyName')
        self.routes = []
        if m.get('routes') is not None:
            for k in m.get('routes'):
                temp_model = NotifyStrategyForViewRoutes()
                self.routes.append(temp_model.from_map(k))
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class SubscriptionForModifyPushingSetting(TeaModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
        response_plan_id: str = None,
        restore_action_ids: List[str] = None,
        template_uuid: str = None,
    ):
        self.alert_action_ids = alert_action_ids
        self.response_plan_id = response_plan_id
        self.restore_action_ids = restore_action_ids
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_action_ids is not None:
            result['alertActionIds'] = self.alert_action_ids
        if self.response_plan_id is not None:
            result['responsePlanId'] = self.response_plan_id
        if self.restore_action_ids is not None:
            result['restoreActionIds'] = self.restore_action_ids
        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids = m.get('alertActionIds')
        if m.get('responsePlanId') is not None:
            self.response_plan_id = m.get('responsePlanId')
        if m.get('restoreActionIds') is not None:
            self.restore_action_ids = m.get('restoreActionIds')
        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')
        return self


class SubscriptionForModify(TeaModel):
    def __init__(
        self,
        description: str = None,
        filter_setting: FilterSetting = None,
        notify_strategy_id: str = None,
        pushing_setting: SubscriptionForModifyPushingSetting = None,
        subscription_name: str = None,
    ):
        self.description = description
        self.filter_setting = filter_setting
        self.notify_strategy_id = notify_strategy_id
        self.pushing_setting = pushing_setting
        # This parameter is required.
        self.subscription_name = subscription_name

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()
        if self.pushing_setting:
            self.pushing_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id
        if self.pushing_setting is not None:
            result['pushingSetting'] = self.pushing_setting.to_map()
        if self.subscription_name is not None:
            result['subscriptionName'] = self.subscription_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('notifyStrategyId') is not None:
            self.notify_strategy_id = m.get('notifyStrategyId')
        if m.get('pushingSetting') is not None:
            temp_model = SubscriptionForModifyPushingSetting()
            self.pushing_setting = temp_model.from_map(m['pushingSetting'])
        if m.get('subscriptionName') is not None:
            self.subscription_name = m.get('subscriptionName')
        return self


class SubscriptionForViewPushingSetting(TeaModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
        response_plan_id: str = None,
        restore_action_ids: List[str] = None,
        template_uuid: str = None,
    ):
        self.alert_action_ids = alert_action_ids
        self.response_plan_id = response_plan_id
        self.restore_action_ids = restore_action_ids
        self.template_uuid = template_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_action_ids is not None:
            result['alertActionIds'] = self.alert_action_ids
        if self.response_plan_id is not None:
            result['responsePlanId'] = self.response_plan_id
        if self.restore_action_ids is not None:
            result['restoreActionIds'] = self.restore_action_ids
        if self.template_uuid is not None:
            result['templateUuid'] = self.template_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids = m.get('alertActionIds')
        if m.get('responsePlanId') is not None:
            self.response_plan_id = m.get('responsePlanId')
        if m.get('restoreActionIds') is not None:
            self.restore_action_ids = m.get('restoreActionIds')
        if m.get('templateUuid') is not None:
            self.template_uuid = m.get('templateUuid')
        return self


class SubscriptionForView(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        enable: bool = None,
        filter_setting: FilterSetting = None,
        notify_strategy_id: str = None,
        pushing_setting: SubscriptionForViewPushingSetting = None,
        subscription_id: str = None,
        subscription_name: str = None,
        update_time: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.enable = enable
        self.filter_setting = filter_setting
        self.notify_strategy_id = notify_strategy_id
        self.pushing_setting = pushing_setting
        self.subscription_id = subscription_id
        # This parameter is required.
        self.subscription_name = subscription_name
        self.update_time = update_time
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.filter_setting:
            self.filter_setting.validate()
        if self.pushing_setting:
            self.pushing_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.enable is not None:
            result['enable'] = self.enable
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.notify_strategy_id is not None:
            result['notifyStrategyId'] = self.notify_strategy_id
        if self.pushing_setting is not None:
            result['pushingSetting'] = self.pushing_setting.to_map()
        if self.subscription_id is not None:
            result['subscriptionId'] = self.subscription_id
        if self.subscription_name is not None:
            result['subscriptionName'] = self.subscription_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('notifyStrategyId') is not None:
            self.notify_strategy_id = m.get('notifyStrategyId')
        if m.get('pushingSetting') is not None:
            temp_model = SubscriptionForViewPushingSetting()
            self.pushing_setting = temp_model.from_map(m['pushingSetting'])
        if m.get('subscriptionId') is not None:
            self.subscription_id = m.get('subscriptionId')
        if m.get('subscriptionName') is not None:
            self.subscription_name = m.get('subscriptionName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class TransformerForModify(TeaModel):
    def __init__(
        self,
        actions: List[TransformAction] = None,
        description: str = None,
        filter_setting: FilterSetting = None,
        quit_after_match: bool = None,
        sort_id: int = None,
        transformer_name: str = None,
    ):
        self.actions = actions
        self.description = description
        self.filter_setting = filter_setting
        self.quit_after_match = quit_after_match
        self.sort_id = sort_id
        # This parameter is required.
        self.transformer_name = transformer_name

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['actions'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.quit_after_match is not None:
            result['quitAfterMatch'] = self.quit_after_match
        if self.sort_id is not None:
            result['sortId'] = self.sort_id
        if self.transformer_name is not None:
            result['transformerName'] = self.transformer_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('actions') is not None:
            for k in m.get('actions'):
                temp_model = TransformAction()
                self.actions.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('quitAfterMatch') is not None:
            self.quit_after_match = m.get('quitAfterMatch')
        if m.get('sortId') is not None:
            self.sort_id = m.get('sortId')
        if m.get('transformerName') is not None:
            self.transformer_name = m.get('transformerName')
        return self


class TransformerForView(TeaModel):
    def __init__(
        self,
        actions: List[TransformAction] = None,
        create_time: str = None,
        description: str = None,
        enable: bool = None,
        filter_setting: FilterSetting = None,
        quit_after_match: bool = None,
        sort_id: int = None,
        transformer_id: str = None,
        transformer_name: str = None,
        update_time: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.actions = actions
        self.create_time = create_time
        self.description = description
        self.enable = enable
        self.filter_setting = filter_setting
        self.quit_after_match = quit_after_match
        self.sort_id = sort_id
        self.transformer_id = transformer_id
        # This parameter is required.
        self.transformer_name = transformer_name
        self.update_time = update_time
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.actions:
            for k in self.actions:
                if k:
                    k.validate()
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['actions'] = []
        if self.actions is not None:
            for k in self.actions:
                result['actions'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.enable is not None:
            result['enable'] = self.enable
        if self.filter_setting is not None:
            result['filterSetting'] = self.filter_setting.to_map()
        if self.quit_after_match is not None:
            result['quitAfterMatch'] = self.quit_after_match
        if self.sort_id is not None:
            result['sortId'] = self.sort_id
        if self.transformer_id is not None:
            result['transformerId'] = self.transformer_id
        if self.transformer_name is not None:
            result['transformerName'] = self.transformer_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('actions') is not None:
            for k in m.get('actions'):
                temp_model = TransformAction()
                self.actions.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('filterSetting') is not None:
            temp_model = FilterSetting()
            self.filter_setting = temp_model.from_map(m['filterSetting'])
        if m.get('quitAfterMatch') is not None:
            self.quit_after_match = m.get('quitAfterMatch')
        if m.get('sortId') is not None:
            self.sort_id = m.get('sortId')
        if m.get('transformerId') is not None:
            self.transformer_id = m.get('transformerId')
        if m.get('transformerName') is not None:
            self.transformer_name = m.get('transformerName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListAlertActionsRequest(TeaModel):
    def __init__(
        self,
        alert_action_ids: List[str] = None,
        alert_action_name: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.alert_action_ids = alert_action_ids
        self.alert_action_name = alert_action_name
        self.page_number = page_number
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_action_ids is not None:
            result['alertActionIds'] = self.alert_action_ids
        if self.alert_action_name is not None:
            result['alertActionName'] = self.alert_action_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids = m.get('alertActionIds')
        if m.get('alertActionName') is not None:
            self.alert_action_name = m.get('alertActionName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAlertActionsShrinkRequest(TeaModel):
    def __init__(
        self,
        alert_action_ids_shrink: str = None,
        alert_action_name: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.alert_action_ids_shrink = alert_action_ids_shrink
        self.alert_action_name = alert_action_name
        self.page_number = page_number
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_action_ids_shrink is not None:
            result['alertActionIds'] = self.alert_action_ids_shrink
        if self.alert_action_name is not None:
            result['alertActionName'] = self.alert_action_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionIds') is not None:
            self.alert_action_ids_shrink = m.get('alertActionIds')
        if m.get('alertActionName') is not None:
            self.alert_action_name = m.get('alertActionName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAlertActionsResponseBodyAlertActionsEssParam(TeaModel):
    def __init__(
        self,
        ess_group_id: str = None,
        ess_rule_id: str = None,
        region_id: str = None,
    ):
        self.ess_group_id = ess_group_id
        self.ess_rule_id = ess_rule_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ess_group_id is not None:
            result['essGroupId'] = self.ess_group_id
        if self.ess_rule_id is not None:
            result['essRuleId'] = self.ess_rule_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('essGroupId') is not None:
            self.ess_group_id = m.get('essGroupId')
        if m.get('essRuleId') is not None:
            self.ess_rule_id = m.get('essRuleId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListAlertActionsResponseBodyAlertActionsFcParam(TeaModel):
    def __init__(
        self,
        function: str = None,
        region_id: str = None,
        service: str = None,
    ):
        self.function = function
        self.region_id = region_id
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function is not None:
            result['function'] = self.function
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.service is not None:
            result['service'] = self.service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('service') is not None:
            self.service = m.get('service')
        return self


class ListAlertActionsResponseBodyAlertActionsMnsParam(TeaModel):
    def __init__(
        self,
        mns_type: str = None,
        name: str = None,
        region_id: str = None,
    ):
        self.mns_type = mns_type
        self.name = name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mns_type is not None:
            result['mnsType'] = self.mns_type
        if self.name is not None:
            result['name'] = self.name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mnsType') is not None:
            self.mns_type = m.get('mnsType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListAlertActionsResponseBodyAlertActionsPagerDutyParam(TeaModel):
    def __init__(
        self,
        key: str = None,
        url: str = None,
    ):
        self.key = key
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListAlertActionsResponseBodyAlertActionsSlsParam(TeaModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region_id: str = None,
    ):
        self.logstore = logstore
        self.project = project
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logstore is not None:
            result['logstore'] = self.logstore
        if self.project is not None:
            result['project'] = self.project
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class ListAlertActionsResponseBodyAlertActionsWebhookParam(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        headers: Dict[str, str] = None,
        method: str = None,
        url: str = None,
    ):
        self.content_type = content_type
        self.headers = headers
        self.method = method
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.headers is not None:
            result['headers'] = self.headers
        if self.method is not None:
            result['method'] = self.method
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListAlertActionsResponseBodyAlertActions(TeaModel):
    def __init__(
        self,
        alert_action_id: str = None,
        alert_action_name: str = None,
        ess_param: ListAlertActionsResponseBodyAlertActionsEssParam = None,
        fc_param: ListAlertActionsResponseBodyAlertActionsFcParam = None,
        mns_param: ListAlertActionsResponseBodyAlertActionsMnsParam = None,
        pager_duty_param: ListAlertActionsResponseBodyAlertActionsPagerDutyParam = None,
        sls_param: ListAlertActionsResponseBodyAlertActionsSlsParam = None,
        type: str = None,
        webhook_param: ListAlertActionsResponseBodyAlertActionsWebhookParam = None,
    ):
        self.alert_action_id = alert_action_id
        self.alert_action_name = alert_action_name
        self.ess_param = ess_param
        self.fc_param = fc_param
        self.mns_param = mns_param
        self.pager_duty_param = pager_duty_param
        self.sls_param = sls_param
        self.type = type
        self.webhook_param = webhook_param

    def validate(self):
        if self.ess_param:
            self.ess_param.validate()
        if self.fc_param:
            self.fc_param.validate()
        if self.mns_param:
            self.mns_param.validate()
        if self.pager_duty_param:
            self.pager_duty_param.validate()
        if self.sls_param:
            self.sls_param.validate()
        if self.webhook_param:
            self.webhook_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_action_id is not None:
            result['alertActionId'] = self.alert_action_id
        if self.alert_action_name is not None:
            result['alertActionName'] = self.alert_action_name
        if self.ess_param is not None:
            result['essParam'] = self.ess_param.to_map()
        if self.fc_param is not None:
            result['fcParam'] = self.fc_param.to_map()
        if self.mns_param is not None:
            result['mnsParam'] = self.mns_param.to_map()
        if self.pager_duty_param is not None:
            result['pagerDutyParam'] = self.pager_duty_param.to_map()
        if self.sls_param is not None:
            result['slsParam'] = self.sls_param.to_map()
        if self.type is not None:
            result['type'] = self.type
        if self.webhook_param is not None:
            result['webhookParam'] = self.webhook_param.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertActionId') is not None:
            self.alert_action_id = m.get('alertActionId')
        if m.get('alertActionName') is not None:
            self.alert_action_name = m.get('alertActionName')
        if m.get('essParam') is not None:
            temp_model = ListAlertActionsResponseBodyAlertActionsEssParam()
            self.ess_param = temp_model.from_map(m['essParam'])
        if m.get('fcParam') is not None:
            temp_model = ListAlertActionsResponseBodyAlertActionsFcParam()
            self.fc_param = temp_model.from_map(m['fcParam'])
        if m.get('mnsParam') is not None:
            temp_model = ListAlertActionsResponseBodyAlertActionsMnsParam()
            self.mns_param = temp_model.from_map(m['mnsParam'])
        if m.get('pagerDutyParam') is not None:
            temp_model = ListAlertActionsResponseBodyAlertActionsPagerDutyParam()
            self.pager_duty_param = temp_model.from_map(m['pagerDutyParam'])
        if m.get('slsParam') is not None:
            temp_model = ListAlertActionsResponseBodyAlertActionsSlsParam()
            self.sls_param = temp_model.from_map(m['slsParam'])
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('webhookParam') is not None:
            temp_model = ListAlertActionsResponseBodyAlertActionsWebhookParam()
            self.webhook_param = temp_model.from_map(m['webhookParam'])
        return self


class ListAlertActionsResponseBody(TeaModel):
    def __init__(
        self,
        alert_actions: List[ListAlertActionsResponseBodyAlertActions] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total: int = None,
    ):
        self.alert_actions = alert_actions
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total = total

    def validate(self):
        if self.alert_actions:
            for k in self.alert_actions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['alertActions'] = []
        if self.alert_actions is not None:
            for k in self.alert_actions:
                result['alertActions'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alert_actions = []
        if m.get('alertActions') is not None:
            for k in m.get('alertActions'):
                temp_model = ListAlertActionsResponseBodyAlertActions()
                self.alert_actions.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAlertActionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlertActionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAlertActionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


