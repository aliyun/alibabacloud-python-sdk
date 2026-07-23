# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListRoutineBuildConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        routine_build_configurations: List[main_models.ListRoutineBuildConfigurationsResponseBodyRoutineBuildConfigurations] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The list of ER build configurations.
        self.routine_build_configurations = routine_build_configurations

    def validate(self):
        if self.routine_build_configurations:
            for v1 in self.routine_build_configurations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RoutineBuildConfigurations'] = []
        if self.routine_build_configurations is not None:
            for k1 in self.routine_build_configurations:
                result['RoutineBuildConfigurations'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.routine_build_configurations = []
        if m.get('RoutineBuildConfigurations') is not None:
            for k1 in m.get('RoutineBuildConfigurations'):
                temp_model = main_models.ListRoutineBuildConfigurationsResponseBodyRoutineBuildConfigurations()
                self.routine_build_configurations.append(temp_model.from_map(k1))

        return self

class ListRoutineBuildConfigurationsResponseBodyRoutineBuildConfigurations(DaraModel):
    def __init__(
        self,
        latest_routine_build_task: main_models.ListRoutineBuildConfigurationsResponseBodyRoutineBuildConfigurationsLatestRoutineBuildTask = None,
        routine_build_configuration: main_models.ListRoutineBuildConfigurationsResponseBodyRoutineBuildConfigurationsRoutineBuildConfiguration = None,
    ):
        # The latest ER build task information.
        self.latest_routine_build_task = latest_routine_build_task
        # The ER build configuration information.
        self.routine_build_configuration = routine_build_configuration

    def validate(self):
        if self.latest_routine_build_task:
            self.latest_routine_build_task.validate()
        if self.routine_build_configuration:
            self.routine_build_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latest_routine_build_task is not None:
            result['LatestRoutineBuildTask'] = self.latest_routine_build_task.to_map()

        if self.routine_build_configuration is not None:
            result['RoutineBuildConfiguration'] = self.routine_build_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestRoutineBuildTask') is not None:
            temp_model = main_models.ListRoutineBuildConfigurationsResponseBodyRoutineBuildConfigurationsLatestRoutineBuildTask()
            self.latest_routine_build_task = temp_model.from_map(m.get('LatestRoutineBuildTask'))

        if m.get('RoutineBuildConfiguration') is not None:
            temp_model = main_models.ListRoutineBuildConfigurationsResponseBodyRoutineBuildConfigurationsRoutineBuildConfiguration()
            self.routine_build_configuration = temp_model.from_map(m.get('RoutineBuildConfiguration'))

        return self

class ListRoutineBuildConfigurationsResponseBodyRoutineBuildConfigurationsRoutineBuildConfiguration(DaraModel):
    def __init__(
        self,
        git_account_name: str = None,
        git_platform: str = None,
        production_branch: str = None,
        repository: str = None,
        routine_name: str = None,
    ):
        # The Git account name.
        self.git_account_name = git_account_name
        # The Git platform. Valid values: github, gitee, and upload.
        self.git_platform = git_platform
        # The production branch name.
        self.production_branch = production_branch
        # The repository name.
        self.repository = repository
        # The ER routine name.
        self.routine_name = routine_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.git_account_name is not None:
            result['GitAccountName'] = self.git_account_name

        if self.git_platform is not None:
            result['GitPlatform'] = self.git_platform

        if self.production_branch is not None:
            result['ProductionBranch'] = self.production_branch

        if self.repository is not None:
            result['Repository'] = self.repository

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GitAccountName') is not None:
            self.git_account_name = m.get('GitAccountName')

        if m.get('GitPlatform') is not None:
            self.git_platform = m.get('GitPlatform')

        if m.get('ProductionBranch') is not None:
            self.production_branch = m.get('ProductionBranch')

        if m.get('Repository') is not None:
            self.repository = m.get('Repository')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        return self

class ListRoutineBuildConfigurationsResponseBodyRoutineBuildConfigurationsLatestRoutineBuildTask(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        routine_name: str = None,
        status: str = None,
    ):
        # The creation time, in ISO 8601 format (UTC), formatted as yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The ER routine name.
        self.routine_name = routine_name
        # The status of the build task. Valid values:
        # 
        # - int: Init.
        # - pending: Pending.
        # - building: Building.
        # - succeed: Succeeded.
        # - failed: Failed.
        # - canceled: Canceled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

