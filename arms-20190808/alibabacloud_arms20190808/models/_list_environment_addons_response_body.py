# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListEnvironmentAddonsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListEnvironmentAddonsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        # The result of the operation.
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListEnvironmentAddonsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEnvironmentAddonsResponseBodyData(DaraModel):
    def __init__(
        self,
        addons: List[main_models.ListEnvironmentAddonsResponseBodyDataAddons] = None,
        total: int = None,
    ):
        # The queried add-ons.
        self.addons = addons
        self.total = total

    def validate(self):
        if self.addons:
            for v1 in self.addons:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Addons'] = []
        if self.addons is not None:
            for k1 in self.addons:
                result['Addons'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addons = []
        if m.get('Addons') is not None:
            for k1 in m.get('Addons'):
                temp_model = main_models.ListEnvironmentAddonsResponseBodyDataAddons()
                self.addons.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListEnvironmentAddonsResponseBodyDataAddons(DaraModel):
    def __init__(
        self,
        alias: str = None,
        categories: List[str] = None,
        dashboards: List[main_models.ListEnvironmentAddonsResponseBodyDataAddonsDashboards] = None,
        description: str = None,
        environments: List[main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironments] = None,
        icon: str = None,
        keywords: List[str] = None,
        language: str = None,
        latest_release_create_time: str = None,
        name: str = None,
        once: bool = None,
        scene: str = None,
        version: str = None,
        weight: str = None,
    ):
        # The alias of the add-on.
        self.alias = alias
        # The tags of the add-on.
        self.categories = categories
        # The dashboards.
        self.dashboards = dashboards
        # The description of the add-on.
        self.description = description
        # The supported environments.
        self.environments = environments
        # The URL of the icon.
        self.icon = icon
        # The collection of keywords.
        self.keywords = keywords
        # The language.
        self.language = language
        # The time when the instance was last created.
        self.latest_release_create_time = latest_release_create_time
        # The name of the add-on.
        self.name = name
        # Indicates whether the add-on can be installed only once.
        self.once = once
        # The scenario.
        self.scene = scene
        # The version of the agent.
        self.version = version
        # The weight.
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
            result['Alias'] = self.alias

        if self.categories is not None:
            result['Categories'] = self.categories

        result['Dashboards'] = []
        if self.dashboards is not None:
            for k1 in self.dashboards:
                result['Dashboards'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        result['Environments'] = []
        if self.environments is not None:
            for k1 in self.environments:
                result['Environments'].append(k1.to_map() if k1 else None)

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.keywords is not None:
            result['Keywords'] = self.keywords

        if self.language is not None:
            result['Language'] = self.language

        if self.latest_release_create_time is not None:
            result['LatestReleaseCreateTime'] = self.latest_release_create_time

        if self.name is not None:
            result['Name'] = self.name

        if self.once is not None:
            result['Once'] = self.once

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.version is not None:
            result['Version'] = self.version

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        self.dashboards = []
        if m.get('Dashboards') is not None:
            for k1 in m.get('Dashboards'):
                temp_model = main_models.ListEnvironmentAddonsResponseBodyDataAddonsDashboards()
                self.dashboards.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.environments = []
        if m.get('Environments') is not None:
            for k1 in m.get('Environments'):
                temp_model = main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironments()
                self.environments.append(temp_model.from_map(k1))

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('LatestReleaseCreateTime') is not None:
            self.latest_release_create_time = m.get('LatestReleaseCreateTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Once') is not None:
            self.once = m.get('Once')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class ListEnvironmentAddonsResponseBodyDataAddonsEnvironments(DaraModel):
    def __init__(
        self,
        dependencies: main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsDependencies = None,
        description: str = None,
        enable: bool = None,
        label: str = None,
        name: str = None,
        policies: main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsPolicies = None,
    ):
        # The dependencies of the environment.
        self.dependencies = dependencies
        # The description of the environment.
        self.description = description
        # Indicates whether the feature is enabled.
        self.enable = enable
        # The tag of the environment.
        self.label = label
        # The name of the environment.
        self.name = name
        # The control policies in the environment.
        self.policies = policies

    def validate(self):
        if self.dependencies:
            self.dependencies.validate()
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dependencies is not None:
            result['Dependencies'] = self.dependencies.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.policies is not None:
            result['Policies'] = self.policies.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dependencies') is not None:
            temp_model = main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsDependencies()
            self.dependencies = temp_model.from_map(m.get('Dependencies'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policies') is not None:
            temp_model = main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsPolicies()
            self.policies = temp_model.from_map(m.get('Policies'))

        return self

class ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsPolicies(DaraModel):
    def __init__(
        self,
        alert_default_status: str = None,
        default_install: bool = None,
        enable_service_account: bool = None,
        metric_check_rule: main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsPoliciesMetricCheckRule = None,
        need_restart_after_integration: bool = None,
        protocols: List[main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsPoliciesProtocols] = None,
        target_addon_name: str = None,
    ):
        # The default alert status.
        self.alert_default_status = alert_default_status
        # The default installation status.
        self.default_install = default_install
        # Indicates whether a service account is enabled.
        self.enable_service_account = enable_service_account
        # The metric check rule.
        self.metric_check_rule = metric_check_rule
        # Indicates whether a restart is required after the installation.
        self.need_restart_after_integration = need_restart_after_integration
        # The supported protocols.
        self.protocols = protocols
        # The target name of the add-on.
        self.target_addon_name = target_addon_name

    def validate(self):
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
            result['AlertDefaultStatus'] = self.alert_default_status

        if self.default_install is not None:
            result['DefaultInstall'] = self.default_install

        if self.enable_service_account is not None:
            result['EnableServiceAccount'] = self.enable_service_account

        if self.metric_check_rule is not None:
            result['MetricCheckRule'] = self.metric_check_rule.to_map()

        if self.need_restart_after_integration is not None:
            result['NeedRestartAfterIntegration'] = self.need_restart_after_integration

        result['Protocols'] = []
        if self.protocols is not None:
            for k1 in self.protocols:
                result['Protocols'].append(k1.to_map() if k1 else None)

        if self.target_addon_name is not None:
            result['TargetAddonName'] = self.target_addon_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDefaultStatus') is not None:
            self.alert_default_status = m.get('AlertDefaultStatus')

        if m.get('DefaultInstall') is not None:
            self.default_install = m.get('DefaultInstall')

        if m.get('EnableServiceAccount') is not None:
            self.enable_service_account = m.get('EnableServiceAccount')

        if m.get('MetricCheckRule') is not None:
            temp_model = main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsPoliciesMetricCheckRule()
            self.metric_check_rule = temp_model.from_map(m.get('MetricCheckRule'))

        if m.get('NeedRestartAfterIntegration') is not None:
            self.need_restart_after_integration = m.get('NeedRestartAfterIntegration')

        self.protocols = []
        if m.get('Protocols') is not None:
            for k1 in m.get('Protocols'):
                temp_model = main_models.ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsPoliciesProtocols()
                self.protocols.append(temp_model.from_map(k1))

        if m.get('TargetAddonName') is not None:
            self.target_addon_name = m.get('TargetAddonName')

        return self

class ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsPoliciesProtocols(DaraModel):
    def __init__(
        self,
        description: str = None,
        icon: str = None,
        label: str = None,
        name: str = None,
    ):
        # The description of the protocol.
        self.description = description
        # The URL of the protocol icon.
        self.icon = icon
        # The tag of the protocol.
        self.label = label
        # The name of the protocol.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsPoliciesMetricCheckRule(DaraModel):
    def __init__(
        self,
        prom_ql: List[str] = None,
    ):
        # The PromQL statements.
        self.prom_ql = prom_ql

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prom_ql is not None:
            result['PromQL'] = self.prom_ql

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromQL') is not None:
            self.prom_ql = m.get('PromQL')

        return self

class ListEnvironmentAddonsResponseBodyDataAddonsEnvironmentsDependencies(DaraModel):
    def __init__(
        self,
        cluster_types: List[str] = None,
        features: Dict[str, bool] = None,
        services: List[str] = None,
    ):
        # The cluster type.
        self.cluster_types = cluster_types
        # The feature that can be installed in the environment.
        self.features = features
        # The services.
        self.services = services

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_types is not None:
            result['ClusterTypes'] = self.cluster_types

        if self.features is not None:
            result['Features'] = self.features

        if self.services is not None:
            result['Services'] = self.services

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterTypes') is not None:
            self.cluster_types = m.get('ClusterTypes')

        if m.get('Features') is not None:
            self.features = m.get('Features')

        if m.get('Services') is not None:
            self.services = m.get('Services')

        return self

class ListEnvironmentAddonsResponseBodyDataAddonsDashboards(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        url: str = None,
    ):
        # The description of the dashboard.
        self.description = description
        # The name of the dashboard.
        self.name = name
        # The URL of the dashboard.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

