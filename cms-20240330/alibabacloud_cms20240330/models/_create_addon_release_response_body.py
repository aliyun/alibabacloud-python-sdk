# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateAddonReleaseResponseBody(DaraModel):
    def __init__(
        self,
        release: main_models.CreateAddonReleaseResponseBodyRelease = None,
        request_id: str = None,
    ):
        # Accessed component information.
        self.release = release
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.release:
            self.release.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.release is not None:
            result['release'] = self.release.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('release') is not None:
            temp_model = main_models.CreateAddonReleaseResponseBodyRelease()
            self.release = temp_model.from_map(m.get('release'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateAddonReleaseResponseBodyRelease(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        alert_rule_count: int = None,
        conditions: List[main_models.CreateAddonReleaseResponseBodyReleaseConditions] = None,
        config: str = None,
        create_time: str = None,
        dashboard_count: int = None,
        entity_rules: main_models.EntityGroupBase = None,
        env_type: str = None,
        environment_id: str = None,
        exporter_count: int = None,
        have_config: bool = None,
        install_user_id: str = None,
        language: str = None,
        managed: bool = None,
        parent_addon_release_id: str = None,
        policy_id: str = None,
        region_id: str = None,
        release_id: str = None,
        release_name: str = None,
        scene: str = None,
        status: str = None,
        update_time: str = None,
        user_id: str = None,
        version: str = None,
        workspace: str = None,
    ):
        # The Addon name of the component being monitored.
        self.addon_name = addon_name
        # Number of alert groups.
        self.alert_rule_count = alert_rule_count
        # Component installation phase information.
        self.conditions = conditions
        # Component configuration.
        self.config = config
        # Connection time.
        self.create_time = create_time
        # Number of dashboards.
        self.dashboard_count = dashboard_count
        # Entity details.
        self.entity_rules = entity_rules
        # Environment type.
        self.env_type = env_type
        # Environment ID.
        self.environment_id = environment_id
        # Number of plugins.
        self.exporter_count = exporter_count
        # Whether it has configuration.
        self.have_config = have_config
        # ID of the user who installed it.
        self.install_user_id = install_user_id
        # Language.
        self.language = language
        # Whether it is a managed component.
        self.managed = managed
        # Parent AddonReleaseId.
        self.parent_addon_release_id = parent_addon_release_id
        # Policy environment ID.
        self.policy_id = policy_id
        # Region ID.
        self.region_id = region_id
        # ReleaseID after installation.
        self.release_id = release_id
        # Name of the Release.
        self.release_name = release_name
        # Component scenario.
        self.scene = scene
        # Component status.
        self.status = status
        # Update time.
        self.update_time = update_time
        # ID of the owner user.
        self.user_id = user_id
        # Component version.
        self.version = version
        # Workspace.
        self.workspace = workspace

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.entity_rules:
            self.entity_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['addonName'] = self.addon_name

        if self.alert_rule_count is not None:
            result['alertRuleCount'] = self.alert_rule_count

        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.config is not None:
            result['config'] = self.config

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.dashboard_count is not None:
            result['dashboardCount'] = self.dashboard_count

        if self.entity_rules is not None:
            result['entityRules'] = self.entity_rules.to_map()

        if self.env_type is not None:
            result['envType'] = self.env_type

        if self.environment_id is not None:
            result['environmentId'] = self.environment_id

        if self.exporter_count is not None:
            result['exporterCount'] = self.exporter_count

        if self.have_config is not None:
            result['haveConfig'] = self.have_config

        if self.install_user_id is not None:
            result['installUserId'] = self.install_user_id

        if self.language is not None:
            result['language'] = self.language

        if self.managed is not None:
            result['managed'] = self.managed

        if self.parent_addon_release_id is not None:
            result['parentAddonReleaseId'] = self.parent_addon_release_id

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.release_id is not None:
            result['releaseId'] = self.release_id

        if self.release_name is not None:
            result['releaseName'] = self.release_name

        if self.scene is not None:
            result['scene'] = self.scene

        if self.status is not None:
            result['status'] = self.status

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addonName') is not None:
            self.addon_name = m.get('addonName')

        if m.get('alertRuleCount') is not None:
            self.alert_rule_count = m.get('alertRuleCount')

        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.CreateAddonReleaseResponseBodyReleaseConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('dashboardCount') is not None:
            self.dashboard_count = m.get('dashboardCount')

        if m.get('entityRules') is not None:
            temp_model = main_models.EntityGroupBase()
            self.entity_rules = temp_model.from_map(m.get('entityRules'))

        if m.get('envType') is not None:
            self.env_type = m.get('envType')

        if m.get('environmentId') is not None:
            self.environment_id = m.get('environmentId')

        if m.get('exporterCount') is not None:
            self.exporter_count = m.get('exporterCount')

        if m.get('haveConfig') is not None:
            self.have_config = m.get('haveConfig')

        if m.get('installUserId') is not None:
            self.install_user_id = m.get('installUserId')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('managed') is not None:
            self.managed = m.get('managed')

        if m.get('parentAddonReleaseId') is not None:
            self.parent_addon_release_id = m.get('parentAddonReleaseId')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('releaseId') is not None:
            self.release_id = m.get('releaseId')

        if m.get('releaseName') is not None:
            self.release_name = m.get('releaseName')

        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class CreateAddonReleaseResponseBodyReleaseConditions(DaraModel):
    def __init__(
        self,
        first_transition_time: str = None,
        last_transition_time: str = None,
        message: str = None,
        status: str = None,
        type: str = None,
    ):
        # First transition time.
        self.first_transition_time = first_transition_time
        # Last transition time.
        self.last_transition_time = last_transition_time
        # Detailed information.
        self.message = message
        # Phase status.
        self.status = status
        # Phase type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_transition_time is not None:
            result['firstTransitionTime'] = self.first_transition_time

        if self.last_transition_time is not None:
            result['lastTransitionTime'] = self.last_transition_time

        if self.message is not None:
            result['message'] = self.message

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstTransitionTime') is not None:
            self.first_transition_time = m.get('firstTransitionTime')

        if m.get('lastTransitionTime') is not None:
            self.last_transition_time = m.get('lastTransitionTime')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

