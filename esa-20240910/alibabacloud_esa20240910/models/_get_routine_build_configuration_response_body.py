# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class GetRoutineBuildConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        assets_directory: str = None,
        build_branches: str = None,
        build_command: str = None,
        create_time: str = None,
        environment_variables: Dict[str, str] = None,
        git_account_id: int = None,
        git_account_type: str = None,
        git_platform: str = None,
        install_command: str = None,
        is_private: bool = None,
        node_version: str = None,
        production_branch: str = None,
        repository: str = None,
        request_id: str = None,
        root_directory: str = None,
        routine_build_configuration_id: int = None,
        routine_entry: str = None,
        routine_name: str = None,
        update_time: str = None,
    ):
        # The static assets directory.
        self.assets_directory = assets_directory
        # The branches that trigger builds. A value of * indicates all branches. Multiple specific branches are separated by commas.
        self.build_branches = build_branches
        # The build command.
        self.build_command = build_command
        # The creation time, in ISO 8601 format using UTC time. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The environment variables.
        self.environment_variables = environment_variables
        # The Git account ID.
        self.git_account_id = git_account_id
        # The Git account type. Valid values:
        # - User: individual account.
        # - Organization: organization account.
        self.git_account_type = git_account_type
        # The Git platform.
        self.git_platform = git_platform
        # The install command.
        self.install_command = install_command
        # Indicates whether the repository is private. Valid values:
        # 
        # - true: The repository is private.
        # - false: The repository is not private.
        self.is_private = is_private
        # The Node.js version.
        self.node_version = node_version
        # The production branch name.
        self.production_branch = production_branch
        # The repository name.
        self.repository = repository
        # The request ID.
        self.request_id = request_id
        # The root directory.
        self.root_directory = root_directory
        # The ER build configuration ID.
        self.routine_build_configuration_id = routine_build_configuration_id
        # The ER entry file path.
        self.routine_entry = routine_entry
        # The ER name.
        self.routine_name = routine_name
        # The modification time, in ISO 8601 format using UTC time. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assets_directory is not None:
            result['AssetsDirectory'] = self.assets_directory

        if self.build_branches is not None:
            result['BuildBranches'] = self.build_branches

        if self.build_command is not None:
            result['BuildCommand'] = self.build_command

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables

        if self.git_account_id is not None:
            result['GitAccountId'] = self.git_account_id

        if self.git_account_type is not None:
            result['GitAccountType'] = self.git_account_type

        if self.git_platform is not None:
            result['GitPlatform'] = self.git_platform

        if self.install_command is not None:
            result['InstallCommand'] = self.install_command

        if self.is_private is not None:
            result['IsPrivate'] = self.is_private

        if self.node_version is not None:
            result['NodeVersion'] = self.node_version

        if self.production_branch is not None:
            result['ProductionBranch'] = self.production_branch

        if self.repository is not None:
            result['Repository'] = self.repository

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory

        if self.routine_build_configuration_id is not None:
            result['RoutineBuildConfigurationId'] = self.routine_build_configuration_id

        if self.routine_entry is not None:
            result['RoutineEntry'] = self.routine_entry

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsDirectory') is not None:
            self.assets_directory = m.get('AssetsDirectory')

        if m.get('BuildBranches') is not None:
            self.build_branches = m.get('BuildBranches')

        if m.get('BuildCommand') is not None:
            self.build_command = m.get('BuildCommand')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')

        if m.get('GitAccountId') is not None:
            self.git_account_id = m.get('GitAccountId')

        if m.get('GitAccountType') is not None:
            self.git_account_type = m.get('GitAccountType')

        if m.get('GitPlatform') is not None:
            self.git_platform = m.get('GitPlatform')

        if m.get('InstallCommand') is not None:
            self.install_command = m.get('InstallCommand')

        if m.get('IsPrivate') is not None:
            self.is_private = m.get('IsPrivate')

        if m.get('NodeVersion') is not None:
            self.node_version = m.get('NodeVersion')

        if m.get('ProductionBranch') is not None:
            self.production_branch = m.get('ProductionBranch')

        if m.get('Repository') is not None:
            self.repository = m.get('Repository')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootDirectory') is not None:
            self.root_directory = m.get('RootDirectory')

        if m.get('RoutineBuildConfigurationId') is not None:
            self.routine_build_configuration_id = m.get('RoutineBuildConfigurationId')

        if m.get('RoutineEntry') is not None:
            self.routine_entry = m.get('RoutineEntry')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

