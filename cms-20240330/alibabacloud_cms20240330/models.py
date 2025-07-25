# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AddonMetaDashboards(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        url: str = None,
    ):
        self.description = description
        self.name = name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class AddonMetaEnvironmentsDependencies(TeaModel):
    def __init__(
        self,
        cluster_types: List[str] = None,
        features: Dict[str, bool] = None,
        services: List[str] = None,
    ):
        self.cluster_types = cluster_types
        self.features = features
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_types is not None:
            result['clusterTypes'] = self.cluster_types
        if self.features is not None:
            result['features'] = self.features
        if self.services is not None:
            result['services'] = self.services
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterTypes') is not None:
            self.cluster_types = m.get('clusterTypes')
        if m.get('features') is not None:
            self.features = m.get('features')
        if m.get('services') is not None:
            self.services = m.get('services')
        return self


class AddonMetaEnvironmentsPoliciesBindEntity(TeaModel):
    def __init__(
        self,
        entity_group_mode: bool = None,
        entity_type: str = None,
        single_entity_mode: bool = None,
        vpc_id_field_key: str = None,
    ):
        self.entity_group_mode = entity_group_mode
        self.entity_type = entity_type
        self.single_entity_mode = single_entity_mode
        self.vpc_id_field_key = vpc_id_field_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_group_mode is not None:
            result['entityGroupMode'] = self.entity_group_mode
        if self.entity_type is not None:
            result['entityType'] = self.entity_type
        if self.single_entity_mode is not None:
            result['singleEntityMode'] = self.single_entity_mode
        if self.vpc_id_field_key is not None:
            result['vpcIdFieldKey'] = self.vpc_id_field_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityGroupMode') is not None:
            self.entity_group_mode = m.get('entityGroupMode')
        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')
        if m.get('singleEntityMode') is not None:
            self.single_entity_mode = m.get('singleEntityMode')
        if m.get('vpcIdFieldKey') is not None:
            self.vpc_id_field_key = m.get('vpcIdFieldKey')
        return self


class AddonMetaEnvironmentsPoliciesMetricCheckRule(TeaModel):
    def __init__(
        self,
        prom_ql: List[str] = None,
    ):
        self.prom_ql = prom_ql

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prom_ql is not None:
            result['promQL'] = self.prom_ql
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('promQL') is not None:
            self.prom_ql = m.get('promQL')
        return self


class AddonMetaEnvironmentsPoliciesProtocols(TeaModel):
    def __init__(
        self,
        description: str = None,
        icon: str = None,
        label: str = None,
        name: str = None,
    ):
        self.description = description
        self.icon = icon
        self.label = label
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.icon is not None:
            result['icon'] = self.icon
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class AddonMetaEnvironmentsPolicies(TeaModel):
    def __init__(
        self,
        alert_default_status: str = None,
        bind_default_policy: bool = None,
        bind_entity: AddonMetaEnvironmentsPoliciesBindEntity = None,
        default_install: bool = None,
        enable_service_account: bool = None,
        metric_check_rule: AddonMetaEnvironmentsPoliciesMetricCheckRule = None,
        need_restart_after_integration: bool = None,
        protocols: List[AddonMetaEnvironmentsPoliciesProtocols] = None,
        target_addon_name: str = None,
    ):
        self.alert_default_status = alert_default_status
        self.bind_default_policy = bind_default_policy
        self.bind_entity = bind_entity
        self.default_install = default_install
        self.enable_service_account = enable_service_account
        self.metric_check_rule = metric_check_rule
        self.need_restart_after_integration = need_restart_after_integration
        self.protocols = protocols
        self.target_addon_name = target_addon_name

    def validate(self):
        if self.bind_entity:
            self.bind_entity.validate()
        if self.metric_check_rule:
            self.metric_check_rule.validate()
        if self.protocols:
            for k in self.protocols:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_default_status is not None:
            result['alertDefaultStatus'] = self.alert_default_status
        if self.bind_default_policy is not None:
            result['bindDefaultPolicy'] = self.bind_default_policy
        if self.bind_entity is not None:
            result['bindEntity'] = self.bind_entity.to_map()
        if self.default_install is not None:
            result['defaultInstall'] = self.default_install
        if self.enable_service_account is not None:
            result['enableServiceAccount'] = self.enable_service_account
        if self.metric_check_rule is not None:
            result['metricCheckRule'] = self.metric_check_rule.to_map()
        if self.need_restart_after_integration is not None:
            result['needRestartAfterIntegration'] = self.need_restart_after_integration
        result['protocols'] = []
        if self.protocols is not None:
            for k in self.protocols:
                result['protocols'].append(k.to_map() if k else None)
        if self.target_addon_name is not None:
            result['targetAddonName'] = self.target_addon_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertDefaultStatus') is not None:
            self.alert_default_status = m.get('alertDefaultStatus')
        if m.get('bindDefaultPolicy') is not None:
            self.bind_default_policy = m.get('bindDefaultPolicy')
        if m.get('bindEntity') is not None:
            temp_model = AddonMetaEnvironmentsPoliciesBindEntity()
            self.bind_entity = temp_model.from_map(m['bindEntity'])
        if m.get('defaultInstall') is not None:
            self.default_install = m.get('defaultInstall')
        if m.get('enableServiceAccount') is not None:
            self.enable_service_account = m.get('enableServiceAccount')
        if m.get('metricCheckRule') is not None:
            temp_model = AddonMetaEnvironmentsPoliciesMetricCheckRule()
            self.metric_check_rule = temp_model.from_map(m['metricCheckRule'])
        if m.get('needRestartAfterIntegration') is not None:
            self.need_restart_after_integration = m.get('needRestartAfterIntegration')
        self.protocols = []
        if m.get('protocols') is not None:
            for k in m.get('protocols'):
                temp_model = AddonMetaEnvironmentsPoliciesProtocols()
                self.protocols.append(temp_model.from_map(k))
        if m.get('targetAddonName') is not None:
            self.target_addon_name = m.get('targetAddonName')
        return self


class AddonMetaEnvironments(TeaModel):
    def __init__(
        self,
        dependencies: AddonMetaEnvironmentsDependencies = None,
        description: str = None,
        enable: bool = None,
        label: str = None,
        name: str = None,
        policies: AddonMetaEnvironmentsPolicies = None,
        policy_type: str = None,
    ):
        self.dependencies = dependencies
        self.description = description
        self.enable = enable
        self.label = label
        self.name = name
        self.policies = policies
        self.policy_type = policy_type

    def validate(self):
        if self.dependencies:
            self.dependencies.validate()
        if self.policies:
            self.policies.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dependencies is not None:
            result['dependencies'] = self.dependencies.to_map()
        if self.description is not None:
            result['description'] = self.description
        if self.enable is not None:
            result['enable'] = self.enable
        if self.label is not None:
            result['label'] = self.label
        if self.name is not None:
            result['name'] = self.name
        if self.policies is not None:
            result['policies'] = self.policies.to_map()
        if self.policy_type is not None:
            result['policyType'] = self.policy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dependencies') is not None:
            temp_model = AddonMetaEnvironmentsDependencies()
            self.dependencies = temp_model.from_map(m['dependencies'])
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('policies') is not None:
            temp_model = AddonMetaEnvironmentsPolicies()
            self.policies = temp_model.from_map(m['policies'])
        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')
        return self


class AddonMeta(TeaModel):
    def __init__(
        self,
        alias: str = None,
        categories: List[str] = None,
        dashboards: List[AddonMetaDashboards] = None,
        description: str = None,
        environments: List[AddonMetaEnvironments] = None,
        icon: str = None,
        keywords: List[str] = None,
        language: str = None,
        latest_release_create_time: str = None,
        name: str = None,
        once: bool = None,
        scene: str = None,
        version: str = None,
        weight: int = None,
    ):
        self.alias = alias
        self.categories = categories
        self.dashboards = dashboards
        self.description = description
        self.environments = environments
        self.icon = icon
        self.keywords = keywords
        self.language = language
        self.latest_release_create_time = latest_release_create_time
        self.name = name
        self.once = once
        self.scene = scene
        self.version = version
        self.weight = weight

    def validate(self):
        if self.dashboards:
            for k in self.dashboards:
                if k:
                    k.validate()
        if self.environments:
            for k in self.environments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['alias'] = self.alias
        if self.categories is not None:
            result['categories'] = self.categories
        result['dashboards'] = []
        if self.dashboards is not None:
            for k in self.dashboards:
                result['dashboards'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        result['environments'] = []
        if self.environments is not None:
            for k in self.environments:
                result['environments'].append(k.to_map() if k else None)
        if self.icon is not None:
            result['icon'] = self.icon
        if self.keywords is not None:
            result['keywords'] = self.keywords
        if self.language is not None:
            result['language'] = self.language
        if self.latest_release_create_time is not None:
            result['latestReleaseCreateTime'] = self.latest_release_create_time
        if self.name is not None:
            result['name'] = self.name
        if self.once is not None:
            result['once'] = self.once
        if self.scene is not None:
            result['scene'] = self.scene
        if self.version is not None:
            result['version'] = self.version
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')
        if m.get('categories') is not None:
            self.categories = m.get('categories')
        self.dashboards = []
        if m.get('dashboards') is not None:
            for k in m.get('dashboards'):
                temp_model = AddonMetaDashboards()
                self.dashboards.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        self.environments = []
        if m.get('environments') is not None:
            for k in m.get('environments'):
                temp_model = AddonMetaEnvironments()
                self.environments.append(temp_model.from_map(k))
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('latestReleaseCreateTime') is not None:
            self.latest_release_create_time = m.get('latestReleaseCreateTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('once') is not None:
            self.once = m.get('once')
        if m.get('scene') is not None:
            self.scene = m.get('scene')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


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
        token: str = None,
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
        self.token = token
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
        if self.token is not None:
            result['token'] = self.token
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
        if m.get('token') is not None:
            self.token = m.get('token')
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
        dim_disabled: bool = None,
        display_name_cn: str = None,
        display_name_en: str = None,
        hidden: bool = None,
        label_disabled: bool = None,
        opt: str = None,
        supported_opts: List[AlertRuleAlertMetricFilterDefSupportedOpts] = None,
    ):
        self.dim = dim
        self.dim_disabled = dim_disabled
        self.display_name_cn = display_name_cn
        self.display_name_en = display_name_en
        self.hidden = hidden
        self.label_disabled = label_disabled
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
        if self.dim_disabled is not None:
            result['dimDisabled'] = self.dim_disabled
        if self.display_name_cn is not None:
            result['displayNameCn'] = self.display_name_cn
        if self.display_name_en is not None:
            result['displayNameEn'] = self.display_name_en
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.label_disabled is not None:
            result['labelDisabled'] = self.label_disabled
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
        if m.get('dimDisabled') is not None:
            self.dim_disabled = m.get('dimDisabled')
        if m.get('displayNameCn') is not None:
            self.display_name_cn = m.get('displayNameCn')
        if m.get('displayNameEn') is not None:
            self.display_name_en = m.get('displayNameEn')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('labelDisabled') is not None:
            self.label_disabled = m.get('labelDisabled')
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


class AlertRuleConditionCompositeEscalationEscalations(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        metric_name: str = None,
        period: int = None,
        statistics: str = None,
        threshold: float = None,
    ):
        self.comparison_operator = comparison_operator
        self.metric_name = metric_name
        self.period = period
        self.statistics = statistics
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.period is not None:
            result['period'] = self.period
        if self.statistics is not None:
            result['statistics'] = self.statistics
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class AlertRuleConditionCompositeEscalation(TeaModel):
    def __init__(
        self,
        escalations: List[AlertRuleConditionCompositeEscalationEscalations] = None,
        level: str = None,
        relation: str = None,
        times: int = None,
    ):
        self.escalations = escalations
        self.level = level
        self.relation = relation
        self.times = times

    def validate(self):
        if self.escalations:
            for k in self.escalations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['escalations'] = []
        if self.escalations is not None:
            for k in self.escalations:
                result['escalations'].append(k.to_map() if k else None)
        if self.level is not None:
            result['level'] = self.level
        if self.relation is not None:
            result['relation'] = self.relation
        if self.times is not None:
            result['times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalations = []
        if m.get('escalations') is not None:
            for k in m.get('escalations'):
                temp_model = AlertRuleConditionCompositeEscalationEscalations()
                self.escalations.append(temp_model.from_map(k))
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('relation') is not None:
            self.relation = m.get('relation')
        if m.get('times') is not None:
            self.times = m.get('times')
        return self


class AlertRuleConditionExpressEscalation(TeaModel):
    def __init__(
        self,
        level: str = None,
        raw_expression: str = None,
        times: int = None,
    ):
        self.level = level
        self.raw_expression = raw_expression
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['level'] = self.level
        if self.raw_expression is not None:
            result['rawExpression'] = self.raw_expression
        if self.times is not None:
            result['times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('rawExpression') is not None:
            self.raw_expression = m.get('rawExpression')
        if m.get('times') is not None:
            self.times = m.get('times')
        return self


class AlertRuleConditionSimpleEscalationEscalations(TeaModel):
    def __init__(
        self,
        comparison_operator: str = None,
        level: str = None,
        statistics: str = None,
        threshold: float = None,
        times: int = None,
    ):
        self.comparison_operator = comparison_operator
        self.level = level
        self.statistics = statistics
        self.threshold = threshold
        self.times = times

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison_operator is not None:
            result['comparisonOperator'] = self.comparison_operator
        if self.level is not None:
            result['level'] = self.level
        if self.statistics is not None:
            result['statistics'] = self.statistics
        if self.threshold is not None:
            result['threshold'] = self.threshold
        if self.times is not None:
            result['times'] = self.times
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comparisonOperator') is not None:
            self.comparison_operator = m.get('comparisonOperator')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('statistics') is not None:
            self.statistics = m.get('statistics')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        if m.get('times') is not None:
            self.times = m.get('times')
        return self


class AlertRuleConditionSimpleEscalation(TeaModel):
    def __init__(
        self,
        escalations: List[AlertRuleConditionSimpleEscalationEscalations] = None,
        metric_name: str = None,
        period: int = None,
    ):
        self.escalations = escalations
        self.metric_name = metric_name
        self.period = period

    def validate(self):
        if self.escalations:
            for k in self.escalations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['escalations'] = []
        if self.escalations is not None:
            for k in self.escalations:
                result['escalations'].append(k.to_map() if k else None)
        if self.metric_name is not None:
            result['metricName'] = self.metric_name
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.escalations = []
        if m.get('escalations') is not None:
            for k in m.get('escalations'):
                temp_model = AlertRuleConditionSimpleEscalationEscalations()
                self.escalations.append(temp_model.from_map(k))
        if m.get('metricName') is not None:
            self.metric_name = m.get('metricName')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self


class AlertRuleCondition(TeaModel):
    def __init__(
        self,
        alert_count: int = None,
        case_list: List[AlertRuleConditionCaseList] = None,
        compare_list: List[AlertRuleConditionCompareList] = None,
        composite_escalation: AlertRuleConditionCompositeEscalation = None,
        escalation_type: str = None,
        express_escalation: AlertRuleConditionExpressEscalation = None,
        no_data_alert_level: str = None,
        no_data_append_value: str = None,
        no_data_policy: str = None,
        relation: str = None,
        simple_escalation: AlertRuleConditionSimpleEscalation = None,
        type: str = None,
    ):
        # type=SLS_CONDITION时指定，满足条件几次后告警，默认为1
        self.alert_count = alert_count
        # type=SLS_CONDITION时指定
        self.case_list = case_list
        self.compare_list = compare_list
        self.composite_escalation = composite_escalation
        self.escalation_type = escalation_type
        self.express_escalation = express_escalation
        # 无数据时按什么级别告警，不指定则不对无数据报警
        self.no_data_alert_level = no_data_alert_level
        self.no_data_append_value = no_data_append_value
        self.no_data_policy = no_data_policy
        self.relation = relation
        self.simple_escalation = simple_escalation
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
        if self.composite_escalation:
            self.composite_escalation.validate()
        if self.express_escalation:
            self.express_escalation.validate()
        if self.simple_escalation:
            self.simple_escalation.validate()

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
        if self.composite_escalation is not None:
            result['compositeEscalation'] = self.composite_escalation.to_map()
        if self.escalation_type is not None:
            result['escalationType'] = self.escalation_type
        if self.express_escalation is not None:
            result['expressEscalation'] = self.express_escalation.to_map()
        if self.no_data_alert_level is not None:
            result['noDataAlertLevel'] = self.no_data_alert_level
        if self.no_data_append_value is not None:
            result['noDataAppendValue'] = self.no_data_append_value
        if self.no_data_policy is not None:
            result['noDataPolicy'] = self.no_data_policy
        if self.relation is not None:
            result['relation'] = self.relation
        if self.simple_escalation is not None:
            result['simpleEscalation'] = self.simple_escalation.to_map()
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
        if m.get('compositeEscalation') is not None:
            temp_model = AlertRuleConditionCompositeEscalation()
            self.composite_escalation = temp_model.from_map(m['compositeEscalation'])
        if m.get('escalationType') is not None:
            self.escalation_type = m.get('escalationType')
        if m.get('expressEscalation') is not None:
            temp_model = AlertRuleConditionExpressEscalation()
            self.express_escalation = temp_model.from_map(m['expressEscalation'])
        if m.get('noDataAlertLevel') is not None:
            self.no_data_alert_level = m.get('noDataAlertLevel')
        if m.get('noDataAppendValue') is not None:
            self.no_data_append_value = m.get('noDataAppendValue')
        if m.get('noDataPolicy') is not None:
            self.no_data_policy = m.get('noDataPolicy')
        if m.get('relation') is not None:
            self.relation = m.get('relation')
        if m.get('simpleEscalation') is not None:
            temp_model = AlertRuleConditionSimpleEscalation()
            self.simple_escalation = temp_model.from_map(m['simpleEscalation'])
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
        app_type: str = None,
        ds_list: List[AlertRuleDataSourceDsList] = None,
        instance_id: str = None,
        namespace: str = None,
        region_id: str = None,
        type: str = None,
    ):
        self.app_type = app_type
        self.ds_list = ds_list
        # 实例id，当type=PROMETHEUS_DS/ENTERPRISE_DS时必填，为prometheus实例的clusterId或指标仓库名称
        self.instance_id = instance_id
        self.namespace = namespace
        self.region_id = region_id
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
        if self.app_type is not None:
            result['appType'] = self.app_type
        result['dsList'] = []
        if self.ds_list is not None:
            for k in self.ds_list:
                result['dsList'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        self.ds_list = []
        if m.get('dsList') is not None:
            for k in m.get('dsList'):
                temp_model = AlertRuleDataSourceDsList()
                self.ds_list.append(temp_model.from_map(k))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
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


class AlertRuleQueryQueriesApmFilters(TeaModel):
    def __init__(
        self,
        dim: str = None,
        type: str = None,
        value: str = None,
    ):
        self.dim = dim
        self.type = type
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
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dim') is not None:
            self.dim = m.get('dim')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AlertRuleQueryQueries(TeaModel):
    def __init__(
        self,
        apm_alert_metric_id: str = None,
        apm_filters: List[AlertRuleQueryQueriesApmFilters] = None,
        apm_group_by: List[str] = None,
        duration: int = None,
        end: int = None,
        expr: str = None,
        start: int = None,
        time_unit: str = None,
        window: int = None,
    ):
        self.apm_alert_metric_id = apm_alert_metric_id
        self.apm_filters = apm_filters
        self.apm_group_by = apm_group_by
        self.duration = duration
        # 时间偏移结束时间(相对)，如果指定了start、end，则不指定window。
        self.end = end
        # 查询表达式
        self.expr = expr
        # sls查询的时间偏移开始时间(相对)，如果指定了start、end，则不指定window。  例如：start=15， timeUnit=minute，表示15分钟前
        self.start = start
        # start和end、window的时间单位： day/hour/minute/second
        self.time_unit = time_unit
        # 整点时间查询区间。  如果指定了window则不指定start、end
        self.window = window

    def validate(self):
        if self.apm_filters:
            for k in self.apm_filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apm_alert_metric_id is not None:
            result['apmAlertMetricId'] = self.apm_alert_metric_id
        result['apmFilters'] = []
        if self.apm_filters is not None:
            for k in self.apm_filters:
                result['apmFilters'].append(k.to_map() if k else None)
        if self.apm_group_by is not None:
            result['apmGroupBy'] = self.apm_group_by
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
        if m.get('apmAlertMetricId') is not None:
            self.apm_alert_metric_id = m.get('apmAlertMetricId')
        self.apm_filters = []
        if m.get('apmFilters') is not None:
            for k in m.get('apmFilters'):
                temp_model = AlertRuleQueryQueriesApmFilters()
                self.apm_filters.append(temp_model.from_map(k))
        if m.get('apmGroupBy') is not None:
            self.apm_group_by = m.get('apmGroupBy')
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
        check_after_data_complete: bool = None,
        dimensions: List[Dict[str, str]] = None,
        duration: int = None,
        expr: str = None,
        first_join: AlertRuleSlsQueryJoin = None,
        group_field_list: List[str] = None,
        group_id: str = None,
        group_type: str = None,
        namespace: str = None,
        queries: List[AlertRuleQueryQueries] = None,
        relation_type: str = None,
        second_join: AlertRuleSlsQueryJoin = None,
        type: str = None,
    ):
        self.check_after_data_complete = check_after_data_complete
        self.dimensions = dimensions
        self.duration = duration
        self.expr = expr
        self.first_join = first_join
        self.group_field_list = group_field_list
        self.group_id = group_id
        self.group_type = group_type
        self.namespace = namespace
        self.queries = queries
        self.relation_type = relation_type
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
        if self.check_after_data_complete is not None:
            result['checkAfterDataComplete'] = self.check_after_data_complete
        if self.dimensions is not None:
            result['dimensions'] = self.dimensions
        if self.duration is not None:
            result['duration'] = self.duration
        if self.expr is not None:
            result['expr'] = self.expr
        if self.first_join is not None:
            result['firstJoin'] = self.first_join.to_map()
        if self.group_field_list is not None:
            result['groupFieldList'] = self.group_field_list
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_type is not None:
            result['groupType'] = self.group_type
        if self.namespace is not None:
            result['namespace'] = self.namespace
        result['queries'] = []
        if self.queries is not None:
            for k in self.queries:
                result['queries'].append(k.to_map() if k else None)
        if self.relation_type is not None:
            result['relationType'] = self.relation_type
        if self.second_join is not None:
            result['secondJoin'] = self.second_join.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checkAfterDataComplete') is not None:
            self.check_after_data_complete = m.get('checkAfterDataComplete')
        if m.get('dimensions') is not None:
            self.dimensions = m.get('dimensions')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('expr') is not None:
            self.expr = m.get('expr')
        if m.get('firstJoin') is not None:
            temp_model = AlertRuleSlsQueryJoin()
            self.first_join = temp_model.from_map(m['firstJoin'])
        if m.get('groupFieldList') is not None:
            self.group_field_list = m.get('groupFieldList')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        self.queries = []
        if m.get('queries') is not None:
            for k in m.get('queries'):
                temp_model = AlertRuleQueryQueries()
                self.queries.append(temp_model.from_map(k))
        if m.get('relationType') is not None:
            self.relation_type = m.get('relationType')
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
        send_to_arms: bool = None,
    ):
        self.action = action
        self.notification = notification
        self.send_to_arms = send_to_arms

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
        if self.send_to_arms is not None:
            result['sendToArms'] = self.send_to_arms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            temp_model = AlertRuleAction()
            self.action = temp_model.from_map(m['action'])
        if m.get('notification') is not None:
            temp_model = AlertRuleNotification()
            self.notification = temp_model.from_map(m['notification'])
        if m.get('sendToArms') is not None:
            self.send_to_arms = m.get('sendToArms')
        return self


class BizTraceConfig(TeaModel):
    def __init__(
        self,
        advanced_config: str = None,
        biz_trace_code: str = None,
        biz_trace_id: str = None,
        biz_trace_name: str = None,
        create_time: str = None,
        region_id: str = None,
        rule_config: str = None,
        workspace: str = None,
    ):
        self.advanced_config = advanced_config
        self.biz_trace_code = biz_trace_code
        self.biz_trace_id = biz_trace_id
        self.biz_trace_name = biz_trace_name
        self.create_time = create_time
        self.region_id = region_id
        self.rule_config = rule_config
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced_config is not None:
            result['advancedConfig'] = self.advanced_config
        if self.biz_trace_code is not None:
            result['bizTraceCode'] = self.biz_trace_code
        if self.biz_trace_id is not None:
            result['bizTraceId'] = self.biz_trace_id
        if self.biz_trace_name is not None:
            result['bizTraceName'] = self.biz_trace_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.rule_config is not None:
            result['ruleConfig'] = self.rule_config
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advancedConfig') is not None:
            self.advanced_config = m.get('advancedConfig')
        if m.get('bizTraceCode') is not None:
            self.biz_trace_code = m.get('bizTraceCode')
        if m.get('bizTraceId') is not None:
            self.biz_trace_id = m.get('bizTraceId')
        if m.get('bizTraceName') is not None:
            self.biz_trace_name = m.get('bizTraceName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('ruleConfig') is not None:
            self.rule_config = m.get('ruleConfig')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class DataStorageItem(TeaModel):
    def __init__(
        self,
        data_type: str = None,
        project: str = None,
        region_id: str = None,
        store_name: str = None,
        store_type: str = None,
    ):
        self.data_type = data_type
        self.project = project
        self.region_id = region_id
        self.store_name = store_name
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.project is not None:
            result['project'] = self.project
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.store_name is not None:
            result['storeName'] = self.store_name
        if self.store_type is not None:
            result['storeType'] = self.store_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('storeName') is not None:
            self.store_name = m.get('storeName')
        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')
        return self


class EntityDiscoverRuleAnnotations(TeaModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.op = op
        self.tag_key = tag_key
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op is not None:
            result['op'] = self.op
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_values is not None:
            result['tagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValues') is not None:
            self.tag_values = m.get('tagValues')
        return self


class EntityDiscoverRuleFieldRules(TeaModel):
    def __init__(
        self,
        field_key: str = None,
        field_values: List[str] = None,
        op: str = None,
    ):
        self.field_key = field_key
        self.field_values = field_values
        self.op = op

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_key is not None:
            result['fieldKey'] = self.field_key
        if self.field_values is not None:
            result['fieldValues'] = self.field_values
        if self.op is not None:
            result['op'] = self.op
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')
        if m.get('fieldValues') is not None:
            self.field_values = m.get('fieldValues')
        if m.get('op') is not None:
            self.op = m.get('op')
        return self


class EntityDiscoverRuleIpMatchRule(TeaModel):
    def __init__(
        self,
        ip_cidr: str = None,
        ip_field_key: str = None,
    ):
        self.ip_cidr = ip_cidr
        self.ip_field_key = ip_field_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_cidr is not None:
            result['ipCIDR'] = self.ip_cidr
        if self.ip_field_key is not None:
            result['ipFieldKey'] = self.ip_field_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipCIDR') is not None:
            self.ip_cidr = m.get('ipCIDR')
        if m.get('ipFieldKey') is not None:
            self.ip_field_key = m.get('ipFieldKey')
        return self


class EntityDiscoverRuleLabels(TeaModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.op = op
        self.tag_key = tag_key
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op is not None:
            result['op'] = self.op
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_values is not None:
            result['tagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValues') is not None:
            self.tag_values = m.get('tagValues')
        return self


class EntityDiscoverRuleTags(TeaModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.op = op
        self.tag_key = tag_key
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.op is not None:
            result['op'] = self.op
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_values is not None:
            result['tagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValues') is not None:
            self.tag_values = m.get('tagValues')
        return self


class EntityDiscoverRule(TeaModel):
    def __init__(
        self,
        annotations: List[EntityDiscoverRuleAnnotations] = None,
        entity_types: List[str] = None,
        field_rules: List[EntityDiscoverRuleFieldRules] = None,
        instance_ids: List[str] = None,
        ip_match_rule: List[EntityDiscoverRuleIpMatchRule] = None,
        labels: List[EntityDiscoverRuleLabels] = None,
        region_ids: List[str] = None,
        resource_group_id: str = None,
        tags: List[EntityDiscoverRuleTags] = None,
    ):
        self.annotations = annotations
        self.entity_types = entity_types
        self.field_rules = field_rules
        self.instance_ids = instance_ids
        self.ip_match_rule = ip_match_rule
        self.labels = labels
        self.region_ids = region_ids
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.annotations:
            for k in self.annotations:
                if k:
                    k.validate()
        if self.field_rules:
            for k in self.field_rules:
                if k:
                    k.validate()
        if self.ip_match_rule:
            for k in self.ip_match_rule:
                if k:
                    k.validate()
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['annotations'] = []
        if self.annotations is not None:
            for k in self.annotations:
                result['annotations'].append(k.to_map() if k else None)
        if self.entity_types is not None:
            result['entityTypes'] = self.entity_types
        result['fieldRules'] = []
        if self.field_rules is not None:
            for k in self.field_rules:
                result['fieldRules'].append(k.to_map() if k else None)
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        result['ipMatchRule'] = []
        if self.ip_match_rule is not None:
            for k in self.ip_match_rule:
                result['ipMatchRule'].append(k.to_map() if k else None)
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.region_ids is not None:
            result['regionIds'] = self.region_ids
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotations = []
        if m.get('annotations') is not None:
            for k in m.get('annotations'):
                temp_model = EntityDiscoverRuleAnnotations()
                self.annotations.append(temp_model.from_map(k))
        if m.get('entityTypes') is not None:
            self.entity_types = m.get('entityTypes')
        self.field_rules = []
        if m.get('fieldRules') is not None:
            for k in m.get('fieldRules'):
                temp_model = EntityDiscoverRuleFieldRules()
                self.field_rules.append(temp_model.from_map(k))
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        self.ip_match_rule = []
        if m.get('ipMatchRule') is not None:
            for k in m.get('ipMatchRule'):
                temp_model = EntityDiscoverRuleIpMatchRule()
                self.ip_match_rule.append(temp_model.from_map(k))
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = EntityDiscoverRuleLabels()
                self.labels.append(temp_model.from_map(k))
        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = EntityDiscoverRuleTags()
                self.tags.append(temp_model.from_map(k))
        return self


class EntityGroupBaseEntityQueries(TeaModel):
    def __init__(
        self,
        entity_type: str = None,
        spl: str = None,
    ):
        self.entity_type = entity_type
        self.spl = spl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entity_type is not None:
            result['entityType'] = self.entity_type
        if self.spl is not None:
            result['spl'] = self.spl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')
        if m.get('spl') is not None:
            self.spl = m.get('spl')
        return self


class EntityGroupBase(TeaModel):
    def __init__(
        self,
        description: str = None,
        entity_group_id: str = None,
        entity_group_name: str = None,
        entity_queries: List[EntityGroupBaseEntityQueries] = None,
        entity_rules: EntityDiscoverRule = None,
        region_id: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        self.description = description
        self.entity_group_id = entity_group_id
        self.entity_group_name = entity_group_name
        self.entity_queries = entity_queries
        self.entity_rules = entity_rules
        self.region_id = region_id
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.entity_queries:
            for k in self.entity_queries:
                if k:
                    k.validate()
        if self.entity_rules:
            self.entity_rules.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.entity_group_id is not None:
            result['entityGroupId'] = self.entity_group_id
        if self.entity_group_name is not None:
            result['entityGroupName'] = self.entity_group_name
        result['entityQueries'] = []
        if self.entity_queries is not None:
            for k in self.entity_queries:
                result['entityQueries'].append(k.to_map() if k else None)
        if self.entity_rules is not None:
            result['entityRules'] = self.entity_rules.to_map()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('entityGroupId') is not None:
            self.entity_group_id = m.get('entityGroupId')
        if m.get('entityGroupName') is not None:
            self.entity_group_name = m.get('entityGroupName')
        self.entity_queries = []
        if m.get('entityQueries') is not None:
            for k in m.get('entityQueries'):
                temp_model = EntityGroupBaseEntityQueries()
                self.entity_queries.append(temp_model.from_map(k))
        if m.get('entityRules') is not None:
            temp_model = EntityDiscoverRule()
            self.entity_rules = temp_model.from_map(m['entityRules'])
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class IncidentContactStruct(TeaModel):
    def __init__(
        self,
        channel: List[str] = None,
        contact_id: str = None,
        contact_type: str = None,
    ):
        self.channel = channel
        self.contact_id = contact_id
        self.contact_type = contact_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.contact_id is not None:
            result['contactId'] = self.contact_id
        if self.contact_type is not None:
            result['contactType'] = self.contact_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')
        if m.get('contactType') is not None:
            self.contact_type = m.get('contactType')
        return self


class IncidentEscalationStageStruct(TeaModel):
    def __init__(
        self,
        contact: List[IncidentContactStruct] = None,
        cycle_notify_count: int = None,
        cycle_notify_time: int = None,
        description: str = None,
        effect_time: str = None,
        name: str = None,
        stage_index: int = None,
        time_zone: str = None,
        wait_to_next_stage_time: int = None,
    ):
        self.contact = contact
        self.cycle_notify_count = cycle_notify_count
        self.cycle_notify_time = cycle_notify_time
        self.description = description
        self.effect_time = effect_time
        self.name = name
        self.stage_index = stage_index
        self.time_zone = time_zone
        self.wait_to_next_stage_time = wait_to_next_stage_time

    def validate(self):
        if self.contact:
            for k in self.contact:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['contact'] = []
        if self.contact is not None:
            for k in self.contact:
                result['contact'].append(k.to_map() if k else None)
        if self.cycle_notify_count is not None:
            result['cycleNotifyCount'] = self.cycle_notify_count
        if self.cycle_notify_time is not None:
            result['cycleNotifyTime'] = self.cycle_notify_time
        if self.description is not None:
            result['description'] = self.description
        if self.effect_time is not None:
            result['effectTime'] = self.effect_time
        if self.name is not None:
            result['name'] = self.name
        if self.stage_index is not None:
            result['stageIndex'] = self.stage_index
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.wait_to_next_stage_time is not None:
            result['waitToNextStageTime'] = self.wait_to_next_stage_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.contact = []
        if m.get('contact') is not None:
            for k in m.get('contact'):
                temp_model = IncidentContactStruct()
                self.contact.append(temp_model.from_map(k))
        if m.get('cycleNotifyCount') is not None:
            self.cycle_notify_count = m.get('cycleNotifyCount')
        if m.get('cycleNotifyTime') is not None:
            self.cycle_notify_time = m.get('cycleNotifyTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('effectTime') is not None:
            self.effect_time = m.get('effectTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('stageIndex') is not None:
            self.stage_index = m.get('stageIndex')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('waitToNextStageTime') is not None:
            self.wait_to_next_stage_time = m.get('waitToNextStageTime')
        return self


class IncidentEscalationStruct(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        description: str = None,
        incident_escalation_id: str = None,
        modify_time: int = None,
        name: str = None,
        region_id: str = None,
        stage: List[IncidentEscalationStageStruct] = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.incident_escalation_id = incident_escalation_id
        self.modify_time = modify_time
        self.name = name
        self.region_id = region_id
        self.stage = stage
        self.workspace = workspace

    def validate(self):
        if self.stage:
            for k in self.stage:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.incident_escalation_id is not None:
            result['incidentEscalationId'] = self.incident_escalation_id
        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time
        if self.name is not None:
            result['name'] = self.name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        result['stage'] = []
        if self.stage is not None:
            for k in self.stage:
                result['stage'].append(k.to_map() if k else None)
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('incidentEscalationId') is not None:
            self.incident_escalation_id = m.get('incidentEscalationId')
        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        self.stage = []
        if m.get('stage') is not None:
            for k in m.get('stage'):
                temp_model = IncidentEscalationStageStruct()
                self.stage.append(temp_model.from_map(k))
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class IncidentEventStruct(TeaModel):
    def __init__(
        self,
        auto_recover_time: int = None,
        content: str = None,
        count: int = None,
        dimension: Dict[str, str] = None,
        group_by: Dict[str, str] = None,
        incident_event_id: str = None,
        incident_id: str = None,
        last_time: int = None,
        recover_time: int = None,
        resource: Dict[str, str] = None,
        status: int = None,
        time: str = None,
        title: str = None,
        user_id: str = None,
    ):
        self.auto_recover_time = auto_recover_time
        self.content = content
        self.count = count
        self.dimension = dimension
        self.group_by = group_by
        self.incident_event_id = incident_event_id
        self.incident_id = incident_id
        self.last_time = last_time
        self.recover_time = recover_time
        self.resource = resource
        self.status = status
        self.time = time
        self.title = title
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_recover_time is not None:
            result['autoRecoverTime'] = self.auto_recover_time
        if self.content is not None:
            result['content'] = self.content
        if self.count is not None:
            result['count'] = self.count
        if self.dimension is not None:
            result['dimension'] = self.dimension
        if self.group_by is not None:
            result['groupBy'] = self.group_by
        if self.incident_event_id is not None:
            result['incidentEventId'] = self.incident_event_id
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.last_time is not None:
            result['lastTime'] = self.last_time
        if self.recover_time is not None:
            result['recoverTime'] = self.recover_time
        if self.resource is not None:
            result['resource'] = self.resource
        if self.status is not None:
            result['status'] = self.status
        if self.time is not None:
            result['time'] = self.time
        if self.title is not None:
            result['title'] = self.title
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRecoverTime') is not None:
            self.auto_recover_time = m.get('autoRecoverTime')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')
        if m.get('groupBy') is not None:
            self.group_by = m.get('groupBy')
        if m.get('incidentEventId') is not None:
            self.incident_event_id = m.get('incidentEventId')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('lastTime') is not None:
            self.last_time = m.get('lastTime')
        if m.get('recoverTime') is not None:
            self.recover_time = m.get('recoverTime')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class IncidentMemberStructAcknowledge(TeaModel):
    def __init__(
        self,
        break_level: str = None,
        verify_time: int = None,
    ):
        self.break_level = break_level
        self.verify_time = verify_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.break_level is not None:
            result['breakLevel'] = self.break_level
        if self.verify_time is not None:
            result['verifyTime'] = self.verify_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('breakLevel') is not None:
            self.break_level = m.get('breakLevel')
        if m.get('verifyTime') is not None:
            self.verify_time = m.get('verifyTime')
        return self


class IncidentMemberStructContacts(TeaModel):
    def __init__(
        self,
        channel: str = None,
        contact_mask: str = None,
    ):
        self.channel = channel
        self.contact_mask = contact_mask

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.contact_mask is not None:
            result['contactMask'] = self.contact_mask
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('contactMask') is not None:
            self.contact_mask = m.get('contactMask')
        return self


class IncidentMemberStructEscalation(TeaModel):
    def __init__(
        self,
        description: str = None,
        incident_escalation_id: str = None,
        name: str = None,
        stage_index: str = None,
        title: str = None,
    ):
        self.description = description
        self.incident_escalation_id = incident_escalation_id
        self.name = name
        self.stage_index = stage_index
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.incident_escalation_id is not None:
            result['incidentEscalationId'] = self.incident_escalation_id
        if self.name is not None:
            result['name'] = self.name
        if self.stage_index is not None:
            result['stageIndex'] = self.stage_index
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('incidentEscalationId') is not None:
            self.incident_escalation_id = m.get('incidentEscalationId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('stageIndex') is not None:
            self.stage_index = m.get('stageIndex')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class IncidentMemberStructScheduleGroup(TeaModel):
    def __init__(
        self,
        contact_id: str = None,
        name: str = None,
    ):
        self.contact_id = contact_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact_id is not None:
            result['contactId'] = self.contact_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class IncidentMemberStruct(TeaModel):
    def __init__(
        self,
        acknowledge: IncidentMemberStructAcknowledge = None,
        contact_id: str = None,
        contacts: List[IncidentMemberStructContacts] = None,
        escalation: IncidentMemberStructEscalation = None,
        incident_id: str = None,
        incident_member_id: str = None,
        schedule_group: IncidentMemberStructScheduleGroup = None,
        time: int = None,
        user_id: int = None,
    ):
        self.acknowledge = acknowledge
        self.contact_id = contact_id
        self.contacts = contacts
        self.escalation = escalation
        self.incident_id = incident_id
        self.incident_member_id = incident_member_id
        self.schedule_group = schedule_group
        self.time = time
        self.user_id = user_id

    def validate(self):
        if self.acknowledge:
            self.acknowledge.validate()
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()
        if self.escalation:
            self.escalation.validate()
        if self.schedule_group:
            self.schedule_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acknowledge is not None:
            result['acknowledge'] = self.acknowledge.to_map()
        if self.contact_id is not None:
            result['contactId'] = self.contact_id
        result['contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['contacts'].append(k.to_map() if k else None)
        if self.escalation is not None:
            result['escalation'] = self.escalation.to_map()
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_member_id is not None:
            result['incidentMemberId'] = self.incident_member_id
        if self.schedule_group is not None:
            result['scheduleGroup'] = self.schedule_group.to_map()
        if self.time is not None:
            result['time'] = self.time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acknowledge') is not None:
            temp_model = IncidentMemberStructAcknowledge()
            self.acknowledge = temp_model.from_map(m['acknowledge'])
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')
        self.contacts = []
        if m.get('contacts') is not None:
            for k in m.get('contacts'):
                temp_model = IncidentMemberStructContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('escalation') is not None:
            temp_model = IncidentMemberStructEscalation()
            self.escalation = temp_model.from_map(m['escalation'])
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentMemberId') is not None:
            self.incident_member_id = m.get('incidentMemberId')
        if m.get('scheduleGroup') is not None:
            temp_model = IncidentMemberStructScheduleGroup()
            self.schedule_group = temp_model.from_map(m['scheduleGroup'])
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class IncidentNoteStructOperator(TeaModel):
    def __init__(
        self,
        contact: str = None,
        contact_id: str = None,
        name: str = None,
        user_id: int = None,
    ):
        self.contact = contact
        self.contact_id = contact_id
        self.name = name
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contact is not None:
            result['contact'] = self.contact
        if self.contact_id is not None:
            result['contactId'] = self.contact_id
        if self.name is not None:
            result['name'] = self.name
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contact') is not None:
            self.contact = m.get('contact')
        if m.get('contactId') is not None:
            self.contact_id = m.get('contactId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class IncidentNoteStruct(TeaModel):
    def __init__(
        self,
        content: str = None,
        format: str = None,
        incident_id: str = None,
        note_id: str = None,
        operator: IncidentNoteStructOperator = None,
        time: int = None,
        type: str = None,
    ):
        self.content = content
        self.format = format
        self.incident_id = incident_id
        self.note_id = note_id
        self.operator = operator
        self.time = time
        self.type = type

    def validate(self):
        if self.operator:
            self.operator.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.format is not None:
            result['format'] = self.format
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.note_id is not None:
            result['noteId'] = self.note_id
        if self.operator is not None:
            result['operator'] = self.operator.to_map()
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('noteId') is not None:
            self.note_id = m.get('noteId')
        if m.get('operator') is not None:
            temp_model = IncidentNoteStructOperator()
            self.operator = temp_model.from_map(m['operator'])
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class IncidentPlanCorporationStruct(TeaModel):
    def __init__(
        self,
        channel: str = None,
        robot_id: str = None,
    ):
        self.channel = channel
        self.robot_id = robot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.robot_id is not None:
            result['robotId'] = self.robot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('robotId') is not None:
            self.robot_id = m.get('robotId')
        return self


class IncidentPlanFieldPath(TeaModel):
    def __init__(
        self,
        field_alias: str = None,
        field_path: List[str] = None,
    ):
        self.field_alias = field_alias
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field_alias is not None:
            result['fieldAlias'] = self.field_alias
        if self.field_path is not None:
            result['fieldPath'] = self.field_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldAlias') is not None:
            self.field_alias = m.get('fieldAlias')
        if m.get('fieldPath') is not None:
            self.field_path = m.get('fieldPath')
        return self


class IncidentPlanStruct(TeaModel):
    def __init__(
        self,
        auto_recover_seconds: int = None,
        close_expire: int = None,
        corporation: List[IncidentPlanCorporationStruct] = None,
        description: str = None,
        escalation_id: List[str] = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        group_by: List[IncidentPlanFieldPath] = None,
        incident_plan_id: str = None,
        name: str = None,
        resource_filed: List[IncidentPlanFieldPath] = None,
        status: str = None,
        user_id: int = None,
        workspace: str = None,
    ):
        self.auto_recover_seconds = auto_recover_seconds
        self.close_expire = close_expire
        self.corporation = corporation
        self.description = description
        self.escalation_id = escalation_id
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_by = group_by
        self.incident_plan_id = incident_plan_id
        self.name = name
        self.resource_filed = resource_filed
        self.status = status
        self.user_id = user_id
        self.workspace = workspace

    def validate(self):
        if self.corporation:
            for k in self.corporation:
                if k:
                    k.validate()
        if self.group_by:
            for k in self.group_by:
                if k:
                    k.validate()
        if self.resource_filed:
            for k in self.resource_filed:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_recover_seconds is not None:
            result['autoRecoverSeconds'] = self.auto_recover_seconds
        if self.close_expire is not None:
            result['closeExpire'] = self.close_expire
        result['corporation'] = []
        if self.corporation is not None:
            for k in self.corporation:
                result['corporation'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.escalation_id is not None:
            result['escalationId'] = self.escalation_id
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        result['groupBy'] = []
        if self.group_by is not None:
            for k in self.group_by:
                result['groupBy'].append(k.to_map() if k else None)
        if self.incident_plan_id is not None:
            result['incidentPlanId'] = self.incident_plan_id
        if self.name is not None:
            result['name'] = self.name
        result['resourceFiled'] = []
        if self.resource_filed is not None:
            for k in self.resource_filed:
                result['resourceFiled'].append(k.to_map() if k else None)
        if self.status is not None:
            result['status'] = self.status
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoRecoverSeconds') is not None:
            self.auto_recover_seconds = m.get('autoRecoverSeconds')
        if m.get('closeExpire') is not None:
            self.close_expire = m.get('closeExpire')
        self.corporation = []
        if m.get('corporation') is not None:
            for k in m.get('corporation'):
                temp_model = IncidentPlanCorporationStruct()
                self.corporation.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('escalationId') is not None:
            self.escalation_id = m.get('escalationId')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        self.group_by = []
        if m.get('groupBy') is not None:
            for k in m.get('groupBy'):
                temp_model = IncidentPlanFieldPath()
                self.group_by.append(temp_model.from_map(k))
        if m.get('incidentPlanId') is not None:
            self.incident_plan_id = m.get('incidentPlanId')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.resource_filed = []
        if m.get('resourceFiled') is not None:
            for k in m.get('resourceFiled'):
                temp_model = IncidentPlanFieldPath()
                self.resource_filed.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class IncidentResourceDetail(TeaModel):
    def __init__(
        self,
        extra_id: str = None,
        resource_id: Dict[str, Any] = None,
        type: str = None,
    ):
        self.extra_id = extra_id
        self.resource_id = resource_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra_id is not None:
            result['extraId'] = self.extra_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extraId') is not None:
            self.extra_id = m.get('extraId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class IncidentResourceStruct(TeaModel):
    def __init__(
        self,
        description: str = None,
        incident_id: str = None,
        incident_resource_id: str = None,
        resource: IncidentResourceDetail = None,
        source: str = None,
        time: int = None,
        user_id: int = None,
    ):
        self.description = description
        self.incident_id = incident_id
        self.incident_resource_id = incident_resource_id
        self.resource = resource
        self.source = source
        self.time = time
        self.user_id = user_id

    def validate(self):
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_resource_id is not None:
            result['incidentResourceId'] = self.incident_resource_id
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.source is not None:
            result['source'] = self.source
        if self.time is not None:
            result['time'] = self.time
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentResourceId') is not None:
            self.incident_resource_id = m.get('incidentResourceId')
        if m.get('resource') is not None:
            temp_model = IncidentResourceDetail()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class IncidentStruct(TeaModel):
    def __init__(
        self,
        content: str = None,
        escalations: List[IncidentEscalationStruct] = None,
        incident_id: str = None,
        incident_plan: IncidentPlanStruct = None,
        resource: IncidentResourceDetail = None,
        severity: str = None,
        status: str = None,
        time: int = None,
        title: str = None,
        user_id: str = None,
    ):
        self.content = content
        self.escalations = escalations
        self.incident_id = incident_id
        self.incident_plan = incident_plan
        self.resource = resource
        self.severity = severity
        self.status = status
        self.time = time
        self.title = title
        self.user_id = user_id

    def validate(self):
        if self.escalations:
            for k in self.escalations:
                if k:
                    k.validate()
        if self.incident_plan:
            self.incident_plan.validate()
        if self.resource:
            self.resource.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        result['escalations'] = []
        if self.escalations is not None:
            for k in self.escalations:
                result['escalations'].append(k.to_map() if k else None)
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_plan is not None:
            result['incidentPlan'] = self.incident_plan.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.severity is not None:
            result['severity'] = self.severity
        if self.status is not None:
            result['status'] = self.status
        if self.time is not None:
            result['time'] = self.time
        if self.title is not None:
            result['title'] = self.title
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        self.escalations = []
        if m.get('escalations') is not None:
            for k in m.get('escalations'):
                temp_model = IncidentEscalationStruct()
                self.escalations.append(temp_model.from_map(k))
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentPlan') is not None:
            temp_model = IncidentPlanStruct()
            self.incident_plan = temp_model.from_map(m['incidentPlan'])
        if m.get('resource') is not None:
            temp_model = IncidentResourceDetail()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class IncidentTimeline(TeaModel):
    def __init__(
        self,
        child_type: str = None,
        content: str = None,
        incident_id: str = None,
        incident_timeline_id: str = None,
        time: int = None,
        timeline_id: str = None,
        title: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.child_type = child_type
        self.content = content
        self.incident_id = incident_id
        self.incident_timeline_id = incident_timeline_id
        self.time = time
        self.timeline_id = timeline_id
        self.title = title
        self.type = type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.child_type is not None:
            result['childType'] = self.child_type
        if self.content is not None:
            result['content'] = self.content
        if self.incident_id is not None:
            result['incidentId'] = self.incident_id
        if self.incident_timeline_id is not None:
            result['incidentTimelineId'] = self.incident_timeline_id
        if self.time is not None:
            result['time'] = self.time
        if self.timeline_id is not None:
            result['timelineId'] = self.timeline_id
        if self.title is not None:
            result['title'] = self.title
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('childType') is not None:
            self.child_type = m.get('childType')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('incidentId') is not None:
            self.incident_id = m.get('incidentId')
        if m.get('incidentTimelineId') is not None:
            self.incident_timeline_id = m.get('incidentTimelineId')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('timelineId') is not None:
            self.timeline_id = m.get('timelineId')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class MaintainWindowForModifyEffectTimeRange(TeaModel):
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


class MaintainWindowForModify(TeaModel):
    def __init__(
        self,
        description: str = None,
        effect_time_range: MaintainWindowForModifyEffectTimeRange = None,
        effective: str = None,
        end_time: str = None,
        filter_setting: FilterSetting = None,
        maintain_window_name: str = None,
        start_time: str = None,
    ):
        self.description = description
        self.effect_time_range = effect_time_range
        self.effective = effective
        self.end_time = end_time
        self.filter_setting = filter_setting
        # This parameter is required.
        self.maintain_window_name = maintain_window_name
        self.start_time = start_time

    def validate(self):
        if self.effect_time_range:
            self.effect_time_range.validate()
        if self.filter_setting:
            self.filter_setting.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.effect_time_range is not None:
            result['effectTimeRange'] = self.effect_time_range.to_map()
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
        if m.get('effectTimeRange') is not None:
            temp_model = MaintainWindowForModifyEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m['effectTimeRange'])
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


class MaintainWindowForViewEffectTimeRange(TeaModel):
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


class MaintainWindowForView(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        effect_time_range: MaintainWindowForViewEffectTimeRange = None,
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
        self.effect_time_range = effect_time_range
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
        if self.effect_time_range:
            self.effect_time_range.validate()
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
        if self.effect_time_range is not None:
            result['effectTimeRange'] = self.effect_time_range.to_map()
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
        if m.get('effectTimeRange') is not None:
            temp_model = MaintainWindowForViewEffectTimeRange()
            self.effect_time_range = temp_model.from_map(m['effectTimeRange'])
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


class MergeContact(TeaModel):
    def __init__(
        self,
        email: str = None,
        email_verify: bool = None,
        extend: Dict[str, Any] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        identifier: str = None,
        lang: str = None,
        name: str = None,
        phone: str = None,
        phone_code: str = None,
        phone_verify: bool = None,
        source: str = None,
    ):
        self.email = email
        self.email_verify = email_verify
        self.extend = extend
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.identifier = identifier
        self.lang = lang
        self.name = name
        self.phone = phone
        self.phone_code = phone_code
        self.phone_verify = phone_verify
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.email_verify is not None:
            result['emailVerify'] = self.email_verify
        if self.extend is not None:
            result['extend'] = self.extend
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.lang is not None:
            result['lang'] = self.lang
        if self.name is not None:
            result['name'] = self.name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.phone_code is not None:
            result['phoneCode'] = self.phone_code
        if self.phone_verify is not None:
            result['phoneVerify'] = self.phone_verify
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('emailVerify') is not None:
            self.email_verify = m.get('emailVerify')
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('phoneCode') is not None:
            self.phone_code = m.get('phoneCode')
        if m.get('phoneVerify') is not None:
            self.phone_verify = m.get('phoneVerify')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class MergeContactGroup(TeaModel):
    def __init__(
        self,
        contacts: List[str] = None,
        extend: Dict[str, Any] = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        identifier: str = None,
        name: str = None,
        source: str = None,
    ):
        self.contacts = contacts
        self.extend = extend
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.identifier = identifier
        self.name = name
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contacts is not None:
            result['contacts'] = self.contacts
        if self.extend is not None:
            result['extend'] = self.extend
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contacts') is not None:
            self.contacts = m.get('contacts')
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class MergeRobotExtend(TeaModel):
    def __init__(
        self,
        card_template: str = None,
        daily_noc: bool = None,
        daily_noc_time: str = None,
        ding_sign_key: str = None,
        enable_outgoing: bool = None,
        token: str = None,
    ):
        self.card_template = card_template
        self.daily_noc = daily_noc
        self.daily_noc_time = daily_noc_time
        self.ding_sign_key = ding_sign_key
        self.enable_outgoing = enable_outgoing
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_template is not None:
            result['cardTemplate'] = self.card_template
        if self.daily_noc is not None:
            result['dailyNoc'] = self.daily_noc
        if self.daily_noc_time is not None:
            result['dailyNocTime'] = self.daily_noc_time
        if self.ding_sign_key is not None:
            result['dingSignKey'] = self.ding_sign_key
        if self.enable_outgoing is not None:
            result['enableOutgoing'] = self.enable_outgoing
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardTemplate') is not None:
            self.card_template = m.get('cardTemplate')
        if m.get('dailyNoc') is not None:
            self.daily_noc = m.get('dailyNoc')
        if m.get('dailyNocTime') is not None:
            self.daily_noc_time = m.get('dailyNocTime')
        if m.get('dingSignKey') is not None:
            self.ding_sign_key = m.get('dingSignKey')
        if m.get('enableOutgoing') is not None:
            self.enable_outgoing = m.get('enableOutgoing')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class MergeRobot(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        extend: MergeRobotExtend = None,
        gmt_modified: str = None,
        identifier: str = None,
        lang: str = None,
        name: str = None,
        source: str = None,
        type: str = None,
        webhook: str = None,
    ):
        self.create_time = create_time
        self.extend = extend
        self.gmt_modified = gmt_modified
        self.identifier = identifier
        self.lang = lang
        self.name = name
        self.source = source
        self.type = type
        self.webhook = webhook

    def validate(self):
        if self.extend:
            self.extend.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.extend is not None:
            result['extend'] = self.extend.to_map()
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.lang is not None:
            result['lang'] = self.lang
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.type is not None:
            result['type'] = self.type
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('extend') is not None:
            temp_model = MergeRobotExtend()
            self.extend = temp_model.from_map(m['extend'])
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
        return self


class MergeWebhook(TeaModel):
    def __init__(
        self,
        content_type: str = None,
        extend: str = None,
        gmt_create: str = None,
        gmt_modified: Dict[str, Any] = None,
        headers: str = None,
        identifier: str = None,
        lang: str = None,
        method: str = None,
        name: str = None,
        source: str = None,
        type: str = None,
        webhook: str = None,
    ):
        self.content_type = content_type
        self.extend = extend
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.headers = headers
        self.identifier = identifier
        self.lang = lang
        self.method = method
        self.name = name
        self.source = source
        self.type = type
        self.webhook = webhook

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_type is not None:
            result['contentType'] = self.content_type
        if self.extend is not None:
            result['extend'] = self.extend
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified
        if self.headers is not None:
            result['headers'] = self.headers
        if self.identifier is not None:
            result['identifier'] = self.identifier
        if self.lang is not None:
            result['lang'] = self.lang
        if self.method is not None:
            result['method'] = self.method
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.type is not None:
            result['type'] = self.type
        if self.webhook is not None:
            result['webhook'] = self.webhook
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contentType') is not None:
            self.content_type = m.get('contentType')
        if m.get('extend') is not None:
            self.extend = m.get('extend')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('identifier') is not None:
            self.identifier = m.get('identifier')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('webhook') is not None:
            self.webhook = m.get('webhook')
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


class PrometheusManagedInstance(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        instance_type: str = None,
        prometheus_instance_id: str = None,
        prometheus_instance_name: str = None,
        region_id: str = None,
        status: str = None,
        workspace: str = None,
    ):
        self.create_time = create_time
        self.instance_type = instance_type
        self.prometheus_instance_id = prometheus_instance_id
        self.prometheus_instance_name = prometheus_instance_name
        self.region_id = region_id
        self.status = status
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.prometheus_instance_id is not None:
            result['prometheusInstanceId'] = self.prometheus_instance_id
        if self.prometheus_instance_name is not None:
            result['prometheusInstanceName'] = self.prometheus_instance_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.status is not None:
            result['status'] = self.status
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('prometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('prometheusInstanceId')
        if m.get('prometheusInstanceName') is not None:
            self.prometheus_instance_name = m.get('prometheusInstanceName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class RumDnsResponse(TeaModel):
    def __init__(
        self,
        domain: str = None,
        message: str = None,
        result: bool = None,
    ):
        self.domain = domain
        self.message = message
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.message is not None:
            result['message'] = self.message
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('result') is not None:
            self.result = m.get('result')
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


class CreateEntityStoreResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        workspace_name: str = None,
    ):
        self.request_id = request_id
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        return self


class CreateEntityStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEntityStoreResponseBody = None,
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
            temp_model = CreateEntityStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePrometheusInstanceRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreatePrometheusInstanceRequest(TeaModel):
    def __init__(
        self,
        archive_duration: int = None,
        auth_free_read_policy: str = None,
        auth_free_write_policy: str = None,
        enable_auth_free_read: bool = None,
        enable_auth_free_write: bool = None,
        enable_auth_token: bool = None,
        payment_type: str = None,
        prometheus_instance_name: str = None,
        status: str = None,
        storage_duration: int = None,
        tags: List[CreatePrometheusInstanceRequestTags] = None,
        workspace: str = None,
    ):
        self.archive_duration = archive_duration
        self.auth_free_read_policy = auth_free_read_policy
        self.auth_free_write_policy = auth_free_write_policy
        self.enable_auth_free_read = enable_auth_free_read
        self.enable_auth_free_write = enable_auth_free_write
        self.enable_auth_token = enable_auth_token
        self.payment_type = payment_type
        # This parameter is required.
        self.prometheus_instance_name = prometheus_instance_name
        self.status = status
        self.storage_duration = storage_duration
        self.tags = tags
        self.workspace = workspace

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.archive_duration is not None:
            result['archiveDuration'] = self.archive_duration
        if self.auth_free_read_policy is not None:
            result['authFreeReadPolicy'] = self.auth_free_read_policy
        if self.auth_free_write_policy is not None:
            result['authFreeWritePolicy'] = self.auth_free_write_policy
        if self.enable_auth_free_read is not None:
            result['enableAuthFreeRead'] = self.enable_auth_free_read
        if self.enable_auth_free_write is not None:
            result['enableAuthFreeWrite'] = self.enable_auth_free_write
        if self.enable_auth_token is not None:
            result['enableAuthToken'] = self.enable_auth_token
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.prometheus_instance_name is not None:
            result['prometheusInstanceName'] = self.prometheus_instance_name
        if self.status is not None:
            result['status'] = self.status
        if self.storage_duration is not None:
            result['storageDuration'] = self.storage_duration
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('archiveDuration') is not None:
            self.archive_duration = m.get('archiveDuration')
        if m.get('authFreeReadPolicy') is not None:
            self.auth_free_read_policy = m.get('authFreeReadPolicy')
        if m.get('authFreeWritePolicy') is not None:
            self.auth_free_write_policy = m.get('authFreeWritePolicy')
        if m.get('enableAuthFreeRead') is not None:
            self.enable_auth_free_read = m.get('enableAuthFreeRead')
        if m.get('enableAuthFreeWrite') is not None:
            self.enable_auth_free_write = m.get('enableAuthFreeWrite')
        if m.get('enableAuthToken') is not None:
            self.enable_auth_token = m.get('enableAuthToken')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('prometheusInstanceName') is not None:
            self.prometheus_instance_name = m.get('prometheusInstanceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('storageDuration') is not None:
            self.storage_duration = m.get('storageDuration')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = CreatePrometheusInstanceRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreatePrometheusInstanceResponseBody(TeaModel):
    def __init__(
        self,
        prometheus_instance_id: str = None,
        request_id: str = None,
    ):
        self.prometheus_instance_id = prometheus_instance_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prometheus_instance_id is not None:
            result['prometheusInstanceId'] = self.prometheus_instance_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('prometheusInstanceId') is not None:
            self.prometheus_instance_id = m.get('prometheusInstanceId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreatePrometheusInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePrometheusInstanceResponseBody = None,
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
            temp_model = CreatePrometheusInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateServiceRequest(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        description: str = None,
        display_name: str = None,
        pid: str = None,
        service_name: str = None,
        service_status: str = None,
        service_type: str = None,
    ):
        self.attributes = attributes
        self.description = description
        self.display_name = display_name
        self.pid = pid
        # This parameter is required.
        self.service_name = service_name
        self.service_status = service_status
        # This parameter is required.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['attributes'] = self.attributes
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.pid is not None:
            result['pid'] = self.pid
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class CreateServiceResponseBody(TeaModel):
    def __init__(
        self,
        pid: str = None,
        request_id: str = None,
        service_id: str = None,
    ):
        self.pid = pid
        self.request_id = request_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.pid is not None:
            result['pid'] = self.pid
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        return self


class CreateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateServiceResponseBody = None,
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
            temp_model = CreateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTicketRequest(TeaModel):
    def __init__(
        self,
        access_token_expiration_time: int = None,
        expiration_time: int = None,
    ):
        self.access_token_expiration_time = access_token_expiration_time
        self.expiration_time = expiration_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token_expiration_time is not None:
            result['accessTokenExpirationTime'] = self.access_token_expiration_time
        if self.expiration_time is not None:
            result['expirationTime'] = self.expiration_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessTokenExpirationTime') is not None:
            self.access_token_expiration_time = m.get('accessTokenExpirationTime')
        if m.get('expirationTime') is not None:
            self.expiration_time = m.get('expirationTime')
        return self


class CreateTicketResponseBody(TeaModel):
    def __init__(
        self,
        ticket: str = None,
    ):
        self.ticket = ticket

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ticket is not None:
            result['ticket'] = self.ticket
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ticket') is not None:
            self.ticket = m.get('ticket')
        return self


class CreateTicketResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTicketResponseBody = None,
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
            temp_model = CreateTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUmodelRequestCommonSchemaRef(TeaModel):
    def __init__(
        self,
        group: str = None,
        items: List[str] = None,
        version: str = None,
    ):
        self.group = group
        self.items = items
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.items is not None:
            result['items'] = self.items
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('items') is not None:
            self.items = m.get('items')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class CreateUmodelRequest(TeaModel):
    def __init__(
        self,
        common_schema_ref: List[CreateUmodelRequestCommonSchemaRef] = None,
        description: str = None,
    ):
        self.common_schema_ref = common_schema_ref
        self.description = description

    def validate(self):
        if self.common_schema_ref:
            for k in self.common_schema_ref:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['commonSchemaRef'] = []
        if self.common_schema_ref is not None:
            for k in self.common_schema_ref:
                result['commonSchemaRef'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_schema_ref = []
        if m.get('commonSchemaRef') is not None:
            for k in m.get('commonSchemaRef'):
                temp_model = CreateUmodelRequestCommonSchemaRef()
                self.common_schema_ref.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class CreateUmodelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        workspace: str = None,
    ):
        self.request_id = request_id
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class CreateUmodelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUmodelResponseBody = None,
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
            temp_model = CreateUmodelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEntityStoreResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteEntityStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEntityStoreResponseBody = None,
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
            temp_model = DeleteEntityStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteServiceResponseBody = None,
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
            temp_model = DeleteServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUmodelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteUmodelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUmodelResponseBody = None,
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
            temp_model = DeleteUmodelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUmodelDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        kind: str = None,
        name: str = None,
    ):
        self.domain = domain
        self.kind = kind
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DeleteUmodelDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteUmodelDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteUmodelDataResponseBody = None,
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
            temp_model = DeleteUmodelDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkspaceResponseBody = None,
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
            temp_model = DeleteWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEntityStoreResponseBody(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        request_id: str = None,
        workspace_name: str = None,
    ):
        self.region_id = region_id
        self.request_id = request_id
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        return self


class GetEntityStoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEntityStoreResponseBody = None,
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
            temp_model = GetEntityStoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetEntityStoreDataHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        accept_encoding: str = None,
    ):
        self.common_headers = common_headers
        self.accept_encoding = accept_encoding

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.accept_encoding is not None:
            result['acceptEncoding'] = self.accept_encoding
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('acceptEncoding') is not None:
            self.accept_encoding = m.get('acceptEncoding')
        return self


class GetEntityStoreDataRequest(TeaModel):
    def __init__(
        self,
        from_: int = None,
        query: str = None,
        to: int = None,
    ):
        # This parameter is required.
        self.from_ = from_
        # This parameter is required.
        self.query = query
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.query is not None:
            result['query'] = self.query
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self


class GetEntityStoreDataResponseBody(TeaModel):
    def __init__(
        self,
        data: List[List[str]] = None,
        header: List[str] = None,
        request_id: str = None,
    ):
        self.data = data
        self.header = header
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.header is not None:
            result['header'] = self.header
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('header') is not None:
            self.header = m.get('header')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetEntityStoreDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetEntityStoreDataResponseBody = None,
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
            temp_model = GetEntityStoreDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceResponseBodyService(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        pid: str = None,
        region_id: str = None,
        service_id: str = None,
        service_name: str = None,
        service_status: str = None,
        service_type: str = None,
        workspace: str = None,
    ):
        self.attributes = attributes
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.pid = pid
        self.region_id = region_id
        self.service_id = service_id
        self.service_name = service_name
        self.service_status = service_status
        self.service_type = service_type
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['attributes'] = self.attributes
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.pid is not None:
            result['pid'] = self.pid
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service: GetServiceResponseBodyService = None,
    ):
        self.request_id = request_id
        self.service = service

    def validate(self):
        if self.service:
            self.service.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.service is not None:
            result['service'] = self.service.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('service') is not None:
            temp_model = GetServiceResponseBodyService()
            self.service = temp_model.from_map(m['service'])
        return self


class GetServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceResponseBody = None,
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
            temp_model = GetServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetServiceObservabilityResponseBodyEntryPointInfo(TeaModel):
    def __init__(
        self,
        auth_token: str = None,
        private_domain: str = None,
        project: str = None,
        public_domain: str = None,
    ):
        self.auth_token = auth_token
        self.private_domain = private_domain
        # SLS Project
        self.project = project
        self.public_domain = public_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_token is not None:
            result['authToken'] = self.auth_token
        if self.private_domain is not None:
            result['privateDomain'] = self.private_domain
        if self.project is not None:
            result['project'] = self.project
        if self.public_domain is not None:
            result['publicDomain'] = self.public_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authToken') is not None:
            self.auth_token = m.get('authToken')
        if m.get('privateDomain') is not None:
            self.private_domain = m.get('privateDomain')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('publicDomain') is not None:
            self.public_domain = m.get('publicDomain')
        return self


class GetServiceObservabilityResponseBody(TeaModel):
    def __init__(
        self,
        entry_point_info: GetServiceObservabilityResponseBodyEntryPointInfo = None,
        fee_type: str = None,
        quotas: Dict[str, str] = None,
        region_id: str = None,
        request_id: str = None,
        settings: Dict[str, str] = None,
        status: str = None,
        type: str = None,
        workspace: str = None,
    ):
        self.entry_point_info = entry_point_info
        self.fee_type = fee_type
        self.quotas = quotas
        self.region_id = region_id
        self.request_id = request_id
        self.settings = settings
        self.status = status
        self.type = type
        self.workspace = workspace

    def validate(self):
        if self.entry_point_info:
            self.entry_point_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry_point_info is not None:
            result['entryPointInfo'] = self.entry_point_info.to_map()
        if self.fee_type is not None:
            result['feeType'] = self.fee_type
        if self.quotas is not None:
            result['quotas'] = self.quotas
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.settings is not None:
            result['settings'] = self.settings
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entryPointInfo') is not None:
            temp_model = GetServiceObservabilityResponseBodyEntryPointInfo()
            self.entry_point_info = temp_model.from_map(m['entryPointInfo'])
        if m.get('feeType') is not None:
            self.fee_type = m.get('feeType')
        if m.get('quotas') is not None:
            self.quotas = m.get('quotas')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('settings') is not None:
            self.settings = m.get('settings')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetServiceObservabilityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceObservabilityResponseBody = None,
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
            temp_model = GetServiceObservabilityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUmodelResponseBodyCommonSchemaRef(TeaModel):
    def __init__(
        self,
        group: str = None,
        items: List[str] = None,
        version: str = None,
    ):
        self.group = group
        self.items = items
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.items is not None:
            result['items'] = self.items
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('items') is not None:
            self.items = m.get('items')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetUmodelResponseBody(TeaModel):
    def __init__(
        self,
        common_schema_ref: List[GetUmodelResponseBodyCommonSchemaRef] = None,
        description: str = None,
        region_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        self.common_schema_ref = common_schema_ref
        self.description = description
        self.region_id = region_id
        self.request_id = request_id
        self.workspace = workspace

    def validate(self):
        if self.common_schema_ref:
            for k in self.common_schema_ref:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['commonSchemaRef'] = []
        if self.common_schema_ref is not None:
            for k in self.common_schema_ref:
                result['commonSchemaRef'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_schema_ref = []
        if m.get('commonSchemaRef') is not None:
            for k in m.get('commonSchemaRef'):
                temp_model = GetUmodelResponseBodyCommonSchemaRef()
                self.common_schema_ref.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class GetUmodelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUmodelResponseBody = None,
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
            temp_model = GetUmodelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUmodelDataRequest(TeaModel):
    def __init__(
        self,
        content: Any = None,
        method: str = None,
    ):
        self.content = content
        # This parameter is required.
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.method is not None:
            result['method'] = self.method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('method') is not None:
            self.method = m.get('method')
        return self


class GetUmodelDataResponseBodyErrors(TeaModel):
    def __init__(
        self,
        message: str = None,
        type: str = None,
    ):
        self.message = message
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetUmodelDataResponseBody(TeaModel):
    def __init__(
        self,
        errors: List[GetUmodelDataResponseBodyErrors] = None,
        links: List[Any] = None,
        nodes: List[Any] = None,
        request_id: str = None,
        total_links_count: int = None,
        total_nodes_count: int = None,
    ):
        self.errors = errors
        self.links = links
        self.nodes = nodes
        self.request_id = request_id
        self.total_links_count = total_links_count
        self.total_nodes_count = total_nodes_count

    def validate(self):
        if self.errors:
            for k in self.errors:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['errors'] = []
        if self.errors is not None:
            for k in self.errors:
                result['errors'].append(k.to_map() if k else None)
        if self.links is not None:
            result['links'] = self.links
        if self.nodes is not None:
            result['nodes'] = self.nodes
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_links_count is not None:
            result['totalLinksCount'] = self.total_links_count
        if self.total_nodes_count is not None:
            result['totalNodesCount'] = self.total_nodes_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.errors = []
        if m.get('errors') is not None:
            for k in m.get('errors'):
                temp_model = GetUmodelDataResponseBodyErrors()
                self.errors.append(temp_model.from_map(k))
        if m.get('links') is not None:
            self.links = m.get('links')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalLinksCount') is not None:
            self.total_links_count = m.get('totalLinksCount')
        if m.get('totalNodesCount') is not None:
            self.total_nodes_count = m.get('totalNodesCount')
        return self


class GetUmodelDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUmodelDataResponseBody = None,
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
            temp_model = GetUmodelDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        last_modify_time: str = None,
        region_id: str = None,
        request_id: str = None,
        sls_project: str = None,
        workspace_name: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ss.SSSZ
        self.create_time = create_time
        # 工作空间描述
        self.description = description
        self.display_name = display_name
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.last_modify_time = last_modify_time
        # 地域ID
        self.region_id = region_id
        self.request_id = request_id
        # 工作空间绑定的日志服务项目名称
        self.sls_project = sls_project
        # 工作空间名称
        # 
        # This parameter is required.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.sls_project is not None:
            result['slsProject'] = self.sls_project
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        return self


class GetWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWorkspaceResponseBody = None,
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
            temp_model = GetWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
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


class ListAlertActionsResponseBodyAlertActionsEbParam(TeaModel):
    def __init__(
        self,
        eb_source: str = None,
        event_bus_name: str = None,
        region_id: str = None,
        subject: str = None,
    ):
        self.eb_source = eb_source
        self.event_bus_name = event_bus_name
        self.region_id = region_id
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eb_source is not None:
            result['ebSource'] = self.eb_source
        if self.event_bus_name is not None:
            result['eventBusName'] = self.event_bus_name
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.subject is not None:
            result['subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ebSource') is not None:
            self.eb_source = m.get('ebSource')
        if m.get('eventBusName') is not None:
            self.event_bus_name = m.get('eventBusName')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
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


class ListAlertActionsResponseBodyAlertActionsFc3Param(TeaModel):
    def __init__(
        self,
        function: str = None,
        qualifier: str = None,
        region_id: str = None,
    ):
        self.function = function
        self.qualifier = qualifier
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function is not None:
            result['function'] = self.function
        if self.qualifier is not None:
            result['qualifier'] = self.qualifier
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function') is not None:
            self.function = m.get('function')
        if m.get('qualifier') is not None:
            self.qualifier = m.get('qualifier')
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
        eb_param: ListAlertActionsResponseBodyAlertActionsEbParam = None,
        ess_param: ListAlertActionsResponseBodyAlertActionsEssParam = None,
        fc_3param: ListAlertActionsResponseBodyAlertActionsFc3Param = None,
        fc_param: ListAlertActionsResponseBodyAlertActionsFcParam = None,
        mns_param: ListAlertActionsResponseBodyAlertActionsMnsParam = None,
        pager_duty_param: ListAlertActionsResponseBodyAlertActionsPagerDutyParam = None,
        sls_param: ListAlertActionsResponseBodyAlertActionsSlsParam = None,
        type: str = None,
        webhook_param: ListAlertActionsResponseBodyAlertActionsWebhookParam = None,
    ):
        self.alert_action_id = alert_action_id
        self.alert_action_name = alert_action_name
        self.eb_param = eb_param
        self.ess_param = ess_param
        self.fc_3param = fc_3param
        self.fc_param = fc_param
        self.mns_param = mns_param
        self.pager_duty_param = pager_duty_param
        self.sls_param = sls_param
        self.type = type
        self.webhook_param = webhook_param

    def validate(self):
        if self.eb_param:
            self.eb_param.validate()
        if self.ess_param:
            self.ess_param.validate()
        if self.fc_3param:
            self.fc_3param.validate()
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
        if self.eb_param is not None:
            result['ebParam'] = self.eb_param.to_map()
        if self.ess_param is not None:
            result['essParam'] = self.ess_param.to_map()
        if self.fc_3param is not None:
            result['fc3Param'] = self.fc_3param.to_map()
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
        if m.get('ebParam') is not None:
            temp_model = ListAlertActionsResponseBodyAlertActionsEbParam()
            self.eb_param = temp_model.from_map(m['ebParam'])
        if m.get('essParam') is not None:
            temp_model = ListAlertActionsResponseBodyAlertActionsEssParam()
            self.ess_param = temp_model.from_map(m['essParam'])
        if m.get('fc3Param') is not None:
            temp_model = ListAlertActionsResponseBodyAlertActionsFc3Param()
            self.fc_3param = temp_model.from_map(m['fc3Param'])
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


class ListServicesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        service_type: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        return self


class ListServicesResponseBodyServices(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        pid: str = None,
        service_id: str = None,
        service_name: str = None,
        service_status: str = None,
        service_type: str = None,
        workspace: str = None,
    ):
        self.attributes = attributes
        self.create_time = create_time
        self.description = description
        self.display_name = display_name
        self.pid = pid
        self.service_id = service_id
        self.service_name = service_name
        self.service_status = service_status
        self.service_type = service_type
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['attributes'] = self.attributes
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.pid is not None:
            result['pid'] = self.pid
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class ListServicesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        services: List[ListServicesResponseBodyServices] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.services = services
        self.total_count = total_count

    def validate(self):
        if self.services:
            for k in self.services:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['services'] = []
        if self.services is not None:
            for k in self.services:
                result['services'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.services = []
        if m.get('services') is not None:
            for k in m.get('services'):
                temp_model = ListServicesResponseBodyServices()
                self.services.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListServicesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListServicesResponseBody = None,
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
            temp_model = ListServicesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkspacesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        workspace_name: str = None,
        workspace_name_list: List[str] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region = region
        self.workspace_name = workspace_name
        self.workspace_name_list = workspace_name_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region is not None:
            result['region'] = self.region
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        if self.workspace_name_list is not None:
            result['workspaceNameList'] = self.workspace_name_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        if m.get('workspaceNameList') is not None:
            self.workspace_name_list = m.get('workspaceNameList')
        return self


class ListWorkspacesShrinkRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region: str = None,
        workspace_name: str = None,
        workspace_name_list_shrink: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.region = region
        self.workspace_name = workspace_name
        self.workspace_name_list_shrink = workspace_name_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.region is not None:
            result['region'] = self.region
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        if self.workspace_name_list_shrink is not None:
            result['workspaceNameList'] = self.workspace_name_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        if m.get('workspaceNameList') is not None:
            self.workspace_name_list_shrink = m.get('workspaceNameList')
        return self


class ListWorkspacesResponseBodyWorkspaces(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        display_name: str = None,
        last_modify_time: str = None,
        region_id: str = None,
        sls_project: str = None,
        workspace_name: str = None,
    ):
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        # 工作空间描述
        self.description = description
        self.display_name = display_name
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.last_modify_time = last_modify_time
        # 地域ID
        self.region_id = region_id
        # 工作空间绑定的日志服务项目名称
        self.sls_project = sls_project
        # 工作空间名称
        # 
        # This parameter is required.
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.last_modify_time is not None:
            result['lastModifyTime'] = self.last_modify_time
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.sls_project is not None:
            result['slsProject'] = self.sls_project
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('lastModifyTime') is not None:
            self.last_modify_time = m.get('lastModifyTime')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        return self


class ListWorkspacesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total: int = None,
        workspaces: List[ListWorkspacesResponseBodyWorkspaces] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total = total
        self.workspaces = workspaces

    def validate(self):
        if self.workspaces:
            for k in self.workspaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        result['workspaces'] = []
        if self.workspaces is not None:
            for k in self.workspaces:
                result['workspaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('total') is not None:
            self.total = m.get('total')
        self.workspaces = []
        if m.get('workspaces') is not None:
            for k in m.get('workspaces'):
                temp_model = ListWorkspacesResponseBodyWorkspaces()
                self.workspaces.append(temp_model.from_map(k))
        return self


class ListWorkspacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkspacesResponseBody = None,
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
            temp_model = ListWorkspacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PutWorkspaceRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        display_name: str = None,
        sls_project: str = None,
    ):
        # 工作空间描述
        self.description = description
        self.display_name = display_name
        # 工作空间绑定的日志服务项目名称
        # 
        # This parameter is required.
        self.sls_project = sls_project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.sls_project is not None:
            result['slsProject'] = self.sls_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('slsProject') is not None:
            self.sls_project = m.get('slsProject')
        return self


class PutWorkspaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        workspace_name: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        return self


class PutWorkspaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PutWorkspaceResponseBody = None,
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
            temp_model = PutWorkspaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServiceRequest(TeaModel):
    def __init__(
        self,
        attributes: str = None,
        description: str = None,
        display_name: str = None,
        service_status: str = None,
    ):
        self.attributes = attributes
        self.description = description
        self.display_name = display_name
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attributes is not None:
            result['attributes'] = self.attributes
        if self.description is not None:
            result['description'] = self.description
        if self.display_name is not None:
            result['displayName'] = self.display_name
        if self.service_status is not None:
            result['serviceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attributes') is not None:
            self.attributes = m.get('attributes')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')
        if m.get('serviceStatus') is not None:
            self.service_status = m.get('serviceStatus')
        return self


class UpdateServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_id: str = None,
    ):
        self.request_id = request_id
        self.service_id = service_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        return self


class UpdateServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateServiceResponseBody = None,
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
            temp_model = UpdateServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUmodelRequestCommonSchemaRef(TeaModel):
    def __init__(
        self,
        group: str = None,
        items: List[str] = None,
        version: str = None,
    ):
        self.group = group
        self.items = items
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group
        if self.items is not None:
            result['items'] = self.items
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')
        if m.get('items') is not None:
            self.items = m.get('items')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpdateUmodelRequest(TeaModel):
    def __init__(
        self,
        common_schema_ref: List[UpdateUmodelRequestCommonSchemaRef] = None,
        description: str = None,
    ):
        self.common_schema_ref = common_schema_ref
        self.description = description

    def validate(self):
        if self.common_schema_ref:
            for k in self.common_schema_ref:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['commonSchemaRef'] = []
        if self.common_schema_ref is not None:
            for k in self.common_schema_ref:
                result['commonSchemaRef'].append(k.to_map() if k else None)
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_schema_ref = []
        if m.get('commonSchemaRef') is not None:
            for k in m.get('commonSchemaRef'):
                temp_model = UpdateUmodelRequestCommonSchemaRef()
                self.common_schema_ref.append(temp_model.from_map(k))
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateUmodelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        workspace: str = None,
    ):
        self.request_id = request_id
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.workspace is not None:
            result['workspace'] = self.workspace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')
        return self


class UpdateUmodelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateUmodelResponseBody = None,
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
            temp_model = UpdateUmodelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpsertUmodelDataRequest(TeaModel):
    def __init__(
        self,
        elements: List[Any] = None,
        method: str = None,
    ):
        self.elements = elements
        self.method = method

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.elements is not None:
            result['elements'] = self.elements
        if self.method is not None:
            result['method'] = self.method
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('elements') is not None:
            self.elements = m.get('elements')
        if m.get('method') is not None:
            self.method = m.get('method')
        return self


class UpsertUmodelDataResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpsertUmodelDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpsertUmodelDataResponseBody = None,
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
            temp_model = UpsertUmodelDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


