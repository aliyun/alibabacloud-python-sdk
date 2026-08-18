# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class MicroSandboxConfig(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        image: str = None,
        os_type: str = None,
        ready_command: str = None,
        registry_config: main_models.RegistryConfig = None,
        start_command: str = None,
    ):
        # The ID of the ACR Enterprise Edition image repository instance. Used in pair with MicroSandbox images. This parameter is optional. If not provided, the server resolves it as needed.
        self.acr_instance_id = acr_instance_id
        # The image address.
        self.image = image
        self.os_type = os_type
        self.ready_command = ready_command
        # The image repository configuration.
        self.registry_config = registry_config
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

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('osType') is not None:
            self.os_type = m.get('osType')

        if m.get('readyCommand') is not None:
            self.ready_command = m.get('readyCommand')

        if m.get('registryConfig') is not None:
            temp_model = main_models.RegistryConfig()
            self.registry_config = temp_model.from_map(m.get('registryConfig'))

        if m.get('startCommand') is not None:
            self.start_command = m.get('startCommand')

        return self

