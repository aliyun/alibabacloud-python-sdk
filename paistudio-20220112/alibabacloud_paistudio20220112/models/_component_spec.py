# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class ComponentSpec(DaraModel):
    def __init__(
        self,
        code_dir: main_models.Location = None,
        command: str = None,
        hyper_parameters: List[main_models.HyperParameterDefinition] = None,
        image: str = None,
        input_channels: List[main_models.Channel] = None,
        job_type: str = None,
        metric_definitions: List[main_models.MetricDefinition] = None,
        output_channels: List[main_models.Channel] = None,
        resource_requirements: List[main_models.ConditionExpression] = None,
    ):
        self.code_dir = code_dir
        # This parameter is required.
        self.command = command
        self.hyper_parameters = hyper_parameters
        # This parameter is required.
        self.image = image
        self.input_channels = input_channels
        # This parameter is required.
        self.job_type = job_type
        self.metric_definitions = metric_definitions
        self.output_channels = output_channels
        self.resource_requirements = resource_requirements

    def validate(self):
        if self.code_dir:
            self.code_dir.validate()
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

        result['ResourceRequirements'] = []
        if self.resource_requirements is not None:
            for k1 in self.resource_requirements:
                result['ResourceRequirements'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeDir') is not None:
            temp_model = main_models.Location()
            self.code_dir = temp_model.from_map(m.get('CodeDir'))

        if m.get('Command') is not None:
            self.command = m.get('Command')

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

        self.resource_requirements = []
        if m.get('ResourceRequirements') is not None:
            for k1 in m.get('ResourceRequirements'):
                temp_model = main_models.ConditionExpression()
                self.resource_requirements.append(temp_model.from_map(k1))

        return self

