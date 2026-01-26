# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class ListAddonReleasesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListAddonReleasesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. The status code 200 indicates that the request was successful.
        self.code = code
        # The result returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: true and false.
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
            temp_model = main_models.ListAddonReleasesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAddonReleasesResponseBodyData(DaraModel):
    def __init__(
        self,
        releases: List[main_models.ListAddonReleasesResponseBodyDataReleases] = None,
        total: int = None,
    ):
        # The queried add-ons.
        self.releases = releases
        # The total number of entries.
        self.total = total

    def validate(self):
        if self.releases:
            for v1 in self.releases:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Releases'] = []
        if self.releases is not None:
            for k1 in self.releases:
                result['Releases'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.releases = []
        if m.get('Releases') is not None:
            for k1 in m.get('Releases'):
                temp_model = main_models.ListAddonReleasesResponseBodyDataReleases()
                self.releases.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListAddonReleasesResponseBodyDataReleases(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        alert_rule_count: int = None,
        conditions: List[main_models.ListAddonReleasesResponseBodyDataReleasesConditions] = None,
        config: str = None,
        create_time: str = None,
        dashboard_count: int = None,
        environment_id: str = None,
        exporter_count: int = None,
        have_config: bool = None,
        install_user_id: str = None,
        language: str = None,
        managed: bool = None,
        next_version: str = None,
        region_id: str = None,
        release_id: str = None,
        release_name: str = None,
        scene: str = None,
        status: str = None,
        update_time: str = None,
        user_id: str = None,
        version: str = None,
    ):
        # The name of the add-on.
        self.addon_name = addon_name
        # The number of alert rules.
        self.alert_rule_count = alert_rule_count
        # The installation phase.
        self.conditions = conditions
        # The configuration information of the add-on release.
        self.config = config
        # The time when the add-on was created.
        self.create_time = create_time
        # The number of dashboards.
        self.dashboard_count = dashboard_count
        # The environment ID.
        self.environment_id = environment_id
        # The number of exporters.
        self.exporter_count = exporter_count
        # Indicates whether the configuration is available.
        self.have_config = have_config
        # The user ID.
        self.install_user_id = install_user_id
        # The language.
        self.language = language
        # Indicates whether the component is fully managed.
        self.managed = managed
        # The latest version.
        self.next_version = next_version
        # The region ID.
        self.region_id = region_id
        # The release ID after installation.
        self.release_id = release_id
        # The name of the release.
        self.release_name = release_name
        # The scenario.
        self.scene = scene
        # The status.
        self.status = status
        # The time when the add-on was updated.
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id
        # The version of the add-on.
        self.version = version

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name

        if self.alert_rule_count is not None:
            result['AlertRuleCount'] = self.alert_rule_count

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.config is not None:
            result['Config'] = self.config

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dashboard_count is not None:
            result['DashboardCount'] = self.dashboard_count

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.exporter_count is not None:
            result['ExporterCount'] = self.exporter_count

        if self.have_config is not None:
            result['HaveConfig'] = self.have_config

        if self.install_user_id is not None:
            result['InstallUserId'] = self.install_user_id

        if self.language is not None:
            result['Language'] = self.language

        if self.managed is not None:
            result['Managed'] = self.managed

        if self.next_version is not None:
            result['NextVersion'] = self.next_version

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_id is not None:
            result['ReleaseId'] = self.release_id

        if self.release_name is not None:
            result['ReleaseName'] = self.release_name

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')

        if m.get('AlertRuleCount') is not None:
            self.alert_rule_count = m.get('AlertRuleCount')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.ListAddonReleasesResponseBodyDataReleasesConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DashboardCount') is not None:
            self.dashboard_count = m.get('DashboardCount')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('ExporterCount') is not None:
            self.exporter_count = m.get('ExporterCount')

        if m.get('HaveConfig') is not None:
            self.have_config = m.get('HaveConfig')

        if m.get('InstallUserId') is not None:
            self.install_user_id = m.get('InstallUserId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Managed') is not None:
            self.managed = m.get('Managed')

        if m.get('NextVersion') is not None:
            self.next_version = m.get('NextVersion')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseId') is not None:
            self.release_id = m.get('ReleaseId')

        if m.get('ReleaseName') is not None:
            self.release_name = m.get('ReleaseName')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ListAddonReleasesResponseBodyDataReleasesConditions(DaraModel):
    def __init__(
        self,
        first_transition_time: str = None,
        last_transition_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        # The first transition time.
        self.first_transition_time = first_transition_time
        # The last transition time.
        self.last_transition_time = last_transition_time
        # The detailed information.
        self.message = message
        # The reason for the failure.
        self.reason = reason
        # The status of the phase.
        self.status = status
        # The type of the phase.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_transition_time is not None:
            result['FirstTransitionTime'] = self.first_transition_time

        if self.last_transition_time is not None:
            result['LastTransitionTime'] = self.last_transition_time

        if self.message is not None:
            result['Message'] = self.message

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstTransitionTime') is not None:
            self.first_transition_time = m.get('FirstTransitionTime')

        if m.get('LastTransitionTime') is not None:
            self.last_transition_time = m.get('LastTransitionTime')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

