# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class GetRoutineBuildResponseBody(DaraModel):
    def __init__(
        self,
        assets_directory: str = None,
        branch: str = None,
        build_command: str = None,
        commit_id: str = None,
        commit_message: str = None,
        create_time: str = None,
        environment_variables: Dict[str, str] = None,
        git_account_id: int = None,
        id: int = None,
        install_command: str = None,
        is_private: bool = None,
        node_version: str = None,
        pipeline_id: int = None,
        pipeline_run_id: int = None,
        production_branch: str = None,
        repository: str = None,
        request_id: str = None,
        root_directory: str = None,
        routine_entry: str = None,
        routine_name: str = None,
        status: str = None,
        template_name: str = None,
        update_time: str = None,
    ):
        # The static resource directory.
        self.assets_directory = assets_directory
        # The branch used for the build.
        self.branch = branch
        # The build command.
        self.build_command = build_command
        # The commit ID.
        self.commit_id = commit_id
        # The commit message.
        self.commit_message = commit_message
        # The creation time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.create_time = create_time
        # The environment variables.
        self.environment_variables = environment_variables
        # The Git account ID.
        self.git_account_id = git_account_id
        # The ID of the ER build task.
        self.id = id
        # The install command.
        self.install_command = install_command
        # Indicates whether the repository is private. Valid values:
        # 
        # - true: The repository is private.
        # - false: The repository is not private.
        self.is_private = is_private
        # The Node.js version. Valid values: `22.x`, `20.x`, `18.x`, `16.x`, `14.x`, `12.x`.
        self.node_version = node_version
        # The pipeline ID in Yunxiao.
        self.pipeline_id = pipeline_id
        # The build task ID in Yunxiao.
        self.pipeline_run_id = pipeline_run_id
        # The production branch name.
        self.production_branch = production_branch
        # The repository name.
        self.repository = repository
        # The request ID.
        self.request_id = request_id
        # The root directory.
        self.root_directory = root_directory
        # The ER entry file path.
        self.routine_entry = routine_entry
        # The ER name.
        self.routine_name = routine_name
        # The status of the build task. Valid values:
        # 
        # - int: init
        # - pending: preparing
        # - building: building
        # - succeed: build succeeded
        # - failed: build failed
        # - canceled: canceled
        self.status = status
        # The template name.
        self.template_name = template_name
        # The modification time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
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

        if self.branch is not None:
            result['Branch'] = self.branch

        if self.build_command is not None:
            result['BuildCommand'] = self.build_command

        if self.commit_id is not None:
            result['CommitId'] = self.commit_id

        if self.commit_message is not None:
            result['CommitMessage'] = self.commit_message

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.environment_variables is not None:
            result['EnvironmentVariables'] = self.environment_variables

        if self.git_account_id is not None:
            result['GitAccountId'] = self.git_account_id

        if self.id is not None:
            result['Id'] = self.id

        if self.install_command is not None:
            result['InstallCommand'] = self.install_command

        if self.is_private is not None:
            result['IsPrivate'] = self.is_private

        if self.node_version is not None:
            result['NodeVersion'] = self.node_version

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id

        if self.production_branch is not None:
            result['ProductionBranch'] = self.production_branch

        if self.repository is not None:
            result['Repository'] = self.repository

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory

        if self.routine_entry is not None:
            result['RoutineEntry'] = self.routine_entry

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        if self.status is not None:
            result['Status'] = self.status

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetsDirectory') is not None:
            self.assets_directory = m.get('AssetsDirectory')

        if m.get('Branch') is not None:
            self.branch = m.get('Branch')

        if m.get('BuildCommand') is not None:
            self.build_command = m.get('BuildCommand')

        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')

        if m.get('CommitMessage') is not None:
            self.commit_message = m.get('CommitMessage')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnvironmentVariables') is not None:
            self.environment_variables = m.get('EnvironmentVariables')

        if m.get('GitAccountId') is not None:
            self.git_account_id = m.get('GitAccountId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstallCommand') is not None:
            self.install_command = m.get('InstallCommand')

        if m.get('IsPrivate') is not None:
            self.is_private = m.get('IsPrivate')

        if m.get('NodeVersion') is not None:
            self.node_version = m.get('NodeVersion')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')

        if m.get('ProductionBranch') is not None:
            self.production_branch = m.get('ProductionBranch')

        if m.get('Repository') is not None:
            self.repository = m.get('Repository')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootDirectory') is not None:
            self.root_directory = m.get('RootDirectory')

        if m.get('RoutineEntry') is not None:
            self.routine_entry = m.get('RoutineEntry')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

