# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ContainerConfiguration(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        command: List[str] = None,
        image: str = None,
        image_registry_type: str = None,
    ):
        # 阿里云容器镜像服务（ACR）的实例ID或名称
        self.acr_instance_id = acr_instance_id
        # 在容器中运行的命令（例如：[\"python3\", \"app.py\"]）
        self.command = command
        self.image = image
        # 容器镜像的来源类型，支持ACR（阿里云容器镜像服务）、ACREE（阿里云容器镜像服务企业版）、CUSTOM（自定义镜像仓库）
        self.image_registry_type = image_registry_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.command is not None:
            result['command'] = self.command

        if self.image is not None:
            result['image'] = self.image

        if self.image_registry_type is not None:
            result['imageRegistryType'] = self.image_registry_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('imageRegistryType') is not None:
            self.image_registry_type = m.get('imageRegistryType')

        return self

