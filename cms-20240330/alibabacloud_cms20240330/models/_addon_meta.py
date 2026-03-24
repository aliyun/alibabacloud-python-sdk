# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class AddonMeta(DaraModel):
    def __init__(
        self,
        alias: str = None,
        categories: List[str] = None,
        dashboards: List[main_models.AddonMetaDashboards] = None,
        description: str = None,
        environments: List[main_models.AddonMetaEnvironments] = None,
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
        # 组件别名，显示名称
        self.alias = alias
        # 组件分类信息
        self.categories = categories
        # 组件示意图列表
        self.dashboards = dashboards
        # 描述信息。
        self.description = description
        # 支持的环境类型列表
        self.environments = environments
        # 组件图标。
        self.icon = icon
        # 关键词列表
        self.keywords = keywords
        # 语言，取值：
        # 
        # - zh：中文（默认值）
        # - en：英文
        self.language = language
        # 该组件上一次接入时间
        self.latest_release_create_time = latest_release_create_time
        # 组件名称
        self.name = name
        # Policy 下是否只能安装一次
        self.once = once
        # 场景
        self.scene = scene
        # 版本号
        self.version = version
        # 组件排序权重
        self.weight = weight

    def validate(self):
        if self.dashboards:
            for v1 in self.dashboards:
                 if v1:
                    v1.validate()
        if self.environments:
            for v1 in self.environments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.categories is not None:
            result['categories'] = self.categories

        result['dashboards'] = []
        if self.dashboards is not None:
            for k1 in self.dashboards:
                result['dashboards'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        result['environments'] = []
        if self.environments is not None:
            for k1 in self.environments:
                result['environments'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('dashboards'):
                temp_model = main_models.AddonMetaDashboards()
                self.dashboards.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        self.environments = []
        if m.get('environments') is not None:
            for k1 in m.get('environments'):
                temp_model = main_models.AddonMetaEnvironments()
                self.environments.append(temp_model.from_map(k1))

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

class AddonMetaEnvironments(DaraModel):
    def __init__(
        self,
        common_schema_refs: List[main_models.AddonMetaEnvironmentsCommonSchemaRefs] = None,
        dependencies: main_models.AddonMetaEnvironmentsDependencies = None,
        description: str = None,
        enable: bool = None,
        label: str = None,
        name: str = None,
        policies: main_models.AddonMetaEnvironmentsPolicies = None,
        policy_type: str = None,
    ):
        # 绑定的CommonSchema 列表
        self.common_schema_refs = common_schema_refs
        # 依赖描述信息
        self.dependencies = dependencies
        # 环境类型的描述
        self.description = description
        # 是否启用
        self.enable = enable
        # 环境类型显示名称
        self.label = label
        # 环境类型名称
        self.name = name
        # 组件的控制策略组合信息
        self.policies = policies
        # 策略类型
        self.policy_type = policy_type

    def validate(self):
        if self.common_schema_refs:
            for v1 in self.common_schema_refs:
                 if v1:
                    v1.validate()
        if self.dependencies:
            self.dependencies.validate()
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['commonSchemaRefs'] = []
        if self.common_schema_refs is not None:
            for k1 in self.common_schema_refs:
                result['commonSchemaRefs'].append(k1.to_map() if k1 else None)

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
        self.common_schema_refs = []
        if m.get('commonSchemaRefs') is not None:
            for k1 in m.get('commonSchemaRefs'):
                temp_model = main_models.AddonMetaEnvironmentsCommonSchemaRefs()
                self.common_schema_refs.append(temp_model.from_map(k1))

        if m.get('dependencies') is not None:
            temp_model = main_models.AddonMetaEnvironmentsDependencies()
            self.dependencies = temp_model.from_map(m.get('dependencies'))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('policies') is not None:
            temp_model = main_models.AddonMetaEnvironmentsPolicies()
            self.policies = temp_model.from_map(m.get('policies'))

        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')

        return self

class AddonMetaEnvironmentsPolicies(DaraModel):
    def __init__(
        self,
        alert_default_status: str = None,
        bind_default_policy: bool = None,
        bind_entity: main_models.AddonMetaEnvironmentsPoliciesBindEntity = None,
        default_install: bool = None,
        enable_service_account: bool = None,
        metric_check_rule: main_models.AddonMetaEnvironmentsPoliciesMetricCheckRule = None,
        need_restart_after_integration: bool = None,
        protocols: List[main_models.AddonMetaEnvironmentsPoliciesProtocols] = None,
        target_addon_name: str = None,
    ):
        # 告警规则默认安装后是否启用
        self.alert_default_status = alert_default_status
        # 默认模式，即无需绑定实体的接入模式。
        self.bind_default_policy = bind_default_policy
        # 绑定的目标实体信息
        self.bind_entity = bind_entity
        # 是否默认安装
        self.default_install = default_install
        # 是否启用内部授权Token分配
        self.enable_service_account = enable_service_account
        # 组件接入后的数据检查规则
        self.metric_check_rule = metric_check_rule
        # 是否需要在接入后提示重启工作负载
        self.need_restart_after_integration = need_restart_after_integration
        # 支持的客户端协议信息列表
        self.protocols = protocols
        # 跳转的目标组件名称
        self.target_addon_name = target_addon_name

    def validate(self):
        if self.bind_entity:
            self.bind_entity.validate()
        if self.metric_check_rule:
            self.metric_check_rule.validate()
        if self.protocols:
            for v1 in self.protocols:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
            for k1 in self.protocols:
                result['protocols'].append(k1.to_map() if k1 else None)

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
            temp_model = main_models.AddonMetaEnvironmentsPoliciesBindEntity()
            self.bind_entity = temp_model.from_map(m.get('bindEntity'))

        if m.get('defaultInstall') is not None:
            self.default_install = m.get('defaultInstall')

        if m.get('enableServiceAccount') is not None:
            self.enable_service_account = m.get('enableServiceAccount')

        if m.get('metricCheckRule') is not None:
            temp_model = main_models.AddonMetaEnvironmentsPoliciesMetricCheckRule()
            self.metric_check_rule = temp_model.from_map(m.get('metricCheckRule'))

        if m.get('needRestartAfterIntegration') is not None:
            self.need_restart_after_integration = m.get('needRestartAfterIntegration')

        self.protocols = []
        if m.get('protocols') is not None:
            for k1 in m.get('protocols'):
                temp_model = main_models.AddonMetaEnvironmentsPoliciesProtocols()
                self.protocols.append(temp_model.from_map(k1))

        if m.get('targetAddonName') is not None:
            self.target_addon_name = m.get('targetAddonName')

        return self

class AddonMetaEnvironmentsPoliciesProtocols(DaraModel):
    def __init__(
        self,
        description: str = None,
        icon: str = None,
        label: str = None,
        name: str = None,
    ):
        # 协议描述
        self.description = description
        # 协议显示icon
        self.icon = icon
        # 协议显示名称
        self.label = label
        # 协议名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class AddonMetaEnvironmentsPoliciesMetricCheckRule(DaraModel):
    def __init__(
        self,
        prom_ql: List[str] = None,
    ):
        # 检测规则 PromQL
        self.prom_ql = prom_ql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prom_ql is not None:
            result['promQL'] = self.prom_ql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('promQL') is not None:
            self.prom_ql = m.get('promQL')

        return self

class AddonMetaEnvironmentsPoliciesBindEntity(DaraModel):
    def __init__(
        self,
        entity_group_mode: bool = None,
        entity_type: str = None,
        single_entity_mode: bool = None,
        vpc_id_field_key: str = None,
    ):
        # 是否是组模式
        self.entity_group_mode = entity_group_mode
        # 实体类型
        self.entity_type = entity_type
        # 是否是单实体模式
        self.single_entity_mode = single_entity_mode
        # 实体中提取VPC ID 信息的字段
        self.vpc_id_field_key = vpc_id_field_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class AddonMetaEnvironmentsDependencies(DaraModel):
    def __init__(
        self,
        cluster_types: List[str] = None,
        features: Dict[str, bool] = None,
        services: List[str] = None,
    ):
        # 支持的集群类型
        self.cluster_types = cluster_types
        # 探针依赖描述，组件名称。新版已由 collectors 字段替换
        self.features = features
        # 依赖的服务列表
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class AddonMetaEnvironmentsCommonSchemaRefs(DaraModel):
    def __init__(
        self,
        group: str = None,
        version: str = None,
    ):
        # CommonSchema 的分组名称
        self.group = group
        # CommonSchema 的分组版本
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['group'] = self.group

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self



class AddonMetaDashboards(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        url: str = None,
    ):
        # 描述信息
        self.description = description
        # 示意图名称
        self.name = name
        # 示意图 URL
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

