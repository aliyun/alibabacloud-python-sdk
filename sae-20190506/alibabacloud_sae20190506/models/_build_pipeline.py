# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class BuildPipeline(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_name: str = None,
        build_config: main_models.BuildPipelineBuildConfig = None,
        code_config: main_models.BuildPipelineCodeConfig = None,
        deploy_config: main_models.BuildPipelineDeployConfig = None,
        enabled: bool = None,
        image_config: main_models.BuildPipelineImageConfig = None,
        package_config: main_models.BuildPipelinePackageConfig = None,
        trigger_config: main_models.BuildPipelineTriggerConfig = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        # This parameter is required.
        self.application_name = application_name
        # This parameter is required.
        self.build_config = build_config
        # This parameter is required.
        self.code_config = code_config
        self.deploy_config = deploy_config
        self.enabled = enabled
        self.image_config = image_config
        self.package_config = package_config
        # This parameter is required.
        self.trigger_config = trigger_config

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
        if self.trigger_config:
            self.trigger_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.build_config is not None:
            result['BuildConfig'] = self.build_config.to_map()

        if self.code_config is not None:
            result['CodeConfig'] = self.code_config.to_map()

        if self.deploy_config is not None:
            result['DeployConfig'] = self.deploy_config.to_map()

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.image_config is not None:
            result['ImageConfig'] = self.image_config.to_map()

        if self.package_config is not None:
            result['PackageConfig'] = self.package_config.to_map()

        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('BuildConfig') is not None:
            temp_model = main_models.BuildPipelineBuildConfig()
            self.build_config = temp_model.from_map(m.get('BuildConfig'))

        if m.get('CodeConfig') is not None:
            temp_model = main_models.BuildPipelineCodeConfig()
            self.code_config = temp_model.from_map(m.get('CodeConfig'))

        if m.get('DeployConfig') is not None:
            temp_model = main_models.BuildPipelineDeployConfig()
            self.deploy_config = temp_model.from_map(m.get('DeployConfig'))

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ImageConfig') is not None:
            temp_model = main_models.BuildPipelineImageConfig()
            self.image_config = temp_model.from_map(m.get('ImageConfig'))

        if m.get('PackageConfig') is not None:
            temp_model = main_models.BuildPipelinePackageConfig()
            self.package_config = temp_model.from_map(m.get('PackageConfig'))

        if m.get('TriggerConfig') is not None:
            temp_model = main_models.BuildPipelineTriggerConfig()
            self.trigger_config = temp_model.from_map(m.get('TriggerConfig'))

        return self

class BuildPipelineTriggerConfig(DaraModel):
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

class BuildPipelinePackageConfig(DaraModel):
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

class BuildPipelineImageConfig(DaraModel):
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

class BuildPipelineDeployConfig(DaraModel):
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

class BuildPipelineCodeConfig(DaraModel):
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

class BuildPipelineBuildConfig(DaraModel):
    def __init__(
        self,
        before_build_command: str = None,
        build_type: str = None,
        dockerfile_path: str = None,
        run_command: str = None,
        runtime_type: str = None,
        runtime_version: str = None,
        tomcat_config: main_models.TomcatConfig = None,
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
        self.working_dir = working_dir

    def validate(self):
        if self.tomcat_config:
            self.tomcat_config.validate()

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

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

