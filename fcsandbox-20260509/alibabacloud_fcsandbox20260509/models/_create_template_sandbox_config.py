# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class CreateTemplateSandboxConfig(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        generation: int = None,
        image: str = None,
        os_type: str = None,
        ready_command: str = None,
        registry_config: main_models.CreateTemplateRegistryConfig = None,
        registry_type: str = None,
        start_command: str = None,
        steps: List[main_models.CreateTemplateStep] = None,
    ):
        # The Container Registry Enterprise instance ID.
        self.acr_instance_id = acr_instance_id
        # The sandbox generation. A value of 1 indicates the first-generation sandbox. A value of 2 indicates the second-generation sandbox.
        self.generation = generation
        # The image address.
        self.image = image
        # The operating system type.
        self.os_type = os_type
        # The sandbox readiness probe command.
        self.ready_command = ready_command
        # The image repository configuration.
        self.registry_config = registry_config
        # The image repository type.
        self.registry_type = registry_type
        # The sandbox startup command.
        self.start_command = start_command
        # The list of custom build steps.
        self.steps = steps

    def validate(self):
        if self.registry_config:
            self.registry_config.validate()
        if self.steps:
            for v1 in self.steps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.generation is not None:
            result['generation'] = self.generation

        if self.image is not None:
            result['image'] = self.image

        if self.os_type is not None:
            result['osType'] = self.os_type

        if self.ready_command is not None:
            result['readyCommand'] = self.ready_command

        if self.registry_config is not None:
            result['registryConfig'] = self.registry_config.to_map()

        if self.registry_type is not None:
            result['registryType'] = self.registry_type

        if self.start_command is not None:
            result['startCommand'] = self.start_command

        result['steps'] = []
        if self.steps is not None:
            for k1 in self.steps:
                result['steps'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('generation') is not None:
            self.generation = m.get('generation')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('osType') is not None:
            self.os_type = m.get('osType')

        if m.get('readyCommand') is not None:
            self.ready_command = m.get('readyCommand')

        if m.get('registryConfig') is not None:
            temp_model = main_models.CreateTemplateRegistryConfig()
            self.registry_config = temp_model.from_map(m.get('registryConfig'))

        if m.get('registryType') is not None:
            self.registry_type = m.get('registryType')

        if m.get('startCommand') is not None:
            self.start_command = m.get('startCommand')

        self.steps = []
        if m.get('steps') is not None:
            for k1 in m.get('steps'):
                temp_model = main_models.CreateTemplateStep()
                self.steps.append(temp_model.from_map(k1))

        return self

