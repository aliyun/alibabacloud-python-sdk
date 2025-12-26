# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class AlgorithmSpec(DaraModel):
    def __init__(
        self,
        code_dir: main_models.Location = None,
        command: List[str] = None,
        compute_resource: main_models.AlgorithmSpecComputeResource = None,
        customization: main_models.AlgorithmSpecCustomization = None,
        hyper_parameters: List[main_models.HyperParameterDefinition] = None,
        image: str = None,
        input_channels: List[main_models.Channel] = None,
        job_type: str = None,
        metric_definitions: List[main_models.MetricDefinition] = None,
        output_channels: List[main_models.Channel] = None,
        progress_definitions: main_models.AlgorithmSpecProgressDefinitions = None,
        resource_requirements: List[main_models.ConditionExpression] = None,
        supported_instance_types: List[str] = None,
        supports_distributed_training: bool = None,
    ):
        self.code_dir = code_dir
        # This parameter is required.
        self.command = command
        self.compute_resource = compute_resource
        self.customization = customization
        self.hyper_parameters = hyper_parameters
        # This parameter is required.
        self.image = image
        self.input_channels = input_channels
        # This parameter is required.
        self.job_type = job_type
        self.metric_definitions = metric_definitions
        self.output_channels = output_channels
        self.progress_definitions = progress_definitions
        self.resource_requirements = resource_requirements
        self.supported_instance_types = supported_instance_types
        self.supports_distributed_training = supports_distributed_training

    def validate(self):
        if self.code_dir:
            self.code_dir.validate()
        if self.compute_resource:
            self.compute_resource.validate()
        if self.customization:
            self.customization.validate()
        if self.hyper_parameters:
            for v1 in self.hyper_parameters:
                 if v1:
                    v1.validate()
        if self.input_channels:
            for v1 in self.input_channels:
                 if v1:
                    v1.validate()
        if self.metric_definitions:
            for v1 in self.metric_definitions:
                 if v1:
                    v1.validate()
        if self.output_channels:
            for v1 in self.output_channels:
                 if v1:
                    v1.validate()
        if self.progress_definitions:
            self.progress_definitions.validate()
        if self.resource_requirements:
            for v1 in self.resource_requirements:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_dir is not None:
            result['CodeDir'] = self.code_dir.to_map()

        if self.command is not None:
            result['Command'] = self.command

        if self.compute_resource is not None:
            result['ComputeResource'] = self.compute_resource.to_map()

        if self.customization is not None:
            result['Customization'] = self.customization.to_map()

        result['HyperParameters'] = []
        if self.hyper_parameters is not None:
            for k1 in self.hyper_parameters:
                result['HyperParameters'].append(k1.to_map() if k1 else None)

        if self.image is not None:
            result['Image'] = self.image

        result['InputChannels'] = []
        if self.input_channels is not None:
            for k1 in self.input_channels:
                result['InputChannels'].append(k1.to_map() if k1 else None)

        if self.job_type is not None:
            result['JobType'] = self.job_type

        result['MetricDefinitions'] = []
        if self.metric_definitions is not None:
            for k1 in self.metric_definitions:
                result['MetricDefinitions'].append(k1.to_map() if k1 else None)

        result['OutputChannels'] = []
        if self.output_channels is not None:
            for k1 in self.output_channels:
                result['OutputChannels'].append(k1.to_map() if k1 else None)

        if self.progress_definitions is not None:
            result['ProgressDefinitions'] = self.progress_definitions.to_map()

        result['ResourceRequirements'] = []
        if self.resource_requirements is not None:
            for k1 in self.resource_requirements:
                result['ResourceRequirements'].append(k1.to_map() if k1 else None)

        if self.supported_instance_types is not None:
            result['SupportedInstanceTypes'] = self.supported_instance_types

        if self.supports_distributed_training is not None:
            result['SupportsDistributedTraining'] = self.supports_distributed_training

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeDir') is not None:
            temp_model = main_models.Location()
            self.code_dir = temp_model.from_map(m.get('CodeDir'))

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('ComputeResource') is not None:
            temp_model = main_models.AlgorithmSpecComputeResource()
            self.compute_resource = temp_model.from_map(m.get('ComputeResource'))

        if m.get('Customization') is not None:
            temp_model = main_models.AlgorithmSpecCustomization()
            self.customization = temp_model.from_map(m.get('Customization'))

        self.hyper_parameters = []
        if m.get('HyperParameters') is not None:
            for k1 in m.get('HyperParameters'):
                temp_model = main_models.HyperParameterDefinition()
                self.hyper_parameters.append(temp_model.from_map(k1))

        if m.get('Image') is not None:
            self.image = m.get('Image')

        self.input_channels = []
        if m.get('InputChannels') is not None:
            for k1 in m.get('InputChannels'):
                temp_model = main_models.Channel()
                self.input_channels.append(temp_model.from_map(k1))

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        self.metric_definitions = []
        if m.get('MetricDefinitions') is not None:
            for k1 in m.get('MetricDefinitions'):
                temp_model = main_models.MetricDefinition()
                self.metric_definitions.append(temp_model.from_map(k1))

        self.output_channels = []
        if m.get('OutputChannels') is not None:
            for k1 in m.get('OutputChannels'):
                temp_model = main_models.Channel()
                self.output_channels.append(temp_model.from_map(k1))

        if m.get('ProgressDefinitions') is not None:
            temp_model = main_models.AlgorithmSpecProgressDefinitions()
            self.progress_definitions = temp_model.from_map(m.get('ProgressDefinitions'))

        self.resource_requirements = []
        if m.get('ResourceRequirements') is not None:
            for k1 in m.get('ResourceRequirements'):
                temp_model = main_models.ConditionExpression()
                self.resource_requirements.append(temp_model.from_map(k1))

        if m.get('SupportedInstanceTypes') is not None:
            self.supported_instance_types = m.get('SupportedInstanceTypes')

        if m.get('SupportsDistributedTraining') is not None:
            self.supports_distributed_training = m.get('SupportsDistributedTraining')

        return self

class AlgorithmSpecProgressDefinitions(DaraModel):
    def __init__(
        self,
        overall_progress: main_models.AlgorithmSpecProgressDefinitionsOverallProgress = None,
        remaining_time: main_models.AlgorithmSpecProgressDefinitionsRemainingTime = None,
    ):
        self.overall_progress = overall_progress
        self.remaining_time = remaining_time

    def validate(self):
        if self.overall_progress:
            self.overall_progress.validate()
        if self.remaining_time:
            self.remaining_time.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.overall_progress is not None:
            result['OverallProgress'] = self.overall_progress.to_map()

        if self.remaining_time is not None:
            result['RemainingTime'] = self.remaining_time.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OverallProgress') is not None:
            temp_model = main_models.AlgorithmSpecProgressDefinitionsOverallProgress()
            self.overall_progress = temp_model.from_map(m.get('OverallProgress'))

        if m.get('RemainingTime') is not None:
            temp_model = main_models.AlgorithmSpecProgressDefinitionsRemainingTime()
            self.remaining_time = temp_model.from_map(m.get('RemainingTime'))

        return self

class AlgorithmSpecProgressDefinitionsRemainingTime(DaraModel):
    def __init__(
        self,
        description: str = None,
        regex: str = None,
    ):
        self.description = description
        self.regex = regex

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.regex is not None:
            result['Regex'] = self.regex

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Regex') is not None:
            self.regex = m.get('Regex')

        return self

class AlgorithmSpecProgressDefinitionsOverallProgress(DaraModel):
    def __init__(
        self,
        description: str = None,
        regex: str = None,
    ):
        self.description = description
        self.regex = regex

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.regex is not None:
            result['Regex'] = self.regex

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Regex') is not None:
            self.regex = m.get('Regex')

        return self

class AlgorithmSpecCustomization(DaraModel):
    def __init__(
        self,
        code_dir: bool = None,
    ):
        self.code_dir = code_dir

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_dir is not None:
            result['CodeDir'] = self.code_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeDir') is not None:
            self.code_dir = m.get('CodeDir')

        return self

class AlgorithmSpecComputeResource(DaraModel):
    def __init__(
        self,
        policy: main_models.AlgorithmSpecComputeResourcePolicy = None,
    ):
        # This parameter is required.
        self.policy = policy

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = main_models.AlgorithmSpecComputeResourcePolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        return self



class AlgorithmSpecComputeResourcePolicy(DaraModel):
    def __init__(
        self,
        value: str = None,
        version: str = None,
    ):
        # This parameter is required.
        self.value = value
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.value is not None:
            result['Value'] = self.value

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

