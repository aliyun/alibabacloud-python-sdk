# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListRoutineBuildsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListRoutineBuildsResponseBodyData] = None,
        page_index: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # The list of ER build tasks.
        self.data = data
        # The page number, same as the PageIndex request parameter.
        self.page_index = page_index
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count
        # The total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListRoutineBuildsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListRoutineBuildsResponseBodyData(DaraModel):
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
        git_account_name: str = None,
        install_command: str = None,
        is_private: bool = None,
        node_version: str = None,
        pipeline_id: int = None,
        pipeline_run_id: int = None,
        production_branch: str = None,
        repository: str = None,
        root_directory: str = None,
        routine_build_id: int = None,
        routine_entry: str = None,
        routine_name: str = None,
        status: str = None,
        template_name: str = None,
        update_time: str = None,
        user_id: int = None,
    ):
        # The static assets directory.
        self.assets_directory = assets_directory
        # The branch used for the build.
        self.branch = branch
        # The build command.
        self.build_command = build_command
        # The ID of the commit.
        self.commit_id = commit_id
        # The commit message.
        self.commit_message = commit_message
        # The creation time, in ISO 8601 format using UTC time. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The environment variables.
        self.environment_variables = environment_variables
        # The Git account ID.
        self.git_account_id = git_account_id
        # The Git account name.
        self.git_account_name = git_account_name
        # The install command.
        self.install_command = install_command
        # Indicates whether the repository is private. Valid values:
        # 
        # - true: The repository is private.
        # - false: The repository is not private.
        self.is_private = is_private
        # The Node.js version. Valid values: `22.x`, `20.x`, `18.x`, `16.x`, `14.x`, and `12.x`.
        self.node_version = node_version
        # The pipeline ID.
        self.pipeline_id = pipeline_id
        # The pipeline execution ID.
        self.pipeline_run_id = pipeline_run_id
        # The production branch name.
        self.production_branch = production_branch
        # The repository name.
        self.repository = repository
        # The root directory.
        self.root_directory = root_directory
        # The ER build task ID.
        self.routine_build_id = routine_build_id
        # The ER entry file path.
        self.routine_entry = routine_entry
        # The ER name.
        self.routine_name = routine_name
        # The status of the build task. Valid values:
        # 
        # - int: initialization
        # - pending: preparing
        # - building: building
        # - succeed: build succeeded
        # - failed: build failed
        # - canceled: canceled
        self.status = status
        # The template name.
        self.template_name = template_name
        # The modification time, in ISO 8601 format using UTC time. Format: yyyy-MM-ddTHH:mm:ssZ.
        self.update_time = update_time
        # The user ID.
        self.user_id = user_id

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

        if self.git_account_name is not None:
            result['GitAccountName'] = self.git_account_name

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

        if self.root_directory is not None:
            result['RootDirectory'] = self.root_directory

        if self.routine_build_id is not None:
            result['RoutineBuildId'] = self.routine_build_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

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

        if m.get('GitAccountName') is not None:
            self.git_account_name = m.get('GitAccountName')

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

        if m.get('RootDirectory') is not None:
            self.root_directory = m.get('RootDirectory')

        if m.get('RoutineBuildId') is not None:
            self.routine_build_id = m.get('RoutineBuildId')

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

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

