# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitContainerConfig(DaraModel):
    def __init__(
        self,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: str = None,
        empty_dir_desc: str = None,
        envs: str = None,
        image_url: str = None,
        name: str = None,
    ):
        self.command = command
        self.command_args = command_args
        self.config_map_mount_desc = config_map_mount_desc
        self.empty_dir_desc = empty_dir_desc
        self.envs = envs
        self.image_url = image_url
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc

        if self.empty_dir_desc is not None:
            result['EmptyDirDesc'] = self.empty_dir_desc

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')

        if m.get('EmptyDirDesc') is not None:
            self.empty_dir_desc = m.get('EmptyDirDesc')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

