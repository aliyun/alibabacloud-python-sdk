# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class PublicTemplateSandboxConfig(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        generation: int = None,
        image: str = None,
        os_type: str = None,
        ready_command: str = None,
        registry_config: main_models.PublicTemplateRegistryConfig = None,
        start_command: str = None,
    ):
        # The ACR Enterprise instance ID.
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
        # The sandbox startup command.
        self.start_command = start_command

    def validate(self):
        if self.registry_config:
            self.registry_config.validate()

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

        if self.start_command is not None:
            result['startCommand'] = self.start_command

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
            temp_model = main_models.PublicTemplateRegistryConfig()
            self.registry_config = temp_model.from_map(m.get('registryConfig'))

        if m.get('startCommand') is not None:
            self.start_command = m.get('startCommand')

        return self

