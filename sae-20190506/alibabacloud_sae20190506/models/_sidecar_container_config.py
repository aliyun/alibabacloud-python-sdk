# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SidecarContainerConfig(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: str = None,
        cpu: int = None,
        empty_dir_desc: str = None,
        envs: str = None,
        image_url: str = None,
        liveness: str = None,
        memory: int = None,
        name: str = None,
        post_start: str = None,
        pre_stop: str = None,
        readiness: str = None,
        secret_mount_desc: str = None,
    ):
        # The instance ID of the ACR Enterprise Edition. This parameter is required if the `ImageUrl` is from an ACR Enterprise Edition repository.
        self.acr_instance_id = acr_instance_id
        # The startup command for the image. This command overrides the `ENTRYPOINT` defined in the image.
        self.command = command
        # The arguments for the startup command. This parameter corresponds to `CMD` in the Dockerfile.
        self.command_args = command_args
        # The settings for mounting a ConfigMap. Use this to inject configuration data into the container as files.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU resources allocated to the container, measured in millicores. For example, a value of 1000 represents 1 vCPU.
        self.cpu = cpu
        # The configuration for an `emptyDir` volume. This creates a temporary directory that persists for the life of the application instance.
        self.empty_dir_desc = empty_dir_desc
        # The environment variables to set in the container. Specify the variables as a JSON array of key-value pairs.
        self.envs = envs
        # The container image URL.
        self.image_url = image_url
        # The configuration for the liveness probe. The liveness probe checks if the container is running. If the probe fails, the system restarts the container.
        self.liveness = liveness
        # The amount of memory allocated to the container, measured in MB.
        self.memory = memory
        # The name of the container.
        self.name = name
        # The configuration for the postStart hook. This hook runs immediately after the container starts to perform initialization tasks.
        self.post_start = post_start
        # The configuration for the preStop hook. This hook runs immediately before the container is terminated to ensure a graceful shutdown.
        self.pre_stop = pre_stop
        # The configuration for the readiness probe. The readiness probe checks if the container is ready to handle requests. The system will not direct traffic to a container until its readiness probe succeeds.
        self.readiness = readiness
        # Specifies how to mount a Secret. This lets you securely use sensitive data, such as credentials or keys, in your application.
        self.secret_mount_desc = secret_mount_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id

        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.empty_dir_desc is not None:
            result['EmptyDirDesc'] = self.empty_dir_desc

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        if self.secret_mount_desc is not None:
            result['SecretMountDesc'] = self.secret_mount_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('EmptyDirDesc') is not None:
            self.empty_dir_desc = m.get('EmptyDirDesc')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        if m.get('SecretMountDesc') is not None:
            self.secret_mount_desc = m.get('SecretMountDesc')

        return self

