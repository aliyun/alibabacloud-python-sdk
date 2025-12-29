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
        memory: int = None,
        name: str = None,
    ):
        self.acr_instance_id = acr_instance_id
        self.command = command
        self.command_args = command_args
        self.config_map_mount_desc = config_map_mount_desc
        self.cpu = cpu
        self.empty_dir_desc = empty_dir_desc
        self.envs = envs
        self.image_url = image_url
        self.memory = memory
        self.name = name

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

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

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

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

