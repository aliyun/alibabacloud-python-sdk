# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class CreateTrainingJobRequest(DaraModel):
    def __init__(
        self,
        algorithm_name: str = None,
        algorithm_provider: str = None,
        algorithm_spec: main_models.AlgorithmSpec = None,
        algorithm_version: str = None,
        assign_node_spec: main_models.AssignNodeSpec = None,
        code_dir: main_models.Location = None,
        compute_resource: main_models.CreateTrainingJobRequestComputeResource = None,
        environments: Dict[str, str] = None,
        experiment_config: main_models.CreateTrainingJobRequestExperimentConfig = None,
        hyper_parameters: List[main_models.CreateTrainingJobRequestHyperParameters] = None,
        input_channels: List[main_models.CreateTrainingJobRequestInputChannels] = None,
        labels: List[main_models.CreateTrainingJobRequestLabels] = None,
        output_channels: List[main_models.CreateTrainingJobRequestOutputChannels] = None,
        priority: int = None,
        python_requirements: List[str] = None,
        role_arn: str = None,
        scheduler: main_models.CreateTrainingJobRequestScheduler = None,
        settings: main_models.JobSettings = None,
        training_job_description: str = None,
        training_job_name: str = None,
        user_vpc: main_models.CreateTrainingJobRequestUserVpc = None,
        workspace_id: str = None,
    ):
        self.algorithm_name = algorithm_name
        self.algorithm_provider = algorithm_provider
        self.algorithm_spec = algorithm_spec
        self.algorithm_version = algorithm_version
        self.assign_node_spec = assign_node_spec
        self.code_dir = code_dir
        self.compute_resource = compute_resource
        self.environments = environments
        self.experiment_config = experiment_config
        self.hyper_parameters = hyper_parameters
        self.input_channels = input_channels
        self.labels = labels
        self.output_channels = output_channels
        self.priority = priority
        self.python_requirements = python_requirements
        self.role_arn = role_arn
        self.scheduler = scheduler
        self.settings = settings
        self.training_job_description = training_job_description
        # This parameter is required.
        self.training_job_name = training_job_name
        self.user_vpc = user_vpc
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.algorithm_spec:
            self.algorithm_spec.validate()
        if self.assign_node_spec:
            self.assign_node_spec.validate()
        if self.code_dir:
            self.code_dir.validate()
        if self.compute_resource:
            self.compute_resource.validate()
        if self.experiment_config:
            self.experiment_config.validate()
        if self.hyper_parameters:
            for v1 in self.hyper_parameters:
                 if v1:
                    v1.validate()
        if self.input_channels:
            for v1 in self.input_channels:
                 if v1:
                    v1.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.output_channels:
            for v1 in self.output_channels:
                 if v1:
                    v1.validate()
        if self.scheduler:
            self.scheduler.validate()
        if self.settings:
            self.settings.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm_name is not None:
            result['AlgorithmName'] = self.algorithm_name

        if self.algorithm_provider is not None:
            result['AlgorithmProvider'] = self.algorithm_provider

        if self.algorithm_spec is not None:
            result['AlgorithmSpec'] = self.algorithm_spec.to_map()

        if self.algorithm_version is not None:
            result['AlgorithmVersion'] = self.algorithm_version

        if self.assign_node_spec is not None:
            result['AssignNodeSpec'] = self.assign_node_spec.to_map()

        if self.code_dir is not None:
            result['CodeDir'] = self.code_dir.to_map()

        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource.to_map()

        if self.environments is not None:
            result['Environments'] = self.environments

        if self.experiment_config is not None:
            result['ExperimentConfig'] = self.experiment_config.to_map()

        result['HyperParameters'] = []
        if self.hyper_parameters is not None:
            for k1 in self.hyper_parameters:
                result['HyperParameters'].append(k1.to_map() if k1 else None)

        result['InputChannels'] = []
        if self.input_channels is not None:
            for k1 in self.input_channels:
                result['InputChannels'].append(k1.to_map() if k1 else None)

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        result['OutputChannels'] = []
        if self.output_channels is not None:
            for k1 in self.output_channels:
                result['OutputChannels'].append(k1.to_map() if k1 else None)

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.python_requirements is not None:
            result['PythonRequirements'] = self.python_requirements

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler.to_map()

        if self.settings is not None:
            result['Settings'] = self.settings.to_map()

        if self.training_job_description is not None:
            result['TrainingJobDescription'] = self.training_job_description

        if self.training_job_name is not None:
            result['TrainingJobName'] = self.training_job_name

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlgorithmName') is not None:
            self.algorithm_name = m.get('AlgorithmName')

        if m.get('AlgorithmProvider') is not None:
            self.algorithm_provider = m.get('AlgorithmProvider')

        if m.get('AlgorithmSpec') is not None:
            temp_model = main_models.AlgorithmSpec()
            self.algorithm_spec = temp_model.from_map(m.get('AlgorithmSpec'))

        if m.get('AlgorithmVersion') is not None:
            self.algorithm_version = m.get('AlgorithmVersion')

        if m.get('AssignNodeSpec') is not None:
            temp_model = main_models.AssignNodeSpec()
            self.assign_node_spec = temp_model.from_map(m.get('AssignNodeSpec'))

        if m.get('CodeDir') is not None:
            temp_model = main_models.Location()
            self.code_dir = temp_model.from_map(m.get('CodeDir'))

        if m.get('ComputeResource') is not None:
            temp_model = main_models.CreateTrainingJobRequestComputeResource()
            self.compute_resource = temp_model.from_map(m.get('ComputeResource'))

        if m.get('Environments') is not None:
            self.environments = m.get('Environments')

        if m.get('ExperimentConfig') is not None:
            temp_model = main_models.CreateTrainingJobRequestExperimentConfig()
            self.experiment_config = temp_model.from_map(m.get('ExperimentConfig'))

        self.hyper_parameters = []
        if m.get('HyperParameters') is not None:
            for k1 in m.get('HyperParameters'):
                temp_model = main_models.CreateTrainingJobRequestHyperParameters()
                self.hyper_parameters.append(temp_model.from_map(k1))

        self.input_channels = []
        if m.get('InputChannels') is not None:
            for k1 in m.get('InputChannels'):
                temp_model = main_models.CreateTrainingJobRequestInputChannels()
                self.input_channels.append(temp_model.from_map(k1))

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.CreateTrainingJobRequestLabels()
                self.labels.append(temp_model.from_map(k1))

        self.output_channels = []
        if m.get('OutputChannels') is not None:
            for k1 in m.get('OutputChannels'):
                temp_model = main_models.CreateTrainingJobRequestOutputChannels()
                self.output_channels.append(temp_model.from_map(k1))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('PythonRequirements') is not None:
            self.python_requirements = m.get('PythonRequirements')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('Scheduler') is not None:
            temp_model = main_models.CreateTrainingJobRequestScheduler()
            self.scheduler = temp_model.from_map(m.get('Scheduler'))

        if m.get('Settings') is not None:
            temp_model = main_models.JobSettings()
            self.settings = temp_model.from_map(m.get('Settings'))

        if m.get('TrainingJobDescription') is not None:
            self.training_job_description = m.get('TrainingJobDescription')

        if m.get('TrainingJobName') is not None:
            self.training_job_name = m.get('TrainingJobName')

        if m.get('UserVpc') is not None:
            temp_model = main_models.CreateTrainingJobRequestUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateTrainingJobRequestUserVpc(DaraModel):
    def __init__(
        self,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        security_group_id: str = None,
        switch_id: str = None,
        vpc_id: str = None,
    ):
        self.default_route = default_route
        self.extended_cidrs = extended_cidrs
        self.security_group_id = security_group_id
        self.switch_id = switch_id
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route

        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')

        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateTrainingJobRequestScheduler(DaraModel):
    def __init__(
        self,
        max_running_time_in_minutes: int = None,
        max_running_time_in_seconds: int = None,
    ):
        self.max_running_time_in_minutes = max_running_time_in_minutes
        self.max_running_time_in_seconds = max_running_time_in_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_running_time_in_minutes is not None:
            result['MaxRunningTimeInMinutes'] = self.max_running_time_in_minutes

        if self.max_running_time_in_seconds is not None:
            result['MaxRunningTimeInSeconds'] = self.max_running_time_in_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxRunningTimeInMinutes') is not None:
            self.max_running_time_in_minutes = m.get('MaxRunningTimeInMinutes')

        if m.get('MaxRunningTimeInSeconds') is not None:
            self.max_running_time_in_seconds = m.get('MaxRunningTimeInSeconds')

        return self

class CreateTrainingJobRequestOutputChannels(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        name: str = None,
        output_uri: str = None,
        version_name: str = None,
    ):
        self.dataset_id = dataset_id
        self.name = name
        self.output_uri = output_uri
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.name is not None:
            result['Name'] = self.name

        if self.output_uri is not None:
            result['OutputUri'] = self.output_uri

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputUri') is not None:
            self.output_uri = m.get('OutputUri')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class CreateTrainingJobRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateTrainingJobRequestInputChannels(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        input_uri: str = None,
        name: str = None,
        options: str = None,
        version_name: str = None,
    ):
        self.dataset_id = dataset_id
        self.input_uri = input_uri
        self.name = name
        self.options = options
        self.version_name = version_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.input_uri is not None:
            result['InputUri'] = self.input_uri

        if self.name is not None:
            result['Name'] = self.name

        if self.options is not None:
            result['Options'] = self.options

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('InputUri') is not None:
            self.input_uri = m.get('InputUri')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        return self

class CreateTrainingJobRequestHyperParameters(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateTrainingJobRequestExperimentConfig(DaraModel):
    def __init__(
        self,
        experiment_id: str = None,
    ):
        self.experiment_id = experiment_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.experiment_id is not None:
            result['ExperimentId'] = self.experiment_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExperimentId') is not None:
            self.experiment_id = m.get('ExperimentId')

        return self

class CreateTrainingJobRequestComputeResource(DaraModel):
    def __init__(
        self,
        ecs_count: int = None,
        ecs_spec: str = None,
        instance_count: int = None,
        instance_spec: main_models.CreateTrainingJobRequestComputeResourceInstanceSpec = None,
        resource_id: str = None,
        spot_spec: main_models.CreateTrainingJobRequestComputeResourceSpotSpec = None,
        use_spot_instance: bool = None,
    ):
        self.ecs_count = ecs_count
        self.ecs_spec = ecs_spec
        self.instance_count = instance_count
        self.instance_spec = instance_spec
        self.resource_id = resource_id
        self.spot_spec = spot_spec
        self.use_spot_instance = use_spot_instance

    def validate(self):
        if self.instance_spec:
            self.instance_spec.validate()
        if self.spot_spec:
            self.spot_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_count is not None:
            result['EcsCount'] = self.ecs_count

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_spec is not None:
            result['InstanceSpec'] = self.instance_spec.to_map()

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.spot_spec is not None:
            result['SpotSpec'] = self.spot_spec.to_map()

        if self.use_spot_instance is not None:
            result['UseSpotInstance'] = self.use_spot_instance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EcsCount') is not None:
            self.ecs_count = m.get('EcsCount')

        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceSpec') is not None:
            temp_model = main_models.CreateTrainingJobRequestComputeResourceInstanceSpec()
            self.instance_spec = temp_model.from_map(m.get('InstanceSpec'))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('SpotSpec') is not None:
            temp_model = main_models.CreateTrainingJobRequestComputeResourceSpotSpec()
            self.spot_spec = temp_model.from_map(m.get('SpotSpec'))

        if m.get('UseSpotInstance') is not None:
            self.use_spot_instance = m.get('UseSpotInstance')

        return self

class CreateTrainingJobRequestComputeResourceSpotSpec(DaraModel):
    def __init__(
        self,
        spot_discount_limit: float = None,
        spot_strategy: str = None,
    ):
        self.spot_discount_limit = spot_discount_limit
        self.spot_strategy = spot_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.spot_discount_limit is not None:
            result['SpotDiscountLimit'] = self.spot_discount_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpotDiscountLimit') is not None:
            self.spot_discount_limit = m.get('SpotDiscountLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        return self

class CreateTrainingJobRequestComputeResourceInstanceSpec(DaraModel):
    def __init__(
        self,
        cpu: str = None,
        gpu: str = None,
        gputype: str = None,
        memory: str = None,
        shared_memory: str = None,
    ):
        self.cpu = cpu
        self.gpu = gpu
        self.gputype = gputype
        self.memory = memory
        self.shared_memory = shared_memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')

        return self

