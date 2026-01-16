# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class CustomContainerConfig(DaraModel):
    def __init__(
        self,
        acceleration_info: main_models.AccelerationInfo = None,
        acceleration_type: str = None,
        acr_instance_id: str = None,
        command: List[str] = None,
        entrypoint: List[str] = None,
        health_check_config: main_models.CustomHealthCheckConfig = None,
        image: str = None,
        port: int = None,
        registry_config: main_models.RegistryConfig = None,
        resolved_image_uri: str = None,
    ):
        self.acceleration_info = acceleration_info
        self.acceleration_type = acceleration_type
        self.acr_instance_id = acr_instance_id
        self.command = command
        self.entrypoint = entrypoint
        self.health_check_config = health_check_config
        self.image = image
        self.port = port
        self.registry_config = registry_config
        self.resolved_image_uri = resolved_image_uri

    def validate(self):
        if self.acceleration_info:
            self.acceleration_info.validate()
        if self.health_check_config:
            self.health_check_config.validate()
        if self.registry_config:
            self.registry_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceleration_info is not None:
            result['accelerationInfo'] = self.acceleration_info.to_map()

        if self.acceleration_type is not None:
            result['accelerationType'] = self.acceleration_type

        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.command is not None:
            result['command'] = self.command

        if self.entrypoint is not None:
            result['entrypoint'] = self.entrypoint

        if self.health_check_config is not None:
            result['healthCheckConfig'] = self.health_check_config.to_map()

        if self.image is not None:
            result['image'] = self.image

        if self.port is not None:
            result['port'] = self.port

        if self.registry_config is not None:
            result['registryConfig'] = self.registry_config.to_map()

        if self.resolved_image_uri is not None:
            result['resolvedImageUri'] = self.resolved_image_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accelerationInfo') is not None:
            temp_model = main_models.AccelerationInfo()
            self.acceleration_info = temp_model.from_map(m.get('accelerationInfo'))

        if m.get('accelerationType') is not None:
            self.acceleration_type = m.get('accelerationType')

        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('entrypoint') is not None:
            self.entrypoint = m.get('entrypoint')

        if m.get('healthCheckConfig') is not None:
            temp_model = main_models.CustomHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('healthCheckConfig'))

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('port') is not None:
            self.port = m.get('port')

        if m.get('registryConfig') is not None:
            temp_model = main_models.RegistryConfig()
            self.registry_config = temp_model.from_map(m.get('registryConfig'))

        if m.get('resolvedImageUri') is not None:
            self.resolved_image_uri = m.get('resolvedImageUri')

        return self

