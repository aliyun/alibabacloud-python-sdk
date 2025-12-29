# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class BuildPipelineRun(DaraModel):
    def __init__(
        self,
        build_config: main_models.BuildPipelineRunBuildConfig = None,
        build_duration: int = None,
        code_config: main_models.BuildPipelineRunCodeConfig = None,
        create_time: int = None,
        deploy_config: main_models.BuildPipelineRunDeployConfig = None,
        deploy_duration: int = None,
        end_time: int = None,
        image_config: main_models.BuildPipelineRunImageConfig = None,
        package_config: main_models.BuildPipelineRunPackageConfig = None,
        pipeline_id: str = None,
        pipeline_run_id: str = None,
        start_time: int = None,
        status: str = None,
        steps: List[main_models.BuildPipelineRunSteps] = None,
        trigger_config: main_models.BuildPipelineRunTriggerConfig = None,
        version_id: str = None,
        wait_duration: int = None,
    ):
        self.build_config = build_config
        self.build_duration = build_duration
        self.code_config = code_config
        self.create_time = create_time
        self.deploy_config = deploy_config
        self.deploy_duration = deploy_duration
        self.end_time = end_time
        self.image_config = image_config
        self.package_config = package_config
        self.pipeline_id = pipeline_id
        self.pipeline_run_id = pipeline_run_id
        self.start_time = start_time
        self.status = status
        self.steps = steps
        self.trigger_config = trigger_config
        self.version_id = version_id
        self.wait_duration = wait_duration

    def validate(self):
        if self.build_config:
            self.build_config.validate()
        if self.code_config:
            self.code_config.validate()
        if self.deploy_config:
            self.deploy_config.validate()
        if self.image_config:
            self.image_config.validate()
        if self.package_config:
            self.package_config.validate()
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_config is not None:
            result['BuildConfig'] = self.build_config.to_map()

        if self.build_duration is not None:
            result['BuildDuration'] = self.build_duration

        if self.code_config is not None:
            result['CodeConfig'] = self.code_config.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.deploy_config is not None:
            result['DeployConfig'] = self.deploy_config.to_map()

        if self.deploy_duration is not None:
            result['DeployDuration'] = self.deploy_duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.image_config is not None:
            result['ImageConfig'] = self.image_config.to_map()

        if self.package_config is not None:
            result['PackageConfig'] = self.package_config.to_map()

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.pipeline_run_id is not None:
            result['PipelineRunId'] = self.pipeline_run_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        result['Steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['Steps'].append(k1.to_map() if k1 else None)

        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config.to_map()

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        if self.wait_duration is not None:
            result['WaitDuration'] = self.wait_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildConfig') is not None:
            temp_model = main_models.BuildPipelineRunBuildConfig()
            self.build_config = temp_model.from_map(m.get('BuildConfig'))

        if m.get('BuildDuration') is not None:
            self.build_duration = m.get('BuildDuration')

        if m.get('CodeConfig') is not None:
            temp_model = main_models.BuildPipelineRunCodeConfig()
            self.code_config = temp_model.from_map(m.get('CodeConfig'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DeployConfig') is not None:
            temp_model = main_models.BuildPipelineRunDeployConfig()
            self.deploy_config = temp_model.from_map(m.get('DeployConfig'))

        if m.get('DeployDuration') is not None:
            self.deploy_duration = m.get('DeployDuration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('ImageConfig') is not None:
            temp_model = main_models.BuildPipelineRunImageConfig()
            self.image_config = temp_model.from_map(m.get('ImageConfig'))

        if m.get('PackageConfig') is not None:
            temp_model = main_models.BuildPipelineRunPackageConfig()
            self.package_config = temp_model.from_map(m.get('PackageConfig'))

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('PipelineRunId') is not None:
            self.pipeline_run_id = m.get('PipelineRunId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.steps = []
        if m.get('Steps') is not None:
            for k1 in m.get('Steps'):
                temp_model = main_models.BuildPipelineRunSteps()
                self.steps.append(temp_model.from_map(k1))

        if m.get('TriggerConfig') is not None:
            temp_model = main_models.BuildPipelineRunTriggerConfig()
            self.trigger_config = temp_model.from_map(m.get('TriggerConfig'))

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        if m.get('WaitDuration') is not None:
            self.wait_duration = m.get('WaitDuration')

        return self

class BuildPipelineRunTriggerConfig(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        tag_name: str = None,
        type: str = None,
    ):
        self.branch_name = branch_name
        self.tag_name = tag_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class BuildPipelineRunSteps(DaraModel):
    def __init__(
        self,
        description: str = None,
        duration: int = None,
        end_time: int = None,
        id: str = None,
        name: str = None,
        result: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.description = description
        self.duration = duration
        self.end_time = end_time
        self.id = id
        self.name = name
        self.result = result
        self.start_time = start_time
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.result is not None:
            result['Result'] = self.result

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class BuildPipelineRunPackageConfig(DaraModel):
    def __init__(
        self,
        package_name: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
    ):
        self.package_name = package_name
        self.package_type = package_type
        self.package_url = package_url
        self.package_version = package_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.package_name is not None:
            result['PackageName'] = self.package_name

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PackageName') is not None:
            self.package_name = m.get('PackageName')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        return self

class BuildPipelineRunImageConfig(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        namespace: str = None,
        repository: str = None,
    ):
        self.instance_type = instance_type
        self.namespace = namespace
        self.repository = repository

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.repository is not None:
            result['Repository'] = self.repository

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Repository') is not None:
            self.repository = m.get('Repository')

        return self

class BuildPipelineRunDeployConfig(DaraModel):
    def __init__(
        self,
        always_allocate_cpu: bool = None,
        maximum_instance_count: int = None,
        minimum_instance_count: int = None,
        update_application_input: str = None,
        update_traffic: bool = None,
    ):
        self.always_allocate_cpu = always_allocate_cpu
        self.maximum_instance_count = maximum_instance_count
        self.minimum_instance_count = minimum_instance_count
        self.update_application_input = update_application_input
        self.update_traffic = update_traffic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.always_allocate_cpu is not None:
            result['AlwaysAllocateCPU'] = self.always_allocate_cpu

        if self.maximum_instance_count is not None:
            result['MaximumInstanceCount'] = self.maximum_instance_count

        if self.minimum_instance_count is not None:
            result['MinimumInstanceCount'] = self.minimum_instance_count

        if self.update_application_input is not None:
            result['UpdateApplicationInput'] = self.update_application_input

        if self.update_traffic is not None:
            result['UpdateTraffic'] = self.update_traffic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlwaysAllocateCPU') is not None:
            self.always_allocate_cpu = m.get('AlwaysAllocateCPU')

        if m.get('MaximumInstanceCount') is not None:
            self.maximum_instance_count = m.get('MaximumInstanceCount')

        if m.get('MinimumInstanceCount') is not None:
            self.minimum_instance_count = m.get('MinimumInstanceCount')

        if m.get('UpdateApplicationInput') is not None:
            self.update_application_input = m.get('UpdateApplicationInput')

        if m.get('UpdateTraffic') is not None:
            self.update_traffic = m.get('UpdateTraffic')

        return self

class BuildPipelineRunCodeConfig(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        branch_name: str = None,
        commit_id: str = None,
        commit_url: str = None,
        organization_id: str = None,
        provider: str = None,
        repo_full_name: str = None,
        repo_id: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id
        # This parameter is required.
        self.branch_name = branch_name
        self.commit_id = commit_id
        self.commit_url = commit_url
        self.organization_id = organization_id
        # This parameter is required.
        self.provider = provider
        # This parameter is required.
        self.repo_full_name = repo_full_name
        # This parameter is required.
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.commit_id is not None:
            result['CommitId'] = self.commit_id

        if self.commit_url is not None:
            result['CommitUrl'] = self.commit_url

        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.repo_full_name is not None:
            result['RepoFullName'] = self.repo_full_name

        if self.repo_id is not None:
            result['RepoId'] = self.repo_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('CommitId') is not None:
            self.commit_id = m.get('CommitId')

        if m.get('CommitUrl') is not None:
            self.commit_url = m.get('CommitUrl')

        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('RepoFullName') is not None:
            self.repo_full_name = m.get('RepoFullName')

        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')

        return self

class BuildPipelineRunBuildConfig(DaraModel):
    def __init__(
        self,
        before_build_command: str = None,
        build_type: str = None,
        dockerfile_path: str = None,
        run_command: str = None,
        runtime_type: str = None,
        runtime_version: str = None,
        tomcat_config: main_models.TomcatConfig = None,
        trigger: main_models.BuildPipelineRunBuildConfigTrigger = None,
        working_dir: str = None,
    ):
        self.before_build_command = before_build_command
        # This parameter is required.
        self.build_type = build_type
        self.dockerfile_path = dockerfile_path
        self.run_command = run_command
        self.runtime_type = runtime_type
        self.runtime_version = runtime_version
        self.tomcat_config = tomcat_config
        # This parameter is required.
        self.trigger = trigger
        self.working_dir = working_dir

    def validate(self):
        if self.tomcat_config:
            self.tomcat_config.validate()
        if self.trigger:
            self.trigger.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.before_build_command is not None:
            result['BeforeBuildCommand'] = self.before_build_command

        if self.build_type is not None:
            result['BuildType'] = self.build_type

        if self.dockerfile_path is not None:
            result['DockerfilePath'] = self.dockerfile_path

        if self.run_command is not None:
            result['RunCommand'] = self.run_command

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        if self.runtime_version is not None:
            result['RuntimeVersion'] = self.runtime_version

        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config.to_map()

        if self.trigger is not None:
            result['Trigger'] = self.trigger.to_map()

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeforeBuildCommand') is not None:
            self.before_build_command = m.get('BeforeBuildCommand')

        if m.get('BuildType') is not None:
            self.build_type = m.get('BuildType')

        if m.get('DockerfilePath') is not None:
            self.dockerfile_path = m.get('DockerfilePath')

        if m.get('RunCommand') is not None:
            self.run_command = m.get('RunCommand')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        if m.get('RuntimeVersion') is not None:
            self.runtime_version = m.get('RuntimeVersion')

        if m.get('TomcatConfig') is not None:
            temp_model = main_models.TomcatConfig()
            self.tomcat_config = temp_model.from_map(m.get('TomcatConfig'))

        if m.get('Trigger') is not None:
            temp_model = main_models.BuildPipelineRunBuildConfigTrigger()
            self.trigger = temp_model.from_map(m.get('Trigger'))

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class BuildPipelineRunBuildConfigTrigger(DaraModel):
    def __init__(
        self,
        branch_name: str = None,
        tag_name: str = None,
        type: str = None,
    ):
        self.branch_name = branch_name
        self.tag_name = tag_name
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch_name is not None:
            result['BranchName'] = self.branch_name

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BranchName') is not None:
            self.branch_name = m.get('BranchName')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

